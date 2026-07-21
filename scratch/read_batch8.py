import json
from pathlib import Path

def main():
    files = ["dpK5W8XFat4.json", "rIn924lOk1w.json", "jIimadrlkns.json", "9hVM6IMciLs.json"]
    pending_dir = Path("data/pending")
    
    out_path = Path("scratch/temp_batch.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        for fname in files:
            fpath = pending_dir / fname
            if not fpath.exists():
                f.write(f"=== FILE: {fname} (NOT FOUND) ===\n\n")
                continue
            
            data = json.loads(fpath.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            t_len = len(transcript)
            
            f.write(f"=== FILE: {fname} ===\n")
            f.write(f"ID: {fpath.stem}\n")
            f.write(f"TITLE: {video.get('title')}\n")
            f.write(f"CHANNEL: {video.get('channel_name')}\n")
            f.write(f"PUBLISHED: {video.get('published')}\n")
            f.write(f"TRANSCRIPT LENGTH: {t_len} chars\n")
            f.write("TRANSCRIPT:\n")
            
            if t_len <= 1000:
                f.write(transcript)
            else:
                f.write(transcript[:500] + "\n... [TRUNCATED] ...\n" + transcript[-500:])
            f.write("\n================================================================================\n\n")
            
    print("Wrote Batch 8 transcripts to scratch/temp_batch.txt")

if __name__ == "__main__":
    main()
