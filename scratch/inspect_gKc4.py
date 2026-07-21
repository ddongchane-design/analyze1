import json
from pathlib import Path

path = Path("data/pending/gKc4ZH2rjFk.json")
data = json.loads(path.read_text(encoding="utf-8"))
print("Title:", data["video"]["title"])
transcript = data["transcript"]
print("Transcript Length:", len(transcript))

# Print first 2000 characters
print("\n--- FIRST 2000 CHARS ---")
print(transcript[:2000])

# Print some sections in the middle or search for keywords
print("\n--- KEYWORD SEARCHES ---")
keywords = ["반대매매", "신용", "미수", "반도체", "금리", "유가", "스페이스"]
for kw in keywords:
    matches = [m.start() for m in re.finditer(kw, transcript)] if 're' in globals() else []
    # Let's import re inside or just search simple
    import re
    matches = [m.start() for m in re.finditer(kw, transcript)]
    print(f"Keyword '{kw}' found {len(matches)} times. First few matches:")
    for idx in matches[:3]:
        start = max(0, idx - 100)
        end = min(len(transcript), idx + 150)
        print(f"[{idx}]: ... {transcript[start:end]} ...")
        print("-" * 40)
