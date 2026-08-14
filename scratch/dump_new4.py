import json, sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_dir = Path("data/pending")
files = sorted(list(pending_dir.glob("*.json")))

out = []
for idx, f in enumerate(files):
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        clean_t = " ".join(transcript.split())
        out.append({
            "idx": idx,
            "id": video.get("id"),
            "title": video.get("title"),
            "channel_name": video.get("channel_name"),
            "published": video.get("published"),
            "url": video.get("url"),
            "thumbnail": video.get("thumbnail"),
            "t_len": len(clean_t),
            "transcript_sample": clean_t[:3000]
        })
    except Exception as e:
        print(f"Error {f}: {e}")

Path("scratch/pending_new4_dump.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Dumped {len(out)} new files to scratch/pending_new4_dump.json")
