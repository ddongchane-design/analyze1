import json
from pathlib import Path
vids = ["Ctsa5j5TlAA", "DfgXcw2a5Pg", "Dmgc7OfFjNM", "ETtzfE6XJhE", "HFAspbOn2T8", "JF6oUUk1JZE", "Lbt7aPJCpGk"]
for vid in vids:
    p = Path(f"data/pending/{vid}.json")
    if not p.exists():
        print(f"{vid}: does not exist")
        continue
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        title = data.get("video", {}).get("title")
        trans_len = len(data.get("transcript", ""))
        print(f"{vid}: title='{title}', trans_len={trans_len}")
    except Exception as e:
        print(f"{vid}: error {e}")
