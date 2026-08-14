import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.batch_save import save_batch

batch_2 = [
  {
    "video": {
      "id": "bj3ot8RHy8k",
      "title": "[어바웃 뉴욕] 1조 달러 잭팟 터질까…테슬라-스페이스X 합병설 재부각 | 이나연 특파원",
      "published": "2026-08-12T03:00:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=bj3ot8RHy8k",
      "thumbnail": "https://img.youtube.com/vi/bj3ot8RHy8k/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">테슬라(TSLA)</span>와 <span class=\"text-cyan-300 font-semibold\">스페이스X(SpaceX)</span>의 시너지 합병 시나리오가 부각되며 일론 머스크의 기업가치가 <span class=\"text-amber-300 font-bold\">1조 달러 평가</span>에 진입할 것이라는 월가 전망을 다룸. 자율주행, AI 컴퓨팅 데이터센터 및 스타링크 저궤도 위성 통신의 인프라 결합이 시너지를 극대화할 수 있으나 지배구조 및 주주 반발 리스크가 상존함.",
      "key_claims": [
        "테슬라 AI 데이터센터와 스페이스X 스타링크 네트워크의 결합에 따른 플랫폼 파워 시너지.",
        "스페이스X 비상장 지분 가치 재평가와 테슬라 주가의 연동 모멘텀 형성."
      ],
      "data_points": [
        "합병 시 예상 통합 시가총액: 1조 달러(약 1,350조 원) 이상 추산"
      ],
      "signal": "bullish",
      "signal_reason": "테슬라와 스페이스X의 융합 시너지 및 우주 인터넷/AI 인프라 결합 기대감 모멘텀.",
      "key_companies": ["테슬라(TSLA)", "스페이스X(SpaceX)"],
      "insight": "지상 자율주행 AI와 저궤도 우주 통신망의 결합은 피지컬 AI 시대의 독점적 생태계를 형성하는 거대한 전환점이 될 수 있음.",
      "action_point": "테슬라 및 우주 항공 밸류체인 부품사의 시너지 모멘텀 관찰."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["stock", "tech"],
      "tags": ["테슬라", "스페이스X", "1조달러합병", "스타링크", "일론머스크"]
    }
  },
  {
    "video": {
      "id": "DHh2YlsRN7s",
      "title": "AI 챗봇 도입했더니 매출 3배 폭등? 기업들이 챗봇에 돈 쏟아붓는 이유",
      "published": "2026-08-12T09:00:00+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=DHh2YlsRN7s",
      "thumbnail": "https://img.youtube.com/vi/DHh2YlsRN7s/hqdefault.jpg"
    },
    "analysis": {
      "summary": "기업들이 단순 고객 문의 응대를 넘어 실질적인 결제 유도와 매출 성장을 이끄는 <span class=\"text-cyan-300 font-semibold\">에이전틱 AI 챗봇</span>을 도입하면서 영업 실적이 급격히 상승하는 사례를 다룸. <span class=\"text-amber-300 font-bold\">실시간 구매 전환율</span> 향상과 운영 인건비 절감 효과가 검증되면서 챗봇이 비즈니스 필수 인프라로 자리잡고 있음.",
      "key_claims": [
        "생성형 AI 에이전트 도입이 기업 매출 3배 증가 등 실질적 ROI로 연결.",
        "상담 자동화를 통한 인건비 절감과 구매 유도 알선으로 전환율 극대화."
      ],
      "data_points": [
        "AI 챗봇 도입 기업 매출 성장률: 기존 대비 최고 3배 이상 폭증 사례 확인"
      ],
      "signal": "bullish",
      "signal_reason": "AI 에이전트 도입에 따른 기업 생산성 및 매출 증가 효과 입증으로 관련 소프트웨어 투심 호조.",
      "key_companies": ["오픈AI", "마이크로소프트(MSFT)"],
      "insight": "AI 투자가 단순 비용 지출을 넘어 실질 매출(ROI)을 창출하는 상용화 단계에 안착했음을 보여줌.",
      "action_point": "기업용 AI 에이전트 및 챗봇 솔루션 개발사의 성장성 및 실적 추이 주시."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["AI챗봇", "에이전틱AI", "매출3배", "ROI증명", "고객상담자동화"]
    }
  },
  {
    "video": {
      "id": "EpNKSRDQ-CI",
      "title": "[지식뉴스] \"머스크의 1조 달러 잭팟\" 스페이스X와 테슬라 합병설, 진짜 머스크의 계획",
      "published": "2026-08-12T13:00:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=EpNKSRDQ-CI",
      "thumbnail": "https://img.youtube.com/vi/EpNKSRDQ-CI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "일론 머스크의 스페이스X 상장 및 테슬라와의 우회 합병 구상을 정밀 분석함. 우주 제조, <span class=\"text-cyan-300 font-semibold\">스타링크 위성 네트워크</span>, 테슬라 자율주행 AI의 결합을 통해 <span class=\"text-amber-300 font-bold\">1조 달러 통합 생태계</span> 구축이 논의되는 한편, 지분 희석 이슈와 SEC 규제 등 <span class=\"text-rose-400 font-medium\">지배구조 관련 장애물</span>도 동시에 존재함을 강조함.",
      "key_claims": [
        "스페이스X 스타링크와 테슬라 자율주행 AI의 물리적 네트워크 결합 시도.",
        "일론 머스크 그룹 전반의 자금 조달 및 지배구조 재편 가능성."
      ],
      "data_points": [
        "스페이스X 기업가치 평가액: 주당 150달러 상회 및 2,000억 달러 이상 추산"
      ],
      "signal": "bullish",
      "signal_reason": "스페이스X 상장 모멘텀과 테슬라 기술 시너지에 따른 주가 상방 압력 유효.",
      "key_companies": ["테슬라(TSLA)", "스페이스X(SpaceX)"],
      "insight": "우주항공과 육상 AI의 결합은 단순한 기업 합병을 넘어 미래 산업 주도권을 재편하는 메가 트렌드임.",
      "action_point": "스페이스X의 상장 타임라인 및 테슬라 자율주행 소프트웨어 업데이트 일정 체크."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["stock", "tech"],
      "tags": ["스페이스X", "테슬라합병", "스타링크", "머스크계획", "우주생태계"]
    }
  },
  {
    "video": {
      "id": "BpWNuOc8Yeg",
      "title": "레버리지가 주는 도파민, 너무 위험하다 | 하창완 & 정프로 & 빈센트 [더블 체크]",
      "published": "2026-08-12T06:57:48+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=BpWNuOc8Yeg",
      "thumbnail": "https://img.youtube.com/vi/BpWNuOc8Yeg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "단일 종목 2~3배 레버리지 ETF 및 고변동성 자산 투자가 유발하는 심리적 중독성과 <span class=\"text-rose-400 font-medium\">계좌 원금 손실 위험</span>을 경고함. 변동성에 적응된 도파민 중심의 투자 방식은 <span class=\"text-amber-300 font-bold\">자산배분 원칙</span>을 훼손하여 급락장에서 회복 불가능한 타격을 줄 수 있으므로 리스크 관리가 시급하다고 지적함.",
      "key_claims": [
        "레버리지 상품의 높은 변동성으로 인한 뇌동매매 및 자산 손실 리스크 심화.",
        "도파민 추구형 매매를 피하고 체계적인 원금 방어 전략 수립 필요."
      ],
      "data_points": [
        "레버리지 ETF 투자자의 원금 손실 확률: 일반 정립식 투자 대비 급격히 높음"
      ],
      "signal": "neutral",
      "signal_reason": "투자자 행동학적 리스크 경고 및 리스크 관리 중점 레포트.",
      "key_companies": [],
      "insight": "시장의 변동성 도파민에 휘둘리지 않고 철저한 자산배분과 손절 기준을 지키는 것이 개인 투자자의 장기 생존 조건임.",
      "action_point": "고레버리지 ETF 비중을 축소하고 우량주 및 현금 비중 확대를 통한 리스크 관리."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["레버리지위험", "투자도파민", "자산배분", "리스크관리", "뇌동매매방지"]
    }
  },
  {
    "video": {
      "id": "c-HyoZAinT8",
      "title": "중국 스페이스x 따라잡나?",
      "published": "2026-08-12T08:30:09+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=c-HyoZAinT8",
      "thumbnail": "https://img.youtube.com/vi/c-HyoZAinT8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "중국이 차세대 재사용 로켓 '창정 10B' 시험 발사에서 스페이스X의 다리 착륙 방식 대신 <span class=\"text-cyan-300 font-semibold\">그물 포획(Net Capture) 방식</span>을 도입함. 착륙 충격을 포획 그물이 완수하여 로켓 기체 무게를 경량화하는 혁신을 시도 중이나, 정밀 제어 난이도라는 <span class=\"text-rose-400 font-medium\">기술적 난관</span>이 존재함.",
      "key_claims": [
        "중국의 그물 포획 방식 재사용 로켓 개발로 발사체 무게 경량화 도모.",
        "스페이스X 발사체 독점에 대응한 국가 차원의 우주 기술 자립 속도전."
      ],
      "data_points": [
        "중국 창정 10B 로켓: 넷 캡처 그물 완충 장치 적용"
      ],
      "signal": "neutral",
      "signal_reason": "중국의 우주 기술 독자 개발 시도에 따른 글로벌 우주 패권 경쟁 다변화 분석.",
      "key_companies": ["스페이스X(SpaceX)", "블루오리진(Blue Origin)"],
      "insight": "글로벌 재사용 발사체 기술이 다변화되면서 우주 소부장 및 발사체 회수 솔루션 기술의 가치가 급상승 중임.",
      "action_point": "글로벌 민간 우주 기업들의 로켓 회수 방식 및 발사체 비용 절감 기술 발전 동향 주시."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["tech"],
      "tags": ["중국우주기술", "재사용로켓", "그물포획방식", "창정10B", "스페이스X경쟁"]
    }
  },
  {
    "video": {
      "id": "CezNCD51nx4",
      "title": "코인 맡기면 알아서 굴려준다? 월가도 주목한 '볼트'",
      "published": "2026-08-12T03:25:43+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=CezNCD51nx4",
      "thumbnail": "https://img.youtube.com/vi/CezNCD51nx4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "디파이(DeFi) 생태계에서 스마트 컨트랙트 기반 자산 자동 운용 도구인 <span class=\"text-cyan-300 font-semibold\">볼트(Vault)</span>에 월가 제도권 자금이 유입되는 흐름을 다룸. 실물자산 토큰화(<span class=\"text-cyan-300 font-semibold\">RWA</span>)와 결합된 프로그래밍 방식의 자동화 이자 창출 메커니즘이 기존 자산운용업의 지형을 바꿀 잠재력을 지님.",
      "key_claims": [
        "디파이 볼트(Vault)를 통한 스마트 컨트랙트 자동 자산 운용의 효율성.",
        "기관 자금 및 월가 금융사들의 RWA 토큰 연계 디파이 예치 확대."
      ],
      "data_points": [
        "디파이 볼트 유입 자금 및 RWA 기반 스태이블코인 운용액 증가 추세"
      ],
      "signal": "bullish",
      "signal_reason": "제도권 자금의 디파이 볼트 및 RWA 편입 호조로 가상자산 생태계의 펀더멘털 강화.",
      "key_companies": ["블랙록(BLK)", "Circle(USDC)"],
      "insight": "월가 기관들이 디파이 온체인 파이프라인(Vault)을 수용하면서 온체인 금융과 제1금융권 간의 인프라 통합이 빨라지고 있음.",
      "action_point": "RWA 연계 디파이 프로젝트 및 우량 프로토콜의 TVL 변동성 모니터링."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": ["tech", "stock"],
      "tags": ["디파이볼트", "Vault", "RWA", "월가자금유입", "스마트컨트랙트"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_2)
    print(f"Processed batch 2: {n} items saved.")
