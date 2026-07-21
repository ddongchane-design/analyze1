import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_dir = Path("data/pending")
json_files = sorted(list(pending_dir.glob("*.json")))

# Batch 4 is indices 0 to 4 (the first 5 files of the remaining 13 pending files)
batch_indices = [0, 1, 2, 3, 4]

output_path = Path("scratch/batch4_raw.txt")
output_content = []

for idx in batch_indices:
    if idx >= len(json_files):
        continue
    file_path = json_files[idx]
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        output_content.append(f"=== INDEX {idx} | FILE: {file_path.name} ===")
        output_content.append(f"TITLE: {video.get('title')}")
        output_content.append(f"CHANNEL: {video.get('channel_name')}")
        output_content.append(f"PUBLISHED: {video.get('published')}")
        output_content.append(f"TRANSCRIPT LENGTH: {len(transcript)}")
        output_content.append(f"TRANSCRIPT:\n{transcript}")
        output_content.append("\n" + "="*80 + "\n")
    except Exception as e:
        output_content.append(f"=== INDEX {idx} | ERROR reading {file_path.name}: {e} ===")

output_path.write_text("\n".join(output_content), encoding="utf-8")
print(f"Batch 4 transcripts written to {output_path}")
