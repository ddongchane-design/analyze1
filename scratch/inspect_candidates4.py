import json
from pathlib import Path
import textwrap
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def dump_video_details(video_id):
    f_path = Path(f"data/pending/{video_id}.json")
    if not f_path.exists():
        print(f"{video_id}.json not found")
        return
    
    data = json.loads(f_path.read_text(encoding="utf-8"))
    video = data["video"]
    transcript = data.get("transcript", "")
    
    print(f"\n======================================")
    print(f"ID: {video_id}")
    print(f"TITLE: {video.get('title')}")
    print(f"CHANNEL: {video.get('channel_name')}")
    print(f"LENGTH: {len(transcript)} chars")
    
    if len(transcript) < 3000:
        print("TRANSCRIPT:")
        print(textwrap.fill(transcript, width=80))
    else:
        out_file = Path(f"scratch/details_{video_id}.txt")
        wrapped = textwrap.fill(transcript, width=80)
        out_file.write_text(f"TITLE: {video.get('title')}\n\nTRANSCRIPT:\n{wrapped}", encoding="utf-8")
        print(f"Transcript is long. Dumped to {out_file}")

ids = ["NDiyXbv_CZM", "NfCq0lC5n5Q", "OP6FjNHfxl4", "QMyEr0KQDbc", "rQBWsbxYl10", "TtLOy4-DhNo"]
for vid in ids:
    dump_video_details(vid)
