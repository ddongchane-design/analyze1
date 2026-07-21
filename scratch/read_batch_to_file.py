import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python read_batch_to_file.py <file1.json> <file2.json> ...")
        return
    
    pending_dir = Path("data/pending")
    out_path = Path("scratch/temp_batch.txt")
    
    with open(out_path, "w", encoding="utf-8") as out_file:
        for filename in sys.argv[1:]:
            file_path = pending_dir / filename
            if not file_path.exists():
                out_file.write(f"File {filename} does not exist in data/pending\n\n")
                continue
            try:
                data = json.loads(file_path.read_text(encoding="utf-8"))
                video = data.get("video", {})
                transcript = data.get("transcript", "")
                
                out_file.write(f"=== FILE: {filename} ===\n")
                out_file.write(f"ID: {video.get('id')}\n")
                out_file.write(f"TITLE: {video.get('title')}\n")
                out_file.write(f"CHANNEL: {video.get('channel_name')}\n")
                out_file.write(f"PUBLISHED: {video.get('published')}\n")
                out_file.write(f"TRANSCRIPT LENGTH: {len(transcript)} chars\n")
                out_file.write("TRANSCRIPT:\n")
                out_file.write(transcript)
                out_file.write("\n" + "=" * 80 + "\n\n")
            except Exception as e:
                out_file.write(f"Error reading {filename}: {e}\n\n")
                
    print(f"Successfully wrote transcripts to {out_path}")

if __name__ == "__main__":
    main()
