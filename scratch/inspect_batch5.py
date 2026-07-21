import glob
import textwrap
from pathlib import Path
import re

files = sorted(glob.glob("scratch/transcript_new_batch5_*.txt"))
output = []

def get_context_around_keywords(txt, keywords):
    sentences = re.split(r'(?<=[.!?])\s+', txt)
    found = []
    for i, sent in enumerate(sentences):
        if any(kw in sent for kw in keywords):
            start = max(0, i - 3)
            end = min(len(sentences), i + 4)
            ctx = " ".join(sentences[start:end])
            found.append(ctx)
    return found[:6]

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
    
    output.append("--- FIRST 1500 CHARS ---")
    output.append(textwrap.fill(body[:1500], width=80))
    
    output.append("--- LAST 1500 CHARS ---")
    output.append(textwrap.fill(body[-1500:], width=80))
    
    # Extract keyword context depending on the file
    kws = []
    if "suQ68ikbD0U" in f:
        kws = ["ETF", "하이닉스", "솔", "SOL", "비중", "집중"]
    elif "vAnFMgnU95g" in f:
        kws = ["7월", "실적", "리밸런싱", "반도체", "오버행", "외국인"]
    elif "vFn-Rw3m048" in f:
        kws = ["리더", "생산성", "AI", "40", "50", "신수정"]
    elif "vbsVscEButA" in f:
        kws = ["블랙홀", "X선", "과학"]
    elif "wNsSdwETx9Q" in f:
        kws = ["에어컨", "온도", "최저", "효율", "과학"]
        
    output.append(f"--- KEYWORD CONTEXTS FOR {kws} ---")
    ctxs = get_context_around_keywords(body, kws)
    for idx, ctx in enumerate(ctxs):
        output.append(f"[{idx+1}] {textwrap.fill(ctx[:600], width=80)}")
        output.append("-" * 40)
        
    output.append("=" * 60)
    output.append("\n\n")

Path("scratch/batch5_clean_inspected.txt").write_text("\n".join(output), encoding="utf-8")
print("Wrote inspection output to scratch/batch5_clean_inspected.txt")
