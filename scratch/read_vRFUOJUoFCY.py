import json
from pathlib import Path

video_id = "vRFUOJUoFCY"
pending_path = Path("data/pending") / f"{video_id}.json"
data = json.loads(pending_path.read_text(encoding="utf-8"))
transcript = data.get("transcript", "")

chunk_size = 20000
for i in range(0, len(transcript), chunk_size):
    chunk = transcript[i:i+chunk_size]
    out_path = Path("scratch") / f"vRFUOJUoFCY_part_{i//chunk_size + 1}.txt"
    out_path.write_text(chunk, encoding="utf-8")
    print(f"Wrote {out_path} with {len(chunk)} characters")
