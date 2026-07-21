import pathlib
import json

def main():
    pending_dir = pathlib.Path("data/pending")
    json_files = sorted(list(pending_dir.glob("*.json")))
    for idx, file_path in enumerate(json_files):
        try:
            data = json.loads(file_path.read_text(encoding="utf-8"))
            video = data.get("video", {})
            print(f"{idx+1}. [{video.get('channel_name')}] {video.get('title')} ({file_path.name})")
        except Exception as e:
            print(f"{idx+1}. Error reading {file_path.name}: {e}")

if __name__ == "__main__":
    main()
