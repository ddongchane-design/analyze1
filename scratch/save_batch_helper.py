import json
import os

def save_analyses(analyzed_list):
    """
    analyzed_list: list of dict with structure:
    {
      "video": { "id", "title", "published", "channel_name", "url", "thumbnail" },
      "analysis": { "summary", "key_claims", "data_points", "signal", "signal_reason", "key_companies", "insight", "action_point" },
      "classification": { "primary_topic", "secondary_topics", "tags" }
    }
    """
    saved_count = 0
    topics_touched = set()
    
    for item in analyzed_list:
        vid = item["video"]["id"]
        topic = item.get("classification", {}).get("primary_topic", "tech")
        topics_touched.add(topic)
        
        # 1. Save to data/analyzed/{topic}/{vid}.json
        topic_dir = os.path.join("data", "analyzed", topic)
        os.makedirs(topic_dir, exist_ok=True)
        out_path = os.path.join(topic_dir, f"{vid}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
            
        # 2. Remove from data/pending/{vid}.json
        pending_path = os.path.join("data", "pending", f"{vid}.json")
        if os.path.exists(pending_path):
            os.remove(pending_path)
            
        saved_count += 1
        print(f"  [저장 완료] {out_path} (pending 삭제 완료)")

    # 3. Invalidate synthesis cache
    for topic in topics_touched:
        synth_path = os.path.join("data", "synthesis", f"{topic}.json")
        if os.path.exists(synth_path):
            os.remove(synth_path)
            print(f"  [캐시 무효화] {synth_path} 삭제됨 (추후 갱신)")

    print(f"총 {saved_count}개 영상 분석 저장 완료!")
