import json
from pathlib import Path

pending_dir = Path("data/pending")
files = sorted(list(pending_dir.glob("*.json")))

output_path = Path("scratch/pending_list.txt")
lines = []

for idx, f in enumerate(files):
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
        video = data.get("video", {})
        lines.append(f"{idx:02d} | FILE: {f.name}")
        lines.append(f"   TITLE: {video.get('title')}")
        lines.append(f"   CHANNEL: {video.get('channel_name')}")
        lines.append(f"   PUBLISHED: {video.get('published')}")
        lines.append(f"   TRANSCRIPT LENGTH: {len(data.get('transcript', ''))}")
        lines.append("-" * 60)
    except Exception as e:
        lines.append(f"{idx:02d} | ERROR reading {f.name}: {e}")
        lines.append("-" * 60)

output_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Pending list written to {output_path}")
