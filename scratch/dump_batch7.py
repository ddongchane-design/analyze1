import json
from pathlib import Path

files = [
    "BzFFX9qqdOQ.json",
    "d3hjW9oDNbw.json",
    "dCDjXzOojdU.json",
    "fdNiTlRHJGA.json",
    "I13-lsYeVqw.json",
    "Ip8W84qlZ2c.json"
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

out_path = Path("scratch/batch7_raw.txt")
out_path.write_text("\n".join(out_lines), encoding="utf-8")
print(f"Successfully dumped Batch 7 to {out_path.absolute()}")
