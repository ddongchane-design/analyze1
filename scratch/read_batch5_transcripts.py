import json
import textwrap
from pathlib import Path

pending_dir = Path("data/pending")
json_files = sorted(list(pending_dir.glob("*.json")))

output_path = Path("scratch/batch5_clean.txt")
lines = []

for idx in range(5):
    if idx >= len(json_files):
        break
    file_path = json_files[idx]
    data = json.loads(file_path.read_text(encoding="utf-8"))
    video = data.get("video", {})
    transcript = data.get("transcript", "")
    
    lines.append("=" * 80)
    lines.append(f"INDEX: {idx}")
    lines.append(f"FILE: {file_path.name}")
    lines.append(f"TITLE: {video.get('title')}")
    lines.append(f"CHANNEL: {video.get('channel_name')}")
    lines.append(f"PUBLISHED: {video.get('published')}")
    lines.append(f"TRANSCRIPT LENGTH: {len(transcript)}")
    lines.append("-" * 80)
    
    paragraphs = transcript.split("\n")
    wrapped_lines = []
    for para in paragraphs:
        wrapped_lines.extend(textwrap.wrap(para, width=100))
    
    lines.extend(wrapped_lines[:200]) # First 200 wrapped lines of transcript
    lines.append("=" * 80 + "\n\n")

output_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Batch 5 clean text written to {output_path}")
