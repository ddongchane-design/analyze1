import glob
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('data/pending/*.json'))

def dump_files(indices):
    for idx in indices:
        if idx < len(files):
            f = files[idx]
            with open(f, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
                v = d.get('video', {})
                t = d.get('transcript', '')
                print(f"=== INDEX {idx+1}: {os.path.basename(f)} ===")
                print(f"Title: {v.get('title')}")
                print(f"Channel: {v.get('channel_name')}")
                print(f"Published: {v.get('published')}")
                print(f"Transcript length: {len(t)}")
                print(f"Full/Key Text Snippet:\n{t[:4000]}\n")
                print("="*60)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        idxs = [int(x)-1 for x in sys.argv[1:]]
        dump_files(idxs)
