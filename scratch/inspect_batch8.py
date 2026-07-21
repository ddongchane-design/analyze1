import json
from pathlib import Path
import textwrap

video_ids = ["4gRQXb_uLr4", "5Iq71prrSf0", "8ifkwnuet-M", "bq_GAPruaYU"]
output_lines = []

for vid in video_ids:
    filepath = Path("data/pending") / f"{vid}.json"
    if not filepath.exists():
        output_lines.append(f"File {vid}.json does not exist in pending.\n")
        continue
    data = json.loads(filepath.read_text(encoding="utf-8"))
    video = data.get("video", {})
    transcript = data.get("transcript", "")
    output_lines.append(f"==================================================")
    output_lines.append(f"ID: {vid}")
    output_lines.append(f"TITLE: {video.get('title')}")
    output_lines.append(f"CHANNEL: {video.get('channel_name')}")
    output_lines.append(f"TRANSCRIPT PREVIEW:")
    
    # Let's write the first 5000 characters of transcript, wrapped
    wrapped = textwrap.wrap(transcript[:5000], width=80)
    output_lines.extend(wrapped)
    output_lines.append(f"==================================================\n")

out_file = Path("scratch/inspect_batch8_output.txt")
out_file.write_text("\n".join(output_lines), encoding="utf-8")
print(f"Successfully wrote inspect results to {out_file.absolute()}")
