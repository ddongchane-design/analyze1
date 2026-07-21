import json
from pathlib import Path

batch_11 = [
    "8tUfR9WZtmA.json",
    "CTHMrzXPH1E.json",
    "CVFtZV4WEJM.json",
    "CbcE45MNaoM.json",
    "CrerETT7k2I.json",
    "Cv-gi8-Kn9o.json",
    "IAEJ9qWPjeE.json",
    "Ip4Ia4yblfU.json",
    "LGf6jWKC8oc.json",
    "O-szWnndpBQ.json",
    "Td7U_4SuXC0.json",
    "UQ-Hz9FDEiA.json",
    "ZwxgQIG7S1Q.json",
    "_es2GIlzVmc.json"
]

pending_dir = Path("data/pending")
out_lines = []

for idx, filename in enumerate(batch_11):
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

Path("scratch/inspect_batch11_output.txt").write_text("\n".join(out_lines), encoding="utf-8")
print("Wrote Batch 11 summaries to scratch/inspect_batch11_output.txt")
