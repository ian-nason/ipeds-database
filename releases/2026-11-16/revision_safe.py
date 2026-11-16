"""Strict NCES CSV selection and fresh official-source downloads."""
from pathlib import PurePosixPath,Path
import hashlib,zipfile,requests,datetime,json

def select_member(names,stem):
    """Prefer exactly one revised member; reject duplicate/unknown data CSVs."""
    expected=stem.lower(); groups={'original':[],'revised':[]};unknown=[]
    for name in names:
        base=PurePosixPath(name).name.lower()
        if not base.endswith('.csv') or '_dict' in base or '_freq' in base:continue
        if base==expected+'.csv':groups['original'].append(name)
        elif base==expected+'_rv.csv':groups['revised'].append(name)
        else:unknown.append(name)
    if unknown or any(len(v)>1 for v in groups.values()):raise ValueError(f'Ambiguous data members: {names}')
    candidates=groups['revised'] or groups['original']
    if not candidates:raise ValueError(f'No data CSV for {stem}')
    return candidates[0]

def fetch_fresh(stem,destination,session=None,base_url="https://nces.ed.gov/ipeds/complete-data-files/"):
    """Never return an existing cache silently; no stale legacy fallback."""
    if base_url not in ('https://nces.ed.gov/ipeds/complete-data-files/','https://nces.ed.gov/ipeds/datacenter/data/'): raise ValueError('Unrecognized source endpoint')
    url=f'{base_url}{stem}.zip'
    response=(session or requests).get(url,timeout=120);response.raise_for_status()
    dst=Path(destination);tmp=dst.with_suffix(dst.suffix+'.tmp');tmp.write_bytes(response.content)
    with zipfile.ZipFile(tmp) as z:member=select_member(z.namelist(),stem);z.read(member)
    tmp.replace(dst)
    record={'url':url,'downloaded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archive_sha256':hashlib.sha256(response.content).hexdigest(),'member':member,'etag':response.headers.get('ETag'),'last_modified':response.headers.get('Last-Modified')}
    dst.with_suffix(dst.suffix+'.provenance.json').write_text(json.dumps(record,indent=2))
    return record
