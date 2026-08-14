import json
import os
from pathlib import Path

# 8 pending files dictionary
batch_8_data = {
  "3cxyGSzT2PY": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "3cxyGSzT2PY",
        "title": "[어바웃 뉴욕] BTS 콘서트, 아미들이 낸 티켓값은 어디로 갔나 | 이나연 특파원",
        "published": "2026-08-05T03:00:20+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=3cxyGSzT2PY",
        "thumbnail": "https://img.youtube.com/vi/3cxyGSzT2PY/hqdefault.jpg"
      },
      "analysis": {
        "summary": "<span class=\"text-amber-300 font-bold\">티켓 마스터</span>와 <span class=\"text-cyan-300 font-semibold\">라이브 네이션</span>이 글로벌 매표소 시장 86%를 독점하며 전가와 리세일 거래 양쪽에서 사상 최대 수수료 마진(티케팅 37%)을 챙기고 있음. 미 법무부 및 34개 주정부가 <span class=\"text-rose-400 font-medium\">반독점법 위반 소송</span>으로 회사 분리 매각을 추진 중이나 2분기 실적은 역대 최고치를 경신함.",
        "key_claims": [
          "라이브 네이션-티켓 마스터는 전가 매표와 2차 리세일 플랫폼을 동시 소유하여 양방향 고마진 수수료 수익 구조를 구축함.",
          "미국 법무부와 34개 주정부가 독점 폐해를 이유로 기업 분리매각 소송을 진행 중이나, 라이브 네이션 2분기 관객 및 티켓 매출은 사상 최고치를 달성함.",
          "공연 마진은 3.3%에 불과하나 티케팅 마진은 37%에 달해 매표소 독점권이 실적의 핵심 원동력임."
        ],
        "data_points": [
          "1차 티케팅 시장 독점 점유율: 약 86%",
          "티케팅 부문 조정 영업이익률: 약 37%",
          "2분기 공연 관객 수: 4,900만 명 / 티켓 판매: 9,000만 장"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "역대 최고 실적과 압도적 티케팅 독점력에도 불구하고 <span class=\"text-rose-400 font-medium\">미 법무부 반독점 강제 분리매각 소송</span>이라는 거대한 사법 리스크가 상존함.",
        "key_companies": ["라이브 네이션(LYV)", "티켓 마스터", "하이브(HYBE)"],
        "insight": "엔터 산업의 핵심 수익은 공연 자체가 아니라 티케팅 매표소 독점 플랫폼에서 창출됨. 미국 법원의 독점 판결 및 분리매각 여부가 엔터 플랫폼 생태계 재편의 관건임.",
        "action_point": "라이브 네이션(LYV)의 강한 실적 펀더멘탈과 별개로 법원의 반독점 구제 조치 판결 향방을 주시하며 변동성 대응 필요."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["etc"],
        "tags": ["라이브네이션", "티켓마스터", "반독점", "BTS콘서트", "티케팅"]
      }
    }
  },
  "h-WpAGTcPOM": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "h-WpAGTcPOM",
        "title": "\"모두가 당했습니다\"",
        "published": "2026-08-05T00:19:48+00:00",
        "channel_name": "월텍남",
        "url": "https://www.youtube.com/watch?v=h-WpAGTcPOM",
        "thumbnail": "https://img.youtube.com/vi/h-WpAGTcPOM/hqdefault.jpg"
      },
      "analysis": {
        "summary": "최근 <span class=\"text-rose-400 font-medium\">메모리 반도체 폭락</span>은 개미들의 패닉셀 물량을 해지펀드가 <span class=\"text-amber-300 font-bold\">숏커버링 및 순매수</span>로 받아내며 수급이 정상화된 결과임. 시타델 보고서에 따르면 과열 레버리지가 25% 이상 청산되어 기술주 선행 PER이 20배(5년 평균 25배)로 저평가 구간에 진입함.",
        "key_claims": [
          "개인 투자자들의 주간 평균 20배 달하는 매도물량을 기관/해지펀드가 숏커버링으로 모두 흡수함.",
          "S&P500 기술주 선행 PER은 20배 수준으로 최근 5년 평균(25배) 및 10년 평균(23배) 대비 저평가 상태임.",
          "빅테크 CAPEX 투자는 2027년 1.3조~1.5조 달러(2,000조 원)로 상향 조정되어 AI 인프라 펀더멘탈이 견조함."
        ],
        "data_points": [
          "기술주 선행 PER: 20배 (2022년 하락장 수준 저평가)",
          "빅테크 2027년 AI CAPEX 전망: 1.3조~1.5조 달러 (약 2,000조 원)",
          "기술주 기업 EPS 상승률 전망: 40%~50%"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "<span class=\"text-amber-300 font-bold\">레버리지 거품 청산</span> 완료 후 실적 이익 상승률(EPS +40~50%)에 기반한 강력한 <span class=\"text-cyan-300 font-semibold\">실적 장세</span> 진입이 명백함.",
        "key_companies": ["엔비디아(NVDA)", "SK하이닉스", "삼성전자", "시타델"],
        "insight": "수급 왜곡으로 인한 투매 현상은 막을 내렸으며, AI 클라우드 매출 폭증과 막대한 CAPEX 집행으로 반도체·네트워크·광통신 등 AI 병목 인프라 기업의 수혜가 지속될 것임.",
        "action_point": "저평가 영역에 진입한 메모리 반도체 및 광통신(루멘텀), 네오클라우드(코이브, 아이렌) 밸류체인 분할 매수 관점 접근."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["economy", "tech"],
        "tags": ["숏커버링", "시타델", "메모리저평가", "CAPEX", "선행PER"]
      }
    }
  },
  "HPsDQZJc9VU": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "HPsDQZJc9VU",
        "title": "AMD 날았다 머스크가 찬물?ㅣ일라이릴리 어닝 서프라이즈…비만약 질주ㅣ디즈니 호실적…스트리밍·테마파크 동반 성장ㅣ샌디스크, 4분기 실적 발표…메모리 업황 주목ㅣ홍혜진의 뉴욕브리핑",
        "published": "2026-08-05T13:59:04+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=HPsDQZJc9VU",
        "thumbnail": "https://img.youtube.com/vi/HPsDQZJc9VU/hqdefault.jpg"
      },
      "analysis": {
        "summary": "<span class=\"text-cyan-300 font-semibold\">AMD</span> 2분기 매출 115억 달러, 영업이익 사상 최고치 및 매출총이익률 56%를 기록하며 압도적 호실적을 달성함. <span class=\"text-cyan-300 font-semibold\">일라이 릴리</span>는 비만치료제 호조로 어닝 서프라이즈를 기록했고, 디즈니도 테마파크와 스트리밍 양방향 호실적을 거둠.",
        "key_claims": [
          "AMD 2분기 매출 115억 달러(사상 최고), 매출총이익률 56%, 조정 EPS 1.66달러로 시장 컨센서스 상회.",
          "일라이 릴리 매출 48% 급증하며 비만치료제(GLP-1) 수요 지속 확인 및 파이프라인 확장 인수 진행.",
          "AMD 컨퍼런스 콜에서 AI GPU용 HBM 공급망 확보 및 데이터센터 칩 수요 강세 확인."
        ],
        "data_points": [
          "AMD 2분기 매출: 115억 달러 (YoY 상향, 마진율 56%)",
          "일라이 릴리 2분기 매출 증가율: 48% (GLP-1 실적 견인)",
          "AMD CAPEX: 8억 8,000만 달러 (설비투자 확대)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "<span class=\"text-cyan-300 font-semibold\">AMD와 일라이 릴리</span> 등 주력 기술주 및 바이오 헬스케어 빅테크의 펀더멘탈 실적 성장이 입증됨.",
        "key_companies": ["AMD", "일라이 릴리(LLY)", "디즈니(DIS)", "SK하이닉스", "삼성전자"],
        "insight": "AMD의 AI 가속기 및 데이터센터 CPU 성장은 국내 메모리 반도체(HBM, DDR5) 수요 확대의 직접적 신호탄임.",
        "action_point": "AMD 실적 발표 후 일시적 조정 구간을 활용하여 AI 반도체 밸류체인 및 비만치료제 대장주 주가 추이 모니터링."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["AMD실적", "일라이릴리", "어닝서프라이즈", "HBM수요", "디즈니"]
      }
    }
  },
  "iKfvqq6H5Is": {
    "primary": "robot",
    "data": {
      "video": {
        "id": "iKfvqq6H5Is",
        "title": "삼성전자 로봇사업 재편… 큰 그림 보인다",
        "published": "2026-08-05T08:00:00+00:00",
        "channel_name": "엔지니어TV",
        "url": "https://www.youtube.com/watch?v=iKfvqq6H5Is",
        "thumbnail": "https://img.youtube.com/vi/iKfvqq6H5Is/hqdefault.jpg"
      },
      "analysis": {
        "summary": "<span class=\"text-cyan-300 font-semibold\">삼성전자</span>가 DX 부문 내 로봇 사업 조직을 대대적으로 재편하며 <span class=\"text-amber-300 font-bold\">휴머노이드 및 AI 융합 로봇</span> 상용화 속도를 올리고 있음. 레인보우로보틱스와의 협력을 공고히 하고 서비스·제조용 로봇 생태계를 구축하는 전략임.",
        "key_claims": [
          "삼성전자가 로봇 전담 조직을 강화하여 가전·스마트홈과 연계된 봇핏(Bot Fit) 및 AI 로봇 플랫폼 다각화 추진.",
          "지분 투자한 레인보우로보틱스 양팔형 협동 로봇 및 피지컬 AI 결합 모델 도입 본격화.",
          "반도체 및 배터리 공장 자동화에 자체 로봇 기술 우선 적용 예정."
        ],
        "data_points": [
          "삼성전자 차세대 로봇 투자 규모: 조 단위 생태계 조성",
          "협동로봇 및 휴머노이드 상용화 타깃: 2026~2027년"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "<span class=\"text-cyan-300 font-semibold\">삼성전자</span>의 본격적인 로봇 사업 재편 및 실질적 자금/기술 투입으로 <span class=\"text-amber-300 font-bold\">피지컬 AI 로봇</span> 시장 개화가 가속화됨.",
        "key_companies": ["삼성전자", "레인보우로보틱스"],
        "insight": "글로벌 IT 빅테크(테슬라, 엔비디아, 삼성)가 모두 휴머노이드 로봇 주도권 싸움에 뛰어들면서 로봇 핵심 부품 및 엑추에이터 밸류체인의 재평가가 이루어질 것임.",
        "action_point": "삼성 로봇 생태계와 직결된 레인보우로보틱스 및 핵심 감속기·센서 관련 기업 주가 동향 주목."
      },
      "classification": {
        "primary_topic": "robot",
        "secondary_topics": ["tech", "stock"],
        "tags": ["삼성로봇", "레인보우로보틱스", "휴머노이드", "피지컬AI", "로봇재편"]
      }
    }
  },
  "J29kcYgE0Cs": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "J29kcYgE0Cs",
        "title": "[미드나잇 LIVE] 리얼티인컴 사지 마라? 이 종목 사세요 | BOA \"3회 금리인하 시점\" | 마크 저커버그 의미심장 발언",
        "published": "2026-08-06T00:00:00+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=J29kcYgE0Cs",
        "thumbnail": "https://img.youtube.com/vi/J29kcYgE0Cs/hqdefault.jpg"
      },
      "analysis": {
        "summary": "<span class=\"text-amber-300 font-bold\">Bank of America</span>가 연내 3회 연준 금리 인하 가능성을 제시함에 따라 리츠 및 배당주 재평가 국면 진입. <span class=\"text-cyan-300 font-semibold\">리얼티인컴(O)</span> 대비 배당 성장률과 재무 안정성이 높은 대체 리츠 종목 분석 및 빅테크 AI 발언 영향 진단.",
        "key_claims": [
          "BOA는 고용 지표 둔화와 인플레이션 안정을 근거로 9월부터 연내 3차례 기준금리 인하 예측.",
          "금리 인하 수혜주인 리츠(REITs) 부문에서 단순 고배당주 리얼티인컴보다 이커머스/물류 기반 고성장 리츠 선호 권장.",
          "메타 마크 저커버그의 AI 인프라 투자 정당화 발언으로 테크주와 배당주의 균형 투자 부각."
        ],
        "data_points": [
          "BOA 예측 연내 기준금리 인하 횟수: 3회",
          "미국 7월 ADP 민간 고용 증가폭: 4만 4천 명 (예상치 7만 명 하회)"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "<span class=\"text-amber-300 font-bold\">연준 금리 인하</span> 가시화로 고금리 피해 업종이었던 <span class=\"text-cyan-300 font-semibold\">리츠 및 부동산 섹터</span> 자금 유입 수혜 예상.",
        "key_companies": ["리얼티인컴(O)", "메타(META)", "Bank of America"],
        "insight": "금리 피벗(Pivot) 시기에는 배당률만 높은 종목보다 순자산가치(NAV) 증가율과 자본 이득이 동시 발생할 수 있는 성장형 리츠 종목 선택이 유리함.",
        "action_point": "금리 인하 전환에 맞춰 금리 민감주(리츠, 수소/에너지 인프라) 포트폴리오 비중 조절 점검."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["금리인하", "BOA", "리얼티인컴", "리츠", "저커버그"]
      }
    }
  },
  "kaSf9gSynRw": {
    "primary": "tech",
    "data": {
      "video": {
        "id": "kaSf9gSynRw",
        "title": "\"곧 터진다, AI 반도체 종말?\" 마크 3년 연속 경고… 이제 돈은 여기서 터집니다",
        "published": "2026-08-05T11:00:00+00:00",
        "channel_name": "월텍남",
        "url": "https://www.youtube.com/watch?v=kaSf9gSynRw",
        "thumbnail": "https://img.youtube.com/vi/kaSf9gSynRw/hqdefault.jpg"
      },
      "analysis": {
        "summary": "마크 저커버그와 빅테크 수장들이 AI 데이터센터 병목 현상이 GPU 칩 자체에서 <span class=\"text-amber-300 font-bold\">광통신 네트워크 및 메모리 전력 인프라</span>로 이동하고 있음을 경고함. 2027년까지 빅테크 CAPEX 지출 1.3조 달러 중 <span class=\"text-cyan-300 font-semibold\">광통신(CPO)과 네오클라우드</span> 섹터가 최대 수혜를 입을 전망.",
        "key_claims": [
          "GPU 칩 확보만으로는 한계에 도달했으며, 데이터센터 간 데이터 전송 병목을 해결할 광통신(루멘텀 등)이 폭발적 성장 단계 진입.",
          "메모리 반도체 CAPEX 지출이 2027년 7,610억 달러로 급증하며 D램/HBM 공급 부족(Shortage) 장기화.",
          "전력 수급 및 클라우드 인프라를 신속히 확보한 네오클라우드(코이브, 아이렌) 기업들의 4분기 영업이익 흑자전환 개화."
        ],
        "data_points": [
          "광통신 대장주(루멘텀) EPS 성장률: 연간 130%",
          "빅테크 2027년 메모리 반도체 지출액: 7,610억 달러",
          "네오클라우드 확보 계획 전력: 30GW 이상"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "AI 병목 지점이 컴퓨팅 칩에서 <span class=\"text-cyan-300 font-semibold\">광통신 및 메모리/전력 인프라</span>로 확장됨에 따라 후속 밸류체인의 폭발적 수혜 진입.",
        "key_companies": ["메타(META)", "루멘텀(LITE)", "코이브(CORZ)", "엔비디아(NVDA)"],
        "insight": "AI 패러다임 변화는 단기 GPU 붐을 넘어, 데이터 전송 속도를 결정을 짓는 광통신 파이버 및 차세대 전력 인프라로 지속적인 온기가 확산 중임.",
        "action_point": "조정을 거친 광통신 메이저(LITE) 및 네오클라우드/메모리 부품주 펀더멘탈 실적 확인 후 분할 매수."
      },
      "classification": {
        "primary_topic": "tech",
        "secondary_topics": ["stock", "energy"],
        "tags": ["광통신", "루멘텀", "네오클라우드", "마크저커버그", "AI병목"]
      }
    }
  },
  "TD2oHqb0jPo": {
    "primary": "space",
    "data": {
      "video": {
        "id": "TD2oHqb0jPo",
        "title": "[1부] 138억 년 동안 우주가 확장할 수 있었던 진짜 이유! (우주팽창의 비밀)",
        "published": "2026-08-05T09:00:00+00:00",
        "channel_name": "안될과학 Unrealscience",
        "url": "https://www.youtube.com/watch?v=TD2oHqb0jPo",
        "thumbnail": "https://img.youtube.com/vi/TD2oHqb0jPo/hqdefault.jpg"
      },
      "analysis": {
        "summary": "우주 탄생 138억 년 동안 공간이 팽창해온 물리적 원리와 <span class=\"text-amber-300 font-bold\">암흑 에너지(Dark Energy)</span>의 역할을 입자물리학 및 천문학적 관점에서 해설함. 우리가 관측 가능한 물질은 우주의 단 5%에 불과하며 95%는 미지의 암흑 물질과 에너지라는 점을 탐구.",
        "key_claims": [
          "우주는 단순히 물질이 퍼져나가는 것이 아니라 공간 자체가 빛보다 빠르게 팽창하는 인플레이션 과정을 거침.",
          "우주 구성 요소 중 일반 물질은 5%, 암흑 물질 27%, 암흑 에너지가 68%를 차지함.",
          "최근 차세대 우주망원경(제임스웹, 루빈 관측소) 데이터로 우주 팽창 속도 측정 불일치(허블 텐션) 해명 시도 중."
        ],
        "data_points": [
          "우주 나이: 138억 년",
          "관측 가능 일반 물질 비율: 5%",
          "암흑 에너지 비율: 68%"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "순수 우주 과학 기술 및 천문학 기초 이론 탐구 콘텐츠로 단기 투자 시그널과는 직접적 관련 없음.",
        "key_companies": [],
        "insight": "우주 관측 기술 발전은 차세대 센서, 광학 렌즈, 고성능 데이터 분석 컴퓨팅 파이프라인 발전을 견인하는 기술적 기반이 됨.",
        "action_point": "우주항공 테마 및 최첨단 광학/데이터 기술 기업의 기초 기술 개발 동향 참고."
      },
      "classification": {
        "primary_topic": "space",
        "secondary_topics": ["tech", "etc"],
        "tags": ["우주팽창", "암흑에너지", "138억년", "제임스웹", "우주과학"]
      }
    }
  },
  "ySlTqalG--I": {
    "primary": "etc",
    "data": {
      "video": {
        "id": "ySlTqalG--I",
        "title": "바다 30m 아래에서 인간이 100일간 살면 일어나는 기적?!",
        "published": "2026-08-05T07:00:00+00:00",
        "channel_name": "안될과학 Unrealscience",
        "url": "https://www.youtube.com/watch?v=ySlTqalG--I",
        "thumbnail": "https://img.youtube.com/vi/ySlTqalG--I/hqdefault.jpg"
      },
      "analysis": {
        "summary": "수심 30m 해저의 고압 환경에서 100일간 거주하는 <span class=\"text-cyan-300 font-semibold\">데니스 체임벌린 심해 프로젝트</span>를 통해 인간 생체 지표 변화와 텔로미어(수명 유전자) 연장 효과를 분석함. 고압 산소 치료 및 극한 환경 인체 적응 연구의 가능성 조명.",
        "key_claims": [
          "수심 20~30m 고압 수중 환경 거주 시 줄기세포 수증가 및 텔로미어 길이 연장 관측.",
          "심해 고압 환경은 체내 염증 감소 및 세포 재생 효과를 유도하는 고압산소 챔버 치료 원리와 유사.",
          "극한 환경 우주인 및 심해 연구원 생존 키트 기술 개발에 기여."
        ],
        "data_points": [
          "수중 거주 깊이: 해저 30m",
          "거주 기간: 100일 연속"
        ],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "의학·생명과학 연구 기반 기초 과학 실험 내용으로 특정 상장사 단기 영향 없음.",
        "key_companies": [],
        "insight": "항노화(Anti-aging) 및 줄기세포, 고압산소 치료 기술은 헬스케어 및 바이오 분야의 장기적 성장 테마임.",
        "action_point": "바이오 헬스케어 및 재생 의학 밸류체인의 장기 연구 과제 흐름 파악."
      },
      "classification": {
        "primary_topic": "etc",
        "secondary_topics": ["space"],
        "tags": ["해저100일", "고압산소", "텔로미어", "생체실험", "안될과학"]
      }
    }
  }
}

count = 0
for vid, item in batch_8_data.items():
    primary = item["primary"]
    data = item["data"]
    target_dir = Path(f"data/analyzed/{primary}")
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / f"{vid}.json"
    
    target_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    
    pending_file = Path(f"data/pending/{vid}.json")
    if pending_file.exists():
        pending_file.unlink()
        
    count += 1
    print(f"[{count}/8] Saved analyzed data to data/analyzed/{primary}/{vid}.json and removed pending file.")

print("\nAll 8 pending videos successfully analyzed and saved!")
