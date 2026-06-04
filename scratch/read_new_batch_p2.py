import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_dir = Path("data/pending")
json_files = sorted(list(pending_dir.glob("*.json")))

for idx in range(8, len(json_files)):
    file_path = json_files[idx]
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        print(f"[{idx+1}] FILE: {file_path.name}")
        print(f"    TITLE: {video.get('title')}")
        print(f"    CHANNEL: {video.get('channel_name')}")
        print(f"    PUBLISHED: {video.get('published')}")
        print(f"    TRANSCRIPT LENGTH: {len(transcript)}")
        print(f"    PREVIEW: {transcript[:1200]}")
        print("-" * 60)
    except Exception as e:
        print(f"[{idx+1}] Error reading {file_path.name}: {e}")
        print("-" * 60)
