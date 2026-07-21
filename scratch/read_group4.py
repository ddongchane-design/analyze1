import json
import textwrap
from pathlib import Path

def dump_group4():
    pending_dir = Path("data/pending")
    # Group 4 files explicitly
    group4_files = [
        "Qc7KGoDj5m8.json",
        "QJtL1fYQ_yQ.json",
        "qZqCE7xfl0g.json",
        "RBrP44mxPuE.json",
        "RjvFCXUJ3kA.json",
        "tk-LXS-w0y8.json",
        "UtUyfRostjY.json",
        "V0IfOF0eE24.json",
        "wKrKPWYUDho.json",
        "xd60MxaPcTg.json"
    ]
    
    out_lines = []
    
    for idx, fname in enumerate(group4_files, 1):
        f = pending_dir / fname
        if not f.exists():
            print(f"Warning: {fname} does not exist in pending")
            continue
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
        
    out_path = Path("scratch/temp_read_4.txt")
    out_path.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Dumped {len(group4_files)} files to {out_path.absolute()}")

if __name__ == "__main__":
    dump_group4()
