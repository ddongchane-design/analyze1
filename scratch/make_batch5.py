import json, sys
from pathlib import Path

dump = json.loads(Path("scratch/pending_new4_dump.json").read_text(encoding="utf-8"))
batch5_data = []

# Item 0: 2NIm_ABg-9Y
item0 = dump[0]
batch5_data.append({
  "video": {
    "id": item0["id"],
    "title": item0["title"],
    "published": item0["published"],
    "channel_name": item0["channel_name"],
    "url": item0["url"],
    "thumbnail": item0["thumbnail"]
  },
  "analysis": {
    "summary": "미 미국 상원의 <span class=\"text-amber-300 font-bold\">크립토 클래리티 법안(Clarity Act)</span> 표결 일정이 8월 토론 종결 동의안 제출 후 9월 최종 표결로 이월된 현황과 비트코인·이더리움 현물 ETF 유입세 전환을 다룸. 달러 및 국채 금리 안정과 함께 스테이블코인 수익률 경쟁 및 공직자 윤리 조항이 막판 쟁점으로 조율 중임을 해설함.",
    "key_claims": [
      "크래리티 법안의 상원 표결이 8월 휴회 전 토론 종결 동의안(Cloture) 제출을 거쳐 9월에 본격 추진됨.",
      "비트코인 현물 ETF에 8억 5천만 달러 자금이 다시 유입되며 고금리·강달러 압력 완화 수혜를 받기 시작함.",
      "<span class=\"text-cyan-300 font-semibold\">스테이블코인 은행 예금 이자 경쟁</span> 및 공직자 크립토 사업 제한 윤리 조항이 주요 타협 과제임."
    ],
    "data_points": [
      "비트코인 현물 ETF 주간 자금 유입액: 8억 5,000만 달러",
      "클래리티 법안 상원 심의 일정: 8월 토론 종결 절차 제출 후 9월 표결 추진",
      "핵심 조율 쟁점: 스테이블코인 이자 이익 제공 허용 및 공직자 크립토 윤리 조항"
    ],
    "signal": "bullish",
    "signal_reason": "<span class=\"text-amber-300 font-bold\">미국 법안 명확성(Clarity) 추진</span>과 ETF 자금 재유입으로 암호화폐 시장의 규제 불확실성 해소 및 자금 유동성 반등 모멘텀 형성.",
    "key_companies": [
      "Bitcoin",
      "Ethereum",
      "BlackRock ETF"
    ],
    "insight": "크립토 규제 법제화(Clarity Act)는 단순한 제도 정비를 넘어 가상자산을 제도권 금융 자산으로 이관하는 분수령이 되며, 달러 유동성 환경과 맞물려 장기 상승 기반이 구축되고 있음.",
    "action_point": "9월 상원 법안 표결 일정과 비트코인/이더리움 현물 ETF 순유입 추이를 모니터링하며 비중 확대를 검토해야 함."
  },
  "classification": {
    "primary_topic": "crypto",
    "secondary_topics": ["economy", "stock"],
    "tags": ["클래리티법안", "이더리움", "비트코인ETF", "가상자산법제화", "크립토규제"]
  }
})

# Item 1: 5TNIgjxCuhc
item1 = dump[1]
batch5_data.append({
  "video": {
    "id": item1["id"],
    "title": item1["title"],
    "published": item1["published"],
    "channel_name": item1["channel_name"],
    "url": item1["url"],
    "thumbnail": item1["thumbnail"]
  },
  "analysis": {
    "summary": "모건스탠리의 <span class=\"text-cyan-300 font-semibold\">'메모리 반도체 주가 가파른 조정 완료'</span> 바닥론 보고서와 소비재·화장품 순환매 장세를 조명함. 정부의 ISA 및 주가누르기 방지법(상법 개정) 손질 동향과 함께 3프로TV 앱 정보유출 사과 및 국내 증시 수급 재편 이슈를 종합 분석함.",
    "key_claims": [
      "모건스탠리가 메모리 반도체의 가파른 하락 조정이 일단락되었음을 밝히며 반도체 바닥론에 힘을 실음.",
      "정부가 주가누르기 방지법 및 ISA 세제 혜택 개선안을 추가 손질하여 주주가치 제고 모멘텀을 이어감.",
      "내수 소비재, 화장품 등 <span class=\"text-amber-300 font-bold\">실적 기반 저평가 업종으로 순환매</span> 자금이 이동함."
    ],
    "data_points": [
      "모건스탠리 보고서 핵심 요지: 메모리 반도체 주가 과도한 조정 선반영 후 바닥 형성",
      "정책 동향: 주가누르기 방지법 및 ISA 개정안 추가 보완 발표",
      "증시 수급 특징: 반도체 쏠림 해소 및 화장품·소비재 순환매 유입"
    ],
    "signal": "bullish",
    "signal_reason": "<span class=\"text-cyan-300 font-semibold\">메모리 반도체 바닥 형성 지점 포착</span>과 정부 주주가치 제고 정책의 연속성으로 증시 지지력 강화.",
    "key_companies": [
      "Morgan Stanley",
      "삼성전자",
      "SK하이닉스"
    ],
    "insight": "메모리 반도체의 조정 완료 신호와 상법/ISA 정책 보완은 지수의 과도한 조정을 멈추고 저평가 소비재·밸류업 주식으로 순환매 확산을 일으키는 긍정적 촉매제임.",
    "action_point": "조정이 마무리된 반도체 대장주의 분할 매수와 함께 상법 개정 수혜 및 실적 모멘텀이 있는 소비재·화장품 종목에 관심을 가져야 함."
  },
  "classification": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["모건스탠리", "메모리바닥론", "ISA개정안", "주가누르기방지법", "소비재순환매"]
  }
})

# Item 2: aw0Wbz3o5S8
item2 = dump[2]
batch5_data.append({
  "video": {
    "id": item2["id"],
    "title": item2["title"],
    "published": item2["published"],
    "channel_name": item2["channel_name"],
    "url": item2["url"],
    "thumbnail": item2["thumbnail"]
  },
  "analysis": {
    "summary": "8월 기간 조정을 거친 후 <span class=\"text-amber-300 font-bold\">9월 증시 반등 가능성</span>과 시장 흐름을 결정짓는 외국인 수급 3가지 핵심 축을 분석함. 외국인의 코스피 선물 이익실현 매매 패턴과 나스닥 급등 속 메모리 반도체의 상대적 소외 현상 및 가을 증시 전환점을 다룸.",
    "key_claims": [
      "8월 증시는 가격 조정이 완료된 상태에서 매물 소화를 거치는 기간 조정 양상을 보이며 9월 반등을 준비하는 구간임.",
      "외국인 현선물 매매가 하방 매도 포지션 이익실현으로 전환되며 지수 하단 방어력을 형성하고 있음.",
      "미국 나스닥 급등에도 불구하고 <span class=\"text-rose-400 font-medium\">메모리 반도체 차별화 및 쏠림 해소</span> 과정에서 종목별 양극화가 진행됨."
    ],
    "data_points": [
      "증시 예상 타임라인: 8월 기간 조정 소화 후 9월 상승 전환 전망",
      "외국인 수급 변화: 선물 매도 포지션 숏커버링 및 이익실현 진입",
      "미국 반도체 지수 특징: 빅테크 및 설비주 대비 메모리 반도체 상대적 가격 조정"
    ],
    "signal": "neutral",
    "signal_reason": "8월 기간 조정의 변동성이 상존하나 외국인 포지션 전환으로 9월 추세적 반등 기대감이 고조됨.",
    "key_companies": [
      "SK하이닉스",
      "삼성전자",
      "위즈웨이브"
    ],
    "insight": "8월의 지루한 기간 조정은 9월 금리 인하 기대감과 빅테크 어닝 모멘텀을 반영하기 위한 에너지 축적 과정이므로 소외된 실적 우량주 포착 기회로 삼아야 함.",
    "action_point": "외국인 선물 매수 전환 여부를 관찰하며 기간 조정 구간을 활용해 9월 반등 주도주를 선제적으로 모아가는 전략이 유효함."
  },
  "classification": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["9월증시반등", "8월기간조정", "외국인수급", "선물매매", "코스피전망"]
  }
})

# Item 3: EmxFZ0q99TI
item3 = dump[3]
batch5_data.append({
  "video": {
    "id": item3["id"],
    "title": item3["title"],
    "published": item3["published"],
    "channel_name": item3["channel_name"],
    "url": item3["url"],
    "thumbnail": item3["thumbnail"]
  },
  "analysis": {
    "summary": "미국 7월 고용 지표 쇼크(23,000건 감소)에 따른 <span class=\"text-cyan-300 font-semibold\">연준 금리 인상 우려 완전 완화</span>와 S&P500 전반의 강세 장세를 분석함. 메모리 반도체를 제외한 빅테크 및 전통 산업의 실적 호조와 함께 3프로TV 서비스 보안 유출 2차 피해 방지 조치 현황을 다룸.",
    "key_claims": [
      "미국 고용 감소로 긴축 우려가 빠르게 소멸되며 채권 금리 안정과 함께 증시 전반의 매수세가 재개됨.",
      "메모리 반도체 섹터의 나홀로 약세를 제외하고 S&P500 대부분의 빅테크 및 가치주가 신고가 흐름을 나타냄.",
      "<span class=\"text-amber-300 font-bold\">고용 시장 둔화</span>가 연준의 피벗(금리 인하) 명분을 완성하며 자산 시장 전반에 온기를 불어넣음."
    ],
    "data_points": [
      "7월 미국 비농업 고용 변화: 23,000건 감소 (시장 예상치 대폭 하회)",
      "증시 반응: 금리 인상 가능성 완전 제거 및 S&P500 대부분 종목 강세",
      "섹터별 차별화: 메모리 반도체 소폭 약세 vs 빅테크·가치주 신고가"
    ],
    "signal": "bullish",
    "signal_reason": "<span class=\"text-amber-300 font-bold\">연준 피벗 가시화</span>와 기업 실적 견조함이 결합되어 증시의 우상향 동력이 확실히 작동함.",
    "key_companies": [
      "S&P 500 Index",
      "Federal Reserve",
      "삼프로TV"
    ],
    "insight": "고용 둔화는 경제 둔화 리스크보다 연준의 금리 인하 폭을 늘려주는 강력한 거시 호재로 해석되고 있으며 자산 가격 밸류에이션을 받쳐주고 있음.",
    "action_point": "금리 인하 수혜가 예상되는 성장주 및 고배당·가치주 포트폴리오를 강화하며 매크로 피벗 흐름에 탑승해야 함."
  },
  "classification": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["미국고용쇼크", "금리인상우려완화", "SP500신고가", "연준피벗", "월가뉴스레터"]
  }
})

Path("scratch/batch5_analysis.json").write_text(json.dumps(batch5_data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Wrote batch 5 to scratch/batch5_analysis.json")
