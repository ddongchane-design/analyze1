import sys
import json
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python read_large_file.py <video_id>")
    sys.exit(1)

video_id = sys.argv[1]
pending_path = Path("data/pending") / f"{video_id}.json"

if not pending_path.exists():
    print(f"File not found: {pending_path}")
    sys.exit(1)

try:
    data = json.loads(pending_path.read_text(encoding="utf-8"))
    video = data.get("video", {})
    transcript = data.get("transcript", "")
    
    # Truncate transcript to 80,000 characters to fit in LLM context comfortably
    truncated_transcript = transcript[:80000]
    
    output_data = {
        "video": video,
        "transcript_length": len(transcript),
        "transcript_truncated": truncated_transcript
    }
    
    print(json.dumps(output_data, ensure_ascii=False, indent=2))
except Exception as e:
    print(f"Error: {e}")
