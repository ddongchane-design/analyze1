import os
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_dir = "data/pending"
files = sorted([f for f in os.listdir(pending_dir) if f.endswith(".json")])

print(f"Total pending files: {len(files)}")
for f in files:
    path = os.path.join(pending_dir, f)
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    video = data.get("video", {})
    transcript = data.get("transcript", "")
    print(f"ID: {f}")
    print(f"  Title: {video.get('title')}")
    print(f"  Channel: {video.get('channel_name')}")
    print(f"  Published: {video.get('published')}")
    print(f"  Sub Length: {len(transcript)}")
    print(f"  Preview: {transcript[:200]}...")
    print("-" * 60)
