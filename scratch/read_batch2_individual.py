import json
import re
from pathlib import Path

def clean_transcript(text):
    cleaned = text.replace(">>", "\n>>").replace("[음악]", "\n[음악]\n").replace("[웃음]", "\n[웃음]\n")
    cleaned = re.sub(r'\n+', '\n', cleaned)
    return cleaned

def main():
    video_ids = ["Ctsa5j5TlAA", "DfgXcw2a5Pg", "Dmgc7OfFjNM", "ETtzfE6XJhE", "HFAspbOn2T8", "JF6oUUk1JZE", "Lbt7aPJCpGk"]
    
    for vid in video_ids:
        p_file = Path(f"data/pending/{vid}.json")
        if not p_file.exists():
            print(f"{vid}: not found")
            continue
            
        try:
            data = json.loads(p_file.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            cleaned = clean_transcript(transcript)
            
            output_path = Path(f"scratch/details_{vid}.txt")
            with output_path.open("w", encoding="utf-8") as out:
                out.write(f"Title: {video.get('title')}\n")
                out.write(f"Channel: {video.get('channel_name')}\n")
                out.write(f"Published: {video.get('published')}\n")
                out.write(f"Transcript Length: {len(cleaned)}\n\n")
                out.write("Transcript:\n")
                out.write(cleaned + "\n")
            print(f"Wrote scratch/details_{vid}.txt")
        except Exception as e:
            print(f"Error {vid}: {e}")

if __name__ == "__main__":
    main()
