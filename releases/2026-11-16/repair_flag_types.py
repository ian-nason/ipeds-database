"""Preserve IC2011_PY letter status codes with an explicit VARCHAR type repair."""
from pathlib import Path
import argparse,json,hashlib,zipfile,io,importlib.util
import pandas as pd
import duckdb

def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def q(value):return '"'+value.replace('"','""')+'"'
def main():
 root=Path(__file__).resolve().parent
 ap=argparse.ArgumentParser();ap.add_argument('--database',type=Path,default=root/'ipeds.duckdb');ap.add_argument('--report',type=Path,default=root/'validation-intermediate.json');ap.add_argument('--output-report',type=Path,default=root/'validation.json');ap.add_argument('--harmonizer',type=Path,default=root/'build_database.upstream.py');args=ap.parse_args()
 assert duckdb.__version__=='1.5.5' and pd.__version__=='3.1.1'
 report=json.loads(args.report.read_text());assert sha(args.database)==report['artifact']['sha256']
 pending=[r for r in report['results'] if r['status']=='blocked'];assert len(pending)==1 and (pending[0]['table'],pending[0]['year'])==('ic_py',2011)
 rec=pending[0];pin=json.loads((root/'baseline.json').read_text());base=root/'baseline.duckdb';assert sha(base)==pin['sha256']
 src=next(r for r in json.loads((root/'source-lock.json').read_text()) if r['table']=='ic_py' and r['year']==2011);archive=root/'sources/IC2011_PY.zip';assert sha(archive)==src['sha256']
 spec=importlib.util.spec_from_file_location('legacy',args.harmonizer);b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
 c=duckdb.connect(str(args.database),config={'threads':'1','memory_limit':'2GiB','max_temp_directory_size':'1GiB','preserve_insertion_order':'false'});c.execute(f"ATTACH '{base}' AS baseline (READ_ONLY)")
 oldschema=c.execute('DESCRIBE ic_py').fetchall();types={r[0]:r[1] for r in oldschema};frames={};proof={};rawframes={}
 with zipfile.ZipFile(archive) as z:
  for member,name in [('ic2011_py.csv','original'),('ic2011_py_rv.csv','revised')]:
   raw=z.read(member);frame=b.HARMONIZERS['ic_py'](pd.read_csv(io.BytesIO(raw),low_memory=False),2011)
   rawframe=pd.read_csv(io.BytesIO(raw),dtype=str,keep_default_na=False);rawframe.columns=rawframe.columns.str.strip().str.lower();rawframes[name]=rawframe
   extra=set(frame.columns)-set(types)
   if name=='revised':assert extra=={'py0','py1','py2','py3'} and frame[list(extra)].isna().all().all()
   else:assert not extra
   frames[name]=frame;proof[name]={'member':member,'sha256':hashlib.sha256(raw).hexdigest(),'rows':len(frame),'empty_extra_fields':sorted(extra)}
 original=frames['original'];projection=','.join(f'TRY_CAST({q(col)} AS {typ}) AS {q(col)}' if col in original.columns else f'NULL::{typ} AS {q(col)}' for col,typ in types.items());c.execute(f'CREATE TEMP TABLE original AS SELECT {projection} FROM original')
 assert c.execute('SELECT count(*) FROM ((SELECT * FROM original EXCEPT ALL SELECT * FROM baseline.ic_py WHERE year=2011) UNION ALL (SELECT * FROM baseline.ic_py WHERE year=2011 EXCEPT ALL SELECT * FROM original))').fetchone()[0]==0
 revised=frames['revised'];flags=[];flag_values={}
 for col,typ in types.items():
  if typ=='VARCHAR' or col not in rawframes['revised'].columns:continue
  values=rawframes['revised'][col];bad=values.ne('') & values.ne('.') & pd.to_numeric(values,errors='coerce').isna()
  if bad.any():
   assert col.startswith('x') and typ=='DOUBLE' and set(values.unique()) <= {'R','A'},f'Unexpected type repair: {col}'
   flags.append(col);flag_values[col]=values.value_counts().to_dict();revised[col]=values
 assert len(flags)==25,'Status-flag repair scope changed'
 newtypes={col:('VARCHAR' if col in flags else typ) for col,typ in types.items()}
 # Other numeric fields must not acquire new coercion losses.
 numeric=[(col,typ) for col,typ in types.items() if col not in flags and typ!='VARCHAR' and col in revised.columns]
 terms=','.join(f'''count(*) FILTER(WHERE {q(col)} IS NOT NULL AND TRIM(CAST({q(col)} AS VARCHAR)) NOT IN ('', '.') AND TRY_CAST({q(col)} AS {typ}) IS NULL)''' for col,typ in numeric)
 assert not any(c.execute('SELECT '+terms+' FROM revised').fetchone()),'Substantive non-flag values would be lost'
 projection=','.join(f'TRY_CAST({q(col)} AS {typ}) AS {q(col)}' if col in revised.columns else f'NULL::{typ} AS {q(col)}' for col,typ in newtypes.items());c.execute(f'CREATE TEMP TABLE incoming AS SELECT {projection} FROM revised')
 c.execute('CREATE TEMP TABLE before_ic_py AS SELECT * FROM ic_py');c.execute('BEGIN')
 try:
  for col in flags:c.execute(f'ALTER TABLE ic_py ALTER COLUMN {q(col)} TYPE VARCHAR USING CAST({q(col)} AS VARCHAR)')
  c.execute('DELETE FROM ic_py WHERE year=2011');c.execute('INSERT INTO ic_py SELECT * FROM incoming')
  assert c.execute('SELECT count(*) FROM ((SELECT * FROM ic_py WHERE year=2011 EXCEPT ALL SELECT * FROM incoming) UNION ALL (SELECT * FROM incoming EXCEPT ALL SELECT * FROM ic_py WHERE year=2011))').fetchone()[0]==0
  old_projection=','.join(f'CAST({q(col)} AS {typ}) AS {q(col)}' for col,typ in types.items())
  assert c.execute(f'SELECT count(*) FROM ((SELECT {old_projection} FROM ic_py WHERE year<>2011 EXCEPT ALL SELECT * FROM before_ic_py WHERE year<>2011) UNION ALL (SELECT * FROM before_ic_py WHERE year<>2011 EXCEPT ALL SELECT {old_projection} FROM ic_py WHERE year<>2011))').fetchone()[0]==0
  for col in flags:
   assert c.execute(f'SELECT count(*) FROM ic_py WHERE year=2011 AND {q(col)} IS NULL').fetchone()[0]==0
   actual=dict(c.execute(f'SELECT {q(col)},count(*) FROM ic_py WHERE year=2011 GROUP BY 1').fetchall());assert actual==flag_values[col]
   c.execute('UPDATE _columns SET data_type=\'VARCHAR\',example_value=? WHERE table_name=\'ic_py\' AND column_name=?',[next(iter(flag_values[col])),col])
  cols=list(newtypes);terms=','.join(f'round(100.0*count(*) FILTER(WHERE {q(col)} IS NULL)/count(*),1)' for col in cols);nulls=c.execute('SELECT '+terms+' FROM ic_py').fetchone();c.executemany('UPDATE _columns SET null_pct=? WHERE table_name=\'ic_py\' AND column_name=?',list(zip(nulls,cols)))
  c.execute("UPDATE _metadata SET row_count=(SELECT count(*) FROM ic_py) WHERE table_name='ic_py'");c.execute('COMMIT')
 except:c.execute('ROLLBACK');raise
 new_schema=c.execute('DESCRIBE ic_py').fetchall();assert [(r[0],r[1]) for r in new_schema]==list(newtypes.items())
 report['schema_repairs']={'ic_py':{'columns':flags,'old_type':'DOUBLE','new_type':'VARCHAR','source_year':2011,'raw_code_counts':flag_values,'other_years':'Existing numeric values converted to text with CAST; casting back reproduces every pre-repair row outside 2011 exactly. Missing values remain NULL; codes are not normalized across years.','empty_source_columns':['py0','py1','py2','py3'],'empty_source_disposition':'All four additional source fields are empty in all 2,707 revised rows; no substantive value omitted.'}}
 rec.update(status='corrected',selected_source=proof['revised'],original_source=proof['original'],original_diff=[0,0],schema_repair=flags);rec.pop('error',None);report['changes'].setdefault('ic_py',[]).append(2011)
 report['blocked_count']=0;report['tables']=c.execute('SELECT table_name,row_count FROM _metadata ORDER BY table_name').fetchall();report['rows']=sum(r[1] for r in report['tables']);report['validation']='All 496 historical partitions and both Cost inputs checked. Additional revisions match selected sources under documented harmonization. Twenty-five IC_PY flag types corrected to text to preserve R/A codes; all other existing values and schemas retained with documented GR/HD limitations.'
 report['view_metadata_checked']=[]
 for view in ['v_admission_rates','v_tuition_trends','v_institutions']:
  names=[r[0] for r in c.execute('SELECT column_name FROM _columns WHERE table_name=?',[view]).fetchall()]
  terms=','.join(f'round(100.0*count(*) FILTER(WHERE {q(col)} IS NULL)/count(*),1)' for col in names);values=c.execute('SELECT '+terms+' FROM '+view).fetchone()
  c.executemany('UPDATE _columns SET null_pct=? WHERE table_name=? AND column_name=?',[(value,view,col) for col,value in zip(names,values)]);report['view_metadata_checked'].append(view)
 c.execute('CHECKPOINT');c.close();report['artifact']={'bytes':args.database.stat().st_size,'sha256':sha(args.database)};args.output_report.write_text(json.dumps(report,indent=2));print('FINAL',report['rows'],'revisions',sum(map(len,report['changes'].values())),'flag fields',len(flags),flush=True)

if __name__=='__main__':main()
