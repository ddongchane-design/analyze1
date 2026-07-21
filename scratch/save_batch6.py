import json
from pathlib import Path

batch6_data = {
  "BDvajI4kTqQ": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "BDvajI4kTqQ",
        "title": "분산투자의 함정, 개인투자자가 놓치는 핵심은? | 박병창 MP파트너스 대표 [마켓 인사이드]",
        "published": "2026-06-17T00:32:47+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=BDvajI4kTqQ",
        "thumbnail": "https://img.youtube.com/vi/BDvajI4kTqQ/hqdefault.jpg"
      },
      "analysis": {
        "summary": "미국의 <span class=\"text-cyan-300 font-semibold\">스페이스X</span> 폭등에 따른 수급 쏠림으로 엔비디아, 마이크론 등 반도체 주도주가 일시 조정을 받은 가운데, 미 행정부의 항소 포기로 풍력 개발 규제가 무너지며 국내 <span class=\"text-cyan-300 font-semibold\">풍력 기자재 기업(CS윈드 등)</span>들이 무더기 상한가를 기록함. 또한 일본 BOJ의 금리 인상(1%)과 한국은행의 추가 긴축 가능성이 부각되나 채권 시장은 안정세를 보이고 있음.",
        "key_claims": [
          "스페이스X의 단기 폭등(시총 2.9조 달러)이 패시브 수급을 흡수하여 기존 M7 빅테크와 반도체 섹터의 차익 실현을 자극함.",
          "미국 법원의 풍력 규제 위헌 판결 및 행정부의 항소 포기로 신재생에너지 정책 리스크가 제거되며 풍력주가 부활함.",
          "한-일 양국 중앙은행의 긴축 움직임(BOJ 1%로 인상, 한은 추가 인상 가능성) 속에서 단기 금리 상승 영향은 이미 시장에 선반영됨."
        ],
        "data_points": [
          "필라델피아 반도체 지수 하락률: 5.7% (마이크론 -6%, 샌디스크 -5.5% 등 동반 하락)",
          "스페이스X 최고 주가 및 시총: 주당 225달러 (시총 2.9조 달러 도달)",
          "일본 BOJ 기준금리 도달 수준: 1.0% (1995년 이후 약 30년 만에 최고치)"
        ],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "풍력 규제 취소와 금리 우려 완화는 긍정적이나, <span class=\"text-rose-400 font-medium\">스페이스X의 수급 블랙홀 효과</span>로 반도체 소부장 및 기존 주도주들의 변동성이 확대되는 구간이기 때문임.",
        "key_companies": ["스페이스X", "CS윈드(112610)", "마이크론(MU)", "엔비디아(NVDA)"],
        "insight": "개인 투자자의 무분별한 포트폴리오 다변화는 오히려 수익률을 갉아먹는 함정이 될 수 있으며, 시장 주도권이 명확한 섹터(AI 메모리)의 비중을 지키되 정책 리스크가 해소된 풍력 등 특정 순환매 섹터를 선별적으로 편입하는 스페이스 분산이 요구됨.",
        "action_point": "스페이스X의 쏠림으로 인해 하락한 <span class=\"text-cyan-300 font-semibold\">마이크론 등 메모리 반도체 주도주</span>는 적극적인 비중 확대 기회이며, 정책 불확실성이 걷힌 <span class=\"text-cyan-300 font-semibold\">풍력 및 원전주</span>를 바스켓으로 일부 분산 투자하는 전략이 유효함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["economy", "energy"],
        "tags": ["분산투자의함정", "스페이스X수급", "풍력관련주", "금리인상우려"]
      }
    }
  },
  "vR_73S_rDGk": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "vR_73S_rDGk",
        "title": "[빈난새의 개장전요것만-6월16일] 미-이란 합의 이후 전망 | 퀄컴 텐스토렌트 인수 논의 | 스페이스X 시총 5위 | 역시 비둘기 BOJ | 시게이트 웨스턴디지털 GM 엑손모빌",
        "published": "2026-06-16T14:37:33+00:00",
        "channel_name": "한경 글로벌마켓",
        "url": "https://www.youtube.com/watch?v=vR_73S_rDGk",
        "thumbnail": "https://img.youtube.com/vi/vR_73S_rDGk/hqdefault.jpg"
      },
      "analysis": {
        "summary": "미국과 이란의 종전 타결로 <span class=\"text-violet-300 font-medium\">유가가 80달러선 아래로 급락</span>하며 금리 불안이 해소된 가운데, 모바일 AP 강자 <span class=\"text-cyan-300 font-semibold\">퀄컴</span>이 AI 칩 설계 스타트업 <span class=\"text-cyan-300 font-semibold\">텐스토렌트</span> 인수를 논의한다는 빅딜 소식이 전해짐. 또한 일본 BOJ의 긴축에도 불구하고 시장 개입 약속에 따라 엔화는 여전히 160엔대 약세를 기록함.",
        "key_claims": [
          "미-이란 합의에 따른 호르무즈 해협 통행 재개로 에너지발 공급망 병목이 완화되어 국채 금리가 하락 안정화됨.",
          "퀄컴의 텐스토렌트 인수 시도는 온디바이스 AI에서 클라우드/서버용 AI 가속기 시장으로 비즈니스를 리레이팅하겠다는 의도임.",
          "스페이스X의 2.1조 달러 돌파는 대형 자금이 상장 유니콘의 AI 가치(xAI 연산력 결합)에 부여하는 강력한 기대 멀티플을 증명함."
        ],
        "data_points": [
          "WTI 및 브랜드유 가격: WTI 77.5달러 (브랜드유 80.5달러로 80달러선 붕괴 시도)",
          "미 10년물 국채 금리: 4.45%선으로 하향 안정화",
          "스페이스X 상장 시가총액: 2.1조 달러 돌파 (글로벌 7위 등극)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "<span class=\"text-violet-300 font-medium\">국제 유가 급락</span>이 물가 압력을 직접적으로 낮추어 매크로 금리 안정을 이끌고 있고, 퀄컴의 대형 M&A 추진 등 AI 시장의 생태계 확장 모멘텀이 견고하기 때문임.",
        "key_companies": ["퀄컴(QCOM)", "스페이스X", "GM", "텐스토렌트"],
        "insight": "퀄컴의 텐스토렌트 인수는 엔비디아가 독점하고 있는 데이터센터 칩 시장에 도전장을 던지는 행보로, 향후 NPU 설계 경쟁이 심화될 것임을 암시함. 지정학 완화로 인한 유가 하락은 제조업 및 IT 기업들의 비용 절감으로 이어져 증시 랠리의 탄탄한 기초가 됨.",
        "action_point": "유가 하락으로 수혜를 입는 <span class=\"text-cyan-300 font-semibold\">IT 빅테크</span> 및 자사주 매입으로 체력을 다진 <span class=\"text-cyan-300 font-semibold\">GM</span> 등의 비중을 확대하고, 텐스토렌트 지분을 보유하거나 협력 관계에 있는 국내 반도체 디자인하우스 및 관련 소부장 기업들의 동향을 추적할 필요가 있음."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["국제유가하락", "퀄컴인수합병", "텐스토렌트", "BOJ통화정책"]
      }
    }
  },
  "I_NcnH7sjHs": {
    "primary": "crypto",
    "data": {
      "video": {
        "id": "I_NcnH7sjHs",
        "title": "매달 80만 원씩 비트코인을 모으면, 15년 뒤 노후가 달라집니다ㅣ이장우·박종한·강승구 [풀영상]",
        "published": "2026-06-16T10:07:01+00:00",
        "channel_name": "이효석아카데미",
        "url": "https://www.youtube.com/watch?v=I_NcnH7sjHs",
        "thumbnail": "https://img.youtube.com/vi/I_NcnH7sjHs/hqdefault.jpg"
      },
      "analysis": {
        "summary": "전 세계 비트코인의 한정된 공급량(2,100만 개)에 착안해 상위 1% 자산 계층 진입을 위한 <span class=\"text-cyan-300 font-semibold\">0.21 비트코인 적립 목표</span>가 제시됨. 극심한 시장 변동성을 극복하기 위해 매달 80만 원 수준의 <span class=\"text-amber-300 font-bold\">정립식 투자(DCA)</span>를 활용, 장기적인 국가 화폐 가치 하락 및 재정 리스크에 대응하는 은퇴 전략이 입증됨.",
        "key_claims": [
          "비트코인은 2,100만 개라는 절대적 희소성을 가진 자산으로, 전 세계 인구 중 단 0.21개만 보유해도 상위 1%의 부를 확보하는 효과를 지님.",
          "변동성이 극도로 높은 자산 특성상 일시불 매수보다 매달 소액으로 꾸준히 사 모으는 정립식 매수(DCA)가 평균단가 조절에 가장 유리함.",
          "정부의 국채 발행 남발과 피아트 화폐 가치의 인위적 디플레이션 속에서, 비트코인은 국가 리스크가 배제된 중립적 개인 금고 기능을 수행함."
        ],
        "data_points": [
          "비트코인 총 발행 한도: 2,100만 개",
          "상위 1% 진입을 위한 비트코인 보유 기준량: 0.21 BTC",
          "비트세이빙 서비스 사용자 수: 약 13,000명 돌파"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "거시 경제의 재정 적자 누적과 통화 가치 절하 흐름 속에서 <span class=\"text-cyan-300 font-semibold\">비트코인의 희소 자산 매력</span>이 장기 축적 수요에 의해 확고한 하방 지지선을 형성하고 있기 때문임.",
        "key_companies": [],
        "insight": "비트코인은 전통 금융 주식이나 채권 포트폴리오의 하락 시 보조적인 대체 자산으로서 가치가 있으며, 단기 트레이딩 대상이 아닌 화폐 가치 절하에 대비해 장기 보유(HODL) 및 DCA로 축적해야 할 자산 범주임.",
        "action_point": "투자 포트폴리오의 2~5% 수준에서 매달 일정한 현금 흐름을 활용해 <span class=\"text-cyan-300 font-semibold\">비트코인을 정립식으로 매수</span>하는 시스템을 구축하고, 단기 변동성 급락 시 동요하지 않고 10년 이상의 장기 호흡으로 보유하는 전략을 가져가야 함."
      },
      "classification": {
        "primary_topic": "crypto",
        "secondary_topics": ["stock", "economy"],
        "tags": ["비트코인DCA", "은퇴준비", "희소자산", "화폐가치하락"]
      }
    }
  },
  "q-zONq9JzNA": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "q-zONq9JzNA",
        "title": "반도체만 담기 불안한 장세…조선·소비재로 분산해야 할 타이밍ㅣ명민준, 최효은, 황유현 [주린이 구조대]",
        "published": "2026-06-16T14:00:32+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=q-zONq9JzNA",
        "thumbnail": "https://img.youtube.com/vi/q-zONq9JzNA/hqdefault.jpg"
      },
      "analysis": {
        "summary": "반도체 일변도의 쏠림에서 탈피해 역사적 슈퍼사이클을 맞이한 <span class=\"text-cyan-300 font-semibold\">조선 3사</span>와 트럼프 규제 리스크 해소로 급반등한 <span class=\"text-cyan-300 font-semibold\">풍력 섹터(CS윈드 등)</span>로 자금이 분산되는 순환매가 시작됨. 유가 하락 안정화 수혜를 입는 백화점 등 전통 내수 소비재도 매력적인 하방 지지를 받고 있음.",
        "key_claims": [
          "반도체 주도주의 단기 차익 실현 매물이 나오는 시점에서, 친환경 선가 상승세를 띤 조선주가 주도주 대안으로 부각됨.",
          "미 행정부의 항소 포기로 풍력 규제 소송이 일단락되어 풍력 소부장 기업들의 주주 리스크가 완전히 해소됨.",
          "유가 갤런당 4달러 붕괴에 따른 가계 소비력 회복 논리를 바탕으로 백화점 및 유통 섹터의 단기 밸류에이션 갭 메우기가 나타남."
        ],
        "data_points": [
          "미국 갤런당 휘발유 가격: 4달러 하회 (두 달 만에 최저치)",
          "조선 업계 선가 지수: 친환경선 중심의 지속적인 상승세 유지"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "반도체의 주도권이 꺾인 것이 아니라 수급이 <span class=\"text-cyan-300 font-semibold\">조선, 방산, 풍력</span> 등 호실적 자본재 및 정책 수혜 섹터로 고르게 확산되며 시장의 펀더멘탈 체력이 다변화되고 있기 때문임.",
        "key_companies": ["HD현대중공업(329180)", "CS윈드(112610)", "한화오션(042660)", "현대백화점(069960)"],
        "insight": "시장이 단기 도파민(빅테크 쏠림)에서 벗어나 실적이 가시화되는 기계/조선/방산/에너지 등 구경제(Old Economy) 인프라로 온기를 넓히는 과정임. 특히 조선업은 다년치 수주 잔고와 친환경 규제 수혜로 매크로 변동성과 무관하게 실적 우상향이 확실한 업종임.",
        "action_point": "반도체 핵심 포지션을 유지한 채, 슈퍼사이클 어닝 서프라이즈가 기대되는 <span class=\"text-cyan-300 font-semibold\">HD현대중공업/한화오션</span>과 소송 승소로 규제 족쇄가 풀린 <span class=\"text-cyan-300 font-semibold\">CS윈드</span>를 포트폴리오에 적극 분산 편입하는 로테이션 전략이 바람직함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["economy", "energy"],
        "tags": ["조선슈퍼사이클", "풍력관련주", "소비재순환매", "수급분산"]
      }
    }
  }
}

pending_dir = Path("data/pending")
analyzed_root = Path("data/analyzed")

for video_id, item in batch6_data.items():
    primary = item["primary"]
    data = item["data"]
    
    dest_dir = analyzed_root / primary
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / f"{video_id}.json"
    
    dest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[분석 저장 완료] {dest_path}")
    
    pending_file = pending_dir / f"{video_id}.json"
    if pending_file.exists():
        pending_file.unlink()
        print(f"[대기파일 삭제] {pending_file}")

print("Batch 6 processing completed successfully.")
