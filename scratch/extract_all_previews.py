import json
from pathlib import Path

def main():
    pending_dir = Path("data/pending")
    json_files = sorted(list(pending_dir.glob("*.json")))
    
    output_path = Path("scratch/all_previews.txt")
    lines = []
    
    for idx, file_path in enumerate(json_files):
        try:
            data = json.loads(file_path.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            
            lines.append("=" * 80)
            lines.append(f"INDEX: {idx}")
            lines.append(f"FILE: {file_path.name}")
            lines.append(f"TITLE: {video.get('title')}")
            lines.append(f"CHANNEL: {video.get('channel_name')}")
            lines.append(f"PUBLISHED: {video.get('published')}")
            lines.append(f"TRANSCRIPT LENGTH: {len(transcript)}")
            lines.append("-" * 80)
            
            # Get first 2000 chars and last 2000 chars of transcript
            if len(transcript) <= 4000:
                lines.append(transcript)
            else:
                lines.append("[START OF TRANSCRIPT]")
                lines.append(transcript[:2000])
                lines.append("\n... [TRUNCATED] ...\n")
                lines.append("[END OF TRANSCRIPT]")
                lines.append(transcript[-2000:])
                
            lines.append("=" * 80 + "\n\n")
            
        except Exception as e:
            lines.append(f"INDEX: {idx} | FILE: {file_path.name} | ERROR: {e}\n\n")
            
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Successfully extracted previews of {len(json_files)} files to {output_path}")

if __name__ == "__main__":
    main()
