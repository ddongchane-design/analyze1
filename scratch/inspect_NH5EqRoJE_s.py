import json
from pathlib import Path

def main():
    path = Path("data/pending/NH5EqRoJE_s.json")
    if not path.exists():
        print("File does not exist")
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    video = data.get("video", {})
    transcript = data.get("transcript", "")
    
    out_path = Path("scratch/NH5EqRoJE_s_info_utf8.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"Title: {video.get('title')}\n")
        f.write(f"Channel: {video.get('channel_name')}\n")
        f.write(f"Transcript Length: {len(transcript)} chars\n")
        f.write(f"Start of Transcript (first 2500 chars):\n")
        f.write(transcript[:2500])
        f.write("\n...\n")
        f.write(f"End of Transcript (last 2500 chars):\n")
        f.write(transcript[-2500:])
        
    print("Wrote to scratch/NH5EqRoJE_s_info_utf8.txt")

if __name__ == "__main__":
    main()
