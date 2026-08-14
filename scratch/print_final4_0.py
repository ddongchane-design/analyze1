import json, sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

data = json.loads(Path("scratch/pending_final4_dump.json").read_text(encoding="utf-8"))
d = data[0]
print(f"ID: {d['id']}")
print(f"TITLE: {d['title']}")
print(f"CHANNEL: {d['channel_name']}")
print(f"SAMPLE:\n{d['transcript_sample'][:1000]}")
