import json
from save_batch_helper import save_analyses

batch3_results = [
  {
    "video": {
      "id": "J10-RoNjH8I",
      "title": "버핏도 AI 투자했다 이번엔 여기서 터진다 (한동대학교 AI융합학부 김학주 교수) | 2026년 8월 12일 방송",
      "published": "2026-08-13T07:55:18+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=J10-RoNjH8I",
      "thumbnail": "https://img.youtube.com/vi/J10-RoNjH8I/hqdefault.jpg"
    },
    "analysis": {
      "summary": "워런 버핏의 버크셔 해서웨이가 <span class=\"text-cyan-300 font-semibold\">알파벳(구글)</span> 지분을 매수한 것은 AI 산업의 발전이 좌초되거나 크게 지연되지 않을 것임을 확신한 신호로 해석됨. 현재 AI 확장의 최대 병목인 전력/용수 부족을 해결하기 위해, 대규모 데이터센터 대신 소형 모듈형 데이터센터를 분산 배치하고 <span class=\"text-cyan-300 font-semibold\">광통신</span> 및 <span class=\"text-cyan-300 font-semibold\">저궤도 위성망(스타링크)</span>으로 연결하는 새로운 아키텍처가 부상하고 있음. 스페이스X 스타십의 연 1,000회 발사 로드맵과 함께 우주 기반 데이터센터 구상이 가시화되고 있으며, 우주 방열(액체 암모니아 기화 냉각)의 <span class=\"text-cyan-300 font-semibold\">이튼(Eaton)</span>, 초정밀 자세 제어 모터의 <span class=\"text-cyan-300 font-semibold\">무그(Moog)</span>, 그리고 분산 반도체를 연결하는 광통신 칩 선두주자 <span class=\"text-cyan-300 font-semibold\">마벨 테크놀로지(Marvell)</span>가 AI 인프라 병목 해결의 핵심 수혜주로 제시됨.",
      "key_claims": [
        "워런 버핏의 알파벳 투자는 AI 인프라 투자 회의론과 달리 AI 생태계가 실질적인 비즈니스 모델과 가치를 창출할 것이라는 강력한 징표임.",
        "지상 데이터센터의 전력/냉각 병목을 극복하기 위해 분산형 모듈 데이터센터와 저궤도 우주 데이터센터 인프라가 본격적으로 태동하고 있음.",
        "AI 하드웨어의 병목을 우회하는 광통신 네트워킹(마벨)과 우주/전력 인프라 부품(이튼, 무그, ATI)이 차세대 핵심 투자처임."
      ],
      "data_points": [
        "스페이스X 스타십 발사 계획: 팰컨9 연 150회 대비 연간 1,000회 이상 발사 목표.",
        "저궤도 위성 1회 발사 탑재량: 기존 20개에서 50~60개로 2.5~3배 확대.",
        "우주 극한 온도: 액체산소 -183도 vs 엔진 연소 1,000도 이상을 견디는 특수합금(ATI) 수요.",
        "버크셔 해서웨이 포트폴리오: 과거 애플 비중 최대 46% 수준 운용 후 구글 지분 편입."
      ],
      "signal": "bullish",
      "signal_reason": "버핏의 구글 투자로 입증된 AI 장기 성장 신뢰와 데이터센터 물리적 병목(전력/냉각/통신)을 해결하는 특화 인프라 기업들의 실적 모멘텀.",
      "key_companies": [
        "알파벳(GOOGL)",
        "마벨 테크놀로지(MRVL)",
        "이튼(ETN)",
        "무그(MOG.A)",
        "ATI(ATI)",
        "스페이스X"
      ],
      "insight": "AI 인프라 경쟁은 단순한 GPU 연산력 확보에서 전력 전송, 우주 레이저 통신, 극한 방열 엔지니어링 등 물리적 병목을 해결하는 융합 하드웨어 영역으로 확장되고 있음.",
      "action_point": "엔비디아/빅테크 외에 AI 데이터센터 병목을 해소하는 광통신 칩(마벨 테크놀로지), 전력·방열 솔루션(이튼), 정밀 제어 부품(무그)으로 포트폴리오를 다변화할 것."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": [
        "stock",
        "space"
      ],
      "tags": [
        "워런버핏",
        "알파벳",
        "AI데이터센터",
        "스페이스X",
        "마벨테크놀로지",
        "이튼",
        "무그",
        "우주데이터센터"
      ]
    }
  },
  {
    "video": {
      "id": "JOqiUy602PY",
      "title": "'아시아 최대 국부 펀드' 삼전닉스 러브콜? | 하창완 하보노의 주식 이야기 대표 [더블 체크]",
      "published": "2026-08-13T08:06:24+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=JOqiUy602PY",
      "thumbnail": "https://img.youtube.com/vi/JOqiUy602PY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "아시아 최대 국부펀드인 싱가포르 <span class=\"text-cyan-300 font-semibold\">테마섹(Temasek)</span>이 최근 주가 조정을 겪은 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>와 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>에 대한 지분 투자 검토 및 매수 타진(러브콜)을 진행 중인 것으로 알려짐. 단기 투기성 헤지펀드가 아닌 장기 국부펀드의 자금 유입은 국내 반도체 투톱의 밸류에이션 바닥 확인과 외국인 수급 턴어라운드를 이끄는 강력한 신호탄으로 평가됨.",
      "key_claims": [
        "싱가포르 테마섹 등 글로벌 메가 국부펀드의 반도체 투톱 매수 검토는 주가의 바닥 통과를 의미함.",
        "중장기 펀드의 선제적 진입은 다른 글로벌 연기금과 국부펀드의 후속 매수를 유발하는 마중물 역할을 수행함."
      ],
      "data_points": [
        "싱가포르 국부펀드(테마섹/GIC): 아시아 최대 규모의 글로벌 자산운용 국부펀드.",
        "국내 대표 국부펀드 KIC(한국투자공사) 및 노르웨이 국부펀드(NBIM)와 비견되는 초대형 기관 자금."
      ],
      "signal": "bullish",
      "signal_reason": "아시아 최대 국부펀드의 삼성전자/SK하이닉스 지분 매입 타진으로 인한 수급 및 투자 심리의 극적인 반전.",
      "key_companies": [
        "삼성전자(005930)",
        "SK하이닉스(000660)"
      ],
      "insight": "패시브 및 헤지펀드의 단기 매도 공세가 일단락된 시점에서 국부펀드의 가치 투자 자금 유입은 주가의 하방 경직성을 극대화함.",
      "action_point": "글로벌 국부펀드의 매수세 유입 국면에서 삼성전자와 SK하이닉스 비중 확대를 유지할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "tech"
      ],
      "tags": [
        "테마섹",
        "삼성전자",
        "SK하이닉스",
        "국부펀드",
        "외국인수급",
        "반도체러브콜"
      ]
    }
  },
  {
    "video": {
      "id": "KNKT2NVNDic",
      "title": "애플의 배신 중국 반도체 쓰려고 CXMT 메모리 테스트하는 이유 (언더스탠딩 백종훈 기자)",
      "published": "2026-08-13T12:25:19+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=KNKT2NVNDic",
      "thumbnail": "https://img.youtube.com/vi/KNKT2NVNDic/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">애플(Apple)</span>이 메모리 가격 급등에 따른 원가 부담을 낮추기 위해 중국 내수용 아이폰을 대상으로 중국 1위 D램 제조사 <span class=\"text-cyan-300 font-semibold\">창신메모리(CXMT)</span>의 칩 품질 테스트에 착수했다고 WSJ이 보도함. CXMT는 중국 안후이성 허페이시와 <span class=\"text-rose-400 font-medium\">인민해방군</span>의 출자로 설립되어 상하이 증시 상장으로 15조 원 이상의 자금을 조달했으며, 내년 상하이/베이징 공장 증설 시 마이크론급(월 38만 장) 생산 능력을 갖추게 됨. 미국 의회와 정계가 자국 메모리 산업 붕괴를 우려하며 강력 반발하고 있어 실제 채택까지는 거센 규제 역풍이 예상되나, 한국 D램 3사의 모바일 시장 점유율에 잠재적 위협 요인으로 부각됨.",
      "key_claims": [
        "애플의 CXMT D램 테스트는 모바일용 저전력 메모리(LPDDR) 원가 절감과 중국 내수 판매 방어를 위한 시도임.",
        "CXMT는 인민해방군 지분과 막대한 정부 보조금을 바탕으로 급성장하여 글로벌 D램 점유율 8%에 도달함.",
        "미국 의회의 초당적 규제 반발로 인해 애플이 실제로 중국산 D램을 대량 채택하기는 정치적으로 매우 어려울 전망임."
      ],
      "data_points": [
        "글로벌 D램 시장 점유율: 삼성전자 38%, SK하이닉스 29%, 마이크론 22%, CXMT 8%.",
        "CXMT 생산 목표: 내년 웨이퍼 기준 월 38만 장(마이크론 생산량에 근접).",
        "애플 전체 매출 중 중국 비중: 약 20%.",
        "CXMT 상하이 상장 후 주가 상승률: 공모가 8.6위안에서 50위안 이상으로 약 470% 폭등."
      ],
      "signal": "neutral",
      "signal_reason": "애플의 테스트 소식이 단기 투자 심리에 부담을 줄 수 있으나, 미국 정부의 제재 리스크와 기술적 격차로 단기간 내 공급망 전면 대체는 제한적임.",
      "key_companies": [
        "애플(AAPL)",
        "삼성전자(005930)",
        "SK하이닉스(000660)",
        "마이크론(MU)",
        "CXMT(창신메모리)"
      ],
      "insight": "중국 정부의 막대한 보조금 지원을 등에 업은 CXMT의 레거시 D램 추격은 가속화되고 있으나, HBM 및 선단 LPDDR5X 공정에서는 한국 기업들의 기술적 해자가 여전히 공고함.",
      "action_point": "미국 대중 반도체 추가 제재 및 애플의 공급망 승인 여부를 모니터링하되, CXMT가 침투하기 어려운 첨단 HBM 및 DDR5 비중이 높은 SK하이닉스 선호도를 유지할 것."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": [
        "stock",
        "economy"
      ],
      "tags": [
        "애플",
        "창신메모리",
        "CXMT",
        "LPDDR",
        "삼성전자",
        "SK하이닉스",
        "미중반도체전쟁"
      ]
    }
  },
  {
    "video": {
      "id": "KyA2ejPjb_0",
      "title": "비닐봉지 매듭까지 묶는다? 로봇 손이 정교해진 이유",
      "published": "2026-08-13T09:30:33+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=KyA2ejPjb_0",
      "thumbnail": "https://img.youtube.com/vi/KyA2ejPjb_0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "단순한 집게 형태를 벗어나 사람처럼 22개의 관절을 독립적으로 제어하여 쓰레기 비닐봉지 매듭 묶기나 전구 교체 같은 초미세 물체 조작(Fine Manipulation)을 수행하는 차세대 <span class=\"text-cyan-300 font-semibold\">로봇 손</span> 기술을 소개함. 과거에는 불가능하다고 여겨졌던 복잡한 비정형 물질 조작을 강화학습과 엔드투엔드(End-to-End) 신경망 AI 모델을 통해 실시간으로 해결하는 로봇 엔지니어링의 진보를 강조함.",
      "key_claims": [
        "로봇의 진정한 난제는 점프나 백플립 같은 거대 동작이 아니라 비닐봉지 묶기 같은 미세 관절 조작임.",
        "인간이 무의식적으로 움직이는 22개 손가락 관절을 AI 모델이 직접 학습하고 제어하면서 휴머노이드 로봇의 실용성이 극대화되고 있음."
      ],
      "data_points": [
        "인간형 로봇 손 관절 제어 자유도: 22개 이상의 독립 관절 동시 제어."
      ],
      "signal": "bullish",
      "signal_reason": "가사 노동 및 정밀 제조 공정에 투입 가능한 로봇 핸드 및 미세 조작 AI 기술의 획기적 발전 확인.",
      "key_companies": [
        "테슬라(TSLA)",
        "피규어AI",
        "보스턴다이내믹스"
      ],
      "insight": "휴머노이드 로봇의 상용화 성공 여부는 보행 능력보다 비정형 부품과 도구를 자유자재로 다루는 정교한 '로봇 핸드(Dextrous Hand)'의 완성도에 달려 있음.",
      "action_point": "정밀 액추에이터, 촉각 센서 및 다관절 로봇 핸드 하드웨어·소프트웨어 기술을 보유한 밸류체인에 주목할 것."
    },
    "classification": {
      "primary_topic": "robot",
      "secondary_topics": [
        "tech"
      ],
      "tags": [
        "로봇손",
        "정밀조작",
        "22개관절",
        "휴머노이드핸드",
        "인공지능제어",
        "안될공학"
      ]
    }
  },
  {
    "video": {
      "id": "SPiCZMyeWFo",
      "title": "CPI 잘 나왔는데 비트코인 왜 못 올라? | 권혁, 김동환, 하나 김재희 이사 [크립토 PLUS]",
      "published": "2026-08-13T03:03:31+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=SPiCZMyeWFo",
      "thumbnail": "https://img.youtube.com/vi/SPiCZMyeWFo/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 CPI 안정세 발표에도 불구하고 <span class=\"text-cyan-300 font-semibold\">비트코인</span>이 급반등하지 못하고 횡보하는 이유를 분석함. AI 데이터센터 및 반도체 섹터의 실적 호조로 시중 유동성이 테크주로 쏠리는 가운데, 비트코인과 금의 상관계수가 0.74로 양전(디지털 금 네러티브 복원)되었으나 단기 촉매는 부족한 상황임. 한편 미국 <span class=\"text-cyan-300 font-semibold\">SEC</span>가 8월 14일 토큰화 상장 증권(애플, 테슬라 등 <span class=\"text-cyan-300 font-semibold\">토큰화 주식</span>)에 대한 혁신 면제(규제 샌드박스) 발표를 앞두고 있어 제도권 편입 기대감이 커지고 있으며, 국내 국세청은 AI 포렌식을 통한 가상자산 체납 은닉 재산 추적 및 포상금 제도를 강화함.",
      "key_claims": [
        "CPI 안정 이후 유동성이 AI 반도체 실적주로 집중되면서 가상자산 시장의 단기 자금 유입이 지연되고 있음.",
        "비트코인과 금의 가격 상관계수가 0.74로 급등하며 희소 비주권 자산으로서의 지위가 강화됨.",
        "미 SEC의 토큰화 주식 혁신 면제 추진은 실물연계자산(RWA) 및 스마트 컨트랙트 블록체인 생태계에 중장기 호재로 작용함."
      ],
      "data_points": [
        "비트코인-금 가격 상관계수: 연초 -0.9에서 최근 0.74로 급상승(일간 수익률 상관계수 0.50).",
        "미국 SEC 토큰화 상장 증권 혁신 면제 회의: 8월 14일 예정 (발행사 주도형/수탁형/합성형 3종 분류).",
        "국세청 가상자산 은닉 탈세 포상금: 최저 징수 기준 5천만 원에서 3천만 원으로 하향, 지급률 10~30%로 상향."
      ],
      "signal": "neutral",
      "signal_reason": "SEC의 토큰화 증권 혁신면제 및 디지털 금 위상 회복은 긍정적이나, AI 테크주로의 유동성 분산으로 단기 박스권 횡보 전망.",
      "key_companies": [
        "체인링크(LINK)",
        "바이낸스(BNB)"
      ],
      "insight": "가상자산 시장이 독자적 투기 장세에서 벗어나 실물 주식의 토큰화(RWA) 및 전통 금융 제도권과의 융합 단계로 체질을 개선하고 있음.",
      "action_point": "비트코인의 박스권 분할 매수 전략을 유지하며, SEC 토큰화 주식 혁신 면제 수혜가 기대되는 체인링크(LINK) 등 RWA 핵심 인프라 코인에 주목할 것."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": [
        "economy",
        "stock"
      ],
      "tags": [
        "비트코인",
        "디지털금",
        "SEC토큰화주식",
        "RWA",
        "체인링크",
        "국세청가상자산추적",
        "삼프로TV"
      ]
    }
  },
  {
    "video": {
      "id": "TYWTkKpS7q4",
      "title": "[문지웅의 빅머니 LIVE] 엑스 출몰 잦아진 젠슨황 | 하이닉스ADR 프리미엄 확대  | 美증시 2020년이후 최고 8월",
      "published": "2026-08-13T21:58:45+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=TYWTkKpS7q4",
      "thumbnail": "https://img.youtube.com/vi/TYWTkKpS7q4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 생산자물가지수(PPI)가 CPI에 이어 안정세를 기록하며 S&P 500이 7,800선을 돌파하고 사상 최고치에 근접함. 낸드 플래시 선두주자 <span class=\"text-cyan-300 font-semibold\">샌디스크(SanDisk)</span>는 인베스터 데이에서 초과 잉여현금흐름(FCF) <span class=\"text-emerald-400 font-semibold\">100% 주주환원</span>과 함께, 최저보장가격(Floor)과 상한선(Ceiling)을 갖춘 장기공급계약(NBM) 939억 달러 체결 및 마진 80% 달성 로드맵을 발표해 주가가 13.7% 폭등함. 한편 <span class=\"text-cyan-300 font-semibold\">SK하이닉스 ADR</span>은 추가 발행 제한에 따른 차익거래 제약으로 원주 대비 프리미엄이 <span class=\"text-emerald-400 font-semibold\">47%</span>까지 급등했으며, <span class=\"text-cyan-300 font-semibold\">엔비디아</span> 젠슨 황 CEO는 쿠다(CUDA) 소프트웨어 파워를 통해 2020년 출시된 A100 등 구형 GPU도 10년간 사용 가능하다고 강조함.",
      "key_claims": [
        "샌디스크의 NBM 장기 공급 계약(939억 달러)과 80% 마진 가이던스는 낸드 플래시 시장의 구조적 피크아웃 우려를 완벽히 불식시킴.",
        "SK하이닉스 미국 ADR 프리미엄이 47%까지 치솟은 것은 글로벌 기관들의 하이닉스 주식에 대한 폭발적 매수 수요를 방증함.",
        "엔비디아 쿠다 소프트웨어는 구형 GPU 수명을 10년까지 연장시켜 클라우드 AI 인프라 투자(AIDC)의 원금 회수 기간을 3년으로 단축시키는 핵심 경쟁력임."
      ],
      "data_points": [
        "S&P 500 연초 대비 13.93% 상승, 장중 7,800선 돌파.",
        "샌디스크 장기계약(NBM) 규모: 8개 고객사 대상 총 939억 달러, 보증금 165억 달러 확보, 매출총이익률 80% 목표.",
        "SK하이닉스 미국 ADR 종가: 165.67달러 (+7.29%), 한국 원주 대비 프리미엄 47%.",
        "AIDC(AI 데이터센터) 회수 기간: 네비우스/코어위브 연간 임대 수익률 33% 기준 약 3년 만에 CapEx 원금 회수."
      ],
      "signal": "bullish",
      "signal_reason": "샌디스크의 100% 주주환원 및 장기계약 마진 80% 발표, SK하이닉스 ADR의 47% 프리미엄, 엔비디아의 AIDC 빠른 투자금 회수성 입증.",
      "key_companies": [
        "샌디스크(SNDK)",
        "SK하이닉스(000660)",
        "엔비디아(NVDA)",
        "마이크론(MU)",
        "코어위브(CoreWeave)"
      ],
      "insight": "메모리 및 AI 반도체 산업이 고변동성 시클리컬에서 장기 공급 계약(LTA/NBM) 기반의 안정적 고수익 구조로 체질이 완전히 전환되었음.",
      "action_point": "하이닉스 ADR 프리미엄 확대로 인한 국내 하이닉스 원주의 강력한 키 맞추기 상승에 베팅하며, 낸드 고부가 공급망 및 엔비디아 생태계를 집중 보유할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "tech",
        "economy"
      ],
      "tags": [
        "샌디스크",
        "SK하이닉스ADR",
        "엔비디아",
        "쿠다",
        "NBM장기계약",
        "주주환원",
        "월가월부"
      ]
    }
  }
]

if __name__ == "__main__":
    save_analyses(batch3_results)
