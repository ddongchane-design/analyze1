import glob
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('data/pending/*.json'))
print(f'Total pending files: {len(files)}')

batch_size = 6
for b_idx in range(0, len(files), batch_size):
    batch = files[b_idx:b_idx+batch_size]
    print(f"\n{'='*20} BATCH {b_idx//batch_size + 1} (Files {b_idx+1}~{b_idx+len(batch)}) {'='*20}")
    for f in batch:
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        vid = d['video']['id']
        title = d['video']['title']
        ch = d['video'].get('channel_name', '')
        pub = d['video'].get('published', '')
        t_len = len(d.get('transcript', ''))
        print(f"[{vid}] ({ch}) {title} | Pub: {pub} | Transcript: {t_len} chars")
