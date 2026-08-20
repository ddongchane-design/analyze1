import sys
import json
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python print_topic.py <topic_id>")
        return
    topic_id = sys.argv[1]
    
    path = Path("data/recent_analyses_raw.json")
    if not path.exists():
        print("data/recent_analyses_raw.json does not exist")
        return
        
    data = json.loads(path.read_text(encoding="utf-8"))
    if topic_id in data:
        temp_path = Path("data/temp_topic.json")
        temp_path.write_text(json.dumps(data[topic_id], ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Saved {topic_id} data to {temp_path}")
    else:
        print(f"Topic {topic_id} not found in aggregated data")

if __name__ == "__main__":
    main()
