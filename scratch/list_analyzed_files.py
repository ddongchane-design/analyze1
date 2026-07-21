import json
from pathlib import Path

def main():
    analyzed_dir = Path("data/analyzed")
    out_path = Path("scratch/list_analyzed_files_output.txt")
    
    with open(out_path, "w", encoding="utf-8") as out_file:
        for topic_folder in sorted(list(analyzed_dir.iterdir())):
            if topic_folder.is_dir():
                files = list(topic_folder.glob("*.json"))
                out_file.write(f"=== Topic: {topic_folder.name} ({len(files)} files) ===\n")
                entries = []
                for f in files:
                    try:
                        data = json.loads(f.read_text(encoding="utf-8"))
                        video = data.get("video", {})
                        entries.append((video.get("published", ""), video.get("title", ""), f.name))
                    except Exception as e:
                        out_file.write(f"  Error reading {f.name}: {e}\n")
                entries.sort(reverse=True)
                for pub, title, name in entries[:10]:
                    out_file.write(f"  [{pub[:10]}] {name} - {title}\n")
                out_file.write("\n")
                
    print(f"Wrote list to {out_path}")

if __name__ == "__main__":
    main()
