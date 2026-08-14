import glob
import json
import os

files = glob.glob('data/pending/*.json')
print(f"TOTAL PENDING: {len(files)}")
for i, f in enumerate(sorted(files)):
    with open(f, encoding='utf-8') as fp:
        d = json.load(fp)
        v = d['video']
        t = d.get('transcript_text', '')
        print(f"{i+1:2d}. [{v['id']}] {v['title']} ({v['channel_name']}) | text length: {len(t)}")
