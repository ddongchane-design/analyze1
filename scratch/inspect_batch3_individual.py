import json
from pathlib import Path

def inspect_file(fname, f_out):
    path = Path(f"data/pending/{fname}")
    if not path.exists():
        f_out.write(f"=== {fname} NOT FOUND ===\n\n")
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    video = data.get("video", {})
    transcript = data.get("transcript", "")
    f_out.write(f"=== {fname} ===\n")
    f_out.write(f"Title: {video.get('title')}\n")
    f_out.write(f"Channel: {video.get('channel_name')}\n")
    f_out.write(f"Transcript Len: {len(transcript)}\n")
    f_out.write(f"Snippet (first 3000 chars):\n")
    f_out.write(transcript[:3000])
    f_out.write("\n\nSnippet (last 3000 chars):\n")
    f_out.write(transcript[-3000:])
    f_out.write("\n=========================================\n\n")

def main():
    out_path = Path("scratch/batch3_individual_info_utf8.txt")
    with open(out_path, "w", encoding="utf-8") as f_out:
        inspect_file("81C4RYcyw7Y.json", f_out)
        inspect_file("_jerMEDkb-o.json", f_out)
        inspect_file("UZEZ1KJXQt4.json", f_out)
    print("Wrote to scratch/batch3_individual_info_utf8.txt")

if __name__ == "__main__":
    main()
