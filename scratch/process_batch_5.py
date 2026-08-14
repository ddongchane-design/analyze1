import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.batch_save import save_batch

batch_5 = [
  {
    "video": {
      "id": "J12wxfY5RSM",
      "title": "시중은행보다 돈 더 버는 증권사... 미래에셋 분기 순익 1.9조 달성 [뉴스3]",
      "published": "2026-08-12T22:30:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=J12wxfY5RSM",
      "thumbnail": "https://img.youtube.com/vi/J12wxfY5RSM/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">미래에셋증권</span>이 해외 분산 자산의 트레이딩 및 수수료 수입 급증으로 2분기 분기 순이익 <span class=\"text-amber-300 font-bold\">1조 9,000억 원</span>을 기록하며 시중 4대 은행을 제치고 금융권 1위를 차지함. 국내외 증시 거래대금 증가와 글로벌 IB 자산 평가이익이 실적 어닝 서프라이즈를 견인함.",
      "key_claims": [
        "미래에셋증권 분기 순이익 1.9조 원 달성으로 시중은행 영업이익 수치 추월.",
        "해외 자산 포트폴리오 트레이딩 성과와 거래대금 증가가 실적 성장을 인도."
      ],
      "data_points": [
        "미래에셋증권 2분기 순이익: 1조 9,000억 원 (사상 최대 기록)"
      ],
      "signal": "bullish",
      "signal_reason": "증권 대장주의 사상 최대 실적 달성과 대형 금융주 밸류에이션 재평가 호조.",
      "key_companies": ["미래에셋증권(006800)"],
      "insight": "증시 유동성 회복과 대형 IB의 글로벌 자산배분 성과가 결합될 때 증권주의 수익 창출력이 기존 은행권을 압도할 수 있음을 입증함.",
      "action_point": "대형 증권주 및 금융 지주사 위주의 실적 모멘텀주 분할 매수."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["미래에셋증권", "분기순익1.9조", "어닝서프라이즈", "금융주", "증시유동성"]
    }
  },
  {
    "video": {
      "id": "K2WMj9XER3A",
      "title": "[박신영의 개장전요것만-8월13일] 엔비디아·MS·구글 실적 가이던스 상회 | 코스피 반도체 순환매 지속",
      "published": "2026-08-13T00:10:00+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=K2WMj9XER3A",
      "thumbnail": "https://img.youtube.com/vi/K2WMj9XER3A/hqdefault.jpg"
    },
    "analysis": {
      "summary": "빅테크 M7(엔비디아, MS, 구글)의 3분기 실적 가이던스가 시장 예상치를 웃돌며 기술주 주가 상승세를 이끔. 국내 증시에서는 대장주 SK하이닉스의 독주에 이어 저평가된 <span class=\"text-cyan-300 font-semibold\">전공정 장비 및 수주 부품주</span>로 온기가 퍼지는 <span class=\"text-amber-300 font-bold\">반도체 온기 순환매</span>가 지속되는 양상임.",
      "key_claims": [
        "빅테크들의 강한 실적 가이던스가 AI 인프라 투자 지속 가능성을 보증함.",
        "코스피 반도체 투톱 중심에서 코스닥 핵심 장비주로 자금이 확산되는 순환매 장세 전개."
      ],
      "data_points": [
        "엔비디아 및 M7 실적 가이던스: 상향 조정 유지"
      ],
      "signal": "bullish",
      "signal_reason": "미국 빅테크 호실적 가이던스와 국내 반도체 전공정 밸류체인 순환매 호조.",
      "key_companies": ["엔비디아(NVDA)", "마이크로소프트(MSFT)", "SK하이닉스(000660)", "원익IPS(030530)"],
      "insight": "빅테크 CapEx 가이던스가 훼손되지 않는 한, 반도체 밸류체인의 낙수 효과는 후공정 HBM에서 전공정 레거시 장비사로 확대됨.",
      "action_point": "실적 상향 조정이 이어지는 반도체 전공정 장비 및 소재주 보유."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["엔비디아가이던스", "반도체순환매", "SK하이닉스", "전공정장비", "M7실적"]
    }
  },
  {
    "video": {
      "id": "K7jgUOHEvjU",
      "title": "지금 주가보다 먼저 봐야 할 건 잉여현금흐름입니다, 삼성전자가 시가총액의 10%를 주주에게 돌려주는 계산 [월간아신 8월호 풀영상]",
      "published": "2026-08-12T06:15:45+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=K7jgUOHEvjU",
      "thumbnail": "https://img.youtube.com/vi/K7jgUOHEvjU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "단기 주가 변동성 폭락 장세에서 기업의 진짜 가치를 판단하는 핵심 지표로 <span class=\"text-cyan-300 font-semibold\">잉여현금흐름(FCF)</span>을 제시함. <span class=\"text-cyan-300 font-semibold\">삼성전자</span>가 창출하는 압도적 현금 창출력과 시가총액 10% 수준의 주주 환원 재원을 분석하며, 투매 장세에 휩쓸리지 않는 <span class=\"text-amber-300 font-bold\">펀더멘탈 가치 평가</span> 기준을 강조함.",
      "key_claims": [
        "폭락장에서 반대매매와 수급 악재에 휩쓸리지 않으려면 FCF 펀더멘탈 점검 필수.",
        "삼성전자의 잉여현금흐름 창출력이 시가총액 대비 10% 수준의 강력한 자사주/배당 재원 기반 제공."
      ],
      "data_points": [
        "코스피 7월 조정 폭: 1997년 IMF 외환위기 이후 최대 변동성 기록",
        "삼성전자 FCF 기반 주주환원 여력: 시가총액의 약 10% 상당"
      ],
      "signal": "bullish",
      "signal_reason": "주가 급락 이후 실물 FCF 기반 밸류에이션 매력도 급상승에 따른 저평가 반등 기대.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "시장이 수급과 투매 노이즈로 붕괴될 때 잉여현금흐름(FCF)이 튼튼한 대장주는 가장 빠른 반등탄성력을 보여줌.",
      "action_point": "FCF 마진율이 뛰어난 반도체 1등주의 펀더멘탈을 신뢰하며 하락 시 분할 매수 모색."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["잉여현금흐름", "FCF", "삼성전자주주환원", "펀더멘탈", "폭락장대응"]
    }
  },
  {
    "video": {
      "id": "LiAkRAiPa1k",
      "title": "[2부] 과학으로 읽어본 빅뱅의 COSMOS (미미미누)",
      "published": "2026-08-12T11:00:25+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=LiAkRAiPa1k",
      "thumbnail": "https://img.youtube.com/vi/LiAkRAiPa1k/hqdefault.jpg"
    },
    "analysis": {
      "summary": "우주의 탄생인 <span class=\"text-cyan-300 font-semibold\">빅뱅 이론</span>과 칼 세이건의 《코스모스》 개념을 대중적인 관점에서 재해석한 대중 과학 교양 콘텐츠. 천체 물리학의 기초 법칙인 우주 팽창론, <span class=\"text-amber-300 font-bold\">우주 배경 방사선</span>, 그리고 별의 진화 과정을 쉽고 유쾌하게 설명함.",
      "key_claims": [
        "빅뱅 이론과 우주배경복사 데이터를 통한 우주 창조 시점 및 물리 법칙 해설.",
        "인류와 우주 입자의 연관성(코스모스 원리)에 대한 교양적 탐구."
      ],
      "data_points": [
        "우주의 나이: 약 138억 년 추산"
      ],
      "signal": "neutral",
      "signal_reason": "천문학 및 기초 과학 대중화 교양 영상 콘텐츠.",
      "key_companies": [],
      "insight": "기초 과학 지식의 대중적 확산이 우주항공 및 기초 소부장 기술에 대한 인문적 관심을 제고함.",
      "action_point": "우주 과학 인프라 및 대중 인공지능/과학 교육 커뮤니케이션 트렌드 모니터링."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["etc"],
      "tags": ["빅뱅이론", "코스모스", "천체물리학", "우주배경복사", "궤도과학"]
    }
  },
  {
    "video": {
      "id": "LIX0bjqRtt4",
      "title": "엔비디아 칩을 담보로 돈을 빌려준다? 월가가 만든 희한한 자금 조달법",
      "published": "2026-08-12T12:00:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=LIX0bjqRtt4",
      "thumbnail": "https://img.youtube.com/vi/LIX0bjqRtt4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "월가 금융사들이 <span class=\"text-cyan-300 font-semibold\">엔비디아 H100/B200 GPU가속기</span> 현물을 물리적 담보로 설정하여 자금을 대출해 주는 신종 담보대출(<span class=\"text-amber-300 font-bold\">Asset-Backed Finance</span>) 기법을 정밀 조명함. 사모펀드(Blackstone 등)의 대출 파이프라인이 AI 스타트업의 설비 투자를 촉진하나, 칩 감가상각 및 차세대 칩 출시 시 <span class=\"text-rose-400 font-medium\">담보 가치 폭락 리스크</span>가 상존함.",
      "key_claims": [
        "엔비디아 GPU를 금융 실물 담보로 활용한 월가의 파격적 신종 자금 조달 구조.",
        "사모부채(Private Credit) 펀드들이 AI 데이터센터 차입 금리를 보증하는 순환 금융 확산.",
        "차세대 AI 칩 출시에 따른 기존 H100 담보 가치 하락 및 청산 뇌관 경계."
      ],
      "data_points": [
        "GPU 담보 대출 규모: 수십억 달러 단위 자금 구조화 집행"
      ],
      "signal": "neutral",
      "signal_reason": "AI 하드웨어 펀딩의 유동성 공급과 담보 가치 훼손 리스크가 동시에 팽팽함.",
      "key_companies": ["엔비디아(NVDA)", "블랙스톤(BX)", "코어위브(CoreWeave)"],
      "insight": "AI 가속기가 실물 금융 상품 및 담보 자산으로 승격되었으나, 칩의 빠른 감가상각 주기가 새로운 금융 리스크를 낳을 수 있음.",
      "action_point": "GPU 담보대출 기반 AI 스타트업의 재무 건전성 및 신규 칩 교체 주기 변동성 체크."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["GPU담보대출", "엔비디아H100", "월가순환금융", "사모부채", "담보가치위험"]
    }
  },
  {
    "video": {
      "id": "Lnn5JCY69Ts",
      "title": "[어바웃 뉴욕] \"스페이스X 상장하면 테슬라 두 배 간다\" | 이나연 특파원",
      "published": "2026-08-12T03:30:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=Lnn5JCY69Ts",
      "thumbnail": "https://img.youtube.com/vi/Lnn5JCY69Ts/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">스페이스X(SpaceX)</span>의 상장(IPO) 성사 시 일론 머스크의 십자 지분 구조 및 브랜드 파워에 입힘어 <span class=\"text-cyan-300 font-semibold\">테슬라(TSLA)</span> 주가가 2배 이상 재평가될 수 있다는 투자 보고서를 분석함. 스타링크 매출의 기하급수적 성장과 <span class=\"text-amber-300 font-bold\">우주 제조 캡슐 회수</span> 사업 가치 반영이 핵심 상승 밸류로 지목됨.",
      "key_claims": [
        "스페이스X 상장 시 머스크 그룹 지배구조 프리미엄으로 테슬라 멀티플 대폭 상향 가능성.",
        "스타링크 및 우주 물류 사업의 수혜로 우주 항공 산업의 투자 붐 가속."
      ],
      "data_points": [
        "스페이스X 목표 시가총액: 3,000억~5,000억 달러 이상 상장 목표"
      ],
      "signal": "bullish",
      "signal_reason": "스페이스X 상장 흥행 기대감과 테슬라의 동반 밸류 상향 프리미엄 모멘텀.",
      "key_companies": ["스페이스X(SpaceX)", "테슬라(TSLA)"],
      "insight": "우주항공 대장주의 상장은 단순한 1개 기업 상장을 넘어 우주 경제 밸류체인 전반의 멀티플을 재평가시키는 기폭제임.",
      "action_point": "스페이스X IPO 타임라인 관련 보도와 국내 우주항공 관련 부품주 추이 모니터링."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["stock", "tech"],
      "tags": ["스페이스X상장", "테슬라2배", "스타링크", "우주항공IPO", "머스크그룹"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_5)
    print(f"Processed batch 5: {n} items saved.")
