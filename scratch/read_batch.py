import sys
import json
from pathlib import Path

# Set stdout to UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    if len(sys.argv) < 2:
        print("Usage: python read_batch.py file1.json file2.json ...")
        return

    pending_dir = Path("data/pending")
    for filename in sys.argv[1:]:
        filepath = pending_dir / filename
        if not filepath.exists():
            print(f"File not found: {filename}")
            continue
        
        try:
            data = json.loads(filepath.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            print("=" * 80)
            print(f"FILENAME: {filename}")
            print(f"TITLE: {video.get('title')}")
            print(f"CHANNEL: {video.get('channel_name')}")
            print(f"TRANSCRIPT LENGTH: {len(transcript)}")
            print("-" * 40)
            print(transcript[:8000]) # Limit to 8000 chars as in analyzer.py
            print("=" * 80)
            print("\n")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

if __name__ == "__main__":
    main()
