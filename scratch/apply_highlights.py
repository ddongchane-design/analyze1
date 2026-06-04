import os
import json
import re
from pathlib import Path

# 강조 규칙 정의
HIGHLIGHTS = [
    # 1. Megatrends / Macro (amber-300)
    ("고금리 장기화", '<span class="text-amber-300 font-bold">고금리 장기화</span>'),
    ("고금리", '<span class="text-amber-300 font-bold">고금리</span>'),
    ("금리 인하", '<span class="text-amber-300 font-bold">금리 인하</span>'),
    ("원달러 환율", '<span class="text-amber-300 font-bold">원달러 환율</span>'),
    ("환율", '<span class="text-amber-300 font-bold">환율</span>'),
    ("유가 상승", '<span class="text-amber-300 font-bold">유가 상승</span>'),
    ("유가", '<span class="text-amber-300 font-bold">유가</span>'),
    ("인플레이션", '<span class="text-amber-300 font-bold">인플레이션</span>'),
    ("ETF 시대", '<span class="text-amber-300 font-bold">ETF 시대</span>'),
    ("퇴직연금", '<span class="text-amber-300 font-bold">퇴직연금</span>'),
    ("에너지 전환", '<span class="text-amber-300 font-bold">에너지 전환</span>'),
    ("재생에너지", '<span class="text-amber-300 font-bold">재생에너지</span>'),
    ("가상발전소", '<span class="text-amber-300 font-bold">가상발전소</span>'),
    ("평균 회귀", '<span class="text-amber-300 font-bold">평균 회귀</span>'),
    ("감마 스퀴즈", '<span class="text-amber-300 font-bold">감마 스퀴즈</span>'),
    ("포모 트레이딩", '<span class="text-amber-300 font-bold">포모 트레이딩</span>'),
    ("제본스의 역설", '<span class="text-amber-300 font-bold">제본스의 역설</span>'),
    ("고용 시장", '<span class="text-amber-300 font-bold">고용 시장</span>'),
    ("민간고용", '<span class="text-amber-300 font-bold">민간고용</span>'),

    # 2. Tech / Companies / Products (cyan-300)
    ("AI 반도체", '<span class="text-cyan-300 font-semibold">AI 반도체</span>'),
    ("메모리 반도체", '<span class="text-cyan-300 font-semibold">메모리 반도체</span>'),
    ("반도체", '<span class="text-cyan-300 font-semibold">반도체</span>'),
    ("HBM", '<span class="text-cyan-300 font-semibold">HBM</span>'),
    ("구글", '<span class="text-cyan-300 font-semibold">구글</span>'),
    ("인텔", '<span class="text-cyan-300 font-semibold">인텔</span>'),
    ("마벨", '<span class="text-cyan-300 font-semibold">마벨</span>'),
    ("스페이스X", '<span class="text-cyan-300 font-semibold">스페이스X</span>'),
    ("스타링크", '<span class="text-cyan-300 font-semibold">스타링크</span>'),
    ("스타십", '<span class="text-cyan-300 font-semibold">스타십</span>'),
    ("테슬라", '<span class="text-cyan-300 font-semibold">테슬라</span>'),
    ("브로드컴", '<span class="text-cyan-300 font-semibold">브로드컴</span>'),
    ("크라우드 스트라이크", '<span class="text-cyan-300 font-semibold">크라우드 스트라이크</span>'),
    ("코인베이스", '<span class="text-cyan-300 font-semibold">코인베이스</span>'),
    ("지멘스", '<span class="text-cyan-300 font-semibold">지멘스</span>'),
    ("ABB", '<span class="text-cyan-300 font-semibold">ABB</span>'),
    ("버크셔 해서웨이", '<span class="text-cyan-300 font-semibold">버크셔 해서웨이</span>'),
    ("노바티스", '<span class="text-cyan-300 font-semibold">노바티스</span>'),
    ("콜키신", '<span class="text-cyan-300 font-semibold">콜키신</span>'),
    ("현대자동차", '<span class="text-cyan-300 font-semibold">현대자동차</span>'),
    ("현대차", '<span class="text-cyan-300 font-semibold">현대차</span>'),
    ("기아", '<span class="text-cyan-300 font-semibold">기아</span>'),
    ("삼성전자", '<span class="text-cyan-300 font-semibold">삼성전자</span>'),
    ("SK하이닉스", '<span class="text-cyan-300 font-semibold">SK하이닉스</span>'),
    ("화외이", '<span class="text-cyan-300 font-semibold">화외이</span>'),
    ("화웨이", '<span class="text-cyan-300 font-semibold">화웨이</span>'),
    ("ASML", '<span class="text-cyan-300 font-semibold">ASML</span>'),
    ("TSMC", '<span class="text-cyan-300 font-semibold">TSMC</span>'),

    # 3. Risks / Negatives (rose-400)
    ("급락세", '<span class="text-rose-400 font-medium">급락세</span>'),
    ("급락", '<span class="text-rose-400 font-medium">급락</span>'),
    ("조정", '<span class="text-rose-400 font-medium">조정</span>'),
    ("청산", '<span class="text-rose-400 font-medium">청산</span>'),
    ("유출", '<span class="text-rose-400 font-medium">유출</span>'),
    ("수율 저하", '<span class="text-rose-400 font-medium">수율 저하</span>'),
    ("수율", '<span class="text-rose-400 font-medium">수율</span>'),
    ("사모신용", '<span class="text-rose-400 font-medium">사모신용</span>'),
    ("과열", '<span class="text-rose-400 font-medium">과열</span>'),
    ("리스크", '<span class="text-rose-400 font-medium">리스크</span>'),
    ("위험", '<span class="text-rose-400 font-medium">위험</span>'),
    ("부실", '<span class="text-rose-400 font-medium">부실</span>'),
    ("꼬리 위험", '<span class="text-rose-400 font-medium">꼬리 위험</span>'),
    ("취약성", '<span class="text-rose-400 font-medium">취약성</span>'),

    # 4. Geopolitics (violet-300)
    ("이란", '<span class="text-violet-300 font-medium">이란</span>'),
    ("중동", '<span class="text-violet-300 font-medium">중동</span>'),
    ("쿠웨이트", '<span class="text-violet-300 font-medium">쿠웨이트</span>'),
    ("바레인", '<span class="text-violet-300 font-medium">바레인</span>'),
    ("호르무즈 해협", '<span class="text-violet-300 font-medium">호르무즈 해협</span>'),
    ("호르무즈", '<span class="text-violet-300 font-medium">호르무즈</span>'),
    ("중국", '<span class="text-violet-300 font-medium">중국</span>'),
    ("대중", '<span class="text-violet-300 font-medium">대중</span>')
]

def strip_spans(text: str) -> str:
    """기존의 모든 span 태그를 제거하여 중복 태깅을 방지합니다."""
    text = re.sub(r'</?span[^>]*>', '', text)
    return text

def apply_highlights_to_text(text: str) -> str:
    if not isinstance(text, str):
        return text
    
    text = strip_spans(text)
    
    # 텍스트의 부분을 임시 플레이스홀더로 치환하며 순차적으로 강조를 적용
    placeholders = {}
    temp_text = text
    
    for idx, (word, replacement) in enumerate(HIGHLIGHTS):
        # 대소문자 무관하게 치환하되, 이미 치환된 다른 플레이스홀더 내부의 단어는 건드리지 않음
        pattern = re.compile(re.escape(word))
        
        def repl(match):
            placeholder_key = f"__PH_{idx}__"
            placeholders[placeholder_key] = replacement
            return placeholder_key
            
        temp_text = pattern.sub(repl, temp_text)
        
    # 플레이스홀더들을 실제 강조 span 태그로 복원
    final_text = temp_text
    for placeholder_key, replacement in placeholders.items():
        final_text = final_text.replace(placeholder_key, replacement)
        
    return final_text

def highlight_dict_fields(d, fields):
    if not isinstance(d, dict):
        return
    for f in fields:
        if f in d:
            if isinstance(d[f], str):
                d[f] = apply_highlights_to_text(d[f])
            elif isinstance(d[f], list):
                d[f] = [apply_highlights_to_text(item) if isinstance(item, str) else item for item in d[f]]

def main():
    analyzed_dir = Path("data/analyzed")
    synthesis_dir = Path("data/synthesis")
    
    # 1. data/analyzed 하위의 모든 JSON 처리
    if analyzed_dir.exists():
        json_files = list(analyzed_dir.glob("**/*.json"))
        print(f"총 {len(json_files)}개의 분석 JSON 파일 처리 중...")
        for file_path in json_files:
            try:
                data = json.loads(file_path.read_text(encoding="utf-8"))
                analysis = data.get("analysis", {})
                if analysis:
                    highlight_dict_fields(analysis, ["summary", "insight", "action_point", "signal_reason", "key_claims"])
                    data["analysis"] = analysis
                    file_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            except Exception as e:
                print(f"Error processing {file_path.name}: {e}")

    # 2. data/synthesis 하위의 모든 JSON 처리
    if synthesis_dir.exists():
        syn_files = list(synthesis_dir.glob("*.json"))
        print(f"총 {len(syn_files)}개의 종합 JSON 파일 처리 중...")
        for file_path in syn_files:
            try:
                data = json.loads(file_path.read_text(encoding="utf-8"))
                highlight_dict_fields(data, ["cross_insight", "divergence"])
                file_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            except Exception as e:
                print(f"Error processing synthesis {file_path.name}: {e}")

    print("하이라이트 적용 완료! 대시보드를 다시 빌드합니다...")

if __name__ == "__main__":
    main()
