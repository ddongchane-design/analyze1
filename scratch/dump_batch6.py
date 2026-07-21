import json
from pathlib import Path

files = [
    "-bRiG8h-QXE.json",
    "0HGyYoYOAo0.json",
    "1PIV_NGa3vc.json",
    "6Fcrl1LznV4.json",
    "8A28Cm2K3OE.json",
    "8AEtq1ACIsU.json"
]
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

out_path = Path("scratch/batch6_raw.txt")
out_path.write_text("\n".join(out_lines), encoding="utf-8")
print(f"Successfully dumped Batch 6 to {out_path.absolute()}")
