from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent
for name,pin in json.loads((root/'replay_file_manifest.json').read_text()).items():
 p=root/name
 assert p.stat().st_size==pin['bytes'],name
 with p.open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==pin['sha256'],name
print('All included payload identities verified')
