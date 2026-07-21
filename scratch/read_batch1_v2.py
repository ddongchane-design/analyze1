import json
import re
from pathlib import Path

def clean_transcript(text):
    # Insert newlines before ">>" or similar markers to make it readable
    cleaned = text.replace(">>", "\n>>").replace("[음악]", "\n[음악]\n").replace("[웃음]", "\n[웃음]\n")
    # Replace multiple newlines
    cleaned = re.sub(r'\n+', '\n', cleaned)
    return cleaned

def main():
    video_ids = ["-ADB_o6C2ig", "-LUnTYx_xAA", "08Lrl4ijgS4", "1Q2XkHeNrIk", "95_M8-DYUA8", "9fRankiszG4", "AbBJl3_G_s4"]
    output_path = Path("scratch/batch1_readable.txt")
    
    with output_path.open("w", encoding="utf-8") as out:
        for vid in video_ids:
            p_file = Path(f"data/pending/{vid}.json")
            if not p_file.exists():
                out.write(f"File for {vid} not found.\n\n")
                continue
            
            try:
                data = json.loads(p_file.read_text(encoding="utf-8"))
                video = data.get("video", {})
                transcript = data.get("transcript", "")
                cleaned = clean_transcript(transcript)
                
                out.write(f"=== VIDEO_ID: {vid} ===\n")
                out.write(f"Title: {video.get('title')}\n")
                out.write(f"Channel: {video.get('channel_name')}\n")
                out.write(f"Published: {video.get('published')}\n")
                out.write("Transcript:\n")
                out.write(cleaned[:8000] + "\n")
                if len(cleaned) > 8000:
                    out.write(f"... [TRUNCATED, TOTAL LENGTH {len(cleaned)}]\n")
                out.write("=" * 60 + "\n\n")
            except Exception as e:
                out.write(f"Error reading {vid}: {e}\n\n")
                
    print("Done writing to scratch/batch1_readable.txt")

if __name__ == "__main__":
    main()
