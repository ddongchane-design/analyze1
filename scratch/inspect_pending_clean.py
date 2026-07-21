import json
from pathlib import Path

def inspect_all_pending():
    pending_dir = Path("data/pending")
    json_files = sorted(list(pending_dir.glob("*.json")))
    
    out_lines = []
    for idx, f in enumerate(json_files, 1):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            
            out_lines.append(f"INDEX: {idx}")
            out_lines.append(f"FILE: {f.name}")
            out_lines.append(f"TITLE: {video.get('title')}")
            out_lines.append(f"CHANNEL: {video.get('channel_name')}")
            out_lines.append("TRANSCRIPT START:")
            out_lines.append(transcript[:1500])
            out_lines.append("="*100)
            out_lines.append("\n")
        except Exception as e:
            out_lines.append(f"ERROR reading {f.name}: {e}")
            
    Path("scratch/pending_previews.txt").write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Dumped {len(json_files)} previews to scratch/pending_previews.txt")

if __name__ == "__main__":
    inspect_all_pending()
