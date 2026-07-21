import json
import glob
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob("data/pending/*.json"))
for idx, f in enumerate(files[:9], 1):
    data = json.loads(Path(f).read_text(encoding="utf-8"))
    video = data.get("video", {})
    print(f"[{idx}] ID: {video.get('id')} | Channel: {video.get('channel_name')}")
    print(f"    Title: {video.get('title')}")
    print(f"    Published: {video.get('published')}")
    print("-" * 60)
