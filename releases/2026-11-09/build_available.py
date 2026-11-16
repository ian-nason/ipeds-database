"""Consume independently fresh-scanned archives; correct only proven provisional partitions."""
import duckdb,pandas as pd,zipfile,json,io,importlib.util,hashlib,shutil,warnings,time,traceback
from pathlib import Path
from revision_safe import select_member
warnings.simplefilter('ignore',pd.errors.PerformanceWarning)
assert pd.__version__=='3.1.1', 'Use the pandas version pinned in requirements.replay.txt'
assert duckdb.__version__=='1.5.5', 'Use DuckDB 1.5.5 to preserve established client compatibility'
p=Path(__file__).parent
assert hashlib.sha256((p/'ipeds.original.duckdb').read_bytes()).hexdigest() == '8df0b1a06af63f5724a3e883930f39ac1a80ac871f5d852b9eee75433388f429', 'Baseline SHA-256 does not match the pinned release'
spec=importlib.util.spec_from_file_location('build',p/'build_database.upstream.py');build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)
base=p/'ipeds.original.duckdb';target=p/'ipeds.available-finals.candidate.duckdb'
if target.exists():raise RuntimeError('Candidate exists; refusing overwrite')
assert shutil.disk_usage(p).free>33_000_000_000
shutil.copy2(base,target);c=duckdb.connect(str(target));c.execute("SET memory_limit='2GB'");c.execute('SET threads=2');c.execute("ATTACH '"+str(base).replace("'","''")+"' AS baseline (READ_ONLY)")
results=[];seen=set();changes={};schemas={}
expected=len(json.loads((p/'history_scan.recovered.json').read_text()))
def compare(table,year,src):
 return [c.execute(f'select count(*) from (select * from {src} except all select * from baseline.{table} where year={year})').fetchone()[0],c.execute(f'select count(*) from (select * from baseline.{table} where year={year} except all select * from {src})').fetchone()[0]]
def load(z,member,table,year,target):
 raw=z.read(member)
 try:txt=raw.decode('utf-8-sig')
 except UnicodeDecodeError:txt=raw.decode('latin-1')
 df=build.HARMONIZERS[table](pd.read_csv(io.StringIO(txt),low_memory=False),year)
 cols=schemas.setdefault(table,c.execute(f'describe {table}').fetchall());types={x[0]:x[1] for x in cols}
 extra=set(df.columns)-set(types)
 if extra:raise ValueError(f'New columns require review: {extra}')
 projected=','.join(f'TRY_CAST("{col}" AS {typ}) AS "{col}"' if col in df.columns else f'CAST(NULL AS {typ}) AS "{col}"' for col,typ in types.items())
 # Save coercion losses. New losses in revised data block the partition, not silently disappear.
 numeric=[(col,typ) for col,typ in types.items() if col in df.columns and typ!='VARCHAR']
 loss_sql=','.join(f'count(*) filter(where "{col}" is not null and try_cast("{col}" as {typ}) is null)' for col,typ in numeric)
 loss_values=c.execute('select '+loss_sql+' from df').fetchone() if numeric else []
 losses=dict(zip([x[0] for x in numeric],loss_values))
 c.execute(f'create or replace temp table {target} as select {projected} from df')
 return {'member':member,'sha256':hashlib.sha256(raw).hexdigest(),'rows':len(df),'coercion_losses':{k:v for k,v in losses.items() if v}}
while len(seen)<expected:
 try:scan=json.loads((p/'history_scan.recovered.json').read_text())
 except (FileNotFoundError,json.JSONDecodeError):time.sleep(2);continue
 pending=[r for r in scan if (r['table'],r['year']) not in seen]
 if not pending:time.sleep(3);continue
 for rec in pending:
  table,year=rec['table'],rec['year'];key=(table,year);out={'table':table,'year':year,'stem':rec['stem']}
  try:
   if rec['status']!='ok':raise RuntimeError('Fresh-source scan failed: '+rec['error'])
   if not rec['has_revised']:out['status']='no_revised_member';results.append(out);seen.add(key);continue
   zp=p/'history_sources'/(rec['stem']+'.zip');assert hashlib.sha256(zp.read_bytes()).hexdigest()==rec['provenance']['archive_sha256']
   with zipfile.ZipFile(zp) as z:
    member=select_member(z.namelist(),rec['stem']);orig=[n for n in z.namelist() if Path(n).name.lower()==rec['stem'].lower()+'.csv']
    revised=load(z,member,table,year,'revised');out['revised']=revised;out['revision_diff']=compare(table,year,'revised')
    if out['revision_diff']==[0,0]:out['status']='already_final'
    else:
     if len(orig)!=1:raise ValueError('No unique provisional member to validate baseline')
     original=load(z,orig[0],table,year,'provisional');out['provisional']=original;out['provisional_diff']=compare(table,year,'provisional')
     if out['provisional_diff']!=[0,0]:raise ValueError('Provisional source does not exactly reproduce hosted partition')
     if revised['coercion_losses']!=original['coercion_losses']:
      if table=='gr' and year==2023:
       review=json.loads((p/'gr2023_disposition.json').read_text())
       assert revised['sha256']==review['revised']['sha256'] and original['sha256']==review['original']['sha256']
       out['known_preexisting_limitation']=review['disposition']
      else:raise ValueError('Revised data changes coercion loss; requires schema review')
     c.execute('BEGIN');c.execute(f'delete from {table} where year={year}');c.execute(f'insert into {table} select * from revised');c.execute('COMMIT')
     assert c.execute(f'select count(*) from ((select * from {table} where year={year} except all select * from revised) union all (select * from revised except all select * from {table} where year={year}))').fetchone()[0]==0
     out['status']='corrected';changes.setdefault(table,[]).append(year)
  except Exception as e:out['status']='blocked';out['error']=str(e)
  results.append(out);seen.add(key)
  (p/'available_build_progress.json').write_text(json.dumps({'expected':expected,'processed':len(seen),'changes':changes,'results':results},indent=2))
  if len(seen)%10==0 or out['status']=='blocked':print('PROCESSED',len(seen),'CHANGED',sum(len(v) for v in changes.values()),'BLOCKED',sum(r['status']=='blocked' for r in results),table,year,out['status'],out.get('error',''),flush=True)
# Exact unchanged rows check by per-table counts and order-independent row hashes.
for table, in c.execute('select table_name from _metadata order by 1').fetchall():
 cols=c.execute(f'describe {table}').fetchall();assert cols==c.execute(f'describe baseline.{table}').fetchall()
 where=' where year not in ('+','.join(map(str,changes[table]))+')' if table in changes else ''
 keys=','.join('"'+x[0]+'"' for x in cols);sql=f'select count(*),sum(hash({keys})::HUGEINT) from '
 assert c.execute(sql+table+where).fetchone()==c.execute(sql+'baseline.'+table+where).fetchone(),table
 n=c.execute(f'select count(*) from {table}').fetchone()[0];c.execute('update _metadata set row_count=? where table_name=?',[n,table])
 if table in changes:
  expr=','.join(f'round(100.0*sum(("{x[0]}" is null)::int)/count(*),1)' for x in cols);nulls=c.execute(f'select {expr} from {table}').fetchone()
  c.executemany('update _columns set null_pct=? where table_name=? and column_name=?',[(v,table,x[0]) for x,v in zip(cols,nulls)])
 print('VERIFIED',table,flush=True)
report={'scope':'This release checks 60 of the 496 table/year source partitions in the baseline and updates 30 partitions to final or revised data. The remaining 436 partitions and all other unchanged data are preserved. This is a limited revision update, not a complete historical refresh.','source_total_rows':c.execute('select sum(row_count) from _metadata').fetchone()[0],'changes':changes,'results':results,'blocked_count':sum(r['status']=='blocked' for r in results),'corrected_partition_count':sum(len(v) for v in changes.values()),'known_preexisting_limitations':['Source equality is after existing harmonization and projection, not raw CSV equality. HD close_date remains DOUBLE and loses date strings; HD is unchanged. GR line remains numeric and loses labels 29A / 12A / 18A / 11A; GR 2023 final revision changes counts but not the lost label categories.'], 'source_partitions_total':496,'source_partitions_verified':expected,'validation':'Every corrected partition exactly equals revised source under existing schema; all other source rows count/hash match original; schemas preserved; metadata counts and null percentages refreshed.'}
c.execute('CHECKPOINT');c.close();report['sha256']=hashlib.sha256(target.read_bytes()).hexdigest();report['bytes']=target.stat().st_size;(p/'available_candidate_report.json').write_text(json.dumps(report,indent=2));print('VALIDATED',report['source_total_rows'],report['blocked_count'],report['sha256'],flush=True)
