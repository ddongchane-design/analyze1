import json
from pathlib import Path

condensed_path = Path("scratch/condensed_transcripts.json")
if condensed_path.exists():
    data = json.loads(condensed_path.read_text(encoding="utf-8"))
    print(f"Total items: {len(data)}")
    if len(data) > 0:
        first_item = data[0]
        print(f"First item keys: {list(first_item.keys())}")
        if isinstance(first_item, dict):
            # Print a few examples
            for i, (k, v) in enumerate(data.items() if isinstance(data, dict) else enumerate(data)):
                # If data is list of dicts, or dict of dicts
                if isinstance(data, dict):
                    print(f"{i}: key={k}, title={v.get('video', {}).get('title', 'N/A')}")
                else:
                    print(f"{i}: id={v.get('id', 'N/A')}, title={v.get('title', 'N/A')}")
        else:
            print("First item is not a dict")
else:
    print("Not found")
