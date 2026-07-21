import json
import sys
from pathlib import Path

video_ids = ["2JQWDZU_icE", "ICoVvcF3ODs", "JifZJZWWlPk", "Rb4PDaiE_kY", "S86P-vnX_Xg"]

out_path = Path("scratch/batch2_raw.txt")
with out_path.open("w", encoding="utf-8") as f:
    for vid in video_ids:
        filepath = Path("data/pending") / f"{vid}.json"
        if not filepath.exists():
            f.write(f"File {filepath} not found.\n")
            continue
        data = json.loads(filepath.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        f.write(f"ID: {vid}\n")
        f.write(f"Title: {video.get('title')}\n")
        f.write(f"Channel: {video.get('channel_name')}\n")
        f.write(f"Published: {video.get('published')}\n")
        f.write(f"Transcript Length: {len(transcript)} chars\n")
        f.write("-" * 50 + "\n")
        if len(transcript) <= 15000:
            f.write(transcript + "\n")
        else:
            f.write("--- START ---\n")
            f.write(transcript[:7000] + "\n")
            f.write("\n... [TRUNCATED] ...\n\n")
            f.write("--- END ---\n")
            f.write(transcript[-7000:] + "\n")
        f.write("=" * 80 + "\n")
print("Done writing to scratch/batch2_raw.txt")
