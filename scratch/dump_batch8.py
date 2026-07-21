import json
from pathlib import Path

files = [
    "JTBk1MUy4Fw.json",
    "lKxiy3gtR3M.json",
    "lMES84se7wI.json",
    "mvdT1R3bMi8.json",
    "NClzF2H2Aag.json",
    "ntqOoAXHchY.json"
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

out_path = Path("scratch/batch8_raw.txt")
out_path.write_text("\n".join(out_lines), encoding="utf-8")
print(f"Successfully dumped Batch 8 to {out_path.absolute()}")
