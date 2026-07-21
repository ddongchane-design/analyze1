import json
import os
from pathlib import Path

# Set stdout to UTF-8
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

TARGET_FILES = [
    "economy/gVxoj-o14Kk.json",
    "etc/2LA-WYN3U4Y.json",
    "etc/YHDfkArYGpA.json",
    "etc/YL9tGdB9UvE.json",
    "stock/bz5SAPymEgQ.json",
    "stock/kDZVAHZBB50.json",
    "stock/LrNICf6ok3s.json",
    "stock/q-zONq9JzNA.json",
    "stock/wieaUTwTpiY.json",
    "tech/TA1U6vnjBUE.json"
]

def main():
    base_dir = Path("data/analyzed")
    dest_dir = base_dir / "shipbuilding"
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    moved_count = 0
    
    for rel_path in TARGET_FILES:
        src_path = base_dir / rel_path
        if not src_path.exists():
            print(f"File not found: {src_path}")
            continue
            
        try:
            data = json.loads(src_path.read_text(encoding="utf-8"))
            
            # Update classification
            classification = data.setdefault("classification", {})
            old_primary = classification.get("primary_topic")
            
            classification["primary_topic"] = "shipbuilding"
            
            secondary_topics = classification.setdefault("secondary_topics", [])
            if old_primary and old_primary != "shipbuilding" and old_primary not in secondary_topics:
                secondary_topics.append(old_primary)
                
            # Write to new path
            dest_path = dest_dir / src_path.name
            dest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            
            # Remove old file
            src_path.unlink()
            
            print(f"Moved {src_path.name}: {old_primary} -> shipbuilding")
            moved_count += 1
        except Exception as e:
            print(f"Failed to move {src_path.name}: {e}")
            
    print(f"Successfully moved {moved_count} files to shipbuilding.")

if __name__ == "__main__":
    main()
