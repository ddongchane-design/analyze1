import json
import glob

files = sorted(glob.glob('data/pending/*.json'))[:6]
for i, f in enumerate(files):
    with open(f, encoding='utf-8') as fp:
        d = json.load(fp)
        v = d['video']
        t = d.get('transcript_text', d.get('transcript', ''))
        print(f"=== [{i+1}] {v['id']} : {v['title']} ===")
        print(f"Channel: {v['channel_name']}, Published: {v['published']}")
        print(f"Transcript length: {len(t)}")
        print(f"First 300 chars: {t[:300]}")
        print(f"Last 300 chars: {t[-300:]}\n")
