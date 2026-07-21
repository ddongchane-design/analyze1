import json
from pathlib import Path

def main():
    files = ["lIxLeB4H2IM.json", "NIr8nJs7gEg.json", "81C4RYcyw7Y.json", "_jerMEDkb-o.json", "UZEZ1KJXQt4.json"]
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
            
            f.write(transcript)
            f.write("\n================================================================================\n\n")
            
    print("Wrote Batch 3 transcripts to scratch/temp_batch.txt")

if __name__ == "__main__":
    main()
