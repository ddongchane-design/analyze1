import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.batch_save import save_batch

batch_6 = [
  {
    "video": {
      "id": "LOi9MB-OpR0",
      "title": "시중은행보다 돈 더 버는 증권사... 미래에셋 분기 순익 1.9조 달성 [뉴스3]",
      "published": "2026-08-12T22:40:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=LOi9MB-OpR0",
      "thumbnail": "https://img.youtube.com/vi/LOi9MB-OpR0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">미래에셋증권</span>이 해외 분산 트레이딩 및 대형 IB 자산 수익에 힘입어 분기 순이익 <span class=\"text-amber-300 font-bold\">1.9조 원</span>을 기록하며 시중 4대 은행을 능가함. 국내외 증시 거래대금 상향과 글로벌 유동성 수혜가 대형 증권주의 실적 가시성을 극대화함.",
      "key_claims": [
        "미래에셋증권의 1.9조 원 사상 최대 분기 순익으로 금융권 최고 이익 경신.",
        "글로벌 IB 트레이딩 및 해외 자산 평가이익 회수 호조."
      ],
      "data_points": [
        "미래에셋증권 2분기 순이익: 1.9조 원 달성"
      ],
      "signal": "bullish",
      "signal_reason": "대형 증권사의 사상 최대 순익 달성과 증시 유동성 회복에 따른 밸류에이션 호조.",
      "key_companies": ["미래에셋증권(006800)"],
      "insight": "글로벌 자산배분에 성공한 대형 증권사는 증시 유동성 국면에서 은행권 이상의 폭발적 이익 마진을 창출함.",
      "action_point": "실적 모멘텀이 입증된 초대형 금융주 위주의 수혜 포트폴리오 유지."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["미래에셋증권", "분기순익1.9조", "어닝서프라이즈", "금융주", "증시유동성"]
    }
  },
  {
    "video": {
      "id": "M1ESaXWUOa0",
      "title": "[박신영의 개장전요것만-8월12일] 네비우스, 클라우드 매출 500%↑ | \"스페이스X 두 배 이상 간다\"",
      "published": "2026-08-12T14:00:00+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=M1ESaXWUOa0",
      "thumbnail": "https://img.youtube.com/vi/M1ESaXWUOa0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "AI 특화 클라우드 기업 <span class=\"text-cyan-300 font-semibold\">네비우스(Nebius)</span>의 분기 클라우드 매출이 전년 대비 <span class=\"text-amber-300 font-bold\">500% 폭증</span>하며 주가가 급등함. 동시에 스페이스X의 주당 150달러선 상장 안착 모멘텀과 스타링크 기반 우주 경제 가치가 재평가됨.",
      "key_claims": [
        "네비우스의 클라우드 매출 500% 폭증으로 AI 호스팅 인프라 수혜 입증.",
        "스페이스X 비상장 시가총액 상승에 따른 테슬라 및 우주 항공 밸류체인 멀티플 팽창."
      ],
      "data_points": [
        "네비우스 클라우드 분기 매출 성장률: 전년 대비 500% 폭증"
      ],
      "signal": "bullish",
      "signal_reason": "네오클라우드 매출 폭증 및 스페이스X 상장 모멘텀 호조.",
      "key_companies": ["네비우스(NBIS)", "스페이스X(SpaceX)", "테슬라(TSLA)"],
      "insight": "AI 인프라 호스팅과 우주 위성 인터넷망의 고성장은 글로벌 기술주 시장의 가장 강한 두 축으로 작용함.",
      "action_point": "네오클라우드 및 우주항공 핵심 부품사 포트폴리오 비중 확대."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["space", "tech"],
      "tags": ["네비우스", "NBIS", "클라우드500%성장", "스페이스X", "AI호스팅"]
    }
  },
  {
    "video": {
      "id": "m8UroqrUKCY",
      "title": "스페이스X AI 접고 PC방 차렸습니다 (유진투자증권 정의훈 연구원) | 2026년 08월 10일 녹화",
      "published": "2026-08-11T07:55:10+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=m8UroqrUKCY",
      "thumbnail": "https://img.youtube.com/vi/m8UroqrUKCY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">스페이스X(SpaceX)</span>의 상장 이후 실적 발표 데이터를 분석하며, 단순 궤도 발사를 넘어 <span class=\"text-cyan-300 font-semibold\">스타링크 위성 서비스 구독</span>과 우주 제조 캡슐 회수 사업으로 수익성을 고도화하는 흐름을 조명함. 상장 초기 주가 변동성을 이겨내기 위해 스타링크 캐시카우 실현 여부 확인이 필수적임을 조언함.",
      "key_claims": [
        "스페이스X의 매출 구조가 발사체 중심에서 스타링크 서비스 구독 현금 흐름으로 전환.",
        "상장 직후 변동성 장세 속에서 스타링크 캐시카우 및 우주 회수 캡슐 실적 검증 진증."
      ],
      "data_points": [
        "스타링크 구독자 수 및 궤도 위성 군집 운용 규모 지속 확대"
      ],
      "signal": "neutral",
      "signal_reason": "우주 사업의 구조적 성장세는 확실하나 상장 초기 주가 변동성에 유의 필요.",
      "key_companies": ["스페이스X(SpaceX)", "테슬라(TSLA)", "유진투자증권"],
      "insight": "민간 우주 기업의 성공은 발사 횟수 이상으로 스타링크 등 실질 월 구독료 기반의 캐시카우 구축 여부에 달림.",
      "action_point": "스페이스X의 실질 캐시카우 수치와 스타링크 가입자 추이 모니터링."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["stock", "tech"],
      "tags": ["스페이스X", "스타링크", "우주경제", "정의훈", "우주캐시카우"]
    }
  },
  {
    "video": {
      "id": "NBABD6ar8IQ",
      "title": "동물원정대 시즌2 몰아보기ㅣZoo Rangers2ㅣAI Animation",
      "published": "2026-08-11T05:22:02+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=NBABD6ar8IQ",
      "thumbnail": "https://img.youtube.com/vi/NBABD6ar8IQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "생성형 AI로 제작된 브랜드 애니메이션 '동물원정대 시즌 2'를 통해 검증되지 않은 정보와 <span class=\"text-rose-400 font-medium\">딥페이크/가짜 뉴스</span>가 만드는 위험을 경고함. 데이터 마을 모험 스토리를 통해 올바른 정보 선별과 <span class=\"text-amber-300 font-bold\">디지털 리터러시</span>의 중요성을 교양적으로 전달함.",
      "key_claims": [
        "AI 애니메이션 제작 기술을 활용한 금융사 콘텐츠 마케팅 시도.",
        "가짜 정보 및 허위 데이터 확산 방지를 위한 리터러시 강화 메시지."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "AI 애니메이션 마케팅 및 데이터 교양 콘텐츠.",
      "key_companies": ["미래에셋증권"],
      "insight": "생성형 AI 기술이 영상 제작 인프라를 혁신하는 동시에, 정보의 신뢰성 검증 기술에 대한 수요를 창출함.",
      "action_point": "AI 영상 제작 소프트웨어 및 정보 검증 솔루션 시장 동향 관심."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["etc"],
      "tags": ["동물원정대", "AI애니메이션", "미래에셋", "가짜뉴스경고", "디지털리터러시"]
    }
  },
  {
    "video": {
      "id": "nH5O7kdV-SE",
      "title": "나스닥, CPI 예상치 부합에 상승…코어위브, 네비우스 등 네오클라우드 급등 [월가 뉴스레터]",
      "published": "2026-08-12T22:03:22+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=nH5O7kdV-SE",
      "thumbnail": "https://img.youtube.com/vi/nH5O7kdV-SE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 7월 소비자물가지수(CPI)가 시장 예상치에 부합하며 인플레이션 우려가 완화됨에 따라 나스닥이 강세를 보임. 특히 <span class=\"text-cyan-300 font-semibold\">코어위브(CoreWeave)</span>와 <span class=\"text-cyan-300 font-semibold\">네비우스(Nebius)</span> 등 AI 특화 <span class=\"text-amber-300 font-bold\">네오클라우드(NeoCloud) 호스팅주</span>가 500% 이상의 실적 폭증에 힘입어 시장 상승을 주도함.",
      "key_claims": [
        "미국 CPI 안정세로 금리 우려가 완화되며 기술주 전반에 유동성 재유입.",
        "코어위브, 네비우스 등 네오클라우드 호스팅 기업들의 실적 대폭 호조에 따른 주가 폭등."
      ],
      "data_points": [
        "미국 7월 CPI: 전년 대비 예상치 부합 발표",
        "네비우스 및 코어위브 주가 상승률: 각 10~20% 폭등"
      ],
      "signal": "bullish",
      "signal_reason": "물가지표 안도감과 네오클라우드 실적 폭발로 기술주 중심 상승세 진입.",
      "key_companies": ["코어위브(CoreWeave)", "네비우스(NBIS)", "엔비디아(NVDA)"],
      "insight": "거시 거품 우려 완화와 실질 AI 인프라 매출 폭증이 결합될 때 기술주의 주가 반등 탄성력은 극대화됨.",
      "action_point": "미국 CPI 안정세 속 AI 데이터센터 및 네오클라우드 밸류체인 수혜주 보유."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["미국CPI", "나스닥상승", "코어위브", "네비우스", "네오클라우드"]
    }
  },
  {
    "video": {
      "id": "NhKNlAfNHws",
      "title": "[박신영의 개장전요것만-8월12일] 네비우스, 클라우드 매출 500%↑ | \"스페이스X 두 배 이상 간다\"",
      "published": "2026-08-12T14:10:00+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=NhKNlAfNHws",
      "thumbnail": "https://img.youtube.com/vi/NhKNlAfNHws/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">네비우스(NBIS)</span>의 500% 클라우드 매출 폭증과 <span class=\"text-cyan-300 font-semibold\">스페이스X(SpaceX)</span>의 상장 시가총액 상승 프리미엄을 다룸. AI 호스팅 클라우드와 민간 우주 인터넷망(스타링크)의 폭발적 성장이 미증시 기술주의 <span class=\"text-amber-300 font-bold\">쌍두마차 상승 동력</span>으로 안착함.",
      "key_claims": [
        "네비우스의 AI 클라우드 500% 매출 성장을 통한 하이퍼스케일 호스팅 실적 확인.",
        "스페이스X 상장 프리미엄과 우주 경제 인프라 확장에 따른 멀티플 상향."
      ],
      "data_points": [],
      "signal": "bullish",
      "signal_reason": "AI 클라우드와 우주 경제의 동반 모멘텀에 따른 기술주 상방 압력 유효.",
      "key_companies": ["네비우스(NBIS)", "스페이스X(SpaceX)", "테슬라(TSLA)"],
      "insight": "AI 컴퓨팅 자원 인프라와 지구 저궤도 위성망 사업은 4차 산업혁명의 독점적 디지털 파이프라인 역할을 공고히 함.",
      "action_point": "미국 AI 네오클라우드주 및 우주항공 수혜 밸류체인 집중 보유."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["space", "tech"],
      "tags": ["네비우스", "스페이스X", "클라우드500%", "AI인프라", "미증시상승"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_6)
    print(f"Processed batch 6: {n} items saved.")
