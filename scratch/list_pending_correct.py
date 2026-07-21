import json
from pathlib import Path

pending_dir = Path("data/pending")
pending_files = sorted(list(pending_dir.glob("*.json")))

print(f"Total pending files found: {len(pending_files)}")
for idx, filepath in enumerate(pending_files):
    try:
        data = json.loads(filepath.read_text(encoding="utf-8"))
        video = data.get("video", {})
        title = video.get("title", "No Title")
        channel = video.get("channel_name", "No Channel")
        print(f"{idx+1:02d}. {filepath.name} | {channel} | {title}")
    except Exception as e:
        print(f"{idx+1:02d}. {filepath.name} | Error: {e}")
