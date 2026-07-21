import json
from pathlib import Path

video_ids = [
    "HVCgpNZabaM", "xj0xkk2OKPI", "gVH6r7UjsNE", "D8oT0ADxMQs", "nesggTklEAk", 
    "wShEgg61924", "VHWAkTiMDHU", "ityvCMGBIow", "wkmam3gRivY", "nxl1POuRbC4", 
    "EDcxwRV8zPs", "y2B98IMlln8", "Em2E82hh3Fk", "Rg0TmtqaoVI", "ziNh804Rd_I", 
    "lR0xneVTky8", "kusArgj7avo", "4LhmaauRGXk", "UDQP_TxqSxI"
]

output_lines = []

for vid in video_ids:
    file_path = Path(f"data/pending/{vid}.json")
    if file_path.exists():
        data = json.loads(file_path.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        output_lines.append("=" * 80)
        output_lines.append(f"ID: {vid}")
        output_lines.append(f"TITLE: {video.get('title')}")
        output_lines.append(f"CHANNEL: {video.get('channel_name')}")
        output_lines.append("TRANSCRIPT BRIEF (first 1000 chars):")
        output_lines.append(transcript[:1000])
        output_lines.append("=" * 80)
        output_lines.append("\n")

out_file = Path("scratch/transcripts_brief.txt")
out_file.write_text("\n".join(output_lines), encoding="utf-8")
print(f"Written briefs to {out_file}")
