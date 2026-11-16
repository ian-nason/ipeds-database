"""Create compatible Cost database from validated portable tables with DuckDB 1.5.5."""
import duckdb,json,hashlib
from pathlib import Path
p=Path(__file__).parent;target=p/'ipeds.cost2024.addition.duckdb155.candidate.duckdb'
assert duckdb.__version__=='1.5.5',duckdb.__version__
if target.exists():raise RuntimeError('Refusing to overwrite existing compatible candidate')
c=duckdb.connect(str(target));report=json.loads((p/'cost_addition_report.json').read_text());report['supersedes_unreadable_sidecar_sha256']=report.pop('candidate_sha256');report['supersedes_unreadable_sidecar_bytes']=report.pop('candidate_bytes');report['portable_sources']={}
for table in ['cost1','cost2','_metadata','_columns']:
 src=p/'cost_portable'/(table+'.parquet');c.execute(f'CREATE TABLE {table} AS SELECT * FROM read_parquet(?)',[str(src)])
 assert c.execute(f'select count(*) from ((select * from {table} except all select * from read_parquet(?)) union all (select * from read_parquet(?) except all select * from {table}))',[str(src),str(src)]).fetchone()[0]==0
 report['portable_sources'][table]={'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'rows':c.execute(f'select count(*) from {table}').fetchone()[0]}
c.execute('CHECKPOINT');c.close()
# A distinct closed-file reopen under the exact established client runtime is mandatory.
c=duckdb.connect(str(target),read_only=True)
assert c.execute('select count(*),count(distinct unitid),min(year),max(year) from cost1').fetchone()==(5867,5867,2024,2024)
assert c.execute('select count(*),count(distinct unitid),min(year),max(year) from cost2').fetchone()==(5406,5406,2024,2024)
assert c.execute('select sum(row_count) from _metadata').fetchone()[0]==11273;c.close()
report['candidate_sha256']=hashlib.sha256(target.read_bytes()).hexdigest();report['candidate_bytes']=target.stat().st_size;report['writer_version']='1.5.5';report['reopen_version']='1.5.5';report['compatibility_validation']='Created and independently reopened with DuckDB 1.5.5; full-row equality to portable export of raw-source-validated tables; exact row/key/metadata counts passed.'
(p/'cost_addition_compatible_report.json').write_text(json.dumps(report,indent=2));print('VALIDATED',target,report['candidate_sha256'],report['candidate_bytes'])
