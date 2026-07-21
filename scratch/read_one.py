import json
import sys
from pathlib import Path

# Set output to utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def print_file_details(filename):
    f_path = Path(f"data/pending/{filename}")
    if not f_path.exists():
        print(f"{filename} not found")
        return
    data = json.loads(f_path.read_text(encoding="utf-8"))
    print(f"\n======================================")
    print(f"FILE: {filename}")
    print(f"TITLE: {data['video'].get('title')}")
    print(f"CHANNEL: {data['video'].get('channel_name')}")
    print(f"TRANSCRIPT:\n{data.get('transcript', '')}")

for f in ["Az9LBgm3_h0.json", "BLvI5dBN8Ws.json", "boq4Dn4H238.json"]:
    print_file_details(f)
