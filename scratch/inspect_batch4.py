import glob
import textwrap
from pathlib import Path
import re

files = sorted(glob.glob("scratch/transcript_new_batch4_*.txt"))
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
    if "q73I1ZjEosg" in f:
        kws = ["효석", "반도체", "코스닥", "매크로", "시장"]
    elif "rdSxgmmQNYQ" in f:
        kws = ["미국", "블랙스톤", "S&P", "금리", "성장"]
    elif "Rk50SpNxJH0" in f:
        kws = ["CXMT", "애플", "수율", "D램", "메모리"]
    elif "S3HE3t08RDw" in f:
        kws = ["현장", "진실", "반도체", "공장"]
    elif "YcpHhjaH000" in f:
        kws = ["마이크론", "오픈AI", "애플", "반도체", "리밸런싱"]
    elif "YQmLrfjTRIE" in f:
        kws = ["AI", "반도체", "수급", "조정", "엔비디아"]
        
    output.append(f"--- KEYWORD CONTEXTS FOR {kws} ---")
    ctxs = get_context_around_keywords(body, kws)
    for idx, ctx in enumerate(ctxs):
        output.append(f"[{idx+1}] {textwrap.fill(ctx[:600], width=80)}")
        output.append("-" * 40)
        
    output.append("=" * 60)
    output.append("\n\n")

Path("scratch/batch4_clean_inspected.txt").write_text("\n".join(output), encoding="utf-8")
print("Wrote inspection output to scratch/batch4_clean_inspected.txt")
