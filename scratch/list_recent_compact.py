import json
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

topics = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))["topics"]

for topic in topics:
    topic_id = topic["id"]
    analyzed_dir = Path(f"data/analyzed/{topic_id}")
    synthesis_days = topic.get("synthesis_days", 7)
    cutoff = datetime.now(timezone.utc) - timedelta(days=synthesis_days)
    
    recent_videos = []
    if analyzed_dir.exists():
        for json_file in analyzed_dir.glob("*.json"):
            try:
                data = json.loads(json_file.read_text(encoding="utf-8"))
                pub_str = data["video"].get("published", "")
                pub_dt = datetime.fromisoformat(pub_str)
                if pub_dt >= cutoff:
                    recent_videos.append({
                        "id": data["video"]["id"],
                        "title": data["video"]["title"],
                        "signal": data["analysis"]["signal"],
                        "summary": data["analysis"]["summary"]
                    })
            except Exception as e:
                pass
                
    print(f"=== {topic_id} ({topic['label']}), count: {len(recent_videos)} ===")
    for v in recent_videos:
        print(f"  [{v['signal'].upper()}] {v['title']}")
        print(f"    {v['summary'][:150]}...")
    print("-" * 50)
