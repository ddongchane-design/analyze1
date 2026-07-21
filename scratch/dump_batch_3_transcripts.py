import json
from pathlib import Path

batch3_files = [
    "huowP4qybrk.json",
    "K7UWEJ9nL18.json",
    "kbiuXUY3Eqw.json",
    "L__4lvXJ3lM.json",
    "N6Nr9zXuuGg.json",
    "Owhne6ECfQU.json"
]

for idx, fname in enumerate(batch3_files):
    p = Path("data/pending") / fname
    if p.exists():
        data = json.loads(p.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        
        out_content = f"ID: {video.get('id')}\nTITLE: {video.get('title')}\nCHANNEL: {video.get('channel_name')}\nPUBLISHED: {video.get('published')}\n\nTRANSCRIPT:\n{transcript}"
        out_path = Path("scratch") / f"transcript_new_batch3_{idx+1}_{video.get('id')}.txt"
        out_path.write_text(out_content, encoding="utf-8")
        print(f"Dumped: {out_path.name} (length: {len(transcript)})")
    else:
        print(f"Not found: {fname}")
