from pathlib import Path
import json
from datetime import datetime, timezone

root = Path("song")
exts = {".mp3", ".m4a", ".aac", ".ogg", ".wav", ".flac", ".opus", ".webm"}
files = []

if root.exists():
    for p in sorted(root.iterdir(), key=lambda x: x.name.lower()):
        if p.is_file() and p.suffix.lower() in exts:
            files.append(p.name)

out = root / "index.json"
out.parent.mkdir(parents=True, exist_ok=True)
payload = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "files": files,
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {out} with {len(files)} files")