import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_dir = Path("data/pending")
json_files = sorted(list(pending_dir.glob("*.json")))

scratch_dir = Path("scratch")
scratch_dir.mkdir(parents=True, exist_ok=True)

for idx in range(0, 6):
    if idx >= len(json_files):
        break
    file_path = json_files[idx]
    data = json.loads(file_path.read_text(encoding="utf-8"))
    video = data.get("video", {})
    transcript = data.get("transcript", "")
    
    out_path = scratch_dir / f"transcript_single_{idx+1}_{video.get('id')}.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"Title: {video.get('title')}\n")
        f.write(f"Channel: {video.get('channel_name')}\n")
        f.write(f"Published: {video.get('published')}\n")
        f.write(f"URL: {video.get('url')}\n")
        f.write("-" * 60 + "\n")
        f.write(transcript)
    
    print(f"Dumped {idx+1} to {out_path.name}")
