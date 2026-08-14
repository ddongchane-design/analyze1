import json
from save_batch_helper import save_analyses

batch6_results = [
  {
    "video": {
      "id": "nQ3LdKR2JzM",
      "title": "해맥 “지금 금리 올려야”ㅣ10년물 낙찰금리 2007년 이후 최고ㅣ장기금리 왜 안 내려가나ㅣ일본 정부 9월 BOJ 인상 지지ㅣ앤트로픽, 데카르트 AI 인수 논의ㅣ홍혜진의 뉴욕브리핑",
      "published": "2026-08-13T14:42:26+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=nQ3LdKR2JzM",
      "thumbnail": "https://img.youtube.com/vi/nQ3LdKR2JzM/hqdefault.jpg"
    },
    "analysis": {
      "summary": "7월 미국 PPI가 전월 대비 보합(0.0%, 예상치 0.2% 하회)으로 완화되며 인플레이션 우려가 경감되었으나, 햄핵(Hammack) 클리블랜드 연은 총재의 추가 금리 인상 매파 발언과 미 10년물 국채 낙찰금리의 2007년 이후 최고치 기록 등 장기금리 고공행진이 증시를 압박함. 일본 정부가 물가 안정을 위해 <span class=\"text-rose-400 font-medium\">9월 BOJ 금리 인상을 용인</span>하기로 했다는 단독 보도로 엔캐리 트레이드 청산 위험이 재부각되었으며, <span class=\"text-cyan-300 font-semibold\">앤트로픽</span>은 AI 훈련 비용 절감을 위해 이스라엘 <span class=\"text-cyan-300 font-semibold\">디카트 AI(60억 달러)</span> 인수를 추진 중임.",
      "key_claims": [
        "미국 PPI 완화로 9월 FOMC 금리 동결/인하 기대가 커졌으나 장기 국채 금리 상승세가 지속되어 매크로 부담으로 작용함.",
        "일본 정부의 9월 BOJ 금리 인상 지지 선회는 엔화 강세를 유발해 글로벌 엔캐리 자금 청산 리스크를 재점화할 수 있음.",
        "앤트로픽의 디카트 AI 인수는 AI 모델 훈련 단가를 낮춰 IPO 시 투자자들에게 수익성 개선 역량을 입증하기 위한 전략임."
      ],
      "data_points": [
        "미국 7월 PPI: 전월 대비 0.0% 보합 (예상치 +0.2% 하회), 전년 대비 +4.7% (전월 +5.5%에서 급락).",
        "미국 10년물 국채 낙찰금리: 2007년 이후 최고 수준 기록.",
        "일본은행(BOJ) 9월 금리 인상 시장 확률: 74%로 상승.",
        "앤트로픽의 디카트 AI 인수 논의 규모: 60억 달러."
      ],
      "signal": "neutral",
      "signal_reason": "PPI 완화 호재와 장기금리 상승 및 일본 9월 금리인상(엔캐리 청산) 매크로 불확실성이 팽팽히 맞서는 중립 국면.",
      "key_companies": [
        "앤트로픽",
        "델(DELL)",
        "시스코(CSCO)",
        "X에너지(X-energy)"
      ],
      "insight": "단기 물가 지표 안정에도 불구하고 미·일 장기 국채 금리의 구조적 상승과 통화 긴축 기조는 자산 시장의 변동성을 지속시키는 핵심 요인임.",
      "action_point": "8월 26일 PCE 물가 지표와 9월 BOJ 회의를 앞두고 외환 및 채권 금리 변동성에 대비한 리스크 관리가 필요함."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": [
        "stock",
        "tech"
      ],
      "tags": [
        "미국PPI",
        "장기국채금리",
        "BOJ금리인상",
        "엔캐리청산",
        "앤트로픽",
        "디카트AI",
        "월가월부"
      ]
    }
  },
  {
    "video": {
      "id": "ouT-f05lIG4",
      "title": "공포 끝난 코스피, 삼전·닉스·삼성전기 승자는 누구?ㅣ명민준, 박가영, 유영화 [주린이 구조대]",
      "published": "2026-08-13T13:00:03+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=ouT-f05lIG4",
      "thumbnail": "https://img.youtube.com/vi/ouT-f05lIG4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "7월 말 패닉 셀링으로 98까지 치솟았던 코스피 변동성(VKOSPI)이 55선으로 급락하며 시장 공포가 진정됨. 외국인들이 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>에 집중했던 숏(공매도) 포지션을 대거 환매수(숏커버링)하고, <span class=\"text-cyan-300 font-semibold\">삼성전자</span>와 <span class=\"text-cyan-300 font-semibold\">삼성전기(009150)</span>의 롱 포지션을 늘리면서 코스피 6,800선이 강하게 안착함. 과도한 레버리지 청산 이후 펀더멘털 기반의 주가 정상화 국면에 진입함.",
      "key_claims": [
        "코스피 변동성 지수 급락으로 외국인의 헷지성 숏 매도가 중단되고 대규모 숏커버링 매수가 유입됨.",
        "SK하이닉스는 밸류에이션 바닥 확인 후 숏커버링이 주가를 견인 중이며, 삼성전자와 삼성전기는 추세 반등을 주도함."
      ],
      "data_points": [
        "코스피 변동성 지수: 7월 말 피크 98 수준에서 최근 55로 급락 (정상 범위 15~20).",
        "SK하이닉스 종가: 159만 원대 (+6% 반등), 삼성전자 26만 원대 회복."
      ],
      "signal": "bullish",
      "signal_reason": "시장 변동성 완화와 외국인의 SK하이닉스 숏 청산 및 대형 IT주 강력한 바스켓 매수 전환.",
      "key_companies": [
        "SK하이닉스(000660)",
        "삼성전자(005930)",
        "삼성전기(009150)"
      ],
      "insight": "변동성 지표의 안정화는 기관과 외국인이 한국 대형 테크주에 대해 비중 확대(Overweight)를 집행할 수 있는 시스템적 환경을 조성함.",
      "action_point": "패닉 구간에서 벗어난 SK하이닉스 및 삼성전자, AI 기판/MLCC 수혜가 큰 삼성전기를 조정 시마다 분할 매수할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "tech"
      ],
      "tags": [
        "코스피안착",
        "SK하이닉스숏커버링",
        "삼성전자",
        "삼성전기",
        "변동성지수",
        "주린이구조대"
      ]
    }
  },
  {
    "video": {
      "id": "t_gfn1YqOhs",
      "title": "반도체 다시 올라갈 수 있을까? 환율은 왜 오르고, 코스피는 왜 왜 오를까? | 권혁, 이진우, 염승환, 김학주 [아침N아침]",
      "published": "2026-08-13T02:41:36+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=t_gfn1YqOhs",
      "thumbnail": "https://img.youtube.com/vi/t_gfn1YqOhs/hqdefault.jpg"
    },
    "analysis": {
      "summary": "빅테크 실적 발표를 통해 AI 데이터센터 투자(CapEx)의 강력한 지속성이 재확인되면서 반도체 고점론이 불식됨. 원화 약세와 달러 강세 환경에서도 글로벌 자금이 한국의 <span class=\"text-cyan-300 font-semibold\">HBM</span> 및 <span class=\"text-cyan-300 font-semibold\">메모리 반도체</span> 밸류체인을 집중 매수하는 구조적 원인을 점검함. AI 병목을 해결하는 차세대 네트워킹 및 고대역폭 메모리 기업들의 실적 우상향 추세를 재확인함.",
      "key_claims": [
        "빅테크들의 AI 인프라 투자는 축소가 아닌 가속화 단계에 있으며, 반도체 고점론은 기우에 불과함.",
        "환율 상승 국면에서도 한국 반도체 기업들의 이익 창출력과 글로벌 독점력이 외국인 자금 유입을 강력히 견인함."
      ],
      "data_points": [
        "글로벌 빅테크 CapEx 가이던스: AI 인프라 및 데이터센터 중심 두 자릿수 증가세 유지."
      ],
      "signal": "bullish",
      "signal_reason": "AI CapEx 확장 사이클 유지 및 한국 메모리 반도체 기업들의 견고한 실적 모멘텀.",
      "key_companies": [
        "삼성전자(005930)",
        "SK하이닉스(000660)"
      ],
      "insight": "AI 인프라 병목을 극복하려는 전 세계 테크 기업들의 필수 하드웨어 공급처로서 한국 반도체 산업의 위상은 더욱 공고해지고 있음.",
      "action_point": "반도체 투톱 및 HBM 핵심 장비/소재주를 중심으로 장기 보유 전략을 지속할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "tech",
        "economy"
      ],
      "tags": [
        "반도체반등",
        "AI인프라투자",
        "HBM",
        "외국인수급",
        "염승환",
        "김학주",
        "아침N아침"
      ]
    }
  },
  {
    "video": {
      "id": "ts7O43Bxzz8",
      "title": "미국 통화 완화 움직임 속 진짜 달러 유동성 풀리나 트럼프 '큰 그림' 나온다 | 권혁, 김동환, 하나 김재희 이사 [크립토 PLUS]",
      "published": "2026-08-13T03:25:42+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=ts7O43Bxzz8",
      "thumbnail": "https://img.youtube.com/vi/ts7O43Bxzz8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국의 금리 인하 사이클 진입 및 연준의 유동성 공급 완화 기조와 함께, 트럼프 행정부의 친(親) 비트코인 정책 구상이 글로벌 가상자산 시장의 차세대 상승 동력으로 분석됨. <span class=\"text-cyan-300 font-semibold\">비트코인 전략비축자산 편입</span> 논의와 <span class=\"text-cyan-300 font-semibold\">스테이블코인 법안</span> 통과 기대감이 맞물려, 달러 패권 유지와 가상자산 생태계 성장이 결합된 '트럼프노믹스 2.0'의 거시적 파급력을 조명함.",
      "key_claims": [
        "연준의 금리 인하와 글로벌 유동성 재확대는 가상자산 시장의 중장기 상승장을 뒷받침하는 핵심 매크로 배경임.",
        "트럼프의 비트코인 국가 전략자산화 정책은 전 세계 중앙은행과 기관들의 비트코인 편입을 촉발할 수 있는 메가 이벤트임."
      ],
      "data_points": [
        "미국 연준 9월 기준금리 인하 유력.",
        "미국 스테이블코인 시가총액 및 국채 담보 규모 지속 증가."
      ],
      "signal": "bullish",
      "signal_reason": "글로벌 달러 유동성 완화와 미국 정치권의 가상자산 친화적 정책 전환 기대.",
      "key_companies": [
        "비트코인(BTC)"
      ],
      "insight": "스테이블코인이 미국 국채의 핵심 수요처로 자리 잡으면서, 미국 정부의 가상자산 육성은 달러 패권 연장을 위한 국가적 전략 자산으로 재정의되고 있음.",
      "action_point": "금리 인하 및 유동성 공급 사이클에 발맞추어 비트코인 및 핵심 스테이블코인/RWA 인프라에 대한 비중을 확대할 것."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": [
        "economy"
      ],
      "tags": [
        "비트코인",
        "달러유동성",
        "통화완화",
        "트럼프정책",
        "전략비축자산",
        "크립토플러스"
      ]
    }
  },
  {
    "video": {
      "id": "uYvr7czeSBE",
      "title": "[26.08.13 마감 증시 풀버전] 대만보다 더 센 외국인 폭풍 매수!...하락장 탈출, 다시 달릴 수 있을까?",
      "published": "2026-08-13T11:03:58+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=uYvr7czeSBE",
      "thumbnail": "https://img.youtube.com/vi/uYvr7czeSBE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "외국인 투자자들이 대만 증시(TSMC)보다 한국 증시(<span class=\"text-cyan-300 font-semibold\">삼성전자</span>, <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>)를 더 강하게 순매수(코스피 2.4조 원)하며 아시아 테크 랠리를 견인함. 7월 조정장에서 과도하게 벌어졌던 한국 반도체 주가의 저평가 갭을 메우는 강력한 밸류에이션 리레이팅이 진행 중임.",
      "key_claims": [
        "외국인의 한국 증시 순매수 강도가 대만을 추월한 것은 HBM 공급망에서 한국 투톱의 대체 불가능한 수익성을 재평가했기 때문임.",
        "하락장 공포에서 완전히 벗어나 하반기 실적 랠리로 진입하는 강력한 변곡점 형성."
      ],
      "data_points": [
        "코스피 외국인 순매수 규모: 2조 4,270억 원으로 아시아 주요국 대비 1위 기록."
      ],
      "signal": "bullish",
      "signal_reason": "외국인의 아시아 테크 바스켓 매수에서 한국 반도체에 대한 압도적 선호 확인.",
      "key_companies": [
        "삼성전자(005930)",
        "SK하이닉스(000660)",
        "TSMC(TSM)"
      ],
      "insight": "AI 가속기 시장의 폭발적 성장에서 고대역폭 메모리를 독점 공급하는 한국 반도체 생태계의 전략적 가치가 글로벌 자본에 의해 재확인됨.",
      "action_point": "한국 반도체 대표주 및 소부장 밸류체인에 대한 적극적인 매수 및 보유 전략을 견지할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "tech"
      ],
      "tags": [
        "마감증시",
        "외국인폭풍매수",
        "대만비교",
        "삼성전자",
        "SK하이닉스",
        "삼프로TV"
      ]
    }
  },
  {
    "video": {
      "id": "xX8HLws6gMQ",
      "title": "[안효찬] 불황 온 미국? 고용과 함께 봐야 할 \"진짜 지표\"",
      "published": "2026-08-13T14:57:01+00:00",
      "channel_name": "안효찬",
      "url": "https://www.youtube.com/watch?v=xX8HLws6gMQ",
      "thumbnail": "https://img.youtube.com/vi/xX8HLws6gMQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 경기 침체(R의 공포) 논란 속에서 헤드라인 실업률 외에 반드시 함께 확인해야 할 실질 고용 지표인 <span class=\"text-cyan-300 font-semibold\">신규 실업수당 청구건수</span>, <span class=\"text-cyan-300 font-semibold\">주간 평균 근로시간</span>, 및 기업 채용 공고(JOLTS) 데이터를 분석함. 최근 실업률 상승은 대규모 해고(Layoff)가 원인이 아니라 이민자 유입 등에 따른 노동 공급 증가가 주도한 것으로, 실질 해고 건수는 역사적으로 여전히 낮은 수준을 유지해 급격한 침체 가능성은 낮다고 진단함.",
      "key_claims": [
        "미국의 실업률 상승은 급격한 경기 침체에 의한 해고 증가가 아니라 노동 공급 증가에 따른 완만한 정상화 과정임.",
        "주간 신규 실업수당 청구건수가 20만 건대 초반으로 안정적인 한 시스템적 경기 불황 우려는 과도함."
      ],
      "data_points": [
        "신규 실업수당 청구건수: 20만 9천 건으로 안정적 레벨 유지.",
        "미국 기업들의 인력 해고율: 역사적 저점 부근 유지."
      ],
      "signal": "neutral",
      "signal_reason": "경기 침체 우려는 과도하나 노동 시장의 완만한 둔화로 연준의 금리 인하 명분 강화.",
      "key_companies": [],
      "insight": "노동 시장의 점진적 둔화는 인플레이션을 억제하면서도 급격한 경기 침체를 피하는 이상적인 '골디락스' 연착륙 환경을 조성하고 있음.",
      "action_point": "침체 공포에 따른 과도한 위험자산 투매를 경계하고, 금리 인하 수혜가 기대되는 성장주와 우량 배당주 중심의 포트폴리오를 유지할 것."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": [
        "stock"
      ],
      "tags": [
        "미국고용지표",
        "경기침체논란",
        "실업수당청구",
        "골디락스",
        "연착륙",
        "안효찬"
      ]
    }
  }
]

if __name__ == "__main__":
    save_analyses(batch6_results)
