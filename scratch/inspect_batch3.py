import glob
from pathlib import Path

files = sorted(glob.glob("scratch/transcript_new_batch3_*.txt"))
output = []

for f in files:
    p = Path(f)
    txt = p.read_text(encoding="utf-8")
    lines = txt.split("\n")
    
    header = lines[:8]
    transcript_lines = lines[8:]
    t_len = len(transcript_lines)
    
    output.append("=" * 60)
    output.append(f"FILE: {p.name}")
    output.extend(header)
    output.append(f"TRANSCRIPT LINE COUNT: {t_len}")
    output.append("--- FIRST 40 LINES ---")
    output.extend(transcript_lines[:40])
    output.append("--- MIDDLE 40 LINES ---")
    mid = t_len // 2
    output.extend(transcript_lines[max(0, mid-20):min(t_len, mid+20)])
    output.append("--- LAST 40 LINES ---")
    output.extend(transcript_lines[max(0, t_len-40):])
    output.append("=" * 60)
    output.append("\n\n")

Path("scratch/batch3_inspected.txt").write_text("\n".join(output), encoding="utf-8")
print("Wrote inspection output to scratch/batch3_inspected.txt")
