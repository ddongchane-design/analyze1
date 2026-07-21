import json
import textwrap
from pathlib import Path

def dump_group3():
    pending_dir = Path("data/pending")
    json_files = sorted(list(pending_dir.glob("*.json")))
    
    selected = json_files[0:11]
    out_lines = []
    
    for idx, f in enumerate(selected, 1):
        data = json.loads(f.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        
        out_lines.append(f"=== VIDEO {idx} ===")
        out_lines.append(f"FILE: {f.name}")
        out_lines.append(f"TITLE: {video.get('title')}")
        out_lines.append(f"CHANNEL: {video.get('channel_name')}")
        out_lines.append("TRANSCRIPT PREVIEW:")
        
        sub_text = transcript[:8000]
        wrapped = textwrap.wrap(sub_text, width=80)
        out_lines.extend(wrapped)
        out_lines.append("=" * 80 + "\n")
        
    out_path = Path("scratch/temp_read.txt")
    out_path.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Dumped {len(selected)} files to {out_path.absolute()}")

if __name__ == "__main__":
    dump_group3()
