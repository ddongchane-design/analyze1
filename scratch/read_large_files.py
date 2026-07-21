import json
from pathlib import Path

def inspect_large():
    pending_dir = Path("data/pending")
    
    # Let's inspect E8BMnRLZWsQ (Sweden)
    if (pending_dir / "E8BMnRLZWsQ.json").exists():
        data = json.loads((pending_dir / "E8BMnRLZWsQ.json").read_text(encoding="utf-8"))
        print("=== SWEDEN WELFARE (E8BMnRLZWsQ) ===")
        print("TITLE:", data["video"]["title"])
        transcript = data["transcript"]
        print("TRANSCRIPT LENGTH:", len(transcript))
        # Search for key terms: 상속세, 부자, 세금, 자본주의
        print("Snippets about tax/inheritance:")
        for line in transcript.split(". "):
            if any(term in line for term in ["상속세", "부자", "세금", "이민", "자본주의", "1%"]):
                if len(line) < 300:
                    print("-", line.strip())
        print("\n" + "="*80 + "\n")

    # Let's inspect 8p3Jw-GI1UY (SK Group)
    if (pending_dir / "8p3Jw-GI1UY.json").exists():
        data = json.loads((pending_dir / "8p3Jw-GI1UY.json").read_text(encoding="utf-8"))
        print("=== SK GROUP (8p3Jw-GI1UY) ===")
        print("TITLE:", data["video"]["title"])
        transcript = data["transcript"]
        print("TRANSCRIPT LENGTH:", len(transcript))
        # Search for key terms: 하이닉스, SK, 2000조, 2천조, 주주환원, 최태원, 이혼, ADR
        print("Snippets about SK/Hynix/ADR:")
        count = 0
        for line in transcript.split(". "):
            if any(term in line for term in ["ADR", "2천조", "2,000조", "주주환원", "최태원", "이혼"]):
                if len(line) < 300 and count < 15:
                    print("-", line.strip())
                    count += 1
        print("\n" + "="*80 + "\n")

    # Let's inspect tyGE1ML_KPg (US-Iran peace deal)
    if (pending_dir / "tyGE1ML_KPg.json").exists():
        data = json.loads((pending_dir / "tyGE1ML_KPg.json").read_text(encoding="utf-8"))
        print("=== US-IRAN PEACE DEAL (tyGE1ML_KPg) ===")
        print("TITLE:", data["video"]["title"])
        transcript = data["transcript"]
        print("TRANSCRIPT LENGTH:", len(transcript))
        # Search for key terms: 이란, 종전, 합의, 호르무즈, 스페이스X, 트럼프, 유가
        print("Snippets about US-Iran/SpaceX:")
        count = 0
        for line in transcript.split(". "):
            if any(term in line for term in ["이란", "종전", "호르무즈", "합의", "스페이스X", "유가"]):
                if len(line) < 300 and count < 15:
                    print("-", line.strip())
                    count += 1
        print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    inspect_large()
