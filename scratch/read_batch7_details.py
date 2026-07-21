import json
from pathlib import Path

def main():
    files = [
        "28GFiZhKECI.json",
        "hI1AFp1TJDo.json",
        "E8BMnRLZWsQ.json",
        "8p3Jw-GI1UY.json",
        "tyGE1ML_KPg.json"
    ]
    
    pending_dir = Path("data/pending")
    out_path = Path("scratch/temp_read_batch7.txt")
    
    with open(out_path, "w", encoding="utf-8") as out_file:
        for filename in files:
            path = pending_dir / filename
            if not path.exists():
                out_file.write(f"File {filename} not found\n\n")
                continue
            
            data = json.loads(path.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            
            out_file.write(f"=== FILE: {filename} ===\n")
            out_file.write(f"TITLE: {video.get('title')}\n")
            out_file.write(f"CHANNEL: {video.get('channel_name')}\n")
            out_file.write(f"PUBLISHED: {video.get('published')}\n")
            out_file.write(f"TRANSCRIPT LENGTH: {len(transcript)} chars\n")
            
            # Print first 2000 chars and last 2000 chars, and middle 2000 chars
            out_file.write("--- TRANSCRIPT SNIPPETS ---\n")
            out_file.write("START:\n")
            out_file.write(transcript[:3000])
            out_file.write("\n\nMIDDLE:\n")
            mid = len(transcript) // 2
            out_file.write(transcript[mid-2000:mid+2000])
            out_file.write("\n\nEND:\n")
            out_file.write(transcript[-3000:])
            out_file.write("\n" + "=" * 80 + "\n\n")
            
    print(f"Wrote Batch 7 snippets to {out_path}")

if __name__ == "__main__":
    main()
