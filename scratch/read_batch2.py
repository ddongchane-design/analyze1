import json

def get_transcript(vid):
    with open(f'data/pending/{vid}.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
        return d.get('transcript', '')

vids_batch2 = ['e76johEpuZw', 'G0pXO-S0Es4', 'gEWbNlpKDHY', 'hkFObxd1RJw', 'HxwIonJ2nyw', 'juzmEaBrrM4', 'Jyumom1L6z4']
with open('scratch/batch2_transcripts.txt', 'w', encoding='utf-8') as out:
    for vid in vids_batch2:
        t = get_transcript(vid)
        out.write(f"=== VID: {vid} (len: {len(t)}) ===\n")
        out.write(t[:10000] + "\n\n")

print("Saved batch2 transcripts.")
