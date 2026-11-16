"""Download the pinned baseline and exact historical inputs without credentials."""
from pathlib import Path
import json,hashlib,requests,os
ROOT=Path(__file__).resolve().parent
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def get(url,path,expected):
 if path.exists():
  assert sha(path)==expected, f'Existing file has a different identity: {path}'
  return
 path.parent.mkdir(parents=True,exist_ok=True);part=path.with_suffix(path.suffix+'.part')
 with requests.get(url,stream=True,timeout=(30,180)) as r:
  r.raise_for_status()
  with part.open('wb') as f:
   for chunk in r.iter_content(4*1024*1024):f.write(chunk)
 assert sha(part)==expected,f'Source changed; inspect rather than rebuilding silently: {path}'
 os.replace(part,path);print(path.name,flush=True)
pin=json.loads((ROOT/'baseline.json').read_text());get(pin['url'],ROOT/'baseline.duckdb',pin['sha256'])
for rec in json.loads((ROOT/'source-lock.json').read_text()):
 get(rec['url'],ROOT/'sources'/(rec['stem']+'.zip'),rec['sha256'])
