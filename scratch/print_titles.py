import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_dir = Path("data/pending")
json_files = sorted(list(pending_dir.glob("*.json")))

for idx, file_path in enumerate(json_files, 1):
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        print(f"[{idx}] {file_path.name} | TITLE: {video.get('title')} | CHANNEL: {video.get('channel_name')} | LEN: {len(transcript)}")
    except Exception as e:
        print(f"[{idx}] Error reading {file_path.name}: {e}")
