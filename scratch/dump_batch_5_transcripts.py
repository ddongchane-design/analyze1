import json
from pathlib import Path

batch5_files = [
    "suQ68ikbD0U.json",
    "vAnFMgnU95g.json",
    "vFn-Rw3m048.json",
    "vbsVscEButA.json",
    "wNsSdwETx9Q.json"
]

for idx, fname in enumerate(batch5_files):
    p = Path("data/pending") / fname
    if p.exists():
        data = json.loads(p.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        
        out_content = f"ID: {video.get('id')}\nTITLE: {video.get('title')}\nCHANNEL: {video.get('channel_name')}\nPUBLISHED: {video.get('published')}\n\nTRANSCRIPT:\n{transcript}"
        out_path = Path("scratch") / f"transcript_new_batch5_{idx+1}_{video.get('id')}.txt"
        out_path.write_text(out_content, encoding="utf-8")
        print(f"Dumped: {out_path.name} (length: {len(transcript)})")
    else:
        print(f"Not found: {fname}")
