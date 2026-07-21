import json
from pathlib import Path

def main():
    files = ["zS5D9ryA6Pw.json", "IKfa_RBQlCA.json", "2vmLKRWxsAc.json", "_RQtP1PJuFk.json", "NH5EqRoJE_s.json"]
    pending_dir = Path("data/pending")
    
    out_path = Path("scratch/temp_batch.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        for idx, fname in enumerate(files):
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
            
            if t_len <= 30000:
                f.write(transcript)
            else:
                f.write("[TRANSCRIPT IS TOO LONG, SHOWING CHUNKS]\n")
                f.write("--- CHUNK 1 (START) ---\n")
                f.write(transcript[:15000])
                f.write("\n\n--- CHUNK 2 (MIDDLE) ---\n")
                mid_start = t_len // 2 - 7500
                f.write(transcript[mid_start:mid_start+15000])
                f.write("\n\n--- CHUNK 3 (END) ---\n")
                f.write(transcript[-15000:])
            f.write("\n================================================================================\n\n")
            
    print("Wrote Batch 1 transcripts to scratch/temp_batch.txt")

if __name__ == "__main__":
    main()
