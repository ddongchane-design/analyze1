import json
from pathlib import Path

def main():
    summary_path = Path("scratch/analyzed_summary.json")
    if not summary_path.exists():
        print("Summary path does not exist")
        return
    
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    
    out_path = Path("scratch/recent_summaries_utf8.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        # Let's inspect the files with published dates >= 2026-07-15
        for topic, videos in summary.items():
            f.write(f"\n========================================\nTOPIC: {topic}\n========================================\n")
            recent_videos = []
            for v in videos:
                pub = v.get("published", "")
                if pub >= "2026-07-15":
                    recent_videos.append(v)
            
            # Sort by published date desc
            recent_videos.sort(key=lambda x: x.get("published", ""), reverse=True)
            
            for rv in recent_videos:
                f.write(f"- {rv['published'][:10]} | {rv['id']} | {rv['title']} ({rv['signal']})\n")
                f.write(f"  Summary: {rv['summary']}\n")
    
    print("Wrote to scratch/recent_summaries_utf8.txt")

if __name__ == "__main__":
    main()
