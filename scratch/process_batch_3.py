import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.batch_save import save_batch

batch_3 = [
  {
    "video": {
      "id": "d2QGRYYfkZg",
      "title": "[이슈 몰아보기] \"결국 빅테크가 승자?\" 엔비디아·MS·구글 실적 발표 직후 유입되는 '진짜 자금'의 행방, 반도체 대장주의 운명은? / 교양이를 부탁해",
      "published": "2026-08-11T15:00:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=d2QGRYYfkZg",
      "thumbnail": "https://img.youtube.com/vi/d2QGRYYfkZg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아, 마이크로소프트, 구글 등 글로벌 빅테크의 실적 발표 이후 <span class=\"text-cyan-300 font-semibold\">실질 CapEx 투입 자금</span>의 유입 경로를 추적함. 하이퍼스케일 데이터센터 증설에 필수적인 <span class=\"text-cyan-300 font-semibold\">HBM 및 고성능 메모리</span> 독점력을 보유한 수주 중심 한국 대장주(SK하이닉스)로 패시브 및 메이저 자금 쏠림이 한층 뚜렷해짐.",
      "key_claims": [
        "빅테크들의 CapEx 지출 확대로 반도체 대장주의 마진 가시성이 가장 탄탄함.",
        "글로벌 패시브 자금이 밸류에이션 부담이 적은 메모리 수주 기업으로 원활히 유입 중."
      ],
      "data_points": [
        "빅테크 분기 CapEx 성장률: 전년 대비 평균 40% 이상 상향 유지"
      ],
      "signal": "bullish",
      "signal_reason": "빅테크 AI 인프라 투자 지속 및 수주 기반 반도체 대장주로 자금 쏠림 강화.",
      "key_companies": ["엔비디아(NVDA)", "마이크로소프트(MSFT)", "SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "AI 인프라 투자의 최대 수혜는 과도한 마케팅 비용을 쓰는 서비스사보다 필수 부품 공급 독점권을 쥔 수주형 제조업체에 귀속됨.",
      "action_point": "실적 장세 유효 구간에서 SK하이닉스 등 반도체 톱픽 포트폴리오 비중 유지."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["빅테크실적", "엔비디아", "SK하이닉스", "HBM수혜", "CapEx확대"]
    }
  },
  {
    "video": {
      "id": "Eqeg_m1_4aQ",
      "title": "26.08.11 한국 주식시장의 핵심 이슈와 향후 전망 (박병창 마스터, 김수환 과장)",
      "published": "2026-08-11T03:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=Eqeg_m1_4aQ",
      "thumbnail": "https://img.youtube.com/vi/Eqeg_m1_4aQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "국내 증시가 코스닥 중심의 순환매와 <span class=\"text-cyan-300 font-semibold\">전공정 반도체 소부장</span>으로 수급이 이동하는 현상을 진단함. 미국 물가지표(CPI) 발표와 연준 매파 발언 등 거시 노이즈 속에서도 <span class=\"text-amber-300 font-bold\">실적 개선 가시성</span>이 높은 핵심 주도주 위주의 바벨 전략이 유효하다고 조언함.",
      "key_claims": [
        "코스피 대장주 밸류 부담으로 인한 코스닥 소부장 및 차세대 장비주로의 낙수 효과.",
        "미국 금리 및 유가 변동성 국면에서 실적 확인 중심의 종목 선별 필요."
      ],
      "data_points": [
        "국내 반도체 소부장 업종 평균 수익률 상회 기록"
      ],
      "signal": "neutral",
      "signal_reason": "거시 지표 발표 전 관망세 속 수급 순환매 및 종목별 차별화 진행.",
      "key_companies": ["원익IPS(030530)", "유진테크(084370)", "SK하이닉스(000660)"],
      "insight": "대장주의 밸류에이션 부담이 가중될 때는 밸류체인 하단의 저평가된 1등 부품/장비 공급사로 훈풍이 전이됨.",
      "action_point": "실적 상향이 진행되는 코스닥 전공정 소부장 주도주 분할 매수 대응."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["한국증시전망", "반도체소부장", "순환매장세", "실적선별", "박병창"]
    }
  },
  {
    "video": {
      "id": "FewCsuF8JHw",
      "title": "팔란티어 실적 93% 성장, 시장은 무엇에 돈을 내고 있을까?｜유토피아ㅣ2026.8.12(수)",
      "published": "2026-08-11T23:26:43+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=FewCsuF8JHw",
      "thumbnail": "https://img.youtube.com/vi/FewCsuF8JHw/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">팔란티어(PLTR)</span>가 분기 매출 19억 3,500만 달러(전년 대비 93% 증가)를 기록하며 8분기 연속 성장을 달성함. 단순 LLM 모델 개발사가 아닌 기업의 데이터와 AI를 연결 및 통제하는 <span class=\"text-amber-300 font-bold\">디지털 온톨로지(AIP)</span> 플랫폼 주도권을 쥐면서 기업들이 실질적 통제 소프트웨어에 돈을 지불하고 있음을 증명함.",
      "key_claims": [
        "팔란티어 매출 93% 폭증 및 미국 상업 매출 149% 성장으로 엔터프라이즈 AI 통제권 시장 독점.",
        "기존 고객의 추가 지출 지표(순매출유지율 157%) 확대로 소프트웨어 ROI 입증.",
        "기업들은 비싼 최상위 LLM 대신 적재적소 모델 교체 및 온톨로지 통제 플랫폼에 자금 지출."
      ],
      "data_points": [
        "팔란티어 분기 매출: 19억 3,500만 달러 (전년 대비 93% 폭증)",
        "미국 상업 고객 매출 증가율: 149% 기록",
        "순매출유지율(Net Retention Rate): 157% 달성"
      ],
      "signal": "bullish",
      "signal_reason": "팔란티어의 폭발적 실적 성장이 입증한 엔터프라이즈 AI 소프트웨어 거대한 ROI 창출.",
      "key_companies": ["팔란티어(PLTR)", "엔비디아(NVDA)", "마이크로소프트(MSFT)"],
      "insight": "AI 시대의 진짜 알짜 수익은 모델 자체보다 기업 고유 데이터와 AI를 결합하고 제어하는 거버넌스 플랫폼(온톨로지) 기업이 독식함.",
      "action_point": "팔란티어 등 실질 매출 락인(Lock-in) 효과가 입증된 엔터프라이즈 AI 소프트웨어 대장주에 긍정적 시각 유지."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["팔란티어", "PLTR", "AIP온톨로지", "매출93%성장", "AI소프트웨어"]
    }
  },
  {
    "video": {
      "id": "FO5wiBbYx54",
      "title": "데이터센터 절반이 지연? 주민들이 돌아선 이유 #교양이를부탁해 #반도체 #AI버블 #데이터센터 #코스피",
      "published": "2026-08-11T12:00:31+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=FO5wiBbYx54",
      "thumbnail": "https://img.youtube.com/vi/FO5wiBbYx54/hqdefault.jpg"
    },
    "analysis": {
      "summary": "글로벌 AI 데이터센터 신규 공사의 50% 이상이 지역 주민의 <span class=\"text-rose-400 font-medium\">소음·용수 반대(NIMBY)</span>와 전력망 규제 허가 지연으로 차질을 겪는 현상을 조명함. 지역 고용 창출 효과는 적은 반면 막대한 전력 소모와 소음 피해로 지자체 인허가가 병목으로 부각되면서 <span class=\"text-amber-300 font-bold\">AI 인프라 확장 속도</span>에 제동이 걸리고 있음.",
      "key_claims": [
        "글로벌 AI 데이터센터 증설 공사의 50% 이상이 인허가 및 주민 반대로 일정이 지연됨.",
        "전력 과부하와 소음, 냉각용 용수 부족 이슈가 지역 정가의 민원 뇌관으로 작동.",
        "데이터센터 증설 지연에 따른 자본 비용(CapEx 이자 부담) 상승 리스크."
      ],
      "data_points": [
        "글로벌 신규 데이터센터 사업 지연 비율: 약 50% 상회"
      ],
      "signal": "bearish",
      "signal_reason": "전력 및 지자체 인허가 병목으로 인한 AI 데이터센터 확장 속도 지연 및 차입 비용 증가.",
      "key_companies": ["마이크로소프트(MSFT)", "오라클(ORCL)", "코어위브(CoreWeave)"],
      "insight": "하드웨어 수급 이상으로 전력망 연결 및 지자체 인허가 등 오프라인 물리적 규제가 AI 생태계 병목의 실질 변수로 부상함.",
      "action_point": "독립 전력망 및 이미 인허가를 완료한 데이터센터 운용사 위주의 선별적 투자."
    },
    "classification": {
      "primary_topic": "energy",
      "secondary_topics": ["tech", "stock"],
      "tags": ["데이터센터지연", "전력병목", "NIMBY현상", "인허가병목", "AI인프라"]
    }
  },
  {
    "video": {
      "id": "FrJNgiH4uL4",
      "title": "“반도체만 잘 팔리면 끝?” AI 붐을 흔드는 진짜 변수 #교양이를부탁해 #반도체 #AI버블 #데이터센터 #코스피",
      "published": "2026-08-11T12:30:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=FrJNgiH4uL4",
      "thumbnail": "https://img.youtube.com/vi/FrJNgiH4uL4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "AI 반도체 수요가 견고하더라도 <span class=\"text-rose-400 font-medium\">전력망 둔화와 변압기 쇼티지</span>가 해결되지 않으면 데이터센터 실가동이 불가능한 구조적 불균형을 경고함. 반면 HBM 생산 쏠림으로 인한 <span class=\"text-cyan-300 font-semibold\">범용 DRAM 공급 억제</span> 효과는 한국 메모리 2사의 마진률을 사상 최고치로 견인하는 안전판으로 작동 중임.",
      "key_claims": [
        "전력 인프라 지연이 AI 가속기 실가동을 가로막는 최대 병목 요인.",
        "HBM 쏠림에 따른 레거시 DRAM 공급 부족으로 메모리 판가 상승세 고착화."
      ],
      "data_points": [
        "글로벌 초고압 변압기 리드타임: 평균 3~4년 소요"
      ],
      "signal": "neutral",
      "signal_reason": "전력 병목 리스크와 메모리 반도체 공급 부족 마진 상승 수혜가 팽팽히 대립함.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "HD현대일렉트릭(267260)"],
      "insight": "AI 반도체 구매를 넘어 전력망 및 송배전 기기를 제때 확보한 하이퍼스케일러만이 최종 실적 성과를 거둘 수 있음.",
      "action_point": "전력 송배전 기기주(HD현대일렉트릭 등)와 메모리 톱픽의 분산 보유 권장."
    },
    "classification": {
      "primary_topic": "energy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["전력병목", "변압기쇼티지", "DRAM공급부족", "HBM쏠림", "메모리마진"]
    }
  },
  {
    "video": {
      "id": "FT07VdlQ7ME",
      "title": "“반도체만 잘 팔리면 끝?” AI 붐을 흔드는 진짜 변수 #교양이를부탁해 #반도체 #AI버블 #데이터센터 #코스피",
      "published": "2026-08-11T12:40:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=FT07VdlQ7ME",
      "thumbnail": "https://img.youtube.com/vi/FT07VdlQ7ME/hqdefault.jpg"
    },
    "analysis": {
      "summary": "AI 붐의 지속성을 결정짓는 인프라 공급망 밸류체인(전력, 용수, 반도체 패키징)의 동기화 중요성을 분석함. <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>와 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>의 메모리 독점력이 굳건한 가운데, 전력망 연결 시점이 늦어질 경우 발생할 <span class=\"text-rose-400 font-medium\">단기 재고 조정 가능성</span>을 예의주시해야 함을 제언함.",
      "key_claims": [
        "반도체 칩 출하 대비 데이터센터 전력 수급의 시차로 인한 단기 조정 변수.",
        "메모리 제조업체의 뛰어난 밸류에이션 하방 방어력 증명."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "글로벌 AI 밸류체인의 수급 시차 노이즈 반영.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "인프라 제약이 가져올 시차 변동성을 염두에 두고 수주 가시성이 검증된 핵심 소부장에 자금을 집약하는 지혜가 필요함.",
      "action_point": "반도체주 호실적 모멘텀 속 전력망 이슈 발생 시 저점 매수 기회로 활용."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["energy", "tech"],
      "tags": ["AI밸류체인", "전력수급시차", "메모리독점력", "SK하이닉스", "삼성전자"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_3)
    print(f"Processed batch 3: {n} items saved.")
