import json, sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

data = json.loads(Path("scratch/pending_new4_dump.json").read_text(encoding="utf-8"))

for d in data:
    print(f"=== [{d['idx']}] {d['id']} | {d['title']} ({d['channel_name']}) ===")
    print(f"URL: {d['url']}")
    print(f"PUBLISHED: {d['published']}")
    print(f"SAMPLE:\n{d['transcript_sample'][:1500]}\n" + "-"*50)
