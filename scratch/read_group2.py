import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

filenames = ["gxt3mYJ-Apk.json", "MMKadJnKziE.json", "mv-rVXNIiTo.json", "NhV39Nh0beE.json"]

for filename in filenames:
    filepath = Path("data/pending") / filename
    if filepath.exists():
        data = json.loads(filepath.read_text(encoding="utf-8"))
        print(f"TITLE: {data['video']['title']}")
        print(f"CHANNEL: {data['video']['channel_name']}")
        print(f"TRANSCRIPT LENGTH: {len(data['transcript'])}")
        print("-" * 50)
        print(data['transcript'][:2000])
        print("=" * 80)
