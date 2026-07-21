import json
from pathlib import Path

batch_12 = [
    "_f72XXvVkcU.json",
    "eBt7nHdKFtg.json",
    "fgqjHb7oFGE.json",
    "hxt8OHob-mM.json",
    "j0dz6NlphPs.json",
    "jN5xMaqN6Yk.json",
    "jS_AkPQE33g.json",
    "kQQ2R30DMV0.json",
    "pOcxSKf_PKw.json",
    "sGrU87PLkqQ.json",
    "uZvGP25HCkE.json",
    "webyouAz46w.json"
]

pending_dir = Path("data/pending")
out_lines = []

for idx, filename in enumerate(batch_12):
    filepath = pending_dir / filename
    if filepath.exists():
        data = json.loads(filepath.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        out_lines.append(f"### {idx+1}. FILENAME: {filename}")
        out_lines.append(f"TITLE: {video.get('title')}")
        out_lines.append(f"CHANNEL: {video.get('channel_name')}")
        out_lines.append(f"PARTIAL TRANSCRIPT:")
        out_lines.append(transcript[:3000])
        out_lines.append("-" * 60)
        out_lines.append("\n")

Path("scratch/inspect_batch12_output.txt").write_text("\n".join(out_lines), encoding="utf-8")
print("Wrote Batch 12 summaries to scratch/inspect_batch12_output.txt")
