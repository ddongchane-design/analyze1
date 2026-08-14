import json, sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

data = json.loads(Path("scratch/pending_dump.json").read_text(encoding="utf-8"))

idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0

item = data[idx]
print(f"=== [{item['idx']}] {item['id']} | {item['title']} ({item['channel_name']}) ===")
print(f"URL: {item['url']}")
print(f"PUBLISHED: {item['published']}")
print(f"TRANSCRIPT:\n{item['transcript_sample']}")
