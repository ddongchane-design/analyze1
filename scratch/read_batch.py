import json, sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

data = json.loads(Path("scratch/pending_dump.json").read_text(encoding="utf-8"))

start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
end = int(sys.argv[2]) if len(sys.argv) > 2 else 5

for item in data[start:end]:
    print(f"=== [{item['idx']}] {item['id']} | {item['title']} ({item['channel_name']}) ===")
    print(f"URL: {item['url']}")
    print(f"TRANSCRIPT SAMPLE (first 2500 chars):\n{item['transcript_sample'][:2500]}\n")
