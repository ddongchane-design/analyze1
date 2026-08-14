import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.batch_save import save_batch

batch_1 = [
  {
    "video": {
      "id": "9UtyoY9dV_A",
      "title": "[박신영의 개장전요것만-8월13일] 애플 실적 회복에 반도체 밸류체인 수혜 | \"AI 버블 아냐\" 반박 확산",
      "published": "2026-08-13T00:00:00+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=9UtyoY9dV_A",
      "thumbnail": "https://img.youtube.com/vi/9UtyoY9dV_A/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">애플(AAPL)</span>의 온디바이스 AI 탑재 신제품 수요 회복과 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>, TSMC 등 부품 밸류체인의 실적 견인력이 확인됨. 월가 일각의 <span class=\"text-rose-400 font-medium\">AI 버블론</span>에 대해 빅테크들의 하이퍼스케일 수주잔고와 생산성 향상 데이터가 논박 조항으로 작동하며 반도체 투심이 회복세로 전환됨.",
      "key_claims": [
        "애플의 실적 반등과 AI 기기 교체 주기가 부품 공급망(메모리, 파운드리)의 매출 확대로 연결됨.",
        "월가 주요 기관들이 AI 설비 투자 대비 ROI 창출이 차례로 가시화되고 있음을 들어 버블론을 반박함."
      ],
      "data_points": [
        "미국 나스닥 지수: 기술주 저가 매수세 유입으로 반등"
      ],
      "signal": "bullish",
      "signal_reason": "애플 밸류체인 수혜 및 AI 버블 의구심 완화로 반도체 및 빅테크 중심의 상승 모멘텀 재개.",
      "key_companies": ["애플(AAPL)", "SK하이닉스(000660)", "TSMC(TSM)", "엔비디아(NVDA)"],
      "insight": "AI 인프라 투자가 빅테크 실적과 유통 기기(온디바이스 AI) 실물 수요로 실질화되는 국면에서 반도체 대장주의 마진 가시성이 강화됨.",
      "action_point": "애플 AI 스마트폰 공급망 부품사 및 HBM 공급사 중심의 포트폴리오 유지."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["애플실적", "AI버블논박", "SK하이닉스", "온디바이스AI", "반도체밸류체인"]
    }
  },
  {
    "video": {
      "id": "A6kds6mMlJw",
      "title": "용산 아이맥스 매진 사례... '오디세이'의 압도적 비주얼 비밀",
      "published": "2026-08-12T11:00:00+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=A6kds6mMlJw",
      "thumbnail": "https://img.youtube.com/vi/A6kds6mMlJw/hqdefault.jpg"
    },
    "analysis": {
      "summary": "크리스토퍼 놀란 감독의 영화 '오디세이'가 장편 영화 최초로 전 편을 <span class=\"text-cyan-300 font-semibold\">IMAX 70mm 1565 필름 카메라</span>로 촬영하여 극장 티켓 매진 행렬을 일으킴. 대형 필름 구동 시 발생하는 기계 소음을 차단하는 <span class=\"text-cyan-300 font-semibold\">대형 방음 블림프 하우징</span> 기술 개발이 풀 렌즈 촬영 성공의 결정적 전기가 됨.",
      "key_claims": [
        "1565 규격 필름의 압도적 면적과 해상도로 극장 전용 프리미엄 관람 경험을 제공.",
        "카메라 소음제어 방음 블림프 하우징 기술 혁신이 대화 장면 포함 전편 촬영을 가능하게 함."
      ],
      "data_points": [
        "IMAX 1565 규격 필름: 초당 24프레임 구동 시 1분당 100m 필름 이동"
      ],
      "signal": "neutral",
      "signal_reason": "영상 및 음향 엔지니어링 기술 혁신 사례로 시장 수혜는 개별 멀티플렉스 프리미엄관에 국한됨.",
      "key_companies": ["IMAX"],
      "insight": "OTT 스트리밍 시대에 오프라인 극장이 생존하기 위해 초고화질 아날로그 필름엔지니어링 등 초격차 차별화 경험이 필수적임.",
      "action_point": "프리미엄 멀티플렉스 관람 트렌드와 하이엔드 찰영 장비 엔지니어링 생태계 트렌드 관찰."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["etc"],
      "tags": ["아이맥스", "오디세이", "1565필름", "놀란감독", "카메라엔지니어링"]
    }
  },
  {
    "video": {
      "id": "ah1IcZntJIk",
      "title": "“오픈AI까지 돈이 부족하다?” AI 붐의 예상 못 한 위기 #교양이를부탁해 #반도체 #AI버블 #데이터센터 #코스피",
      "published": "2026-08-12T11:00:23+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=ah1IcZntJIk",
      "thumbnail": "https://img.youtube.com/vi/ah1IcZntJIk/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">오픈AI</span>와 앤스로픽 등 최고위 AI 연구소들이 막대한 데이터센터 임대료와 컴퓨팅 조달로 인한 <span class=\"text-rose-400 font-medium\">자금 경색(CapEx 부담)</span>에 직면함. 금리 부담과 기존 주주의 지분 희석 반대로 유상증자 및 IPO 추진이 지연되면서, 신규 펀딩 및 칩 담보 채권 발행 등 고위험 구조화 금융이 유행하고 있음.",
      "key_claims": [
        "오픈AI 및 스타트업들의 천문학적 컴퓨팅 비용 부담으로 IPO 및 추가 자금 조달 압박 심화.",
        "기존 주주 반대 및 고금리로 인한 증자 및 채권 발행 제약이 AI 생태계의 뇌관으로 부각.",
        "가을-내년 봄 사이 대규모 신주 발행 및 IPO 물량이 시장으로 쏟아질 가능성 경계."
      ],
      "data_points": [
        "OpenAI 및 Anthropic 등 주요 AI 스타트업의 자체 데이터센터 소유 비율: 0% (전량 임대 운영)"
      ],
      "signal": "bearish",
      "signal_reason": "AI 대표 스타트업들의 캐시카우 부재와 데이터센터 임대료 부담에 따른 유동성 리스크가 부각됨.",
      "key_companies": ["OpenAI", "Anthropic", "마이크로소프트(MSFT)"],
      "insight": "AI 모델 고도화 경쟁 속에서 수익화(ROI) 증명이 지연될 경우, 과도한 부채 및 지분 희석에 따른 밸류에이션 하향 조정 압력이 거세질 수 있음.",
      "action_point": "스타트업 기반 AI 관련주의 조달 리스크 경계 및 확실한 현금 창출력을 갖춘 플랫폼 기업 위주 재편."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock", "economy"],
      "tags": ["오픈AI", "자금경색", "AI데이터센터", "IPO연기", "유동성리스크"]
    }
  },
  {
    "video": {
      "id": "Aqrw5z0CDMk",
      "title": "영화 '오디세이' 영화관 안 가던 사람도 IMAX 찾는 이유 | 놀란 감독이 IMAX에 집착한 기술적 이유",
      "published": "2026-08-12T11:09:09+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=Aqrw5z0CDMk",
      "thumbnail": "https://img.youtube.com/vi/Aqrw5z0CDMk/hqdefault.jpg"
    },
    "analysis": {
      "summary": "영화 '오디세이'의 상영을 계기로 <span class=\"text-cyan-300 font-semibold\">IMAX 1.43:1 비율관</span>에 관객이 몰리는 기술적 배경을 다룸. 소음 저감 쿨링 및 <span class=\"text-cyan-300 font-semibold\">방음 블림프 시스템</span> 덕분에 조용한 대사 장면까지 아날로그 대형 필름으로 촬영이 가능해졌으며, 극장에서만 경험할 수 있는 공간감을 선사함.",
      "key_claims": [
        "아이맥스 카메라 소음제어 하우징 도입으로 조용한 실내 대사 장면 전면 필름 촬영 성사.",
        "1.43:1 풀 사이어티 화면 비율이 선사하는 오프라인 전용 공간 몰입감 극대화."
      ],
      "data_points": [
        "아이맥스 1565 필름 면적: 일반 35mm 필름 대비 약 10배 이상 거대"
      ],
      "signal": "neutral",
      "signal_reason": "영화 및 광학 영상 기술 혁신 분석 콘텐츠.",
      "key_companies": ["IMAX"],
      "insight": "기술적 소음과 물리적 한계를 극복한 하드웨어 엔지니어링 혁신이 콘텐츠의 가치를 극대화함.",
      "action_point": "하이엔드 디스플레이 및 영상 장비 기술의 산업적 응용 분야 트렌드 주시."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["etc"],
      "tags": ["IMAX", "오디세이", "광학기술", "방음하우징", "크리스토퍼놀란"]
    }
  },
  {
    "video": {
      "id": "B2NEXlc578k",
      "title": "\"장부에 안 적히는 빚이 있다?\" 빅테크 데이터센터 뒤에 숨은 위험 #교양이를부탁해 #반도체 #AI버블 #데이터센터 #코스피",
      "published": "2026-08-12T11:45:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=B2NEXlc578k",
      "thumbnail": "https://img.youtube.com/vi/B2NEXlc578k/hqdefault.jpg"
    },
    "analysis": {
      "summary": "빅테크들이 AI 데이터센터 구축 자금을 마련하기 위해 특수목적법인(SPC)을 활용한 <span class=\"text-rose-400 font-medium\">부외부채(Off-Balance Sheet Debt)</span> 구조화를 가동함. 재무제표 부채비율 상승을 감추면서 과도한 레버리지를 일으키는 연계 금융 방식은 향후 금리 변동성이나 데이터센터 수요 감소 시 <span class=\"text-rose-400 font-medium\">금융 우발 채무 뇌관</span>으로 작동할 수 있음.",
      "key_claims": [
        "SPC 및 하이퍼스케일 임대 계약을 통한 재무제표 외 부채 확산 위험.",
        "레버리지에 기반한 과도한 데이터센터 우회 증설이 금융 시스템의 잠재 리스크 유발."
      ],
      "data_points": [
        "글로벌 빅테크 데이터센터 우회 레버리지 금융 발행액 증가 추세"
      ],
      "signal": "bearish",
      "signal_reason": "빅테크 재무제표 우회 부채 증가 및 차등 레버리지 노출에 따른 리스크 고조.",
      "key_companies": ["마이크로소프트(MSFT)", "구글(GOOGL)", "오라클(ORCL)"],
      "insight": "AI 인프라 확장이 정통 재무제표를 넘어 위험 금융 기법으로 연계될 경우 레버리지에 의한 후폭풍을 경계해야 함.",
      "action_point": "빅테크 기업들의 부외 부채 비율 및 레버리지 구조 정밀 체크 후 보수적 접근."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["부외부채", "SPC금융", "데이터센터위험", "레버리지", "AI버블"]
    }
  },
  {
    "video": {
      "id": "bGb1gRTHJ-4",
      "title": "시중은행보다 더 버는 증권사...미래에셋, 분기 순익 1.9조원 | SMR·양자·우주…정부, 7대 미래성장동력 '씨앗' 뿌린다 | 권순우 삼프로TV 취재팀장 [뉴스3]",
      "published": "2026-08-12T22:56:04+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=bGb1gRTHJ-4",
      "thumbnail": "https://img.youtube.com/vi/bGb1gRTHJ-4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">미래에셋증권</span>이 해외 투자 자산 평가이익 회수 등에 힘입어 분기 순이익 1.9조 원이라는 사상 최대 실적을 달성함. 동시에 정부가 <span class=\"text-amber-300 font-bold\">SMR(소형모듈원전), 양자, 우주항공</span> 등 7대 미래성장동력 분야에 국가 R&D 및 예산을 집약 투입하는 정책적 지원안을 발표함.",
      "key_claims": [
        "미래에셋증권의 해외 자산 트레이딩 및 IB 실적 대폭 호조로 금융권 최고 실적 기록.",
        "정부 주도의 SMR, 양자컴퓨팅, 우주 산업 7대 딥테크 성장 전략 구체화."
      ],
      "data_points": [
        "미래에셋증권 분기 순이익: 1조 9,000억 원 기록",
        "정부 지정 7대 미래성장동력: SMR, 양자, 우주 등 포함"
      ],
      "signal": "bullish",
      "signal_reason": "증권사 대형 실적 호조와 정부의 미래 첨단 기술(SMR/우주) 강력 지원책 모멘텀.",
      "key_companies": ["미래에셋증권(006800)", "두산에너빌리티(034020)", "한화에어로스페이스(012450)"],
      "insight": "글로벌 유동성과 정책 R&D 예산이 집중되는 SMR 및 우주항공 핵심 밸류체인의 수혜가 장기화될 가능성 높음.",
      "action_point": "실적 모멘텀이 입증된 초대형 금융주 및 정부 정책 테마(SMR, 우주) 수혜주 분할 매수."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["energy", "space", "economy"],
      "tags": ["미래에셋증권", "분기순익1.9조", "SMR", "7대미래성장동력", "우주항공"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_1)
    print(f"Processed batch 1: {n} items saved.")
