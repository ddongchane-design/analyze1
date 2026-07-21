import json
from pathlib import Path

def main():
    pending_dir = Path("data/pending")
    out_path = Path("scratch/list_pending_output.txt")
    
    files = sorted(list(pending_dir.glob("*.json")))
    with open(out_path, "w", encoding="utf-8") as out_file:
        out_file.write(f"{'File':<20} | {'Channel':<25} | {'Date':<22} | {'Title'}\n")
        out_file.write("-" * 120 + "\n")
        for f in files:
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                video = data.get("video", {})
                transcript = data.get("transcript", "")
                t_len = len(transcript) if isinstance(transcript, str) else len(json.dumps(transcript))
                out_file.write(f"{f.name:<20} | {video.get('channel_name', 'N/A'):<25} | {video.get('published', 'N/A'):<22} | {video.get('title')} ({t_len} chars)\n")
            except Exception as e:
                out_file.write(f"{f.name:<20} | Error: {e}\n")
                
    print(f"Wrote list of {len(files)} pending files to {out_path}")

if __name__ == "__main__":
    main()
