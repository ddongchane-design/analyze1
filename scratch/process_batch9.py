import json
from pathlib import Path

# Define the analyzed data for Batch 9
batch_data = {
  "TyMcmTgpvJo": {
    "topic": "crypto",
    "content": {
      "video": {
        "id": "TyMcmTgpvJo",
        "title": "비트코인 0.21개만 있으면 은퇴 후 당신의 노후 준비가 끝납니다ㅣ이장우·박종한·강승구 [3부]",
        "published": "2026-06-11T03:00:00+00:00",
        "channel_name": "이호석아카데미",
        "url": "https://www.youtube.com/watch?v=TyMcmTgpvJo",
        "thumbnail": "https://img.youtube.com/vi/TyMcmTgpvJo/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 15년 뒤 은퇴 자금 16억 원을 만들기 위해 주식/저축은 매달 300~400만 원의 큰 자금이 필요하지만, 비트코인(연 25% 성장 가정)은 매달 <span class=\"text-cyan-300 font-semibold\">80만 원 정립식 저축</span>으로 달성 가능합니다.\n2. 전통 은퇴 설계 공식인 4% 룰 대신 연평균 수익률이 높은 비트코인에는 <span class=\"text-cyan-300 font-semibold\">8% 인출 룰</span>을 적용하여 자본 효율성을 극대화하는 노후 설계가 제시되었습니다.\n3. AI 대두로 전통 일자리가 위협받는 시대에 비트코인은 인플레이션을 상쇄할 <span class=\"text-cyan-300 font-semibold\">국가 밖 중립적 가치 저축 수단</span>으로 작동합니다.",
        "key_claims": [
          "지정학적 리스크가 고조되는 각자도생의 시대에 개인의 자산을 지킬 탈중앙화된 <span class=\"text-cyan-300 font-semibold\">중립적 안전자산</span>의 포트폴리오 편입은 필수적입니다.",
          "미래가치 산정 모델인 파워로우(Power-law) 경로에 의하면 비트코인은 성장 속도가 완화되더라도 2035년경 <span class=\"text-cyan-300 font-semibold\">150만 달러</span> 도달이 가능합니다.",
          "단기 투자(단타)로 포모를 느끼기보다 0.21 BTC 목표치를 정립식 구매를 통해 <span class=\"text-amber-300 font-bold\">기계적으로 축적하는 전략</span>이 유효합니다."
        ],
        "data_points": [
          "은퇴 노후 월평균 희망 생활비 297만 원, 15년 뒤 인플레이션(연 4%) 감안 시 월 520만 원 필요",
          "30년 자금 고갈 방지를 위해 은퇴 시점 목표 자산 16억 원 필요",
          "15년 동안 16억 확보를 위한 저축액: 국내주식 월 460만 원, S&P500 월 330만 원, 비트코인(연 25% 성장) 월 80만 원",
          "보수적 비트코인 성장 모델 기준 15년 뒤 필요한 비트코인 수량 0.21개 (8% 인출 적용)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "전통 화폐의 가치 하락(인플레이션) 리스크를 장기 방어할 희소자산으로서 비트코인의 보편적 가치가 부각되며, 개인의 장기 정립식 저축 전략이 실천 가능합니다.",
        "key_companies": [
          "블랙록",
          "모건스탠리"
        ],
        "insight": "비트코인을 투기 수단이 아닌 장기 노후 연금 대안으로 재정의하는 것은 자산 관리 패러다임의 중대한 변곡점입니다. 특히 일반 대중의 발행량 한계 인지율(6%)과 기관의 401K 퇴직연금 편입 확대 추세는 장기적 공급 부족 가치를 보장합니다.",
        "action_point": "시세 급락에 흔들려 투매하기보다, 은퇴 시점 0.21 BTC 보유를 최종 목표로 삼아 소액 정립식 자동 매수 프로그램을 활용해 꾸준히 모아가는 정석 투자가 필요합니다."
      },
      "classification": {
        "primary_topic": "crypto",
        "relevance_score": 9.4
      }
    }
  },
  "UUMUD5VEmJ8": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "UUMUD5VEmJ8",
        "title": "스페이스X 상장이 한국 증시에 미칠 영향 | 한유건 하나증권 리서치센터 팀장 [더블 업]",
        "published": "2026-06-11T03:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=UUMUD5VEmJ8",
        "thumbnail": "https://img.youtube.com/vi/UUMUD5VEmJ8/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 시가총액 1.75조 달러(2,670조 원) 규모의 초대형 <span class=\"text-cyan-300 font-semibold\">스페이스X(SpaceX)</span>가 미국 상장에 돌입하며 역대급 기업 공개 신기록을 경신 중입니다.\n2. 상장 초기 유통 물량이 4.2% 수준에 불과하고 락업 해제도 6개월간 순차 분산되므로 즉각적인 수급 고갈 우려는 낮으나, <span class=\"text-violet-300 font-medium\">7월 7일 나스닥 100 패스트트랙 편입</span> 시기 리밸런싱 블랙홀 압박이 예상됩니다.\n3. 스페이스X 상장은 국내 우주 및 HBM 특수 엔진 부품 기업들에 <span class=\"text-cyan-300 font-semibold\">낙수 효과(CapEx 조달 수혜)</span>를 유발하며 장기적 호재로 작동할 것입니다.",
        "key_claims": [
          "스페이스X의 상장 초기 유통 물량 비중은 4.2% 수준으로 페이스북(15.4%) 등 과거 대형 IPO에 비해 <span class=\"text-amber-300 font-bold\">오버행 부담이 제한적</span>입니다.",
          "글로벌 지수(나스닥 100 등) 조기 편입에 따른 패시브 자금 쏠림은 7월 7일 전후로 국내 정보통신 및 대형 기술주의 <span class=\"text-rose-400 font-medium\">일시적 수급 이탈</span>을 가져올 수 있습니다.",
          "스페이스X에 직접 부품을 공급하는 국내 특수 철강, 알루미늄, HBM 엔진 소재 제조 기업들의 <span class=\"text-cyan-300 font-semibold\">공급망 가치 재평가</span>가 시작될 것입니다."
        ],
        "data_points": [
          "스페이스X 기업가치 1.75조~2조 달러 (원화 2,670조 원 수준, 삼성전자/SK하이닉스 시총 규모 상회)",
          "상장 유통 가능 물량: 전체 131억 주 중 약 4.2% 수준 극소 배정",
          "나스닥 100 지수 패스트트랙 편입 예정일: 2026년 7월 7일 (삼성전자 잠정 실적 발표일과 근접)",
          "올해 스페이스X 예상 매출 중 스타링크 부문 비중 60~70% 차지 (스타링크 가입자 작년 대비 2배 성장)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "대규모 상장 조달 자금이 스타링크 및 스타십 투자 확대로 연결되며, 글로벌 우주 공급망에 참여한 국내 특수 부품 제조사와 지분 투자 금융사들의 가치 상승을 자극합니다.",
        "key_companies": [
          "스페이스X",
          "세아베스틸지주(001430)",
          "알맥(365120)",
          "미래에셋증권(006800)"
        ],
        "insight": "스페이스X 상장에 따른 글로벌 시장의 시총 지각 변동은 단기 수급 이탈 공포를 자극하지만, 본질은 우주 인터넷(스타링크)과 민간 발사체 인프라 시장의 무제한적 팽창입니다. 국내 증시 수급 역시 대규모 패시브 리밸런싱이 끝나는 7월 중순 이후 공급망 낙수 효과를 향해 빠르게 안정을 찾을 것입니다.",
        "action_point": "수급 노이즈로 주가가 흔들리는 스페이스X 직접 공급망 밸류체인(소재 공급사) 및 지분 보유 투자사에 대해 7월 초 리밸런싱 조정 구간을 <span class=\"text-cyan-300 font-semibold\">매수 진입 기회</span>로 삼아야 합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.5
      }
    }
  },
  "WLZzm6hq5IE": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "WLZzm6hq5IE",
        "title": "지금은 급하게 던질 때가 아닙니다 | 장우진 작가 [더블 체크]",
        "published": "2026-06-11T04:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=WLZzm6hq5IE",
        "thumbnail": "https://img.youtube.com/vi/WLZzm6hq5IE/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 극단적 매도 사이드카와 지수 하락은 선물/옵션 만기 수급 꼬임과 스페이스X 상장 대기 현상이 맞물린 <span class=\"text-rose-400 font-medium\">일시적 수급 공포증</span>에 불과합니다.\n2. 미국 내 소비자 물가 통계 신뢰성 논란(통계 조작설 및 체감 물가 갭)과 금리 리스크가 투자 심리를 억누르고 있으나, 기업들의 실질 펀더멘탈은 견고합니다.\n3. 코스피/코스닥의 하락을 섣불리 손절하기보다는, 지수 하방 지지선을 확인하고 <span class=\"text-cyan-300 font-semibold\">기계적 분할 매수</span> 관점을 고수해야 하는 시점입니다.",
        "key_claims": [
          "미국의 공식 물가 지표가 실제 개인의 체감 인플레이션과 지나친 괴리를 보여 <span class=\"text-rose-400 font-medium\">시장 내 통계 부정설</span>과 금리 불안 심리가 확대되었습니다.",
          "국내 증시는 시클리컬(경기 순환)적 성향이 강하므로 지수 고점 부근의 묻지마 장기 투자보다 <span class=\"text-amber-300 font-bold\">철저한 분할 트레이딩</span> 접근이 유효합니다.",
          "미국 증시와 달리 한국 시장은 변동성이 증폭되므로 공포에 동참해 저점에서 급하게 주식을 던지는 것은 실책입니다."
        ],
        "data_points": [
          "선물 만기일 수급 변동성으로 매도 사이드카 발동 및 선물 5% 하락 노이즈 발생",
          "5월 미국 CPI 전년 대비 4.2% 발표에 대한 미국 현지 체감 괴리 지적 지속"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "체감 물가 불안과 옵션 만기일 기계적 매도로 단기 조정 강도가 세지만, 펀더멘탈 버블 붕괴 시그널이 부재하므로 저가 대기 매수세가 받쳐주는 중립 구간입니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)"
        ],
        "insight": "단기 급락장은 투자자들의 멘탈을 붕괴시키지만, 한국 반도체 대형주들의 실적과 수출 데이터는 역사적 최고점을 예고하고 있습니다. 펀더멘탈 지지 없는 공포성 매도는 수급이 안정을 찾는 즉시 빠른 V자 반등을 초래하는 경우가 많습니다.",
        "action_point": "보유 주식을 섣불리 저점에서 매도하지 말고 홀딩하며, 2024년 바닥에서 보여주었던 기계적 매수 평단을 유지하되, 고점 매수는 지양해야 합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.1
      }
    }
  },
  "y7wUcmIh-aw": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "y7wUcmIh-aw",
        "title": "변동성 큰 시장, 언제 마무리될까? '창과 방패' 전략은 이렇게!_26.06.11. | 박현지, 여도은, 허재무 [아침N투자]",
        "published": "2026-06-11T04:30:00+00:00",
        "channel_name": "아침N투자",
        "url": "https://www.youtube.com/watch?v=y7wUcmIh-aw",
        "thumbnail": "https://img.youtube.com/vi/y7wUcmIh-aw/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 6월 옵션 만기일(네 마녀의 날) 변동성과 이란 공습 지정학적 긴장 속에서도, 6월 1~10일 수출입 데이터가 <span class=\"text-cyan-300 font-semibold\">역대 최고치를 경신</span>하며 국내 반도체주의 강한 반등세를 견인했습니다.\n2. 금리 동결 논쟁 및 유가 불안 리스크가 여전하므로 투자자들은 자산의 과밀 투자를 피하고, 이익 실현과 현금 유연성을 적절히 믹스하는 <span class=\"text-amber-300 font-bold\">창과 방패 전략</span>을 취해야 합니다.\n3. 단기 차익 실현 욕구가 강한 장세이므로 하반기 실적 가시성이 뚜렷한 유통(백화점), 수출 화장품, 비만 치료제 등 <span class=\"text-cyan-300 font-semibold\">실적 개선 수남매 테마</span>에 포커스를 맞춰야 합니다.",
        "key_claims": [
          "수출 데이터에서 확인된 반도체 부문의 폭발적인 성장은 시장의 피크아웃 우려를 종식시키는 <span class=\"text-cyan-300 font-semibold\">강력한 펀더멘탈 증거</span>입니다.",
          "단기 시세 급등락에 심리적으로 흔들리기보다 정해진 요일이나 조건에 맞춘 <span class=\"text-amber-300 font-bold\">기계적 정립식 분할 매수</span>가 개인의 투자 멘탈 관리에 절대적으로有利합니다.",
          "전통 IT 외에 경기 침체기에도 이익 방어 및 성장을 실현하는 유럽 명품(LVMH 등)과 비만 치료제 섹터로의 순환매 배분이 포트폴리오를 지키는 방패가 됩니다."
        ],
        "data_points": [
          "6월 1~10일 수출 데이터: 전년 대비 반도체 부문 200% 폭증 기록 (전체 수출액 약 286억 달러 기록)",
          "코스피 장중 양전 성공, SK하이닉스 4% 이상 급등하여 30만 원 선 회복 주도",
          "유럽 명품 브랜드(LVMH 등) 실적 전망치 하향 극복 및 매출 역성장 우려 극복(전년 대비 +1% 상승 기록)",
          "비만 치료제(위고비, 마운자로) 7월 미국 내 보험 급여 수혜자 확대 호재 발생"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "수출입 동향의 반도체 수치가 사상 최고를 입증하여 어닝 서프라이즈 기대감을 고조시켰고, 단기 변동성 수급이 안정되며 전방 소부장과 주도주가 동시 반등하고 있습니다.",
        "key_companies": [
          "SK하이닉스(000660)",
          "삼성전자(005930)",
          "LVMH",
          "이수페타시스(007660)",
          "주성엔지니어링(036930)"
        ],
        "insight": "옵션 만기일의 기계적 털기가 종료되는 시점과 최고조에 달한 한국 수출 호조가 겹치면서 투자 심리가 악재 중심에서 실적 중심으로 급격히 회복되었습니다. 현시점의 순환매 기조는 주도 메모리주의 과열을 분산시키는 동시에 7월 어닝 장세로 진입하기 위한 유익한 징검다리 역할을 합니다.",
        "action_point": "주가 급반등 시 추격 매수하기보다, 변동성을 방어할 주식/채권 혼합형 상품 및 <span class=\"text-cyan-300 font-semibold\">실적 가시성 유통/수출 대형주</span> 위주로 기계적 적립식 매수를 집행해야 합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.6
      }
    }
  },
  "ycIncK4a_h4": {
    "topic": "crypto",
    "content": {
      "video": {
        "id": "ycIncK4a_h4",
        "title": "비트코인 바닥 6만불이 아닙니다. 앞으로 '여기'까지는 생각하셔야 합니다ㅣ이장우·박종한·강승구 [2부]",
        "published": "2026-06-11T05:00:00+00:00",
        "channel_name": "이호석아카데미",
        "url": "https://www.youtube.com/watch?v=ycIncK4a_h4",
        "thumbnail": "https://img.youtube.com/vi/ycIncK4a_h4/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 비트코인 온체인 지표상 저평가 영역에 도달했으나, 규제 불안과 기관 매도 압력으로 61.8k(200주 이평선) 이탈 시 <span class=\"text-rose-400 font-medium\">54k 수준까지의 2차 하락 가능성</span>을 열어두어야 합니다.\n2. 반감기 직후 6개월간은 채굴 보상이 절반으로 깎여 채굴 기업들의 재무가 가장 악화되는 시기이며, 이에 대응해 채굴 기업들이 <span class=\"text-cyan-300 font-semibold\">AI 데이터센터 비즈니스로의 빠른 체질 개선</span>을 시도하고 있습니다.\n3. 시장이 구조적 약세 장으로 꺾이지 않고 상승 추세를 안정적으로 회복하기 위한 핵심 분수령 가격은 <span class=\"text-cyan-300 font-semibold\">75k 돌파</span>입니다.",
        "key_claims": [
          "온체인 MVRV 지표가 1 미만(겨울 국면)으로 떨어질 확률은 낮으나, 단기 홀더들의 원금 회수 욕구로 인해 <span class=\"text-rose-400 font-medium\">하단 지지선 확인을 위한 진통</span>이 계속되고 있습니다.",
          "아이리스 에너지 등 유연한 채굴사들은 남는 잉여 전력을 AI 연산 데이터 센터용 인프라로 유연하게 치환하여 <span class=\"text-cyan-300 font-semibold\">단위 매출 효율성</span>을 올리고 있습니다.",
          "미 의회의 스폰서 규제 합의와 이란 지정학적 긴장 조율 등 입법/지정학 리스크가 가시적으로 해소되어야 대기 자금의 본격적 유입이 가능합니다."
        ],
        "data_points": [
          "기술적 지지선: 200주 이평선 61.8k 및 전체 투자자 평균 실현 단가 54k",
          "추세 복귀 분수령 저항선: 75k 돌파 및 안착 여부",
          "반감기 직후 채굴 수량의 50% 반토막 하락에 따른 채굴 마진 축소",
          "아이리스에너지(Iris Energy), 마라톤디지털(MARA) 등 채굴사들의 AI 데이터센터 전용 공시 발표"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "장기 가치 모델은 유효하지만, 반감기 직후 채굴 마진 축소 압박과 단기 보유 매물 출회 및 54k까지의 변동성 열림에 따라 보수적 관찰이 요구됩니다.",
        "key_companies": [
          "아이리스에너지(IREN)",
          "마라톤디지털(MARA)"
        ],
        "insight": "크립토 채굴 산업의 미래는 전력 자원의 '인공지능 데이터센터(AI DC)' 인프라 전환 속도에 달렸습니다. 채굴 난이도 증가와 단가 압박 속에서 비트코인 채굴의 헷지 수단으로 AI 연산 비즈니스를 유연하게 결합하는 기업만이 생존하여 주가 상승을 주도할 것입니다.",
        "action_point": "비트코인이 61.8k를 지지하지 못하고 54k 부근으로 밀릴 때를 대비하여 유동성을 확보하고, AI 인프라 사업으로의 빠른 피봇에 성공해 이익 체력을 증명한 채굴 기업에 선별 투자해야 합니다."
      },
      "classification": {
        "primary_topic": "crypto",
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
