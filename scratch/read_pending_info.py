import json
import glob
import os

files = glob.glob('data/pending/*.json')
out_lines = []
out_lines.append(f"Total: {len(files)}")
for idx, f in enumerate(files):
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
        v = data.get('video', {})
        t = data.get('transcript', '')
        out_lines.append("="*60)
        out_lines.append(f"[{idx+1:02d}/{len(files):02d}] ID: {v.get('id')}")
        out_lines.append(f"File: {os.path.basename(f)}")
        out_lines.append(f"Title: {v.get('title')}")
        out_lines.append(f"Channel: {v.get('channel_name')}")
        out_lines.append(f"Published: {v.get('published')}")
        out_lines.append(f"Transcript Length: {len(t)}")
        snippet = t[:400].replace('\n', ' ')
        out_lines.append(f"Snippet: {snippet}...")

with open('scratch/pending_info.txt', 'w', encoding='utf-8') as out_fp:
    out_fp.write('\n'.join(out_lines))

print("Wrote pending info successfully.")
