import json
import glob
import sys

def inspect_range(start_idx, end_idx):
    files = sorted(glob.glob('data/pending/*.json'))
    for i in range(start_idx, min(end_idx, len(files))):
        f = files[i]
        with open(f, encoding='utf-8') as fp:
            d = json.load(fp)
            v = d['video']
            t = d.get('transcript_text', d.get('transcript', ''))
            print(f"=== [{i+1}] {v['id']} : {v['title']} ({v['channel_name']}) ===")
            print(f"Transcript length: {len(t)}")
            print(f"Sample transcript (first 600 chars):\n{t[:600]}\n")

if __name__ == '__main__':
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    e = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    inspect_range(s, e)
