import os
import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python save_analyses.py <analyses_json_path>")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    if not json_path.exists():
        print(f"Error: {json_path} does not exist.")
        sys.exit(1)

    try:
        batch = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error parsing JSON batch file: {e}")
        sys.exit(1)

    print(f"Loaded {len(batch)} analyses to save.")
    
    topics_config = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))["topics"]
    valid_topic_ids = {t["id"] for t in topics_config}

    for item in batch:
        video = item.get("video")
        analysis = item.get("analysis")
        classification = item.get("classification")

        if not video or not analysis or not classification:
            print(f"Skipping invalid item: {item.get('video', {}).get('id', 'unknown')}")
            continue

        video_id = video["id"]
        primary = classification.get("primary_topic", "etc")
        if primary not in valid_topic_ids:
            primary = "etc"

        # Construct final format
        final_data = {
            "video": video,
            "analysis": analysis,
            "classification": classification
        }

        # Validate with the harness
        from agents.harness import validate_item
        is_valid, errors = validate_item(final_data)
        if not is_valid:
            print(f"Error: Item {video_id} failed validation harness:")
            for err in errors:
                print(f"  - {err}")
            print("Skipping save for this item.")
            continue

        # Save to analyzed folder
        dest_dir = Path("data/analyzed") / primary
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_path = dest_dir / f"{video_id}.json"
        
        dest_path.write_text(json.dumps(final_data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Saved: {dest_path}")

        # Delete pending file
        pending_path = Path("data/pending") / f"{video_id}.json"
        if pending_path.exists():
            pending_path.unlink()
            print(f"Deleted pending: {pending_path}")

        # Invalidate synthesis cache
        synthesis_cache = Path("data/synthesis") / f"{primary}.json"
        if synthesis_cache.exists():
            try:
                synthesis_cache.unlink()
                print(f"Deleted synthesis cache for '{primary}'")
            except Exception as e:
                print(f"Warning: Failed to delete synthesis cache for {primary}: {e}")

if __name__ == "__main__":
    main()
