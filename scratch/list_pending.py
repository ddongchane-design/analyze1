import os
import json
import glob

pending_files = glob.glob('data/pending/*.json')
print(f"Total pending files: {len(pending_files)}")
items = []
for p in pending_files:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
            v = d.get('video', {})
            t = d.get('transcript', '')
            items.append({
                'file': p,
                'id': v.get('id', os.path.splitext(os.path.basename(p))[0]),
                'title': v.get('title', ''),
                'channel': v.get('channel_name', ''),
                'published': v.get('published', ''),
                'transcript_len': len(t)
            })
    except Exception as e:
        print(f"Error reading {p}: {e}")

for i, item in enumerate(items, 1):
    print(f"[{i:02d}] {item['id']} | {item['channel']} | {item['title'][:40]}... (len: {item['transcript_len']})")
