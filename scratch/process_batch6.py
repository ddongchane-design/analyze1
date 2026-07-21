import json
from pathlib import Path

# Define the analyzed data for Batch 6
batch_data = {
  "vZD2-70U_ts": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "vZD2-70U_ts",
        "title": "[6월 10일 마감시황] 삼전닉스 쉬어갈 때, 소부장을 봐야 하는 이유ㅣ홍선애, 이권희, 장우진 [클로징벨 라이브]",
        "published": "2026-06-10T07:11:30+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=vZD2-70U_ts",
        "thumbnail": "https://img.youtube.com/vi/vZD2-70U_ts/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 코스피는 선물 옵션 동기 만기일을 맞아 외국인·기관의 5.8조 원 규모 대량 매도로 4.5% 폭락(7,730선)하며 극심한 널뛰기 변동성을 기록했습니다.\n2. 삼성전자와 SK하이닉스 등 대형주가 쉬어가는 타이밍에, 이익 성장과 장비 공급 모멘텀이 뛰어난 <span class=\"text-cyan-300 font-semibold\">반도체 소부장 대장주</span>들로 수급 이동이 나타났습니다.\n3. 대표 장비주인 PSK홀딩스가 11% 가까이 급등하고 유진테크, 테스가 선방하는 등 하이엔드 후공정 장비 밸류체인의 강세가 두드러졌습니다.",
        "key_claims": [
          "옵션 만기 수급 교란과 신용/미수 반대매매로 대형 기술주의 낙폭이 과장되었으나, <span class=\"text-cyan-300 font-semibold\">메모리 HBM 소부장 테마</span>의 펀더멘탈은 유효합니다.",
          "종합 반도체 제조 대형주(삼성전자) 대비 투자 효율성과 마진율이 돋보이는 중소형 <span class=\"text-cyan-300 font-semibold\">하드웨어 공급망 리더</span>들로 스마트 머니가 유입되고 있습니다.",
          "미수 반대매매로 인한 장 초반 기계적 투매 이후, 기관의 실적 우량 소부장 바닥권 순환 매수 유입세가 확인됩니다."
        ],
        "data_points": [
          "코스피 지수 4.5% 급락한 7,730선 마감 (외국인·기관 5.8조 원 순매도)",
          "PSK홀딩스 11% 상승, 유진테크 및 테스 등 장비주 상대적 강세 마감",
          "원/달러 환율 1,525원대 돌파로 파생상품 헷지 거래량 급증"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "대형주 조정기에 견고한 이익 성장 기반의 반도체 소부장 대장주들로의 수급 이동이 확인되어 하이엔드 후공정 패키징 장비 투자의 신뢰성을 높여줍니다.",
        "key_companies": [
          "PSK홀딩스(037950)",
          "유진테크(084370)",
          "테스(095610)",
          "삼성전자(005930)",
          "SK하이닉스(000660)"
        ],
        "insight": "삼성전자와 SK하이닉스가 옵션 만기 변동성에 묶인 사이, 투자자들은 <span class=\"text-cyan-300 font-semibold\">HBM 후공정(Reflow, 세정 등) 장비 시장</span> 내 독점적 기술을 가진 강소기업들로 대피했습니다. 대형주 조정은 중소형 실적주들의 저가 매력을 부각시키는 효과가 있습니다.",
        "action_point": "대형주 투매에 동참하기보다 HBM 양산 확대에 따라 실적이 직접 급증하는 <span class=\"text-cyan-300 font-semibold\">글로벌 특허 장비 공급사</span>들의 기술적 지지선을 파악하고 분할 매수 관점으로 매집을 계속해야 합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.6
      }
    }
  },
  "W39mjKPd0LA": {
    "topic": "robot",
    "content": {
      "video": {
        "id": "W39mjKPd0LA",
        "title": "현대차 엔비디아 새만금 AI밸리의 정체?",
        "published": "2026-06-10T11:00:16+00:00",
        "channel_name": "엔지니어TV",
        "url": "https://www.youtube.com/watch?v=W39mjKPd0LA",
        "thumbnail": "https://img.youtube.com/vi/W39mjKPd0LA/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 엔비디아 젠슨 황 CEO가 한국 방문 중 현대차그룹 정의선 회장과 1시간 비공개 단독 회동을 갖고 <span class=\"text-cyan-300 font-semibold\">모빌리티, 로보틱스, AI 공장</span> 전략을 논의했습니다.\n2. 양사는 보스턴 다이내믹스의 휴머노이드 아틀라스(Atlas) 상용화와 관련해 제조 공장에 로봇을 대량 배치하는 <span class=\"text-cyan-300 font-semibold\">피지컬 AI(Physical AI)</span> 실현 방안을 주요 의제로 다뤘습니다.\n3. 엔비디아는 한국 새만금을 'AI Valley'로 지칭하며, 친환경 에너지 기반의 초대형 AI 데이터 센터 및 스마트 팩토리 클러스터 구축 가능성을 시사했습니다.",
        "key_claims": [
          "엔비디아가 현대차와 밀착하는 본질은 자율주행 차량을 넘어, 로봇과 공장 자체가 AI로 학습하고 구동되는 <span class=\"text-cyan-300 font-semibold\">피지컬 AI 로봇 플랫폼 표준화</span>를 장악하려는 목적입니다.",
          "보스턴 다이내믹스의 휴머노이드 로봇 상용화 시점이 임박했으며, 현대차의 자동차 생산 라인이 엔비디아 플랫폼의 최대 <span class=\"text-cyan-300 font-semibold\">실증 공장(AI Factory)</span>이 될 것입니다.",
          "새만금 AI 밸리 구상은 전력 소모가 극심한 데이터 센터 문제를 비중국 아시아 친환경 에너지 거점 구축을 통해 극복하려는 전략입니다."
        ],
        "data_points": [
          "엔비디아 젠슨 황 CEO 및 현대차그룹 정의선 회장 1시간 비공개 회의 진행",
          "현대차 산하 로봇 전문 자회사 '보스턴 다이내믹스'(Boston Dynamics)의 차세대 휴머노이드 아틀라스 상용화 일정 연동",
          "한국 새만금 'AI 밸리' 데이터 센터 및 AI 팩토리 파트너십 구상 언급"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "글로벌 AI 1위 엔비디아와 모빌리티·로봇 강자 현대차의 비공개 기술 파트너십은 차세대 피지컬 AI 및 휴머노이드 로봇 산업화 속도를 획기적으로 앞당길 메가톤급 호재입니다.",
        "key_companies": [
          "현대자동차(005380)",
          "엔비디아(NVDA)"
        ],
        "insight": "자율주행과 로봇 제조는 소프트웨어 중심의 AI가 현실 세계 물리 법칙과 결합하는 <span class=\"text-cyan-300 font-semibold\">피지컬 AI 혁명</span>의 양대 축입니다. 엔비디아는 현대차의 글로벌 완성차 공장을 하드웨어 실증 베이스로 삼고, 현대차는 엔비디아의 시뮬레이터(Omniverse)와 칩을 통해 로봇 상용화 경제성을 빠르게 극대화할 것입니다.",
        "action_point": "현대차-엔비디아 로봇 동맹의 실질적 기술 주도권을 쥔 <span class=\"text-cyan-300 font-semibold\">보스턴 다이내믹스 공급망 관련 정밀 기어 및 액추에이터 부품사</span>와 새만금 전력 클러스터에 수혜를 받는 전력망 인프라 대장주의 장기 성장 가능성에 적극 베팅해야 합니다."
      },
      "classification": {
        "primary_topic": "robot",
        "relevance_score": 9.8
      }
    }
  },
  "_2UbO3ketmM": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "_2UbO3ketmM",
        "title": "슈마컴, 70억달러 증자 발표에 주가 하락ㅣTSMC, 5월 매출 전년比 30% 증가ㅣ中정부, 25년 이후 월간 최대 규모 금 매입ㅣ홍키자의 매일뉴욕",
        "published": "2026-06-10T10:00:14+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=_2UbO3ketmM",
        "thumbnail": "https://img.youtube.com/vi/_2UbO3ketmM/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 뉴욕 증시는 3년 만에 최고를 기록한 5월 CPI(4.2%) 및 트럼프발 이란 긴장 고조의 영향으로 반도체 등 기술주 위주의 단기 조정을 겪었습니다.\n2. 슈퍼마이크로컴퓨터(SMCI)가 AI 서버 인프라 투자를 위한 70억 달러 규모 자금 조달(지분 희석 우려)을 기습 발표하며 주가가 크게 하락했습니다.\n3. TSMC는 전년 대비 30% 증가한 월간 호실적을 발표했으며, 중국 인민은행이 2025년 이후 최대 규모의 월간 금 매입을 단행해 자산 안전 헷징을 이어갔습니다.",
        "key_claims": [
          "근원 인플레이션의 안정 조짐에도 불구하고, 이란 공습에 따른 <span class=\"text-amber-300 font-bold\">원유 유가 불안</span> 및 지정학적 리스크가 성장주 투자 투심에 직격탄을 날리고 있습니다.",
          "슈퍼마이크로의 70억 달러 자금 조달은 AI 폭증 수요를 감당하기 위한 설비 자금 필요성을 보여주지만, 단기적으로 <span class=\"text-rose-400 font-medium\">지분 가치 희석 리스크</span>가 우세합니다.",
          "중국 정부의 역사적 규모의 금 매입은 서방과의 갈등(지정학 패권) 장기화를 염두에 둔 달러 외 <span class=\"text-violet-300 font-medium\">대안 안전자산 다변화 전략</span>의 일환입니다."
        ],
        "data_points": [
          "5월 소비자물가지수(CPI) 전년 대비 4.2% 상승 (3년 만에 최고치)",
          "슈퍼마이크로컴퓨터(SMCI) 70억 달러 규모의 신규 자금 조달 발표 (50억 달러 유상증자, 20억 달러 채권 등 포함)",
          "TSMC 5월 매출 전년 동기 대비 30% 급성장 기록",
          "중국 인민은행 2025년 이후 최대 월간 규모의 골드(금) 현물 매입 단행",
          "국제 유가 WTI 89달러, 브렌트유 92달러선 돌파"
        ],
        "signal": "bearish",
        "signal_confidence": "medium",
        "signal_reason": "AI 대표 인프라 기업(SMCI)의 자금 희석 악재와 환율·유가 등 매크로 불안 요소가 맞물려 단기적인 뉴욕 증시 기술주 조정 압력을 가속화하고 있습니다.",
        "key_companies": [
          "슈퍼마이크로컴퓨터(SMCI)",
          "TSMC(TSM)",
          "엔비디아(NVDA)",
          "마이크론(MU)"
        ],
        "insight": "초대형 증자 소식은 단기 주가 폭락을 유도하지만, 확보한 70억 달러가 전액 AI 액체 냉각 서버 설비 증설에 투입된다는 점은 <span class=\"text-cyan-300 font-semibold\">서버 인프라 장기 수요</span>가 여전히 확실함을 입증합니다. 중국의 금 매집 역시 지정학 긴장에 의한 자산 시장 리스크 헷지 트렌드를 강화합니다.",
        "action_point": "유상증자 충격으로 낙폭이 심화된 AI 하드웨어 장비주는 단기 지지선 확인 시점까지 관망을 늘리되, 실적 성장이 보증된 <span class=\"text-cyan-300 font-semibold\">파운드리 대장주(TSMC) 및 금 현물 자산</span>에 대해 분할 분산 적립 투자를 시작할 타이밍입니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.3
      }
    }
  }
}

# Write results and clean up pending
pending_dir = Path("data/pending")
analyzed_base_dir = Path("data/analyzed")

for video_id, info in batch_data.items():
    topic = info["topic"]
    content = info["content"]
    
    # Write to analyzed path
    topic_dir = analyzed_base_dir / topic
    topic_dir.mkdir(parents=True, exist_ok=True)
    analyzed_path = topic_dir / f"{video_id}.json"
    analyzed_path.write_text(json.dumps(content, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved: {analyzed_path}")
    
    # Delete from pending
    pending_path = pending_dir / f"{video_id}.json"
    if pending_path.exists():
        pending_path.unlink()
        print(f"Deleted pending: {pending_path}")
