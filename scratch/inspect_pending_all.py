import json
import glob
from pathlib import Path

def main():
    pending_files = sorted(glob.glob("data/pending/*.json"))
    print(f"Total pending files: {len(pending_files)}")
    
    res = []
    for idx, fpath in enumerate(pending_files):
        p = Path(fpath)
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            v = data.get("video", {})
            t = data.get("transcript", "")
            res.append({
                "index": idx,
                "file": p.name,
                "id": v.get("id"),
                "title": v.get("title"),
                "channel": v.get("channel_name"),
                "published": v.get("published"),
                "t_len": len(t)
            })
        except Exception as e:
            print(f"Error {p.name}: {e}")

    # Output list as json for easy reading
    out_p = Path("scratch/pending_list.json")
    out_p.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved list of {len(res)} items to scratch/pending_list.json")

if __name__ == "__main__":
    main()
