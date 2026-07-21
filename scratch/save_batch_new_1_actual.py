import json
from pathlib import Path

def save_and_delete(video_id, primary_topic, secondary_topics, tags, analysis_data):
    pending_path = Path(f"data/pending/{video_id}.json")
    if not pending_path.exists():
        print(f"Warning: {pending_path} does not exist.")
        return
        
    pending_data = json.loads(pending_path.read_text(encoding="utf-8"))
    video_data = pending_data["video"]
    
    classification_data = {
        "primary_topic": primary_topic,
        "secondary_topics": secondary_topics,
        "tags": tags
    }
    
    analyzed_dir = Path(f"data/analyzed/{primary_topic}")
    analyzed_dir.mkdir(parents=True, exist_ok=True)
    
    result_path = analyzed_dir / f"{video_id}.json"
    result_path.write_text(
        json.dumps({
            "video": video_data,
            "analysis": analysis_data,
            "classification": classification_data
        }, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"Saved: {result_path}")
    
    pending_path.unlink()
    print(f"Deleted pending: {pending_path}")
    
    synthesis_cache = Path(f"data/synthesis/{primary_topic}.json")
    if primary_topic != "economy" and synthesis_cache.exists():
        synthesis_cache.unlink()
        print(f"Invalidated cache: {synthesis_cache}")

batch_data = {
  "2bdYTLIuYYc": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["기축통화", "트리핀의딜레마", "미국부채", "경상수지적자", "환율상승"],
    "analysis": {
      "summary": "미국 무역 적자가 기축 통화 공급 때문에 필연적이라는 <span class=\"text-rose-400 font-medium\">트리핀의 딜레마</span>는 현대 금융 환경에 맞지 않는 환상입니다. 달러 수요는 연준의 유동성 공급보다 민간이 수익과 투자를 추구하는 '수익형 달러(Profit Dollar)' 흐름과 역외 유로달러 시장의 신용 창출에 의해 더 강하게 추동됩니다. 한국 원화 가치 하락(환율 급등)은 펀더멘털 문제가 아닌 <span class=\"text-cyan-300 font-semibold\">국민연금</span>의 해외 자산 매수 및 반도체 비중 조절을 위한 포트폴리오 리밸런싱에 따른 일시적 현상으로 풀이됩니다.",
      "key_claims": [
        "미국의 무역 적자는 기축통화 지위 유지를 위한 통화 공급 때문이 아니라, <span class=\"text-amber-300 font-bold\">저축 대비 높은 투자 규모</span>와 정부의 재정 적자에서 기인합니다.",
        "달러의 한계 구매자는 각국 중앙은행이 아니라 AI 붐과 고금리 혜택을 쫓아 미국 국채 및 기술주에 투자하는 글로벌 민간 자본(수익형 달러)입니다.",
        "한국 원화의 비정상적 약세는 경제 펀더멘털 훼손이 아닌 국민연금의 해외 송금 및 반도체 대장주의 리밸런싱 수요가 맞물린 기술적 하방 압력 때문입니다."
      ],
      "data_points": [
        "미국 국채 보유국 중 민간 부문 보유 비중: 약 58% (공공 부문 42% 대비 추세적 상승)",
        "미국 총 부채 규모: 약 39조 달러 (조만간 40조 달러 돌파 전망)",
        "외국인 보유 미국 국채 총액: 약 9.2조 달러 (작년 말 기준)"
      ],
      "signal": "neutral",
      "signal_reason": "달러 자산의 강력한 메리트로 미국 예외주의가 공고해지나, 민간 비중이 늘면서 미국의 금리 및 환율 변동성은 한층 커지는 위험이 공존합니다.",
      "key_companies": ["국민연금", "엔비디아(NVDA)", "삼성전자", "SK하이닉스"],
      "insight": "기축통화의 공급 메커니즘이 강제적 안전자산 축적에서 자발적 고수익 투자 수단(Profit Dollar)으로 체질이 변화했습니다. 이는 미국 외 시장(특히 한국 등 신흥국)의 일시적 자금 유출과 환율 상승을 초래하나 중장기적으로 펀더멘털이 우수한 국가는 정상화 경로를 밟을 것입니다.",
      "action_point": "환율 급등에 과도한 공포를 갖기보다는, 원화 가치 저평가 국면을 활용해 국내 우량 기업의 저가 매수 기회로 삼는 것이 현명합니다."
    }
  },
  "5469mSMhoBM": {
    "primary_topic": "tech",
    "secondary_topics": ["stock", "economy"],
    "tags": ["HBM", "AI비용통제", "모델라우팅", "CXMT", "반도체피크아웃"],
    "analysis": {
      "summary": "빅테크 기업들의 AI 비용 통제 압박이 임계점에 도달하면서 <span class=\"text-rose-400 font-medium\">메모리(HBM) 가격 상한선</span>이 설정되고 있습니다. 빅테크들은 고비용 미국 고급 AI 모델의 비중을 73%에서 33%로 낮추고 중국산 및 오픈소스 모델을 혼합하는 '모델 라우팅'을 본격화하고 있습니다. 메모리 제조사들이 추가적인 HBM 가격 인상을 시도할 경우, 최종 고객인 AI 서비스사들의 수익성 붕괴와 중국 <span class=\"text-cyan-300 font-semibold\">CXMT</span> 등으로의 공급망 다변화라는 역풍에 직면할 수 있습니다.",
      "key_claims": [
        "비용 한계에 봉착한 기업들이 OpenAI, Anthropic 등의 비중을 축소하고 67%의 업무를 저가 모델로 전환하는 비용 통제 조치에 나섰습니다.",
        "메모리 제조업체(삼성전자, SK하이닉스)의 마진율은 최종 고객의 판가 전가 한계로 인해 당분간 고점을 형성할 가능성이 높습니다.",
        "HBM 등 가격이 임계점을 초과할 경우 글로벌 AI 진영이 비용 부담을 견디지 못하고 중국 메모리 대안을 모색할 수 있는 구축 효과가 우려됩니다."
      ],
      "data_points": [
        "미국 프리미엄 AI 모델(ChatGPT, Claude, Gemini) 사용 비중: 73% -> 33% (1년 만에 대폭 하락)",
        "업무 중 저가/오픈소스/중국 모델로 라우팅되는 비중: 약 67%",
        "AI 자동화 침투율: 미국 내 주요 3개 분야(코딩, 금융, 법률) 외에는 실질 침투율 1% 미만 (성장 잠재력은 여전)"
      ],
      "signal": "bearish",
      "signal_reason": "HBM 수요는 굳건하나 빅테크들의 강력한 AI 비용 통제 및 모델 다변화 움직임으로 반도체 가격의 추가 인상 폭이 제한되어 메모리 업계의 이익률 상단이 제한될 위험이 큽니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "CXMT", "OpenAI", "Anthropic"],
      "insight": "AI 생태계의 부가가치가 하드웨어에서 소프트웨어의 효율화(모델 라우팅)로 이동하고 있습니다. 최종 단말의 수익화 지연은 결국 상단의 반도체 밸류체인으로 가격 인하 혹은 가격 동결 압력으로 고스란히 전가될 것입니다.",
      "action_point": "메모리 업종의 추가적인 마진 스프레드 확대 기대치를 낮추고, 무리한 추격 매수보다는 밸류에이션 상한선을 고려한 포트폴리오 조절이 요구됩니다."
    }
  },
  "9rG6UOIvguc": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["반대매매", "신용리스크", "삼성전자", "SK하이닉스", "레버리지ETF"],
    "analysis": {
      "summary": "최근 코스피 폭락은 펀더멘털의 훼손이 아닌 고점 대비 급락으로 유발된 <span class=\"text-rose-400 font-medium\">신용 반대매매</span>와 수급 교란 때문입니다. 레버리지를 사용한 개인 투자자들이 강제 청산을 피하기 위해 멀쩡한 대형 실적주(삼성전자, SK하이닉스 등)까지 투매하면서 '매도가 매도를 부르는' 투심 붕괴 현상이 나타났습니다. 이번 수급의 꼬임은 7월 중순 예정된 글로벌 반도체 장비 및 TSMC의 실적 발표에서 실적 펀더멘털이 입증되어야 해소될 전망입니다.",
      "key_claims": [
        "주요 대형주가 고점 대비 30% 이상 하락함에 따라 담보 부족으로 인한 신용 반대매매 경고 문자가 무더기로 발송되었습니다.",
        "반대매매 물량은 특정 종목에 한정되지 않고, 개인 투자자들이 현금을 신속히 확보하기 위해 거래량이 많은 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>, <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>를 매도하면서 전방위 지수 하락을 부추깁니다.",
        "국내 도입된 단일종목 레버리지 ETF의 규제 논란과 정책적 혼선이 헤지 거래 유출과 선물 매도를 부추겨 변동성을 키웠습니다."
      ],
      "data_points": [
        "코스피 고객예탁금 추이: 과거 최고치 130조 원 규모 -> 최근 약 30조 원 유출되어 100조 원대 붕괴 위험",
        "반대매매 발동 조건 임계점: 주가 고점 대비 약 30% ~ 35% 이상 폭락 시 강제 청산 위험 노출"
      ],
      "signal": "bearish",
      "signal_reason": "실적은 양호하나 반대매매의 기계적 프로그램 주문과 고객예탁금 감소(체력 저하)로 인한 수급 붕괴가 단기적으로 지수 하방 압력을 높이고 있습니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "ASML", "TSMC"],
      "insight": "시장 체력(고객예탁금)이 고갈된 상태에서 기계적 프로그램 반대매매가 집행되면 펀더멘털과 무관하게 언더슈팅이 심해집니다. 이 국면은 감정적 매매가 지배하는 비이성적 시장이므로 개인의 투심 회복이 시급합니다.",
      "action_point": "신용 및 미수 거래를 철저히 지양하고, 수급에 의해 강제로 주가가 억눌린 실적주(IT, 방산, 전력 등)를 분할 저가 매수 관점으로 대응해야 합니다."
    }
  },
  "Az9LBgm3_h0": {
    "primary_topic": "etc",
    "secondary_topics": [],
    "tags": ["도파민", "보상예측오차", "신경과학", "목표추구", "동기부여"],
    "analysis": {
      "summary": "도파민은 쾌락을 느낄 때 분비되는 호르몬이 아니라, 무언가를 <span class=\"text-amber-300 font-bold\">추구하고 기대할 때</span> 작동하는 물질입니다. 뇌는 예상했던 것보다 더 큰 보상을 마주했을 때인 '보상 예측 오차' 상황과, 목표를 달성할 수 있다는 강한 희망을 품을 때 도파민을 폭발적으로 분비합니다. 즉, 도파민은 결과물이 아닌 '성공의 가능성을 향해 나아가는 과정'에서 인간을 움직이게 하는 원동력입니다.",
      "key_claims": [
        "도파민은 쾌락 그 자체를 제공하는 물질이 아니라, 인간이 목표를 향해 달려가도록 추동하는 <span class=\"text-violet-300 font-medium\">추구와 희망의 신경전달물질</span>입니다.",
        "자신이 예상했던 수준을 넘어서는 깜짝 보상이 주어질 때(보상 예측 오차) 뇌에서 가장 강한 도파민 반응이 유도됩니다."
      ],
      "data_points": [],
      "signal": "na",
      "signal_reason": "인간의 뇌 메커니즘과 도파민 분비 기전에 관한 순수 신경과학 교육 영상이므로 투자 시그널을 제공하지 않습니다.",
      "key_companies": [],
      "insight": "주식이나 가상자산 투자자들이 매수 직후의 상승 기대감에서 도파민을 강하게 느끼는 이유가 규명됩니다. 즉, 이윤 획득이라는 결과보다 '수익이 날 것 같은 기대 국면'에서 뇌가 흥분하는 신경학적 관성을 인지해야 뇌동매매를 예방할 수 있습니다.",
      "action_point": "투자 의사결정 시 도파민성 기대감에 취하지 않도록 이성적 필터를 거치고, 과정의 도파민 분비를 제어하는 규칙적인 매매 프로세스를 수립해야 합니다."
    }
  },
  "BLvI5dBN8Ws": {
    "primary_topic": "tech",
    "secondary_topics": ["etc"],
    "tags": ["한국과학기술", "과장광고", "벤치마크왜곡", "로봇스타트업", "엔비디아"],
    "analysis": {
      "summary": "대한민국 과학기술계 및 스타트업계에 성과를 부풀려 과장 홍보하는 문화가 만연해 있습니다. 극단적으로 제약된 특정 실험 조건이나 벤치마크 성과를 바탕으로 <span class=\"text-cyan-300 font-semibold\">엔비디아</span>나 구글을 뛰어넘었다고 포장하여 이를 <span class=\"text-rose-400 font-medium\">정치적 슬로건</span>으로 소비하는 행태는 국가 R&D 생태계의 정직한 성장을 저해합니다.",
      "key_claims": [
        "국내 다수의 기술 기업과 초기 스타트업들이 정부 행사나 투자 유치 시 제한된 벤치마크 우위를 근거로 '글로벌 빅테크 초월'이라는 문구를 남발합니다.",
        "이를 실제 범용적 상용 성과가 아닌 정치적 업적 및 전시성 홍보로 소비함으로써 기술에 대한 대중과 의사결정권자의 왜곡된 인식을 낳습니다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "한국 기술 생태계의 과장 홍보 관행을 꼬집는 비판적 시사 정보로, 단기적인 주식 시장 시그널을 유도하지는 않습니다.",
      "key_companies": ["엔비디아(NVDA)", "구글(GOOGL)"],
      "insight": "단일 벤치마크 1위 달성과 전 세계에 배포된 상용 인프라 장악력은 천양지차입니다. 데모 수준의 성과에 속지 않고, 글로벌 하드웨어 및 소프트웨어 연동 경쟁력(생태계 락인)을 갖추었는지를 선별하는 투자자의 안목이 필수적입니다.",
      "action_point": "국내 테크 및 로봇 테마주 투자 시 '엔비디아 제쳤다'식의 언론 보도에 현혹되지 말고, 실제 납품 계약 및 상용화 지표를 철저히 검증해야 합니다."
    }
  },
  "boq4Dn4H238": {
    "primary_topic": "etc",
    "secondary_topics": ["stock"],
    "tags": ["포스코인터내셔널", "ESG경영", "상생협력", "식량안보", "인프라투자"],
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">포스코인터내셔널</span>은 글로벌 기업들이 척박한 인프라로 인해 철수한 해외 식량 사업지에서 현지 주민과의 상생 협력을 바탕으로 사업 안정성을 확보했습니다. 단순한 농장 운영을 넘어 병원, 학교 등 필수 인프라 투자를 병행하여 동반 성장 모델을 구축함으로써 지속 가능한 해외 영농 인프라의 성공 사례를 제시하고 있습니다.",
      "key_claims": [
        "포스코인터내셔널은 인허가 규제와 열악한 인프라 극복을 위해 현지 주민의 삶 속에 융합되는 상생 방식을 핵심 전략으로 선택했습니다.",
        "지역사회와의 우호적 파생 관계 및 인프라 구축은 사업 리스크를 최소화하고 식량 안전망을 강화하는 안정적인 디딤돌 역할을 수행합니다."
      ],
      "data_points": [],
      "signal": "bullish",
      "signal_reason": "해외 자원 및 식량 개발 사업의 최대 위험 요인인 현지 정부·주민과의 갈등 리스크를 ESG 상생 경영으로 통제하며 장기 성장 동력을 성공적으로 확보했기 때문입니다.",
      "key_companies": ["포스코인터내셔널(047050)"],
      "insight": "개발도상국 원자재 개발은 지정학 및 현지 소요 리스크가 큽니다. 포스코인터내셔널의 상생형 거점 구축 방식은 단순 영리 활동을 넘어 '자원 공급망 안정화'라는 국가적 가치와 결합해 강력한 비즈니스 성벽을 만듭니다.",
      "action_point": "글로벌 공급망 재편 및 식량 안보의 수혜주인 포스코인터내셔널의 장기적 ESG 사업 성과와 이익 기여도를 긍정적으로 모니터링할 필요가 있습니다."
    }
  }
}

for video_id, item in batch_data.items():
    save_and_delete(
        video_id=video_id,
        primary_topic=item["primary_topic"],
        secondary_topics=item["secondary_topics"],
        tags=item["tags"],
        analysis_data=item["analysis"]
    )
