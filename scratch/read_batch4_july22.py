import json
from pathlib import Path

def main():
    files = ["jBK9j9d1c2I.json", "PmeCeihxEQA.json", "4X8hIvke3oc.json", "Rl2FNhq2njc.json", "2otaEljkFPc.json"]
    pending_dir = Path("data/pending")
    
    out_path = Path("scratch/batch4_july22_info.txt")
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
            
    print("Wrote Batch 4 July 22 to scratch/batch4_july22_info.txt")

if __name__ == "__main__":
    main()
