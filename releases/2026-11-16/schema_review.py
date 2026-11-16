"""Explicit compatibility review for the already lossy numeric GR line field."""
import io
import pandas as pd

def raw_labels(raw,column):
 try:text=raw.decode('utf-8-sig')
 except UnicodeDecodeError:text=raw.decode('latin1')
 frame=pd.read_csv(io.StringIO(text),dtype=str,keep_default_na=False,usecols=lambda col:col.strip().lower()==column)
 assert len(frame.columns)==1
 values=frame.iloc[:,0];bad=values.ne('') & pd.to_numeric(values,errors='coerce').isna()
 return values[bad].value_counts().to_dict()

def review_gr_labels(table,old,new):
 assert table=='gr'
 assert set(old)==set(new)=={'29A','12A','18A','11A'},'Unreviewed source labels'
 return {'original':old,'revised':new,'disposition':'Counts of the same four known GR line labels changed. Existing numeric schema represents these labels as NULL; no new unsupported label class is accepted.'}

def review_empty_placeholders(table,year,frame,extra):
 assert table=='ic_py' and year==2011 and extra=={'py0','py1','py2','py3'}
 assert frame[list(extra)].isna().all().all(),'A new source field contains values'
