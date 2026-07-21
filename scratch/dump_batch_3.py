import json
from pathlib import Path

files = ["LrNICf6ok3s.json", "LrVWY6pm1ss.json", "MRdSs2FBfcU.json", "Mun_sp-D6aQ.json", "nmyz_A431wM.json", "nyjKbt4TmTk.json"]
pending_dir = Path("data/pending")
out_lines = []

for filename in files:
    filepath = pending_dir / filename
    if filepath.exists():
        data = json.loads(filepath.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        out_lines.append("=" * 80)
        out_lines.append(f"FILENAME: {filename}")
        out_lines.append(f"TITLE: {video.get('title')}")
        out_lines.append(f"CHANNEL: {video.get('channel_name')}")
        out_lines.append(f"TRANSCRIPT PREVIEW (8000 chars):")
        out_lines.append(transcript[:8000])
        out_lines.append("=" * 80)
        out_lines.append("\n")

Path("scratch/batch3_raw.txt").write_text("\n".join(out_lines), encoding="utf-8")
print("Successfully dumped Batch 3")
