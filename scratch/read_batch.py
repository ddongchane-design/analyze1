import glob
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def read_batch(batch_num, batch_size=6):
    files = sorted(glob.glob('data/pending/*.json'))
    start = (batch_num - 1) * batch_size
    end = start + batch_size
    batch = files[start:end]
    
    print(f"=== BATCH {batch_num} ({len(batch)} files) ===")
    for idx, f in enumerate(batch):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        v = d['video']
        t = d.get('transcript', '')
        print(f"\n[{idx+1}/{len(batch)}] ID: {v['id']} | Channel: {v.get('channel_name')} | Date: {v.get('published')}")
        print(f"Title: {v.get('title')}")
        print(f"Transcript length: {len(t)}")
        print("--- Transcript Preview (First 2500 chars) ---")
        print(t[:2500])
        print("--- Transcript End Preview (Last 1000 chars) ---")
        print(t[-1000:] if len(t) > 2500 else "")
        print("="*60)

if __name__ == '__main__':
    b = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    read_batch(b)
