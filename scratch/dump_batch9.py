import json
from pathlib import Path

files = [
    "nxFaHLJmUB8.json",
    "rLwxMsZ-Xrw.json",
    "Rrr_s8X6nTs.json",
    "sjw4z2QzrhQ.json",
    "SZgH58tvqwE.json",
    "VA3uW3atR_4.json",
    "vajSoLiW3F8.json",
    "zcJSWiwAYjI.json",
    "ZqN0tOnE-Us.json",
    "_Ds243MMWhI.json"
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

out_path = Path("scratch/batch9_raw.txt")
out_path.write_text("\n".join(out_lines), encoding="utf-8")
print(f"Successfully dumped Batch 9 to {out_path.absolute()}")
