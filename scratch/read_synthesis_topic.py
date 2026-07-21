import sys
import json
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python read_synthesis_topic.py <topic_id>")
    sys.exit(1)

topic_id = sys.argv[1]
input_path = Path("scratch/synthesis_input.json")

if not input_path.exists():
    print("Error: scratch/synthesis_input.json does not exist")
    sys.exit(1)

try:
    data = json.loads(input_path.read_text(encoding="utf-8"))
    if topic_id not in data:
        print(f"Topic '{topic_id}' not found in synthesis data.")
        sys.exit(0)
        
    print(json.dumps(data[topic_id], ensure_ascii=False, indent=2))
except Exception as e:
    print(f"Error: {e}")
