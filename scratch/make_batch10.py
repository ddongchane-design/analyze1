import json, sys
from pathlib import Path

dump = json.loads(Path("scratch/pending_final4_dump.json").read_text(encoding="utf-8"))
batch10_data = []

# Item 0: fMdbBpWWW3g
item0 = dump[0]
batch10_data.append({
  "video": {
    "id": item0["id"],
    "title": item0["title"],
    "published": item0["published"],
    "channel_name": item0["channel_name"],
    "url": item0["url"],
    "thumbnail": item0["thumbnail"]
  },
  "analysis": {
    "summary": "미국과 이란 간의 지정학적 장기전 및 <span class=\"text-rose-400 font-medium\">패트리엇 미사일 재고 소진(1,700기 미만)</span> 우려 속에서 유가 및 석유 정제 시설 공급망 충격 여파를 분석함. 홍해 후티 방군 및 이라크 민병대의 장기전으로 정제유(디젤) 가격 및 빅테크 정책 환경에 미치는 거시적 영향을 조명함.",
    "key_claims": [
      "미국의 패트리엇 요격 미사일 재고가 1,700기 미만으로 감축되어 중동 지정학 방어 체계의 한계가 노출됨.",
      "단순 원유 공급 차단을 넘어 석유 정제 시설 부재에 따른 휘발유·디젤 실물 공급망 쇼티지 가능성이 제기됨.",
      "<span class=\"text-amber-300 font-bold\">중동 지정학 장기화</span>에 따라 미국 정치권의 빅테크 규제 및 유가 조절 정책에 새로운 변수로 작용함."
    ],
    "data_points": [
      "미국 패트리엇 요격 미사일 보유 재고: 1,700기 미만",
      "지정학 개입 주체: 이란, 후티 방군, 이라크 민병대, 사우디, 미국",
      "주요 위험 자산: WTI 유가, 정제유(디젤) 선물 가격"
    ],
    "signal": "neutral",
    "signal_reason": "중동 지정학 불안에 따른 유가 변동성이 존재하나 공급망 재편 및 인프라 방산 수혜가 교차함.",
    "key_companies": [
      "Lockheed Martin",
      "Saudi Aramco"
    ],
    "insight": "중동의 지정학적 리스크가 점조직 민병대 중심의 장기 분열전으로 교체됨에 따라 단순 원유 가격뿐 아니라 방산 재고 및 정제유 공급망 전체의 가치를 재평가해야 함.",
    "action_point": "유가 변동성 확대 및 방산 재고 확충 관련 글로벌 방산·정유주의 수혜 가능성을 예의주시해야 함."
  },
  "classification": {
    "primary_topic": "economy",
    "secondary_topics": ["energy", "stock"],
    "tags": ["중동지정학", "패트리엇재고", "유가변동성", "정제유공급망", "미국외교"]
  }
})

# Item 1: GzkLqg9zx_Q
item1 = dump[1]
batch10_data.append({
  "video": {
    "id": item1["id"],
    "title": item1["title"],
    "published": item1["published"],
    "channel_name": item1["channel_name"],
    "url": item1["url"],
    "thumbnail": item1["thumbnail"]
  },
  "analysis": {
    "summary": "충북대학교 화학공학과 연구팀이 개발한 <span class=\"text-cyan-300 font-semibold\">노화 억제 및 운동 능력 2배 향상 항노화(Anti-aging) 신소재</span> 연구 결과를 소개함. 70대 연령 상당의 고령 노화 쥐 실험에서 근육 지구력과 대사 활성도를 획기적으로 개선한 바이오 화학 신물질의 작용 기전과 상용화 가능성을 다룸.",
    "key_claims": [
      "충북대 연구진이 고령 쥐 대상 신물질 투여 임상에서 운동 주행 거리가 기존 대비 2배 향상되는 항노화 효능을 입증함.",
      "근육 손실 억제 및 세포 미토콘드리아 대사 활성화 기전을 통해 역연령(Rejuvenation) 바이오 신약 기술의 가능성을 열음.",
      "<span class=\"text-amber-300 font-bold\">항노화 바이오 신소재 기술</span>이 에이징 테크 및 실버 헬스케어 시장의 게임 체인저로 부상함."
    ],
    "data_points": [
      "임상 대상: 70대 연령 상당의 노화 실험 쥐",
      "효능 지표: 운동 지속 능력 및 주행 거리 2배(200%) 증가",
      "연구 주체: 충북대학교 화학공학과 김범수 교수 연구팀"
    ],
    "signal": "bullish",
    "signal_reason": "<span class=\"text-cyan-300 font-semibold\">국산 바이오 항노화 물질 개발</span>로 실버 바이오 헬스케어 산업의 고부가가치 기술 경쟁력 입증.",
    "key_companies": [
      "충북대학교",
      "한국연구재단"
    ],
    "insight": "고령화 사회로 진입함에 따라 근감소증 및 항노화 메커니즘을 타겟팅하는 바이오 신소재/신약 파이프라인의 상업적 가치가 비약적으로 높아질 것임.",
    "action_point": "항노화 헬스케어 및 대사 개선 파이프라인을 다루는 바이오 벤처 및 관련 화학 신소재 기업의 임상 진행 경과를 주목해야 함."
  },
  "classification": {
    "primary_topic": "tech",
    "secondary_topics": ["etc"],
    "tags": ["항노화신물질", "충북대연구팀", "근감소증치료", "바이오헬스케어", "역연령기술"]
  }
})

# Item 2: L78E69zPejs
item2 = dump[2]
batch10_data.append({
  "video": {
    "id": item2["id"],
    "title": item2["title"],
    "published": item2["published"],
    "channel_name": item2["channel_name"],
    "url": item2["url"],
    "thumbnail": item2["thumbnail"]
  },
  "analysis": {
    "summary": "달러/엔 환율이 162엔을 기록하며 <span class=\"text-amber-300 font-bold\">40년 만의 엔저 및 실질실효환율 55년 최저치</span>를 경신한 일본 경제의 구조적 역설을 분석함. 극심한 엔저가 일본 국민의 구매력을 떨어뜨렸으나, 서비스 수출(인바운드 외국인 관광) 폭증과 실질 GDP 0.25%p 상승 효과를 창출하며 '비정상의 정상화'로 평가받는 일본의 금융 완화 전략을 다룸.",
    "key_claims": [
      "달러/엔 환율 160엔 돌파로 실질실효환율 기준 구매력이 1970년 수준(55년 만의 최저)으로 하락함.",
      "10% 엔저 유지 시 서비스 인바운드 관광과 서비스 수출 증가에 힘입어 일본 실질 GDP를 약 +0.25%p 밀어 올리는 긍정적 효과가 발생함.",
      "<span class=\"text-cyan-300 font-semibold\">일본 정치권(다카이치 등 적극재정파)</span>은 140~150엔대의 엔화 수준을 일본의 체질 개선 기회로 활용하고 있음."
    ],
    "data_points": [
      "달러/엔 환율: 최대 162엔 돌파 (40년 만의 엔저)",
      "실질실효환율 기준: 1970년 이후 55년 만의 최저 수준",
      "엔저의 실질 GDP 기여도: 10% 엔저 지속 시 실질 GDP +0.25%p 밀어 올림"
    ],
    "signal": "bullish",
    "signal_reason": "<span class=\"text-amber-300 font-bold\">엔저를 활용한 일본 실질 GDP 성장</span> 및 인바운드 관광 서비스 수지 호조로 일본 기업 실적 및 증시에 긍정적 탄력 제공.",
    "key_companies": [
      "Bank of Japan",
      "일본 관광청",
      "도요타"
    ],
    "insight": "과거 고평가된 엔고(70엔대) 미스테리에서 벗어나 저평가 엔저를 적극 재정 정책과 결합하여 글로벌 인바운드 자금을 쓸어 담는 일본 경제의 체질 전환에 주목해야 함.",
    "action_point": "엔저 수혜를 받는 일본 인바운드 관련 유통/서비스 및 수출형 완성차/전자 기업들의 실적 호조세를 포트폴리오에 활용해야 함."
  },
  "classification": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["일본엔저", "실질실효환율", "일본GDP", "인바운드관광", "다카이치재정"]
  }
})

# Item 3: RPF4G5jH8bc
item3 = dump[3]
batch10_data.append({
  "video": {
    "id": item3["id"],
    "title": item3["title"],
    "published": item3["published"],
    "channel_name": item3["channel_name"],
    "url": item3["url"],
    "thumbnail": item3["thumbnail"]
  },
  "analysis": {
    "summary": "삼성전자 및 SK하이닉스의 주가 조정기에 <span class=\"text-amber-300 font-bold\">'펀더멘탈 가치를 할인된 가격에 사는 역발상 가치 투자 원칙'</span>을 제시함. AI 데이터센터 인허가 및 금융 PF 리스크 우려를 점검하며, 공포 장세 속에서 검증된 반도체 우량주를 저가 분할 매수하는 가치 중심 전략을 해설함.",
    "key_claims": [
      "투자 성공의 본질은 가격이 비쌀 때 뇌동매수하는 것이 아니라, 검증된 우량주의 가치를 불황과 할인 시기에 싸게 얻는 데 있음.",
      "가을 이후 데이터센터 PF 및 대출 인허가 리스크가 조정을 유발할 수 있으나 본질적 AI 펀더멘탈 흐름은 훼손되지 않음.",
      "<span class=\"text-cyan-300 font-semibold\">삼성전자 및 하이닉스</span>의 장기 가치 대비 현재 가격의 할인가(Margin of Safety)를 측정해야 승자가 됨."
    ],
    "data_points": [
      "가치 투자 대전제: 가치(Value)와 가격(Price)의 괴리 활용",
      "리스크 검증 포인트: 데이터센터 PF 자금 조달 및 전력망 인허가 추이",
      "매수 최적 타점: 시장의 공포 및 하락 조정기 (할인 구간)"
    ],
    "signal": "bullish",
    "signal_reason": "<span class=\"text-amber-300 font-bold\">반도체 펀더멘탈의 할인가 진입</span>으로 조정기를 활용한 장기 분할 매수 모멘텀이 극대화됨.",
    "key_companies": [
      "삼성전자",
      "SK하이닉스"
    ],
    "insight": "가격에 휘둘리는 군중 심리에서 벗어나 펀더멘탈 가치가 명확한 반도체 대장주를 할인 구간에서 모아가는 장기 투자자가 최종 승자가 됨.",
    "action_point": "주가 조정 시 삼성전자 및 SK하이닉스의 분할 매수 타점을 잡고, 펀더멘탈 수혜를 지속 점검해야 함."
  },
  "classification": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["가치투자", "삼성전자", "SK하이닉스", "반도체할인매수", "데이터센터PF"]
  }
})

Path("scratch/batch10_analysis.json").write_text(json.dumps(batch10_data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Wrote batch 10 to scratch/batch10_analysis.json")
