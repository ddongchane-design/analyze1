import json
import sys
from pathlib import Path

def main():
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    pending_files = sorted(list(Path("data/pending").glob("*.json")))
    batch_files = pending_files[start:start+count]

    print(f"Total pending: {len(pending_files)}")
    print(f"Processing batch from index {start} to {start+len(batch_files)-1} (Count: {len(batch_files)})")
    print("=" * 80)

    items = []
    for idx, f in enumerate(batch_files):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            v = data.get("video", {})
            t = data.get("transcript", "")
            items.append({
                "file": f.name,
                "video": v,
                "transcript": t
            })
            print(f"[{start+idx+1}/{len(pending_files)}] {v.get('id')} | {v.get('channel_name')} | {v.get('title')[:60]} | Len: {len(t)}")
        except Exception as e:
            print(f"Error reading {f}: {e}")

    out_file = Path("scratch") / f"batch_input_{start}_{start+len(batch_files)}.json"
    out_file.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved batch input to {out_file}")

if __name__ == "__main__":
    main()
