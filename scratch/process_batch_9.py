import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.batch_save import save_batch

batch_9 = [
  {
    "video": {
      "id": "teiwI7A2Tx4",
      "title": "[이슈 몰아보기] \"돈 줄 테니 칩 가지고 가\" 젠슨 황, 월가까지 끌어들였다...'엔비디아발 순환금융' 시즌2될까, 시장이 두려워하는 최악의 시나리오 / 교양이를 부탁해",
      "published": "2026-08-12T15:46:41+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=teiwI7A2Tx4",
      "thumbnail": "https://img.youtube.com/vi/teiwI7A2Tx4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아 젠슨 황 CEO가 월가 사모펀드와 연계하여 AI 가속기 구매 자금을 대출해 주는 <span class=\"text-cyan-300 font-semibold\">엔비디아발 순환 금융 메커니즘</span>을 정밀 분석함. 칩 판매 매출이 대출 자금으로 선순환하며 실적을 끌어올리고 있으나, 칩 감가상각과 <span class=\"text-rose-400 font-medium\">버블 청산 시 파급력</span>이 시장의 핵심 우려로 제기됨.",
      "key_claims": [
        "엔비디아 칩을 담보로 한 사모 부채 금융이 AI 인프라 구매 유동성을 전격 공급.",
        "수출 실적이 금융 레버리지와 상호 연동되어 칩 가격 하락 시 리스크 증폭 가능성."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "AI 하드웨어 매출 성장의 강한 모멘텀과 순환 금융의 잠재 리스크 팽팽.",
      "key_companies": ["엔비디아(NVDA)", "코어위브(CoreWeave)"],
      "insight": "제조업과 월가 레버리지 금융의 결합은 매출 폭증을 만들어내지만, 차세대 반도체 교체 주기에 따른 담보 가치 평가가 밸류에이션의 변수임.",
      "action_point": "엔비디아 실적 발표 시 사모펀드 및 네오클라우드 채권 발행 잔고 정밀 모니터링."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["엔비디아", "젠슨황", "순환금융", "GPU담보대출", "AI버블시나리오"]
    }
  },
  {
    "video": {
      "id": "tqKwh452Bk4",
      "title": "비트코인 바닥 임박? 기관은 이미 움직였다 | 서동주, 김동환, 박상혁 디지털애셋 편집장 [크립토 PLUS]",
      "published": "2026-08-12T02:57:18+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=tqKwh452Bk4",
      "thumbnail": "https://img.youtube.com/vi/tqKwh452Bk4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "비트코인 가격이 조정 국면을 마치고 바닥을 형성 중인 온체인 데이터를 분석함. 전통 금융 기관들의 <span class=\"text-cyan-300 font-semibold\">현물 ETF 유입세</span>와 마이크로스트레티지(MSTR) 등의 기업용 트레저리 자금 유입이 하방 지지선을 단단히 형성하며 <span class=\"text-amber-300 font-bold\">제도권 자금 재유입</span>이 본격화되고 있음.",
      "key_claims": [
        "비트코인의 온체인 바닥 지표 확인 및 글로벌 기관 자금의 저점 매수세 유입.",
        "MSTR 및 비트코인 현물 ETF를 통한 지속적인 락인 자금 축적."
      ],
      "data_points": [
        "비트코인 현물 ETF 일간 순유입: 플러스 전환 유지"
      ],
      "signal": "bullish",
      "signal_reason": "기관 자금 및 트레저리 펀드 유입으로 가상자산 바닥 확인 및 재반등 기대.",
      "key_companies": ["MicroStrategy(MSTR)", "BlackRock(BLK)"],
      "insight": "크립토 자산은 개미 투기판을 넘어 기업 재무재표 및 기관 ETF 포트폴리오의 필수 대체 자산으로 안착하고 있음.",
      "action_point": "비트코인 현물 ETF 순유입 데이터 추적 및 기술적 바닥선 분할 매수 관점."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": ["stock", "economy"],
      "tags": ["비트코인바닥", "기관자금유입", "현물ETF", "MSTR", "디지털자산"]
    }
  },
  {
    "video": {
      "id": "uebrH9DEkZU",
      "title": "IMF 때보다 힘들었다. 한국만 뜯어먹힌 이유 (AFW파트너스 이선엽 대표) | 26년 08월 11일 녹화",
      "published": "2026-08-12T07:55:17+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=uebrH9DEkZU",
      "thumbnail": "https://img.youtube.com/vi/uebrH9DEkZU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "7월 한국 증시가 글로벌 최악의 폭락을 경험한 원인을 수급과 반대매매 구조 관점에서 분석함. 해외 매크로 악재보다 <span class=\"text-rose-400 font-medium\">국내 신용 반대매매 폭탄</span>과 자산가들의 청산이 겹친 쏠림 현상이었으며, 실적 펀더멘탈(반도체 마진)이 살아있는 만큼 <span class=\"text-amber-300 font-bold\">과도한 하락 후 반등 타당성</span>을 보증함.",
      "key_claims": [
        "한국 증시 폭락의 본질은 글로벌 펀더멘탈 훼손이 아닌 국내 신용 털어내기 수급 폭탄.",
        "반도체 대장주의 영업이익률 및 FCF 펀더멘탈이 견고하여 V자 반등 여력 상존."
      ],
      "data_points": [
        "코스피 7월 한 달 하락 폭: 약 22%~23% 기록 (역대급 단기 낙폭)"
      ],
      "signal": "bullish",
      "signal_reason": "수급 투매로 인한 과도한 저평가 상태로 반도체 펀더멘탈 기반 기술적 강반등 유력.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "펀더멘탈과 괴리된 수급 악재성 폭락은 시장 참여자에게 극도의 고통을 주지만, 동시에 사상 최대의 저점 매수 기회를 제공함.",
      "action_point": "신용 청산이 마무리된 수주형 반도체 대장주의 바닥 매수 전략 실행."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["한국증시폭락", "이선엽", "신용반대매매", "수급청산", "반도체펀더멘탈"]
    }
  },
  {
    "video": {
      "id": "UQ76V08T8dI",
      "title": "[LIVE] 매출 5.8억 달러인데 57억 달러 투자…네비우스는 돈을 어디서 구했나 | 이나연 특파원",
      "published": "2026-08-12T21:16:21+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=UQ76V08T8dI",
      "thumbnail": "https://img.youtube.com/vi/UQ76V08T8dI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "AI 클라우드 기업 <span class=\"text-cyan-300 font-semibold\">네비우스(Nebius)</span>의 주가가 30% 이상 폭등한 사업 모델을 정밀 분석함. 분기 매출 5.8억 달러의 10배인 57억 달러를 투자할 수 있었던 비결은 <span class=\"text-amber-300 font-bold\">고객 선결제 자금(90억 달러 이상)</span>을 미리 받아 GPU와 데이터센터를 짓는 파이프라인 덕분이며, 에비타 마진율 49%를 달성함.",
      "key_claims": [
        "네비우스 2분기 매출 5.8억 달러(454% 성장), AI 클라우드 매출 5.7억 달러(514% 성장).",
        "고객사 선결제(90억 달러 이상)로 투자금을 조달하는 선순환 데이터센터 증설 모델 확립.",
        "AI 클라우드 사업부의 조정 EBITDA 마진율 49% 달성으로 흑자 구조 안착."
      ],
      "data_points": [
        "네비우스 2분기 매출: 5억 8,230만 달러 (전년 대비 454% 급증)",
        "고객 선결제 예상 규모: 90억 달러 상회",
        "조정 EBITDA 마진율: 49% 흑자 달성"
      ],
      "signal": "bullish",
      "signal_reason": "고객 선결제 기반 자금 선순환과 에비타 마진 49%로 입증된 네오클라우드의 강력한 수익성.",
      "key_companies": ["네비우스(NBIS)", "마이크로소프트(MSFT)", "메타(META)", "엔비디아(NVDA)"],
      "insight": "AI 컴퓨팅 자원은 이제 서비스 개시 전 고객이 먼저 대금을 납입하는 강력한 매도자 우위 시장(Seller's Market)임.",
      "action_point": "네비우스 및 AI 클라우드 인프라주 추가 상승 모멘텀 보유."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["네비우스", "NBIS", "선결제모델", "EBITDA마진49%", "AI클라우드"]
    }
  },
  {
    "video": {
      "id": "vaVGAtlxGfI",
      "title": "모건스탠리 “메모리 조달 FOMO”ㅣ앤트로픽·유니트리 상장 러시ㅣ브렌트유 장중 90달러 돌파ㅣ테슬라·스페이스X 합병, 머스크 1조달러 잭팟? | 홍혜진의 뉴욕브리핑",
      "published": "2026-08-11T14:15:48+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=vaVGAtlxGfI",
      "thumbnail": "https://img.youtube.com/vi/vaVGAtlxGfI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "모건스탠리가 글로벌 빅테크들의 <span class=\"text-cyan-300 font-semibold\">메모리 조달 FOMO</span> 상태를 보고하며 한국 메모리 2사의 가격 결정권을 높이 평가함. 동시에 앤스로픽, 유니트리 등 AI 및 휴머노이드 상장 러시와 국제 유가 90달러 돌파에 따른 <span class=\"text-rose-400 font-medium\">거시 인플레 리스크</span>를 종합 다룸.",
      "key_claims": [
        "모건스탠리의 글로벌 서버 업체 메모리 칩 확보 경쟁(FOMO) 진단.",
        "앤스로픽(AI) 및 유니트리(휴머노이드)의 IPO 추진으로 피지컬 AI 투자 붐 가속."
      ],
      "data_points": [
        "브렌트유 가격: 장중 배럴당 90달러 돌파"
      ],
      "signal": "bullish",
      "signal_reason": "메모리 칩 조달 FOMO와 AI/휴머노이드 기업 상장 러시로 반도체 및 테크주 강력 수혜.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "Anthropic", "Unitree"],
      "insight": "AI 모델과 로봇 기업들의 상장 열풍은 하드웨어 실물 부품을 공급하는 메모리와 액추에이터 제조업체의 마진을 사상 최고치로 당겨옴.",
      "action_point": "메모리 조달 수혜주(SK하이닉스) 및 피지컬 AI 로봇 관련주 비중 확정."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "robot"],
      "tags": ["모건스탠리", "메모리FOMO", "유니트리IPO", "앤스로픽", "SK하이닉스"]
    }
  },
  {
    "video": {
      "id": "w6Zfi8dY6ao",
      "title": "[26.08.12 오전 방송 전체보기] 미·이란 협상 불안과 CPI 발표 경계감 속 뉴욕증시 하락 마감",
      "published": "2026-08-12T03:15:31+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=w6Zfi8dY6ao",
      "thumbnail": "https://img.youtube.com/vi/w6Zfi8dY6ao/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국과 이란의 평화 협상 지정학적 난항과 7월 CPI 발표를 앞둔 시장의 관망세로 뉴욕증시가 약세를 보임. 지정학적 유가 상승 압력에도 불구하고 <span class=\"text-cyan-300 font-semibold\">빅테크 AI CapEx 실적</span>이 하방 지지력을 형성하는 <span class=\"text-amber-300 font-bold\">혼조세 장세</span>를 분석함.",
      "key_claims": [
        "중동 지정학 불안과 CPI 대기 심리로 뉴욕 증시 단기 숨고르기.",
        "유가 상승 노이즈 속에서도 빅테크들의 인프라 투자 가이던스는 굳건."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "지정학 노이즈와 CPI 지표 발표 전 관망세 심리 우세.",
      "key_companies": [],
      "insight": "매크로 지표 발표 직전의 불안은 과도한 투매를 자제하고 펀더멘탈 우량주를 저점 체크하는 적기임.",
      "action_point": "CPI 결과 발표 확인 전 관망 기조 속 반도체주 분할 대응."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["뉴욕증시하락", "미이란협상", "CPI경계감", "매크로관망세", "삼프로TV"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_9)
    print(f"Processed batch 9: {n} items saved.")
