import glob
import json
import os

files = glob.glob('data/pending/*.json')
print(f"Total files: {len(files)}")
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            title = data['video']['title']
            transcript = data.get('transcript', '')
            transcript_len = len(transcript)
            print(f"{os.path.basename(f)}: len={transcript_len} | Title: {title}")
    except Exception as e:
        print(f"Error {f}: {e}")
