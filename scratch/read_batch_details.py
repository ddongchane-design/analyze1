import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    start_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    pending_files = sorted(list(Path("data/pending").glob("*.json")))
    target_files = pending_files[start_idx:start_idx+count]

    out_lines = []
    out_lines.append(f"=== BATCH DETAILS (Index {start_idx} to {start_idx+len(target_files)-1}) ===")
    for i, f in enumerate(target_files):
        data = json.loads(f.read_text(encoding="utf-8"))
        v = data.get("video", {})
        t = data.get("transcript", "")
        out_lines.append(f"\n--- ITEM {start_idx+i+1}/{len(pending_files)} ({f.name}) ---")
        out_lines.append(f"ID: {v.get('id')}")
        out_lines.append(f"Title: {v.get('title')}")
        out_lines.append(f"Channel: {v.get('channel_name')}")
        out_lines.append(f"Published: {v.get('published')}")
        out_lines.append(f"URL: {v.get('url')}")
        out_lines.append(f"Thumbnail: {v.get('thumbnail')}")
        out_lines.append(f"Transcript Snippet (First 1500 chars):\n{t[:1500]}")
        out_lines.append("="*60)

    res_text = "\n".join(out_lines)
    Path("scratch/batch_view.txt").write_text(res_text, encoding="utf-8")
    print(res_text)

if __name__ == "__main__":
    main()
