import json
from pathlib import Path

def main():
    pending_dir = Path("data/pending")
    files = list(pending_dir.glob("*.json"))
    output_path = Path("scratch/pending_list.txt")
    with output_path.open("w", encoding="utf-8") as out:
        out.write(f"Total pending files: {len(files)}\n")
        for f in sorted(files, key=lambda x: x.name):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                video = data.get("video", {})
                out.write(f"ID: {video.get('id')}\n")
                out.write(f"Title: {video.get('title')}\n")
                out.write(f"Channel: {video.get('channel_name')}\n")
                out.write("-" * 40 + "\n")
            except Exception as e:
                out.write(f"Error reading {f.name}: {e}\n")
    print("Done writing to scratch/pending_list.txt")

if __name__ == "__main__":
    main()
