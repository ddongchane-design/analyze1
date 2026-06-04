import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_dir = Path("data/pending")
json_files = sorted(list(pending_dir.glob("*.json")))

print(f"Total pending files: {len(json_files)}")
print("-" * 60)

for idx, file_path in enumerate(json_files, 1):
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        print(f"[{idx}] FILE: {file_path.name}")
        print(f"    TITLE: {video.get('title')}")
        print(f"    CHANNEL: {video.get('channel_name')}")
        print(f"    PUBLISHED: {video.get('published')}")
        print(f"    TRANSCRIPT LENGTH: {len(transcript)}")
        print(f"    PREVIEW: {transcript[:1200]}")
        print("-" * 60)
    except Exception as e:
        print(f"[{idx}] Error reading {file_path.name}: {e}")
        print("-" * 60)
