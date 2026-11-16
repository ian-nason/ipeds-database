import unittest,tempfile,io,zipfile
from pathlib import Path
from revision_safe import select_member,fetch_fresh
class Tests(unittest.TestCase):
 def test_prefer_revised(self):self.assertEqual(select_member(['efia2024.csv','efia2024_rv.csv'],'EFIA2024'),'efia2024_rv.csv')
 def test_original(self):self.assertEqual(select_member(['HD2024.csv','hd2024_dict.csv'],'HD2024'),'HD2024.csv')
 def test_duplicate(self):
  with self.assertRaises(ValueError):select_member(['a/hd2024.csv','b/HD2024.csv'],'hd2024')
 def test_unknown(self):
  with self.assertRaises(ValueError):select_member(['hd2024.csv','other.csv'],'hd2024')
 def test_empty(self):
  with self.assertRaises(ValueError):select_member(['README.txt'],'hd2024')
 def test_no_stale_cache(self):
  class Failed:
   def get(self,*a,**kw):raise RuntimeError('network failure')
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'old.zip';p.write_bytes(b'old')
   with self.assertRaises(RuntimeError):fetch_fresh('HD2024',p,Failed())
   self.assertEqual(p.read_bytes(),b'old')
if __name__=='__main__':unittest.main()
