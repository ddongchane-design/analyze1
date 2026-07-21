import json
from pathlib import Path

def main():
    analyzed_dir = Path("data/analyzed")
    summary = {}
    for topic_dir in analyzed_dir.iterdir():
        if topic_dir.is_dir():
            topic = topic_dir.name
            summary[topic] = []
            for file_path in topic_dir.glob("*.json"):
                try:
                    data = json.loads(file_path.read_text(encoding="utf-8"))
                    video = data.get("video", {})
                    analysis = data.get("analysis", {})
                    summary[topic].append({
                        "id": video.get("id"),
                        "title": video.get("title"),
                        "published": video.get("published"),
                        "signal": analysis.get("signal"),
                        "summary": analysis.get("summary")
                    })
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    out_path = Path("scratch/analyzed_summary.json")
    out_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote summary of analyzed files to {out_path}")
    
    # Print count per topic
    for topic, items in summary.items():
        print(f"Topic: {topic:15} | Count: {len(items)}")

if __name__ == "__main__":
    main()
