import glob
import json
import sys
from pathlib import Path

def main():
    pending_files = list(Path("data/pending").glob("*.json"))
    if not pending_files:
        print("No pending files found.")
        return

    print(f"Total pending files: {len(pending_files)}")
    print("=" * 80)

    for i, file_path in enumerate(pending_files):
        try:
            data = json.loads(file_path.read_text(encoding="utf-8"))
            video = data["video"]
            transcript = data["transcript"]
            
            print(f"INDEX: {i}")
            print(f"ID: {video['id']}")
            print(f"TITLE: {video['title']}")
            print(f"CHANNEL: {video['channel_name']}")
            print(f"PUBLISHED: {video['published']}")
            print(f"TRANSCRIPT_LEN: {len(transcript)}")
            print("-" * 40)
            print("TRANSCRIPT_START:")
            # Print first 6000 characters of transcript
            print(transcript[:6000])
            print("=" * 80)
        except Exception as e:
            print(f"Error reading {file_path.name}: {e}")

if __name__ == "__main__":
    main()
