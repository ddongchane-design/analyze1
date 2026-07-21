import sys
import json
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    pending_dir = Path("data/pending")
    files = sorted(list(pending_dir.glob("*.json")))
    print(f"Total pending: {len(files)}")
    for i, f in enumerate(files):
        data = json.loads(f.read_text(encoding="utf-8"))
        video = data.get("video", {})
        title = video.get('title', '').replace('\u2026', '...').replace('\u22ef', '...')
        print(f"{i+1:02d} | {video.get('id')} | {title}")

if __name__ == "__main__":
    main()
