import sys
import json
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    if len(sys.argv) < 2:
        print("Usage: python read_one.py filename.json")
        return
    
    filepath = Path("data/pending") / sys.argv[1]
    if not filepath.exists():
        print(f"File not found: {sys.argv[1]}")
        return
        
    data = json.loads(filepath.read_text(encoding="utf-8"))
    video = data.get("video", {})
    transcript = data.get("transcript", "")
    print(f"TITLE: {video.get('title')}")
    print(f"CHANNEL: {video.get('channel_name')}")
    print(f"TRANSCRIPT LENGTH: {len(transcript)}")
    print("-" * 50)
    print(transcript[:5000]) # Print first 5000 chars

if __name__ == "__main__":
    main()
