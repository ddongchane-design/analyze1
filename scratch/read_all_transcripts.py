import os
import json

pending_dir = "data/pending"
files = sorted([f for f in os.listdir(pending_dir) if f.endswith(".json")])

analyses = []

for f in files:
    path = os.path.join(pending_dir, f)
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    v = data.get("video", {})
    t = data.get("transcript", "")
    v_id = v.get("id")
    title = v.get("title")
    channel = v.get("channel_name")
    
    print(f"ID: {v_id} | Title: {title} | Channel: {channel}")
