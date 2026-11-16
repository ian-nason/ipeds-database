"""Prepare GR 2023 revised partition under existing schema with explicit label-loss warning."""
import duckdb,pandas as pd,zipfile,io,json,importlib.util,hashlib
from pathlib import Path
assert pd.__version__=='3.1.1', 'Use the pandas version pinned in requirements.replay.txt'
assert duckdb.__version__=='1.5.5', 'Use DuckDB 1.5.5 to preserve established client compatibility'
p=Path(__file__).parent
assert hashlib.sha256((p/'ipeds.original.duckdb').read_bytes()).hexdigest() == '8df0b1a06af63f5724a3e883930f39ac1a80ac871f5d852b9eee75433388f429', 'Baseline SHA-256 does not match the pinned release'
spec=importlib.util.spec_from_file_location('build',p/'build_database.upstream.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
c=duckdb.connect();c.execute("ATTACH '"+str(p/'ipeds.original.duckdb').replace("'","''")+"' AS base (READ_ONLY)");schema=c.execute('describe base.gr').fetchall();cols={x[0]:x[1] for x in schema};out={};badsets=[]
with zipfile.ZipFile(p/'history_sources/GR2023.zip') as z:
 for name,target in [('gr2023.csv','original'),('gr2023_RV.csv','revised')]:
  raw=z.read(name);raw_df=pd.read_csv(io.BytesIO(raw),low_memory=False)
  raw_line=raw_df[next(col for col in raw_df.columns if col.strip().lower()=='line')]
  raw_bad=raw_line.notna() & pd.to_numeric(raw_line,errors='coerce').isna()
  bad=raw_line[raw_bad].value_counts().to_dict();badsets.append(set(bad))
  df=b.harmonize_gr(raw_df.copy(),2023)
  after_bad=df.line.notna() & pd.to_numeric(df.line,errors='coerce').isna()
  stage_counts={'raw_nonnumeric_labels':int(raw_bad.sum()),'lost_during_harmonization':int((raw_bad & df.line.isna()).sum()),'lost_during_casting':int(after_bad.sum())}
  assert stage_counts['raw_nonnumeric_labels']==stage_counts['lost_during_harmonization']+stage_counts['lost_during_casting']
  projected=','.join(f'TRY_CAST("{col}" AS {typ}) AS "{col}"' if col in df.columns else f'CAST(NULL AS {typ}) AS "{col}"' for col,typ in cols.items());c.execute(f'create table {target} as select {projected} from df')
  out[target]={'rows':len(df),'lost_line_labels':bad,'loss_stages':stage_counts,'sha256':hashlib.sha256(raw).hexdigest()}
assert badsets[0]==badsets[1]=={'29A','12A','18A','11A'}
assert c.execute('select count(*) from ((select * from original except all select * from base.gr where year=2023) union all (select * from base.gr where year=2023 except all select * from original))').fetchone()[0]==0
out['different_revised_rows']=c.execute('select count(*) from (select * from revised except all select * from original)').fetchone()[0];out['different_original_rows']=c.execute('select count(*) from (select * from original except all select * from revised)').fetchone()[0]
assert out['different_revised_rows']==642 and out['different_original_rows']==619
c.execute('COPY revised TO ? (FORMAT PARQUET)',[str(p/'gr2023.final.existing-schema.parquet')])
out['disposition']='Safe to apply final revisions within unchanged existing lossy schema after review. Exactly the same four nonnumeric line-label categories are already lost in baseline; final file changes their counts, not the unsupported categories. No new label class introduced. Preserving the true labels requires a separately reviewed schema repair to VARCHAR; this partition does not make that change.'
(p/'gr2023_disposition.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
