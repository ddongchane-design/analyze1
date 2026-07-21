import json
from pathlib import Path

def main():
    pending_dir = Path("data/pending")
    filenames = [
        "TsfT4KgxMP8.json",
        "ucmqQuBiF3M.json",
        "uCWnxj7GUSc.json",
        "VN_xMQ6D4lA.json",
        "whEA3-nnA3Y.json",
        "WrmcOjiedBY.json"
    ]
    
    out_lines = []
    for filename in filenames:
        filepath = pending_dir / filename
        if not filepath.exists():
            out_lines.append(f"File not found: {filename}\n")
            continue
        
        try:
            data = json.loads(filepath.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            out_lines.append("=" * 80)
            out_lines.append(f"FILENAME: {filename}")
            out_lines.append(f"TITLE: {video.get('title')}")
            out_lines.append(f"CHANNEL: {video.get('channel_name')}")
            out_lines.append(f"TRANSCRIPT LENGTH: {len(transcript)}")
            out_lines.append("-" * 40)
            out_lines.append(transcript[:12000]) # Read up to 12000 chars for richer detail
            out_lines.append("=" * 80)
            out_lines.append("\n\n")
        except Exception as e:
            out_lines.append(f"Error reading {filename}: {e}\n\n")
            
    Path("scratch/batch5_info.txt").write_text("\n".join(out_lines), encoding="utf-8")
    print("Done")

if __name__ == "__main__":
    main()
