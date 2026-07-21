import json
from pathlib import Path

pending_dir = Path("data/pending")
analyzed_dir = Path("data/analyzed")

cleaned_count = 0
for f in pending_dir.glob("*.json"):
    video_id = f.stem
    # Find if this video ID is present in any topic subfolder of data/analyzed/
    found = False
    for topic_folder in analyzed_dir.iterdir():
        if topic_folder.is_dir():
            analyzed_file = topic_folder / f.name
            if analyzed_file.exists():
                found = True
                break
    
    if found:
        try:
            f.unlink()
            print(f"Deleted pending: {f.name}")
            cleaned_count += 1
        except Exception as e:
            print(f"Error deleting {f.name}: {e}")

print(f"Cleaned up {cleaned_count} pending files.")
