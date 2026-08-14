import json
import os

synthesis_data = {
  "stock": {
    "consensus": "bullish",
    "cross_insight": "7월 말 코스피 변동성 지수(VKOSPI)가 98까지 치솟았던 극단적 패닉 구간을 지나 <span class=\"text-cyan-300 font-semibold\">6,800선</span>에 안착하며 하반기 대세 턴어라운드에 돌입했습니다. 외국인이 코스피에서만 하루 <span class=\"text-emerald-400 font-semibold\">2조 4천억 원</span> 이상의 기록적 바스켓 순매수를 집행했으며, <span class=\"text-cyan-300 font-semibold\">SK하이닉스 ADR 프리미엄이 47%</span>까지 폭등하고 싱가포르 <span class=\"text-cyan-300 font-semibold\">테마섹</span> 등 글로벌 국부펀드가 저점 매수를 타진하고 있습니다. 샌디스크의 NBM 장기계약(80% 마진/FCF 100% 주주환원)과 CME의 <span class=\"text-cyan-300 font-semibold\">GPU 선물 상품(10월)</span> 발표로 반도체는 고변동 시클리컬에서 AI 핵심 원자재 자산으로 완벽히 재평가받고 있습니다.",
    "divergence": "미국 10년물 국채 금리 고공행진과 일본 9월 금리 인상에 따른 엔캐리 트레이드 청산 위험을 경계하는 신중론과, 삼성전자/SK하이닉스의 역사적 PBR(1.1배)/PER(4~5배) 바닥 및 AI CapEx 가속화에 따른 숏커버링 랠리를 확신하는 강력한 낙관론이 공존합니다.",
    "key_themes": [
      "외국인 2.4조 원 역대급 순매수와 SK하이닉스 숏커버링 및 미국 ADR 47% 프리미엄 폭등",
      "샌디스크의 FCF 100% 주주환원 및 장기공급계약(NBM) 80% 마진 가이던스 발표",
      "시카고상품거래소(CME)의 H100/블랙웰 GPU 임대료 선물 인덱스(10월) 상장 추진",
      "삼성전자(PBR 1.1배)와 SK하이닉스의 역사적 밸류에이션 바닥 확인 및 국부펀드 유입"
    ],
    "watch_list": [
      "외국인의 코스피 현물 연속 순매수 지속 여부 및 하이닉스 ADR 프리미엄 추이",
      "8월 26일 미국 7월 PCE 물가 지수 및 엔비디아 실적/CapEx 코멘트",
      "CME GPU 선물 상품 규제 승인 및 10월 5일 공식 상장 일정"
    ]
  },
  "tech": {
    "consensus": "bullish",
    "cross_insight": "FMS 2026(Future of Memory and Storage)에서 삼성전자의 <span class=\"text-cyan-300 font-semibold\">ZHBM</span>(연산 성능 8배/전력 효율 3배 개선)과 SK하이닉스의 <span class=\"text-cyan-300 font-semibold\">3D 적층 D램(Tier 0.5)</span> 및 <span class=\"text-cyan-300 font-semibold\">HBF(High Bandwidth Flash)</span>가 공개되며, 메모리가 GPU 위로 직접 올라가는 <span class=\"text-amber-300 font-bold\">3D 수직 통합 아키텍처</span> 시대가 열렸습니다. 앤트로픽의 디카트 AI(60억 달러) 인수와 일론 머스크 테라팹의 <span class=\"text-cyan-300 font-semibold\">FEL-EUV(가속기 광원)</span> 도입 추진 등 AI 전력/비용 병목을 돌파하기 위한 하드웨어-소프트웨어 융합 혁신이 폭발하고 있습니다.",
    "divergence": "애플의 중국 CXMT 저전력 LPDDR 테스트로 인한 레거시 메모리 공급망 침투 우려와, 선단 HBM4/ZHBM 및 3D 적층 기술에서 한국 기업들의 독점적 기술 격차가 더욱 벌어질 것이라는 기술 우위론이 맞서고 있습니다.",
    "key_themes": [
      "메모리-GPU 3D 직접 적층(ZHBM / 3D D램) 및 개방형 고대역폭 플래시(HBF) 표준화",
      "AI 데이터센터 전력/냉각 병목 해소를 위한 광통신(루멘텀/마벨) 및 분산 모듈형 센터 확산",
      "일론 머스크 테라팹의 입자가속기 기반 자유전자레이저(FEL-EUV) 광원 프로토타입 실증",
      "앤트로픽의 AI 훈련 비용 절감용 디카트 AI 60억 달러 인수 추진"
    ],
    "watch_list": [
      "FMS 2026 이후 빅테크(구글, 엔비디아)의 3D 적층 메모리(ZHBM/HBF) 채택 로드맵",
      "루멘텀/마벨 등 AI 데이터센터 고속 광트랜시버 및 스위치 공급 실적",
      "미국 정부의 칩스법 기반 FEL-EUV 광원(xLight) 연구개발 진척도"
    ]
  },
  "economy": {
    "consensus": "neutral",
    "cross_insight": "미국 7월 CPI와 PPI가 연이어 시장 예상치를 밑돌며 인플레이션 둔화 신호를 보냈으나, 휘발유 가격이 <span class=\"text-rose-400 font-medium\">갤런당 4달러</span>를 넘어서며 체감 물가 압박이 유권자 민심을 강타하고 있습니다. 미국 중간선거를 앞두고 트럼프 행정부의 중동 분쟁 개입 역풍과 의회 권력 상실(하원 패배 시 3번째 탄핵 위기) 리스크가 부각되는 가운데, 일본 정부의 <span class=\"text-amber-300 font-bold\">9월 BOJ 금리 인상 용인</span> 움직임으로 글로벌 외환 및 채권 시장의 변동성이 상존하고 있습니다.",
    "divergence": "PPI 안정과 고용 시장의 점진적 둔화로 9월 FOMC 금리 인하 및 골디락스 연착륙이 완성될 것이라는 낙관론과, 장기 국채 금리 상승 및 미 대선/중간선거 정치 리스크로 시장 변동성이 재확대될 것이라는 경계론이 대립합니다.",
    "key_themes": [
      "미국 7월 PPI 0.0% 보합 및 CPI 안정에 따른 9월 금리 인하 기대 공고화",
      "미국 전국 휘발유 갤런당 4달러 돌파에 따른 체감 물가 위기 및 중간선거 정치 뇌관",
      "일본 정부의 9월 BOJ 금리 인상 지지 선회에 따른 엔캐리 트레이드 청산 위험",
      "수도권 23만 가구 공급 대책과 가계대출 총량 관리(1.5% -> 3.0%) 완화"
    ],
    "watch_list": [
      "8월 26일 미국 7월 개인소비지출(PCE) 물가지수 결과",
      "9월 일본은행(BOJ) 금융정책결정회의 금리 인상 여부 및 엔/달러 환율 추이",
      "미국 중간선거 상·하원 여론조사 및 유가 동향"
    ]
  },
  "robot": {
    "consensus": "bullish",
    "cross_insight": "휴머노이드 로봇이 단순한 연구실 기술 시연을 넘어 <span class=\"text-cyan-300 font-semibold\">'24시간 무중단 자율 생산 체계'</span>의 상용화 단계로 진입했습니다. <span class=\"text-cyan-300 font-semibold\">현대차그룹</span>은 2028년 아틀라스 로봇 연 3만 대 양산을 위해 1차 협력사 200여 곳과 액추에이터/감속기 공급망을 구축하고 2027년 초 보스턴 다이내믹스 IPO를 서두르고 있습니다. 중국 유니트리가 매출총이익률 60% 흑자 IPO를 달성하고 출하량 90%를 장악하는 가운데, 메타의 피지컬 AI 오픈소스 선언과 테슬라 옵티머스의 공장 실전 배치가 가속화되고 있습니다.",
    "divergence": "중국의 저렴한 로봇 부품 공급망 장악과 단기 적자 누적에 대한 우려와, 현대차·구글 연합의 독자 부품 공급망 내재화 및 미·중 규제 반사이익을 통해 글로벌 휴머노이드 시장을 선점할 것이라는 성장론이 팽팽합니다.",
    "key_themes": [
      "현대차 아틀라스 2028년 3만 대 양산 체제 돌입 및 1차 협력사 로봇 모듈 R&D 지원",
      "보스턴 다이내믹스 조기 IPO(2027년) 추진 및 구글 Pre-IPO 신주 지분 투자 타진",
      "중국 유니트리의 흑자 IPO(GPM 60%)와 글로벌 휴머노이드 출하량 90% 장악",
      "22개 관절 독립 제어 로봇 핸드와 미세 조작(Fine Manipulation) AI 기술의 비약적 진보"
    ],
    "watch_list": [
      "8월 26일 현대차 CEO 인베스터 데이 로보틱스 세부 전략 및 부품 파트너십",
      "보스턴 다이내믹스 Pre-IPO 구글 지분 투자 및 2027년 상장 일정",
      "테슬라 기가팩토리 내 옵티머스 2세대 투입 대수 및 양산 단가 추이"
    ]
  },
  "space": {
    "consensus": "bullish",
    "cross_insight": "스페이스X <span class=\"text-cyan-300 font-semibold\">팰컨9</span> 상단부의 달 충돌 사건에서 한국의 달 탐사선 <span class=\"text-cyan-300 font-semibold\">다누리호(KPLO)</span>가 세계 최초로 충돌 전후 달 표면 흔적을 정밀 포착하며 한국의 우주 관측 기술력을 전 세계에 입증했습니다. 스페이스X 스타십의 연간 1,000회 발사 로드맵과 함께 저궤도 위성망을 활용한 <span class=\"text-amber-300 font-bold\">우주 데이터센터</span> 아키텍처(액체 암모니아 기화 냉각 및 레이저 광통신)가 지상 데이터센터의 전력/용수 병목을 극복할 현실적 대안으로 부상하고 있습니다.",
    "divergence": "우주 데이터센터 및 심우주 탐사의 막대한 발사 비용과 기술적 난이도에 대한 회의론과, 스타십 재사용 혁신으로 발사 단가가 급락하여 우주 인프라 산업이 기하급수적으로 팽창할 것이라는 낙관론이 공존합니다.",
    "key_themes": [
      "한국 다누리호의 스페이스X 팰컨9 달 충돌 흔적 세계 최초 관측 및 우주 풍화 데이터 확보",
      "스페이스X 스타십 대량 발사(연 1,000회) 기반 우주 레이저 통신 및 분산 데이터센터 구축",
      "우주 극한 환경 극복을 위한 방열 솔루션(이튼/보이드) 및 초정밀 자세 제어 모터(무그) 부각"
    ],
    "watch_list": [
      "스페이스X 스타십 차기 지구 궤도 시험 비행 및 스타링크 V3 위성 발사 일정",
      "나사(NASA) LRO 탐사선의 팰컨9 달 충돌 크레이터 초고해상도 후속 촬영 결과",
      "우주항공청(KASA)의 차세대 달 탐사선 및 궤도선 개발 프로젝트 진행 상황"
    ]
  },
  "crypto": {
    "consensus": "neutral",
    "cross_insight": "미국 CPI 안정세 속에서도 AI 반도체 실적주로 시중 유동성이 집중되면서 <span class=\"text-cyan-300 font-semibold\">비트코인</span>은 단기 박스권 횡보를 지속하고 있습니다. 그러나 비트코인-금 가격 상관계수가 <span class=\"text-emerald-400 font-semibold\">0.74</span>로 양전하며 희소 비주권 자산(디지털 금)의 위상이 확고해졌으며, 미국 SEC의 <span class=\"text-cyan-300 font-semibold\">토큰화 상장 증권(RWA)</span> 혁신 면제 발표와 트럼프의 비트코인 전략비축자산 편입 공약이 중장기 제도권 자금 유입의 강력한 촉매로 작용하고 있습니다.",
    "divergence": "AI 테크주와의 유동성 흡수 경쟁 및 국내외 과세/포렌식 추적 강화로 인한 단기 조정론과, 9월 글로벌 금리 인하 및 토큰화 주식(RWA) 제도화에 따른 4분기 메가 랠리론이 맞서고 있습니다.",
    "key_themes": [
      "비트코인-금 상관계수 0.74 급등 및 디지털 금 네러티브 복원",
      "미국 SEC의 상장 증권 토큰화(RWA) 혁신 면제 추진 및 스마트 컨트랙트 수혜",
      "트럼프의 가상자산 전략비축자산 편입 공약 및 달러 유동성 공급 사이클 도래",
      "국세청 AI 포렌식 기반 가상자산 체납 은닉 재산 추적 및 포상금 제도 강화"
    ],
    "watch_list": [
      "8월 14일 미 SEC 토큰화 상장 증권 혁신 면제 세부 가이드라인",
      "미국 비트코인 및 이더리움 현물 ETF 주간 순유입액 추이",
      "9월 미국 연준(FOMC) 기준금리 인하 폭 및 글로벌 달러 유동성 지표"
    ]
  },
  "culture": {
    "consensus": "neutral",
    "cross_insight": "한반도 지형과 태풍의 반시계 방향 순환이 맞물려 동해안의 기록적 폭우(시간당 80mm)와 서쪽 내륙의 극단적 폭염(39.5도)이 동시에 발생하는 <span class=\"text-cyan-300 font-semibold\">푄 현상(Foehn Phenomenon)</span> 등 국지적 기상 이변이 일상화되고 있습니다. 기후 변화에 대응하는 에너지 인프라와 재난 방재 체계의 과학적 엔지니어링이 국가적 필수 과제로 부상하고 있습니다.",
    "divergence": "단기 이상 기상에 따른 일시적 현상이라는 시각과, 기후 변동성 고착화로 인한 에너지 소비 패턴 및 산업 인프라의 근본적 재설계가 필요하다는 주장이 공존합니다.",
    "key_themes": [
      "태백산맥 지형성 단열 압축(푄 현상)으로 인한 국지적 폭우-폭염 양극화",
      "기상이변에 따른 전력망 부하 및 도시 방재 인프라의 과학적 대응 필요성"
    ],
    "watch_list": [
      "하반기 태풍 이동 경로 및 전력 수급 피크 관리 현황",
      "지자체별 국지성 집중호우 및 폭염 방재 시스템 구축 사업"
    ]
  }
}

os.makedirs('data/synthesis', exist_ok=True)

for topic, data in synthesis_data.items():
    out_path = f'data/synthesis/{topic}.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[종합 인사이트 작성 완료] {out_path}")
