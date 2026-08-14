import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.batch_save import save_batch

batch_8 = [
  {
    "video": {
      "id": "QWu3V_Xl5hU",
      "title": "태풍 찬홈, 한국 쪽으로 방향 틀었다. 우리나라까지 영향 줄까?",
      "published": "2026-08-11T11:00:05+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=QWu3V_Xl5hU",
      "thumbnail": "https://img.youtube.com/vi/QWu3V_Xl5hU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "태풍 '찬홈'의 경로가 기온 및 기압 배치 변화로 한국 방향으로 변경된 기상역학적 원인을 분석함. 수온 기조와 북태평양 고기압의 경계선 이동에 따라 <span class=\"text-violet-300 font-medium\">한반도 상륙 리스크</span> 및 집중호우 피해 우려를 교양 기상학 관점에서 해설함.",
      "key_claims": [
        "태풍 찬홈의 기압 경로 변경에 따른 기상 변화 분석.",
        "해수면 온도 상승과 북태평양 고기압 기조가 태풍 이동 경로에 미치는 기상학적 영향."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "기상 과학 및 태풍 경로 해설 콘텐츠.",
      "key_companies": [],
      "insight": "기후 변화에 따른 태풍 이동 경로의 불확실성이 커지면서 기상 모니터링 및 재난 대비 인프라의 중요성이 증대됨.",
      "action_point": "여름철 기상 재난 및 수해 대비 방재·농업 수혜주 동향 모니터링."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["태풍찬홈", "기상학", "태풍경로", "기후변화", "안될과학"]
    }
  },
  {
    "video": {
      "id": "r-DQQIMrSRU",
      "title": "[박신영의 개장전요것만-8월11일] AI 연이은 해킹 사고에 팔로알토 주목 | MS 자체 AI칩에 마벨 수혜",
      "published": "2026-08-11T14:00:55+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=r-DQQIMrSRU",
      "thumbnail": "https://img.youtube.com/vi/r-DQQIMrSRU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "AI 프런티어 모델 관련 해킹 및 탈옥 사태 확산으로 사이버 보안 대표주인 <span class=\"text-cyan-300 font-semibold\">팔로알토 네트워크(PANW)</span>의 지출 수혜가 예상됨. 마이크로소프트의 자체 AI 칩(Maia) 탈엔비디아 행보로 커스텀 실리콘 파트너사인 <span class=\"text-cyan-300 font-semibold\">마벨 테크놀로지(MRVL)</span>의 ASIC 설계 매출 호조가 기대됨.",
      "key_claims": [
        "AI 보안 사고 증가로 팔로알토 네트워크 등 사이버 보안 솔루션 수요 폭증.",
        "MS의 자체 AI 가속기 생산에 따른 마벨(MRVL) 커스텀 ASIC 수주 확대."
      ],
      "data_points": [],
      "signal": "bullish",
      "signal_reason": "AI 사이버 보안 필수화 및 자체 빅테크 ASIC 칩 파트너사 실적 모멘텀 호조.",
      "key_companies": ["팔로알토 네트워크(PANW)", "마벨 테크놀로지(MRVL)", "마이크로소프트(MSFT)"],
      "insight": "AI 생태계가 팽창할수록 필수 안전장치인 보안 솔루션과 전력/비용을 절감하는 자체 커스텀 ASIC 칩 파트너사의 기업가치가 지속 상승함.",
      "action_point": "AI 사이버 보안주(PANW) 및 주문형 반도체 파트너(MRVL)의 분할 매수 전략."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["팔로알토", "PANW", "마벨테크놀로지", "MRVL", "ASIC"]
    }
  },
  {
    "video": {
      "id": "R80LPDWRkps",
      "title": "코스닥부터 화장품·조선·배터리까지 하반기 투자전략은? | 박승영 한화투자증권 PLUS자산전략팀장 [글로벌 인터뷰]",
      "published": "2026-08-12T22:56:04+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=R80LPDWRkps",
      "thumbnail": "https://img.youtube.com/vi/R80LPDWRkps/hqdefault.jpg"
    },
    "analysis": {
      "summary": "한국 증시의 높은 변동성과 섹터별 차별화 국면에서 <span class=\"text-amber-300 font-bold\">하반기 투자 전략</span>을 제시함. 코스닥 순환매 장세 속에서 이익 증가가 입증된 <span class=\"text-cyan-300 font-semibold\">조선, 화장품, 반도체 소부장</span> 중심의 주도주 선별과 퇴직연금(401K) 기반의 장기 자산배분 문화의 필요성을 강조함.",
      "key_claims": [
        "미국 대비 한국 증시의 큰 변동성은 중간재 수출 비중과 주주환원율 차이에서 기인.",
        "하반기 실적 모멘텀이 강한 조선, 화장품, 반도체 소부장 섹터 위주의 종목 대응 권고."
      ],
      "data_points": [
        "코스피 일일 사상 최고가 기록 비율: 3.8% (미국 S&P 500은 8% 기록)"
      ],
      "signal": "bullish",
      "signal_reason": "실적 장세에 진입한 조선, 화장품, 반도체 소부장 중심의 주도주 장세 기대.",
      "key_companies": ["한화 오션(042660)", "HD한국조선해양(009540)", "코스맥스(192820)"],
      "insight": "변동성이 큰 장세일수록 주주환원과 실적 성장 가시성을 동시에 보유한 수출 1등주 위주로 포트폴리오를 압축해야 함.",
      "action_point": "하반기 이익 가시성이 우수한 조선 및 반도체 소부장 주도주 분할 선점."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["하반기투자전략", "조선주", "화장품주", "박승영", "변동성대응"]
    }
  },
  {
    "video": {
      "id": "s0UZeF1a0Mg",
      "title": "[박신영의 개장전요것만-8월12일] 네비우스, 클라우드 매출 500%↑ | \"스페이스X 두 배 이상 간다\"",
      "published": "2026-08-12T14:16:18+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=s0UZeF1a0Mg",
      "thumbnail": "https://img.youtube.com/vi/s0UZeF1a0Mg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 7월 근원 CPI가 2.5% 상승하며 시장 예상치에 부합하자 국채 금리가 하락하고 나스닥 선물이 강세를 기록함. AI 클라우드 매출이 514% 폭증한 <span class=\"text-cyan-300 font-semibold\">네비우스(NBIS)</span>와 상장 프리미엄이 고조된 <span class=\"text-cyan-300 font-semibold\">스페이스X</span>가 기술주 랠리를 진두지휘함.",
      "key_claims": [
        "7월 미국 CPI 3.4%(근원 2.5%)로 시장 예상치에 완벽히 부합하여 인플레이션 안도감 제공.",
        "네비우스의 2분기 AI 클라우드 매출 5억 7,500만 달러(514% 폭증) 발표로 호스팅 수혜 입증."
      ],
      "data_points": [
        "미국 7월 근원 CPI: 전년 동월 대비 2.5% 상승 (예상 부합)",
        "네비우스 AI 클라우드 매출: 5억 7,500만 달러 (전년비 514% 급증)",
        "국제 유가: WTI 배럴당 82.78달러 선 기록"
      ],
      "signal": "bullish",
      "signal_reason": "CPI 부합 안도감과 네비우스 호실적 발표에 따른 기술주 랠리 가속.",
      "key_companies": ["네비우스(NBIS)", "스페이스X(SpaceX)", "엔비디아(NVDA)"],
      "insight": "거시 통화 인플레 압력 해소와 테크 기업의 실질 매출 폭발이 조화를 이루는 안정적 랠리 구간에 진입함.",
      "action_point": "미국 테크 클라우드 및 우주 경제 수혜주 포트폴리오 비중 유지."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["space", "economy"],
      "tags": ["네비우스", "514%급증", "미국7월CPI", "스페이스X", "나스닥상승"]
    }
  },
  {
    "video": {
      "id": "SUDk-BvbCy4",
      "title": "[김현석의 브레이킹 뉴스] 7월 소비자물가지수(CPI) 발표! 8월 12일 오후 9시 30분 L.I.V.E",
      "published": "2026-08-12T12:46:38+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=SUDk-BvbCy4",
      "thumbnail": "https://img.youtube.com/vi/SUDk-BvbCy4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 7월 소비자물가지수(CPI) 생중계를 통해 거시 물가 경로와 연준의 금리 결정 전망을 다룸. 헤드라인 및 근원 CPI 지표가 모두 시장 컨센서스에 들어맞으면서 <span class=\"text-amber-300 font-bold\">고금리 장기화 피로감</span>이 안도감으로 돌아서고 주식 시장의 기술주 저가 매수세를 촉발함.",
      "key_claims": [
        "7월 CPI 지표 부합으로 연준의 금리 인하 기대감 보존.",
        "인플레이션의 완만한 하향 안정세 속에서 시장의 관망세가 랠리로 전환."
      ],
      "data_points": [
        "미국 7월 헤드라인 CPI: 3.4% (예상치 3.4% 부합)"
      ],
      "signal": "bullish",
      "signal_reason": "CPI 지표 시장 컨센서스 완전 부합으로 불확실성 해소 및 증시 반등.",
      "key_companies": [],
      "insight": "매크로 지표의 불확실성이 제거되면 시장의 관심은 다시 기업의 실적(ROI)과 성장성으로 빠르게 복귀함.",
      "action_point": "CPI 통과 후 기술주 및 실적 호조주 중심 주식 비중 재확대."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["미국7월CPI", "김현석", "인플레이션", "연준금리", "매크로안도감"]
    }
  },
  {
    "video": {
      "id": "Td9WU2ahx60",
      "title": "[지식뉴스] \"엔비디아칩이 금융상품 됐다\" AI를 담보 잡아 본격적으로 돈 풀기 시작한 월가...지금부터 봐야 할 진짜 돈의 흐름 / 교양이를 부탁해",
      "published": "2026-08-11T13:00:10+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=Td9WU2ahx60",
      "thumbnail": "https://img.youtube.com/vi/Td9WU2ahx60/hqdefault.jpg"
    },
    "analysis": {
      "summary": "월가 금융권이 엔비디아 GPU를 담보로 대출 자금을 제공하는 <span class=\"text-cyan-300 font-semibold\">실물 자산 담보 금융(Asset-Backed Debt)</span> 메커니즘을 파헤침. 사모펀드 자금이 AI 호스팅 기업에 쏟아져 들어가며 유동성을 공급하고 있으나, 차세대 칩 출시 시 발생할 <span class=\"text-rose-400 font-medium\">기존 담보 가치 폭락 리스크</span>를 경고함.",
      "key_claims": [
        "엔비디아 GPU 가속기를 실물 금융 담보로 인정한 월가의 파격적 사모 대출 구조화.",
        "레버리지에 기반한 과도한 GPU 구매가 차세대 칩(B200/R100) 출시에 따라 감가상각 위험 고조."
      ],
      "data_points": [
        "월가 사모펀드의 GPU 담보 대출 집행액: 수십억 달러 연계"
      ],
      "signal": "neutral",
      "signal_reason": "신종 AI 금융 기법을 통한 유동성 공급과 감가상각 리스크의 팽팽한 대립.",
      "key_companies": ["엔비디아(NVDA)", "블랙스톤(BX)", "코어위브(CoreWeave)"],
      "insight": "AI 하드웨어의 자산화는 유동성 공급에는 긍정적이나, 감가상각 속도가 가파른 기술 자산 특성상 금융 리스크의 연쇄를 유발할 수 있음.",
      "action_point": "GPU 담보 자금 구조를 활용한 AI 기업의 부채 비율 및 차세대 칩 교체 주기 모니터링."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["GPU담보금융", "엔비디아칩자산화", "월가자금흐름", "사모펀드대출", "감가상각위험"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_8)
    print(f"Processed batch 8: {n} items saved.")
