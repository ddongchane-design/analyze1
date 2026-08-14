import json
from save_batch_helper import save_analyses

batch4_results = [
  {
    "video": {
      "id": "V6Q982egXwU",
      "title": "[박신영의 개장전요것만-8월13일] 앤트로픽, 상장 앞두고 M&A 승부수 | 애크먼이 AI 대신 선택한 기업 | 250년 된 기업이 성장주인 이유",
      "published": "2026-08-13T14:24:26+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=V6Q982egXwU",
      "thumbnail": "https://img.youtube.com/vi/V6Q982egXwU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 도매물가지수(PPI) 둔화와 유가 급락으로 채권 금리가 하락하며 뉴욕 증시가 일제히 상승 출발함. <span class=\"text-cyan-300 font-semibold\">어플라이드 머티리얼즈(AMAT)</span>는 전공정뿐 아니라 HBM/GPU 이종 집적을 위한 첨단 패키징(ASMPT 인수 및 에픽 연구소 협력)으로 실적 기대감을 높이고 있으며, <span class=\"text-cyan-300 font-semibold\">앤트로픽(Anthropic)</span>은 상장을 앞두고 AI 훈련 비용을 대폭 절감해주는 <span class=\"text-cyan-300 font-semibold\">디카트 AI(Decart AI)</span>를 60억 달러에 인수를 추진 중임. 한편 헤지펀드 거물 빌 애크먼은 과열된 AI 곡괭이주 대신 <span class=\"text-cyan-300 font-semibold\">비자(V)</span>, <span class=\"text-cyan-300 font-semibold\">마스터카드(MA)</span>, <span class=\"text-cyan-300 font-semibold\">넷플릭스(NFLX)</span> 등 저평가 독점 플랫폼을 신규 매수했으며, 광통신 대장주 <span class=\"text-cyan-300 font-semibold\">루멘텀(Lumentum)</span>은 사상 첫 분기 매출 10억 달러를 돌파함.",
      "key_claims": [
        "앤트로픽의 디카트 AI(60억 달러) 인수는 GPU 컴퓨팅 효율화 및 AI 훈련 비용 절감을 통해 상장(IPO) 가치를 극대화하기 위한 승부수임.",
        "빌 애크먼은 S&P500 상승분의 85%를 차지한 AI 하드웨어 쏠림을 경계하고, 에이전트 결제 수혜가 기대되는 비자/마스터 및 스트리밍 승자 넷플릭스를 편입함.",
        "루멘텀은 AI 데이터센터 고속 광트랜시버 수요 폭증으로 분기 매출 10억 달러 돌파 및 마진율 50%대를 달성하며 코히어런트를 압도함."
      ],
      "data_points": [
        "어플라이드 머티리얼즈: 올해 주가 104% 급등, 예상 EPS 3.39달러 (+36.7%), 분기 매출 90억 달러.",
        "앤트로픽 디카트 AI 인수액: 60억 달러 (작년 8월 31억 달러 -> 5월 40억 달러 -> 현재 60억 달러로 급등).",
        "루멘텀(Lumentum) 4분기 실적: 매출 11억 달러 돌파 (전년비 +109%), 비GAAP 매출총이익률 50.4%로 급상승.",
        "넷플릭스 지표: 가입자 3억 2,500만 명 돌파, 영업이익률 31.5% 기록."
      ],
      "signal": "bullish",
      "signal_reason": "PPI 안정과 국채 금리 하락 속에서 AI 효율화 M&A(앤트로픽), 첨단 패키징(AMAT), AI 광통신(루멘텀) 및 독점 플랫폼(비자/넷플릭스)의 견고한 실적 모멘텀.",
      "key_companies": [
        "어플라이드 머티리얼즈(AMAT)",
        "루멘텀(LITE)",
        "네비우스(NBIS)",
        "비자(V)",
        "넷플릭스(NFLX)",
        "앤트로픽"
      ],
      "insight": "AI 투자가 단순 하이프에서 AI 훈련 원가 절감(소프트웨어/최적화), 광통신 고속 전송, 첨단 후공정 패키징 등 실질적인 인프라 수익성 개선 기업으로 옥석 가리기가 진행되고 있음.",
      "action_point": "AI 데이터센터 광통신 수혜주 루멘텀/네비우스와 함께, 밸류에이션 부담이 낮고 AI 에이전트 결제 인프라로 재평가받는 비자/마스터카드에 대한 분산 투자를 추천함."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "tech",
        "economy"
      ],
      "tags": [
        "어플라이드머티리얼즈",
        "앤트로픽",
        "디카트AI",
        "빌애크먼",
        "루멘텀",
        "네비우스",
        "한경글로벌마켓"
      ]
    }
  },
  {
    "video": {
      "id": "YCWth3BAECY",
      "title": "팰컨9 달 충돌 영상은 가짜? 다누리가 확인한 진짜 흔적",
      "published": "2026-08-13T11:00:35+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=YCWth3BAECY",
      "thumbnail": "https://img.youtube.com/vi/YCWth3BAECY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "2026년 8월 5일 스페이스X <span class=\"text-cyan-300 font-semibold\">팰컨9</span> 상단부(질량 4.9톤, 초속 2.43km)가 달 아인슈타인 크레이터 인근에 충돌한 사건에서, 한국의 달 궤도선 <span class=\"text-cyan-300 font-semibold\">다누리호(KPLO)</span>가 세계 최초로 충돌 전후 달 표면 변화 흔적을 촬영해 검증에 성공함. 고해상도 카메라(LUTI)와 광시야 편광카메라(PolCam)를 통해 충돌 전 기준 사진과 8차례 촬영한 분출물 방사형 확산 패턴을 확보하여, 달 표토의 <span class=\"text-cyan-300 font-semibold\">우주 풍화</span> 및 인공물 충돌 모델링 연구에 세계적 기준 데이터를 제공함. 칠레 VLT 천문대의 분광 관측에서는 로켓 탱크(알루미늄-리튬 합금) 유래 리튬 방출선이 검출됨.",
      "key_claims": [
        "SNS상에 유포된 팰컨9 달 충돌 순간의 섬광 영상은 모두 AI로 생성된 가짜 영상이며, 실제로는 달 가장자리 뒤편에서 충돌이 일어남.",
        "한국의 다누리호가 충돌 전 사전 촬영과 충돌 직후 8차례 정밀 촬영을 통해 세계 최초로 충돌 흔적과 분출물 확산을 완벽히 포착함.",
        "편광 카메라(PolCam)를 활용한 표토 물성 분석은 달의 우주 풍화 및 차세대 달 탐사 연구에 독보적인 과학 데이터를 제공함."
      ],
      "data_points": [
        "팰컨9 상단부 충돌 제원: 질량 약 4.9톤, 속도 초속 2.43km, 운동에너지 약 145억 줄 (TNT 3톤 폭발 규모).",
        "생성 예상 크레이터 직경: 20~30m 규모.",
        "다누리호 관측: 고해상도 카메라 LUTI 및 편광카메라 PolCam으로 8차례 연속 촬영 성공.",
        "로켓 상단부 리튬 함량: 탱크 벽 알루미늄-리튬 합금 내 약 30kg 함유."
      ],
      "signal": "bullish",
      "signal_reason": "한국 우주항공청(KASA) 및 항우연의 달 탐사선 다누리호의 독보적 궤도 관측 역량 입증과 글로벌 우주 연구 주도권 확보.",
      "key_companies": [
        "스페이스X",
        "한국항공우주연구원"
      ],
      "insight": "다누리호의 선제적 촬영 전략은 글로벌 우주 관측 네트워크에서 한국의 과학 탑재체와 궤도 운영 기술력이 세계 최정상급임을 증명함.",
      "action_point": "우주항공청 출범 이후 본격화되는 국내 우주 탐사 및 인공위성 탑재체/카메라 기술 기업들의 중장기 성장성에 주목할 것."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": [
        "tech"
      ],
      "tags": [
        "다누리호",
        "스페이스X",
        "팰컨9달충돌",
        "항우연",
        "우주풍화",
        "달탐사",
        "안될과학"
      ]
    }
  },
  {
    "video": {
      "id": "Yt-5QjOe5d8",
      "title": "바이든과 똑같은 실수? 물가 민심에 갇힌 트럼프 #교양이를부탁해 #미국중간선거 #트럼프 #미국정치",
      "published": "2026-08-13T11:30:07+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=Yt-5QjOe5d8",
      "thumbnail": "https://img.youtube.com/vi/Yt-5QjOe5d8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "과거 바이든 행정부가 높은 인플레이션과 생활 물가 통제 실패로 대선에서 패배했던 것과 마찬가지로, 트럼프 행정부 역시 관세 인상과 공급망 압박으로 인한 <span class=\"text-rose-400 font-medium\">체감 물가 급등</span>에 갇혀 중간선거 민심 이탈 위기를 맞고 있음. 거시 경제 지표와 달리 유권자들이 매일 마주하는 장바구니 및 기름값 부담이 집권 여당에 가장 치명적인 정치적 뇌관으로 작용함.",
      "key_claims": [
        "트럼프 대통령이 거시 성장률만을 강조하다가 서민들의 실질 체감 물가 압박을 간과하며 바이든 정부와 동일한 정치적 패착을 반복하고 있음.",
        "물가 민심의 반발은 다가오는 중간선거에서 공화당의 상·하원 의석 유지에 최대 위협 요인임."
      ],
      "data_points": [
        "미국 유권자들의 투표 결정 요인 1위: 생활 물가 및 가계 구매력."
      ],
      "signal": "bearish",
      "signal_reason": "체감 물가 상승에 따른 소비 심리 위축 및 중간선거 정치 리스크 심화.",
      "key_companies": [],
      "insight": "선거 국면에서 정치인들의 관세 및 보호무역주의 정책은 필연적으로 국내 수입 물가 상승을 유발하여 자국 유권자의 반발을 사는 딜레마를 초래함.",
      "action_point": "미국 소비재 수요 둔화와 금리 정책 불확실성에 대비하여 방어적 자산 배분을 유지할 것."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": [
        "stock"
      ],
      "tags": [
        "물가민심",
        "트럼프",
        "바이든실수",
        "미국중간선거",
        "인플레이션",
        "소비자부담"
      ]
    }
  },
  {
    "video": {
      "id": "ZL7LDBapR4o",
      "title": "메타, 로보틱스데이에 주가 14% 급등...美 주요 지치 최고치, 금리 인하 기대 속 수혜주는? [모닝 브리핑]",
      "published": "2026-08-13T22:05:34+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=ZL7LDBapR4o",
      "thumbnail": "https://img.youtube.com/vi/ZL7LDBapR4o/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">메타(Meta)</span>가 로보틱스 데이에서 오픈소스 피지컬 AI 플랫폼과 차세대 비전 모델을 공개하며 주가가 하루 만에 <span class=\"text-emerald-400 font-semibold\">14% 급등</span>함. 미국 PPI 지표 안정에 힘입어 9월 금리 인하 기대감이 강화되면서 뉴욕 증시 3대 지수가 일제히 사상 최고치권에 도달함. 빅테크들의 AI 인프라 투자(CapEx) 확대가 소프트웨어뿐 아니라 로보틱스 하드웨어 및 클라우드 서비스 기업들의 전방위적 실적 서프라이즈로 연결되고 있음.",
      "key_claims": [
        "메타의 로보틱스 진출과 피지컬 AI 생태계 선언은 빅테크의 AI 전쟁이 모바일/웹에서 로봇/제조 하드웨어로 전면 확장되었음을 의미함.",
        "물가 지표 완화와 금리 인하 기대가 테크 성장주의 밸류에이션 확장을 강력히 견인하고 있음."
      ],
      "data_points": [
        "메타(Meta) 주가 일간 변동: 로보틱스 데이 발표 후 14% 폭등.",
        "미국 3대 지수(다우, S&P500, 나스닥) 동반 상승세 기록."
      ],
      "signal": "bullish",
      "signal_reason": "메타의 로봇 AI 플랫폼 확장과 금리 인하 수혜가 맞물리며 빅테크 및 피지컬 AI 밸류체인의 강력한 랠리 지속.",
      "key_companies": [
        "메타(META)",
        "엔비디아(NVDA)",
        "테슬라(TSLA)"
      ],
      "insight": "메타의 오픈소스 전략이 라마(LLaMA)에 이어 피지컬 로보틱스 AI 영역까지 확장되면서, 로봇용 AI 모델 개발 속도가 기하급수적으로 빨라지고 있음.",
      "action_point": "메타의 피지컬 AI 오픈소스 생태계와 연계된 로봇 하드웨어 및 AI 엣지 디바이스 관련 수혜주에 적극 관심을 가질 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "robot",
        "tech"
      ],
      "tags": [
        "메타",
        "로보틱스데이",
        "피지컬AI",
        "금리인하기대",
        "뉴욕증시최고치",
        "모닝브리핑"
      ]
    }
  },
  {
    "video": {
      "id": "b0cI1V-RwBE",
      "title": "휴머노이드가 우리에게 줄 최고가치 | New Standard #뉴스탠다드",
      "published": "2026-08-13T07:54:50+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=b0cI1V-RwBE",
      "thumbnail": "https://img.youtube.com/vi/b0cI1V-RwBE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "휴머노이드 로봇이 인류에게 선사할 가장 근본적인 가치는 '노동력의 물리적 한계 해방'과 '24시간 무중단 생산성 혁명'임. 위험하고 반복적인 산업 현장부터 정밀한 조작이 필요한 영역까지 인간의 지능과 신체를 대체함으로써, 기업에는 기하급수적인 원가 절감(ROI 개선)을, 인류에게는 고차원적 창의 영역에 집중할 수 있는 새로운 표준(New Standard)을 제시함.",
      "key_claims": [
        "휴머노이드의 가치는 단순한 자동화 장비를 넘어 인간 노동의 시공간적 한계를 완전히 극복하는 데 있음.",
        "24시간 자율 가동 로봇은 제조 및 서비스 비용을 0원에 가깝게 수렴시키는 디플레이션 혁신을 견인함."
      ],
      "data_points": [
        "로봇 24시간 가동 시 생산성 향상: 기존 인간 교대근무 대비 3배 이상의 연속 작업 효율."
      ],
      "signal": "bullish",
      "signal_reason": "휴머노이드 로봇 도입에 따른 산업 전반의 비약적 생산성 향상과 기업 가치 창출 기대.",
      "key_companies": [
        "테슬라(TSLA)",
        "피규어AI",
        "현대차(005380)"
      ],
      "insight": "로봇 노동의 도입은 노동 공급 부족과 고령화 문제를 해결하는 유일한 구조적 대안이며, 로봇을 가장 빠르게 도입하는 기업이 초과 이윤을 독점할 것임.",
      "action_point": "휴머노이드 로봇 양산 제조사와 핵심 관절 액추에이터 기업에 대한 장기 투자를 유지할 것."
    },
    "classification": {
      "primary_topic": "robot",
      "secondary_topics": [
        "economy",
        "tech"
      ],
      "tags": [
        "휴머노이드가치",
        "24시간생산성",
        "노동력해방",
        "뉴스탠다드",
        "스마트머니"
      ]
    }
  },
  {
    "video": {
      "id": "hAxYUxKxeTc",
      "title": "테슬라 로봇이 사람보다 낫다?!",
      "published": "2026-08-13T11:00:15+00:00",
      "channel_name": "Softdragon SOD",
      "url": "https://www.youtube.com/watch?v=hAxYUxKxeTc",
      "thumbnail": "https://img.youtube.com/vi/hAxYUxKxeTc/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">테슬라(Tesla)</span>의 옵티머스 휴머노이드 로봇이 위험한 배터리 셀 조립 공정 및 무거운 부품 운반 작업에서 인간 작업자 대비 지치지 않고 오차 없는 정밀성을 발휘하는 현장 테스트 성과를 조명함. 인간의 피로, 휴식, 안전사고 위험을 원천 배제하면서 공장 생산 수율을 극대화하는 로봇 노동의 절대적 경제성을 강조함.",
      "key_claims": [
        "테슬라 옵티머스는 실제 공장 현장 배치 테스트에서 인간 대비 높은 작업 균일성과 안전성을 달성함.",
        "기가팩토리 내 로봇 배치는 차량 제조 원가를 극적으로 낮추는 테슬라의 핵심 비밀 병기임."
      ],
      "data_points": [
        "테슬라 기가팩토리 내 옵티머스 로봇 현장 실증 투입 진행 중."
      ],
      "signal": "bullish",
      "signal_reason": "테슬라 옵티머스 로봇의 실제 공정 투입을 통한 제조 원가 절감 및 기술 완성도 입증.",
      "key_companies": [
        "테슬라(TSLA)"
      ],
      "insight": "완성차 제조 라인이 로봇 전용 무인 스마트 팩토리로 진화하면서 테슬라의 마진율 격차가 다시 확대될 것임.",
      "action_point": "테슬라의 로보택시 및 옵티머스 양산 일정을 주시하며 테슬라 밸류체인에 주목할 것."
    },
    "classification": {
      "primary_topic": "robot",
      "secondary_topics": [
        "tech",
        "stock"
      ],
      "tags": [
        "테슬라옵티머스",
        "기가팩토리",
        "로봇생산성",
        "스마트팩토리",
        "소프트드래곤"
      ]
    }
  }
]

if __name__ == "__main__":
    save_analyses(batch4_results)
