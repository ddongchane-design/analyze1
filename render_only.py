import os
import sys
from pathlib import Path
from dotenv import load_dotenv

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

from agents.orchestrator import render_dashboard

# Dynamically delete processed pending files
pending_dir = Path("data/pending")
analyzed_dir = Path("data/analyzed")

if pending_dir.exists():
    for p_file in pending_dir.glob("*.json"):
        video_id = p_file.stem
        # Check if this video has been analyzed in any topic directory
        analyzed_exists = False
        if analyzed_dir.exists():
            for topic_path in analyzed_dir.iterdir():
                if topic_path.is_dir():
                    target_analyzed = topic_path / f"{video_id}.json"
                    if target_analyzed.exists():
                        analyzed_exists = True
                        break
        
        if analyzed_exists:
            try:
                p_file.unlink()
                print(f"Deleted processed pending file: {p_file.name}")
            except Exception as e:
                print(f"Failed to delete {p_file.name}: {e}")

print("Rendering dashboard...")
render_dashboard()
print("Done rendering dashboard!")
