import json, sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

data = json.loads(Path("scratch/pending_final4_dump.json").read_text(encoding="utf-8"))
for idx, d in enumerate(data):
    print(f"[{idx}] ID: {d['id']}")
    print(f"    TITLE: {d['title']}")
    print(f"    CHANNEL: {d['channel_name']}")
    print(f"    PUBLISHED: {d['published']}")
    print(f"    SAMPLE: {d['transcript_sample'][:1500]}")
    print("=" * 60)
