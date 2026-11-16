import pytest
import pandas as pd
from schema_review import review_gr_labels,raw_labels,review_empty_placeholders

def test_changed_counts_of_known_classes():
 labels={'29A':3,'12A':4,'18A':5,'11A':6}
 assert review_gr_labels('gr',labels,{**labels,'29A':4})['revised']['29A']==4

def test_new_class_is_rejected():
 labels={'29A':3,'12A':4,'18A':5,'11A':6}
 with pytest.raises(AssertionError):review_gr_labels('gr',labels,{**labels,'99A':1})

def test_numeric_rows_are_not_label_losses():
 assert raw_labels(b'LINE,COUNT\n1,20\n29A,4\n,6\n12A,2\n','line')=={'29A':1,'12A':1}

def test_empty_source_placeholders_only():
 frame=pd.DataFrame({col:[None,None] for col in ['py0','py1','py2','py3']})
 review_empty_placeholders('ic_py',2011,frame,set(frame.columns))
 frame.loc[0,'py0']='substantive value'
 with pytest.raises(AssertionError):review_empty_placeholders('ic_py',2011,frame,set(frame.columns))
