import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

topics_config = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))["topics"]
topics_map = {t["id"]: t for t in topics_config}

output_input = {}

for topic_id in topics_map.keys():
    topic = topics_map[topic_id]
    analyzed_dir = Path(f"data/analyzed/{topic_id}")
    if not analyzed_dir.exists():
        continue
    analyses = []
    for json_file in analyzed_dir.glob("*.json"):
        try:
            data = json.loads(json_file.read_text(encoding="utf-8"))
            analyses.append(data)
        except Exception:
            pass
    
    # Sort by published date descending
    analyses.sort(key=lambda x: x["video"].get("published", ""), reverse=True)
    
    synthesis_days = topic.get("synthesis_days", 7)
    cutoff = datetime.now(timezone.utc) - timedelta(days=synthesis_days)
    
    recent_analyses = []
    for data in analyses:
        pub_str = data["video"].get("published", "")
        try:
            pub_dt = datetime.fromisoformat(pub_str)
            if pub_dt >= cutoff:
                recent_analyses.append(data["analysis"])
        except Exception:
            recent_analyses.append(data["analysis"])
            
    # Keep top 10 most recent to keep prompt length reasonable
    recent_analyses = recent_analyses[:10]
    if len(recent_analyses) >= 2:
        output_input[topic_id] = {
            "label": topic["label"],
            "analyses": recent_analyses
        }

Path("scratch/synthesis_input.json").write_text(
    json.dumps(output_input, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
print("Saved scratch/synthesis_input.json")
