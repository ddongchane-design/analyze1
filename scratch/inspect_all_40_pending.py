import json
from pathlib import Path

pending_dir = Path("data/pending")
files = sorted(list(pending_dir.glob("*.json")))

out = []
for i, f in enumerate(files):
    data = json.loads(f.read_text(encoding="utf-8"))
    v = data["video"]
    t = data.get("transcript", "")
    out.append(f"[{i+1}/{len(files)}] ID: {v['id']} | Channel: {v['channel_name']} | Title: {v['title']} | Transcript Length: {len(t)}")

Path("scratch/pending_40_list.txt").write_text("\n".join(out), encoding="utf-8")
print(f"Inspected {len(files)} files and saved list to scratch/pending_40_list.txt")
