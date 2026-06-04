import json
from pathlib import Path

pending_dir = Path("data/pending")
files = sorted(list(pending_dir.glob("*.json")), key=lambda x: x.stat().st_size)

print(f"Total files: {len(files)}")
for f in files:
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        print(f"{f.name:<20} | size: {f.stat().st_size:<6} | len: {len(transcript):<6} | {video.get('channel_name')}: {video.get('title')[:30]}")
    except Exception as e:
        print(f"Error {f.name}: {e}")
