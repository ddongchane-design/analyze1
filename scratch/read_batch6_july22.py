import json
from pathlib import Path

def main():
    files = ["PC2ATdiqTaI.json", "Dpb3r3wbjic.json", "HQkjs71O_6k.json", "tfy0Qi7L7Bc.json", "JSaUwNYAvdg.json"]
    pending_dir = Path("data/pending")
    
    out_path = Path("scratch/batch6_july22_info.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        for fname in files:
            fpath = pending_dir / fname
            if not fpath.exists():
                f.write(f"=== {fname} NOT FOUND ===\n\n")
                continue
            data = json.loads(fpath.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            
            f.write(f"=== {fname} ===\n")
            f.write(f"Title: {video.get('title')}\n")
            f.write(f"Channel: {video.get('channel_name')}\n")
            f.write(f"Published: {video.get('published')}\n")
            f.write(f"Transcript Length: {len(transcript)} chars\n")
            f.write("Transcript:\n")
            f.write(transcript[:3000] + "\n... [TRUNCATED] ...\n" if len(transcript) > 3000 else transcript)
            f.write("\n================================================================\n\n")
            
    print("Wrote Batch 6 July 22 to scratch/batch6_july22_info.txt")

if __name__ == "__main__":
    main()
