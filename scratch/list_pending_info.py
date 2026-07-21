import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_dir = Path("data/pending")
json_files = sorted(list(pending_dir.glob("*.json")))

print(f"Total pending files: {len(json_files)}")
for idx, file_path in enumerate(json_files):
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        print(f"{idx+1:02d}. File: {file_path.name} | Length: {len(transcript)} | Title: {video.get('title')} | Channel: {video.get('channel_name')}")
    except Exception as e:
        print(f"{idx+1:02d}. Error reading {file_path.name}: {e}")
