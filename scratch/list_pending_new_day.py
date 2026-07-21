import json
from pathlib import Path

def main():
    pending_dir = Path("data/pending")
    files = list(pending_dir.glob("*.json"))
    print(f"Total pending files: {len(files)}")
    
    records = []
    for fpath in files:
        try:
            data = json.loads(fpath.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            records.append({
                "file_name": fpath.name,
                "video_id": fpath.stem,
                "title": video.get("title", ""),
                "channel_name": video.get("channel_name", ""),
                "published": video.get("published", ""),
                "transcript_len": len(transcript)
            })
        except Exception as e:
            print(f"Error reading {fpath.name}: {e}")
            
    # Sort by published date descending
    records.sort(key=lambda x: x["published"], reverse=True)
    
    out_path = Path("scratch/pending_new_day.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"Total Pending: {len(records)}\n\n")
        for i, r in enumerate(records, 1):
            f.write(f"{i}. [{r['video_id']}] {r['title']}\n")
            f.write(f"   Channel: {r['channel_name']} | Published: {r['published']} | Len: {r['transcript_len']} chars | File: {r['file_name']}\n\n")
            
    print(f"Wrote {len(records)} records to scratch/pending_new_day.txt")

if __name__ == "__main__":
    main()
