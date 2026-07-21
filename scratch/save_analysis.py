import sys
import json
from pathlib import Path

if len(sys.argv) < 4:
    print("Usage: python save_analysis.py <video_id> <primary_topic> <analysis_json_file>")
    sys.exit(1)

video_id = sys.argv[1]
primary_topic = sys.argv[2]
analysis_json_file = Path(sys.argv[3])

pending_path = Path("data/pending") / f"{video_id}.json"
analyzed_base_dir = Path("data/analyzed")

if not pending_path.exists():
    print(f"Pending file not found: {pending_path}")
    sys.exit(1)

if not analysis_json_file.exists():
    print(f"Analysis JSON file not found: {analysis_json_file}")
    sys.exit(1)

try:
    # Load original pending data to get video info
    pending_data = json.loads(pending_path.read_text(encoding="utf-8"))
    video = pending_data.get("video", {})
    
    # Load subagent's generated analysis and classification
    subagent_data = json.loads(analysis_json_file.read_text(encoding="utf-8"))
    
    analysis = subagent_data.get("analysis", {})
    classification = subagent_data.get("classification", {})
    
    # Structure the final output
    final_output = {
        "video": video,
        "analysis": analysis,
        "classification": classification
    }
    
    # Write to target path
    topic_dir = analyzed_base_dir / primary_topic
    topic_dir.mkdir(parents=True, exist_ok=True)
    analyzed_path = topic_dir / f"{video_id}.json"
    
    analyzed_path.write_text(json.dumps(final_output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"SUCCESS: Saved analyzed result to {analyzed_path}")
    
    # Delete pending file
    pending_path.unlink()
    print(f"SUCCESS: Deleted pending file {pending_path}")
    
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
