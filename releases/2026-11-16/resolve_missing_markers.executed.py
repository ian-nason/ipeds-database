"""Apply reviewed NCES missing markers and unchanged legacy GR label classes."""
from pathlib import Path
import duckdb,pandas as pd,numpy as np,zipfile,json,io,hashlib,importlib.util,warnings
ROOT=Path(__file__).resolve().parent;release=ROOT.parent/'ipeds-source/releases/2026-11-09'
assert duckdb.__version__=='1.5.5' and pd.__version__=='3.1.1' and np.__version__=='2.5.4'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
report=json.loads((ROOT/'validation-v2.json').read_text());target=ROOT/'ipeds.history.v2.duckdb';assert sha(target)==report['artifact']['sha256']
blocked=[r for r in report['results'] if r['status']=='blocked' and not (r['table']=='ic_py' and r['year']==2011)];assert blocked,'No reviewed repair is needed'
assert all(r['error']=='Changed coercion loss requires review' for r in blocked),'Other blocked cases require independent review'
spec=importlib.util.spec_from_file_location('ipeds_legacy',release/'build_database.upstream.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
warnings.simplefilter('ignore',pd.errors.PerformanceWarning)
sources={(r['table'],r['year']):r for r in json.loads((ROOT/'source-lock.json').read_text())}
c=duckdb.connect(str(target),config={'threads':'1','memory_limit':'2GiB','max_temp_directory_size':'1GiB','preserve_insertion_order':'false'})
c.execute("SET checkpoint_threshold='1GiB'");c.execute(f"ATTACH '{ROOT}/baseline.duckdb' AS baseline (READ_ONLY)")
reviews=[];touched=set()
for rec in blocked:
 table,year=rec['table'],rec['year'];source=sources[table,year];path=ROOT/'sources'/(rec['stem']+'.zip');assert sha(path)==source['sha256']
 types={r[0]:r[1] for r in c.execute(f'DESCRIBE {table}').fetchall()};loss_cols=set(rec['selected_source']['coercion_losses'])|set(rec['original_source']['coercion_losses']);proof={}
 with zipfile.ZipFile(path) as z:
  for kind,name in [('selected_source','incoming'),('original_source','original')]:
   raw=z.read(rec[kind]['member']);assert hashlib.sha256(raw).hexdigest()==rec[kind]['sha256']
   try:text=raw.decode('utf-8-sig')
   except UnicodeDecodeError:text=raw.decode('latin1')
   rawframe=pd.read_csv(io.StringIO(text),dtype=str,keep_default_na=False);rawframe.columns=[x.strip().lower() for x in rawframe.columns]
   values={col:rawframe.loc[pd.to_numeric(rawframe[col],errors='coerce').isna() & rawframe[col].ne(''),col].value_counts().to_dict() for col in loss_cols}
   for col,counts in values.items():
    allowed={'29A','12A','18A','11A'} if table=='gr' and col=='line' else {'.'}
    assert {value.strip() for value in counts} <= allowed,'Unreviewed nonnumeric values'
   proof[kind]=values
   frame=b.HARMONIZERS[table](pd.read_csv(io.StringIO(text),low_memory=False),year)
   assert not set(frame.columns)-set(types)
   projection=','.join(f'TRY_CAST("{col}" AS {typ}) AS "{col}"' if col in frame.columns else f'CAST(NULL AS {typ}) AS "{col}"' for col,typ in types.items())
   c.execute(f'CREATE OR REPLACE TEMP TABLE {name} AS SELECT {projection} FROM frame')
  if table=='gr' and 'line' in loss_cols:
   assert set(proof['selected_source']['line'])==set(proof['original_source']['line'])=={'29A','12A','18A','11A'},'Unsupported GR label classes changed'
  assert c.execute(f'SELECT count(*) FROM ((SELECT * FROM original EXCEPT ALL SELECT * FROM baseline.{table} WHERE year={year}) UNION ALL (SELECT * FROM baseline.{table} WHERE year={year} EXCEPT ALL SELECT * FROM original))').fetchone()[0]==0
  c.execute('BEGIN')
  try:
   c.execute(f'DELETE FROM {table} WHERE year={year}');c.execute(f'INSERT INTO {table} SELECT * FROM incoming')
   assert c.execute(f'SELECT count(*) FROM ((SELECT * FROM {table} WHERE year={year} EXCEPT ALL SELECT * FROM incoming) UNION ALL (SELECT * FROM incoming EXCEPT ALL SELECT * FROM {table} WHERE year={year}))').fetchone()[0]==0
   c.execute('COMMIT')
  except:c.execute('ROLLBACK');raise
 c.execute('DROP TABLE incoming');c.execute('DROP TABLE original')
 disposition='The same four already unsupported GR line labels are present in both publisher versions; their counts changed. Existing numeric schema and NULL representation retained.' if table=='gr' else 'Only literal dot missing-marker counts changed; typed NULL representation is preserved.'
 reviews.append({'table':table,'year':year,'raw_nonnumeric_values':proof,'disposition':disposition});rec['status']='corrected';rec['reviewed_schema_limits']=proof;rec.pop('error',None);report['changes'].setdefault(table,[]).append(year);touched.add(table)
for table in touched:
 cols=c.execute(f'DESCRIBE {table}').fetchall();assert cols==c.execute(f'DESCRIBE baseline.{table}').fetchall()
 where=' WHERE year NOT IN ('+','.join(map(str,report['changes'][table]))+')';keys=','.join('"'+r[0]+'"' for r in cols);query=f'SELECT count(*),sum(hash({keys})::HUGEINT) FROM '
 assert c.execute(query+table+where).fetchone()==c.execute(query+'baseline.'+table+where).fetchone()
 count=c.execute('SELECT count(*) FROM '+table).fetchone()[0];c.execute('UPDATE _metadata SET row_count=? WHERE table_name=?',[count,table])
 terms=','.join(f'round(100.0*count(*) FILTER(WHERE "{r[0]}" IS NULL)/count(*),1)' for r in cols);nulls=c.execute('SELECT '+terms+' FROM '+table).fetchone();c.executemany('UPDATE _columns SET null_pct=? WHERE table_name=? AND column_name=?',[(v,table,col[0]) for col,v in zip(cols,nulls)])
report['tables']=c.execute('SELECT table_name,row_count FROM _metadata ORDER BY table_name').fetchall();report['rows']=sum(r[1] for r in report['tables']);c.execute('CHECKPOINT');c.close()
report['blocked_count']=sum(r['status']=='blocked' for r in report['results']);assert report['blocked_count']==1
report['schema_limit_reviews']=reviews;report['artifact']={'bytes':target.stat().st_size,'sha256':sha(target)}
report['validation']='All 436 historical partitions checked; dot missing markers and known GR label classes reviewed. IC2011_PY status-flag typing remains pending; this intermediate file is not for publication.'
(ROOT/'validation-before-flag-repair.json').write_text(json.dumps(report,indent=2));print('INTERMEDIATE',report['rows'],'changes',sum(map(len,report['changes'].values())),'blocked',report['blocked_count'],flush=True)
