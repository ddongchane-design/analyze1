import json
from pathlib import Path

def main():
    pending_dir = Path("data/pending")
    files = list(pending_dir.glob("*.json"))
    
    videos = []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            video = data.get("video", {})
            videos.append({
                "id": f.stem,
                "title": video.get("title"),
                "channel": video.get("channel_name"),
                "published": video.get("published"),
                "transcript_len": len(data.get("transcript", ""))
            })
        except Exception as e:
            print(f"Error reading {f.name}: {e}")
            
    # Sort by published date asc (oldest first)
    videos.sort(key=lambda x: x.get("published", ""))
    
    out_path = Path("scratch/pending_new_day_utf8.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"Total pending files: {len(files)}\n")
        for idx, v in enumerate(videos):
            f.write(f"{idx+1:2d} | {v['published'][:10]} | {v['channel'][:15]} | {v['id']} | {v['title']} ({v['transcript_len']} chars)\n")
            
    print("Wrote list to scratch/pending_new_day_utf8.txt")

if __name__ == "__main__":
    main()
