import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_dir = Path("data/pending")
json_files = sorted(list(pending_dir.glob("*.json")))

out_file = Path("scratch/batch1_raw.txt")
with open(out_file, "w", encoding="utf-8") as f:
    for idx in range(0, 6):
        if idx >= len(json_files):
            break
        file_path = json_files[idx]
        data = json.loads(file_path.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        
        f.write(f"============================================================\n")
        f.write(f"INDEX: {idx+1}\n")
        f.write(f"FILE: {file_path.name}\n")
        f.write(f"TITLE: {video.get('title')}\n")
        f.write(f"CHANNEL: {video.get('channel_name')}\n")
        f.write(f"PUBLISHED: {video.get('published')}\n")
        f.write(f"TRANSCRIPT:\n")
        f.write(transcript)
        f.write(f"\n============================================================\n\n")

print(f"Batch 1 raw data dumped to {out_file}")
