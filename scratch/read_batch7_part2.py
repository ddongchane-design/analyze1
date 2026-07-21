import json
from pathlib import Path

def main():
    files = [
        "E8BMnRLZWsQ.json",
        "8p3Jw-GI1UY.json",
        "tyGE1ML_KPg.json"
    ]
    
    pending_dir = Path("data/pending")
    out_path = Path("scratch/temp_read_batch7_part2.txt")
    
    with open(out_path, "w", encoding="utf-8") as out_file:
        for filename in files:
            path = pending_dir / filename
            if not path.exists():
                out_file.write(f"File {filename} not found\n\n")
                continue
            
            data = json.loads(path.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            
            out_file.write(f"=== FILE: {filename} ===\n")
            out_file.write(f"TITLE: {video.get('title')}\n")
            out_file.write(f"CHANNEL: {video.get('channel_name')}\n")
            out_file.write(f"PUBLISHED: {video.get('published')}\n")
            out_file.write(f"TRANSCRIPT LENGTH: {len(transcript)} chars\n")
            
            # Print snippets where key info is spoken
            out_file.write("--- TRANSCRIPT SNIPPETS ---\n")
            # For Sweden, print first 4000 characters and middle
            if filename == "E8BMnRLZWsQ.json":
                out_file.write("START:\n")
                out_file.write(transcript[:4000])
                out_file.write("\n\nMIDDLE:\n")
                mid = len(transcript) // 2
                out_file.write(transcript[mid-2000:mid+2000])
            # For SK Group, search for specific terms or print sections
            elif filename == "8p3Jw-GI1UY.json":
                out_file.write("SK GROUP SECTIONS:\n")
                # print parts around "2천조" and "ADR"
                lines = transcript.split(". ")
                count = 0
                for line in lines:
                    if any(term in line for term in ["2천조", "2,000조", "ADR", "이혼", "최태원"]):
                        out_file.write(f"- {line.strip()}\n")
                        count += 1
                        if count > 30:
                            break
            # For US-Iran peace deal, print parts around "종전", "호르무즈" and "스페이스X"
            elif filename == "tyGE1ML_KPg.json":
                out_file.write("US-IRAN / SPACEX SECTIONS:\n")
                lines = transcript.split(". ")
                count = 0
                for line in lines:
                    if any(term in line for term in ["종전", "호르무즈", "합의", "스페이스X"]):
                        out_file.write(f"- {line.strip()}\n")
                        count += 1
                        if count > 30:
                            break
            out_file.write("\n" + "=" * 80 + "\n\n")
            
    print(f"Wrote Batch 7 Part 2 snippets to {out_path}")

if __name__ == "__main__":
    main()
