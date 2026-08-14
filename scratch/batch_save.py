import json
import sys
from pathlib import Path
from agents.harness import validate_item

def save_batch(items):
    topics_config = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))["topics"]
    valid_topic_ids = {t["id"] for t in topics_config}

    saved_count = 0
    for item in items:
        video = item.get("video")
        analysis = item.get("analysis")
        classification = item.get("classification")

        if not video or not analysis or not classification:
            print(f"Skipping invalid item structure: {video.get('id') if video else 'unknown'}")
            continue

        video_id = video["id"]
        primary = classification.get("primary_topic", "etc")
        if primary not in valid_topic_ids:
            primary = "etc"

        is_valid, errors = validate_item(item)
        if not is_valid:
            print(f"Validation failed for {video_id}:")
            for e in errors:
                print(f"  - {e}")
            continue

        # Save to analyzed
        dest_dir = Path("data/analyzed") / primary
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_path = dest_dir / f"{video_id}.json"
        dest_path.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Saved: {dest_path}")

        # Remove from pending
        pending_path = Path("data/pending") / f"{video_id}.json"
        if pending_path.exists():
            pending_path.unlink()
            print(f"Deleted pending: {pending_path}")

        # Invalidate synthesis cache
        synth_path = Path("data/synthesis") / f"{primary}.json"
        if synth_path.exists():
            try:
                synth_path.unlink()
                print(f"Deleted synthesis cache: {synth_path}")
            except Exception as e:
                print(f"Warning deleting synthesis cache: {e}")
        saved_count += 1
    return saved_count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fpath = Path(sys.argv[1])
        if fpath.exists():
            items = json.loads(fpath.read_text(encoding="utf-8"))
            n = save_batch(items)
            print(f"Batch saved {n}/{len(items)} items successfully.")
