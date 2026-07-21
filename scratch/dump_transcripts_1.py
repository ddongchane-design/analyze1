import json
from pathlib import Path

pending_dir = Path("data/pending")
pending_files = sorted(pending_dir.glob("*.json"))

# Let's take files 0 to 11 (first 12 files)
batch = pending_files[0:12]

out_lines = []
for p in batch:
    try:
        content = p.read_text(encoding="utf-8")
        data = json.loads(content)
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        
        out_lines.append("=" * 80)
        out_lines.append(f"FILE: {p.name}")
        out_lines.append(f"ID: {video.get('id')}")
        out_lines.append(f"TITLE: {video.get('title')}")
        out_lines.append(f"CHANNEL: {video.get('channel_name')}")
        out_lines.append("-" * 80)
        out_lines.append(transcript)
        out_lines.append("\n")
    except Exception as e:
        out_lines.append(f"Error reading {p.name}: {e}\n")

Path("scratch/transcripts_batch_1.txt").write_text("\n".join(out_lines), encoding="utf-8")
print("Dumped transcripts of batch 1 to scratch/transcripts_batch_1.txt")
