"""Compare all remaining historical partitions and apply only proven revisions."""
from pathlib import Path
import duckdb,pandas as pd,numpy as np,zipfile,json,io,importlib.util,hashlib,shutil,time,warnings,sys
assert duckdb.__version__=='1.5.5' and pd.__version__=='3.1.1' and np.__version__=='2.5.4'
ROOT=Path(__file__).resolve().parent;release=ROOT
sys.path.insert(0,str(release));from revision_safe import select_member
from schema_review import raw_labels,review_gr_labels,review_empty_placeholders
spec=importlib.util.spec_from_file_location('ipeds_legacy',release/'build_database.upstream.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
warnings.simplefilter('ignore',pd.errors.PerformanceWarning)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
pin=json.loads((ROOT/'baseline.json').read_text());base=ROOT/'baseline.duckdb';assert sha(base)==pin['sha256']
target=ROOT/'ipeds.duckdb';assert not target.exists();assert shutil.disk_usage(ROOT).free>6*1024**3
shutil.copyfile(base,target);c=duckdb.connect(str(target),config={'threads':'1','memory_limit':'2GiB','max_temp_directory_size':'1GiB','preserve_insertion_order':'false'})
c.execute("SET checkpoint_threshold='1GiB'")
c.execute("ATTACH '"+str(base).replace("'","''")+"' AS baseline (READ_ONLY)")
schemas={t:c.execute(f'DESCRIBE {t}').fetchall() for t, in c.execute('SELECT table_name FROM _metadata').fetchall()};results=[];seen=set();changes={}
def compare(table,year,other):
 return [c.execute(f'SELECT count(*) FROM (SELECT * FROM {other} EXCEPT ALL SELECT * FROM baseline.{table} WHERE year={year})').fetchone()[0],c.execute(f'SELECT count(*) FROM (SELECT * FROM baseline.{table} WHERE year={year} EXCEPT ALL SELECT * FROM {other})').fetchone()[0]]
def load(z,member,table,year,name):
 raw=z.read(member)
 try:text=raw.decode('utf-8-sig')
 except UnicodeDecodeError:text=raw.decode('latin1')
 frame=b.HARMONIZERS[table](pd.read_csv(io.StringIO(text),low_memory=False),year)
 types={r[0]:r[1] for r in schemas[table]};extra=set(frame.columns)-set(types)
 if extra:
  review_empty_placeholders(table,year,frame,extra)
  # The four added NCES placeholder columns are empty in all 2,707 source rows.

 numeric=[(col,typ) for col,typ in types.items() if col in frame.columns and typ!='VARCHAR']
 # NCES uses a literal dot as a numeric missing marker; it is not a lost value.
 terms=','.join(f'''count(*) FILTER(WHERE "{col}" IS NOT NULL AND TRIM(CAST("{col}" AS VARCHAR)) NOT IN ('', '.') AND TRY_CAST("{col}" AS {typ}) IS NULL)''' for col,typ in numeric)
 losses=c.execute('SELECT '+terms+' FROM frame').fetchone() if terms else []
 projection=','.join(f'TRY_CAST("{col}" AS {typ}) AS "{col}"' if col in frame.columns else f'CAST(NULL AS {typ}) AS "{col}"' for col,typ in types.items())
 c.execute(f'CREATE OR REPLACE TEMP TABLE {name} AS SELECT {projection} FROM frame')
 return {'member':member,'sha256':hashlib.sha256(raw).hexdigest(),'rows':len(frame),'coercion_losses':{col:v for (col,_),v in zip(numeric,losses) if v},'empty_extra_fields':sorted(extra)}
assert len(json.loads((ROOT/'source-lock.json').read_text()))==436
while len(seen)<436:
 try:sources=json.loads((ROOT/'source-lock.json').read_text())
 except (json.JSONDecodeError,FileNotFoundError):time.sleep(2);continue
 pending=[r for r in sources if (r['table'],r['year']) not in seen]
 if not pending:time.sleep(2);continue
 for rec in pending:
  table,year=rec['table'],rec['year'];result={'table':table,'year':year,'stem':rec['stem']}
  try:
   assert rec['download_status']=='verified',rec.get('error');path=ROOT/'sources'/(rec['stem']+'.zip');assert sha(path)==rec['sha256']
   with zipfile.ZipFile(path) as z:
    member=select_member(z.namelist(),rec['stem']);current=load(z,member,table,year,'incoming');result['selected_source']=current;result['diff']=compare(table,year,'incoming')
    if result['diff']==[0,0]:result['status']='already_current'
    else:
     assert '_rv' in member.lower(),'Unrevised source differs from hosted partition'
     orig=[n for n in z.namelist() if Path(n).name.lower()==rec['stem'].lower()+'.csv'];assert len(orig)==1,'No unique provisional member'
     original=load(z,orig[0],table,year,'original');result['original_source']=original;result['original_diff']=compare(table,year,'original')
     assert result['original_diff']==[0,0],'Baseline differs from both publisher versions'
     if current['coercion_losses']!=original['coercion_losses']:
      assert table=='gr' and set(current['coercion_losses'])|set(original['coercion_losses'])=={'line'},'Changed coercion loss requires review'
      result['reviewed_schema_limits']=review_gr_labels(table,raw_labels(z.read(orig[0]),'line'),raw_labels(z.read(member),'line'))
     c.execute('BEGIN')
     try:
      c.execute(f'DELETE FROM {table} WHERE year={year}');c.execute(f'INSERT INTO {table} SELECT * FROM incoming')
      assert c.execute(f'SELECT count(*) FROM ((SELECT * FROM {table} WHERE year={year} EXCEPT ALL SELECT * FROM incoming) UNION ALL (SELECT * FROM incoming EXCEPT ALL SELECT * FROM {table} WHERE year={year}))').fetchone()[0]==0
      c.execute('COMMIT')
     except: c.execute('ROLLBACK');raise
     result['status']='corrected';changes.setdefault(table,[]).append(year)
  except Exception as e:
   if 'FATAL' in str(e) or 'invalidated' in str(e) or 'Out of Memory' in str(e):raise
   result.update(status='blocked',error=str(e))
  c.execute('DROP TABLE IF EXISTS incoming');c.execute('DROP TABLE IF EXISTS original')
  results.append(result);seen.add((table,year))
  (ROOT/'progress.json').write_text(json.dumps({'processed':len(seen),'changes':changes,'results':results},indent=2))
  if len(seen)%20==0 or result['status']=='blocked':print(len(seen),'corrected',sum(map(len,changes.values())),'blocked',sum(x['status']=='blocked' for x in results),table,year,result['status'],result.get('error',''),flush=True)
for table,cols in schemas.items():
 assert c.execute(f'DESCRIBE {table}').fetchall()==cols
 where=' WHERE year NOT IN ('+','.join(map(str,changes[table]))+')' if table in changes else ''
 keys=','.join('"'+x[0]+'"' for x in cols);sql=f'SELECT count(*),sum(hash({keys})::HUGEINT) FROM '
 assert c.execute(sql+table+where).fetchone()==c.execute(sql+'baseline.'+table+where).fetchone(),'Unchanged content differs: '+table
 count=c.execute(f'SELECT count(*) FROM {table}').fetchone()[0];c.execute('UPDATE _metadata SET row_count=? WHERE table_name=?',[count,table])
 if table in changes:
  terms=','.join(f'round(100.0*count(*) FILTER(WHERE "{x[0]}" IS NULL)/count(*),1)' for x in cols);nulls=c.execute('SELECT '+terms+' FROM '+table).fetchone()
  c.executemany('UPDATE _columns SET null_pct=? WHERE table_name=? AND column_name=?',[(v,table,col[0]) for col,v in zip(cols,nulls)])
 print('verified retained data',table,flush=True)
counts=c.execute('SELECT table_name,row_count FROM _metadata ORDER BY table_name').fetchall();c.execute('CHECKPOINT');c.close()
report={'checked_partitions':436,'prior_checked_partitions':60,'changes':changes,'results':results,'blocked_count':sum(r['status']=='blocked' for r in results),'tables':counts,'rows':sum(r[1] for r in counts),'artifact':{'bytes':target.stat().st_size,'sha256':sha(target)},'baseline':pin,'validation':'All changed partitions equal selected source after established harmonization; unchanged rows and schemas retained; blocked partitions left unchanged.'}
(ROOT/'validation-intermediate.json').write_text(json.dumps(report,indent=2));print('COMPLETE',report['rows'],'blocked',report['blocked_count'],flush=True)

assert {(r['table'],r['year']) for r in results if r['status']=='blocked'}=={('ic_py',2011)}, 'Unreviewed blocked partitions'
print('Run repair_flag_types.py to preserve the revised status codes and finish validation.',flush=True)
