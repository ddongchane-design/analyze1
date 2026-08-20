import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

def parse_date(pub_str):
    if pub_str.endswith('Z'):
        pub_str = pub_str[:-1] + '+00:00'
    return datetime.fromisoformat(pub_str)

def main():
    topics = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))["topics"]
    aggregated = {}

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
                    recent.append((pub_dt, entry["analysis"]))
            except Exception as e:
                print(f"Error parsing date {pub_str} for {entry['video'].get('id')}: {e}")
                
        # Sort by pub_dt descending
        recent.sort(key=lambda x: x[0], reverse=True)
        
        # Keep top 10 analyses
        top_10 = [analysis for _, analysis in recent[:10]]
        
        if len(top_10) >= 2:
            aggregated[topic_id] = {
                "label": topic_label,
                "analyses": top_10
            }
            print(f"Topic '{topic_id}' has {len(top_10)} recent analyses (synthesis_days={synthesis_days})")
        else:
            print(f"Topic '{topic_id}' has {len(top_10)} recent analyses (requires at least 2, skipped)")
            
    # Write output to recent_analyses_raw.json
    output_path = Path("data/recent_analyses_raw.json")
    output_path.write_text(json.dumps(aggregated, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved aggregated recent analyses to {output_path}")

if __name__ == "__main__":
    main()
