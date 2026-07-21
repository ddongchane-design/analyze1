import json
import sys
from pathlib import Path

# Set stdout to UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    if len(sys.argv) < 2:
        print("Usage: python read_batch.py <file1.json> <file2.json> ...")
        return
    
    pending_dir = Path("data/pending")
    for filename in sys.argv[1:]:
        file_path = pending_dir / filename
        if not file_path.exists():
            print(f"File {filename} does not exist in data/pending")
            continue
        try:
            data = json.loads(file_path.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            print(f"=== FILE: {filename} ===")
            print(f"ID: {video.get('id')}")
            print(f"TITLE: {video.get('title')}")
            print(f"CHANNEL: {video.get('channel_name')}")
            print(f"PUBLISHED: {video.get('published')}")
            print(f"TRANSCRIPT (up to 12000 chars):")
            print(transcript[:12000])
            print("=" * 80 + "\n")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

if __name__ == "__main__":
    main()
