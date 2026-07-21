import json
from pathlib import Path

pending_dir = Path("data/pending")
pending_files = sorted(pending_dir.glob("*.json"))

# Dump files 7 to 15 (indices 7 to 15) into separate text files
for idx in range(7, 16):
    p = pending_files[idx]
    try:
        content = p.read_text(encoding="utf-8")
        data = json.loads(content)
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        
        out_content = f"ID: {video.get('id')}\nTITLE: {video.get('title')}\nCHANNEL: {video.get('channel_name')}\nPUBLISHED: {video.get('published')}\n\nTRANSCRIPT:\n{transcript}"
        
        out_file = Path(f"scratch/transcript_single_{idx}_{video.get('id')}.txt")
        out_file.write_text(out_content, encoding="utf-8")
        print(f"Dumped {p.name} to {out_file.name}")
    except Exception as e:
        print(f"Error dumping {p.name}: {e}")
