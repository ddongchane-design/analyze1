import sys
from pathlib import Path

# Add current workspace root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from scratch.save_batch_afternoon import analyses

def verify():
    success = True
    for video_id, info in analyses.items():
        category = info["primary"]
        html_path = Path(f"output/html/{category}.html")
        if not html_path.exists():
            print(f"[FAIL] HTML file not found: {html_path}")
            success = False
            continue
        
        content = html_path.read_text(encoding="utf-8")
        if video_id in content:
            print(f"[OK] Video {video_id} is in {category}.html")
        else:
            print(f"[FAIL] Video {video_id} NOT found in {category}.html")
            success = False
            
    if success:
        print("\nAll videos are successfully verified in their HTML pages!")
    else:
        print("\nVerification failed. Some videos were not found.")

if __name__ == "__main__":
    verify()
