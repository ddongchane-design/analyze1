from pathlib import Path
import re

def search_keywords(filename, keywords):
    p = Path("scratch") / filename
    if not p.exists():
        return f"File not found: {filename}\n"
    txt = p.read_text(encoding="utf-8")
    
    sentences = re.split(r'(?<=[.!?])\s+', txt)
    found = []
    for i, sent in enumerate(sentences):
        if any(kw in sent for kw in keywords):
            start = max(0, i - 4)
            end = min(len(sentences), i + 5)
            ctx = " ".join(sentences[start:end])
            found.append(ctx)
            
    out = []
    out.append(f"=== KEYWORDS {keywords} IN {filename} ===")
    for idx, f in enumerate(found[:10]):
        out.append(f"[{idx+1}] {f}")
        out.append("-" * 50)
    return "\n".join(out) + "\n\n"

result = ""
result += search_keywords("transcript_new_batch3_3_kbiuXUY3Eqw.txt", ["현대차", "자동차", "소부장", "바이오", "원전"])
result += search_keywords("transcript_new_batch3_4_L__4lvXJ3lM.txt", ["오픈AI", "조정", "가이던스", "애플", "마이크론"])

Path("scratch/search_output.txt").write_text(result, encoding="utf-8")
print("Wrote search output to scratch/search_output.txt")
