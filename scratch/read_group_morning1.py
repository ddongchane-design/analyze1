import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

filenames = ["8po_Mp0QPxs.json", "_Z9FMacSwbE.json", "aoMNqAoPYTw.json", "bgZr7iwWAVA.json"]

for filename in filenames:
    filepath = Path("data/pending") / filename
    if filepath.exists():
        data = json.loads(filepath.read_text(encoding="utf-8"))
        print(f"TITLE: {data['video']['title']}")
        print(f"CHANNEL: {data['video']['channel_name']}")
        print(f"TRANSCRIPT LENGTH: {len(data['transcript'])}")
        print("-" * 50)
        print(data['transcript'][:2500])
        print("=" * 80)
