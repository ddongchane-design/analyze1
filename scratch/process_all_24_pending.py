import os
import json
import glob

# Data dictionary for all 24 pending files
batch_data = {
  "-Z9dDc6Nv-g": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "-Z9dDc6Nv-g",
        "title": "[8월 10일 마감시황] 삼전닉스 쉬자 코스닥으로 몰린 돈…7% 급등 뒤 진짜 매수 타이밍은?",
        "published": "2026-08-10T08:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=-Z9dDc6Nv-g",
        "thumbnail": "https://img.youtube.com/vi/-Z9dDc6Nv-g/hqdefault.jpg"
      },
      "analysis": {
        "summary": "삼성전자와 SK하이닉스가 숨고르기에 들어가자 코스닥 시장으로 자금이 쏠리며 <span class=\"text-cyan-300 font-semibold\">매수 사이드카가 발동</span>하는 순환매 장세가 연출됨. 모건스탠리의 메모리 바닥론 고수 속에 <span class=\"text-amber-300 font-bold\">소비재·2차전지·바이오</span>로 이동한 코스닥 순환매 자금의 지수 하락 채널 상단 돌파 여부가 향후 본격 매수 타이밍의 신호가 될 것임.",
        "key_claims": [
          "반도체 대장주의 조정을 틈타 코스닥으로 자금이 이동하며 8월 세 번째 <span class=\"text-cyan-300 font-semibold\">매수 사이드카</span>가 발동함.",
          "모건스탠리의 메모리 바닥론 발표로 대장주 하방 지지력이 확인되자 장세 온기가 중소형주로 순환함.",
          "코스닥 지수의 하락 채널 상단 돌파가 확인되는 시점이 9월 반등을 노리는 가장 안전한 분할 매수 타점임."
        ],
        "data_points": [
          "코스닥 매수 사이드카 발동: 8월 들어 3번째 발동 (코스닥 급등세)",
          "모건스탠리 SK하이닉스 목표가: 38.1만 원 고수"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "대장주(삼전·닉스) 하방 지지 속에서 코스닥으로 온기가 퍼지는 양호한 순환매 장세가 형성되고 있기 때문임.",
        "key_companies": ["삼성전자", "SK하이닉스", "알테오젠", "에코프로"],
        "insight": "반도체 독주 장세에서 코스닥 밸류체인 및 실적 개선주로 온기가 확산되는 것은 증시 체력이 건강해지고 있음을 의미함.",
        "action_point": "코스닥 하락 채널 상향 탈출 확인 후 밸류에이션 부담이 낮아진 반도체 전공정 및 바이오 실적주로 분할 매수 진입 권장."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["마감시황", "코스닥사이드카", "모건스탠리바닥론", "순환매장세"]
      }
    }
  },
  "DiD2eemzsuM": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "DiD2eemzsuM",
        "title": "[26.08.10 오후 방송 전체보기] 월가 \"메모리 조정 끝\"…삼전닉스 반등할까? 코스닥 8월 세번째 매수 사이드카, 증시 순환매 온기 언제까지",
        "published": "2026-08-10T09:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=DiD2eemzsuM",
        "thumbnail": "https://img.youtube.com/vi/DiD2eemzsuM/hqdefault.jpg"
      },
      "analysis": {
        "summary": "월가 주요 투자은행(모건스탠리 등)이 <span class=\"text-cyan-300 font-semibold\">메모리 반도체 주가 조정 완결</span>을 선언하며 국내 반도체 주가의 반등 기반이 마련됨. 코스닥 시장에서 매수 사이드카가 발동하며 <span class=\"text-amber-300 font-bold\">8월 전강후강 장세</span>와 함께 9월 증시 랠리 재개에 대한 기대감이 확산됨.",
        "key_claims": [
          "월가의 메모리 조정 완료 보고서로 반도체 업종의 투심이 급속도로 개선됨.",
          "8월 코스닥의 잇단 사이드카 발동은 8월 턴어라운드 및 9월 전면 반등의 강력한 선행 지표임.",
          "대장주 안정화 후 중소형 소부장 및 화장품·소비재로 순환매 확산."
        ],
        "data_points": [
          "모건스탠리 2027년 빅테크 CapEx 전망: 29% 상향 제시",
          "코스닥 8월 사이드카 횟수: 총 3회 발동"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "메모리 악재 악소멸 및 코스닥 강한 반등으로 시장의 하방 리스크가 대폭 축소되었기 때문임.",
        "key_companies": ["삼성전자", "SK하이닉스", "한미반도체"],
        "insight": "반도체 피크아웃 우려가 둔화되고 유동성이 중소형주로 공급되는 구간은 하반기 주도 섹터 진입의 최적기임.",
        "action_point": "조정세를 거친 반도체 소부장 대장주와 코스닥 강세 주도주를 중심으로 포트폴리오 비중 확대."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["월가메모리조정끝", "코스닥사이드카", "전강후강", "증시순환매"]
      }
    }
  },
  "EIC4hb1f0jg": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "EIC4hb1f0jg",
        "title": "'8월 전강후강' 아직 유효…삼전닉스 안정되면 코스닥 주도주는 '상승 3법'에서 나온다",
        "published": "2026-08-10T08:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=EIC4hb1f0jg",
        "thumbnail": "https://img.youtube.com/vi/EIC4hb1f0jg/hqdefault.jpg"
      },
      "analysis": {
        "summary": "8월 증시의 '전강후강' 시나리오가 유지되는 가운데, 삼성전자와 SK하이닉스가 지지선을 확보하면 코스닥 주도주 랠리가 본격화될 전망임. 특히 정부의 <span class=\"text-cyan-300 font-semibold\">상법 개정(주가누르기 방지법)</span> 및 ISA 세제 혜택 손질 등 <span class=\"text-amber-300 font-bold\">'상승 3법' 정책 수혜주</span>가 주도주로 부상할 가능성이 높음.",
        "key_claims": [
          "8월 초 증시 조정을 지나 중후반 턴어라운드가 가시화되는 전강후강 패턴을 나타냄.",
          "상법 개정안(이사 충실의무 확대)과 ISA 절세 혜택 확대가 코리아 디스카운트 해소의 촉매가 됨.",
          "반도체 대장주 안정 이후 지배구조 개선 및 주주환원 우수 기업으로 수급이 쏠릴 것임."
        ],
        "data_points": [
          "지수 지지선: 삼성전자 지지선 확보 및 코스닥 하락 채널 상단 돌파 시도",
          "ISA 세제 혜택 한도 확대 개정안 추진 중"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "정책 모멘텀(상법 개정)과 지수 턴어라운드가 맞물리며 코스닥 주주가치 제고 종목의 상승이 기대되기 때문임.",
        "key_companies": ["삼성전자", "SK하이닉스", "한국전력"],
        "insight": "단순 실적 모멘텀 외에 주주환원 법제화라는 정책적 호재가 더해지면서 한국 증시 밸류에이션 재평가 계기가 마련됨.",
        "action_point": "상법 개정 및 ISA 혜택 관련 수혜가 명확한 고배당·주주환원 저평가 지주사 및 코스닥 실적주 매수."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["상승3법", "상법개정", "전강후강", "주가누르기방지"]
      }
    }
  },
  "Gr-P6Z3V6VA": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "Gr-P6Z3V6VA",
        "title": "슈퍼 엘니뇨가 온다 | 월스트리트파인더ㅣ2026.8.10(월)",
        "published": "2026-08-10T08:00:00+00:00",
        "channel_name": "Smart Money by MiraeAsset ",
        "url": "https://www.youtube.com/watch?v=Gr-P6Z3V6VA",
        "thumbnail": "https://img.youtube.com/vi/Gr-P6Z3V6VA/hqdefault.jpg"
      },
      "analysis": {
        "summary": "이상 기후에 따른 <span class=\"text-amber-300 font-bold\">슈퍼 엘니뇨 현상</span>이 글로벌 농산물 및 곡물 가격 인플레이션을 자극하고 있음. 8월 13F 헤지펀드 포트폴리오 공시 및 MSCI 분기 리뷰, 대만 <span class=\"text-cyan-300 font-semibold\">TSMC 7월 매출 발표</span>가 주요 수급 변수로 작용할 전망임.",
        "key_claims": [
          "슈퍼 엘니뇨로 인한 기후 이상이 애그플레이션(농산물 인플레이션) 우려를 자극함.",
          "미국 13F 헤지펀드 지분 공시를 통해 빅테크 및 반도체 기관 매매 향방이 공개됨.",
          "TSMC 7월 매출 실적이 파운드리 및 AI 반도체 수요의 강도를 판가름하는 척도가 됨."
        ],
        "data_points": [
          "미국 13F 공시 마감: 8월 14일 예정",
          "MSCI 분기 리뷰 발표: 8월 12일 현지시간 기준"
        ],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "MSCI 리밸런싱 및 13F 발표를 앞둔 기관 관망세와 원자재 인플레이션 리스크가 수급을 제약하고 있기 때문임.",
        "key_companies": ["TSMC", "NVIDIA"],
        "insight": "기후 이상에 따른 원자재 가격 변동은 매크로 물가 상방 압력으로 작용하나, TSMC 매출을 통해 AI 하드웨어의 실질 수요는 견조함을 지속 입증하고 있음.",
        "action_point": "13F 공시를 통한 주요 헤지펀드의 AI/반도체 포트폴리오 변화를 확인 후 매수 종목 선별."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock", "tech"],
        "tags": ["슈퍼엘니뇨", "TSMC7월매출", "13F공시", "MSCI리밸런싱"]
      }
    }
  },
  "Mdt1fjFm1ng": {
    "primary": "etc",
    "data": {
      "video": {
        "id": "Mdt1fjFm1ng",
        "title": "수학자를 속인 숫자의 함정?!",
        "published": "2026-08-10T09:00:00+00:00",
        "channel_name": "안될과학 Unrealscience",
        "url": "https://www.youtube.com/watch?v=Mdt1fjFm1ng",
        "thumbnail": "https://img.youtube.com/vi/Mdt1fjFm1ng/hqdefault.jpg"
      },
      "analysis": {
        "summary": "페르마의 소수 추측(2^(2^n)+1)이 오일러에 의해 반례가 발견되며 무너진 수학적 사건을 소개함. 초기 소수 사례들에 낚여 섣부른 추론을 내렸던 수학사의 비하인드 스토리를 통해 일반화의 함정을 설명함.",
        "key_claims": [
          "페르마는 n=0~4까지 모두 소수가 나오자 모든 수식이 소수일 것이라 추측했으나 오일러가 반례를 찾아냄.",
          "수학에서 반례는 오류를 밝히는 것에 그치지 않고 새로운 정수론 연구의 기폭제가 됨."
        ],
        "data_points": [
          "페르마 소수 5번째 수 (n=5): 4,294,967,297 = 641 * 6,700,417 (합성수)"
        ],
        "signal": "na",
        "signal_confidence": "high",
        "signal_reason": "투자와 직접 연관되지 않은 순수 수학사 교양 콘텐츠임.",
        "key_companies": [],
        "insight": "부분적 데이터나 초기 성과만으로 전체를 일반화하는 오류는 학문뿐만 아니라 투자 의사결정에서도 유의해야 할 교훈임.",
        "action_point": "본 영상은 주식 시장이나 자산 운용과 무관하므로 투자 판단 대상에서 제외함."
      },
      "classification": {
        "primary_topic": "etc",
        "secondary_topics": [],
        "tags": ["페르마소수", "오일러반례", "수학사", "안될과학"]
      }
    }
  },
  "R8ql_yLbbEg": {
    "primary": "etc",
    "data": {
      "video": {
        "id": "R8ql_yLbbEg",
        "title": "우리가 몰랐던 매미의 길고 조용한 지하생활(갈로아)",
        "published": "2026-08-10T09:30:00+00:00",
        "channel_name": "안될과학 Unrealscience",
        "url": "https://www.youtube.com/watch?v=R8ql_yLbbEg",
        "thumbnail": "https://img.youtube.com/vi/R8ql_yLbbEg/hqdefault.jpg"
      },
      "analysis": {
        "summary": "곤충 연구자 갈로아 작가가 매미의 생태적 특성(노린재목 분화, 7~17년 지하 생활, 나무 수액 흡즙)과 울음소리 진화 과정을 해설함.",
        "key_claims": [
          "매미는 노린재목 곤충으로 주둥이를 통해 나무 수액을 빨아먹는 생태적 구성을 지님.",
          "신생대에 이르러 짝짓기를 위한 울음소리 기관이 진화함."
        ],
        "data_points": [],
        "signal": "na",
        "signal_confidence": "high",
        "signal_reason": "순수 생물학 및 곤충 생태 관련 교양 영상임.",
        "key_companies": [],
        "insight": "자연 곤충 생태의 특이성과 생물학적 진화 과정을 친근하게 조명한 콘텐츠임.",
        "action_point": "투자 자산 운용과는 무관한 영상이므로 의사결정 대상에서 제외함."
      },
      "classification": {
        "primary_topic": "etc",
        "secondary_topics": [],
        "tags": ["매미생태", "노린재목", "갈로아", "생물학"]
      }
    }
  },
  "YDV50MeWpxI": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "YDV50MeWpxI",
        "title": "고용 악화 \"오히려 좋아\"...S&P500 '최고가' | 데일리 라이브 | 2026.8.10(월)",
        "published": "2026-08-10T07:30:00+00:00",
        "channel_name": "Smart Money by MiraeAsset ",
        "url": "https://www.youtube.com/watch?v=YDV50MeWpxI",
        "thumbnail": "https://img.youtube.com/vi/YDV50MeWpxI/hqdefault.jpg"
      },
      "analysis": {
        "summary": "미국 <span class=\"text-amber-300 font-bold\">7월 비농업 고용 쇼크(-2.3만 명)</span>가 연준의 금리 인하(피벗) 명분을 앞당기며 S&P 500이 사상 최고치를 경신함. 동시에 일본 JBIC 및 메가뱅크의 <span class=\"text-cyan-300 font-semibold\">5,500억 달러 대미 인프라 투자</span> 프로젝트가 가시화되며 글로벌 위험 자산 선호가 강화됨.",
        "key_claims": [
          "고용 둔화 지표 발표가 금리 인하 기대감을 자극하여 뉴욕 증시 강세를 주도함.",
          "일본 자본의 대미 energy/인프라 $5,500억 투자가 글로벌 유동성을 지지함."
        ],
        "data_points": [
          "S&P 500: 사상 최고치 경신",
          "일본 대미 투자 스킴: 5,500억 달러 규모 (JBIC-메가뱅크 연계)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "미국 금리 인하 피벗 호재와 일본의 초대형 대미 투자 펀딩이 시장 유동성을 전폭 지원하기 때문임.",
        "key_companies": ["NVIDIA", "Microsoft"],
        "insight": "매크로 악재(고용 쇼크)가 통화 정책 완화라는 호재로 해석되는 전형적인 'Bad news is Good news' 장세임.",
        "action_point": "금리 하락 수혜가 예상되는 빅테크 및 인프라 관련주에 대한 매수 관점 유지."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["economy", "tech"],
        "tags": ["고용쇼크", "연준금리인하", "SP500최고가", "대미투자"]
      }
    }
  },
  "YnCfaLcs1_g": {
    "primary": "shipbuilding",
    "data": {
      "video": {
        "id": "YnCfaLcs1_g",
        "title": "\"이건 조선업 쇼\" 마스가 회의론?ㅣ이상은의 워싱턴나우",
        "published": "2026-08-10T11:00:00+00:00",
        "channel_name": "한경 글로벌마켓",
        "url": "https://www.youtube.com/watch?v=YnCfaLcs1_g",
        "thumbnail": "https://img.youtube.com/vi/YnCfaLcs1_g/hqdefault.jpg"
      },
      "analysis": {
        "summary": "미국 해군력 강화를 위한 <span class=\"text-cyan-300 font-semibold\">MASGA (한·미·일 조선 협력 프로젝트)</span> 구상이 발표되었으나, 미국 의회의 예산 승인 지연 및 존스법(Jones Act) 규제로 상용 조선소의 빠른 재건에 대한 회의론이 제기됨. 다만 한국 함정 정비(MRO) 및 군함 수주에 대한 중장기 실혜택은 유효함.",
        "key_claims": [
          "미 국방부 및 의회의 예산 지연으로 미 조선업 부흥 구상(MASGA)이 단기 쇼에 그칠 우려가 제기됨.",
          "미국 존스법 규제 완화 없이 미국 내 조선소 단기 재건은 물리적으로 불가능함.",
          "한국 조선사(HD현대, 한화오션)의 미 해군 MRO 수주는 실질적 매출로 연결 중임."
        ],
        "data_points": [
          "MASGA 프로젝트: 미국 함정 MRO 및 재건 펀드 구상"
        ],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "미국 입법 및 예산 병목으로 단기 모멘텀은 약화될 수 있으나, 한국 조선사의 미 해군 MRO 수주 체력은 견조하기 때문임.",
        "key_companies": ["HD현대중공업", "한화오션"],
        "insight": "미국 자체 조선업 재건의 어려움은 역설적으로 세계 최고 조선 건조 능력을 가진 한국 대형 조선사들에게 MRO 독점 기회를 제공함.",
        "action_point": "MASGA 정치 노이즈 조정 시 미 해군 MRO 실증 수주를 확보한 HD현대중공업·한화오션 비중 확대."
      },
      "classification": {
        "primary_topic": "shipbuilding",
        "secondary_topics": ["stock", "economy"],
        "tags": ["MASGA", "조선업회의론", "해군MRO", "한화오션", "HD현대"]
      }
    }
  },
  "YpPvayz3mEY": {
    "primary": "crypto",
    "data": {
      "video": {
        "id": "YpPvayz3mEY",
        "title": "클래리티 법안, 9월 15일이 분수령…연내 통과 가능할까? | 서동주, 김동환, 한서희 법무법인 광장 변호사 [크립토 PLUS]",
        "published": "2026-08-10T10:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=YpPvayz3mEY",
        "thumbnail": "https://img.youtube.com/vi/YpPvayz3mEY/hqdefault.jpg"
      },
      "analysis": {
        "summary": "미국 상원의 <span class=\"text-cyan-300 font-semibold\">크립토 클래리티 법안(Clarity Act)</span>이 8월 토론 종결(Cloture) 제출 후 9월 15일표결을 앞두고 있음. 스테이블코인 이자 허용 및 SEC/CFTC 관할권 정리를 골자로 법제화가 순항 시 연내 통과 가능성이 높게 점쳐짐.",
        "key_claims": [
          "9월 15일 미 상원 서머 리세스 복귀 직후 클래리티 법안 표결이 크립토 규제 투명성의 분수령이 됨.",
          "스테이블코인 발행사의 이자 지급 허용 여부가 은행권과 막판 쟁점으로 대립함."
        ],
        "data_points": [
          "표결 예정일: 2026년 9월 15일 미 상원 표결 안건 처리 상정"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "법안 연기에도 불구하고 9월 표결 타임라인이 구체화되며 규제 불확실성이 빠르게 해소되고 있기 때문임.",
        "key_companies": ["Coinbase", "Circle"],
        "insight": "크립토 법제화는 가상자산이 제도권 금융의 정식 자산군으로 편입되는 입법적 이정표 역할을 함.",
        "action_point": "9월 법안 표결 진전 상황을 주시하며 비트코인 및 미국 제도권 크립토 관련주 분할 매수."
      },
      "classification": {
        "primary_topic": "crypto",
        "secondary_topics": ["stock", "economy"],
        "tags": ["클래리티법안", "9월15일표결", "스테이블코인", "크립토법제화"]
      }
    }
  },
  "ZEgot4sfsVA": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "ZEgot4sfsVA",
        "title": "[26.08.10 오전 방송 전체보기] 부진한 고용지표에 금리인상 전망 '뚝'...뉴욕증시 3대 지수 '상승'",
        "published": "2026-08-10T06:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=ZEgot4sfsVA",
        "thumbnail": "https://img.youtube.com/vi/ZEgot4sfsVA/hqdefault.jpg"
      },
      "analysis": {
        "summary": "부진한 미 고용 지표로 인해 연준의 금리 인상 가능성이 소멸하고 인하 명분이 커지며 뉴욕 증시 3대 지수가 강등 반등함. 팔란티어(39.8% 급등) 등 호실적 테크주와 메모리 반도체 바닥론이 시장 랠리를 전폭 지원함.",
        "key_claims": [
          "미 7월 비농업 고용 감소(-2.3만 명)로 금리 인상 우려가 완전 소멸함.",
          "팔란티어의 AI 어닝 서프라이즈가 빅테크 AI CapEx 호조를 증명함."
        ],
        "data_points": [
          "팔란티어 주가 상승률: 39.78%",
          "미 7월 고용 지표: -23,000명 (예상치 대폭 하회)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "금리 하락 완화 기조와 AI 기업들의 강력한 실증 실적이 증시 상승 모멘텀을 지지하기 때문임.",
        "key_companies": ["Palantir", "NVIDIA"],
        "insight": "고용 둔화는 금리 피벗을 이끌어내어 증시의 고평가 부담을 완화해 주는 호재로 작용함.",
        "action_point": "금리 하락 모멘텀과 실적 가이던스를 동시에 충족하는 AI 주도주 비중 유지."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["고용지표부진", "금리인하", "팔란티어폭등", "뉴욕증시상승"]
      }
    }
  },
  "cUWLhUHh-v0": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "cUWLhUHh-v0",
        "title": "미국에 찍혔더니 메일 카드 싹 막혔다  (하수정 경제전문기자)",
        "published": "2026-08-10T10:00:00+00:00",
        "channel_name": "언더스탠딩_Understanding",
        "url": "https://www.youtube.com/watch?v=cUWLhUHh-v0",
        "thumbnail": "https://img.youtube.com/vi/cUWLhUHh-v0/hqdefault.jpg"
      },
      "analysis": {
        "summary": "미국의 대러시아 2차 제재(Secondary Sanctions) 강화로 러시아 그림자 금융망 및 Mail.ru 결제 카드, USDT 차폐 채널이 전면 차단됨. 글로벌 세컨더리 제재로 인한 지정학 금융 분절화 현상을 분석함.",
        "key_claims": [
          "미 재무부의 세컨더리 제재로 우회 결제망이 대대적으로 마비됨.",
          "러시아 기업들의 테더(USDT) 등 가상자산 우회 자금 거래도 강력 제재를 받음."
        ],
        "data_points": [],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "지정학 금융 규제 강화는 원자재 및 글로벌 공급망의 고질적 불확실성으로 작용하기 때문임.",
        "key_companies": [],
        "insight": "미국의 금융 패권(달러 및 제재망) 강화는 글로벌 교역의 파편화를 유발하여 공급망 비용을 증가시킴.",
        "action_point": "대러시아 제재 반사 수혜가 있는 대체 공급망 관련 기업에 관심."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["crypto"],
        "tags": ["세컨더리제재", "러시아금융제재", "달러패권", "그림자금융"]
      }
    }
  },
  "ebFn3gD8dlI": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "ebFn3gD8dlI",
        "title": "주식보다 두 배 올랐다?…내 계좌 손실 줄이는 자산배분 전략ㅣ명민준, 박가영, 송재경 [주린이 구조대]",
        "published": "2026-08-10T08:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=ebFn3gD8dlI",
        "thumbnail": "https://img.youtube.com/vi/ebFn3gD8dlI/hqdefault.jpg"
      },
      "analysis": {
        "summary": "주식 변동성 장세에서 금(+7.5%), 미국 국채, 리츠 등 상관관계가 낮은 자산 배분 포트폴리오의 우수한 성과를 분석함. 리스크 패리티 및 주기적 리밸런싱을 통한 개인 계좌 손실 방지 전략 제시.",
        "key_claims": [
          "금과 국채 등 대체 자산 배분이 단일 주식 투자 대비 2배 이상의 안정적 수익률을 기록함.",
          "지수 변동성 구간에서 계좌를 지키는 핵심은 규칙적인 리밸런싱임."
        ],
        "data_points": [
          "금 수익률: 최근 주식 지수 대비 2배 성과 달성"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "자산 배분 전략을 활용 시 하방 위험을 차단하고 턴어라운드 장세에서 안전하게 복리 수익을 낼 수 있기 때문임.",
        "key_companies": [],
        "insight": "상관관계가 낮은 자산군(주식-채권-금)의 분산 배분은 증시 조정기 손실을 최소화하는 핵심 운용 원칙임.",
        "action_point": "주식 비중 일변도에서 벗어나 미국 국채 ETF 및 금 현물 ETF를 20~30% 비중으로 포트폴리오 편입."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["자산배분", "금투자", "국채ETF", "리밸런싱"]
      }
    }
  },
  "hJrKapqGj0s": {
    "primary": "tech",
    "data": {
      "video": {
        "id": "hJrKapqGj0s",
        "title": "[박신영의 개장전요것만-8월10일] 머스크가 GPU 싹쓸이 하나..코어위브·네비우스 긴장 | 로켓랩 실적, 주목할 3가지",
        "published": "2026-08-10T12:00:00+00:00",
        "channel_name": "한경 글로벌마켓",
        "url": "https://www.youtube.com/watch?v=hJrKapqGj0s",
        "thumbnail": "https://img.youtube.com/vi/hJrKapqGj0s/hqdefault.jpg"
      },
      "analysis": {
        "summary": "일론 머스크의 xAI가 GPU 클러스터 대량 구매를 독점하면서 <span class=\"text-cyan-300 font-semibold\">코어위브·네비우스 등 네오클라우드</span>의 GPU 수급 병목이 심화됨. 로켓랩은 뉴트론 로켓 4분기 발사 및 6.6억 달러 미 우주군 수주로 실적 발표를 앞두고 기대를 모음.",
        "key_claims": [
          "머스크의 GPU 싹쓸이로 클라우드 연산 자원 쇼티지가 장기화됨.",
          "로켓랩은 뉴트론 차세대 대형 로켓 4분기 실물 시험발사가 주가 밸류에이션의 분수령임."
        ],
        "data_points": [
          "로켓랩 미 우주군 수주 총액: 6.63억 달러 계약 체결"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "GPU 연산력 쇼티지로 반도체 공급망 수혜가 지속되고, 로켓랩의 수주 가시성이 대폭 향상되었기 때문임.",
        "key_companies": ["NVIDIA", "RocketLab", "CoreWeave"],
        "insight": "xAI의 대규모 컴퓨팅 흡수는 AI 하드웨어 장비사들의 장기 매출을 보장해 주는 강력한 선행 지표임.",
        "action_point": "로켓랩 및 GPU 인프라 공급망 핵심 부품 기업에 대한 관심."
      },
      "classification": {
        "primary_topic": "tech",
        "secondary_topics": ["space", "stock"],
        "tags": ["GPU쇼티지", "xAI", "로켓랩", "코어위브"]
      }
    }
  },
  "h_TlL8j0Huk": {
    "primary": "tech",
    "data": {
      "video": {
        "id": "h_TlL8j0Huk",
        "title": "이 대통령 \"호남 반도체, 구마모토처럼\" | 배터리 양극재 업체도 ESS 덕분 '동반 흑자' | 세제개편안 후폭풍 | 류종은 삼프로TV 취재팀장 [뉴스3]",
        "published": "2026-08-10T10:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=h_TlL8j0Huk",
        "thumbnail": "https://img.youtube.com/vi/h_TlL8j0Huk/hqdefault.jpg"
      },
      "analysis": {
        "summary": "정부가 호남 지역을 일본 구마모토형 <span class=\"text-cyan-300 font-semibold\">반도체 생태계 클러스터</span>로 육성하겠다고 발표함. 전기차 케즘 속에서도 <span class=\"text-amber-300 font-bold\">ESS(에너지저장장치) 전력망 수요 폭발</span>로 양극재 기업(엘앤에프, 포스코퓨처엠)이 동반 흑자 전환에 성공함.",
        "key_claims": [
          "호남 반도체 클러스터 정부 지원으로 국내 반도체 소재·부품 지방 생태계가 확장됨.",
          "AI 데이터센터 전력 피크 대응을 위한 ESS용 배터리 출하량이 양극재 실적을 견인함."
        ],
        "data_points": [
          "양극재 기업 흑자 전환 요인: ESS용 양극재 공급량 전년비 80% 이상 폭증"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "전기차 케즘 악재를 ESS 데이터센터 전력 망 수요가 완벽히 메우며 2차전지 소재의 실적 턴어라운드가 입증되었기 때문임.",
        "key_companies": ["엘앤에프", "포스코퓨처엠", "삼성SDI"],
        "insight": "AI 데이터센터 전력 인프라 붐은 전력망 송배전뿐만 아니라 2차전지 ESS 밸류체인까지 직접적인 흑자 턴어라운드를 유발함.",
        "action_point": "ESS 비중이 높고 흑자 전환이 확인된 양극재 및 ESS 전력설비 관련주 비중 확대."
      },
      "classification": {
        "primary_topic": "tech",
        "secondary_topics": ["energy", "stock"],
        "tags": ["호남반도체", "ESS흑자전환", "양극재턴어라운드", "구마모토모델"]
      }
    }
  },
  "jbEfkQCjcM0": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "jbEfkQCjcM0",
        "title": "다우 신고가 터졌다…다음은 나스닥? 9월까지 '2막 랠리' 가능성 | 한상희 한화투자증권 수석연구위원 [글로벌 인터뷰]",
        "published": "2026-08-10T11:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=jbEfkQCjcM0",
        "thumbnail": "https://img.youtube.com/vi/jbEfkQCjcM0/hqdefault.jpg"
      },
      "analysis": {
        "summary": "다우 지수의 사상 최고치 경신에 이어 나스닥 중심의 <span class=\"text-cyan-300 font-semibold\">'2막 상승 랠리'</span>가 9월 연준 금리 인하 피벗과 맞아떨어지며 전개될 전망임. 빅테크의 AI ROIC(25%)가 높게 유지되어 상승 여력이 충분함.",
        "key_claims": [
          "다우 지수의 신고가 돌파는 증시 상승 동력이 가치주 및 전통 제조업으로 다변화되었음을 보여줌.",
          "빅테크의 AI 투자 수익률(ROIC)이 차입 비용을 압도하여 9월 나스닥 2막 랠리를 견인할 것임."
        ],
        "data_points": [
          "빅테크 AI ROIC: 약 25% 달성 (자본 조달 금리 5~6% 대비 월등히 높음)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "전통주(다우)와 기술주(나스닥)의 선순환 상승 및 금리 하락 피벗이 증시 2막 랠리를 지지하기 때문임.",
        "key_companies": ["Apple", "Microsoft", "NVIDIA"],
        "insight": "빅테크 CapEx 우려는 25%의 압도적 AI ROIC 실적으로 무력화되며 증시 우상향 궤적을 공고히 만듦.",
        "action_point": "9월 랠리를 앞두고 조정을 거친 빅테크 대장주 및 반도체 밸류체인 보유 전략 집행."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["다우신고가", "나스닥2막랠리", "AI_ROIC", "9월피벗"]
      }
    }
  },
  "m1R65dyI8e8": {
    "primary": "tech",
    "data": {
      "video": {
        "id": "m1R65dyI8e8",
        "title": "사상 최초 단전자 반도체 등장",
        "published": "2026-08-10T12:00:00+00:00",
        "channel_name": "Softdragon SOD",
        "url": "https://www.youtube.com/watch?v=m1R65dyI8e8",
        "thumbnail": "https://img.youtube.com/vi/m1R65dyI8e8/hqdefault.jpg"
      },
      "analysis": {
        "summary": "상온에서 전자를 단 1개씩 제어하는 <span class=\"text-cyan-300 font-semibold\">단전자 트랜지스터(SET)</span> 소자가 개발되어 초저전력 차세대 AI 반도체의 한계를 극복할 기술적 돌파구가 마련됨.",
        "key_claims": [
          "단전자 반도체는 기존 반도체 대비 전력 소모를 1/1,000 수준으로 획기적으로 줄임.",
          "상온 작동 기술 확보로 양자 컴퓨팅 및 차세대 초미세 공정에 실용적 적용 가능성 제시."
        ],
        "data_points": [],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "AI 데이터센터의 최대 병목인 전력 소모 문제를 фундамента적으로 해결할 차세대 반도체 원천기술이기 때문임.",
        "key_companies": ["TSMC", "삼성전자"],
        "insight": "전력 태우기 중심의 현재 AI 반도체 구조에서 단전자 제어 기술은 미래 10년을 좌우할 파괴적 혁신 기술임.",
        "action_point": "차세대 초미세 반도체 원천 기술 보유 연구소 및 파운드리 대장주의 장기 관점 주시."
      },
      "classification": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["단전자반도체", "초저전력칩", "차세대소자", "상온SET"]
      }
    }
  },
  "okw-BDMWb1g": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "okw-BDMWb1g",
        "title": "CPI 발표 앞두고 금리 또 상승…엔비디아, 인텔 등 자금 조달 지속 [월가 뉴스레터]",
        "published": "2026-08-10T22:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=okw-BDMWb1g",
        "thumbnail": "https://img.youtube.com/vi/okw-BDMWb1g/hqdefault.jpg"
      },
      "analysis": {
        "summary": "7월 CPI 발표를 앞둔 관망세 속에 10년물 국채 금리가 반등함. 엔비디아의 $500억 AI 펀딩 플랫폼 구축과 인텔의 $150억 유상증자 등 <span class=\"text-cyan-300 font-semibold\">빅테크의 자금 조달 노이즈</span>가 시장 수급을 제약함.",
        "key_claims": [
          "CPI 발표 직전 관망세로 국채 금리가 상승하며 기술주 단기 숨고르기를 유발함.",
          "엔비디아와 인텔의 대규모 자금 조달은 희석 우려를 낳으나 장기 CapEx 확장의 기반이 됨."
        ],
        "data_points": [
          "엔비디아 AI 자금 조달 펀드: 500억 달러 규모 (사모펀드 연계)",
          "인텔 유상증자: 150억 달러 주식 발행"
        ],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "CPI 이벤트 전 단기 관망세와 증자 노이즈가 주가 상승폭을 제한하고 있기 때문임.",
        "key_companies": ["NVIDIA", "Intel"],
        "insight": "자금 조달로 인한 주가 단기 조정을 장기 AI 인프라 수주 확정 지표로 해석해야 함.",
        "action_point": "CPI 결과 확인 후 단기 조정받은 반도체주 분할 매수 대응."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["CPI발표관망", "엔비디아펀딩", "인텔유상증자", "국채금리상승"]
      }
    }
  },
  "peUMPLwyGuA": {
    "primary": "crypto",
    "data": {
      "video": {
        "id": "peUMPLwyGuA",
        "title": "비트코인 자금 유입 급증…클래리티 9월 연기에도 '최악은 피했다' | 서동주, 김동환, 박상혁 디지털애셋 편집장 [크립토 PLUS]",
        "published": "2026-08-10T10:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=peUMPLwyGuA",
        "thumbnail": "https://img.youtube.com/vi/peUMPLwyGuA/hqdefault.jpg"
      },
      "analysis": {
        "summary": "비트코인 현물 ETF로 <span class=\"text-cyan-300 font-semibold\">8억 5,000만 달러 대규모 자금</span>이 순유입되며 강세 기반이 복원됨. 클래리티 법안 표결이 9월 15일로 연기되었으나 악재 소멸로 규제 리스크 최악을 지났다는 평임.",
        "key_claims": [
          "비트코인 현물 ETF 자금 재유입이 크립토 하방을 강력히 지지함.",
          "미 상원 클래리티 법안 연기는 악재가 아니며 9월 법제화 완성 수순임."
        ],
        "data_points": [
          "비트코인 현물 ETF 순유입액: 8억 5,000만 달러 돌파"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "기관 매수세(ETF 순유입) 복원과 달러 약세 피벗이 크립토 시장의 하방 안정성을 입증하기 때문임.",
        "key_companies": ["Bitcoin", "Ethereum", "BlackRock"],
        "insight": "기관 현물 ETF 자금 유입은 단기 시세 변동을 넘어 크립토가 제도권 대체 자산으로 부상했음을 보여줌.",
        "action_point": "9월 클래리티 법안 표결 전 비트코인 및 이더리움 현물 ETF 분할 매입 유지."
      },
      "classification": {
        "primary_topic": "crypto",
        "secondary_topics": ["stock", "economy"],
        "tags": ["비트코인ETF", "8억5천만달러유입", "클래리티법안", "기관자금"]
      }
    }
  },
  "rpG7N0fe1PE": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "rpG7N0fe1PE",
        "title": "반등한 시장, 지금이 기회일까? 투자자가 해야 할 대응 | 이혁진, 여도은, 허재무 [아침N투자]",
        "published": "2026-08-11T00:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=rpG7N0fe1PE",
        "thumbnail": "https://img.youtube.com/vi/rpG7N0fe1PE/hqdefault.jpg"
      },
      "analysis": {
        "summary": "증시 반등 시점에서 조정받은 <span class=\"text-cyan-300 font-semibold\">메모리 반도체 대장주</span>와 AI 소부장(기판, 전공정 장비)의 저점 매수 전략을 권장함. 8월 롤러코스터 장세 이후 실적 모멘텀주로의 포트폴리오 재편 필요성 강조.",
        "key_claims": [
          "반도체 급락은 펀더멘털 훼손이 아닌 단기 수급 분산 우려 때문이었으므로 반등 기회가 옴.",
          "실적 가이던스가 살아있는 소부장 기판 및 전공정 장비주에 집중 대응해야 함."
        ],
        "data_points": [],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "시장 지수가 바닥을 다지고 실적 모멘텀주 중심의 반등세가 시작되었기 때문임.",
        "key_companies": ["삼성전자", "SK하이닉스", "대덕전자"],
        "insight": "공포 심리로 낙폭이 컸던 반도체 밸류체인은 시장 반등기 가장 빠른 회복 탄력성을 보임.",
        "action_point": "조정받은 메모리 대장주와 기판/장비 수혜주를 저점 분할 매수."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["시장반등", "저점매수", "반도체소부장", "아침N투자"]
      }
    }
  },
  "s935oWldYWE": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "s935oWldYWE",
        "title": "어차피 하락은 계속된다? | \"반도체 호재는 진통제일 뿐\" | 이주완 인더스트리 애널리스트 [더블 업]",
        "published": "2026-08-11T00:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=s935oWldYWE",
        "thumbnail": "https://img.youtube.com/vi/s935oWldYWE/hqdefault.jpg"
      },
      "analysis": {
        "summary": "반도체 산업 분석가 이주완 애널리스트가 HBM 공급 과잉 우려 및 스마트폰/PC 레거시 수요 둔화를 근거로 <span class=\"text-rose-400 font-medium\">메모리 장기 피크아웃 경고론</span>을 제기함.",
        "key_claims": [
          "HBM 고마진 착시 현상이 전체 세트(스마트폰/PC) 수요 둔화를 가리고 있음.",
          "2027년 HBM 공급 과잉과 레거시 D램 가격 하락으로 반도체 사이클이 꺾일 수 있음."
        ],
        "data_points": [
          "세트 수요 성장률: 온디바이스 AI에도 불구하고 스마트폰/PC 출하량 한 자릿수 둔화"
        ],
        "signal": "bearish",
        "signal_confidence": "medium",
        "signal_reason": "레거시 IT 세트 수요 둔화와 2027년 HBM 설비 과잉 공급 리스크를 경고하는 신중론이기 때문임.",
        "key_companies": ["삼성전자", "SK하이닉스", "Micron"],
        "insight": "AI 서버 중심의 강세 뒤편에 존재하는 레거시 IT 세트 부진 리스크에 대한 균형 잡힌 시각이 필요함.",
        "action_point": "반도체 포트폴리오 중 레거시 비중이 높은 종목은 줄이고 AI 전용 HBM/LPDDR5X 비중이 높은 종목으로 압축."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["반도체신중론", "HBM공급과잉", "피크아웃경고", "세트수요둔화"]
      }
    }
  },
  "sVUTmmjuZ6s": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "sVUTmmjuZ6s",
        "title": "300평 펜트하우스 정부가 막았다 (언더스탠딩 장순원 기자)",
        "published": "2026-08-11T00:00:00+00:00",
        "channel_name": "언더스탠딩_Understanding",
        "url": "https://www.youtube.com/watch?v=sVUTmmjuZ6s",
        "thumbnail": "https://img.youtube.com/vi/sVUTmmjuZ6s/hqdefault.jpg"
      },
      "analysis": {
        "summary": "정부의 초고가 주택(300평 펜트하우스) 건축 기준 강화 및 용적률/분양가 규제 강화가 고가 부동산 유동성 분산을 유도하는 경제적 파급효과를 분석함.",
        "key_claims": [
          "초럭셔리 펜트하우스 규제 강화로 부동산 양극화 억제 조치가 단행됨.",
          "부동산 규제 강화는 자산 유동성이 주식 및 자본 시장으로 흐르는 계기가 될 수 있음."
        ],
        "data_points": [],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "부동산 정책 변화가 자산 시장 수급에 미치는 영향이 유동성 이동과 건설 경기 둔화 두 갈래로 나뉘기 때문임.",
        "key_companies": [],
        "insight": "부동산 규제는 자산가들의 자금을 부동산에서 증시나 채권 등 금융 자산으로 이동시키는 유동성 재배치 효과를 낳음.",
        "action_point": "부동산 규제 반사 수혜로 금융 자산(주식 및 ETF) 유입 여부를 관찰."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["부동산규제", "펜트하우스", "자산유동성", "언더스탠딩"]
      }
    }
  },
  "tQ3IkItUsQk": {
    "primary": "energy",
    "data": {
      "video": {
        "id": "tQ3IkItUsQk",
        "title": "[지식뉴스] \"다들 착각하고 있어요, 이란전쟁의 진짜 승자는 '미국'\"...에너지 패권 전쟁 속 한국에게 찾아온 마지막 기회 / 교양이를 부탁해",
        "published": "2026-08-11T00:00:00+00:00",
        "channel_name": "교양이를 부탁해",
        "url": "https://www.youtube.com/watch?v=tQ3IkItUsQk",
        "thumbnail": "https://img.youtube.com/vi/tQ3IkItUsQk/hqdefault.jpg"
      },
      "analysis": {
        "summary": "중동 지정학 분쟁 속에서 미국이 셰일 오일/LNG 수출을 독점하며 최대 수혜를 입음. 이에 대응해 한국은 <span class=\"text-cyan-300 font-semibold\">SMR(소형원자로) 및 원전 기술 수주</span>로 에너지 패권 전쟁에서 반사 이익을 노릴 기회를 잡음.",
        "key_claims": [
          "중동 리스크는 미국의 LNG 및 에너지 패권을 극대화하는 결과로 이어짐.",
          "한국은 SMR 국가전략기술 지정과 함께 글로벌 원전 수주(체코 등) 확장의 기회를 맞음."
        ],
        "data_points": [
          "미국 LNG 수출량: 글로벌 1위 유지",
          "한국 SMR 원전 세액 공제 지정 추진"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "에너지 안보가 부각되는 정세에서 한국 원전 및 SMR 밸류체인의 수주 가시성이 확보되었기 때문임.",
        "key_companies": ["두산에너빌리티", "한전기술"],
        "insight": "글로벌 에너지 패권 전쟁은 단순 원유 시장을 넘어 원전 및 SMR 차세대 에너지 기술력 보유국에게 막대한 국가적 수주 기회를 안겨줌.",
        "action_point": "SMR 원전 국가전략기술 수혜주인 두산에너빌리티 및 원전 소부장주 매수 관점 대응."
      },
      "classification": {
        "primary_topic": "energy",
        "secondary_topics": ["economy", "stock"],
        "tags": ["에너지패권", "미국셰일LNG", "SMR원전", "두산에너빌리티"]
      }
    }
  },
  "wEnMi8VoF3s": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "wEnMi8VoF3s",
        "title": "하반기 코스피 여전히 위쪽…AI 자금줄 쥔 '미 국채'가 마지막 변수ㅣ홍선애, 이은택 KB증권 자산배분전략 이사 [여의도 인사이트]",
        "published": "2026-08-11T01:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=wEnMi8VoF3s",
        "thumbnail": "https://img.youtube.com/vi/wEnMi8VoF3s/hqdefault.jpg"
      },
      "analysis": {
        "summary": "KB증권 자산배분 전략에 따르면 하반기 코스피 상승 목표치(3,000+ 포인트)가 유지됨. 미국 10년물 국채 금리가 4.4% 이하로 하향 안정화되는지 여부가 AI Big Tech CapEx 및 한국 수출 증시 랠리의 마지막 변수임.",
        "key_claims": [
          "코스피 하반기 상방 목표는 견조하며 8월 조정을 지나 9~10월 강한 반등이 예상됨.",
          "미 국채 금리가 안정되면 AI 자금 조달 비용 압박이 해소되어 증시 랠리가 재개됨."
        ],
        "data_points": [
          "코스피 목표 지수: 하반기 3,000+ 포인트 제시",
          "미국 10년물 국채 금리 임계점: 4.4% 이하 하향 안정화 조건"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "한국 수출 대장주의 이익 성장이 견조하고 미 국채 금리 하향 안정 시 강력한 지수 반등이 예상되기 때문임.",
        "key_companies": ["삼성전자", "SK하이닉스", "현대차"],
        "insight": "미 국채 금리 안정은 AI 인프라 투자 자금 흐름을 원활히 하여 국내 반도체·자동차 수출주의 상방을 여는 핵심 트리거임.",
        "action_point": "미 국채 금리 4.4% 이하 하락을 확인하며 코스피 대장주 및 반도체/자동차 비중 확대."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["economy", "tech"],
        "tags": ["코스피하반기전망", "미국국채금리", "KB증권자산배분", "AI자금줄"]
      }
    }
  },
  "zVjlEpwSwt4": {
    "primary": "etc",
    "data": {
      "video": {
        "id": "zVjlEpwSwt4",
        "title": "대통령과 연준의장은 진짜 현피를 뜬 적이 있다",
        "published": "2026-08-11T01:30:00+00:00",
        "channel_name": "언더스탠딩_Understanding",
        "url": "https://www.youtube.com/watch?v=zVjlEpwSwt4",
        "thumbnail": "https://img.youtube.com/vi/zVjlEpwSwt4/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1965년 린든 B. 존슨 미국 대통령과 윌리엄 맥체스니 마틴 연준 의장이 금리 인상을 둘러싸고 텍사스 목장에서 벌인 정면충돌(현피) 사건을 해설하며 연준의 독립성 역사를 비하인드로 풀어냄.",
        "key_claims": [
          "존슨 대통령이 베트남전 자금 조달을 위해 금리 인상을 반대했으나 마틴 연준 의장이 소신을 지켜 금리를 인상함.",
          "이 사건은 연준 통화 정책 독립성을 상징하는 역사적 이정표가 됨."
        ],
        "data_points": [
          "사건 발생 연도: 1965년 텍사스 존슨 대통령 목정 회동"
        ],
        "signal": "na",
        "signal_confidence": "high",
        "signal_reason": "미국 통화정책 역사 및 연준 독립성에 관한 지식 교양 콘텐츠임.",
        "key_companies": [],
        "insight": "정치적 압력 속에서도 중앙은행의 독립성을 지킨 역사는 오늘날 연준 독립성 유지의 중요한 교훈임.",
        "action_point": "투자 자산 운용과는 무관한 역사 교양 영상이므로 의사결정 대상에서 제외함."
      },
      "classification": {
        "primary_topic": "etc",
        "secondary_topics": ["economy"],
        "tags": ["연준독립성", "LBJ존슨대통령", "마틴의장", "통화정책역사"]
      }
    }
  }
}

count = 0
for vid, item in batch_data.items():
    topic = item["primary"]
    data = item["data"]
    target_dir = os.path.join("data", "analyzed", topic)
    os.makedirs(target_dir, exist_ok=True)
    out_file = os.path.join(target_dir, f"{vid}.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    pending_file = os.path.join("data", "pending", f"{vid}.json")
    if os.path.exists(pending_file):
        os.remove(pending_file)
        
    count += 1
    print(f"[{count:02d}/24] Saved {topic}/{vid}.json and removed pending file.")

print("\nSuccessfully processed all 24 pending files!")
