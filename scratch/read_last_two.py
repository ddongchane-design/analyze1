import json
from pathlib import Path

files = ["YT1fa3P45D0.json", "yxGJfI9MTRo.json"]
output_lines = []
for filename in files:
    filepath = Path("data/pending") / filename
    if filepath.exists():
        data = json.loads(filepath.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        output_lines.append(f"=== {filename} ===")
        output_lines.append(f"TITLE: {video.get('title')}")
        output_lines.append(f"CHANNEL: {video.get('channel_name')}")
        output_lines.append(f"TRANSCRIPT (first 8000 chars):")
        output_lines.append(transcript[:8000])
        output_lines.append("===================================\n")

Path("scratch/read_last_two_output.txt").write_text("\n".join(output_lines), encoding="utf-8")
