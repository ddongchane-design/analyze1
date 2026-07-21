import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Load topics config
topics = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))["topics"]

def parse_date(pub_str):
    if pub_str.endswith('Z'):
        pub_str = pub_str[:-1] + '+00:00'
    return datetime.fromisoformat(pub_str)

result_data = {}

for topic in topics:
    topic_id = topic["id"]
    topic_label = topic["label"]
    synthesis_days = topic.get("synthesis_days", 7)
    
    analyzed_dir = Path(f"data/analyzed/{topic_id}")
    if not analyzed_dir.exists():
        continue
        
    entries = []
    for json_file in analyzed_dir.glob("*.json"):
        try:
            data = json.loads(json_file.read_text(encoding="utf-8"))
            entries.append(data)
        except Exception as e:
            print(f"Error loading {json_file.name}: {e}")
            
    # Sort by published date descending
    entries.sort(key=lambda x: x["video"].get("published", ""), reverse=True)
    
    # Filter by synthesis_days limit
    cutoff = datetime.now(timezone.utc) - timedelta(days=synthesis_days)
    recent = []
    for entry in entries:
        pub_str = entry["video"].get("published", "")
        try:
            pub_dt = parse_date(pub_str)
            if pub_dt >= cutoff:
                analysis_with_date = dict(entry["analysis"])
                analysis_with_date["published_date"] = pub_str[:10]
                analysis_with_date["video_title"] = entry["video"].get("title", "")
                recent.append((pub_dt, analysis_with_date))
        except Exception as e:
            # Fallback
            analysis_with_date = dict(entry["analysis"])
            analysis_with_date["published_date"] = pub_str[:10] if pub_str else ""
            analysis_with_date["video_title"] = entry["video"].get("title", "")
            recent.append((datetime.min.replace(tzinfo=timezone.utc), analysis_with_date))
            
    # Sort by pub_dt descending
    recent.sort(key=lambda x: x[0], reverse=True)
    
    # Get top 10 analyses
    recent_analyses = [analysis for _, analysis in recent[:10]]
    
    if len(recent_analyses) >= 2:
        result_data[topic_id] = {
            "label": topic_label,
            "synthesis_days": synthesis_days,
            "analyses": recent_analyses
        }

# Write summary to scratch
Path("scratch/synthesis_input.json").write_text(json.dumps(result_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"SUCCESS: Prepared synthesis input for {list(result_data.keys())}")
