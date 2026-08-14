import json, sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

f_path = Path("data/pending/n8SE6KxRY34.json")
if f_path.exists():
    data = json.loads(f_path.read_text(encoding="utf-8"))
    video = data.get("video", {})
    transcript = data.get("transcript", "")
    print(f"TITLE: {video.get('title')}")
    print(f"CHANNEL: {video.get('channel_name')}")
    print(f"SAMPLE: {transcript[:2000]}")
