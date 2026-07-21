import json
from pathlib import Path

# Define the analyzed data for Batch 7
batch_data = {
  "0T5YyMoOL5o": {
    "topic": "space",
    "content": {
      "video": {
        "id": "0T5YyMoOL5o",
        "title": "2700조 원 최대 상장의 이면..국내 최초 멤피스 데이터센터에서 본 스페이스X의 현주소 | 바이아메리카 in 뉴욕",
        "published": "2026-06-11T01:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=0T5YyMoOL5o",
        "thumbnail": "https://img.youtube.com/vi/0T5YyMoOL5o/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 스페이스X는 XAI의 멤피스 <span class=\"text-cyan-300 font-semibold\">콜로서스 데이터센터</span> 및 전력 인프라 등 지상 AI 생태계를 기반으로 최대 1.8조 달러 몸값의 상장 로드쇼를 개시했습니다.\n2. 공모가는 135달러 단일 고정가로, 물량의 4배가 넘는 대규모 기관 주문이 쏠려 상장 초기 <span class=\"text-violet-300 font-medium\">수급 쏠림(블랙홀)</span> 우려가 고조되고 있습니다.\n3. 락업 해제 시점에 대한 다양한 예외 조항(비상 출구)이 존재하여 임직원과 초기 투자자들의 매도로 인한 <span class=\"text-rose-400 font-medium\">단기 주가 변동성 리스크</span>가 큽니다.",
        "key_claims": [
          "스페이스X는 단순한 로켓 발사 기업이 아니라 스타링크와 XAI, 테라 프로젝트를 엮은 <span class=\"text-cyan-300 font-semibold\">AI 인프라 사슬</span>로 기업가치를 포장하고 있습니다.",
          "6개월 내 물량 해제 예외 조항이 많아 피그마나 세레브라스처럼 <span class=\"text-rose-400 font-medium\">상장 직후 내부자 매도</span>로 인한 급락 악순환의 위험이 있습니다.",
          "다모다란 교수는 템(TAM) 산정 시 소프트웨어 시장 규모(22조 달러)를 과도하게 부풀려 <span class=\"text-rose-400 font-medium\">AI 버블의 경고 시그널</span>로 작용한다고 지적합니다."
        ],
        "data_points": [
          "스페이스X 시가총액 최소 1.8조 달러 (약 2,700조 원) 규모 전망",
          "멤피스 콜로서스 데이터센터 1호기: 22만 개 엔비디아 GPU 기반 가동 중",
          "스페이스X 공모가 135달러, 유통 물량 약 131억 주 중 4.2% 수준 공모",
          "조정 에비타(EBITDA) 작년 65억 8,400만 달러, EV/EBITDA 배수 275배 수준의 높은 멀티플",
          "앤스로픽과 월 12.5억 달러(연 150억 달러), 구글과 총 300억 달러 데이터센터 임대 계약 체결",
          "락업 예외: 주가가 공모가 대비 30% 이상 열흘 중 5일 상승 시 10% 추가 매도 가능"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "스페이스X의 2,700조 원 규모 IPO가 다가오면서 스타링크 독점력은 긍정적이나, 275배에 달하는 높은 EV/EBITDA 밸류에이션과 내부자 락업 예외 조항에 따른 오버행 우려가 팽팽합니다.",
        "key_companies": [
          "스페이스X",
          "테슬라(TSLA)",
          "구글(GOOGL)",
          "앤스로픽",
          "마이크로소프트(MSFT)"
        ],
        "insight": "일론 머스크가 스페이스X 상장을 고집하는 이유는 화성 이주 목적보다 XAI 및 600억 달러 가치의 커서(Cursor) 인수 등 막대한 지상 AI 데이터센터 인프라(콜로서스, 테라 프로젝트) 구축을 위한 자금 조달에 초점이 맞춰져 있습니다. 이는 단기적으로 시장의 자금을 빠라들이는 수급 블랙홀을 야기할 수 있습니다.",
        "action_point": "스페이스X의 지분 투자가 연계된 간접 수혜주(미래에셋증권, 세아베스틸지주 등)는 변동성을 활용한 매수 기회로 보되, 상장 직후 락업 예외 물량이 풀리는 기간(상장 후 2개월 시점) 동안은 변동성을 극히 경계해야 합니다."
      },
      "classification": {
        "primary_topic": "space",
        "relevance_score": 9.5
      }
    }
  },
  "5ApcdsPlJRk": {
    "topic": "crypto",
    "content": {
      "video": {
        "id": "5ApcdsPlJRk",
        "title": "비트코인 지금 팔려고 고민하고 계신 분들 주목. 제발 이것만이라도 확인하고 가세요ㅣ이장우·박종한·강승구 [1부]",
        "published": "2026-06-11T02:00:00+00:00",
        "channel_name": "이호석아카데미",
        "url": "https://www.youtube.com/watch?v=5ApcdsPlJRk",
        "thumbnail": "https://img.youtube.com/vi/5ApcdsPlJRk/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 비트코인은 AI 열풍에 따른 <span class=\"text-amber-300 font-bold\">자본 쏠림</span>과 규제 법안(클래리티 법안)의 단기 무산 우려 등으로 유동성이 소외되며 하락세를 겪고 있습니다.\n2. 마이크로스트레티지(MSTR)가 STRC 우선주 배당 지급 및 재무 건전성 확보를 위해 <span class=\"text-cyan-300 font-semibold\">32 BTC를 매도</span>한 것이 단기 악재로 작동했으나, 이는 시스템 붕괴가 아닌 제도화 과정의 일환입니다.\n3. 과거 루나/FTX 파산 시의 신뢰 붕괴 하락장과 달리, 현재는 미국의 준비자산 법안(비트코인 액트) 도입 준비 등 <span class=\"text-cyan-300 font-semibold\">규제 제도화의 건강한 하방 지지력</span>이 유효합니다.",
        "key_claims": [
          "AI 빅테크 성장의 블랙홀 현상으로 크립토 시장의 유동성이 일시 차단되며 가격이 <span class=\"text-rose-400 font-medium\">6만 달러 부근</span>까지 조정받았습니다.",
          "마이크로스트레티지의 첫 비트코인 매도는 신뢰 훼손이 아닌 고객 약속(배당 지급) 이행 및 레버리지 효율화를 증명하여 리스크를 해소한 것입니다.",
          "하반기로 갈수록 미국의 <span class=\"text-cyan-300 font-semibold\">스테이블코인 법안</span> 및 비트코인 액트(준비금 현대화법) 등 대형 규제 호재들이 대기 중입니다."
        ],
        "data_points": [
          "비트코인 가격 8,000만 원(원화 기준) 돌파 후 조정 국면",
          "마이크로스트레티지, STRC 우선주 배당 재원 조달 위해 32 BTC 매도",
          "미국의 비트코인 인식 조사: 85%는 인지하고 있으나, 2,100만 개 발행량 한계를 이해하는 비중은 6%에 불과",
          "마이크로스트레티지의 비트코인 총 보유량은 여전히 80만 개 이상 유지"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "마이크로스트레티지의 소규모 매도는 시장의 장기 오버행 우려를 해소하는 실뢰 지표이며, 제도권 수용(비트코인 액트 등) 법안이 하반기에 대기하고 있어 장기 하방을 지지합니다.",
        "key_companies": [
          "마이크로스트레티지(MSTR)",
          "코인베이스(COIN)"
        ],
        "insight": "비트코인이 AI와 반도체 섹터의 폭발적 성장에 유동성을 빼앗기며 겪는 단기 조정은 대기 자금이 여전히 풍부함을 감안할 때 오히려 비중 확대의 기회입니다. 특히 일반 대중의 발행량 한계에 대한 인식이 6%에 그친다는 점은 장기적 희소성 가치의 재평가 여력이 큼을 증명합니다.",
        "action_point": "단기 시세 하락에 휩쓸려 패닉셀하기보다는, 하반기 예정된 미 연방의 법안(스테이블코인법, 비트코인 준비금법) 가시화 일정을 고려하여 분할 적립식 매수를 유지하는 것이 좋습니다."
      },
      "classification": {
        "primary_topic": "crypto",
        "relevance_score": 9.3
      }
    }
  },
  "5eeAOpJPBvk": {
    "topic": "etc",
    "content": {
      "video": {
        "id": "5eeAOpJPBvk",
        "title": "살 빼도 근육은 지킨다고?…한미약품 직접 다녀왔습니다. | 조희진 하나증권 압구정금융센터 PB [더블 크루]",
        "published": "2026-06-11T03:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=5eeAOpJPBvk",
        "thumbnail": "https://img.youtube.com/vi/5eeAOpJPBvk/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 한미약품은 자체 보유한 강력한 현금 창출력(연 영업이익 약 2,000억 원)을 기반으로 외부 수급 없이 R&D 비용을 직접 충당하는 <span class=\"text-cyan-300 font-semibold\">견고한 재무 구조</span>를 갖췄습니다.\n2. 4분기에 아시아인 체질 및 췌장 특성에 맞춰 부작용을 최소화한 한국인 맞춤형 <span class=\"text-cyan-300 font-semibold\">비만 치료제(주 1회 주사제)</span>를 국내 출시할 예정입니다.\n3. 비만 치료 시 근육 손실 문제를 해결할 수 있는 '근육 보존 치료제'와 '삼중작용제' 파이프라인의 임상이 진행 중으로 하반기 글로벌 라이선스 아웃(LO)이 기대됩니다.",
        "key_claims": [
          "한미약품은 연내 1건 이상의 대형 기술 수출(LO) 약속을 이행하기 위해 신뢰성 높은 임상 데이터를 확보해 나가고 있습니다.",
          "4분기에 출시될 국내 비만 신약은 글로벌 빅테크 약물 대비 아시아인의 인슐린 분비 능력과 췌장 특징에 적합하게 튜닝되어 <span class=\"text-rose-400 font-medium\">부작용 우려를 낮췄습니다</span>.",
          "경구형(먹는) 비만 치료제는 궁극적인 방향이지만, 현재는 흡수율과 생체이용률 면에서 <span class=\"text-cyan-300 font-semibold\">주사제형의 효율성</span>이 더 보편적입니다."
        ],
        "data_points": [
          "한미약품의 연간 영업이익 규모 약 2,000억 원 수준 (우수한 R&D 자금 조달력 보유)",
          "한국인 맞춤형 비만 치료제 국내 출시 목표 시점: 2026년 4분기",
          "비만 치료 파이프라인: 삼중작용제(LA-Triple) 및 근육 보존제 임상 진행 중"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "현금 창출이 불가능한 일반 바이오 스타트업과 달리 우량한 영업이익으로 R&D를 독자 집행하며 하반기 비만 파이프라인의 글로벌 라이선스 아웃(LO) 가능성이 높아 모멘텀이 견조합니다.",
        "key_companies": [
          "한미약품(128940)",
          "한미사이언스(008930)"
        ],
        "insight": "비만 치료제 시장의 패러다임이 단순한 체중 감량에서 '근육 보존 및 삼중작용'으로 진화하는 가운데, 한미약품이 보유한 퍼스트인클래스(First-in-class) 물질들은 글로벌 빅파마(일라이릴리, 노보노디스크 등)의 강력한 러브콜을 이끌어 낼 핵심 자산이 될 것입니다.",
        "action_point": "바이오 섹터 내 재무 리스크가 없는 대형 우량 바이오주 위주로 비중을 확대하되, 하반기 4분기 비만 신약 출시 및 기술 수출 가시성 일정에 주목하여 대응하는 것이 바람직합니다."
      },
      "classification": {
        "primary_topic": "etc",
        "relevance_score": 9.0
      }
    }
  },
  "bVbctmrmIDk": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "bVbctmrmIDk",
        "title": "[26.06.11 오전 방송 전체보기] 전쟁·물가 우려 속 뉴욕증시 하락 마감",
        "published": "2026-06-11T00:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=bVbctmrmIDk",
        "thumbnail": "https://img.youtube.com/vi/bVbctmrmIDk/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 뉴욕 증시는 지정학적 전쟁 긴장 지속과 <span class=\"text-amber-300 font-bold\">물가 인상 우려</span>가 겹치며 하락세로 마감했으나, 장중 낙폭을 줄이는 변동성 장세를 보였습니다.\n2. 매크로 불확실성에도 불구하고 국내 반도체(삼성전자, SK하이닉스)는 단기 차익 매물을 이겨내고 외국인 수급이 유입되며 <span class=\"text-cyan-300 font-semibold\">하방을 지지</span>하고 있습니다.\n3. 6월 옵션 만기 주간과 겹치며 시장의 일시적 <span class=\"text-rose-400 font-medium\">유동성 변동성</span>이 극대화되고 있지만 중장기적 기초체력은 훼손되지 않았습니다.",
        "key_claims": [
          "지정학적 우려와 유가 변동이 매크로 심리를 압박하고 있지만, 실질적인 기업들의 이익 전망치는 견조하게 상향 조정되고 있습니다.",
          "환율 상승 압박(1,540원대)이 수출 대기업들의 가격 경쟁력과 어닝 기대를 자극하여 주가지수의 <span class=\"text-cyan-300 font-semibold\">극단적인 폭락을 방어</span>하고 있습니다.",
          "단기 지수 하락은 공포로 인한 반대매매나 패닉셀을 유도하지만, 하반기 어닝 시즌 진입 시 <span class=\"text-amber-300 font-bold\">실적 장세</span>로 회복될 것입니다."
        ],
        "data_points": [
          "코스피 변동성 하락 후 코스닥 낙폭 회복 양전 흐름",
          "원/달러 환율 1,540원선 근접 수준 유지",
          "SK하이닉스 등 대형 반도체주 장중 반등(양전) 전환 성공"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "단기 거시경제(전쟁, 유가) 불안과 환율 급변동으로 리스크 경계 심리가 팽팽하지만, 반도체 및 주주환원 대형주 중심으로 하방 지지력이 증명되어 지수의 하방 압력은 제한적입니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)"
        ],
        "insight": "뉴욕 증시의 하락과 환율 급등은 국내 시장에 외인 자금 이탈 우려를 유발하지만, 고환율 수혜를 받는 수출 전방 산업(반도체, 자동차)의 영업이익 추정치가 오르는 역설적인 헷지(Hedge) 구도를 연출하고 있습니다.",
        "action_point": "시장 전반의 단기 지수 밴드 하단 이탈 시 패닉셀하기보다, 호실적이 기대되는 대형 반도체 기업 위주로의 저가 분할 매수 대응이 유효합니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.2
      }
    }
  },
  "jlKh26fxC3Q": {
    "topic": "tech",
    "content": {
      "video": {
        "id": "jlKh26fxC3Q",
        "title": "반도체 권위자 : 쇼티지 절대 안 끝난다, 왜 겁 먹어요? | 김록호 & 빈센트 & 편아나 [더블 업]",
        "published": "2026-06-11T01:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=jlKh26fxC3Q",
        "thumbnail": "https://img.youtube.com/vi/jlKh26fxC3Q/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 반도체 권위자 김록호 위원은 현재 반도체 업황은 대단히 안전하며, 매크로 변동성으로 인한 주가 조정은 <span class=\"text-cyan-300 font-semibold\">비중 확대 기회</span>라고 강조했습니다.\n2. 모바일 기기에 사용되는 <span class=\"text-cyan-300 font-semibold\">LPDDR 쇼티지(공급 부족)</span> 현상은 연내 해결되지 않아 강력한 단가 강세를 이어갈 것입니다.\n3. LPDDR 가격 상승은 D램 전체 블렌디드 ASP(평균판매단가) 상승을 견인하여 삼성전자 및 SK하이닉스의 하반기 실적 전망치를 계속 끌어올릴 것입니다.",
        "key_claims": [
          "매크로 이슈에 의한 메모리 반도체 대형주 주가 조정은 펀더멘탈 훼손이 아니므로 적극적인 <span class=\"text-cyan-300 font-semibold\">매수 전략</span>이 필요합니다.",
          "AI 온디바이스 생태계 확장으로 기존 서버용 HBM뿐 아니라 모바일용 고성능 LPDDR 수요가 폭발해 <span class=\"text-rose-400 font-medium\">쇼티지 장기화</span>가 심화되고 있습니다.",
          "3분기 잠정 실적 발표 시점(10월 초)까지는 반도체 실적 상향이 확실하므로 단기 노이즈에 동요하지 말아야 합니다."
        ],
        "data_points": [
          "LPDDR 쇼티지 심화 및 모바일 D램 단가 강세 기조 지속",
          "삼성전자 및 SK하이닉스 3분기 실적 전망치 상향 트렌드 유지",
          "D램 혼합 평균 판매 단가(ASP) 상승 수치 견조"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "모바일 AIPC 및 AI 스마트폰 수요에 의한 LPDDR 쇼티지가 메모리 반도체 기업들의 ASP를 구조적으로 올리는 구간이며, 실적 펀더멘탈이 극도로 우수합니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)"
        ],
        "insight": "HBM에만 집중되던 AI 반도체 수혜가 온디바이스 AI 활성화에 따라 모바일 저전력 메모리(LPDDR) 시장으로 빠르게 전이되고 있습니다. 이는 메모리 제조사의 가파른 마진 믹스 개선 및 실적 체력 향상으로 직결되며 반도체 피크아웃 우려를 완벽히 종식시키는 계기가 될 것입니다.",
        "action_point": "매크로 변동성으로 인해 삼성전자와 SK하이닉스 주가가 조정을 받을 때마다 적극적으로 비중을 확대하고, 최소한 3분기 잠정 실적이 발표되는 10월 초까지는 반도체 섹터의 롱(Long) 관점을 유지해야 합니다."
      },
      "classification": {
        "primary_topic": "tech",
        "relevance_score": 9.6
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
