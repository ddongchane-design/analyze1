import json
from pathlib import Path

pending_dir = Path("data/pending")
files = sorted(list(pending_dir.glob("*.json")))

print(f"Total pending files: {len(files)}")
for f in files:
    data = json.loads(f.read_text(encoding="utf-8"))
    v = data["video"]
    t = data.get("transcript", "")
    print(f"\nID: {v['id']} | Channel: {v['channel_name']} | Title: {v['title']}")
    print(f"Transcript length: {len(t)} chars")
    print(f"Sample: {t[:150]}...")
