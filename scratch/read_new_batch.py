import sys
import json
from pathlib import Path

# Prevent UnicodeEncodeError on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    pending_dir = Path("data/pending")
    files = list(pending_dir.glob("*.json"))
    
    metadata_list = []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            video = data.get("video", {})
            metadata_list.append({
                "file_name": f.name,
                "id": video.get("id"),
                "title": video.get("title"),
                "channel": video.get("channel_name"),
                "published": video.get("published"),
                "transcript_len": len(data.get("transcript", ""))
            })
        except Exception as e:
            print(f"Error reading {f.name}: {e}")
            
    # Sort by published date descending
    metadata_list.sort(key=lambda x: x["published"] or "", reverse=True)
    
    print(f"Total pending files found: {len(metadata_list)}")
    print("-" * 100)
    for idx, meta in enumerate(metadata_list):
        # Clean title to prevent printing crashes
        clean_title = meta['title'].replace('\u2026', '...').replace('\u22ef', '...')
        print(f"{idx+1:02d} | Channel: {meta['channel']:<25} | Date: {meta['published'][:10]} | Title: {clean_title} ({meta['file_name']})")

if __name__ == "__main__":
    main()
