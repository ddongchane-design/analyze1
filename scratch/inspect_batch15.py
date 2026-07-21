import json
from pathlib import Path

pending_dir = Path("data/pending")
pending_files = sorted(list(pending_dir.glob("*.json")))

out_lines = []

for idx, filepath in enumerate(pending_files):
    data = json.loads(filepath.read_text(encoding="utf-8"))
    video = data.get("video", {})
    transcript = data.get("transcript", "")
    out_lines.append(f"### {idx+1}. FILENAME: {filepath.name}")
    out_lines.append(f"TITLE: {video.get('title')}")
    out_lines.append(f"CHANNEL: {video.get('channel_name')}")
    out_lines.append(f"PARTIAL TRANSCRIPT (3500 chars):")
    out_lines.append(transcript[:3500])
    out_lines.append("-" * 60)
    out_lines.append("\n")

Path("scratch/batch15_raw.txt").write_text("\n".join(out_lines), encoding="utf-8")
print(f"Wrote {len(pending_files)} summaries to scratch/batch15_raw.txt")
