import json
from pathlib import Path

def main():
    pending_dir = Path("data/pending")
    output_file = Path("scratch/transcripts_consolidated.txt")
    
    json_files = sorted(list(pending_dir.glob("*.json")))
    
    with open(output_file, "w", encoding="utf-8") as f:
        for idx, file_path in enumerate(json_files, 1):
            try:
                data = json.loads(file_path.read_text(encoding="utf-8"))
                video = data.get("video", {})
                transcript = data.get("transcript", "")
                
                f.write(f"=== VIDEO {idx} ===\n")
                f.write(f"FILE: {file_path.name}\n")
                f.write(f"TITLE: {video.get('title')}\n")
                f.write(f"CHANNEL: {video.get('channel_name')}\n")
                f.write(f"PUBLISHED: {video.get('published')}\n")
                f.write(f"TRANSCRIPT LENGTH: {len(transcript)}\n")
                f.write("-" * 40 + "\n")
                # Keep up to 8000 characters as in analyzer.py
                f.write(transcript[:8000] + "\n")
                f.write("=" * 80 + "\n\n")
            except Exception as e:
                f.write(f"=== VIDEO {idx} ERROR ===\n")
                f.write(f"FILE: {file_path.name}\n")
                f.write(f"Error: {e}\n")
                f.write("=" * 80 + "\n\n")

if __name__ == "__main__":
    main()
