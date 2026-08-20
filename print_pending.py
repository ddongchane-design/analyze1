import glob
import json
import sys

# Set stdout to utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

files = glob.glob('data/pending/*.json')
print(f"Total pending files: {len(files)}")
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            video = data['video']
            print(f"File: {f}")
            print(f"  Title: {video['title']}")
            print(f"  Channel: {video['channel_name']}")
            print(f"  Published: {video['published']}")
            print("-" * 50)
    except Exception as e:
        print(f"Error reading {f}: {e}")
