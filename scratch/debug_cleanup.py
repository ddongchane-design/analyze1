import json
from pathlib import Path

pending_dir = Path("data/pending").resolve()
analyzed_dir = Path("data/analyzed").resolve()

print("Pending dir:", pending_dir)
print("Analyzed dir:", analyzed_dir)

pending_files = list(pending_dir.glob("*.json"))
print("Pending files found:", len(pending_files))

for f in pending_files:
    video_id = f.stem
    print(f"Checking pending file: {f.name}")
    found = False
    for topic_folder in analyzed_dir.iterdir():
        if topic_folder.is_dir():
            analyzed_file = topic_folder / f.name
            if analyzed_file.exists():
                print(f"  Found matching analyzed file: {analyzed_file}")
                found = True
                break
    
    if found:
        try:
            f.unlink()
            print(f"  SUCCESS: Deleted {f.name}")
        except Exception as e:
            print(f"  ERROR deleting {f.name}: {e}")
