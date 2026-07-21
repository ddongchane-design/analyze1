from pathlib import Path
import re

def search_keywords(filename, keywords):
    p = Path("scratch") / filename
    if not p.exists():
        print(f"File not found: {filename}")
        return
    txt = p.read_text(encoding="utf-8")
    
    # Split text into segments of ~500 chars to find keywords in context
    segments = []
    # Simple sliding window or split by sentences
    sentences = re.split(r'(?<=[.!?])\s+', txt)
    
    found = []
    for i, sent in enumerate(sentences):
        if any(kw in sent for kw in keywords):
            # Print sentence with context
            start = max(0, i - 3)
            end = min(len(sentences), i + 4)
            ctx = " ".join(sentences[start:end])
            found.append(ctx)
            
    print(f"=== KEYWORDS {keywords} IN {filename} ===")
    for idx, f in enumerate(found[:5]): # Show up to 5 instances
        print(f"[{idx+1}] {f[:600]}...")
        print("-" * 50)

search_keywords("transcript_new_batch3_3_kbiuXUY3Eqw.txt", ["현대차", "자동차"])
search_keywords("transcript_new_batch3_4_L__4lvXJ3lM.txt", ["오픈AI", "조정"])
