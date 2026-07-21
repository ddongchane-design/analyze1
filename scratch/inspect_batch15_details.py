import json
import sys
from pathlib import Path

# Set stdout to UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_dir = Path("data/pending")
pending_files = sorted(list(pending_dir.glob("*.json")))

print(f"Total pending files: {len(pending_files)}")
print("-" * 60)
for idx, filepath in enumerate(pending_files):
    try:
        data = json.loads(filepath.read_text(encoding="utf-8"))
        video = data.get("video", {})
        title = video.get("title")
        channel = video.get("channel_name")
        video_id = video.get("video_id", filepath.stem)
        print(f"{idx+1:02d}. File: {filepath.name} | ID: {video_id}")
        print(f"    Channel: {channel}")
        print(f"    Title: {title}")
    except Exception as e:
        print(f"{idx+1:02d}. File: {filepath.name} | Error: {e}")
    print("-" * 60)
