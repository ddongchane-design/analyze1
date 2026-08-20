import os
import json

pending_dir = "data/pending"
temp_dir = "data/temp"
os.makedirs(temp_dir, exist_ok=True)

files = [
    "Qu1CMZd2-E8.json",
    "SJ30yR9GUTk.json",
    "TA1U6vnjBUE.json",
    "vGFPMw4PFtk.json",
    "Wxd95xMDf0M.json"
]

for filename in files:
    path = os.path.join(pending_dir, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        video = data.get("video", {})
        transcript = data.get("transcript", "")
        
        # Write metadata and formatted transcript to a temp txt file
        out_path = os.path.join(temp_dir, filename.replace(".json", ".txt"))
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(f"ID: {video.get('id')}\n")
            out_f.write(f"Title: {video.get('title')}\n")
            out_f.write(f"Channel: {video.get('channel_name')}\n")
            out_f.write(f"Published: {video.get('published')}\n")
            out_f.write(f"URL: {video.get('url')}\n")
            out_f.write("\n--- TRANSCRIPT ---\n")
            
            # Format transcript with line breaks every 80 characters or by sentences/spacing
            words = transcript.split()
            line = []
            for w in words:
                line.append(w)
                if len(" ".join(line)) > 80:
                    out_f.write(" ".join(line) + "\n")
                    line = []
            if line:
                out_f.write(" ".join(line) + "\n")
        print(f"Extracted {filename} to {out_path}")
    else:
        print(f"File not found: {path}")
