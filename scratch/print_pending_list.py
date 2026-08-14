import glob
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('data/pending/*.json'))
print(f"Total pending files count: {len(files)}")

for i, f in enumerate(files, 1):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            v = data.get('video', {})
            print(f"[{i:02d}] {os.path.basename(f)} | {v.get('channel_name', 'Unknown')} | {v.get('title', 'No Title')}")
    except Exception as e:
        print(f"[{i:02d}] {os.path.basename(f)} | Error reading: {e}")
