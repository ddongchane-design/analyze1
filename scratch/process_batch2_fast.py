import json
from save_batch_helper import save_analyses

batch2_results = [
  {
    "video": {
      "id": "6YqDZC7NZ8U",
      "title": "DDR4 구형 모델 가격이 오른 이유",
      "published": "2026-08-13T08:30:27+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=6YqDZC7NZ8U",
      "thumbnail": "https://img.youtube.com/vi/6YqDZC7NZ8U/hqdefault.jpg"
    },
    "analysis": {
      "summary": "구형 규격인 <span class=\"text-cyan-300 font-semibold\">DDR4</span> D램 가격이 최근 반등한 배경을 분석함. 주요 메모리 제조사들이 DDR5와 HBM 등 고부가 차세대 공정으로 생산 라인을 대거 전환하면서 DDR4 공급 여력이 극도로 축소된 상태에서, AI 데이터센터 확장에 따른 <span class=\"text-cyan-300 font-semibold\">기업용 SSD(eSSD)</span> 캐시용 D램 수요가 맞물려 발생한 공급 불균형 현상임.",
      "key_claims": [
        "DDR4 가격 상승은 레거시 수요의 전반적 부활이라기보다, 공급이 이미 축소된 특정 규격에 기업용 SSD 버퍼 메모리 수요가 집중되어 나타난 현상임.",
        "메모리 제조사들의 선단 공정(DDR5/HBM) 집중으로 구형 레거시 D램의 공급 쇼티지가 단기 가격 왜곡을 유발함."
      ],
      "data_points": [
        "서버 메인 메모리/PC/모바일이 D램 수요의 핵심이나, eSSD용 D램 추가 주문이 타이트한 DDR4 공급망을 자극함."
      ],
      "signal": "neutral",
      "signal_reason": "DDR4 가격 상승은 공급 축소와 일시적 SSD 수요가 빚어낸 니치 마켓 현상으로, 메모리 산업 전반의 성장 동력은 여전히 DDR5/HBM에 집중되어 있음.",
      "key_companies": [
        "삼성전자(005930)",
        "SK하이닉스(000660)"
      ],
      "insight": "제조사들의 선제적인 공급 감축(CapEx 통제)이 유지되는 한, 레거시 제품군에서도 작은 수요 변화에 따른 가격 변동성이 크게 나타날 수 있음을 시사함.",
      "action_point": "구형 메모리 가격 반등에 따른 단기 수혜보다는 첨단 HBM3E/HBM4 및 서버용 DDR5 시장 지배력을 가진 선도 업체를 중심으로 포트폴리오를 유지할 것."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": [
        "stock"
      ],
      "tags": [
        "DDR4",
        "D램가격",
        "기업용SSD",
        "메모리반도체",
        "SK하이닉스",
        "삼성전자"
      ]
    }
  },
  {
    "video": {
      "id": "7mTmM9fx3mI",
      "title": "같은 날 한쪽은 폭우, 한쪽은 39.5도?!",
      "published": "2026-08-13T02:00:12+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=7mTmM9fx3mI",
      "thumbnail": "https://img.youtube.com/vi/7mTmM9fx3mI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "동일한 날씨 조건에서 동해안(강릉)은 시간당 80mm의 기록적 폭우가 쏟아진 반면, 산지 서쪽인 경기 화성은 39.5도의 극심한 폭염을 기록한 기상 이변의 과학적 원리를 <span class=\"text-cyan-300 font-semibold\">푄 현상(Foehn Phenomenon)</span>으로 설명함. 태풍의 반시계 방향 회전으로 동해의 습한 공기가 태백산맥을 넘으며 비를 뿌리고 잠열을 방출한 뒤, 서쪽으로 하강하면서 단열 압축(100m당 1도 상승)되어 초고온 건조 공기로 변모한 메커니즘을 규명함.",
      "key_claims": [
        "습한 공기가 산지를 상승할 때는 수증기 응결 잠열로 100m당 약 0.5도 하강하지만, 비를 뿌리고 건조해진 공기가 하강할 때는 100m당 약 1도씩 빠르게 기온이 상승함.",
        "한반도의 남북 산맥 지형과 태풍 순환이 결합하여 동쪽 폭우-서쪽 극단 폭염의 극단적 날씨 양극화를 유발함."
      ],
      "data_points": [
        "수증기 응결 잠열: 물 1kg 응결 시 약 240만 줄(J) 방출.",
        "공기 온도 변화율: 습윤 상승 시 100m당 약 0.5도 하강, 건조 하강 시 100m당 약 1.0도 상승.",
        "실제 관측치: 8월 8일 강원 동해안 시간당 80mm+ 폭우 vs 경기 화성 최고 기온 39.5도."
      ],
      "signal": "na",
      "signal_reason": "대기역학 및 지형성 기상 메커니즘을 다룬 순수 과학/기상 교육 콘텐츠임.",
      "key_companies": [],
      "insight": "기후 변화와 지형 효과가 맞물리며 동일 국가 내에서도 지역별 극단적 기상 이변(국지성 호우 vs 폭염)이 일상화되고 있어 인프라 대비가 중요함.",
      "action_point": "극단적 이상기후에 대응하는 전력망 인프라 및 냉방/재난 방재 관련 산업의 구조적 수요 증가에 주목할 것."
    },
    "classification": {
      "primary_topic": "culture",
      "secondary_topics": [
        "tech"
      ],
      "tags": [
        "푄현상",
        "태백산맥",
        "기상이변",
        "폭우폭염",
        "대기과학",
        "안될과학"
      ]
    }
  },
  {
    "video": {
      "id": "BG6p32gTlDc",
      "title": "휴머노이드 출하량 90% 장악한 국가?! | New Standard #뉴스탠다드",
      "published": "2026-08-13T07:47:45+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=BG6p32gTlDc",
      "thumbnail": "https://img.youtube.com/vi/BG6p32gTlDc/hqdefault.jpg"
    },
    "analysis": {
      "summary": "인공지능이 디지털 모니터를 넘어 물리적 신체를 획득하여 스스로 학습하고 행동하는 <span class=\"text-cyan-300 font-semibold\">임바디드 AI(Embodied AI)</span> 시대로 진입함. 최근 글로벌 보고서에 따르면 전 세계 휴머노이드 로봇 출하량의 무려 <span class=\"text-emerald-400 font-semibold\">90%</span>가 단 한 국가(중국)에서 생산되어 쏟아져 나오고 있으며, 이는 단순한 기술 시연을 넘어 거대한 산업 생태계와 양산 공급망의 패러다임 전환이 본격화되었음을 증명함.",
      "key_claims": [
        "AI가 물리적 육체를 입는 임바디드 AI가 차세대 산업 혁신의 핵심 축으로 부상함.",
        "글로벌 휴머노이드 출하량의 90%가 중국에서 집중 배출되며 로봇 양산 경쟁의 주도권을 장악하고 있음."
      ],
      "data_points": [
        "글로벌 휴머노이드 로봇 출하량 중 단일 국가(중국) 점유율: 90% 장악."
      ],
      "signal": "bullish",
      "signal_reason": "휴머노이드 로봇 산업이 연구실 단계에서 대량 출하 및 상용화 단계로 폭발적 성장을 시작함.",
      "key_companies": [
        "유니트리(Unitree)",
        "테슬라(TSLA)",
        "현대차(005380)"
      ],
      "insight": "로봇의 소프트웨어 AI 지능뿐 아니라 저렴하고 정밀한 하드웨어 양산 인프라를 장악한 진영이 초기 시장의 실질적인 승자가 되고 있음.",
      "action_point": "휴머노이드 양산 경쟁에서 핵심 부품(감속기, 액추에이터, 센서) 및 임바디드 AI 플랫폼을 주도하는 선두 기업에 주목해야 함."
    },
    "classification": {
      "primary_topic": "robot",
      "secondary_topics": [
        "tech",
        "stock"
      ],
      "tags": [
        "임바디드AI",
        "휴머노이드",
        "로봇출하량",
        "로봇생태계",
        "스마트머니",
        "중국로봇"
      ]
    }
  },
  {
    "video": {
      "id": "C2DeAh7RzQo",
      "title": "휘발유 갤런당 4달러 돌파... 트럼프 흔드는 체감 물가 #교양이를부탁해 #미국중간선거 #트럼프 #미국정치",
      "published": "2026-08-13T11:15:34+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=C2DeAh7RzQo",
      "thumbnail": "https://img.youtube.com/vi/C2DeAh7RzQo/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 유권자들의 체감 물가를 나타내는 핵심 지표인 전국 평균 휘발유 가격이 <span class=\"text-rose-400 font-medium\">갤런당 4달러</span>를 돌파함(한국 기준 리터당 약 1,900원에 해당). 대중교통 의존도가 낮고 자가용 이용이 필수적인 미국 서민들의 직접적 생활비 부담이 가중되면서, 중간선거를 앞둔 트럼프 행정부의 지지율에 치명적인 타격을 주고 있음.",
      "key_claims": [
        "미국 휘발유 가격 갤런당 4달러 돌파는 서민 유권자들의 가계 지출에 직접적인 타격을 주는 심리적 저항선임.",
        "체감 유가 상승은 중간선거에서 집권 여당에 가장 불리하게 작용하는 핵심 경제 변수임."
      ],
      "data_points": [
        "미국 전국 평균 휘발유 가격: 갤런당 4달러 초과 (국내 체감 기준 약 리터당 1,900원 수준)."
      ],
      "signal": "bearish",
      "signal_reason": "유가 상승에 따른 인플레이션 압력과 미국 중간선거를 앞둔 집권당의 정치적 불확실성 증대.",
      "key_companies": [],
      "insight": "미국의 소비 여력 둔화와 금리 인하 지연 우려는 유가 안정 여부에 직결되어 있으며, 유가 안정이 실패할 경우 긴축 기조가 장기화될 수 있음.",
      "action_point": "유가 및 에너지 가격 추이를 모니터링하며 에너지 관련 인플레이션 헤지 자산과 소비재 섹터의 실적 둔화 가능성을 체크할 것."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": [
        "stock"
      ],
      "tags": [
        "휘발유가격",
        "갤런당4달러",
        "미국물가",
        "트럼프지지율",
        "중간선거",
        "인플레이션"
      ]
    }
  },
  {
    "video": {
      "id": "CA4mGzVgRvE",
      "title": "테라팹, 기존 EUV 안쓰는 미친 구상 | 입자가속기 도입이 현실이 되는 이유 |  FEL-EUV의 가능성",
      "published": "2026-08-13T03:03:26+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=CA4mGzVgRvE",
      "thumbnail": "https://img.youtube.com/vi/CA4mGzVgRvE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "일론 머스크가 구상하는 초대형 반도체 공장 '테라팹(Terafab)'의 혁신 기술로 거론되는 <span class=\"text-cyan-300 font-semibold\">FEL-EUV(자유전자레이저 EUV)</span>를 심층 분석함. 기존 ASML의 주석(Sn) 액적 플라즈마 방식(초당 6만 번 레이저 타격) 대신, 전자를 빛의 속도로 가속하여 언듈레이터(Undulator)를 통과시켜 강력한 13.5nm EUV 빛을 생산하는 입자가속기 기반 광원임. 단일 가속기 시설에서 빛을 생산해 <span class=\"text-emerald-400 font-semibold\">최대 16대의 스캐너</span>로 분배하는 'Light as a Utility' 개념과 에너지 회수형 선형 가속기(<span class=\"text-cyan-300 font-semibold\">ERL</span>)를 접목해 전력 소비를 줄이는 차세대 노광 인프라임. 미국 정부의 칩스법 1.5억 달러 지원(xLight 개발)과 함께 프로토타입 실증 단계로 진입 중임.",
      "key_claims": [
        "FEL-EUV는 주석 오염과 출력 한계가 있는 기존 EUV 광원을 대체해 입자가속기 기반의 무오염·초고출력 빛을 중앙에서 유틸리티 형태로 공급하는 혁신 기술임.",
        "공장 규모가 극단적으로 거대해지는 테라팹 환경에서는 단일 FEL 가속기로 16대 이상의 노광기를 동시 구동하여 규모의 경제를 달성할 수 있음.",
        "FEL이 상용화되더라도 ASML의 노광 스캐너 장비 자체가 대체되는 것은 아니며, 광원 공급 방식의 혁신으로 이해해야 함."
      ],
      "data_points": [
        "현재 ASML EUV 방식: 초당 6만 번 주석 방울 타격, 최대 1000W급 연구 출력.",
        "포항 4세대 방사광가속기(PAL-XFEL): 가속 구간 780m, 언듈레이터 250m, 건설비 약 4,000억 원 규모.",
        "xLight의 FEL 구상: 단일 가속기 시스템으로 최대 16대 스캐너 동시 지원.",
        "미국 칩스법(CHIPS Act) 지원: 뉴욕 올버니 나노테크 컴플렉스 xLight FEL 프로토타입에 1억 5천만 달러 지원 확정."
      ],
      "signal": "bullish",
      "signal_reason": "초미세 공정의 출력 및 원가 한계를 돌파할 수 있는 차세대 반도체 제조 인프라 기술의 프로토타입 실증 및 정부 자금 유입 본격화.",
      "key_companies": [
        "테슬라(TSLA)",
        "ASML(ASML)",
        "xLight"
      ],
      "insight": "반도체 제조 기술이 개별 장비 단위의 경쟁을 넘어 전력망, 입자가속기, 중앙 광원 인프라를 통합하는 '메가 팹(Mega Fab)' 단위의 엔지니어링 패러다임으로 진화하고 있음.",
      "action_point": "ASML의 중장기 광원 기술 로드맵과 엑스라이트(xLight) 등 가속기 기반 반도체 장비 생태계 및 테슬라 테라팹의 R&D 진행 상황을 추적할 것."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": [
        "stock"
      ],
      "tags": [
        "테라팹",
        "FELEUV",
        "입자가속기",
        "ASML",
        "일론머스크",
        "노광장비",
        "반도체신기술"
      ]
    }
  },
  {
    "video": {
      "id": "I1GVAxM1N0c",
      "title": "\"올랐는데 지금이라도...\" 고민되시죠? | 이학주 하나증권 원주지점 차장 [더블 크루]",
      "published": "2026-08-13T02:00:10+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=I1GVAxM1N0c",
      "thumbnail": "https://img.youtube.com/vi/I1GVAxM1N0c/hqdefault.jpg"
    },
    "analysis": {
      "summary": "코스피 반등 국면에서 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>와 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>의 밸류에이션 바닥론을 강력히 제시함. 메모리 반도체를 고전적인 시클리컬(PBR 기준)로 보더라도 삼성전자는 2027년 예상 BPS 기준 PBR 1.1배 수준까지 하락해 역사적 최저점 구간에 진입했으며, PER 기준으로 보면 더욱 저평가 상태임. 외국인 지분율 역시 삼성전자가 46%대까지 급락해 추가 매도 여력이 제한적인 반면, 싱가포르 테마섹 등 글로벌 국부펀드의 저점 매수 검토와 공매도 숏커버링 유입 가능성이 높아 주도주 홀딩 및 추가 매수 전략을 권고함.",
      "key_claims": [
        "삼성전자와 SK하이닉스는 시클리컬 하단(PBR 1.1배) 수준까지 주가가 빠져 있어 밸류에이션 하방 경직성이 매우 견고함.",
        "삼성전자의 외국인 지분율(46%)은 역사적으로 50%를 밑돈 적이 드물 만큼 극단적 비우호적 수급이 반영된 상태로 강한 숏커버링 반등이 기대됨.",
        "주도주는 고점 대비 40~50% 조정을 거치더라도 실적이 뒷받침되는 한 쉽게 꺾이지 않으므로(에코프로 과거 사례), 공포에 손절하지 말고 물량을 지켜야 함."
      ],
      "data_points": [
        "삼성전자 밸류에이션: PBR 과거 사이클 하단 1.1배 (비정상 적자기 0.7배 제외), 최근 2.3배에서 1.5배 이하로 급락.",
        "SK하이닉스 2027년 예상 PBR: 1.3배 수준.",
        "삼성전자 외국인 지분율: 최근 46%대까지 하락 (통상 48~50% 이상 유지).",
        "빅테크 클라우드 성장률: 구글 80%+, MS 애저 40%+ 유지 중."
      ],
      "signal": "bullish",
      "signal_reason": "역사적 밸류에이션 최하단 도달, 외국인 지분율 비우기 완료 후 숏커버링 및 중장기 국부펀드 유입 본격화.",
      "key_companies": [
        "삼성전자(005930)",
        "SK하이닉스(000660)",
        "주성엔지니어링(036930)",
        "알테오젠(196170)"
      ],
      "insight": "단기 노이즈(금리 불확실성, 피크아웃 우려)로 인해 주도주가 급락할 때야말로 시간과 자금 여력이 있는 투자자에게 최고의 매수 기회를 제공함.",
      "action_point": "고점에서 신용/레버리지로 매수한 물량은 리스크 관리를 하되, 현금 여력이 있는 투자자는 삼성전자/SK하이닉스 및 실적 가시성이 높은 선도주를 저가 매수하여 보유할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "tech",
        "economy"
      ],
      "tags": [
        "삼성전자",
        "SK하이닉스",
        "PBR바닥",
        "외국인지분율",
        "숏커버링",
        "주도주전략",
        "하나증권"
      ]
    }
  }
]

if __name__ == "__main__":
    save_analyses(batch2_results)
