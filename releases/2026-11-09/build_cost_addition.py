"""Separate lossless source-field Cost extension; does not modify existing IPEDS artifacts."""
import csv,io,json,zipfile,hashlib,duckdb,pandas as pd
from pathlib import Path
assert pd.__version__=='3.1.1', 'Use the pandas version pinned in requirements.replay.txt'
assert duckdb.__version__=='1.5.5', 'Use DuckDB 1.5.5 to preserve established client compatibility'
p=Path(__file__).parent;target=p/'ipeds.cost2024.addition.candidate.duckdb'
if target.exists():raise RuntimeError('Do not overwrite an existing candidate')
c=duckdb.connect(str(target));c.execute('CREATE TABLE _metadata(table_name VARCHAR,row_count BIGINT,column_count BIGINT,min_year BIGINT,max_year BIGINT,source_url VARCHAR,license VARCHAR)');c.execute('CREATE TABLE _columns(table_name VARCHAR,column_name VARCHAR,data_type VARCHAR,source_file VARCHAR,example_value VARCHAR,join_hint VARCHAR,null_pct DOUBLE)')
info=json.loads((p/'cost_survey_inspection.json').read_text());report={'scope':'Separate new provisional 2024 Cost tables. No changes to existing IC/tuition tables or any revision candidate. All source fields preserved; no attempt to splice pre-2024 schemas.','typing':'unitid BIGINT after proving exact canonical decimal representation; year BIGINT=2024 is collection/file year, not the reporting period of every field. Every other original field VARCHAR to preserve codes, formatting, missing strings and values without numeric coercion. Empty source strings remain empty strings, not NULL. Original source names mapped case-insensitively to lowercase; no field renaming beyond case.','tables':{}}
for item in info:
 stem=item['stem'];table=stem.split('_')[0].lower();zp=p/(stem+'.zip');assert hashlib.sha256(zp.read_bytes()).hexdigest()==item['provenance']['archive_sha256']
 with zipfile.ZipFile(zp) as z:raw=z.read(item['provenance']['member'])
 text=raw.decode('utf-8-sig');reader=csv.reader(io.StringIO(text));headers=next(reader);names=[x.strip().lower() for x in headers];assert len(names)==len(set(names)) and 'year' not in names
 rows=list(reader);assert all(len(r)==len(names) for r in rows);df=pd.DataFrame(rows,columns=names)
 assert df.unitid.map(lambda x:str(int(x))==x).all();assert df.unitid.is_unique and df.unitid.ne('').all()
 projection=','.join('CAST(unitid AS BIGINT) AS unitid' if name=='unitid' else f'CAST("{name}" AS VARCHAR) AS "{name}"' for name in names)
 c.execute(f'create table {table} as select {projection},2024::BIGINT as year from df')
 # Independent raw string comparison, after restoring the sole lossless integer cast.
 rawcols=','.join(f'CAST("{name}" AS VARCHAR) AS "{name}"' for name in names)
 assert c.execute(f'select count(*) from ((select {rawcols} from {table} except all select * from df) union all (select * from df except all select {rawcols} from {table}))').fetchone()[0]==0
 assert c.execute(f'select count(*),count(distinct unitid),count(*) filter(where unitid is null),min(year),max(year) from {table}').fetchone()==(len(rows),len(rows),0,2024,2024)
 schema=c.execute(f'describe {table}').fetchall();c.execute('insert into _metadata values (?,?,?,?,?,?,?)',[table,len(rows),len(schema),2024,2024,item['provenance']['url'],'Public domain'])
 for name,typ,*_ in schema:
  val=c.execute(f'select "{name}"::VARCHAR from {table} where "{name}" is not null limit 1').fetchone();c.execute('insert into _columns values (?,?,?,?,?,?,?)',[table,name,typ,stem+'.csv',val[0] if val else None,'Primary institution ID, joins across IPEDS tables' if name=='unitid' else None,0.0])
 report['tables'][table]={'rows':len(rows),'columns_including_year':len(schema),'source':item['provenance'],'source_csv_sha256':hashlib.sha256(raw).hexdigest(),'original_fields':headers,'schema':{r[0]:r[1] for r in schema},'tests':'Exact raw string cell/full-row multiset equality after lossless UNITID cast; unique/non-null UNITID; identical row count; collection year=2024; all source columns retained.'}
 print(table,len(rows),len(schema),flush=True)
c.execute('CHECKPOINT');c.close();report['candidate_sha256']=hashlib.sha256(target.read_bytes()).hexdigest();report['candidate_bytes']=target.stat().st_size;report['added_source_rows']=sum(x['rows'] for x in report['tables'].values());(p/'cost_addition_report.json').write_text(json.dumps(report,indent=2));print('VALIDATED',target,report['candidate_sha256'],flush=True)
