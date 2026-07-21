import json
from pathlib import Path

batch_13 = [
    "4tZKFu0NTRg.json",
    "7DltyKQJpbc.json",
    "Bd2HaBCE1ok.json",
    "bdAKvceZ6bs.json",
    "bm506hKgV7E.json",
    "CTNWEzFH2mk.json",
    "FHmSibpBDn0.json",
    "G1L_E8cqyOA.json",
    "H8K-DTS6rGo.json",
    "KPQmHUp7uF0.json",
    "M4ibN5zGGos.json",
    "VuISwtmy910.json",
    "WQXOiexGLDw.json",
    "_NR_-q3H_jw.json"
]

pending_dir = Path("data/pending")
out_lines = []

for idx, filename in enumerate(batch_13):
    filepath = pending_dir / filename
    if filepath.exists():
        data = json.loads(filepath.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        out_lines.append(f"### {idx+1}. FILENAME: {filename}")
        out_lines.append(f"TITLE: {video.get('title')}")
        out_lines.append(f"CHANNEL: {video.get('channel_name')}")
        out_lines.append(f"PARTIAL TRANSCRIPT (4000 chars):")
        out_lines.append(transcript[:4000])
        out_lines.append("-" * 60)
        out_lines.append("\n")

Path("scratch/batch13_raw.txt").write_text("\n".join(out_lines), encoding="utf-8")
print("Wrote Batch 13 summaries to scratch/batch13_raw.txt")
