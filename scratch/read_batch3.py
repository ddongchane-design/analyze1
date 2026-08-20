import json

def get_transcript(vid):
    with open(f'data/pending/{vid}.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
        return d.get('transcript', '')

vids_batch3 = ['KdG8DbyyAiw', 'LJG-yBkpN_M', 'mynVdWBBU38', 'nF-9JSMUihU', 'nxrLHJE5vXU', 'p3Xsk7ONGPc']
with open('scratch/batch3_transcripts.txt', 'w', encoding='utf-8') as out:
    for vid in vids_batch3:
        t = get_transcript(vid)
        out.write(f"=== VID: {vid} (len: {len(t)}) ===\n")
        out.write(t[:10000] + "\n\n")

print("Saved batch3 transcripts.")
