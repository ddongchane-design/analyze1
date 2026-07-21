import glob
import json
from pathlib import Path

files = sorted(glob.glob("data/pending/*.json"))
out = []
out.append(f"Total pending files: {len(files)}")
for f in files:
    try:
        data = json.loads(Path(f).read_text(encoding="utf-8"))
        video = data.get("video", {})
        filename = Path(f).name
        out.append(f"File: {filename}")
        out.append(f"  Title: {video.get('title')}")
        out.append(f"  Channel: {video.get('channel_name')}")
        out.append(f"  Published: {video.get('published')}")
        out.append("-" * 40)
    except Exception as e:
        out.append(f"Error reading {f}: {e}")

Path("scratch/pending_list.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote pending list to scratch/pending_list.txt")
