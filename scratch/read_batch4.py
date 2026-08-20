import json

def get_transcript(vid):
    with open(f'data/pending/{vid}.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
        return d.get('transcript', '')

vids_batch4 = ['Q_VGQa7wK3M', 'Tln76jprMiE', 'tyq4GT_2rGg', 'wEigQQsC_ok', 'WzEcPznO5f4', 'xR5BqDcw5D0', 'yxSBpqS1pSI']
with open('scratch/batch4_transcripts.txt', 'w', encoding='utf-8') as out:
    for vid in vids_batch4:
        t = get_transcript(vid)
        out.write(f"=== VID: {vid} (len: {len(t)}) ===\n")
        out.write(t[:12000] + "\n\n")

print("Saved batch4 transcripts.")
