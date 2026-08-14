import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.batch_save import save_batch

batch_10 = [
  {
    "video": {
      "id": "w8PXBwftwiw",
      "title": "[26.08.12 오후 방송 전체보기] 8월에만 20% 오른 코스닥, 오늘은 오르락 내리락...내일의 운명은?",
      "published": "2026-08-12T11:00:30+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=w8PXBwftwiw",
      "thumbnail": "https://img.youtube.com/vi/w8PXBwftwiw/hqdefault.jpg"
    },
    "analysis": {
      "summary": "8월에만 20% 이상 급등한 코스닥 지수의 단기 변동성과 수급 순환매 양상을 분석함. 대장주 단기 밸류담 완화로 인해 <span class=\"text-cyan-300 font-semibold\">전공정 장비 및 반도체 소부장</span>과 바이오·2차전지 중소형주로 자금이 번지는 <span class=\"text-amber-300 font-bold\">수급 분산 장세</span>가 형성됨.",
      "key_claims": [
        "코스닥 8월 20% 급등에 따른 차익 실현 매물과 장중 등락폭 확대.",
        "반도체 소부장 및 저평가 중소형주 중심의 순환매 지속 유효."
      ],
      "data_points": [
        "코스닥 지수 8월 누적 상승률: 약 20% 기록"
      ],
      "signal": "bullish",
      "signal_reason": "코스닥 중심의 강력한 순환매 유동성과 소부장 실적 장세 선도.",
      "key_companies": ["원익IPS(030530)", "유진테크(084370)"],
      "insight": "지수 단기 급등 후의 변동성은 상방 추세를 꺾기보다 주도 섹터 내부의 1등 장비주로 수급이 재편되는 과정임.",
      "action_point": "코스닥 20% 상승 후 단기 등락 국면에서 실적 개선이 뚜렷한 소부장주 중심 대응."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["코스닥20%급등", "순환매장세", "반도체소부장", "코스닥전망", "삼프로TV"]
    }
  },
  {
    "video": {
      "id": "WgUtsEASCyU",
      "title": "[지식뉴스] \"결국 이 빚, 녹이는 수밖에 없어요\" 미국 40조 부채와 AI의 숨은 연결고리..베센트가 엔저에 개입한 진짜 이유 / 교양이를 부탁해",
      "published": "2026-08-12T11:30:29+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=WgUtsEASCyU",
      "thumbnail": "https://img.youtube.com/vi/WgUtsEASCyU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국의 40조 달러 막대한 국가 부채와 인플레이션을 <span class=\"text-amber-300 font-bold\">AI 생산성 혁명</span>으로 녹여내려는 백악관의 장기 거시 전략을 정밀 분석함. 재무 당국이 엔화 방어 및 30년물 국채 금리 상승 억제에 전격 개입한 본질은 AI 빅테크들의 <span class=\"text-cyan-300 font-semibold\">CapEx 투자 유동성 파이프라인</span>을 보존하기 위함임.",
      "key_claims": [
        "미국 국가 부채 부풀리기를 AI가 촉발하는 거시 생산성 증가로 상쇄하려는 구상.",
        "미 국채 30년물 금리 상승 방어를 통해 빅테크의 AI 투자 자금 경색 차단."
      ],
      "data_points": [
        "미국 국가 부채 총액: 약 40조 달러 경신"
      ],
      "signal": "neutral",
      "signal_reason": "거시 부채 리스크와 AI 생산성 인플레이션 흡수론의 팽팽한 교차.",
      "key_companies": ["마이크로소프트(MSFT)", "엔비디아(NVDA)"],
      "insight": "정부 부채 부담이 가중될수록 백악관은 생성형 AI가 이끄는 생산성 향상을 통해 물가 상승 압력을 흡수하는 정책을 최우선화함.",
      "action_point": "미 국채 금리 안정화 추이 및 미국 정부의 AI 인프라 정책 모니터링."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["미국부채40조", "AI생산성혁명", "국채금리방어", "엔저개입", "거시경제"]
    }
  },
  {
    "video": {
      "id": "WxeERpOAHqI",
      "title": "[문지웅의 빅머니 LIVE] 코어위브, 네비우스 폭등 이유 | 메모리 반도체 일제히 상승  | 7월 CPI 괜찮았지만 유가불안",
      "published": "2026-08-12T21:59:47+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=WxeERpOAHqI",
      "thumbnail": "https://img.youtube.com/vi/WxeERpOAHqI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "코어위브와 네비우스 등 네오클라우드 기업들의 호실적에 입힘어 글로벌 메모리 반도체 주가가 일제히 상승함. 7월 미국 CPI가 안정세를 보였으나 국제 유가 급등 노이즈가 상방을 제한하는 <span class=\"text-amber-300 font-bold\">차별화 실적 랠리</span>를 진단함.",
      "key_claims": [
        "코어위브와 네비우스의 AI 호스팅 폭등이 메모리 반도체 밸류체인 상승을 유인.",
        "미국 CPI 안정 속 유가 변동성이 거시 관망 요인으로 상존."
      ],
      "data_points": [
        "네비우스 AI 클라우드 매출 상승률: 514% 폭등"
      ],
      "signal": "bullish",
      "signal_reason": "AI 인프라 호스팅 폭등과 메모리 반도체 일제 상승 모멘텀.",
      "key_companies": ["코어위브(CoreWeave)", "네비우스(NBIS)", "SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "유가 불안 노이즈에도 불구하고 AI 인프라 수주 둔화가 없다는 데이터가 확인되면 반도체 주도주의 상승은 지속됨.",
      "action_point": "실적 모멘텀이 검증된 메모리 2사 및 네오클라우드 밸류체인 수혜주 보유."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["코어위브", "네비우스", "메모리반도체상승", "7월CPI", "빅머니LIVE"]
    }
  },
  {
    "video": {
      "id": "WZoZbrLfe6U",
      "title": "갑자기 시원해졌는데, 폭염 끝난 걸까?",
      "published": "2026-08-12T02:00:30+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=WZoZbrLfe6U",
      "thumbnail": "https://img.youtube.com/vi/WZoZbrLfe6U/hqdefault.jpg"
    },
    "analysis": {
      "summary": "한반도를 뒤덮었던 티베트 고기압과 북태평양 고기압의 이중 폭염 기조가 일시 후퇴하며 기온이 하강한 과학적 메커니즘을 해설함. 차가운 상공 기압골 유입에 따른 일시적 소강상태이며 늦더위 수증기 유입 가능성을 교양 기상학 관점에서 짚음.",
      "key_claims": [
        "북태평양 고기압 수퇴와 상공 차가운 공기 유입으로 폭염 일시 소강.",
        "기후 변동성에 따른 여름철 2차 늦더위 및 국지성 호우 기조 모니터링."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "기상학적 기온 변화 및 대기 대순환 해설 영상.",
      "key_companies": [],
      "insight": "기후 변화에 따른 폭염과 기온 변동성은 냉방 전력 수요 및 농산물 물가(신선식품 CPI)에 직접적 변수로 작용함.",
      "action_point": "여름철 기후 변동에 따른 전력 계통 및 기후 관련 원자재 물가 변동 모니터링."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["폭염끝", "기상학", "북태평양고기압", "기후변화", "안될과학"]
    }
  },
  {
    "video": {
      "id": "XXsjDpogBOg",
      "title": "\"제일 고생한 분은 주식에 몰빵한 분입니다\" 같은 7월에 반대편에서 싸게 담은 계좌엔 무엇이 있었나?ㅣ신환종 박사 [풀영상]",
      "published": "2026-08-11T08:00:29+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=XXsjDpogBOg",
      "thumbnail": "https://img.youtube.com/vi/XXsjDpogBOg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "7월 주식 시장 폭락장에서 주식 100% 몰빵 투자자들의 계좌 손실과 반대로, <span class=\"text-cyan-300 font-semibold\">미국 국채 및 단기 금리형 자산</span>을 보유하여 바닥에서 주식을 줍줍한 자산가들의 전략을 조명함. <span class=\"text-amber-300 font-bold\">현금 및 채권 자산배분</span>이 폭락장 대형 저가 매수의 승패를 가름을 강조함.",
      "key_claims": [
        "주식 100% 보유자의 폭락장 심리적 붕괴와 반대매매 위험성 경고.",
        "안전 자산(국채, 현금) 비중 유지를 통한 패닉 셀 시 저점 매수 실탄 확보의 중요성."
      ],
      "data_points": [
        "7월 시장 하락 시 채권 및 현금 비중 보유 계좌의 수익률 방어 및 저가 매수 성과"
      ],
      "signal": "bullish",
      "signal_reason": "자산배분을 통한 폭락장 저점 매수 기회 활용 및 장기 우량주 반등 기대.",
      "key_companies": ["이효석아카데미"],
      "insight": "진정한 성과는 장이 좋을 때 오르는 종목을 쥐는 것보다, 시장 폭락 때 저가로 주식을 주울 수 있는 현금·채권 실탄을 쥐고 있느냐에서 갈림.",
      "action_point": "주식 100% 올인 구도를 지양하고 20~30% 현금/국채 안전자산 포트폴리오 상시 유지."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["신환종", "자산배분", "폭락장대응", "현금비중", "미국국채"]
    }
  },
  {
    "video": {
      "id": "YAcLrEYopzM",
      "title": "일본 빚이 1경인데 빚 더 늘리는 이유 (한국외대 융합일본지역학부 이창민 교수)",
      "published": "2026-08-11T12:25:21+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=YAcLrEYopzM",
      "thumbnail": "https://img.youtube.com/vi/YAcLrEYopzM/hqdefault.jpg"
    },
    "analysis": {
      "summary": "일본 국가 부채가 1경 엔을 상회함에도 불구하고 다카이치 등 정가의 <span class=\"text-violet-300 font-medium\">적극 재정파</span>들이 국채 발행 및 재정 지출을 확대하려는 논리를 분석함. 엔저와 디플레이션 탈출, <span class=\"text-cyan-300 font-semibold\">반도체 및 미래 첨단 산업 국유화/보조금 지원</span>을 위해 재정 확대를 밀어붙이는 일본 거시 정책을 진단함.",
      "key_claims": [
        "일본 1경 엔 부채에도 불구하고 성장 동력 확보를 위한 적극 재정 지출 강행.",
        "반도체(라피더스, TSMC 구마모토 공장) 보조금 지원 등 산업 정책 자금 투입."
      ],
      "data_points": [
        "일본 국가 부채 규모: 1경 엔 상회"
      ],
      "signal": "neutral",
      "signal_reason": "일본 적극 재정에 따른 디플레 탈출 기대와 국가 부채 이자 부담 리스크의 대립.",
      "key_companies": ["TSMC(TSM)", "라피더스(Rapidus)"],
      "insight": "일본의 적극 재정 행보는 국가 부채 위험을 감수하면서도 첨단 반도체 제조 부활에 국력을 쏟겠다는 산업 정책적 결단임.",
      "action_point": "일본의 반도체 보조금 집행 및 엔/달러 환율 방향성 모니터링."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["일본부채1경", "이창민교수", "적극재정파", "엔저정책", "반도체보조금"]
    }
  },
  {
    "video": {
      "id": "YZc2620fAj8",
      "title": "[어바웃 뉴욕] 샐러드 공포가 덮친 미국…카바는 왜 스위트그린과 달랐나 | 이나연 특파원",
      "published": "2026-08-12T03:06:20+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=YZc2620fAj8",
      "thumbnail": "https://img.youtube.com/vi/YZc2620fAj8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 내 양상추 기생충 감염 리콜 사태로 샐러드 업계가 직격탄을 맞은 가운데, 단일 샐러드 전문점(스위트그린)과 달리 곡물 및 단백질 다변화 메뉴를 갖춘 <span class=\"text-cyan-300 font-semibold\">카바(CAVA)</span>의 매출 탄력성을 비교 분석함. <span class=\"text-amber-300 font-bold\">공급망 안전성과 메뉴 다변화</span>가 외식업 유통의 핵심 경쟁력임을 증명함.",
      "key_claims": [
        "양상추 기생충 노이즈로 샐러드 업계 리콜 공포 및 수급 불확실성 증대.",
        "지중해식 패스트 캐주얼 카바(CAVA)의 메뉴 다변화 및 공급망 관리 우위로 실적 호조."
      ],
      "data_points": [
        "미국 패스트 캐주얼 샐러드 한 끼 평균 가격: 12달러~18달러선 형성"
      ],
      "signal": "neutral",
      "signal_reason": "외식업계 식품 안전 노이즈 속 수혜 기업(CAVA)과 피해 기업 간 실적 양극화.",
      "key_companies": ["카바(CAVA)", "스위트그린(SG)", "월마트(WMT)"],
      "insight": "식품 유통업에서 단일 재료 의존도가 높은 기업은 공급망 사고 시 치명적이나, 메뉴 다각화 구조를 갖춘 기업은 위기를 기회로 전환함.",
      "action_point": "미국 헬시 패스트 캐주얼 기업 CAVA의 실적 및 식품 안전 공급망 모니터링."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["etc"],
      "tags": ["카바", "CAVA", "스위트그린", "샐러드리콜", "패스트캐주얼"]
    }
  },
  {
    "video": {
      "id": "_-YwmXSAcQU",
      "title": "\"조정은 끝\" 삼성전자가 50만원을 가려면 넘어야할 고개ㅣ차영주 와이즈경제연구소 소장 [집중 오늘의 주식]",
      "published": "2026-08-12T11:30:03+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=_-YwmXSAcQU",
      "thumbnail": "https://img.youtube.com/vi/_-YwmXSAcQU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">삼성전자(005930)</span>의 단기 조정을 완료하고 장기 목표가 달성을 위해 넘어야 할 핵심 과제로 <span class=\"text-cyan-300 font-semibold\">HBM3E/HBM4 품질 승인</span>과 파운드리 수율 개선을 꼽음. D램 판가 상승에 따른 우수한 실적 기반이 갖춰진 만큼 <span class=\"text-amber-300 font-bold\">상방 모멘텀 재개</span> 가능성을 높게 평가함.",
      "key_claims": [
        "삼성전자 단기 조정 마감 및 HBM 품질 퀄테스트 통과가 주가 대폭 재평가의 열쇠.",
        "범용 D램 판가 상승과 파운드리 수율 개선에 따른 체질 개선 전망."
      ],
      "data_points": [],
      "signal": "bullish",
      "signal_reason": "조정 마감 신호와 HBM 승인 기대감에 따른 삼성전자 장기 상승 턴어라운드.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "삼성전자가 HBM4 규격 통과 및 파운드리 턴키 수주를 입증하면 시가총액의 거대한 주가 레벨업이 성사됨.",
      "action_point": "삼성전자 저점 분할 매수 및 엔비디아 퀄테스트 관련 공시 확인."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["삼성전자", "HBM3E퀄테스트", "차영주", "반도체턴어라운드", "파운드리수율"]
    }
  },
  {
    "video": {
      "id": "_JtgR40S2LU",
      "title": "물가지표 앞둔 경계감... 미국증시 이틀째 하락 | 데일리 라이브 | 2026.8.12(수)",
      "published": "2026-08-12T11:18:09+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=_JtgR40S2LU",
      "thumbnail": "https://img.youtube.com/vi/_JtgR40S2LU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "7월 미국 CPI 발표를 앞둔 시장의 경계감으로 뉴욕증시가 이틀 연속 약세를 나타냄. 인플레이션 지표 확인 전까지 관망세가 이어진 가운데 <span class=\"text-cyan-300 font-semibold\">핵심 반도체 밸류체인</span> 및 네오클라우드 수혜주의 저가 매수 타이밍 탐색이 이뤄지는 <span class=\"text-amber-300 font-bold\">숨고르기 장세</span>를 분석함.",
      "key_claims": [
        "CPI 경계감으로 지수 단기 관망세 형성.",
        "인프라 호실적이 보증된 테크 대장주 위주의 저점 지지력 확인."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "거시 물가 발표 전 관망 심리로 이틀 연속 지수 소폭 내림세.",
      "key_companies": ["미래에셋증권"],
      "insight": "지표 발표 전의 이틀 연속 약세는 통상 불확실성 해소 후 반등 랠리를 준비하는 관망 국면임.",
      "action_point": "CPI 발표 후 증시 방향성에 맞춘 반도체 및 빅테크 분할 매수 대응."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["미국증시하락", "CPI경계감", "미래에셋데일리", "관망세", "증시전망"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_10)
    print(f"Processed batch 10: {n} items saved.")
