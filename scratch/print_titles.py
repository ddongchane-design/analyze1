import json
import glob
import textwrap
import sys

with open('scratch/titles_output.txt', 'w', encoding='utf-8') as out:
    for f in glob.glob('data/pending/*.json'):
        try:
            with open(f, encoding='utf-8') as file:
                data = json.load(file)
                title = data.get('video', {}).get('title', '')
                text = data.get('text', '')
                short_text = textwrap.shorten(text, width=400, placeholder='...')
                out.write(f"--- {f} ---\n")
                out.write(f"Title: {title}\n")
                out.write(f"Text: {short_text}\n\n")
        except Exception as e:
            out.write(f"Error reading {f}: {e}\n")
