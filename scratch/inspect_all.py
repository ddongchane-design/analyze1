import glob
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def inspect_all():
    files = sorted(glob.glob("data/pending/*.json"))
    print(f"Total pending: {len(files)}")
    for idx, fpath in enumerate(files):
        data = json.loads(Path(fpath).read_text(encoding="utf-8"))
        video = data.get("video", {})
        transcript = data.get("transcript", "") or video.get("transcript", "")
        vid = video.get("id")
        title = video.get("title")
        channel = video.get("channel_name")
        pub = video.get("published")
        t_len = len(transcript)
        print(f"[{idx+1:02d}] ID: {vid} | Topic candidate? | Channel: {channel}")
        print(f"     Title: {title}")
        print(f"     Transcript length: {t_len} chars")

if __name__ == "__main__":
    inspect_all()
