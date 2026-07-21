import glob
import textwrap
from pathlib import Path

files = sorted(glob.glob("scratch/transcript_new_batch3_*.txt"))
output = []

for f in files:
    p = Path(f)
    txt = p.read_text(encoding="utf-8")
    lines = txt.split("\n")
    
    header = lines[:5]
    body = "\n".join(lines[5:])
    
    output.append("=" * 60)
    output.append(f"FILE: {p.name}")
    output.extend(header)
    output.append(f"TRANSCRIPT LENGTH: {len(body)}")
    output.append("--- WRAPPED SAMPLES (FIRST 2000 CHARS) ---")
    wrapped_first = textwrap.fill(body[:2000], width=80)
    output.append(wrapped_first)
    
    output.append("--- WRAPPED SAMPLES (MIDDLE 2000 CHARS) ---")
    mid = len(body) // 2
    wrapped_mid = textwrap.fill(body[mid:mid+2000], width=80)
    output.append(wrapped_mid)
    
    output.append("--- WRAPPED SAMPLES (LAST 2000 CHARS) ---")
    wrapped_last = textwrap.fill(body[-2000:], width=80)
    output.append(wrapped_last)
    output.append("=" * 60)
    output.append("\n\n")

Path("scratch/batch3_clean_inspected.txt").write_text("\n".join(output), encoding="utf-8")
print("Wrote inspection output to scratch/batch3_clean_inspected.txt")
