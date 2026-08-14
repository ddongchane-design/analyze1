import json, sys
from pathlib import Path

# Load pending dump
dump = json.loads(Path("scratch/pending_dump.json").read_text(encoding="utf-8"))

batch1_data = []

# Item 0: 9cgg3gwFYs0
item0 = dump[0]
batch1_data.append({
  "video": {
    "id": item0["id"],
    "title": item0["title"],
    "published": item0["published"],
    "channel_name": item0["channel_name"],
    "url": item0["url"],
    "thumbnail": item0["thumbnail"]
  },
  "analysis": {
    "summary": "일본 정부가 추진하는 <span class=\"text-amber-300 font-bold\">5,500억 달러 규모 대미 투자 계획</span>의 실체와 자금 조달 메커니즘을 분석함. 오하이오 가스화력발전, 텍사스 원유 수출 인프라, 조지아 인조다이아몬드 거점 등 주요 프로젝트에 <span class=\"text-cyan-300 font-semibold\">일본수출입은행(JBIC)</span>이 마중물 출자를 하고 메가뱅크 3사가 대규모 융자를 담당하는 협업 체계를 구축함.",
    "key_claims": [
      "<span class=\"text-amber-300 font-bold\">일본의 대미 대규모 투자</span>는 정부 기관인 JBIC의 선제적 출자와 민간 메가뱅크의 대대적인 융자가 결합된 민관 합동 금융 스킴으로 구체화됨.",
      "에너지 인프라(가스화력·원유) 및 첨단 소재(인조 다이아몬드) 등 미국의 핵심 전략 산업 거점에 자금을 집중 배치함.",
      "일본 <span class=\"text-cyan-300 font-semibold\">메가뱅크</span>의 막강한 해외 자산 조달 능력이 미-일 경제 협력의 핵심 원동력으로 작용함."
    ],
    "data_points": [
      "일본 대미 투자 총 구상 규모: 5,500억 달러",
      "주요 3대 1호 사업: 오하이오 가스화력발전, 텍사스 원유수출 인프라, 조지아 인조다이아몬드 거점",
      "자금 조달 구조: JBIC 정부 출자 + 메가뱅크 3사 대출 융자"
    ],
    "signal": "bullish",
    "signal_reason": "<span class=\"text-amber-300 font-bold\">미-일 경제 동맹 강화</span>와 일본 금융권의 고수익 해외 인프라 자산 확보로 일본 금융 및 에너지 인프라 관련 기업에 긍정적 모멘텀 제공.",
    "key_companies": [
      "JBIC",
      "미쓰비시UFJ",
      "미쓰이스미토모",
      "미즈호"
    ],
    "insight": "일본 금융권의 글로벌 융자 역량은 국경을 넘는 에너지·IT 인프라 투자에서 정부의 지정학적 협상력을 뒷받침하는 강력한 실체적 무기로 활용되고 있음.",
    "action_point": "미-일 공급망 재편 및 에너지 인프라 투자 수혜를 받는 금융주 및 인프라 엔지니어링 기업의 동향을 지속 관찰할 필요가 있음."
  },
  "classification": {
    "primary_topic": "economy",
    "secondary_topics": ["stock", "energy"],
    "tags": ["일본대미투자", "JBIC", "메가뱅크", "에너지인프라", "미일경제협력"]
  }
})

# Item 1: 9eaa4ZpmskA
item1 = dump[1]
batch1_data.append({
  "video": {
    "id": item1["id"],
    "title": item1["title"],
    "published": item1["published"],
    "channel_name": item1["channel_name"],
    "url": item1["url"],
    "thumbnail": item1["thumbnail"]
  },
  "analysis": {
    "summary": "미국 증시의 <span class=\"text-cyan-300 font-semibold\">빅테크 및 팔란티어</span> 급등과 고용지표 둔화에 따른 금리 전망, 한국 세법 개정안 속 <span class=\"text-amber-300 font-bold\">ISA 절세 개정 이슈</span>를 정리함. 빅테크 실적 호조 및 AI 데이터센터 투자 지속이 주가 상승을 이끌었으나 고용 지표 둔화와 환율 하락(원화 강세)이 국내 투자자의 미국주식 환차익을 감소시키는 요소로 작용함.",
    "key_claims": [
      "<span class=\"text-cyan-300 font-semibold\">팔란티어</span>는 기록적 실적 및 AI 성장 가이던스 상향으로 39.8% 급등하며 강력한 상승 동력을 증명함.",
      "미국 비농업 고용지표가 쇼크 수준(-2.3만 명)을 기록함에 따라 연준의 금리 인하 기대감이 재확산됨.",
      "국내 세법 개정안의 <span class=\"text-amber-300 font-bold\">ISA 개정안</span> 발표에 따른 투자 전략 재점검 및 환율 하락 리스크 관리가 시급함."
    ],
    "data_points": [
      "팔란티어 주가 주간 상승률: 39.8% (150달러 상향 돌파)",
      "미국 비농업 일자리: 8만 명 증가 예상 대비 2.3만 명 감소 (고용 쇼크)",
      "원/달러 환율: 1,410원 수준으로 하락 (환차익 감소 영향)"
    ],
    "signal": "bullish",
    "signal_reason": "AI 관련 핵심 기업들의 어닝 서프라이즈와 피벗 기대감이 지수를 이끄는 강세장이 유지되고 있음.",
    "key_companies": [
      "팔란티어",
      "오라클",
      "아마존",
      "엔비디아"
    ],
    "insight": "지수 상승에도 불구하고 원/달러 환율 하락으로 인한 환차손 효과가 발생하므로, 환노출 및 절세 계좌(ISA)를 조화롭게 활용하는 포트폴리오 관리가 필수적임.",
    "action_point": "팔란티어 등 AI 실적주의 지지선(150달러) 확인과 함께 개정 ISA 제도를 활용한 장기 자산 배분 전략을 수립해야 함."
  },
  "classification": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["팔란티어", "ISA계좌", "미국증시", "고용쇼크", "빅테크실적"]
  }
})

# Item 2: b5fFj3lxrwI
item2 = dump[2]
batch1_data.append({
  "video": {
    "id": item2["id"],
    "title": item2["title"],
    "published": item2["published"],
    "channel_name": item2["channel_name"],
    "url": item2["url"],
    "thumbnail": item2["thumbnail"]
  },
  "analysis": {
    "summary": "화학 입문자들이 가장 어려워하는 <span class=\"text-amber-300 font-bold\">주기율표 118개 원소</span>를 서브컬처 스타일의 풀컬러 캐릭터 및 게임 설정으로 다룬 서적 '원소 원정대'의 감수 비하인드를 소개함. 원소별 특성과 환각·폭발성 화합물(옥타나이트로큐베인 등)까지 원자 구조 한계를 재미있게 해설하여 교양 과학 교육의 커뮤니케이션 패러다임을 보여줌.",
    "key_claims": [
      "어려운 화학 원소를 캐릭터화 및 서계관 설정집 형태로 풀어내어 대중의 거부감을 낮추고 직관적 이해를 유도함.",
      "118개 원소뿐만 아니라 최강의 폭발물, 환각성 화합물 및 원자 구조 물리 한계(137번/172번 원소 한계) 등 깊이 있는 물리화학 이론이 담김.",
      "과학 분야의 텍스트 교재를 서브컬처 및 게임 미디어와 융합하는 <span class=\"text-cyan-300 font-semibold\">대중 과학 콘텐츠 융합</span>의 우수 사례임."
    ],
    "data_points": [
      "등장 원소 수: 118개 공식 원소 + 다수의 특수 화합물 캐릭터",
      "일본 현지 출시 원소 컨셉 게임 다운로드 수: 약 13,000건",
      "원소 존재 이론적 한계: 파인만 예측 137번 및 전속 한계 172번"
    ],
    "signal": "neutral",
    "signal_reason": "대중 과학 교육 서적 및 캐릭터 융합 미디어를 소개하는 문화/과학 교양 콘텐츠로 시장 시그널은 중립임.",
    "key_companies": [
      "안될과학",
      "Cell Press (Chem)"
    ],
    "insight": "복잡한 학술 지식을 엔터테인먼트 및 IP(지적재산권)로 변환하는 시도는 과학 에듀테크 및 미디어 산업에서 새로운 가치를 창출할 수 있음.",
    "action_point": "어려운 테크/과학 분야의 대중화 IP 사업화 모델 및 캐릭터 기반 교육 솔루션의 성장성에 주목할 필요가 있음."
  },
  "classification": {
    "primary_topic": "etc",
    "secondary_topics": ["tech"],
    "tags": ["주기율표", "원소원정대", "화학캐릭터", "안될과학", "대중과학"]
  }
})

# Item 3: b8pL6Gtv-4M
item3 = dump[3]
batch1_data.append({
  "video": {
    "id": item3["id"],
    "title": item3["title"],
    "published": item3["published"],
    "channel_name": item3["channel_name"],
    "url": item3["url"],
    "thumbnail": item3["thumbnail"]
  },
  "analysis": {
    "summary": "동북아, 유럽, 북미 대륙을 동시 타격하는 <span class=\"text-rose-400 font-medium\">동반 전 지구적 폭염</span>의 원인으로 대기 상층 제트기류의 파동 구조인 <span class=\"text-amber-300 font-bold\">로스비파(Rossby Waves)</span> 현상을 분석함. 파수 5 또는 파수 7 파동 패턴이 형성에 따라 수천 km 떨어진 대륙들에 동시 열돔 현상이 발생하여 폭염 확률이 최대 20배까지 상승함을 해설함.",
    "key_claims": [
      "상공 10km의 제트기류가 구비치며 발생하는 로스비파 파동이 북반구 전체의 고기압 열돔 배치를 결정함.",
      "네이처 클라이밋 체인지 논문에 따르면 파수 5 패턴 형성 시 북미 중부, 동유럽, 동아시아 3개 지역에 동시 폭염 발생 확률이 20배 급증함.",
      "이상 기후로 인한 글로벌 기후 리스크가 단일 지역 이슈가 아닌 대기 파동 연쇄 반응임을 입증함."
    ],
    "data_points": [
      "제트기류 고도: 상공 약 10km",
      "동시 폭염 유발 파수 패턴: 파수 5 (북미중부·동유럽·동아시아), 파수 7 (북미서중부·서유럽·서아시아)",
      "파수 5 패턴 시 동시 폭염 확률 증가폭: 최대 20배"
    ],
    "signal": "bearish",
    "signal_reason": "<span class=\"text-rose-400 font-medium\">지구 온난화 및 기후 변화</span>로 인한 글로벌 동시 폭염은 농산물 가격 상승, 전력망 과부하 등 거시 경제 리스크를 가중시킴.",
    "key_companies": [
      "Nature Climate Change"
    ],
    "insight": "대기 파동으로 인한 전 지구적 기후 이상 현상은 전력 인프라, 냉방 에너지는 물론 식량 공급망 전체에 파괴적인 인플레이션 압력을 가할 수 있음.",
    "action_point": "여름철 이상 고온에 따른 전력 피크 관련 에너지 인프라 및 원자재/곡물 관련 리스크 관리가 요망됨."
  },
  "classification": {
    "primary_topic": "etc",
    "secondary_topics": ["energy", "economy"],
    "tags": ["로스비파", "제트기류", "지구폭염", "열돔현상", "기후위기"]
  }
})

# Item 4: CdNRPxL86w4
item4 = dump[4]
batch1_data.append({
  "video": {
    "id": item4["id"],
    "title": item4["title"],
    "published": item4["published"],
    "channel_name": item4["channel_name"],
    "url": item4["url"],
    "thumbnail": item4["thumbnail"]
  },
  "analysis": {
    "summary": "미국 <span class=\"text-cyan-300 font-semibold\">트레이더조(Trader Joe's)</span>에서 대박을 친 한국식 LA갈비 및 K-푸드 제품들의 원가·유통 구조와 유전자 상표 표기 규정을 취재함. 소고기 가격은 사상 최고치를 경신 중이나 대표 육가공업체 타이슨푸드는 적자를 기록하는 미국 축산업의 구조적 모순과 원산지 규정(2026년 Product of USA 개정)의 여파를 다룸.",
    "key_claims": [
      "LA갈비는 유대계 절단법(Flanken Cut)에 한국식 간장 양념을 접목하여 미국 한인 이민자들이 재해석해 성공시킨 K-푸드 대표 사례임.",
      "소고기 사육두수 감소로 생두 가격은 최고치이나, 포장 육가공 업체(<span class=\"text-cyan-300 font-semibold\">타이슨푸드</span>)는 가공비 상승과 마진 압박으로 적자를 겪는 수급 불균형이 발생함.",
      "2026년부터 미국 내 도축·사육 소에만 'Product of USA' 표기가 허용되어 육류 유통 공급망 규제가 강화됨."
    ],
    "data_points": [
      "트레이더조 LA갈비 판매가: 14.99달러",
      "트레이더조 김밥 및 떡볶이 가격: 김밥 3.99달러, 떡볶이 4.00달러",
      "미국 육류 원산지 표시(Product of USA) 강제 적용 시점: 2026년 1월 1일"
    ],
    "signal": "neutral",
    "signal_reason": "K-푸드의 미국 시장 입지 강화는 긍정적이나 미국 축산업 원가 상승 및 육가공 마진 악화 리스크가 공존함.",
    "key_companies": [
      "Trader Joe's",
      "Tyson Foods",
      "H Mart"
    ],
    "insight": "K-푸드 유통 제품은 가격 경쟁력과 현지 맞춤형 재해석을 통해 유통망을 확장하고 있으나, 글로벌 식품 원자재 가격과 유통 규제 변경 대응이 수익성을 좌우함.",
    "action_point": "미국 현지 K-푸드 수출 유통기업 및 식품 원자재/육가공 관련 기업의 마진 변동성을 모니터링해야 함."
  },
  "classification": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["K푸드", "트레이더조", "LA갈비", "타이슨푸드", "미국축산업"]
  }
})

Path("scratch/batch1_analysis.json").write_text(json.dumps(batch1_data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Wrote batch 1 to scratch/batch1_analysis.json")
