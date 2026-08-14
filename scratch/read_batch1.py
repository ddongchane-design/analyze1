import json
from pathlib import Path

files = ['-f9_GdxWYDQ.json', '0ROiLgR4CUo.json', '1EXYsVlV1Rc.json', '4XKllfAhgX8.json', '6yvEpoWQ6Fk.json']

for f in files:
    path = Path("data/pending") / f
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        print(f"=== {f} | {data['video']['channel_name']} | {data['video']['title']} ===")
        print(data['transcript'][:1500])
        print("\n" + "="*50 + "\n")
