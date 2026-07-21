import json
from pathlib import Path

batch5_data = {
  "S0f1kzx6Xo0": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "S0f1kzx6Xo0",
        "title": "삼성전자-SK하이닉스, 같은 반도체인데 주가는 왜 갈렸나ㅣ김장열 유니스토리자산운용 리서치센터장 [집중 오늘의 주식]",
        "published": "2026-06-16T13:00:35+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=S0f1kzx6Xo0",
        "thumbnail": "https://img.youtube.com/vi/S0f1kzx6Xo0/hqdefault.jpg"
      },
      "analysis": {
        "summary": "반도체 특수가스 전문기업 <span class=\"text-cyan-300 font-semibold\">후성</span>이 중국의 대일본 <span class=\"text-violet-300 font-medium\">육불화 텅스텐(WF6) 수출 통제</span> 조치로 인해 전 세계 공급망의 10%를 담당하는 핵심 수혜주로 부상함. 반면 삼성전자와 SK하이닉스의 주가 차별화는 삼성이 <span class=\"text-rose-400 font-medium\">퀄컴 파운드리 수주 실패</span> 및 HBM4 양산 물량 확보 지연 루머에 기인함. 다만 메모리 업계의 전반적인 이익 개선은 HBM보다는 범용 D램의 <span class=\"text-amber-300 font-bold\">가격 급등(50% 이상)</span> 효과가 핵심 동력임.",
        "key_claims": [
          "중국의 대일본 특수가스(WF6) 통제 조치로 가스 가격이 1년 새 3.3배 폭등해 후성의 중국 법인 흑자 전환이 가시화됨.",
          "삼성전자는 퀄컴 파운드리 수주를 놓치고 구글 TPU 우회 수주에 그치며 파운드리 흑자 전환 타이밍이 연기되는 우려가 제기됨.",
          "SK하이닉스가 HBM 선도 지위와 미국 나스닥 ADR 상장(40조 원 조달)을 이끌며 반도체 섹터의 매수 수급을 선점함."
        ],
        "data_points": [
          "육불화 텅스텐(WF6) 1년 전 대비 가격 상승률: 233% (3.3배)",
          "WF6 글로벌 공급망 중 중국의 수출 차단 분량: 전 세계 수요의 약 25%",
          "WF6 글로벌 공급망 중 후성의 점유율: 약 10%",
          "범용 D램 가격 상승률: 최근 50% 이상 급등"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "반도체 미세공정에 필수적인 <span class=\"text-cyan-300 font-semibold\">특수가스 공급 부족</span>으로 후성의 실적 턴어라운드가 강력하게 나타나고 있으며, 메모리 반도체 범용 D램 가격 상승세가 뚜렷하기 때문임.",
        "key_companies": ["후성(099430)", "삼성전자(005930)", "SK하이닉스(000660)"],
        "insight": "HBM 경쟁의 기술적 선도(삼성의 높은 스펙)보다 실제 물량 적기 공급(하이닉스)과 범용 D램의 가격 반등이라는 실질적인 캐시카우 흐름이 주가 차별화를 만들고 있음. 지정학적 규제(중국의 WF6 규제)에 대응한 반도체 소부장 핵심 원재료의 공급망 국산화 및 우회로 확보가 기업 실적을 가르는 변수임.",
        "action_point": "후성은 이미 단기 목표가인 2만 원대에 도달하여 차익 실현 리스크가 존재하므로 추격 매수보다는, 파운드리 노이즈로 저평가된 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>와 캐시카우가 보장된 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>를 분할 매수하는 장기 포지션이 유효함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["삼성전자", "SK하이닉스", "후성", "특수가스"]
      }
    }
  },
  "mB2AVGKMJAw": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "mB2AVGKMJAw",
        "title": "뉴욕증시, FOMC 앞두고 가치주 순환…스페이스X, 아마존 시총 추월 [월가 뉴스레터]",
        "published": "2026-06-16T22:01:05+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=mB2AVGKMJAw",
        "thumbnail": "https://img.youtube.com/vi/mB2AVGKMJAw/hqdefault.jpg"
      },
      "analysis": {
        "summary": "뉴욕 증시에서 FOMC 금리 결정을 앞두고 성장주에서 가치주로의 <span class=\"text-amber-300 font-bold\">자금 순환매</span>가 일어남. 이 과정에서 나스닥에 상장된 <span class=\"text-cyan-300 font-semibold\">스페이스X</span>가 주당 225~230달러선까지 폭등하며 아마존을 제치고 장중 시총 4위(2.9조 달러)를 달성하는 기염을 토함. 스페이스X의 단기 오버슈팅은 <span class=\"text-rose-400 font-medium\">유통 주식수 부족(4.9%)</span>과 기관들의 기계적 패시브 자금 매수가 결합된 수급 효과에 기인함.",
        "key_claims": [
          "미 연준의 FOMC 회의를 앞둔 관망세 속에 빅테크와 마이크론 등 성장 반도체주에서 가치주 영역으로의 매도/순환이 나타남.",
          "스페이스X는 상장 후 3일 연속 폭등하여 시총 2.9조 달러를 기록, 전 세계 시총 4위까지 도약하는 역대급 흥행을 보임.",
          "극도로 적은 유통 물량과 인덱스 편입(나스닥 100 등)을 노린 기관의 무조건적인 매수가 주가 폭등의 도파민을 자극함."
        ],
        "data_points": [
          "스페이스X 최고 주가 및 상승률: 225~230달러선 (장중 약 20% 폭등)",
          "스페이스X 장중 시가총액: 2.9조 달러 (아마존 추월, 시총 4위 기록)",
          "스페이스X 상장 유통 주식수 비중: 약 4.9%"
        ],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "스페이스X의 상장 흥행은 우주 산업 전반의 가치를 올리는 호재이나, 반도체 및 기존 빅테크의 <span class=\"text-rose-400 font-medium\">수급 이탈 및 포모(FOMO) 현상</span>으로 단기 변동성이 극대화되고 있기 때문임.",
        "key_companies": ["스페이스X", "아마존(AMZN)", "마이크로소프트(MSFT)", "마이크론(MU)"],
        "insight": "유통 물량이 4.9%에 불과한 상황에서 불붙은 상장 열기는 정량적 가치 평가를 벗어난 수급 쏠림의 전형임. 스페이스X가 불러온 포모로 인해 마이크론 등 기존 AI 메모리 주도주가 일시적 수급 공백을 겪는 기현상이 발생하고 있음.",
        "action_point": "스페이스X의 추가 오버슈팅에 휘둘려 <span class=\"text-rose-400 font-medium\">추격 매수</span>하기보다, 자금 이탈로 일시 조정을 겪는 반도체/AI 메모리 주도주의 저가 매수 기회로 삼는 것이 현명함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["space", "tech"],
        "tags": ["스페이스X상장", "가치주순환매", "나스닥100편입", "포모현상"]
      }
    }
  },
  "MQX9hVbNbeg": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "MQX9hVbNbeg",
        "title": "삼성전자보다 SK하이닉스? 외국인이 찍은 반도체 기회ㅣ명민준, 최효은, 이제충 [주린이 구조대]",
        "published": "2026-06-16T14:00:18+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=MQX9hVbNbeg",
        "thumbnail": "https://img.youtube.com/vi/MQX9hVbNbeg/hqdefault.jpg"
      },
      "analysis": {
        "summary": "홍콩의 대형 자산운용사 CSOP(자산 75조 원 운용)가 세계 최초로 출시한 한국 반도체 2배 레버리지 ETF에 글로벌 자금이 유입되며, 특히 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span> 레버리지 자산고가 16조 원을 돌파함. 이는 해외 자본(특히 홍콩/중국계 자금)이 한국 금융위원회의 <span class=\"text-amber-300 font-bold\">통합계좌 도입</span> 등 접근성 개선에 힘입어 한국 대표 반도체를 아시아 반도체 투자의 핵심 레일로 채택했기 때문임.",
        "key_claims": [
          "금융당국의 통합계좌 활성화 등 제도적 노력으로 홍콩 및 글로벌 기관들의 한국 반도체 시장 접근성이 획기적으로 개선됨.",
          "CSOP의 삼성전자 2배 레버리지(3.7조 원) 대비 SK하이닉스 2배 레버리지(16조 원) 자산 규모가 4배 이상 커지며 SK하이닉스 쏠림이 뚜렷함.",
          "해외 자금은 HBM 시장의 주도권과 함께 미국 나스닥 ADR 상장(40조 원 규모)을 앞둔 SK하이닉스의 글로벌 재평가 가능성에 적극 베팅함."
        ],
        "data_points": [
          "CSOP 자산운용 총 운용 규모: 500억 달러 (약 75조 원)",
          "CSOP 삼성전자 2배 레버리지 ETF 자산규모: 약 3.7조 원",
          "CSOP SK하이닉스 2배 레버리지 ETF 자산규모: 약 16조 원"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "<span class=\"text-amber-300 font-bold\">통합계좌 활성화</span>로 외국인의 한국 주식 직접 투자 익스포저가 확대되고 있으며, 특히 SK하이닉스를 향한 대규모 홍콩 롱(Long) 자금 유입이 밸류에이션을 강력하게 뒷받침하고 있기 때문임.",
        "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
        "insight": "해외 자본이 삼성전자보다 SK하이닉스에 압도적인 뭉칫돈을 던지는 것은 HBM 독점력 및 미국 나스닥 상장을 통한 밸류에이션 할증(디스카운트 해소) 기대감이 반영된 결과임. 레버리지 ETF에 대규모 패시브 자금이 누적될수록 향후 반도체 주가의 하방 경직성과 상승 탄력이 동시에 강화되는 효과가 있음.",
        "action_point": "외국인 자금의 강력한 수급 뒷받침을 바탕으로 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>의 주도주 지위가 지속될 것이므로, 포지션을 확고히 유지하되 단기 변동성을 헤지하기 위해 분할 매수로 대응하는 것이 바람직함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["외국인수급", "통합계좌", "CSOP자산운용", "레버리지ETF"]
      }
    }
  },
  "aubeiTaOkqw": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "aubeiTaOkqw",
        "title": "의심 없이 파티를 즐겨라. 유가 예언은 맞아가고 있습니다ㅣ홍선애, 문홍철 DB투자증권 자산전략팀장 [여의도 인사이트]",
        "published": "2026-06-16T10:19:41+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=aubeiTaOkqw",
        "thumbnail": "https://img.youtube.com/vi/aubeiTaOkqw/hqdefault.jpg"
      },
      "analysis": {
        "summary": "미-이란 간의 지정학적 임시 합의(MOU)가 물꼬를 트며 <span class=\"text-violet-300 font-medium\">호르무즈 해협 재개방</span> 기대로 국제 유가가 배럴당 70달러대로 하락 안착함. 유가의 하향 안정화는 에너지 비용 인플레이션 압력을 차단하여 미국의 <span class=\"text-amber-300 font-bold\">완화적 통화 정책</span>(금리 인하)을 유도하는 강력한 매크로 배경을 제공함. 이에 따라 증시 및 채권 시장에는 '의심 없이 파티를 즐겨라'라는 수준의 유동성 우호적 랠리 국면이 펼쳐질 전망임.",
        "key_claims": [
          "지정학 갈등 봉합으로 유가는 배럴당 60달러선까지 떨어질 것이라는 예측이 들어맞고 있으며, WTI 기준 77달러선이 무저짐.",
          "공급 측면의 유가 불안 해소는 미 연준의 금리 동결 및 인하 유도를 앞당기는 핵심 지표로 작용할 것임.",
          "매크로 리스크(유가, 인플레) 완화에 따라 주식 시장은 일시적 조정을 딛고 추가적인 상승 랠리('음란한 상승장')를 이어갈 것임."
        ],
        "data_points": [
          "국제 유가 하락 수준: WTI 기준 배럴당 77.5달러 (80달러선 붕괴)",
          "유가 장기 목표 전망: 9월~10월 기준 배럴당 60달러대 진입 예측",
          "호르무즈 해협 통행 추정량: 블룸버그 공식 650건 대비 미국 호위 포함 약 1,000건 수준"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "미-이란 종전 타결과 <span class=\"text-violet-300 font-medium\">유가 배럴당 70달러선 붕괴</span>로 인플레이션 우려가 현저히 감소하여 연준의 긴축 강도 완화와 유동성 랠리(금리 하락 및 증시 상승)의 여건이 성숙했기 때문임.",
        "key_companies": [],
        "insight": "유가는 전쟁 시 3배 급등한다는 시장의 과도한 공포를 뒤엎고, 지정학적 완화와 미국의 묵인 하에 대량 공급이 이미 유통되고 있었다는 사실이 증명됨. 공급 안정화가 이끄는 디스인플레이션은 기술주 및 성장주의 멀티플을 높여주는 강력한 촉매제 역할을 함.",
        "action_point": "지정학 불안이 해소되며 유가가 안정화되는 국면이므로 에너지/원자재 인버스 포지션 또는 <span class=\"text-cyan-300 font-semibold\">금리 하락 수혜주</span>(빅테크 및 반도체 장비주)를 적극적으로 매수하는 '롱(Long)' 플레이가 적절함."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["국제유가", "지정학리스크해소", "통화정책완화", "호르무즈해협"]
      }
    }
  }
}

pending_dir = Path("data/pending")
analyzed_root = Path("data/analyzed")

for video_id, item in batch5_data.items():
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

print("Batch 5 processing completed successfully.")
