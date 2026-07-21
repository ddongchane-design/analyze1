import json
from pathlib import Path

batch4_files = [
    "q73I1ZjEosg.json",
    "rdSxgmmQNYQ.json",
    "Rk50SpNxJH0.json",
    "S3HE3t08RDw.json",
    "YcpHhjaH000.json",
    "YQmLrfjTRIE.json"
]

for idx, fname in enumerate(batch4_files):
    p = Path("data/pending") / fname
    if p.exists():
        data = json.loads(p.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        
        out_content = f"ID: {video.get('id')}\nTITLE: {video.get('title')}\nCHANNEL: {video.get('channel_name')}\nPUBLISHED: {video.get('published')}\n\nTRANSCRIPT:\n{transcript}"
        out_path = Path("scratch") / f"transcript_new_batch4_{idx+1}_{video.get('id')}.txt"
        out_path.write_text(out_content, encoding="utf-8")
        print(f"Dumped: {out_path.name} (length: {len(transcript)})")
    else:
        print(f"Not found: {fname}")
