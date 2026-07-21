import json
from pathlib import Path

f_path = Path("data/pending/jlKh26fxC3Q.json")
if f_path.exists():
    data = json.loads(f_path.read_text(encoding="utf-8"))
    title = data["video"]["title"]
    transcript = data.get("transcript", "")
    print(f"TITLE: {title}")
    # Write first 6000 chars of transcript to a file to inspect
    Path("scratch/single_info.txt").write_text(f"TITLE: {title}\n\nTRANSCRIPT:\n{transcript[:15000]}", encoding="utf-8")
    print("Dumped to scratch/single_info.txt")
else:
    print("File not found")
