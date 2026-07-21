import json
from pathlib import Path
vids = ["-ADB_o6C2ig", "-LUnTYx_xAA", "08Lrl4ijgS4", "1Q2XkHeNrIk", "95_M8-DYUA8", "9fRankiszG4", "AbBJl3_G_s4"]
for vid in vids:
    p = Path(f"data/pending/{vid}.json")
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        print(f"{vid}: parsed successfully, keys={list(data.keys())}")
    except Exception as e:
        print(f"{vid}: failed to parse: {e}")
