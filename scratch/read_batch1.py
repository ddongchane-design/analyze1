import json

def get_transcript(vid):
    with open(f'data/pending/{vid}.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
        return d.get('transcript', '')

# Extract summaries/key parts for batch 1
vids_batch1 = ['0N4PGfhGkV4', '4ZDjjLjfAE4', '503NEYQ6xXo', '9BKjJN7Giog', 'aQ0z5VcNEvU', 'CH1FrANSxgU', 'dHP6_zOmBFk']
with open('scratch/batch1_transcripts.txt', 'w', encoding='utf-8') as out:
    for vid in vids_batch1:
        t = get_transcript(vid)
        out.write(f"=== VID: {vid} (len: {len(t)}) ===\n")
        out.write(t[:10000] + "\n\n")

print("Saved batch1 transcripts.")
