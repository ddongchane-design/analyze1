import json
import sys
from pathlib import Path

# Set stdout to UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

KEYWORDS = ["조선", "해양", "해운", "잠수함", "한화오션", "현대중공업", "삼성중공업", "조선소", "선박", "유조선", "운임", "HMM", "FLNG", "신조선가"]

def match_text(text):
    if not text:
        return False
    return any(kw in text for kw in KEYWORDS)

def main():
    analyzed_dir = Path("data/analyzed")
    all_files = list(analyzed_dir.glob("**/*.json"))
    
    matches = []
    
    for filepath in all_files:
        if filepath.parent.name == "shipbuilding":
            continue
        try:
            data = json.loads(filepath.read_text(encoding="utf-8"))
            video = data.get("video", {})
            title = video.get("title", "")
            analysis = data.get("analysis", {})
            summary = analysis.get("summary", "")
            key_claims = " ".join(analysis.get("key_claims", []))
            tags = " ".join(data.get("classification", {}).get("tags", []))
            
            combined_text = f"{title} {summary} {key_claims} {tags}"
            if match_text(combined_text):
                matches.append((filepath, title))
        except Exception as e:
            print(f"Error reading {filepath.name}: {e}")
            
    print(f"Total matching files found: {len(matches)}")
    for idx, (filepath, title) in enumerate(matches):
        print(f"{idx+1:02d}. [{filepath.parent.name}] {filepath.name} | {title}")

if __name__ == "__main__":
    main()
