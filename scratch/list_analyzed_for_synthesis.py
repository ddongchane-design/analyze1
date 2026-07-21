import json
from pathlib import Path

analyzed_dir = Path("data/analyzed")
for topic_path in sorted(analyzed_dir.iterdir()):
    if not topic_path.is_dir():
        continue
    topic_id = topic_path.name
    print(f"=== TOPIC: {topic_id} ===")
    
    files = sorted(list(topic_path.glob("*.json")), key=lambda x: x.stat().st_mtime, reverse=True)
    # Print the latest 5 videos for each topic
    for f in files[:5]:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            video = data.get("video", {})
            analysis = data.get("analysis", {})
            print(f"  [{video.get('published')[:10]}] {video.get('title')} | Signal: {analysis.get('signal')}")
            print(f"    Summary: {analysis.get('summary')[:150]}...")
        except Exception as e:
            print(f"  Error reading {f.name}: {e}")
    print()
