import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

path = Path("data/pending/gKc4ZH2rjFk.json")
data = json.loads(path.read_text(encoding="utf-8"))
transcript = data["transcript"]

print("Title:", data["video"]["title"])
print("Transcript snippet:")
print(transcript[:3000])

print("\nKeywords summary:")
# Find occurrences of key terms and print matching sentences
import re
sentences = re.split(r'[.!?\n]', transcript)
keywords = ["반대매매", "미수", "소부장", "현대일렉트릭", "금리"]
for kw in keywords:
    print(f"\n--- Matches for {kw} ---")
    count = 0
    for s in sentences:
        if kw in s:
            print("- ", s.strip())
            count += 1
            if count >= 3:
                break
