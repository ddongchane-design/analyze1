import json
from pathlib import Path

batch3 = [
  {
    "video": {
      "id": "jNVY3KtRos4",
      "title": "AI 수익성 우려 재부각..나스닥 1.3%↓ | 데일리 라이브 | 2026.6.23(화)",
      "published": "2026-06-23T11:18:37+00:00",
      "channel_name": "Smart Money by MiraeAsset",
      "url": "https://www.youtube.com/watch?v=jNVY3KtRos4",
      "thumbnail": "https://img.youtube.com/vi/jNVY3KtRos4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 증시는 미국과 이란의 평화 협정 진전 소식에도 불구하고 <span class=\"text-rose-400 font-medium\">AI 투자 수익성(ROI) 우려</span>가 재부각되며 기술주 중심으로 조정받음. 특히 100만 토큰당 연산 비용이 폭락하여 프론티어 AI 모델 자체가 범용화되는 단가 인하 경쟁 속에, 반복적인 현금 흐름과 독점 데이터를 확보하지 못한 단순 호출형 기업들의 생존 부담이 가중됨.",
      "key_claims": [
        "AI 모델의 API 단가가 2023년 GPT-4 기준 대비 90% 이상 폭락하여 모델의 기술 차별성보다 단가와 속도 중심 범용화가 빠르게 진행됨.",
        "단순 API 호출 비즈니스 모델은 마진 훼손에 직면해 있으며, 실질적으로 클라우드 수주잔고와 광고 구매 전환 매출을 입증하는 최선호주로 압축이 요구됨.",
        "뱅크오브아메리카는 강력한 미국 실물 거시 지표와 매파적인 통화 스탠스 하에 연내 정책 금리를 3회(총 75bp) 인상할 것으로 전망을 변경함."
      ],
      "data_points": [
        "나스닥 지수 변동: 당일 기술주 매도세로 1.32% 하락 마감",
        "AI 연산 토큰 가격 추이: 100만 토큰당 비용이 GPT-4 기준 45~90달러선에서 최근 경량 모델 기준 0.05~0.11달러선으로 급감",
        "마이크로소프트 클라우드 수주잔고: 2,400억 달러 돌파 기록"
      ],
      "signal": "neutral",
      "signal_reason": "유가 안정 및 원유 공급 위기 해소는 긍정적이나, 인프라 비용 대비 AI의 실질 ROI 회수 의구심에 다른 밸류에이션 리밸런싱과 연준의 매파적 추가 금리 인상론이 대립하고 있기 때문임.",
      "key_companies": ["마이크로소프트(MSFT)", "메타(META)", "테슬라(TSLA)", "알파벳(GOOGL)"],
      "insight": "AI 메가 트렌드는 모델 성능 경쟁에서 '복제 불가능한 데이터'와 '반복적인 고객 접점 요금 구조'를 확보하여 실제 ROI를 산출하는 실전 비즈니스로 전이되고 있음.",
      "action_point": "모멘텀에 기댄 세 배 레버리지 투기나 단순 래퍼(Wrapper) 서비스사는 축소하고, 압도적인 현금 창출력과 클라우드 백로그를 쥔 빅테크 대장주 위주로 압축 대응할 것."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["AI수익성우려", "토큰단가폭락", "클라우드수주잔고", "금리인상전망", "미래에셋데일리"]
    }
  },
  {
    "video": {
      "id": "K-1YyIYILAI",
      "title": "\"일단 짓고 부수던 시대는 끝났다\" 시뮬레이션 하나로 수백억 아끼는 법 #교양이를부탁해",
      "published": "2026-06-23T09:45:19+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=K-1YyIYILAI",
      "thumbnail": "https://img.youtube.com/vi/K-1YyIYILAI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "건설 현장의 구조적 노동 생산성 한계를 돌파하기 위해 정보통신 기술과 AI를 접목한 <span class=\"text-cyan-300 font-semibold\">스마트 건설</span> 기술 도입이 촉진됨. 특히 공장에서 부재를 사전 조립해 현장으로 가져와 로봇으로 조립하는 <span class=\"text-cyan-300 font-semibold\">프리패브(Prefab)</span> 기법과 가상현실(VR) 시뮬레이션 활용이 시공 기일 단축과 리스크 예방에 크게 기여함.",
      "key_claims": [
        "현장 시공 과정을 공장식 모듈화 및 로봇 조립으로 전환해 현장 위험성과 공사 기간을 획기적으로 낮춤.",
        "디지털 모델과 VR 스캔 장비를 활용해 가상으로 설계 리스크와 현장 동작을 검증하여 오시공 비용을 제거함.",
        "건설 현장의 급격한 고령화와 구인난 속에서 스마트 공정 및 로봇 도입이 건설사 수익 방어의 핵심 변수로 부상함."
      ],
      "data_points": [],
      "signal": "bullish",
      "signal_reason": "인력난과 비용 폭증으로 위축된 건설 시공 현장에 정밀 데이터 시뮬레이션과 모듈러 프리패브 공법이 접목되며 장기 생산성 가치 사슬을 복구하기 때문임.",
      "key_companies": [],
      "insight": "전통 토목 시공에서 탈피하여, 공정을 사전에 가상 시뮬레이션하고 표준 조립 부재를 로봇화하여 시공하는 소프트웨어 중심 가치 창출이 차세대 건설업의 핵심 경쟁력임.",
      "action_point": "모듈러 시공, 건설 자동화 및 디지털 시뮬레이션 소프트웨어 플랫폼 기술을 보유한 혁신 중소기업을 선별 발굴할 것."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["tech", "robot"],
      "tags": ["스마트건설", "프리패브", "공기단축", "VR시뮬레이션", "안전관리"]
    }
  },
  {
    "video": {
      "id": "l0UF9rhl-Yk",
      "title": "오픈AI·앤트로픽 상장하면 반도체 주가는 상상도 못할 만큼 오르게 됩니다ㅣ정주용 의장 [1부]",
      "published": "2026-06-23T08:00:00+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=l0UF9rhl-Yk",
      "thumbnail": "https://img.youtube.com/vi/l0UF9rhl-Yk/hqdefault.jpg"
    },
    "analysis": {
      "summary": "비상장 AI 공룡인 오픈AI와 앤트로픽의 기업공개(IPO)는 대규모 연기금 자본을 유치해 설비 투자(Capex)로 환원되어 <span class=\"text-cyan-300 font-semibold\">AI 반도체 수요의 2차 폭발</span>을 야기할 전망임. 한국의 소버린 AI는 단순 가상 모델 개발이 아닌, 제조업 및 반도체 공정 데이터를 AI와 결합하는 <span class=\"text-cyan-300 font-semibold\">소버린 피지컬 AI</span> 플랫폼과 미들웨어를 장악하는 국가적 생존 전략이어야 함.",
      "key_claims": [
        "1조 달러 가치를 상회하는 오픈AI 및 앤트로픽 상장 시 조달된 금융 자금의 최소 30%가 하드웨어 인프라 및 반도체 조달에 직접 투자됨.",
        "한국은 자체 거대 언어모델(LLM)보다 자동차, 방산, 반도체 제조 공정을 AI로 동기화하는 스마트 팩토리용 피지컬 AI 미들웨어를 장악해야 경쟁력이 있음.",
        "유리기판 및 CPO(광학 소자) 등 차세대 소부장 원천 기술을 확보해야 엔비디아의 생태계 지배력을 능가하는 부가가치를 점유함."
      ],
      "data_points": [
        "비상장 AI 기업 가치 추정: 오픈AI, 앤트로픽, 스페이스X 등 1조~2조 달러 이상의 기업 가치 도달 기대감 반영",
        "상장 조달금 재투자 추정치: 신규 IPO 자금의 최소 30% 이상이 엔비디아 칩 및 아시아 반도체 공급망에 흘러들 것으로 예측"
      ],
      "signal": "bullish",
      "signal_reason": "빅테크 및 상위 AI 랩스의 상장 일정 구체화에 따라 천문학적인 실탄이 공급망 소부장에 쏟아져 들어오며, 아시아 반도체 제조사의 마진 증가 사이클을 장기화하기 때문임.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "오픈AI", "앤스로픽"],
      "insight": "AI의 미래는 가상 서비스에 머물지 않고 제조 실물 데이터를 AI 온톨로지와 연결해 실제 원가 구조를 지배하는 '피지컬 B2B 통합 플랫폼'이 될 것임.",
      "action_point": "단순 소프트웨어 수혜 기대주보다, 차세대 인프라 투자의 병목인 유리기판, CPO(공동광학소자) 등 원천 특허를 쥔 반도체 소부장 대장주에 지속 적립할 것."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock", "economy"],
      "tags": ["비상장IPO", "주권피지컬AI", "소부장혁신", "앤디비아동맹", "정주용"]
    }
  },
  {
    "video": {
      "id": "l_CsySPQPU0",
      "title": "[빈난새의 개장전요것만-6월23일] 들불처럼 번진 반도체 매도 | 버블 붕괴? 월가 생각은 | 러셀 리밸런싱 결과 | 마이크론 IBM 스페이스X 팔란티어 소파이 나이키 인플렉션",
      "published": "2026-06-23T14:27:17+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=l_CsySPQPU0",
      "thumbnail": "https://img.youtube.com/vi/l_CsySPQPU0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "연준의 긴축 스탠스와 더불어 분기말/반기말을 겨냥한 연기금 등 패시브 자금의 자산배분 리밸런싱 매도로 인해 기술주와 반도체 주식 중심의 <span class=\"text-rose-400 font-medium\">급격한 차익 실현 폭탄</span>이 낙폭을 키움. AI 인프라 투자 수익성 의구심이 부각되며 비트코인 등 가상자산과 금 ETF 유출이 심화된 반면, 실적 안정성과 소프트웨어 마진 방어력이 뛰어난 IBM 등은 역주행에 성공함.",
      "key_claims": [
        "반기말 분기말 패시브 자금 재조정에 따른 오버슈팅 해소 차원의 기계적 주도주 매도세가 지수를 강타함.",
        "미국 대통령의 양자 컴퓨팅 국가 안보 자산 격상 명령 및 JP모건의 소프트웨어 마진 개선 평가에 힘입어 IBM 주가는 강세를 나타냄.",
        "달러당 161.5엔을 돌파하는 엔화 약세에도 공동 구두 개입 효과가 약화되는 등 달러 강세 압력이 시장 유동성을 억누르고 있음."
      ],
      "data_points": [
        "글로벌 지수 조정률: 나스닥 100 선물 3%대 하락, S&P 500 선물 1.5% 하락",
        "엔화 환율: 1달러당 161.55엔 도달로 엔저 심화",
        "IBM 목표 주가 상향: JP모건에 의해 270달러에서 291달러로 상향 조정"
      ],
      "signal": "bearish",
      "signal_reason": "분기말 리밸런싱 수급 변동성과 연준 추가 금리 인상 가능성에 대한 공포가 겹쳐 단기 테크 섹터 내 투매 압력이 극대화된 국면이기 때문임.",
      "key_companies": ["IBM(IBM)", "마이크론(MU)", "스페이스X", "비트코인"],
      "insight": "AI 하드웨어 과열 논란 시기에는 밸류에이션 매력이 돋보이고 확실한 B2B 소프트웨어 계약 백로그를 구축한 방어형 대형주로 자금이 이동함.",
      "action_point": "반도체 레버리지 포지션은 조정을 감안해 리스크를 관리하되, 양자 컴퓨터 안보화 호재 및 소프트웨어 수익성이 입증된 IBM과 같은 실적 방어형 기업으로 포트폴리오를 다변화할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["반도체매도세", "패시브리밸런싱", "IBM상승", "엔화약세", "양자컴퓨팅명령"]
    }
  },
  {
    "video": {
      "id": "Mq9X0LC9I9o",
      "title": "11조 원 매수한 개인 투자자분들, 오늘 탁월한 선택이었습니다.ㅣ홍선애, 이경민 대신증권 FICC 리서치 부장 [여의도 인사이트]",
      "published": "2026-06-23T08:56:04+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=Mq9X0LC9I9o",
      "thumbnail": "https://img.youtube.com/vi/Mq9X0LC9I9o/hqdefault.jpg"
    },
    "analysis": {
      "summary": "국내 증시의 급격한 코스피 하락은 매크로 펀더멘탈 손상이 아닌, 금융투자의 기계적 프로그램 매도 및 분기말 리밸런싱에 따른 <span class=\"text-rose-400 font-medium\">수급 쇼크에 의한 일시적 발작</span>임. SK하이닉스의 시총 1위 역전 및 메모리 반도체의 실적 질주는 정상적인 HBM 가격 강세를 반영하고 있으며, 국제 유가 하향 안정화로 6월 인플레 지표 둔화가 예상되어 하방 지지력이 견고함.",
      "key_claims": [
        "외국인 물량과 더불어 ETF 프로그램 매매 중심의 금융투자 매도가 합쳐지며 무차별적인 동반 하락 지수 왜곡을 유발함.",
        "마이크론 및 샌디스크 등 글로벌 반도체 실적 전망은 순항하고 있으며, 2분기 및 3분기 EPS 레벨업 흐름은 유효함.",
        "지정학 에너지 리스크 완화로 국제 유가가 배럴당 70달러 초반대로 내리며 인플레 기대 심리 피크아웃을 지지함."
      ],
      "data_points": [
        "개인 투자자 대응: 단기 코스피 조정 국면에서 약 11조 원 규모 매수 대응으로 저가 매수세 입증",
        "WTI 유가: 호르무즈 협상 타결 등으로 배럴당 74.82달러선으로 하락 마감"
      ],
      "signal": "bullish",
      "signal_reason": "실물 경기 지표와 반도체 영업이익 전망치 개선에 이상이 없는 상태에서 수급 꼬임에 기인한 일시적 지수 급락은 매력적인 진입 가격을 제공하기 때문임.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "마이크론(MU)"],
      "insight": "시장이 공포에 휩쓸려 프로그램에 의해 우량주를 던질 때 펀더멘탈 지표(실적, 유가 하락에 따른 물가 안정)에 기반한 용기 있는 분할 진입은 초과 수익의 토대가 됨.",
      "action_point": "주변 공포 투매에 동요하지 말고, HBM 독점 지위와 확실한 메모리 실적 이익 상승이 지지되는 SK하이닉스와 삼성전자 보통주를 저가 매수 기회로 활용할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["코스피조정", "프로그램매도", "수급불균형", "HBM독점마진", "이경민"]
    }
  },
  {
    "video": {
      "id": "NgDyrWOHAsM",
      "title": "SpaceX 우주 배송 시험! Starfall 발사 생중계!  [항성의 우주속으로]",
      "published": "2026-06-23T11:10:35+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=NgDyrWOHAsM",
      "thumbnail": "https://img.youtube.com/vi/NgDyrWOHAsM/hqdefault.jpg"
    },
    "analysis": {
      "summary": "스페이스X가 우주의 미세 중력 환경을 상업적 용도로 활용해 신약이나 고순도 소재를 제조하는 <span class=\"text-cyan-300 font-semibold\">우주 제조(In-Space Manufacturing)</span> 제품을 회수하는 스타폴(Starfall) 프로젝트 발사 시험을 시작함. 저궤도 <span class=\"text-cyan-300 font-semibold\">스타링크 위성 네트워크</span>를 경유해 지구 재진입 시 대기 마찰 플라즈마로 인한 통신 단절(블랙아웃)을 사상 최초로 제거하는 기술 실증이 핵심임.",
      "key_claims": [
        "미세 중력의 우주 공간은 지상과 달리 밀도 침강이 발생하지 않아 알츠하이머 신약 단백질 등 균일한 결정을 대량으로 배양할 수 있음.",
        "플라즈마 장막을 뚫고 상부 저궤도 스타링크를 이용해 교신함으로써 지구 재진입 중 통신 두절 시간 없이 기체를 완벽히 원격 모니터링함.",
        "스타폴 프로젝트는 단순한 우주 공장 물류 회수를 넘어, 로켓을 이용해 지구 반대편까지 1시간 만에 화물을 보내는 군사/상업용 특송 수송망으로 진화할 수 있음."
      ],
      "data_points": [
        "머크 키트루다 우주 정거장 실험 결과: 지상 13~102마이크로미터의 불균일 크기 대비 우주 배양 시 39마이크로미터로 고르게 형성",
        "부스터 재사용 횟수: 이번 팰컨9 발사는 우주 역사상 최초로 단일 부스터 29회 재사용 성공 달성"
      ],
      "signal": "bullish",
      "signal_reason": "스페이스X가 독점적인 팰컨9 재사용 수송 인프라와 스타링크 저궤도 통신망 결합을 통해, 개화되는 상업용 우주 제조 및 고부가가치 로켓 배송 시장 장벽을 압도적으로 구축하고 있기 때문임.",
      "key_companies": ["스페이스X", "머크(MRK)"],
      "insight": "스타링크를 활용해 대기권 재진입 통신 블랙아웃을 해결하는 것은 우주 물동량 회수 신뢰성을 지상 수준으로 높이는 중대한 물류 혁신임.",
      "action_point": "우주 의약품 배양 플랫폼 및 소형 무인 캡슐 기계 부품 개발사, 그리고 스페이스X 밸류체인 내의 핵심 위성 안테나 부품 공급 기업에 주목할 것."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["tech"],
      "tags": ["SpaceX", "Starfall", "우주제조", "스타링크", "재진입블랙아웃"]
    }
  },
  {
    "video": {
      "id": "nqosdYh5Rr4",
      "title": "[홍장원의 불앤베어] 시장 공포 더하는 3대 매크로 변수",
      "published": "2026-06-23T22:42:46+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=nqosdYh5Rr4",
      "thumbnail": "https://img.youtube.com/vi/nqosdYh5Rr4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "기술주 급락세는 과거 닷컴 버블과 달리 실적이 입증되고 있어 붕괴 징후가 아닌 <span class=\"text-rose-400 font-medium\">모멘텀 포지션 청산에 따른 건전한 조정</span>으로 분석됨. 다만 70년대 인플레이션의 쌍봉 형태 재현 우려 및 일부 빅 유저에 극도로 치우친 <span class=\"text-rose-400 font-medium\">좁은 AI 지출 구조</span>는 인프라 투자의 중장기 리스크 요인으로 부각됨.",
      "key_claims": [
        "현재 메모리 반도체 및 빅테크 밸류에이션(멀티플)은 이익 성장에 의해 충분히 설명 가능한 수준이며, 과거 버블 붕괴 공식과는 확연히 다름.",
        "기업 직원 1인당 월평균 AI 사용액 통계상 상위 1%에 압도적으로 쏠려 있어 일반 대중/소형 기업의 사용 침투율은 여전히 낮은 기초 단계임.",
        "지정학 및 중동 원유 공급 차질이 유발하는 물가 2차 스파이크 시나리오가 나타날 시, 연준의 예상 밖 추가 긴축이 지수의 최대 파괴 변수가 될 수 있음."
      ],
      "data_points": [
        "AI 사용자 지출 통계: 1인당 월평균 AI 지출액 상위 1%는 7,450달러인 반면, 상위 10%는 611달러, 전체 중앙값은 11달러에 불과해 쏠림 극화",
        "마이크론 연간 가이드라인 타겟: 매출 335억 달러, 주당순이익 19달러대 제시 예정"
      ],
      "signal": "neutral",
      "signal_reason": "반도체의 기본 실적 펀더멘탈은 견고하지만, 좁은 유저층에 기대고 있는 AI CapEx 수요와 고금리 인플레 재상승 시나리오가 상단을 압박하는 불안 국면이기 때문임.",
      "key_companies": ["마이크론(MU)", "엔비디아(NVDA)", "뱅크오브아메리카"],
      "insight": "AI 인프라 투자가 정당화되려면 빅테크의 독점적 사용을 넘어, 백오피스 기업 실무 등 일반 기업들의 실질적 도입 및 반복 지출 기반이 확산되어야 함.",
      "action_point": "모멘텀에만 의존해 급등한 고PER 단순 AI 성장주의 노출도는 축소하고, 반도체 제조 병목을 쥔 핵심 제조사 및 고금리 환경에 방어력이 있는 금융 섹터로 일부 분산할 것."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["매크로위험", "AI지출양극화", "인플레이션쌍봉", "모멘텀청산", "홍장원"]
    }
  },
  {
    "video": {
      "id": "nunLrYxo1uU",
      "title": "[26.06.23 오전 방송 전체보기] 엇갈린 기술주 주가에 뉴욕증시 혼조 마감...메모리↑·SPCX↓",
      "published": "2026-06-23T02:58:27+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=nunLrYxo1uU",
      "thumbnail": "https://img.youtube.com/vi/nunLrYxo1uU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "뉴욕 증시는 지정학 위기(미-이란 협상) 완화에도 불구하고 신임 연준 의장하의 긴축 경계로 혼조세 마감함. 특히 역사적으로 신임 연준 의장 취임 초기 6개월 내에 발생했던 큰 폭의 조정인 <span class=\"text-rose-400 font-medium\">연준 징크스 우려</span>와 단기 레버리지 상품의 옵션 청산 및 러셀 리밸런싱 수급 부담이 변동성을 확대하는 요인임.",
      "key_claims": [
        "미-이란 원유 공급 제재 완화로 유가 불안은 소화 중이나, 새로운 매파적 금리 인상론 노이즈가 채권 금리 상방 압력을 지속 유발함.",
        "신임 연준 의장의 허니문 기간인 6개월 이내에 시장 심리를 시험하는 역사적인 연준 징크스 조정 가능성이 제기됨.",
        "글로벌 하이퍼스케일러의 설비 투자는 2~3년간 순항하겠지만, 단기 수급 왜곡과 레버리지 ETF의 투기 쏠림 청산이 주가 변동성을 흔들고 있음."
      ],
      "data_points": [
        "금 가격 장기 가이드라인: 목표치 4,000달러선 지지 의견 유지"
      ],
      "signal": "neutral",
      "signal_reason": "장기 AI Capex와 지정학 원유 리스크 소강 상태는 긍정적이나, 신임 의장발 매파적 긴축 전환에 대한 역사적 징크스 우려와 분기말 패시브 청산 물량이 대치하고 있기 때문임.",
      "key_companies": ["스페이스X", "마이크론(MU)", "엔비디아(NVDA)"],
      "insight": "금융 시장이 실물 실적보다는 신임 의장의 의중 및 파생 수급(레버리지, 연기금 리밸런싱) 등 센티멘트 변수에 의해 지수를 격렬히 흔드는 변동성 구간임.",
      "action_point": "단기 급등한 기술주에 무리하게 레버리지 추격 매수하는 것을 피하고, 실적 가시성이 유지되는 메모리 반도체 대장주를 중심으로 비중을 유지하되 단기 변동성 확대를 감안할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["연준징크스", "뉴욕증시혼조", "금목표가", "하이퍼스케일러", "김장열"]
    }
  }
]

scratch_dir = Path("scratch")
scratch_dir.mkdir(exist_ok=True)
Path("scratch/batch3.json").write_text(json.dumps(batch3, ensure_ascii=False, indent=2), encoding="utf-8")
print("Wrote batch3.json")
