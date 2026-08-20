import glob
import json
import sys
from pathlib import Path

def main():
    num_files = 5
    if len(sys.argv) > 1:
        try:
            num_files = int(sys.argv[1])
        except ValueError:
            pass

    pending_files = list(Path("data/pending").glob("*.json"))
    if not pending_files:
        print("No pending files found.")
        return

    print(f"Total pending: {len(pending_files)}")
    print(f"Reading first {min(num_files, len(pending_files))} files:")
    print("=" * 80)

    for i, file_path in enumerate(pending_files[:num_files]):
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
            print("TRANSCRIPT:")
            print(transcript[:50000]) # Print first 50k chars of transcript
            print("=" * 80)
        except Exception as e:
            print(f"Error reading {file_path.name}: {e}")

if __name__ == "__main__":
    main()
