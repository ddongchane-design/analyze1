import json
from pathlib import Path

pending_dir = Path("data/pending")
files = sorted(list(pending_dir.glob("*.json")))

out = []
for f in files:
    data = json.loads(f.read_text(encoding="utf-8"))
    v = data["video"]
    t = data.get("transcript", "")
    out.append(f"==========================================")
    out.append(f"FILE: {f.name}")
    out.append(f"ID: {v['id']}")
    out.append(f"CHANNEL: {v['channel_name']}")
    out.append(f"TITLE: {v['title']}")
    out.append(f"PUBLISHED: {v['published']}")
    out.append(f"URL: {v['url']}")
    out.append(f"TRANSCRIPT:\n{t}\n")

Path("scratch/batch_8_details.txt").write_text("\n".join(out), encoding="utf-8")
print("Saved details of 8 pending videos to scratch/batch_8_details.txt")
