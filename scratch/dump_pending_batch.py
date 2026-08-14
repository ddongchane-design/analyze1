import glob
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('data/pending/*.json'))

batch_num = int(sys.argv[1]) if len(sys.argv) > 1 else 1
start_idx = (batch_num - 1) * 6
end_idx = min(start_idx + 6, len(files))

print(f"=== BATCH {batch_num} (Files {start_idx+1} to {end_idx}) ===")
for f in files[start_idx:end_idx]:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
        v = d.get('video', {})
        t = d.get('transcript', '')
        print(f"\nFILE: {os.path.basename(f)}")
        print(f"TITLE: {v.get('title')}")
        print(f"CHANNEL: {v.get('channel_name')}")
        print(f"TRANSCRIPT SNIPPET (first 1000 chars):\n{t[:1000]}")
        print("-" * 60)
