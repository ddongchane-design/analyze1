import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

pending_dir = Path("data/pending")
files = sorted(list(pending_dir.glob("*.json")))
for i, f in enumerate(files):
    data = json.loads(f.read_text(encoding="utf-8"))
    video = data.get("video", {})
    print(f"{i+1:02d}. {f.name} - {video.get('title')} [{video.get('channel_name')}]")
