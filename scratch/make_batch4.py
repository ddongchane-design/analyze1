import json, sys
from pathlib import Path

dump = json.loads(Path("scratch/pending_dump.json").read_text(encoding="utf-8"))
batch4_data = []

# Item 15: wTRgn_fEjRI
item15 = dump[15]
batch4_data.append({
  "video": {
    "id": item15["id"],
    "title": item15["title"],
    "published": item15["published"],
    "channel_name": item15["channel_name"],
    "url": item15["url"],
    "thumbnail": item15["thumbnail"]
  },
  "analysis": {
    "summary": "지구에서 68광년 떨어진 갈색 외성(CD35 2722B) 곁을 171일 주기로 공전하는 <span class=\"text-amber-300 font-bold\">목성 0.9배 질량의 최초 외계 위성(Exomoons) 후보</span> 발견을 분석함. 별-갈색외성-외계위성으로 이어지는 최초의 3층 계층 구조 확인과 도플러 효과 관측 기법의 천문학적 의의를 다룸.",
    "key_claims": [
      "6,000개가 넘는 외계 행성 탐사 역사상 명확한 외계 위성 존재가 포착된 것은 이번이 최초 사례임.",
      "모항성(적색 외성) - 갈색 외성 - 외계 위성(목성 0.9배)으로 구성된 정밀한 계층형 궤도 역학을 증명함.",
      "<span class=\"text-cyan-300 font-semibold\">빛의 도플러 시프트 관측</span>과 케플러 법칙 시뮬레이션을 통해 미세한 궤도 섭동을 정밀 측정함."
    ],
    "data_points": [
      "모항성 및 갈색외성 거리: 지구에서 약 68광년 (21파섹)",
      "갈색외성 질량: 목성의 37배",
      "발견된 외계위성 후보 주기 및 질량: 공전주기 171일, 질량 목성의 0.9배 (약 90%)"
    ],
    "signal": "bullish",
    "signal_reason": "<span class=\"text-amber-300 font-bold\">우주 관측 기술 발전</span> 및 궤도 정밀 탐사 관측 장비 시장의 성장에 긍정적 비전을 제시함.",
    "key_companies": [
      "유럽우주국(ESA)",
      "안될과학"
    ],
    "insight": "항성과 행성 사이 갈색 외성에 딸린 위성 구조 확인은 우주 형성 이론의 새로운 지평을 열었으며 우주 탐사 센서 및 망원경 기술의 혁신을 입증함.",
    "action_point": "우주 항공 관측 장비 및 딥스페이스 탐사 관련 테크/우주 산업의 장기 성장에 주목해야 함."
  },
  "classification": {
    "primary_topic": "space",
    "secondary_topics": ["etc"],
    "tags": ["외계위성", "갈색외성", "우주탐사", "도플러효과", "천문학"]
  }
})

# Item 16: XMn4jcgO3t4
item16 = dump[16]
batch4_data.append({
  "video": {
    "id": item16["id"],
    "title": item16["title"],
    "published": item16["published"],
    "channel_name": item16["channel_name"],
    "url": item16["url"],
    "thumbnail": item16["thumbnail"]
  },
  "analysis": {
    "summary": "과학 지식이 고정된 절대 진리가 아니라 합의와 설득에 의해 끊임없이 진화하는 <span class=\"text-amber-300 font-bold\">'패러다임 시프트(Paradigm Shift)'</span>임을 철학 및 현대 물리학(상대성 이론, 양자역학) 관점에서 해설함. 새로운 증거와 설득력에 따라 기존 과학 교리가 대전환되는 현대 과학 철학의 본질을 분석함.",
    "key_claims": [
      "과학적 사실은 영원불변한 절대 진리가 아니라 사회적 설득력과 신뢰성에 기반해 유지되는 동적 체계임.",
      "상대성 이론이나 양자역학 역시 더 높은 설득력을 가진 새로운 패러다임이 등장하면 재구성될 수 있음.",
      "기술 및 산업 현장에서도 기존 공식을 과감히 깨뜨리는 <span class=\"text-cyan-300 font-semibold\">패러다임 혁신</span>을 수용해야 함."
    ],
    "data_points": [
      "과학 철학 핵심 개념: 토마스 쿤의 패러다임 시프트",
      "대체 대상 현대 정설: 아인슈타인 상대성 이론 및 양자역학 표준 모델",
      "과학적 가치 판단 기준: 대중 및 학계의 설득력과 수용도"
    ],
    "signal": "neutral",
    "signal_reason": "과학 철학적 정론을 소개하는 통찰 콘텐츠로 시장 시그널은 중립임.",
    "key_companies": [
      "안될과학"
    ],
    "insight": "기존 패러다임에 고착된 시각은 기술적 독점이나 시장 우위를 영원히 보장하지 못하며, 파괴적 신기술을 유연하게 수용하는 역량이 필수적임.",
    "action_point": "기술 패러다임 전환기(AI, 전고체 등)에 기존 레거시 기술에 안주하는 기업보다 혁신 지향 기업으로 포트폴리오를 다변화해야 함."
  },
  "classification": {
    "primary_topic": "etc",
    "secondary_topics": ["tech"],
    "tags": ["패러다임시프트", "과학철학", "양자역학", "상대성이론", "혁신적사고"]
  }
})

# Item 17: YzT1DepJxls
item17 = dump[17]
batch4_data.append({
  "video": {
    "id": item17["id"],
    "title": item17["title"],
    "published": item17["published"],
    "channel_name": item17["channel_name"],
    "url": item17["url"],
    "thumbnail": item17["thumbnail"]
  },
  "analysis": {
    "summary": "빅테크 클라우드 3사(아마존, MS, 구글)가 <span class=\"text-amber-300 font-bold\">5~6% 금리로 자금을 조달해 25% 이상의 수익률(ROIC)</span>을 창출하는 AI 데이터센터 투자의 경제적 당위성을 분석함. 클라우드 매출 폭증(구글 +82%, MS +43%, 아마존 +37%)과 공급 부족 현상이 지속되어 빅테크의 AI 설비투자가 결코 멈추지 않을 이유를 입증함.",
    "key_claims": [
      "구글의 40조 원 대 회사채 발행에 160조 원 이상의 응찰 자금이 몰리며 빅테크의 막강한 자본 조달 능력이 입증됨.",
      "빅테크는 5~6% 비용으로 빌린 자본으로 AI 컴퓨팅 서비스를 통해 25% 수준의 고수익을 창출하고 있어 투자를 멈출 이유가 없음.",
      "클라우드 3사의 <span class=\"text-cyan-300 font-semibold\">AI 매출 급증</span>으로 반도체(HBM/DRAM) 및 AI 전력 인프라 수요가 확고히 뒷받침됨."
    ],
    "data_points": [
      "구글 회사채 발행 자금 모집: 40조 원 목표에 160조 원 참여 (4배 흥행)",
      "클라우드 전년 대비 성장률: 구글 +82%, MS +43%, 아마존 +37%",
      "자본비용(CoC) 대비 수익률(ROIC): 조달 금리 5~6% vs AI 사업 수익률 약 25%"
    ],
    "signal": "bullish",
    "signal_reason": "<span class=\"text-cyan-300 font-semibold\">빅테크의 압도적 투자 여력 및 AI ROIC</span>가 입증됨에 따라 반도체, AI 클라우드, 전력 인프라 산업에 강력한 장기 강세 시그널 제공.",
    "key_companies": [
      "구글",
      "마이크로소프트",
      "아마존",
      "NVIDIA",
      "SK하이닉스"
    ],
    "insight": "AI 피크아웃 우려는 빅테크의 강한 자본 조달력과 압도적 ROIC 마진 구조를 간과한 오해이며, 클라우드 자본 지출(CapEx)은 여전히 강력하게 유지되고 있음.",
    "action_point": "빅테크 AI CapEx의 최대 수혜주인 메모리 반도체, 전력 기기, 클라우드 인프라 관련 핵심 기업의 비중을 확고히 유지해야 함."
  },
  "classification": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["빅테크CapEx", "AI투자수익률", "클라우드성장", "구글회사채", "반도체수혜"]
  }
})

# Item 18: z-eWF1oycYg
item18 = dump[18]
batch4_data.append({
  "video": {
    "id": item18["id"],
    "title": item18["title"],
    "published": item18["published"],
    "channel_name": item18["channel_name"],
    "url": item18["url"],
    "thumbnail": item18["thumbnail"]
  },
  "analysis": {
    "summary": "코스피의 7월 조정 이후 진행 중인 기술적 반등 장세에서 <span class=\"text-amber-300 font-bold\">진짜 바닥과 추세 전환을 판단하는 4가지 기술적 차트 신호</span>를 분석함. 하락 채널 상단 돌파, 전고점 돌파, 박스권 하단 지지 및 거래량을 동반한 장대 양봉 등 진성 반등을 가려내는 실전 매매 가이드를 제시함.",
    "key_claims": [
      "단순한 가격 반등에 속지 않으려면 하락 채널 상향 탈출과 박스권 상단 돌파 여부를 가장 중요하게 확인해야 함.",
      "하락장 대응 시에는 전저점 붕괴(박스권 하향 돌파) 여부를 통해 리스크 관리 지점을 확실히 설정해야 함.",
      "<span class=\"text-cyan-300 font-semibold\">거래량이 실린 장대 양봉</span>이 전고점을 넘어서야 추세적 상승장(Bull Trend) 재진입으로 확인됨."
    ],
    "data_points": [
      "분석 대상 지수: KOSPI 차트 횡보/하락/상승 채널",
      "핵심 매수 타점 조건: 박스권 상단 돌파 + 하락 추세선 상향 탈출",
      "위험 관리 신호: 전저점 하향 붕괴 및 음봉 거래량 폭증"
    ],
    "signal": "neutral",
    "signal_reason": "하락 채널 탈출 및 거래량 수급이 완전히 확인되기 전까지는 신중한 기술적 확인 매매가 요구됨.",
    "key_companies": [
      "한국거래소(KOSPI)"
    ],
    "insight": "지수 차트 분석은 예측이 아닌 대응의 영역이며, 하락 채널을 완전히 벗어나는 확인 신호가 발생할 때 비중을 확대하는 정석 매매가 계좌를 지킴.",
    "action_point": "코스피 전고점 회복 여부와 하락 채널 상단 돌파 지점을 매수 타점으로 설정하고 감정적 추격 매수를 자제해야 함."
  },
  "classification": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["코스피차트", "진성반등신호", "하락채널탈출", "차트분석", "기술적매매"]
  }
})

# Item 19: ZH3Nm3y-HpE
item19 = dump[19]
batch4_data.append({
  "video": {
    "id": item19["id"],
    "title": item19["title"],
    "published": item19["published"],
    "channel_name": item19["channel_name"],
    "url": item19["url"],
    "thumbnail": item19["thumbnail"]
  },
  "analysis": {
    "summary": "스타트업 OGQ(오지큐) 신철 대표가 M&A 목적 투자유치 과정에서 계약서상 <span class=\"text-rose-400 font-medium\">이해관계인(대표자 개인) 상환 연대책임 조항</span>으로 인해 120억 원의 빚을 개인이 짊어지게 된 독소조항 사건을 법률적으로 파헤침. VC 펀드의 연대보증 우회 계약 문구와 스타트업 벤처 투자의 쥐약이 되는 법률 리스크를 경고함.",
    "key_claims": [
      "게티이미지코리아 인수를 목표로 투자금 90억 원을 유치했으나, 인수 실패 시 대표 개인이 상환 책임을 지는 '이해관계인 상환 조항'이 독소로 작용함.",
      "과거 연대보증 금지 정책을 회피하기 위해 투자 계약서에 대표 개인을 '이해관계인'으로 명시해 법적 상환 책임을 묻는 편법 문구가 성행함.",
      "<span class=\"text-rose-400 font-medium\">스타트업 최고경영자(CEO)</span>의 계약서 독소조항 검토 부주의가 회사는 물론 개인 재산 전액을 파산으로 몰고 갈 수 있음."
    ],
    "data_points": [
      "투자 유치 금액: 90억 원 (상환 청구액 이자 포함 약 120억 원)",
      "대상 회사 및 대표: OGQ (신철 대표)",
      "쟁점 조항: 상환우선주(RCPS) 계약 내 '이해관계인 개인 상환 의무' 독소 문구"
    ],
    "signal": "bearish",
    "signal_reason": "<span class=\"text-rose-400 font-medium\">스타트업 대표 개인 위험 연대 조항</span>으로 벤처 투자의 건전성이 훼손되고 창업 생태계 위축 위험 우려.",
    "key_companies": [
      "OGQ",
      "게티이미지코리아",
      "법무법인 디엘지"
    ],
    "insight": "투자 계약서의 단 한 줄의 '이해관계인' 법률 문구가 연대보증보다 무서운 독소 조항이 되므로, 비대칭 계약 관행 개선과 정밀한 법률 자문이 필수적임.",
    "action_point": "비상장 벤처 기업 투자자 및 스타트업 경영진은 투자계약서(RCPS) 내 대표자 개인 리스크 담보 독소조항을 원천 차단하고 재검토해야 함."
  },
  "classification": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["OGQ사건", "투자계약서독소조항", "이해관계인상환", "연대보증", "스타트업법률"]
  }
})

Path("scratch/batch4_analysis.json").write_text(json.dumps(batch4_data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Wrote batch 4 to scratch/batch4_analysis.json")
