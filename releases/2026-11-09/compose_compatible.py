"""Combine validated bounded revision and lossless Cost extension; no source downloads."""
from pathlib import Path
import json,hashlib,shutil,duckdb
assert duckdb.__version__=='1.5.5',duckdb.__version__
p=Path(__file__).parent;revisions=p/'ipeds.available-finals.candidate.duckdb';costs=p/'ipeds.cost2024.addition.duckdb155.candidate.duckdb';target=p/'ipeds.combined.duckdb155.candidate.duckdb'
if target.exists():raise RuntimeError('Preserve existing candidate; refusing overwrite')
rev=json.loads((p/'available_candidate_report.json').read_text());cost=json.loads((p/'cost_addition_compatible_report.json').read_text());assert hashlib.sha256(revisions.read_bytes()).hexdigest()==rev['sha256'];assert hashlib.sha256(costs.read_bytes()).hexdigest()==cost['candidate_sha256'];assert shutil.disk_usage(p).free>33_000_000_000
shutil.copy2(revisions,target);c=duckdb.connect(str(target));c.execute("SET memory_limit='2GB'");c.execute('SET threads=2');c.execute("ATTACH '"+str(revisions).replace("'","''")+"' AS revised_base (READ_ONLY)");c.execute("ATTACH '"+str(costs).replace("'","''")+"' AS cost_source (READ_ONLY)")
before=[r[0] for r in c.execute('select table_name from _metadata order by 1').fetchall()];assert len(before)==23 and 'cost1' not in before and 'cost2' not in before
for table in ['cost1','cost2']:
 c.execute(f'CREATE TABLE {table} AS SELECT * FROM cost_source.{table}')
 assert c.execute(f'select count(*) from ((select * from {table} except all select * from cost_source.{table}) union all (select * from cost_source.{table} except all select * from {table}))').fetchone()[0]==0
 assert c.execute(f'describe {table}').fetchall()==c.execute(f'describe cost_source.{table}').fetchall()
c.execute('insert into _metadata select * from cost_source._metadata');c.execute('insert into _columns select * from cost_source._columns')
for table in before:
 schema=c.execute(f'describe {table}').fetchall();assert schema==c.execute(f'describe revised_base.{table}').fetchall();cols=','.join('"'+x[0]+'"' for x in schema);sql=f'select count(*),sum(hash({cols})::HUGEINT) from '
 assert c.execute(sql+table).fetchone()==c.execute(sql+'revised_base.'+table).fetchone(),table
 print('PRESERVED',table,flush=True)
for meta in ['_metadata','_columns']:
 clause=" where table_name not in ('cost1','cost2')"
 assert c.execute(f'select count(*) from ((select * from {meta}{clause} except all select * from revised_base.{meta}) union all (select * from revised_base.{meta} except all select * from {meta}{clause}))').fetchone()[0]==0
views=c.execute("select view_name,sql from duckdb_views() where database_name=current_database() and not internal order by 1").fetchall();oldviews=c.execute("select view_name,sql from duckdb_views() where database_name='revised_base' and not internal order by 1").fetchall();assert views==oldviews
for name,_ in views:c.execute(f'select * from {name} limit 1').fetchall()
after=[r[0] for r in c.execute('select table_name from _metadata order by 1').fetchall()];total=c.execute('select sum(row_count) from _metadata').fetchone()[0];assert total==27889050
for name,n in c.execute('select table_name,row_count from _metadata').fetchall():assert c.execute(f'select count(*) from {name}').fetchone()[0]==n
report={'source_tables_before':before,'source_tables_after':after,'source_table_count_before':23,'source_table_count_after':25,'baseline_rows':27876978,'bounded_revision_rows':rev['source_total_rows'],'cost_added_rows':cost['added_source_rows'],'total_rows':total,'net_rows_added':total-27876978,'revision_scope':rev['scope'],'corrected_partition_count':rev['corrected_partition_count'],'cost_vintage':'2024 collection/files, provisional. COST1 includes 2021-22 through 2024-25 cost-of-attendance fields and 2024-25 student charges; COST2 documentation is for average net price 2023-24. Column periods vary; year 2024 is the file/collection label.','cost_typing':cost['typing'],'cost_dictionary_coverage':{'cost1':418,'cost2':539,'missing_source_columns':0},'preserved_views':[x[0] for x in views],'validation':'All 23 existing source tables exactly preserved from bounded revision candidate by schema/count/aggregate row hash. All old metadata rows preserved. New Cost tables exactly equal audited sidecar by full-row multiset comparison, identical schemas, actual counts verified. Existing view definitions unchanged and queried successfully.','limitations':rev['known_preexisting_limitations'],'review_status':'The report records the dataset scope and completed validation checks.'}
c.execute('CHECKPOINT');c.close();reopened=duckdb.connect(str(target),read_only=True);assert reopened.execute('select sum(row_count) from _metadata').fetchone()[0]==27889050;reopened.close();report['writer_version']='1.5.5';report['reopen_version']='1.5.5';report['sha256']=hashlib.sha256(target.read_bytes()).hexdigest();report['bytes']=target.stat().st_size;(p/'combined_compatible_report.json').write_text(json.dumps(report,indent=2));print('VALIDATED',report['total_rows'],report['sha256'],flush=True)
