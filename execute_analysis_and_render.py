import json
import os
import sys
from pathlib import Path

# Set stdout to UTF-8 to avoid encoding errors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# 12 analyzed video data dictionary
analyzed_videos = {
  "y9UUV3vWXOw": {
    "primary": "tech",
    "data": {
      "video": {
        "id": "y9UUV3vWXOw",
        "title": "에이전트가 국가 GDP를 결정할 것",
        "published": "2026-06-11T11:00:01+00:00",
        "channel_name": "Softdragon SOD",
        "url": "https://www.youtube.com/watch?v=y9UUV3vWXOw",
        "thumbnail": "https://img.youtube.com/vi/y9UUV3vWXOw/hqdefault.jpg"
      },
      "analysis": {
        "summary": "<span class=\"text-amber-300 font-bold\">AI 에이전트</span>가 토큰(Tokens)을 폭발적으로 소모(태우는)하는 구조이기 때문에, <span class=\"text-cyan-300 font-semibold\">엔비디아</span>가 이를 강력하게 추진하고 있음. AI 기업들은 더 많은 토큰을 생성하고 <span class=\"text-cyan-300 font-semibold\">AI 팩토리</span>를 짓기를 원하며, 이제 AI는 단순 비용이 아닌 이익 발전기(Profit Generator)로 전환되고 있음.",
        "key_claims": [
          "젠슨 황이 <span class=\"text-amber-300 font-bold\">AI 에이전트</span>를 강력하게 추진하는 이유는 에이전트가 막대한 양의 토큰을 지속적으로 소비하는 구조이기 때문임.",
          "AI 기업들은 토큰 생성량을 늘리고 <span class=\"text-cyan-300 font-semibold\">AI 팩토리</span>를 더 많이 건설하려는 강력한 니즈를 가지고 있음.",
          "AI는 단순한 연구/비용 단계를 넘어 본격적인 이익 창출원(Profit Generator)으로 진화함."
        ],
        "data_points": [],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "AI 에이전트 도입 본격화로 토큰 소모량이 급증함에 따라 AI 인프라(AI 팩토리) 및 하드웨어(반도체/GPU) 수요가 구조적으로 확장될 것이며, AI 비즈니스가 수익 모델로 안착했음을 시사함.",
        "key_companies": ["엔비디아(NVDA)"],
        "insight": "AI 에이전트는 사용자가 프롬프트를 입력할 때뿐만 아니라, 스스로 자율적인 루프를 돌며 판단하고 행동하기 때문에 기존 챗봇보다 기하급수적으로 많은 토큰을 소모함. 이는 <span class=\"text-cyan-300 font-semibold\">엔비디아</span>와 같은 하드웨어 칩 공급사 및 데이터센터 밸류체인에 지속적이고 반복적인 인프라 매출(Recurring demand)을 보장하는 비즈니스 모델로 연결됨.",
        "action_point": "AI 에이전트 서비스 대중화와 AI 팩토리 건설 붐의 직접적인 수혜를 입는 <span class=\"text-cyan-300 font-semibold\">엔비디아</span>와 AI 인프라 관련 밸류체인에 지속적으로 관심을 가질 필요가 있음."
      },
      "classification": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["AI에이전트", "토큰소모", "AI팩토리", "젠슨황"]
      }
    }
  },
  "YO4-HdQaPvA": {
    "primary": "space",
    "data": {
      "video": {
        "id": "YO4-HdQaPvA",
        "title": "실리콘밸리 전문가 \"스페이스X, 첫 번째 조정 후에 사겠다” #shorts",
        "published": "2026-06-11T10:09:56+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=YO4-HdQaPvA",
        "thumbnail": "https://img.youtube.com/vi/YO4-HdQaPvA/hqdefault.jpg"
      },
      "analysis": {
        "summary": "<span class=\"text-cyan-300 font-semibold\">스페이스X</span>의 역대급 IPO 상장을 앞두고 자금 유입 기대감과 유통 물량 부족으로 인한 상장 초기 오버슈팅 우려가 공존함. 실리콘밸리 전문가는 상장 초기 급등했다가 매물 출회로 하락하는 첫 2주간의 조정기를 기다린 후 진입하는 전략이 현명하다고 권고함.",
        "key_claims": [
          "스페이스X 상장은 1.8조 달러 규모로 테슬라의 과거 상장 수준을 능가하며, 일론 머스크가 지분의 82% 이상을 쥐고 통제권을 행사하게 됨.",
          "유통 주식 비율(부력)이 낮아 상장 직후 매수세 쏠림으로 폭등 가능성이 있으나, 결국 락업 해제 및 초기 기관 차익 실현으로 첫 2주 내 조정이 올 것임.",
          "개인 투자자들의 관심이 폭발적이며 주식 거래 대금의 30% 수준의 변동을 소매 부문이 주도할 수 있음."
        ],
        "data_points": [
          "스페이스X IPO 평가 가치: 약 1.8조 달러 수준",
          "일론 머스크의 스페이스X 지분율: 약 82% 수준"
        ],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "초대형 상장 흥행으로 장기적 성장성은 매우 긍정적이나, 극단적으로 적은 유통 물량과 레버리지 상품 쏠림으로 상장 초기 주가 변동성이 극대화될 것이기 때문임.",
        "key_companies": ["스페이스X", "테슬라(TSLA)"],
        "insight": "일론 머스크에게 스페이스X는 테슬라보다 훨씬 더 수익성 높은 보상 체계와 통제권을 제공하는 핵심 제국임. 소수의 유통 물량으로 주가를 띄운 뒤 데이터센터(XAI) 및 지상 인프라 자금 수혈을 꾀하는 구조를 이해해야 함.",
        "action_point": "상장 첫날의 광풍에 추격 매수하기보다는, 페이스북 사례처럼 상장 후 첫 1~2주간 매물이 출회되어 주가가 안정을 찾을 때 진입하는 분할 매수 타이밍을 권장함."
      },
      "classification": {
        "primary_topic": "space",
        "secondary_topics": ["stock", "tech"],
        "tags": ["SpaceX", "IPO", "일론머스크", "변동성"]
      }
    }
  },
  "fvxFU4YjvdE": {
    "primary": "etc",
    "data": {
      "video": {
        "id": "fvxFU4YjvdE",
        "title": "또 다시 등장한 깔따구, 여름만 되면 한강변을 뒤덮는 이유는?!",
        "published": "2026-06-11T11:00:12+00:00",
        "channel_name": "안될과학 Unrealscience",
        "url": "https://www.youtube.com/watch?v=fvxFU4YjvdE",
        "thumbnail": "https://img.youtube.com/vi/fvxFU4YjvdE/hqdefault.jpg"
      },
      "analysis": {
        "summary": "한강변을 비롯한 도심지에 대량 출몰하는 깔따구와 동양하루사리 등 날파리류의 생태적 특성 및 대발생 원인을 설명함. 이들 곤충은 유충 시기 물속에서 대부분의 수명을 보낸 뒤, 성충이 되면 짝짓기만을 목적으로 3일 내외(길면 수 주)의 짧은 기간 활동하며, 밤에 빛을 활용해 등 방향을 잡고 비행하다 인공 조명에 갇혀 도심에 밀집하게 됨.",
        "key_claims": [
          "깔따구는 극한 환경(남극, 북극, 고산지대, 무산소 하천)에서도 생존하는 강력한 적응력을 지닌 원시적 파리류임.",
          "인공 불빛에 곤충들이 몰려드는 것은 불빛을 좋아하는 것이 아니라, 등 위에 달/별빛을 두고 수평을 맞춰 내비게이션 비행을 하던 습성 때문에 인공 광원 주변에 갇히는 현상에 가까움.",
          "동양하루사리는 국내 토종 생물이어서 무차별 방제가 어려우며, 인공 유인 광선 배 등을 활용해 강가에 가두어 자연 사멸을 유도하는 방제 방식이 활용됨."
        ],
        "data_points": [
          "깔따구 및 하루사리 성충 수명: 평균 3일 내외 (짝짓기 안 시킬 경우 최대 4주)",
          "러브버그 성충 수명: 수컷 짝짓기 직후 즉사, 암컷 기준 1~2주",
          "어리맨목파리류 성충 수명: 약 40분 (세계 최단 수준)"
        ],
        "signal": "na",
        "signal_confidence": "high",
        "signal_reason": "투자와 무관한 순수 자연/생물 과학 다큐멘터리 영상임.",
        "key_companies": [],
        "insight": "모기나 파리류와 달리 성충 단계에서 먹이 활동을 거의 하지 않고 애벌레 시기 비축한 에너지만으로 짝짓기를 완수하는 생태 구조는 곤충 진화의 성공 비결(역할 분담) 중 하나이나, 도심지의 인공 조명 및 온난화에 따른 하천 환경 변화와 맞물려 시민 불편을 초래하는 대발생 이슈를 낳고 있음.",
        "action_point": "해당 이슈는 주식/투자 관점과는 거리가 먼 환경/시사 가십성 정보이므로 자산 배분 전략 및 투자 판단 대상에서 제외함."
      },
      "classification": {
        "primary_topic": "etc",
        "secondary_topics": [],
        "tags": ["깔따구", "동양하루사리", "인공광원", "생태분석"]
      }
    }
  },
  "vBwAM-Er29I": {
    "primary": "robot",
    "data": {
      "video": {
        "id": "vBwAM-Er29I",
        "title": "정부가 로봇을 사들이기 시작했다 왜?",
        "published": "2026-06-11T10:17:12+00:00",
        "channel_name": "엔지니어TV",
        "url": "https://www.youtube.com/watch?v=vBwAM-Er29I",
        "thumbnail": "https://img.youtube.com/vi/vBwAM-Er29I/hqdefault.jpg"
      },
      "analysis": {
        "summary": "휴머노이드 로봇 산업의 본격적 개화를 위해서는 민간 시장에만 맡길 것이 아니라 정부 주도의 초기 수요 창출(보조금 및 공공 구매)과 기술 규격/보험 등 제도적 인프라 구축이 필수적임. 중국은 로봇 주민번호(29자리 ID 코드) 부여 및 데이터 수집 생태계를 선도하고 있고, 일본은 2030년까지 30만 대 보급 정책을 펴는 등 로봇 산업은 이제 단순 제조 제품이 아닌 국가 안보 및 생산성 경쟁력을 좌우하는 국가 인프라 주권 사업으로 진화하고 있음.",
        "key_claims": [
          "미국 제조 공정의 88%는 아직 로봇이 없는 상태이며, 이 88%의 미자동화 영역을 범용 휴머노이드가 대체하는 것이 대규모 시장 기회임.",
          "유니트리 로보틱스가 52%의 이익 급감을 겪었듯, 현재 초기 로봇 하드웨어 제조사는 높은 R&D 비용으로 독자 수익 창출이 어려워 정부의 대량 구매 정책이 절실함.",
          "로봇 협동조합 소유 모델(노동자·시민이 로봇을 소유하고 기업에 임대)이나 자율동작 데이터 판매 비즈니스(미 Shift, 중국 징동의 주부 동영상 데이터 수집) 등 새로운 로봇 생산성 공유 모델과 피지컬 AI 데이터 수집 산업이 태동하고 있음."
        ],
        "data_points": [
          "글로벌 휴머노이드 대수: 현재 약 6만 대 수준 → 2040년까지 100억 대 규모 전망",
          "일본의 로봇 정책 목표: 2030년까지 30만 대 도입 (연간 6만 대 보급)",
          "미국 제조 공정 현황: 88%가 로봇을 미소유",
          "중국 휴머노이드 주민번호 부여 건수: 28,000개 이상 부여 완료 (29자리 코드 식별체계)",
          "현대자동차의 보스턴 다이내믹스 아틀라스 구매 계획: 25,000대 예정"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "로봇 산업이 개별 스마트 디바이스 수준을 넘어 전기차(EV) 보조금 폭발기처럼 주요국(중국, 일본 등) 정부의 대규모 구매 정책 및 제도 정비 단계로 격상되고 있으며, 현대차의 2.5만 대 아틀라스 실배치 예정 등 대기업 구매가 가시화되며 시장 성장성이 보장되고 있음.",
        "key_companies": ["유니트리 로보틱스", "현대자동차", "보스턴 다이내믹스", "징동닷컴(JD.com)"],
        "insight": "전기차 시장을 기술력보다 정부 보조금과 초기 구매 정책이 폭발시켰듯이, 휴머노이드 시장 역시 정부의 공공 조달과 안보/국방용 대량 구매가 마중물이 될 것임. 특히 하드웨어 제조보다 인간 행동 및 주거 생활 영상을 촬영해 판매하는 '피지컬 AI 데이터 비즈니스'가 로봇 산업의 알짜 고부가가치 영역으로 안착하고 있음.",
        "action_point": "정부 보조금 수혜 및 대기업(현대차 등)의 조 단위 로봇 도입 물량이 가시화되는 시점에 주목하여, 보스턴 다이내믹스 실물 배치의 핵심 수혜주인 현대차 그룹과 로봇의 핵심 구동 부품사(액추에이터/감속기)에 장기 투자하는 전략을 추천함."
      },
      "classification": {
        "primary_topic": "robot",
        "secondary_topics": ["stock", "tech"],
        "tags": ["정부로봇조달", "로봇주민번호", "피지컬AI데이터", "유니트리"]
      }
    }
  },
  "jaDHU37byXo": {
    "primary": "etc",
    "data": {
      "video": {
        "id": "jaDHU37byXo",
        "title": "이 남자한테 투자해도 될까? | 공강 | 블라인드소개팅",
        "published": "2026-06-11T09:00:06+00:00",
        "channel_name": "Smart Money by MiraeAsset ",
        "url": "https://www.youtube.com/watch?v=jaDHU37byXo",
        "thumbnail": "https://img.youtube.com/vi/jaDHU37byXo/hqdefault.jpg"
      },
      "analysis": {
        "summary": "미래에셋 스마트머니 채널의 예능 콘텐츠인 '블라인드 소개팅(공강)' 편으로, 외모나 조건을 숨긴 채 대화와 성격, 그리고 일부 투자 성향(예금형 대 승부사형, 단기 대 장기 보유 등)에 대한 가치관을 공유하며 매칭을 진행하는 남녀 출연진의 소개팅 흐름을 다룸.",
        "key_claims": [
          "투자 성향이나 방식이 다른 경우에도 대화와 상호 존중을 통해 조율하는 성숙한 연인 관계 구축이 중요함.",
          "단기 시세 확인보다 미래를 위해 장기 투자하며 연인을 배려하겠다는 안정 지향적 가치관이 긍정적 어필 요소로 작용함."
        ],
        "data_points": [],
        "signal": "na",
        "signal_confidence": "high",
        "signal_reason": "투자와 직접 연관되지 않은 일반 예능/시사 콘텐츠임.",
        "key_companies": [],
        "insight": "해당 콘텐츠는 주식 시장의 분석보다는 일반 대중의 투자 성향(예금형 vs 승부사형 등)을 일상적인 라이프스타일 및 관계관과 결합하여 친근하게 풀어낸 예능형 마케팅 콘텐츠에 해당함.",
        "action_point": "본 영상은 투자 가이드나 시장 분석 정보가 존재하지 않는 흥미 위주의 콘텐츠이므로 투자 의사 결정 및 주식 포트폴리오 운용 대상에서 제외함."
      },
      "classification": {
        "primary_topic": "etc",
        "secondary_topics": [],
        "tags": ["블라인드소개팅", "예능마케팅", "투자성향", "미래에셋"]
      }
    }
  },
  "wnBreKg7_54": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "wnBreKg7_54",
        "title": "[홍장원의 불앤베어] 트럼프 \"이란 최고지도자, 합의에 동의\"",
        "published": "2026-06-11T22:15:36+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=wnBreKg7_54",
        "thumbnail": "https://img.youtube.com/vi/wnBreKg7_54/hqdefault.jpg"
      },
      "analysis": {
        "summary": "트럼프 대통령이 이란에 대한 공습 예고(극단적 긴장) 후 12시간 만에 공습 취소 및 이란 최고지도자와의 합의 승인을 발표하며 시장의 긴장을 급격히 완화시켰음. 5월 PPI는 에너지가 상승을 주도하여 예상치를 상회했으나, 에너지 물가 충격의 근원이었던 이란 리스크 해소 기대감으로 유가가 배럴당 90달러 밑으로 급락하고 나스닥을 비롯한 뉴욕 증시(특히 마이크론 12% 상승 등 반도체 주도)가 강력한 랠리를 펼침.",
        "key_claims": [
          "트럼프 대통령이 의도적으로 이란에 대한 공습 위협을 고조시켜 협상력을 극대화한 뒤 극적으로 합의 진전을 이끌어내는 협상 전술을 구사함.",
          "이란 측 외무부 대변인도 대다수 합의 문안이 파이널라이즈(확정)되었음을 인정했으나, 최종 서명 단계에서 미국의 과도한 요구 조건 추가로 아직 100% 종결되지는 않았음을 밝힘.",
          "5월 PPI 급등의 주원인은 에너지 가격(휘발유 24% 급등) 등 공급측 충격이며, 이란 합의로 호르무즈 해협 봉쇄 해제 시 유가 안정과 함께 인플레 우려도 낮아질 것임."
        ],
        "data_points": [
          "마이크론 주가 상승률: 12% 수준",
          "러셀 2000 상승률: 3% 초과, 나스닥 상승률: 2.54%, 다우지수: 1.86%, S&P 500: 1.75%",
          "5월 PPI: 전월 대비 1.1% 상승 (시장 예상치 0.7% 대폭 상회), 연간 기준 6.5% 상승(2022년 11월 이후 최고치)",
          "5월 코어 PPI: 전월 대비 0.4% 상승 (시장 예상치 0.5% 하회)",
          "유가 지표: WTI 기준 90달러 하회"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "지정학적 리스크(호르무즈 해협 봉쇄)로 인한 글로벌 유가 쇼크와 인플레이션 불안이 트럼프의 이란 타결 발표로 인해 급속히 완화되고 있어, 매크로 금리 하락 및 반도체 등 기술주 중심으로 투자 심리가 강력히 회복되고 있음. 다만 최종 서명 전 이견 조율이라는 마지막 변수가 남음.",
        "key_companies": ["마이크론(MU)", "샌디스크"],
        "insight": "트럼프의 극단적 긴장 고조 후 즉각적인 합의 발표는 전형적인 '거래의 기술' 전술로, 시장에 누적된 지루한 교착 상태의 불확실성을 일거에 해소함. 이는 매크로 압박 요소(에너지 공급발 PPI 상승)의 정점을 찍고 하향 안정화시키는 기폭제가 될 수 있음.",
        "action_point": "유가 하락과 이란 리스크 해소로 국채 금리가 안정세를 찾음에 따라, 단기 급락했던 기술주(특히 메모리 반도체 리더인 마이크론 등)의 단기 반등 모멘텀을 활용하되, 최종 합의 서명 완료 시점까지 이란/미국의 막판 조율 잡음을 확인하는 리스크 관리가 병행되어야 함."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock", "tech"],
        "tags": ["미이란협상", "유가하락", "PPI지표", "트럼프전술"]
      }
    }
  },
  "8o89tc_z7OA": {
    "primary": "space",
    "data": {
      "video": {
        "id": "8o89tc_z7OA",
        "title": "스페이스X가 97%를 꽁꽁 묶어놓고 3%만 시장에 던져준 진짜 속내가 따로 있습니다 [Z1뉴스]",
        "published": "2026-06-11T09:30:01+00:00",
        "channel_name": "이효석아카데미",
        "url": "https://www.youtube.com/watch?v=8o89tc_z7OA",
        "thumbnail": "https://img.youtube.com/vi/8o89tc_z7OA/hqdefault.jpg"
      },
      "analysis": {
        "summary": "스페이스X의 1.77조 달러 규모 IPO 상장과 이에 따른 적정 가치 및 시장 유동성 파생 영향을 분석함. 유통 물량 비중이 3%에 불과하여 초기 극단적 변동성이 예상되는 한편, 스페이스X의 밸류에이션을 결정할 핵심 변수는 단순 우주 산업이 아닌 합병된 XAI의 데이터 센터 컴퓨팅 자산 가치(구글과의 260억 달러 규모 컴퓨팅 임대 계약 등) 평가에 달려 있음.",
        "key_claims": [
          "스페이스X의 상장 가치(1.77조 달러)는 밸류에이션 전문가 다모다란 교수의 추정 가치(1.2조 달러) 대비 약 50% 고평가 상태임.",
          "스페이스X 우주/스타링크 본업의 가치는 8천억~1조 달러 수준이며, 나머지 알파는 데이터 센터 자산을 보유한 XAI 가치평가에 의해 결정됨.",
          "신규 대형 IPO(스페이스X, 오픈AI, 엔트로픽 등 약 500조 원 규모) 자금 조달을 위해 투자자들이 기존 M7 빅테크나 금, 비트코인 등 자산을 매각함에 따라 시장 전반의 일시적 유동성 압박이 발생하고 있음."
        ],
        "data_points": [
          "스페이스X IPO 기업 가치: 1.77조 달러 (약 2,600조 원)",
          "다모다란 교수 평가 가치: 1.2조 달러 (공모가 대비 50% 비쌈)",
          "공모 유통 물량 비중: 전체 주식의 3% 수준 (약 110조 원 규모)",
          "M7 및 신규 테크 기업 유상증자/IPO 대기 자금 규모: 약 500조 원 (0.3조 달러 초과)",
          "미국 MMF 잔액: 8.3조 달러",
          "XAI 매출 계약 규모: 구글 등 대상 260억 달러 (약 40조 원) 규모 컴퓨팅 임대",
          "금값 변동: 온스당 2,400달러선(대본상 4,200달러 오기 기재 부문 조율) 붕괴 및 4% 이상 하락"
        ],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "스페이스X 상장은 중장기적으로 AI/우주 시대의 강력한 촉매제이나, 유통 주식 수가 극히 적어(3%) 상장 초기 $100~$200 사이의 극심한 주가 변동성 위험이 있고, 대형 테크 기업들의 유동성 흡수(500조 원대 대기 물량)로 인해 일시적 매크로 쏠림 및 지수 변동성이 커질 수 있기 때문임.",
        "key_companies": ["스페이스X", "구글(GOOGL)", "삼성전자", "마이크론", "골드만삭스"],
        "insight": "스페이스X 상장의 진정한 투자 핵심은 '우주 여행'이 아니라, 일론 머스크가 급격히 지어 올린 XAI의 데이터 센터와 그 컴퓨팅 파워의 가치임. 구글조차 자체 데이터 센터 용량 부족으로 XAI의 연산력을 2배 가격에 임대할 만큼 AI 인프라 쇼티지가 극심함을 시사함.",
        "action_point": "상장 초기 극단적 변동성에 추격 매수하기보다, 보호예수(락업) 해제 및 오픈AI/엔트로픽 상장 등으로 유동성이 분산되어 주가가 $80~$100선 이하로 조정받는 시기를 장기 진입 기회로 노리는 전략이 유효함."
      },
      "classification": {
        "primary_topic": "space",
        "secondary_topics": ["stock", "tech"],
        "tags": ["SpaceX", "다모다란", "XAI데이터센터", "유동성"]
      }
    }
  },
  "pWLFaVgbAWQ": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "pWLFaVgbAWQ",
        "title": "[김종학의 뉴욕, 지금-6월12일] 월드컵 앞둔 트럼프..이란 공습 계획 전면 취소 | 미-이란 합의 임박?..이스라엘 뒤늦은 성명 | 오라클, 어도비, 인텔, 구글, 스페이스X",
        "published": "2026-06-11T21:20:57+00:00",
        "channel_name": "한경 글로벌마켓",
        "url": "https://www.youtube.com/watch?v=pWLFaVgbAWQ",
        "thumbnail": "https://img.youtube.com/vi/pWLFaVgbAWQ/hqdefault.jpg"
      },
      "analysis": {
        "summary": "트럼프의 이란 공습 번복으로 지정학 리스크가 대폭 완화되면서 유가가 86달러선으로 떨어지고, 10년물 국채 금리가 4.46%대로 안정되며 뉴욕 증시가 강력한 매수세와 반등을 기록함. BofA의 인텔 투자의견 매수 상향, 구글과 삼성전자의 2나노 차세대 TPU 공동 개발 소식 등이 반도체 중심의 지수 랠리를 이끌었으나, 오라클과 어도비는 증자 우려 및 실적 한계로 하락했음.",
        "key_claims": [
          "트럼프 대통령이 최고위급 협상 진전을 이유로 이란 공습 취소를 성명하면서 원유 시장의 위기가 소강 상태로 접어들고 위험 자산 선호가 복원됨.",
          "인텔은 서버 CPU 지배력 유지 및 애플·테슬라향 파운드리 실적 가시성을 바탕으로 매수 상향 평가를 받아 9%대 급등함.",
          "구글이 삼성전자와 2nm 공정 기반 차세대 TPU(아이스피크) 공동 개발에 나선 것은 TSMC의 캐파 부족 속에서 한국 파운드리 생태계의 기회가 되고 있음."
        ],
        "data_points": [
          "나스닥 지수 상승률: 2.54%, S&P 500: 1.75%, 다우존스: 1.86%",
          "WTI 유가 변동률: 4.08% 하락한 배럴당 86.36달러",
          "10년물 미국 국채 금리: 7.9bp 하락한 4.461%",
          "인텔 주가 상승률: 9% 수준 (BofA 목표가 $135 제시)",
          "마이크론 주가 상승률: 11.66%, 브로드컴: 3.62%, 엔비디아: 2.2%",
          "오라클 주가 하락률: 8.5% (자본 지출 557억 달러 발표)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "매크로 악재인 중동 지정학 불안이 해제되며 국채 금리 및 유가가 동반 폭락했고, BofA의 인텔 상향 및 구글의 삼성향 2nm TPU 등 반도체 업계의 견고한 개별 호재들이 시장 투심을 전폭 지지하고 있기 때문임.",
        "key_companies": ["인텔(INTC)", "삼성전자", "오라클", "마이크론"],
        "insight": "구글조차 인프라 부족으로 XAI 데이터센터를 고가에 임대할 만큼 연산 쇼티지가 극심한 상황에서, 빅테크의 공격적 CapEx(오라클 557억 달러 등)는 단기 자금조달 노이즈로 주가를 깎아내릴지라도 반도체 부품사에게는 명확한 미래 매출을 담보함.",
        "action_point": "유가 하락과 매크로 리스크 소멸로 반도체 소부장의 강력한 주도권 복귀가 예상되므로, 단기 수급 부담으로 조정받았던 메모리 반도체(마이크론) 및 파운드리/2nm TPU 수혜주(삼성전자, 인텔)에 대한 점진적 매집 전략을 추천함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["인텔매수상향", "삼성2나노TPU", "오라클CapEx", "유가하락"]
      }
    }
  },
  "NQ5Pnr2yC0Y": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "NQ5Pnr2yC0Y",
        "title": "트럼프 “이란 공습 계획 취소”…마이크론, 샌디스크 급반등 [월가 뉴스레터]",
        "published": "2026-06-11T22:25:05+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=NQ5Pnr2yC0Y",
        "thumbnail": "https://img.youtube.com/vi/NQ5Pnr2yC0Y/hqdefault.jpg"
      },
      "analysis": {
        "summary": "트럼프 대통령이 예고했던 이란 공습을 최종 번복하고 이란 지도부와 최종 합의 조율 단계임을 공식화하자 지정학 리스크 완화로 뉴욕 증시가 일제히 반등함. 특히 대형 IPO(스페이스X)를 둘러싼 유동성 압박 속에서 단기 차익매물로 급락했던 메모리 반도체(마이크론 11.6% 급등, 샌디스크 14% 폭등 등) 업종이 시장 상승을 주도함.",
        "key_claims": [
          "이란과 미국 간의 해상 봉쇄 해제 및 최종 서명 조율로 호르무즈 해협 위기가 외교적으로 해결될 가능성이 극도로 높아짐.",
          "오라클의 대규모 CAPEX 및 유상증자 계획에 따른 주가 하락세에도 불구하고, 인텔의 투자의견 상향(BofA) 및 반도체 장비 수요 회복 기대로 전체 반도체 섹터의 투심이 급반전됨."
        ],
        "data_points": [
          "마이크론 상승률: 11.66%",
          "샌디스크 상승률: 14%",
          "WTI 유가: 배럴당 86달러선으로 하락",
          "나스닥 지수 상승률: 2.54%"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "에너지 가격 급등발 PPI 위협이 유가 하락으로 무력화되었고, 반도체 공급 부족(LPDDR, HBM 등) 업황은 여전히 견조하므로 지정학 리스크 완화 시 주도주 중심의 강력한 상승 복귀가 지속될 가능성이 큼.",
        "key_companies": ["마이크론(MU)", "샌디스크", "오라클"],
        "insight": "단기 유동성 분산 우려(스페이스X 상장 등)와 원자재 인플레가 겹치며 조정받던 반도체 섹터가 지정학 리스크 해소 즉시 폭발적으로 반등한 것은 반도체 업황의 강력한 이익 성장 모멘텀이 증시 하방을 단단히 지지하고 있음을 보여줌.",
        "action_point": "조정 시 매수(Buy on dips) 관점에서 마이크론, 샌디스크 및 반도체 장비 밸류체인의 비중을 확대하되, 이란 합의의 공식 서명 시점까지는 분할 매수로 대응함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["마이크론급반등", "샌디스크폭등", "트럼프이란", "반도체수급"]
      }
    }
  },
  "2Dj09apoVMs": {
    "primary": "space",
    "data": {
      "video": {
        "id": "2Dj09apoVMs",
        "title": "CNN \"미국-이란 협상 여전히 진행중\"ㅣ스페이스X 첫 커버리지, 목표가 165달러ㅣ오픈AI, 경쟁력 확보 위해 가격인하 검토 ㅣ홍키자의 매일뉴욕",
        "published": "2026-06-11T14:34:55+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=2Dj09apoVMs",
        "thumbnail": "https://img.youtube.com/vi/2Dj09apoVMs/hqdefault.jpg"
      },
      "analysis": {
        "summary": "스페이스X의 본격적인 나스닥 상장을 앞두고 투자은행 제프리스가 첫 기업 분석을 통해 목표가 165달러를 제시하였음. 또한 미-이란 외교적 대면 협상이 대기업 동결자금 해제 등을 골자로 진행 중이며, 오픈AI는 가격 경쟁력 및 에이전트 서비스 대중화를 위해 자사 API 가격 인하를 검토하고 있는 매크로/테크 뉴스를 요약함.",
        "key_claims": [
          "제프리스는 스페이스X의 발사 및 스타링크 매출 고성장세를 바탕으로 상장 목표주가를 $165(기업가치 약 2.2조 달러에 상응)로 제시함.",
          "오픈AI가 에이전트 기술 보급 및 경쟁사 추격을 위해 토큰 가격 인하 카드를 꺼내 들었으며, 이는 인프라(엔비디아)의 토큰 소모 증가로 귀결될 것임.",
          "미국과 이란 간의 카타르 중재 협상이 여전히 물밑에서 진행 중이며 최종 단계 도달을 위한 자금 해제 방안 등이 다각도로 논의되고 있음."
        ],
        "data_points": [
          "스페이스X 제프리스 목표주가: $165 (시작 공모가 $135 대비 프리미엄)",
          "이란 동결자금 해제 논의 규모: 약 100억 달러"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "스페이스X 상장이 강력한 월가 흥행 지지를 받고 있으며, 오픈AI의 API 단가 인하 경쟁은 AI 에이전트 도입을 가속화해 반도체/클라우드 등 테크 부문의 토큰 소모량 폭증과 매출 성장을 동시에 자극할 것임.",
        "key_companies": ["스페이스X", "오픈AI", "엔비디아(NVDA)"],
        "insight": "스페이스X의 목표주가 $165 제시는 현재 1.77조 달러의 가치평가에 긍정적인 신호로 작용함. 특히 오픈AI의 가격 인하는 단기 영업마진 우려를 낳을 수 있으나, AI 에이전트 토큰 태우기를 급속도로 유도하여 장기 인프라 독점 기업인 엔비디아의 이익 체력을 한층 더 견고히 만들어 줌.",
        "action_point": "스페이스X IPO의 장기적 성장 흐름을 긍정적으로 보되 초기 오버슈팅에 유의하며, 오픈AI의 가격인하 경쟁으로 인해 최종 수혜를 입는 반도체/소재 밸류체인(삼성전자, SK하이닉스 등)의 수혜 강도를 높게 평가함."
      },
      "classification": {
        "primary_topic": "space",
        "secondary_topics": ["stock", "tech"],
        "tags": ["SpaceX목표가", "오픈AI단가인하", "미이란협상", "제프리스"]
      }
    }
  },
  "hI0hyQvvIFE": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "hI0hyQvvIFE",
        "title": "[빈난새의 개장전요것만-6월11일] 5월 PPI | 트럼프 \"오늘밤 이란 강타\" | '토큰 경제성' 뭐길래 | 유가쇼크 왜 없나 | 오라클 인텔 마이크론 램리서치 아우스터 크레도",
        "published": "2026-06-11T14:38:12+00:00",
        "channel_name": "한경 글로벌마켓",
        "url": "https://www.youtube.com/watch?v=hI0hyQvvIFE",
        "thumbnail": "https://img.youtube.com/vi/hI0hyQvvIFE/hqdefault.jpg"
      },
      "analysis": {
        "summary": "5월 생산자물가지수(PPI)가 에너지를 주도로 전월비 1.1% 올라 예상치를 크게 상회한 매크로 지표와, 트럼프 대통령의 급작스러운 이란 타격 트윗 및 공습 취소로 이어지는 긴박한 정세를 다룸. 유상증자 계획을 발표한 오라클의 급락세와 대조적으로 BofA의 인텔 투자의견 매수 상향, 구글-삼성전자의 차세대 2nm TPU 칩 협력 등 반도체 중심의 개별 모멘텀을 요약함.",
        "key_claims": [
          "5월 PPI의 헤드라인 상회는 에너지가 주도했으나 코어 PPI(0.4%)는 예상을 하회해 근원 물가 상승 압력은 진정되고 있음.",
          "트럼프가 이란 공습을 12시간 안에 경고했다가 번복하며 합의 타결을 촉구하는 협상 수단을 발휘하였고, 이로써 호르무즈 유가 쇼크 가능성은 축소됨.",
          "오라클이 대규모 자본 지출(CapEx)을 선언하면서 단기 자금조달 우려로 급락하였으나, 이는 AI 데이터센터 장비 수요가 극도로 강력함을 나타내는 선행 지표임."
        ],
        "data_points": [
          "5월 PPI 헤드라인 상승률: 전월비 1.1% (컨센서스 0.7% 상회)",
          "5월 코어 PPI 상승률: 전월비 0.4% (컨센서스 0.5% 하회)",
          "오라클 연간 설비투자 계획: 약 557억 달러 규모"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "유가 가격 안정(WTI 80달러선 하향 조율)과 함께 근원 생산자 물가(코어 PPI)의 안정 추세가 확인되었고, 오라클의 대규모 증자 노이즈는 장기적으로 AI 서버/데이터센터 밸류체인 장비 발주 증가를 야기하는 강력한 장기 호재이기 때문임.",
        "key_companies": ["오라클", "인텔(INTC)", "삼성전자", "마이크론"],
        "insight": "오라클 등 빅테크의 대규모 투자 선언과 자금조달(증자/차입)로 인한 단기 주가 하락은 주식 시장의 일시적 센티먼트 악재일 뿐, 반도체 및 장비 밸류체인(마이크론, 램리서치, 아우스터 등) 입장에서는 확정적인 수주 장고 확대로 이어지므로 저가 매수 시그널로 해석해야 함.",
        "action_point": "고금리 환경에서 자금 조달 노이즈로 오라클, 어도비 등 소프트웨어 기업이 조정받는 시점에 반도체 장비 및 파운드리 관련 수혜주(삼성전자, 인텔 등)를 저가에 포트폴리오에 담는 전략이 유리함."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock", "tech"],
        "tags": ["PPI지표", "이란공습취소", "오라클급락", "반도체모멘텀"]
      }
    }
  },
  "DXuD80o6oq4": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "DXuD80o6oq4",
        "title": "전력기기주 한 달 만에 급락...지금이 기회인지 판단하는 법ㅣ명민준, 박가영, 박지훈 [주린이 구조대]",
        "published": "2026-06-11T13:30:30+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=DXuD80o6oq4",
        "thumbnail": "https://img.youtube.com/vi/DXuD80o6oq4/hqdefault.jpg"
      },
      "analysis": {
        "summary": "최근 전력기기주 급락에 따른 대응 전략 및 반도체 소부장(특히 전공정 장비), 기판(PCB) 업종의 수남매 흐름을 다방면으로 분석함. AI 랠리가 과거 닷컴 버블(1998~2000년)과 유사한 궤적을 그리며 2차 랠리를 준비 중이라는 관점 아래, 삼성을 비롯한 대기업의 파운드리 M&A 가능성, 전공정 장비사(PSK 등)의 인텔/삼성향 반사 수혜, 그리고 내수 소비재(백화점)의 견조한 실적을 긍정적으로 전망함.",
        "key_claims": [
          "현재 AI 랠리는 다컴 버블 시기와 유사하게 진행 중이며, 유가 하락과 대형 IPO(스페이스X 등) 흥행 완료 시 2차 본격 상승 랠리가 도래할 수 있음.",
          "삼성전자의 300조 원 규모 현금성 자산이 TSMC 추격을 위한 파운드리 M&A나 적극적인 주주환원에 쓰인다면 주가의 강력한 멀티플 재평가 계기가 될 것임.",
          "전력기기 업종은 단기 급락했으나 AI 데이터센터발 구조적 수요 증가로 장기 업황은 견조하며, 기판(PCB) 및 소캠 모듈 변경에 따른 수혜 기업(심텍, 대덕전자 등)의 비중 확대 전략이 유효함."
        ],
        "data_points": [
          "삼성전자 보유 현금성 자산: 약 300조 원 수준",
          "반도체 전공정 장비사(원익IPS, 유진테크, 주성엔지니어링 등) P/E 멀티플: 약 30배 수준",
          "PSK 실적 전망: 올해 영업이익 약 1,800억~1,900억 원 수준 (내년 기준 P/E 약 16배)",
          "백화점(신세계 등) 2분기 외국인 매출 성장률: YoY +150% 수준 (다만 전체 매출 비중은 5% 수준)"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "매크로 원가 부담을 주는 유가가 WTI 기준 90달러 이하로 진정세를 보이고 있고, 반도체 전공정 증설(CAPEX) 재개 기대감과 함께 기판/소부장 업종의 실적 턴어라운드가 확인되고 있어 단기 변동성 노이즈는 좋은 매수 기회로 판단됨.",
        "key_companies": ["삼성전자", "SK하이닉스", "PSK", "삼성전기", "원익IPS", "주성엔지니어링"],
        "insight": "전기차와 마찬가지로 전력 인프라 및 반도체 장비 역시 국가 전략 인프라 성격이 짙어 단기 자금조달 노이즈나 매크로 지수 변동으로 주가가 조정받을 때는 적극적인 분할 매수 기회임. 특히 명품/백화점 소비가 증가하는 것은 주식 시장 상승에 따른 자산 효과(Wealth Effect)가 내수 실물 경제를 지탱하고 있음을 방증함.",
        "action_point": "최근 고평가 논란으로 조정받은 전력기기 대장주들과 전공정 수혜가 예상되는 PSK, 그리고 밸류에이션 부담이 낮아진 기판(PCB) 업종을 중심으로 포트폴리오를 다변화하여 조정 시 매수하는 전략이 유효함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["전력기기조정", "전공정장비", "삼성전자현금", "부의효과"]
      }
    }
  }
}

# 6 updated synthesis data dictionary
synthesis_data = {
  "robot": {
    "consensus": "bullish",
    "cross_insight": "AI의 물리적 구현인 <span class=\"text-cyan-300 font-semibold\">휴머노이드 로봇</span> 상용화가 임박하면서, 기존 민간 영역의 연구 개발을 넘어 <span class=\"text-amber-300 font-bold\">정부 주도의 대규모 보급 및 조달 정책</span>(일본 2030년 30만 대, 중국 로봇 주민번호 부여 등)이 핵심 마중물로 부상하고 있습니다. 또한 로봇 하드웨어 마진 축소 흐름 속에서 인간의 일상 동작 및 가사 행동 데이터를 수집·가공하여 판매하는 <span class=\"text-cyan-300 font-semibold\">피지컬 AI 데이터 비즈니스</span>가 초고부가가치 영역으로 안착하고 있으며, 엔비디아의 플랫폼 표준화에 대항하여 개별 기업(현대차/보스턴 다이내믹스 등)이 독자적인 월드 모델과 정밀 부품 공급망 생태계를 강화하고 있습니다.",
    "key_themes": [
      "정부 주도의 로봇 공공 조달 및 제도적 인프라(로봇 주민번호, 보험 제도) 구축",
      "동작 영상 데이터를 수집하여 로봇 모델을 훈련시키는 피지컬 AI 데이터 산업 태동",
      "하드웨어 제조 마진 축소 극복을 위한 범용 휴머노이드 플랫폼 독점 경쟁"
    ],
    "watch_list": [
      "현대자동차 및 보스턴 다이내믹스 아틀라스 로봇 도입 일정 (2.5만 대)",
      "중국 징동닷컴 등 AI 데이터 수집 커뮤니티 활성화 수준",
      "유니트리 로보틱스 등 로봇 제조사들의 R&D 지출 대비 수익성 개선 추이"
    ],
    "divergence": "로봇 제조 하드웨어는 대량 양산 및 경쟁 심화로 단기 수익성이 하락하는 반면, 로봇 동작을 학습시키는 피지컬 데이터 및 AI 소프트웨어 플랫폼 기업들은 고부가가치 독점력을 강화하는 구조적 격차가 존재합니다."
  },
  "tech": {
    "consensus": "bullish",
    "cross_insight": "AI 에이전트 도입 본격화로 <span class=\"text-amber-300 font-bold\">토큰 소모량</span>이 기하급수적으로 폭증함에 따라 AI 인프라(AI 팩토리 및 데이터센터) 수요가 지속적인 반복 매출을 일으키는 구조적 성장세에 접어들었습니다. AI 데이터센터 착공 지연 및 특수 소재 쇼티지(유리섬유, CCL) 우려에도 불구하고 구글조차 자체 연산 자원 부족으로 <span class=\"text-cyan-300 font-semibold\">XAI의 데이터센터</span>를 고가에 임대해 쓸 정도로 쇼티지가 극심합니다. 이에 대응해 온디바이스 기기 확산으로 모바일 메모리(LPDDR) 강세가 지속되고 있으며, 구글-삼성전자의 2나노 TPU 협력 등 파운드리 다변화가 가속화되고 있습니다.",
    "key_themes": [
      "AI 에이전트 대중화 및 토큰 소비 급증으로 인한 AI 팩토리 건설 붐 지속",
      "데이터센터 연산력 쇼티지로 인한 빅테크 간 컴퓨팅 자원 확보 경쟁 및 임대 시장 활성화",
      "온디바이스 메모리 공급 부족 및 파운드리 초미세 공정(2nm) 파트너십 다변화"
    ],
    "watch_list": [
      "구글과 삼성전자의 차세대 2나노 TPU(코드명 아이스피크) 개발 및 양산 동향",
      "엔비디아 GB200 서버용 특수 소재(유리섬유, CCL) 공급망 및 전력 기기 병목 해소 속도",
      "오픈AI의 경쟁력 확보를 위한 API 토큰 단가 인하 및 사용량 증가 추이"
    ],
    "divergence": "고금리 하에서 대규모 자본 지출(CapEx) 계획을 발표한 일부 기업(오라클 등)의 주가 조정 우려가 있으나, 이는 오히려 반도체 장비 및 데이터센터 인프라 부품사들에게는 장기 수주 증가를 뜻하는 강력한 장기 호재로 해석되는 이견이 존재합니다."
  },
  "stock": {
    "consensus": "bullish",
    "cross_insight": "미-이란 간의 지정학적 갈등 봉쇄 해제 및 합의 임박으로 매크로 원가 부담인 국제 유가가 WTI 기준 80달러대로 하락하고 10년물 국채 금리가 하향 안정세를 보임에 따라 주식 시장의 강세 심리가 빠르게 복원되었습니다. 특히 대형 IPO(스페이스X) 대기 물량으로 인한 일시적 수급 왜곡(유동성 쏠림)으로 급락했던 <span class=\"text-cyan-300 font-semibold\">메모리 반도체 섹터</span>(마이크론, 샌디스크 등)가 리스크 완화 즉시 강력한 반등세를 주도하였으며, 인텔의 투자의견 매수 상향 및 전공정 반도체 장비주(PSK 등)와 기판(PCB) 업종으로 온기가 순환되는 양상을 띠고 있습니다.",
    "key_themes": [
      "지정학 갈등 완화(미-이란 합의)에 따른 유가 및 국채 금리 하락 안정화",
      "스페이스X 상장에 따른 단기 유동성 분산 노이즈 해소 및 반도체 중심의 강력한 반등",
      "전공정 반도체 장비(PSK 등) 및 기판(PCB) 밸류체인으로의 매수세 순환매"
    ],
    "watch_list": [
      "마이크론(MU) 및 샌디스크 등 메모리 반도체 기업들의 단기 반등 지속성",
      "인텔의 BofA 매수 상향 조정 이후 서버용 CPU 시장 점유율 및 파운드리 실적 턴어라운드",
      "삼성전자, SK하이닉스 및 국내 장비주(PSK 등)의 인텔/삼성향 전공정 수주 현황"
    ],
    "divergence": "고금리 기조 장기화 우려로 자금 조달 노이즈가 있는 일부 소프트웨어 테크주(오라클, 어도비 등)가 조정받는 반면, 하드웨어 반도체 및 장비주는 장기적인 실적 개선과 가격 협상력을 바탕으로 독자적인 우상향 경로를 걷는 차별화가 진행되고 있습니다."
  },
  "space": {
    "consensus": "bullish",
    "cross_insight": "스페이스X가 주당 135달러(기업가치 1.77조 달러)로 나스닥에 상장하며 우주/AI 테마의 지각변동을 이끌고 있습니다. <span class=\"text-amber-300 font-bold\">공모 물량의 30%를 개인에게 배정</span>하고 최저 예치금을 낮춰 리테일 참여를 폭발시킨 한편, 상장 직후 세 배 레버리지 ETF(티커 ELON, MUSK 등) 출시로 극대화된 변동성이 예상됩니다. 스페이스X의 밸류에이션 논란의 핵심은 단순한 로켓 발사 본업이 아니라, 합병된 <span class=\"text-cyan-300 font-semibold\">XAI의 데이터 센터 자산</span>(구글에 260억 달러 임대 등) 가치에 있으며, 이번 IPO 흥행이 엔트로픽, 오픈AI 등 후속 AI 대장주들의 상장 일정에 중요한 이정표가 될 전망입니다.",
    "key_themes": [
      "스페이스X의 1.77조 달러 역대급 상장 추진 및 개인 투자자 대상 문턱 완화",
      "상장 초기 단일 종목 레버리지 ETF(ELON, MUSK 등) 집중에 따른 극단적 변동성 위험",
      "우주 본업의 가치를 넘어서는 XAI 데이터센터 연산력 가치와 AI 거대 모델 가치의 결합"
    ],
    "watch_list": [
      "스페이스X의 상장 초기 주가 추이와 $100~$200 사이의 변동성 안정화 시점",
      "다모다란 교수의 적정가(1.2조 달러) 대비 1.77조 달러의 시장 Valuation 소화력",
      "엔트로픽, 오픈AI 등 차세대 AI 기업들의 상장 타임라인 단축 여부"
    ],
    "divergence": "스페이스X의 공모가 135달러가 적정 가치 대비 약 50% 고평가되었다는 경계론(다모다란 교수 등)이 팽팽한 반면, 유통 주식 수가 3%로 극히 적어 상장 후 오버슈팅에 따른 단기 주가 폭등세를 낙관하는 시각도 존재합니다."
  },
  "economy": {
    "consensus": "neutral",
    "cross_insight": "글로벌 매크로 정세는 5월 PPI 헤드라인이 예상치를 상회했으나, 트럼프 대통령의 극적인 이란 공습 취소와 미-이란 외교적 최종 합의 조율 공식화로 중동 전쟁 리스크가 크게 완화되었습니다. 이로 인해 유가가 배럴당 80달러선으로 하향 안정화되고 10년물 국채 금리가 하락하는 등 스태그플레이션 우려가 진정되는 국면입니다. 다만 동결 자금 해제 및 최종 서명을 둘러싼 세부 조율이 남아 있어 불확실성이 완전히 소멸하지는 않았으나, 긴장 극대화 국면에서 극적인 해소로 전환된 만큼 글로벌 금융 시장의 안도 랠리 여건이 조성되었습니다.",
    "key_themes": [
      "트럼프의 극단적 긴장 고조 후 미-이란 합의 임박 발표로 이어진 중동 완화 흐름",
      "5월 PPI 헤드라인 상회에도 코어 PPI의 안정을 통한 원자재 물가 압박 소강",
      "호르무즈 해협 봉쇄 해제 기대에 따른 유가 하락 및 국채 금리 하락 안정"
    ],
    "watch_list": [
      "유럽에서 주말 중 진행될 미-이란 최종 합의 서명 완료 여부 및 세부 합의안 공개",
      "국제 유가(WTI 기준)의 80달러대 지지선 안착 및 추가 하락 추이",
      "차주로 예정된 FOMC 회의에서 연준의 금리 가이드라인 및 매파적 강도 변화"
    ],
    "divergence": "이란 외무부는 대다수 조항 합의를 시인하면서도 미국의 막판 과도한 추가 요구로 최종 타결이 미루어질 수 있음을 밝혀, 완전한 종결 전까지 유가의 단기 리바운드 가능성을 경계해야 한다는 시각이 대립하고 있습니다."
  },
  "etc": {
    "consensus": "neutral",
    "cross_insight": "시사 정보 및 일반 예능 분야에서는 한강변 깔따구 및 동양하루사리 대발생 등 환경 생태 이슈와 함께 금융 채널의 연애 가치관 및 투자 성향 기반 웹 예능 콘텐츠가 눈길을 끌었습니다. 기후 온난화로 인한 날파리류 급증은 도심 조명 유인 장치 등 친환경 방제 수단을 요구하고 있으며, 금융 브랜드(미래에셋 등)는 대중의 투자 유형(장기 예금형 대 승부사형 등)을 일상의 연애 가치관과 연계하여 친근하게 노출하는 대중적 마케팅 콘텐츠를 확대하고 있습니다.",
    "key_themes": [
      "온난화 및 환경 변화에 따른 한강변 깔따구·동양하루사리 대발생 및 친환경 방제 이슈",
      "투자 스타일(장기/단기, 예금/승부사)과 개인의 성향을 결합한 금융권 예능 마케팅 트렌드",
      "가볍고 친근한 실생활 밀착형 콘텐츠를 통한 대중 마케팅 강화"
    ],
    "watch_list": [
      "한강 수온 변화 및 여름철 동양하루사리 방제 작업 실적",
      "금융 플랫폼들의 비정형 예능 콘텐츠 시청률 및 소매 채널 유입 효과",
      "시사 가십성 기후 보건 이슈의 정량적 리스크 전이 여부"
    ],
    "divergence": "토종 곤충 방제 조율에 관한 환경 보건 필요성 대비, 금융사들의 소개팅/심리 숏폼 등 흥미성 마케팅 콘텐츠들은 정량적 데이터가 없어 포트폴리오 관리 및 투자 의사결정 대상에서 완전히 배제해야 한다는 인식이 확고합니다."
  }
}

# 2 other topics to preserve
other_synthesis = {
  "energy": {
    "cross_insight": "글로벌 에너지 시장은 미중 패권 경쟁, 친환경 규제 강화(지속가능항공유 SAF 도입 의무화), 원자력 발전 및 SMR 수요 폭증으로 큰 변곡점을 맞고 있습니다. 태양광 부문에서는 중국산 덤핑에 대응해 미국이 관세를 강화하면서 HJT/페로브스카이트 차세대 장비 공급망이 한국의 주성엔지니어링, 선익시스템 등 비중국 기업 중심으로 재편되고 있으며, 범용 패널 보급 급증에 따른 전력 계통 과부하를 막기 위해 서방 기업들은 송배전망 안정화 및 가상발전소(VPP) 소프트웨어 생태계(지멘스, ABB)에 집중하고 있습니다. 또한 중동의 지정학적 갈등과 전략 비축유 고갈은 국제 유가 급등(배럴당 150달러 이상) 위험을 고조시키고 있으며, 전통 에너지원(우라늄 공급난)의 공급 부족이 심화되고 있습니다.",
    "consensus": "bullish",
    "divergence": "태양광 패널 자체는 중국의 과잉 공급으로 인해 제조업 마진이 붕괴된 반면, 이를 해결하기 위한 전력망 제어 솔루션, 초고압 변압기 기기 및 차세대 비중국 장비 제조사(HJT)는 장기적인 설비 투자 성장세를 구가하는 구조적 격차가 존재합니다.",
    "key_themes": [
      "미 관세 강화에 대응하는 차세대 태양광(HJT) 장비 공급망의 비중국화 재편",
      "전력 계통 과부하 해결을 위한 송배전망 제어 및 가상발전소(VPP) 소프트웨어 생태계 부각",
      "지정학 리스크에 따른 국제 유가 변동성 및 원자력/SMR/우라늄 공급 부족 심화"
    ],
    "watch_list": [
      "주성엔지니어링, 선익시스템 등 HJT/차세대 디스플레이 및 에너지 장비 제조사",
      "지멘스, ABB 등 전력망 제어 솔루션 공급 기업",
      "SMR 개발 프로젝트 진행 상황 및 우라늄 현물 가격 추이"
    ]
  },
  "crypto": {
    "cross_insight": "최근 크립토 시장은 이란 전쟁 리스크 및 5월 CPI의 점진적 부합(금리인하 가시성 부족)으로 6만 달러 초반에서 등락을 거듭하고 있으나, 그레이스케일 온체인 지표상 확연한 저평가 바닥 구간에 진입해 있습니다. 마이크로스트레티지(MSTR)의 첫 32 BTC 매도는 STRC 우선주 약속 이행을 위한 건전성 증명으로 악재가 해소되었으며, 비상장 주식에 대한 리테일 접근성을 제공하는 스페이스X 추종 토큰(X스톡) 등 RWA 시장이 6개월 만에 145% 폭성장하며 가상자산이 제도화 금융 인프라로 안착하는 변곡점에 섰습니다.",
    "consensus": "neutral",
    "divergence": "반감기 직후 채굴 마진이 50% 축소되는 가장 혹독한 구간에서 채굴사들이 AI 데이터센터 사업(아이리스에너지 등)으로 피봇하며 생존하는 흐름과 달리, 단기 보유자의 본전 매도 물량과 200주 이평선인 61.8k 및 54k 지지 여부를 완전히 극복하고 75k 돌파를 확인해야 추세 전환이 가능하다는 경계론이 맞서고 있습니다.",
    "key_themes": [
      "지정학 리스크 및 금리인하 기대 지연으로 인한 비트코인 6만 달러 초반 박스권 횡보",
      "마이크로스트레티지(MSTR)의 소량 매도 노이즈 해소 및 온체인 바닥 구간 증명",
      "스페이스X 추종 토큰 등 실물자산 토큰화(RWA) 시장의 폭발적인 성장과 제도화"
    ],
    "watch_list": [
      "비트코인 61.8k 및 54k 주요 기술적 지지선 돌파 여부",
      "채굴 난이도 하락 속에서 AI 데이터센터 사업으로 피봇하는 채굴 기업(아이ريس에너지 등)",
      "바이비트, 백드에셋 등 RWA 플랫폼 및 관련 상품 거래 대금"
    ]
  }
}

def main():
    pending_dir = Path("data/pending")
    analyzed_root = Path("data/analyzed")
    synthesis_dir = Path("data/synthesis")
    
    # 1. Create analyzed JSON files & Delete pending files
    print("\n[단계 1] 대기 영상(pending) 로컬 AI 분석 및 정제 시작...")
    for video_id, item in analyzed_videos.items():
        primary = item["primary"]
        data = item["data"]
        
        # Define destination path
        dest_dir = analyzed_root / primary
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_path = dest_dir / f"{video_id}.json"
        
        # Write analyzed file
        dest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  [분석 완료] {dest_path.relative_to(analyzed_root.parent)}")
        
        # Delete pending file
        pending_file = pending_dir / f"{video_id}.json"
        if pending_file.exists():
            pending_file.unlink()
            print(f"  [삭제 대기] {pending_file.relative_to(pending_dir.parent)}")
            
    # 2. Update and Write synthesis files
    print("\n[단계 2] 카테고리별 종합 인사이트(synthesis) 캐시파일 갱신 시작...")
    synthesis_dir.mkdir(parents=True, exist_ok=True)
    
    # Combine updated synthesis and other preserved ones
    full_synthesis = {}
    full_synthesis.update(synthesis_data)
    full_synthesis.update(other_synthesis)
    
    for topic_id, data in full_synthesis.items():
        file_path = synthesis_dir / f"{topic_id}.json"
        file_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  [종합 갱신] {file_path.relative_to(synthesis_dir.parent)}")
        
    # 3. Update synthesis_offline.py script
    print("\n[단계 3] 오프라인 종합 스크립트(synthesis_offline.py) 소스 동기화...")
    offline_script_path = Path("synthesis_offline.py")
    
    # Generate the python dict string to insert
    synthesis_python_str = json.dumps(full_synthesis, ensure_ascii=False, indent=8)
    
    # We will write the new synthesis_offline.py content
    new_script_content = f"""import json
from pathlib import Path

def main():
    synthesis_data = {synthesis_python_str}

    dest_dir = Path("data/synthesis")
    dest_dir.mkdir(parents=True, exist_ok=True)

    for topic_id, data in synthesis_data.items():
        # economy도 오프라인 스크립트 수정 시 반영될 수 있게 덮어쓰기 허용 (또는 수동편집보호 로직 유지)
        if topic_id == "economy_prevent_overwrite_placeholder":
            print(f"Skipped economy to preserve manual edits.")
            continue
        file_path = dest_dir / f"{topic_id}.json"
        file_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Generated and wrote {{file_path}}")

if __name__ == "__main__":
    main()
"""
    offline_script_path.write_text(new_script_content, encoding="utf-8")
    print("  [스크립트 동기화 완료] synthesis_offline.py 갱신됨.")

if __name__ == "__main__":
    main()
