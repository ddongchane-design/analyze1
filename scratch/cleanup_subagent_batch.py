import os
from pathlib import Path

video_ids = ["t83Arrj8kKg", "tgAKdQ87jaQ", "TKzLZEKOwWc", "u8Ki0v84gwI", "Ujp7Z1CinMU"]

# Clean up pending files
for vid in video_ids:
    p = Path("data/pending") / f"{vid}.json"
    if p.exists():
        try:
            p.unlink()
            print(f"Deleted pending: {p}")
        except Exception as e:
            print(f"Failed to delete {p}: {e}")

# Clean up temp files
for vid in video_ids:
    p = Path("scratch") / f"temp_{vid}.json"
    if p.exists():
        try:
            p.unlink()
            print(f"Deleted temp: {p}")
        except Exception as e:
            print(f"Failed to delete {p}: {e}")

print("Cleanup complete.")
