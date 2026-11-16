"""Verify the public replay payload before use."""
import hashlib
import json
from pathlib import Path
root = Path(__file__).parent
manifest = json.loads((root / "replay_file_manifest.json").read_text())
for name, expected in manifest.items():
    path = root / name
    data = path.read_bytes()
    assert len(data) == expected["bytes"], name
    assert hashlib.sha256(data).hexdigest() == expected["sha256"], name
print(f"Verified {len(manifest)} payload files.")
