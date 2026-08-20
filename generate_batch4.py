import json
from pathlib import Path

batch4 = [
  {
    "video": {
      "id": "O0yOW-JG7eg",
      "title": "[긴급 - 속보효] 갑작스러운 KOSPI 급락, 왜 이러는 걸까요?",
      "published": "2026-06-23T04:14:13+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=O0yOW-JG7eg",
      "thumbnail": "https://img.youtube.com/vi/O0yOW-JG7eg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "코스피의 갑작스러운 급락세는 경제 펀더멘탈의 악화가 아니라 미국의 <span class=\"text-rose-400 font-medium\">단기 채권 금리 상승(2년물 국채 금리 급등)</span>에 따른 물가 경계 심리와 분기말 기관 자금의 <span class=\"text-rose-400 font-medium\">자산배분 리밸런싱</span>이 중첩되며 발생한 단기 발작 현상임. 나스닥 선물 등 글로벌 증시의 낙폭이 제한적인 만큼 차분한 대응이 필요함.",
      "key_claims": [
        "미국채 2년물 금리가 상승하며 이번 주 발표 예정인 PC 물가 지표가 예상보다 높게 나올 수 있다는 경계감이 촉발됨.",
        "분기말을 앞두고 기관 투자자들이 그간 많이 상승한 기술주 비중을 줄이고 자산을 재배분하는 기계적 매도가 출회됨.",
        "글로벌 선물 시장의 낙폭 대비 국내 코스피 지수가 수급 공백으로 인해 유독 과도한 조정을 겪는 괴리 현상이 보임."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "미국 단기 채권 금리 반등과 분기말 자산배분 리밸런싱이라는 일시적 수급 악화 요인이 작용했으나, 실물 매크로 지표의 훼손은 아니기 때문임.",
      "key_companies": [],
      "insight": "단기 급등으로 누적된 차익 실현 욕구가 매크로 지표 발표 경계감과 결합할 때, 수급이 얇은 신흥국 증시가 기계적 리밸런싱의 희생양이 되기 쉬움.",
      "action_point": "공포에 동조해 저가 투매하기보다는 채권 금리 안정화와 리밸런싱 수급 정리가 마무리되는 시점까지 관망하며 주도주 비중을 유지할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["코스피급락", "미국채금리상승", "분기말리밸런싱", "PC경계감", "이효석"]
    }
  },
  {
    "video": {
      "id": "OQL37oW1umQ",
      "title": "꼭대기에서 물렸다...팔고 복구해야 할까? | 빈센트 & 정프로 & 장우진 [더블 체크]",
      "published": "2026-06-23T06:54:12+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=OQL37oW1umQ",
      "thumbnail": "https://img.youtube.com/vi/OQL37oW1umQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "급격한 주가 상승 국면에서 최고점에 진입해 물린 투자자들의 심리적 조급함을 진단하고, 원금 복구를 위해 무리하게 <span class=\"text-rose-400 font-medium\">급등주 추격 매매</span>에 나서는 도박적 투자 행태의 위험성을 엄중히 경고함. 조정을 겪을 때는 뇌동매매를 멈추고 자산의 밸류에이션 호흡을 보정하는 차분한 전략이 요구됨.",
      "key_claims": [
        "급등 최고점에서 물린 조급한 투자자들은 이성적 판단력을 잃고 더 과격한 투기성 종목으로 이동해 패가망신하는 악순환을 겪음.",
        "시장의 일시적 가격 요동 구간에서는 매매 횟수를 늘리기보다 포트폴리오의 펀더멘탈 적합성을 객관적으로 냉정하게 따져야 함.",
        "시장을 도박판으로 대하며 변동성에 기계적으로 휘둘리는 구조에서는 장기적 복리가 절대 불가능함."
      ],
      "data_points": [],
      "signal": "bearish",
      "signal_reason": "시장이 고점 조정을 겪는 시기에 개인들의 극단적 뇌동매매와 급등주 추격 매수 쏠림은 원금 손실을 극대화하는 네거티브 피드백을 형성하기 때문임.",
      "key_companies": [],
      "insight": "투자 성공의 열쇠는 손실 발생 시 억지로 당장 복구하려는 과격한 베팅이 아니라, 하락 원인을 복기하고 매수 가격의 합리성을 검증하는 밸류에이션 복원력에 있음.",
      "action_point": "고점에 물린 상태에서 추가로 급등주를 쫓아가 물타기하는 뇌동매매는 중단하고, 포트폴리오를 우량 대장주 위주로 압축하여 호흡을 길게 가져갈 것."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["투자심리조절", "추격매수경고", "뇌동매매방지", "자산보정", "삼프로더블체크"]
    }
  },
  {
    "video": {
      "id": "ozj0cU8339o",
      "title": "엔비디아가 800V를 꺼낸 이유... GPU보다 먼저 전기가 막혔다 | 800VDC와 한국 전력기업의 기회",
      "published": "2026-06-23T12:37:45+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=ozj0cU8339o",
      "thumbnail": "https://img.youtube.com/vi/ozj0cU8339o/hqdefault.jpg"
    },
    "analysis": {
      "summary": "AI 데이터 센터의 고전력화에 따른 송배전 전력 소모 손실을 획기적으로 줄이기 위해 엔비디아가 차세대 렉 아키텍처에 <span class=\"text-cyan-300 font-semibold\">800VDC 고전압 배전 구조</span>를 전격 도입함. 이로 인해 갈륨나이트라이드(GaN) 및 실리콘카바이드(SiC)와 같은 <span class=\"text-cyan-300 font-semibold\">전력 반도체 생태계</span>가 급성장하고 있으며, 미국 빅테크 데이터 센터에 배전반을 직공급하는 한국 전력 기기사들에게 초대형 수혜를 제공하고 있음.",
      "key_claims": [
        "기존 54V 저전압 배전 방식은 전류량 폭증으로 인한 전선 열화 및 배전 전력 손실(전류 제곱 비례)이 심각해 고전압 변환이 필수적임.",
        "전력 배전의 변환 단계를 혁신적으로 줄이고 효율을 제고하기 위해 TI, 인피니언 등 글로벌 전력 반도체사와 대대적인 협력 표준화가 진행 중임.",
        "한국의 LS일렉트릭 등은 미국 데이터 센터용 배전 기기 및 차단 시스템 수주에 성공하며 핵심 전력 인프라 파트너로 급부상함."
      ],
      "data_points": [
        "배전 아키텍처 변환: 기존 54V 배전망에서 800VDC(직류 고전압) 렉 아키텍처로 엔비디아 가이드라인 재정의",
        "LS일렉트릭 수주 성과: 미국 초대형 빅테크 데이터 센터향 전력 배전 시스템 공급 계약 체결"
      ],
      "signal": "bullish",
      "signal_reason": "엔비디아가 AI 팩토리의 표준 규격을 고전압으로 전환함에 따라 전력 효율 제어가 AI 성능의 핵심으로 등극하였고, 송배전 기기 및 고전압 반도체의 교체 수요가 구조적으로 폭발하기 때문임.",
      "key_companies": ["LS일렉트릭(010120)", "텍사스 인스트루먼트(TXN)", "엔비디아(NVDA)", "지멘스"],
      "insight": "AI 인프라 병목이 데이터 연산 칩을 넘어 데이터 센터의 물리적 전력 전송 효율로 이동하고 있으며, 이는 고전압 배전망을 공급하는 전통 전력 인프라 기업에 막대한 고마진 기회를 제공함.",
      "action_point": "미국 전력망 쇼티지 수혜가 집중되는 국내 초고압 변압기 및 배전반 대장주(LS일렉트릭 등)와 글로벌 고전압 GaN/SiC 전력 반도체 대표주를 적극 편입할 것."
    },
    "classification": {
      "primary_topic": "energy",
      "secondary_topics": ["tech", "stock"],
      "tags": ["800VDC배전", "전력반도체", "LS일렉트릭", "송배전손실", "안될공학"]
    }
  },
  {
    "video": {
      "id": "pdkmdIM5i6g",
      "title": "대문 길이만 300m, 아파트가 성이 됐다 (언더스탠딩 장순원 기자)",
      "published": "2026-06-23T12:25:18+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=pdkmdIM5i6g",
      "thumbnail": "https://img.youtube.com/vi/pdkmdIM5i6g/hqdefault.jpg"
    },
    "analysis": {
      "summary": "DH 방배 등 하이엔드 아파트 재건축 단지들이 성곽처럼 거대 대문을 짓고 입구를 통제하는 등 <span class=\"text-rose-400 font-medium\">도시 주거 문화의 단절성</span>과 폐쇄성 문제를 짚어봄. 부의 과시와 사생활 보호 명분 하에 공공 기여 시설과 보행자 통로가 가로막혀 발생하는 지역 공동체와의 갈등 및 규제 가이드라인의 타당성을 논의함.",
      "key_claims": [
        "강남 재건축 조합들이 수십억 원을 들여 대문 형태의 문주 길이를 극대화하며 단지 외부와의 물리적 차단벽을 구축함.",
        "인근 서민 주택지와의 단절을 초래하고 위화감을 조성한다는 지자체 가이드라인과, 조합의 소유권 주장 및 명품화 의지가 갈등함.",
        "공공 용지를 포함한 단지 내 편의시설 개방을 꺼리는 폐쇄적 커뮤니티 구조가 장기적 도시 안전과 소통을 저해하는 요인이 됨."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "주거 명품화라는 자산 가치 극대화 욕구와 공공성 확보라는 지자체의 도시 가이드라인이 충돌하는 사회적 현상 정보이기 때문임.",
      "key_companies": [],
      "insight": "하이엔드 아파트의 단지 폐쇄화는 한국 특유의 주택 자산 양극화 심리를 투영하며, 물리적 대문 차단은 장기적으로 도시 연계 부가가치를 떨어뜨릴 수 있음.",
      "action_point": "부동산 및 주택 인프라 투자 관점에서는 공공 개방 가이드라인 조율 분쟁으로 인한 사업 지연 가능성 등을 리스크 항목으로 점검할 것."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["아파트문주분쟁", "주거폐쇄성", "DH방배", "도시단절", "언더스탠딩"]
    }
  },
  {
    "video": {
      "id": "qfqVGyRoltc",
      "title": "오늘 같은 날 매수 버튼보다 중요한 것ㅣ명민준, 강아랑, 황유현 [주린이 구조대]",
      "published": "2026-06-23T12:30:35+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=qfqVGyRoltc",
      "thumbnail": "https://img.youtube.com/vi/qfqVGyRoltc/hqdefault.jpg"
    },
    "analysis": {
      "summary": "글로벌 기술주 조정과 스페이스X 회사채 발행에 따른 변동성 노이즈 속에서, 투자자들이 공포에 휩쓸려 무작정 매수/매도 버튼을 누르기보다 <span class=\"text-rose-400 font-medium\">투자 심리 및 호흡 조절</span>에 집중해야 할 시기임. 특히 레버리지 옵션 청산이 동반 매도를 촉발하는 국면에서, 이번 개인 자금은 확실한 이익 체력을 지닌 반도체 등 핵심 실적주로 응집되어 있어 회복력의 질이 다름.",
      "key_claims": [
        "스페이스X 회사채 흥행 성공에도 불구하고 단기 수급 불균형과 레버리지 상품의 강제 청산 매도가 시장 변동성을 극대화함.",
        "과거 뇌동매매와 달리 이번 하락장에서는 개인 자금이 정부 밸류업 정책과 실적이 굳건한 AI 대장주에 정밀히 응집되어 펀더멘탈 지지력이 강함.",
        "단기 폭락 국면에서 호가창이 얇은 코스닥 소형주 위주로 발생하는 극단적인 기계적 투매(반대매매 루프)에 휘둘리지 말아야 함."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "파생 수급 청산에 의한 강제 하방 압력이 지수를 왜곡하고 있지만, 주도 섹터의 이익 응집력과 실적 펀더멘탈은 유효한 숨고르기 국면이기 때문임.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "스페이스X"],
      "insight": "시장이 수급 노이즈로 30%씩 흔들릴 때 진정한 우량주라면 오히려 기관/외인이 저가 매수에 동참하므로, 매도가 매도를 부르는 패닉 심리를 스스로 끊어내야 함.",
      "action_point": "극도로 과열되었던 단기 레버리지 ETF 베팅 비중은 덜어내어 현금을 일부 확보하고, 실적 펀더멘탈이 검증된 반도체 대표주의 비중은 흔들림 없이 고수할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["투자심리진정", "레버리지청산", "반대매매우려", "실적주응집력", "황유현"]
    }
  },
  {
    "video": {
      "id": "qMdZRJoOylY",
      "title": "반도체주 조정장, 손절보다 중요한 건 '매수 가격'입니다ㅣ김장열 유니스토리자산운용 리서치센터장 [집중 오늘의 주식]",
      "published": "2026-06-23T11:30:20+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=qMdZRJoOylY",
      "thumbnail": "https://img.youtube.com/vi/qMdZRJoOylY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "빅테크의 Capex 조달(회사채 발행) 및 수급 청산 노이즈와 국내 <span class=\"text-rose-400 font-medium\">미실현 이익 과세 보도</span>가 겹쳐 투자 심리가 얼어붙었으나, 반도체 제조 기업들의 실적 지속성은 굳건함. 조정장에서 손절하기보다는 목표 밸류에이션 대비 0.7~0.8 수준을 곱한 <span class=\"text-cyan-300 font-semibold\">보수적 분할 매수가격 가이드</span>(삼성전자 30만 원 이하, SK하이닉스 200만 원 이하 등 보수적 타겟 라인 조정)로 리스크를 관리해야 함.",
      "key_claims": [
        "스페이스X, 슈퍼마이크로 등 테크 기업들의 대규모 설비투자용 조달이 차익 실현 빌미가 되었으나 설비 투자 증가 흐름 자체는 견고함.",
        "미실현 이익에 대한 포괄적 과세 뉴스 논란이 주식 시장 내 패닉성 심리 악화 및 수급 왜곡을 추가적으로 증폭시킴.",
        "마이크론 실적 발표에서 HBM의 극단적 타이트 공급 및 AI 서버향 범용 D램 쇼티지를 재차 확인해 줄 것인지가 단기 방향성의 핵심임."
      ],
      "data_points": [
        "보수적 매수 밴드 가이드(목표가 대비 0.7~0.8 곱 적용): 삼성전자 조정 시 30만 원 이하 분할, SK하이닉스 200만 원 이하 접근 추천 (실질 주가 액면 병합/수정 주가 기준 추정)",
        "마이크론 분기 타겟 가이던스: 시장 기대치를 충족하려면 다음 분기 주당순이익(EPS) 20달러 후반대 및 다음 분기 가이던스 컨센서스 상회가 필요"
      ],
      "signal": "neutral",
      "signal_reason": "미실현 이익 과세 논란 등 세제 센티멘트 훼손과 단기 수급 과열 청산이 겹쳤으나, 반도체 공급 통제권 및 고마진 HBM 영업이익의 장기 지속 체력은 유효하기 때문임.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "마이크론(MU)", "슈퍼마이크로컴퓨터(SMCI)"],
      "insight": "AI 투자의 거시 대세는 무너지지 않지만, 주가의 밸류에이션 상단이 한껏 몰렸을 때는 보수적인 20~30% 마진 안전마진(할인율)을 적용해 분할 진입하는 태도가 계좌를 보존함.",
      "action_point": "패닉에 동조해 손절하기보다, 자체 설정한 우량 반도체 타겟 매수가(목표가 대비 20~30% 할인 가격대) 도달 시에만 차분히 분할 매수로 비중을 채워갈 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["매수가격가이드", "미실현이익과세", "안전마진확보", "마이크론실적대기", "김장열"]
    }
  },
  {
    "video": {
      "id": "RA8i99-yDDc",
      "title": "LG전자 로보티즈 액추에이터 생산 및 휴머노이드 협력?",
      "published": "2026-06-23T10:40:15+00:00",
      "channel_name": "엔지니어TV",
      "url": "https://www.youtube.com/watch?v=RA8i99-yDDc",
      "thumbnail": "https://img.youtube.com/vi/RA8i99-yDDc/hqdefault.jpg"
    },
    "analysis": {
      "summary": "LG전자가 우량 감속기 및 로봇 관절 부품사인 로보티즈의 우즈베키스탄 법인 지분 투자 및 <span class=\"text-cyan-300 font-semibold\">액추에이터(Actuator) 공동 생산 MOU</span>를 체결함. 이는 LG전자가 가전/상업용 대량 제조 노하우를 로보티즈의 감속기 설계력과 융합하여 핵심 구동부 대량 생산 체인을 내재화하고, 중국산 하드웨어를 대체할 독자적 <span class=\"text-cyan-300 font-semibold\">피지컬 AI 학습 데이터 주권</span>을 장악하려는 전략적 포석임.",
      "key_claims": [
        "LG전자의 모터 제어 역량과 로보티즈의 초정밀 감속기 및 다이나믹셀 특허를 융합해 최저 원가의 로봇 액추에이터 라인을 구축함.",
        "로보티즈가 공개한 AI 기반 휴머노이드 플랫폼 'AI 사피엔스'는 모션 캡처 없이 유튜브 학습만으로 동작(춤 등)을 구현해 중국 격차를 줄임.",
        "중국산 로봇 하드웨어 유니트리를 대량 채용할 경우, 로봇 구동 및 제어 데이터가 중국 서버로 귀속되는 심각한 데이터 종속 우려가 존재함."
      ],
      "data_points": [
        "로보티즈 우즈벡 생산 프로젝트 규모: 1차 500억 원 집행 및 중장기 2,000억 원 규모 확장 계획",
        "LG전자의 로보티즈 지분율: 기존 6.56% 보유 상태에서 우즈벡 합작 법인 추가 지분(약 49% 수준) 취득 검토"
      ],
      "signal": "bullish",
      "signal_reason": "글로벌 휴머노이드 경쟁이 본격화되는 가운데, 원가 비중이 가장 높은 액추에이터의 글로벌 대량 생산 벨트를 확보하고 피지컬 AI 훈련 데이터의 국산 주권을 지키는 협력이기 때문임.",
      "key_companies": ["로보티즈(090950)", "LG전자(066570)", "유니트리", "테슬라(TSLA)"],
      "insight": "휴머노이드의 상용화 경쟁력은 단순 하드웨어를 넘어, 자체 제조 로봇을 다양한 실제 서비스 현장(가전, 물류, 상업 공간)에 배치해 반복적인 행동 학습 데이터의 선순환을 완성하느냐에 달려 있음.",
      "action_point": "중국산 하드웨어를 배제하려는 글로벌 피지컬 AI 공급망 재편 기조 속에서, 독보적 휴머노이드 관절 감속기 특허와 LG전자의 제조 동맹 수혜를 입는 로보티즈의 지분을 장기 포트폴리오에 축적할 것."
    },
    "classification": {
      "primary_topic": "robot",
      "secondary_topics": ["tech", "stock"],
      "tags": ["로보티즈합작", "LG전자로봇", "액추에이터양산", "데이터주권", "AI사피엔스"]
    }
  },
  {
    "video": {
      "id": "stn7VEcKMiw",
      "title": "[26.06.23 오후 방송 전체보기] '검은 화요일' 코스피 10% 폭락...외국인 매도 폭탄 개인이 간신히 방어했다",
      "published": "2026-06-23T11:08:10+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=stn7VEcKMiw",
      "thumbnail": "https://img.youtube.com/vi/stn7VEcKMiw/hqdefault.jpg"
    },
    "analysis": {
      "summary": "코스피의 10% 폭락 사태는 미국의 연내 기준금리 3회 인상 경고, 국내 세제 개편(미실현 이익 과세) 논란 및 <span class=\"text-rose-400 font-medium\">3배 레버리지 ETF 금감원 규제 노이즈</span>가 복합 작용하여 발생한 '검은 화요일' 수급 붕괴임. 삼성전자는 업계 최초로 <span class=\"text-cyan-300 font-semibold\">HBM4 분기 매출 10억 달러 속보치</span>를 발표하며 펀더멘탈 가시성을 입증한 만큼, 역사적 학습 효과상 지수 반등 시 가장 빠르게 복원될 섹터는 역시 반도체 대장주임.",
      "key_claims": [
        "BofA의 매파적 금리 전망 변경과 파생 규제 우려가 맞물려, 그동안 반도체에 극단적으로 쏠려 있던 ETF의 매도 루프를 강제 촉발함.",
        "삼성전자는 최초 분기 HBM4 매출 10억 달러 돌파 및 연말 100억 달러 목표 가이던스를 속보로 제시하여 확실한 이익 체력을 입증함.",
        "과거 대형 변동성 장세마다 시장이 안정을 찾은 뒤 가장 신속하게 전고점을 복구한 섹터는 예외 없이 이익 증가세가 유효했던 반도체였음."
      ],
      "data_points": [
        "삼성전자 HBM4 속보 실적: 단일 분기 최초 매출 10억 달러 돌파 (연말 누적 100억 달러 달성 목표 공식화)",
        "코스피 단기 급락률: 하루 기준 장중 약 10% 내외의 역사적 대폭락 장세 시현"
      ],
      "signal": "bullish",
      "signal_reason": "레버리지 규제 및 세제 논란 등 일시적인 감정적 수급 충격에 따른 주가 왜곡일 뿐, HBM4 최초 10억 달러 매출 증명 등 메모리 대형사들의 펀더멘탈 마진 확장 추세는 무너지지 않았기 때문임.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "현대자동차"],
      "insight": "지수가 공포와 파생 상품 강제 매물로 무차별 무너질 때, HBM 독점 마진 및 연말 누적 100억 달러 도달 가시성이 확인된 실질적 대장주를 담는 것이 역사적 반등장에서 극도의 초과 이익을 주는 매커니즘임.",
      "action_point": "규제 노이즈 및 세금 공포에 동조해 패닉셀하지 말고, HBM4 공급 실적이 실물 수치로 최초 증명된 삼성전자와 대표 주도주 SK하이닉스를 최우선으로 매수 비중을 확보할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["코스피폭락", "레버리지규제", "금투세논란", "HBM4매출속보", "바겐세일기회"]
    }
  }
]

scratch_dir = Path("scratch")
scratch_dir.mkdir(exist_ok=True)
Path("scratch/batch4.json").write_text(json.dumps(batch4, ensure_ascii=False, indent=2), encoding="utf-8")
print("Wrote batch4.json")
