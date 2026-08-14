import glob
import json
import os
from pathlib import Path

def dump_all():
    out_dir = Path("scratch/pending_details")
    out_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(glob.glob("data/pending/*.json"))
    print(f"Dumping details for {len(files)} files...")

    summary_list = []

    for idx, fpath in enumerate(files):
        p = Path(fpath)
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            video = data.get("video", {})
            vid_id = video.get("id", p.stem)
            title = video.get("title", "")
            channel = video.get("channel_name", "")
            transcript = video.get("transcript", "")
            
            detail = {
                "index": idx + 1,
                "file": p.name,
                "id": vid_id,
                "title": title,
                "channel": channel,
                "published": video.get("published"),
                "transcript_len": len(transcript),
                "transcript_snippet": transcript[:1500] if transcript else ""
            }
            summary_list.append(detail)
            
            # Write individual summary txt for easy viewing if needed
            (out_dir / f"{idx+1:02d}_{vid_id}.txt").write_text(
                f"Title: {title}\nChannel: {channel}\nID: {vid_id}\n\nTRANSCRIPT:\n{transcript[:4000]}\n",
                encoding="utf-8"
            )
        except Exception as e:
            print(f"Error processing {p.name}: {e}")

    Path("scratch/pending_details_summary.json").write_text(
        json.dumps(summary_list, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print("Done dumping pending details.")

if __name__ == "__main__":
    dump_all()
