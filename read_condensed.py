import json
import sys
from pathlib import Path

def main():
    start = 0
    end = 5
    if len(sys.argv) > 2:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
        except ValueError:
            pass

    json_path = Path("scratch/condensed_transcripts.json")
    if not json_path.exists():
        print("condensed_transcripts.json not found.")
        return

    data = json.loads(json_path.read_text(encoding="utf-8"))
    total = len(data)
    
    out_lines = []
    out_lines.append(f"Total entries: {total}. Printing from index {start} to {end-1}:")
    out_lines.append("=" * 80)
    
    for idx in range(start, min(end, total)):
        item = data[idx]
        out_lines.append(f"INDEX: {idx}")
        out_lines.append(f"ID: {item['id']}")
        out_lines.append(f"TITLE: {item['title']}")
        out_lines.append(f"CHANNEL: {item['channel_name']}")
        out_lines.append(f"PUBLISHED: {item['published']}")
        out_lines.append("-" * 40)
        
        text = item['condensed_transcript']
        # Print in wrapped lines
        for i in range(0, len(text), 100):
            out_lines.append(text[i:i+100])
        out_lines.append("=" * 80)
        
    out_path = Path("scratch/readable.txt")
    out_path.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Wrote readable output to {out_path}")

if __name__ == "__main__":
    main()
