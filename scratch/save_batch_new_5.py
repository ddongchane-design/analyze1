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
  "r3HbquYwBwk": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["치플레이션", "AI인플레이션", "러시아정유공장", "중립금리인상", "고금리장기화"],
    "analysis": {
      "summary": "우크라이나 드론 공격으로 인한 <span class=\"text-rose-400 font-medium\">러시아 정유시설 파괴</span>와 석유 제품 가격의 고공행진, 그리고 급증하는 AI 투자가 물가를 견인하는 '치플레이션(Chip-flation)'이 결합하여 미국의 인플레이션 경로를 교란하고 있습니다. 시장 일각에서는 연준이 기준금리를 추가 인상하거나 고금리를 내년까지 장기화할 것이라는 매파적 우려를 제기하고 있습니다. 비록 단기 경기 침체 확률은 역사적 평균보다 낮으나, 장기 고금리 상태의 유지는 성장주와 <span class=\"text-cyan-300 font-semibold\">AI 인프라 투자 유동성</span>을 위축시킬 잠재적 리스크 요인입니다.",
      "key_claims": [
        "드론 공습으로 인한 러시아 정유 생산 차질 및 디젤 수출 금지 조치는 원유 가격 이상의 <span class=\"text-rose-400 font-medium\">석유 정제 마진 급등</span>을 유발하여 실물 물가를 압박합니다.",
        "모건스탠리는 AI 투자가 생산성 향상에 따른 소비 증가 및 중립 금리 상승을 유발하여 디플레가 아닌 <span class=\"text-amber-300 font-bold\">인플레이션 요인</span>으로 작용한다고 분석했습니다.",
        "만약 연준이 시장 신뢰 회복을 위해 고금리를 내년까지 동결 또는 추가 인상할 경우, 빅테크 기업들의 <span class=\"text-rose-400 font-medium\">채권 조달 비용 급등</span>으로 AI CAPEX 붐이 냉각될 위험이 있습니다."
      ],
      "data_points": [
        "미국 경기 침체 발생 확률 전망치: 약 15% 수준 (역사적 평균 18% 대비 양호한 수준)",
        "근원 CPI에 치플레이션(메모리 및 칩 가격 상승)이 미치는 기여도: 약 0.2% ~ 0.5%p 수준 상승 요인으로 분석",
        "미국 10년물 국채 금리 수준: 4.5% 선 돌파, 2년물 국채 금리는 4.2% 선 초과 유지"
      ],
      "signal": "neutral",
      "signal_reason": "유가 및 칩 가격 상승이 유발하는 복합적인 매크로 인플레이션 우려와 고금리 장기화 리스크를 설명하고 있어 균형 잡힌 중립적 분석이 요구되기 때문입니다.",
      "key_companies": ["Apple(AAPL)"],
      "insight": "AI 버블 붕괴론의 실질적 위협은 단순한 기술적 한계가 아니라, 지속되는 서비스 및 칩 가격 물가 상승으로 인한 <span class=\"text-rose-400 font-medium\">연준의 고금리 장기화 압박</span>입니다. 자금 조달 금리가 임계점을 넘어설 경우 레버리지를 일으키는 인프라 투자의 지속력에 균열이 생길 수 있습니다.",
      "action_point": "연준의 금리 가이던스 변화를 모니터링하며, 물가 전가력을 갖춘 기술 대기업 외에 높은 부채 비율을 지닌 <span class=\"text-rose-400 font-medium\">고레버리지 중소형 성장주</span>의 포트폴리오 비중을 선제적으로 조절하는 위험 관리가 필요합니다."
    }
  },
  "tAAPn9FuTrs": {
    "primary_topic": "space",
    "secondary_topics": ["tech"],
    "tags": ["창정10B", "팰컨9", "이륙추력", "탑재체용량", "재사용로켓효율"],
    "analysis": {
      "summary": "중국이 개발 중인 재사용 로켓 창정 10B(Changzheng 10B)와 스페이스X의 팰컨 9(Falcon 9)의 성능 지표를 분석한 결과, 이륙 추력 면에서는 창정이 우세하나 <span class=\"text-cyan-300 font-semibold\">실질 탑재 중량(Payload) 성능</span>은 매우 유사한 수준인 것으로 나타났습니다. 팰컨 9은 15년간 다듬어진 압도적인 연소 효율성을 지녔으며, 1단 부스터 회수를 위한 예비 연료를 감안한 실제 재사용 모드 시 두 발사체 모두 저궤도 기준 15~16톤 안팎을 쏘아 올릴 수 있습니다. 이는 중국의 재사용 발사체 역량이 글로벌 선두 수준에 바짝 추격했음을 보여줍니다.",
      "key_claims": [
        "창정 10B는 이륙 순간의 지면 추력이 890톤으로 팰컨 9(770~780톤) 대비 <span class=\"text-cyan-300 font-semibold\">100톤 이상 강력한 힘</span>을 지니고 있습니다.",
        "일회용 버리기 모드 시 팰컨 9은 최대 22.8톤을 올릴 수 있지만, 1단 재사용 회수 연료를 탑재하면 실제 LEO 페이로드는 <span class=\"text-cyan-300 font-semibold\">15~16톤 수준으로 감소</span>합니다.",
        "두 발사체 모두 1단 부스터 재사용 회수를 전제로 할 경우, 실질 탑재 체급은 15~16톤 선에서 팽팽한 기술적 균형을 이룹니다."
      ],
      "data_points": [
        "창정 10B 이륙 추력 스펙: 약 890톤 (팰컨 9의 770~780톤 대비 우세)",
        "창정 10B LEO 재사용 모드 탑재 용량: 최대 16톤 수준",
        "팰컨 9 LEO 최대 일회용 탑재 용량: 약 22.8톤 (재사용 회수 모드 시 15~16톤 수준으로 감소 추정)"
      ],
      "signal": "neutral",
      "signal_reason": "미국과 중국의 대표 재사용 발사체 성능 지표를 기술적으로 객관 비교 분석하는 콘텐츠로, 시장 밸류에이션의 급격한 변동을 동반하는 투자 시그널은 아니기 때문입니다.",
      "key_companies": ["SpaceX"],
      "insight": "단순한 이륙 추력의 크기보다 중요한 것은 대기권 진입 연소 효율 및 재사용 모드에서의 페이로드 페널티를 최소화하는 <span class=\"text-cyan-300 font-semibold\">설계 최적화 역량</span>입니다. 창정 10B의 성능 확보는 글로벌 위성 발사 대행 시장의 중장기 단가 인하 경쟁을 가속화할 전망입니다.",
      "action_point": "저궤도 우주 인터넷 군집위성 발사 단가 하락 수혜를 입을 수 있는 글로벌 위성 제조사 및 <span class=\"text-cyan-300 font-semibold\">지상국 안테나/통신 장비 기업</span>들의 장기 수주 파이프라인을 모니터링해야 합니다."
    }
  },
  "uSKKQo_RkO8": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["필립모리스", "알트리아", "KT앤G", "배당재투자", "무연제품전환"],
    "analysis": {
      "summary": "세퇴하는 사양 산업이라 할지라도 강력한 가격 결정력과 설비 투자(CAPEX) 제한에 기반한 독점력을 유지한다면 복리 효과를 통해 시장을 초월하는 수익을 낸 수 있습니다. 1957년부터 2003년까지 배당 재투자 시 필립 모리스는 나스닥 기술주들을 제치고 S&P 500 내 최고의 누적 성과(약 4,600배 성장)를 기록했습니다. 현재 담배 업계는 <span class=\"text-cyan-300 font-semibold\">무연 제품(연기 없는 전자담배 및 파우치)</span>으로의 체질 개선에 따라 필립 모리스 인터내셔널(PMI)과 같은 성장주와 알트리아(Altria) 같은 고배당 정체 가치주로 운명이 갈리고 있습니다. 한국의 KT&G 역시 무연 전환 및 글로벌 독점 유통망 강화를 통해 동일한 시험대에 진입했습니다.",
      "key_claims": [
        "사양 산업은 신규 경쟁자의 진입 위협이 없어 잔존 기업이 제품 가격 인상을 통해 <span class=\"text-cyan-300 font-semibold\">압도적인 현금 흐름</span>을 누리고 배당 및 자사주 매입에 집중할 수 있습니다.",
        "아이코스(IQOS)와 구강 니코틴 진(Zyn) 파우치의 글로벌 대흥행에 성공한 PMI는 <span class=\"text-cyan-300 font-semibold\">무연 제품 매출 비중을 41.5%</span>까지 끌어올리며 강력한 성장 모멘텀을 확보했습니다.",
        "반면 알트리아는 전자담배 엔조이의 특허 소송에 따른 자산 손실(8.7억 달러) 및 내수 규제 정체로 주가 상승 여력이 제한된 채 고배당(5.7%대)에만 의존하는 양상입니다."
      ],
      "data_points": [
        "1957년 ~ 2003년 배당 재투자 시 필립 모리스의 자산 증가: 1,000달러 투자 시 460만 달러로 증가 (동 기간 S&P 500 지수 투자는 12.5만 달러로 증가)",
        "PMI 무연 제품(Smoke-free) 글로벌 매출 비중 목표치: 약 41.5% 수준까지 상승",
        "알트리아 배당수익률 및 특허 분쟁 손상차손 규모: 약 5.7%대 배당수익률, 전자담배 부문 8억 7,300만 달러 손상 처리 반영",
        "미국 성인 및 뉴욕주 성인 흡연율 수준: 각각 9.9% 및 9.3%로 사상 처음 10% 아래로 하락"
      ],
      "signal": "neutral",
      "signal_reason": "전형적인 사양 산업 내 배당 재투자 역사적 의의와 무연 신제품 전환에 따른 기업별 차별화 양상을 중립적 학술/정보 관점에서 제공하는 콘텐츠이기 때문입니다.",
      "key_companies": ["Altria(MO)", "Philip Morris International(PM)", "KT&G(033780)"],
      "insight": "저평가된 주식에서 나오는 높은 배당을 재투자하여 수십 년간 굴리는 복리의 마법은 담배주가 증명한 교과서적인 가치 투자 방법론입니다. 차세대 <span class=\"text-cyan-300 font-semibold\">하이브리드 전자담배 릴(lil)</span>의 해외 유통망을 PMI와 15년 장기 파트너십으로 묶은 KT&G 역시 배당 안정성과 성장성을 동시에 테스트받고 있습니다.",
      "action_point": "무연 신제품 포트폴리오 다변화에 성공하여 높은 가격 결정력과 영업 이익률을 회복하고 있는 <span class=\"text-cyan-300 font-semibold\">필립 모리스(PMI)</span>와 글로벌 유통을 가시화하는 <span class=\"text-cyan-300 font-semibold\">KT&G</span>를 장기 배당 성장 포트폴리오의 안정적 기초 자산으로 확보해 갈 만합니다."
    }
  },
  "v0VjtfKn0OE": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["SK하이닉스ADR", "변동성리스크", "메타인프라투자", "파생상품출시", "장기금리상방"],
    "analysis": {
      "summary": "SK하이닉스가 미국 나스닥 ADR 상장(SKY) 첫날 13% 상승 흥행하며 코리아 디스카운트 해소와 글로벌 투자 자금 유치 모멘텀을 구축했습니다. 최태원 회장은 오랫동안 반도체 시장을 지배하던 사이클이 깨지고 수요가 공급을 크게 초과하는 쇼티지 구조로 진입했다고 시사했습니다. 메타의 내년 14GW 규모 AI 인프라 전력 캐파 증설 계획 등 하이퍼스케일러들의 투자 의지가 여전히 강력함이 확인된 반면, 국내 시장에서 하이닉스 2배 레버리지 ETF 거래량이 본주를 추월하며 나타난 <span class=\"text-rose-400 font-medium\">수급적 가격 교란 현상</span>과 파생상품 출시에 따른 단기 변동성 리스크는 여전히 주시해야 할 요인입니다.",
      "key_claims": [
        "ADR 상장은 마이크론 대비 현저히 저평가된 밸류에이션을 극복하고, 미국 현지 자본이 직접 하이닉스 주식을 매수할 수 있게 함으로써 장기적으로 <span class=\"text-cyan-300 font-semibold\">수급 안정성을 개선</span>합니다.",
        "메타가 올해 7GW에서 내년 14GW로 AI 데이터센터 용량을 배가하기로 발표함에 따라 AI 인프라 CAPEX 성장성 둔화에 대한 <span class=\"text-rose-400 font-medium\">시장 우려가 종식</span>되었습니다.",
        "그러나 미국 시장 내 하이닉스 2배 레버리지 ETF 및 토큰화 거래 상품 출시는 <span class=\"text-rose-400 font-medium\">투기적 거래에 의한 단기 주가 변동성</span>을 추가로 자극할 수 있는 리스크 요인입니다."
      ],
      "data_points": [
        "SK하이닉스 ADR(SKY) 데뷔일 상승률: 공모가 대비 13% 상승한 168달러 마감",
        "메타(Meta) AI 인프라 용량 투자 계획: 올해 7GW에서 내년 14GW로 2배 증설 예정",
        "메모리 반도체 밸류체인 12개월 선행 PER: 10배 미만 수준으로 여전히 글로벌 저평가 상태 유지"
      ],
      "signal": "neutral",
      "signal_reason": "ADR 상장이 지닌 장기적 수급 개선 효과 및 AI 투자 지속성이라는 호재와 함께, 파생상품 난립으로 인한 단기 주가 변동성 및 매크로 장기 금리 압박이라는 리스크를 균형 있게 짚어내고 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "Meta(META)"],
      "insight": "하이닉스의 ADR 성공은 글로벌 유동성이 동아시아 메모리 반도체 공급망의 대체 불가능한 지위를 신뢰한다는 가장 강력한 신호입니다. 다만, 단기 차익 실현 욕구와 2배 레버리지 ETF에 따른 <span class=\"text-rose-400 font-medium\">수급적 꼬리 흔들기(Whip-saw) 변동성</span>을 이겨내야 진정한 밸류에이션 리레이팅이 안착할 수 있습니다.",
      "action_point": "미국 30년물 국채 금리 급등에 따른 전체 기술주 멀티플 압박 요인을 염두에 두고, 하이닉스 본주 가격이 220만 원에서 250만 원 사이의 매물 소화 조정을 거칠 때마다 <span class=\"text-cyan-300 font-semibold\">분할 저가 매수</span>로 접근하는 것이 유효합니다."
    }
  },
  "vNRIpnggmNs": {
    "primary_topic": "crypto",
    "secondary_topics": ["stock"],
    "tags": ["클레리티법안", "로빈후드L2", "아비트럼", "실질금리비트코인", "AI인플레이션논쟁"],
    "analysis": {
      "summary": "미국 의회 상원에서 공직자 코인 보유 윤리성 및 이자 조항 쟁점으로 클레리티 법안(Clarity Act)의 연내 통과 확률이 35%로 주저앉자, SEC가 기다리지 않고 <span class=\"text-cyan-300 font-semibold\">토큰 분류 체계 선제 시행 및 3대 면제 규칙(세이프 하버)</span>을 도입하며 시장의 불확실성을 빠르게 해소하고 있습니다. 비트코인은 전통적으로 7월 강세 계절성(최근 10년 중 8회 상승)을 보이며 ETF 순유입에 힘입어 64,000달러선으로 회복했습니다. 이더리움 진영은 로빈후드가 출시한 아비트럼 기반 레이어 2(L2) 체인의 대흥행과 민코인 트레이딩 자금 쏠림 수혜로 <span class=\"text-cyan-300 font-semibold\">유니스왑과 아비트럼의 거래량 급증</span>을 유도하고 있습니다.",
      "key_claims": [
        "SEC는 클레리티 법안의 프레임워크를 차용해 비트코인, NFT/유틸리티, 스테이블코인 등 4대 자산을 <span class=\"text-cyan-300 font-semibold\">비증권 자산으로 확정</span>하고, 7,500만 달러 규모 조달 면제 등 세이프 하버를 제공합니다.",
        "비트코인은 수급적으로 현물 매도 압력이 7월 중순 이후 최저치로 완화되며 과매도 구간을 통과했으나, 불스코 지수가 20에 머물러 <span class=\"text-rose-400 font-medium\">본격적 강세장 전환 확언은 미지수</span>입니다.",
        "로빈후드 L2 출시에 따른 수혜 배분 계약으로 인해 <span class=\"text-cyan-300 font-semibold\">아비트럼(ARB)</span>과 덱스 거래 수수료가 집중되는 <span class=\"text-cyan-300 font-semibold\">유니스왑(UNI)</span>으로 스마트 머니가 빠르게 이동 중입니다."
      ],
      "data_points": [
        "폴리마켓 기준 클레리티 법안 연내 상원 통과 확률: 기존 60%에서 35%로 하락",
        "비트코인 ETF 자금 유입 데이터: 금주 1억 9,000만 달러 순유입 기록 (IBIT 중심 확대)",
        "7월 비트코인 10개년 계절성 성공 확률: 10년 중 8개 연도 상승 마감 (평균 수익률 7.7%, 중간값 8.0%)",
        "로빈후드 L2 체인 출시에 따른 자금 유출입: 메가이더(MegaETH) 체인에서 2억 달러 이상 자금 이탈 후 로빈후드 L2로 유입"
      ],
      "signal": "neutral",
      "signal_reason": "로빈후드 L2 흥행에 따른 아비트럼/유니스왑의 부분적 수혜가 돋보이나, 거시적으로 연준 의사록의 AI 매파 발언 및 TGA 잔고 급증에 따른 유동성 압박이 실질금리 상승을 이끌어 상방을 제한하기 때문입니다.",
      "key_companies": ["Uniswap", "Arbitrum"],
      "insight": "규제 기관(SEC)이 법안 지연을 우회해 가이드라인(토큰 분류법)을 선제 가동한 것은 크립토 업계 전반의 제도화 비용을 대폭 축소하는 획기적 모멘텀입니다. 단, 매크로 측면에서 AI 투자가 물가 상승 요인으로 재정의되어 <span class=\"text-rose-400 font-medium\">연준의 금리 인하 기대가 후퇴</span>하고 있어 암호화폐 전반의 상방 압력이 존재합니다.",
      "action_point": "비트코인 신규 매수는 7월 말 재무부 유동성 회수 구간과 실질금리 상승 추이를 보며 분할 집행하되, 로빈후드 L2 런칭 수혜가 집중되는 <span class=\"text-cyan-300 font-semibold\">아비트럼(ARB) 및 유니스왑(UNI)</span>의 지분 확보 기회로 활용해야 합니다."
    }
  },
  "wHjbqC9L77Q": {
    "primary_topic": "economy",
    "secondary_topics": [],
    "tags": ["두바이부동산", "러시아자금", "우크라이나전쟁", "대체자산", "서방금융제재"],
    "analysis": {
      "summary": "중동 지역의 지정학적 위기가 지속되는 국면에서도 두바이의 부동산 시장이 전례 없는 호황과 강세를 이어가고 있습니다. 이는 서방의 강력한 러시아 금융 제재를 피해 해외 은행 계좌 대신 <span class=\"text-cyan-300 font-semibold\">부동산 실물 자산</span>을 안전한 대체 은행 계좌로 활용하려는 러시아 및 우크라이나의 초고액 자산가들의 자금이 두바이에 집중적으로 유입되었기 때문입니다. 이들의 자금 회수가 급격히 일어나지 않는 한 두바이 부동산 가격의 하방은 당분간 매우 견고하게 유지될 전망입니다.",
      "key_claims": [
        "서방의 제재망을 피해 자산 동결 리스크를 헷지하려는 <span class=\"text-cyan-300 font-semibold\">러시아·우크라이나 재벌 자금</span>이 두바이 부동산 시장에 유입되어 가격을 지탱합니다.",
        "이들에게 두바이 부동산은 현금성 자산을 장기 저장하고 안정적 자본 이득을 취하는 일종의 <span class=\"text-cyan-300 font-semibold\">대체 안전자산 금융 플랫폼</span> 역할을 수행합니다.",
        "중동 지역의 산발적인 군사적 노이즈에도 불구하고 막대한 해외 도피성 유동성이 유입되는 구조적 특수성 덕분에 자산 붕괴 징후가 보이지 않습니다."
      ],
      "data_points": [
        "지정학적 리스크 영향 분석: 중동 분쟁 고조 국면에서도 두바이 부동산 실물 가치는 오히려 견고함 유지"
      ],
      "signal": "neutral",
      "signal_reason": "특정 글로벌 거시 정치적 흐름에 따른 두바이 부동산 시장의 특수 요인을 기술하는 콘텐츠로 국내외 상장 기업 주가에 미치는 직접적 영향은 제한적이기 때문입니다.",
      "key_companies": [],
      "insight": "글로벌 지정학적 분절과 서방의 제재 강화는 차단된 유동성이 두바이 등 제3의 중립적 안전지대 <span class=\"text-cyan-300 font-semibold\">부동산 및 대체 자산</span>으로 집중되게 만드는 풍선효과를 낳고 있습니다. 이는 전통적인 매크로 금리 분석만으로는 설명하기 힘든 자산 배분 왜곡 현상입니다.",
      "action_point": "글로벌 부동산 펀드 및 자산 배분 전략 수립 시, 매크로 금리 상승 압력 외에 서방 금융 제재에 따른 <span class=\"text-cyan-300 font-semibold\">자금 도피성 실물 자산 유입 모멘텀</span>을 지닌 신흥국 주요 부동산 리츠 및 자산군을 차별화하여 평가해야 합니다."
    }
  },
  "wkguH3f4XMw": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["나스닥ETF비교", "QNDX수수료", "아마존회사채", "환율변동효과", "연준대차대조표"],
    "analysis": {
      "summary": "미국 빅테크 기업들이 AI 인프라 자금의 선제적 확보를 위해 대규모 회사채 발행에 돌입하며 유동성을 기술주로 집중시키고 있으나, 최근 아마존의 발행 흥행률 저하 등 시장이 CAPEX 지출의 <span class=\"text-rose-400 font-medium\">실질적 수익 회수 속도</span>를 냉정히 따지기 시작했습니다. 국내 투자자들의 나스닥-100 ETF 투자에서는 환율 1.9% 하락에 따른 환 노출 손실을 고려해야 하며, 장기 보수 비용을 획기적으로 낮춘 신규 ETF(QNDX 등)의 출현에 따라 비용 복리 효과를 극대화할 수 있는 정립식 갈아타기 전략이 중요해진 시점입니다.",
      "key_claims": [
        "아마존의 250억 달러 채권 모집 배수가 1.6배로 둔화된 것은 시장이 빅테크의 무조건적 AI 투자를 맹목적으로 환영하지만은 않는다는 <span class=\"text-rose-400 font-medium\">투자 심리 변화의 강력한 경고</span>입니다.",
        "나스닥-100 장기 적립식 투자 시 총보수 0.08%p 차이는 20년 복리 기준으로 <span class=\"text-amber-300 font-bold\">2천만 원 이상의 수익금 격차</span>(QNDX 보수 0.10% 대 QQQ 0.18%)를 발생시키는 중대 요소입니다.",
        "연준의 대차대조표 축소(QT) 가속화 시 성장주 할인율 압박이 가중되며, 수혜를 입을 대형 은행주(JP모건)와 변동성 수수료 수익이 늘어나는 자산운용사(블랙록) 비중이 포함된 XLF 금융 ETF가 유망 대안이 될 수 있습니다."
      ],
      "data_points": [
        "원달러 환율 및 나스닥 변동 데이터: 나스닥 지수가 1.8% 상승한 반면 원달러 환율이 1.9% 급락하여, 환 노출 계좌 기준 총자산은 오히려 0.9% 손실 발생 (1,300원 선 하방 이탈)",
        "아마존 회사채 조달 스펙: 250억 달러 모집(올해 누적 620억 달러 조달), 청약 경쟁률은 과거 3배 수준에서 1.6배 수준으로 급감",
        "빅테크 회사채 발행 규모 총합 전망치: 올해 말까지 약 5,700억 달러로 전년 대비 4배 급증 예상",
        "나스닥-100 ETF 총보수 비교: QQQ(0.18%), QQQM(0.15%), 신규 QNDX(0.10%로 최저 보수 달성), IQQ(0.11%, 첫해 0.10% 혜택)"
      ],
      "signal": "neutral",
      "signal_reason": "나스닥-100 신규 수수료 인하 경쟁에 따른 장기 비용 절감 전략과 아마존의 회사채 발행을 둘러싼 거시적 신용 시장 변화를 중립적으로 짚어내고 있기 때문입니다.",
      "key_companies": ["BlackRock(BLK)", "JPMorgan Chase(JPM)", "Amazon(AMZN)", "Meta(META)"],
      "insight": "빅테크 회사채 발행 급증은 채권 시장에서 조달된 유동성이 다시 데이터 센터와 반도체 주식으로 공급되는 독특한 환류 작용을 낳고 있습니다. 비용을 낮추는 것이 장기 가투 수익률을 높이는 가장 확실한 길(존 보글의 명언)이듯, 초저보수 나스닥 ETF인 <span class=\"text-cyan-300 font-semibold\">QNDX</span>로의 정립식 자원 재배치가 합리적입니다.",
      "action_point": "연내 실현 이익 250만 원 양도세 허들을 검토하여 기 보유 QQQM은 세금 범위 내 유지하되, 신규 적립 자금은 지정가를 활용하여 초저보수 <span class=\"text-cyan-300 font-semibold\">QNDX</span>로 모아가고 금리 상방 압력을 헤지할 금융 섹터 대장인 <span class=\"text-cyan-300 font-semibold\">JP모건</span> 편입을 고려해야 합니다."
    }
  },
  "zlVuQelTQtY": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["SK하이닉스ADR", "액면분할검토", "빅테크CDS프리미엄", "삼성전자억가", "오라클CDS"],
    "analysis": {
      "summary": "SK하이닉스가 미국 나스닥 ADR 상장(SKY) 성공으로 한국 본주(220만 원) 대비 약 15%의 역사적 ADR 프리미엄(250만 원선)을 획득했으나, 유통 비중(2.5%)이 낮아 차익거래 수렴 속도가 느려 본주의 단기 급등 촉매로는 제한적이므로 추격 매수보다는 220~250만 원 사이의 매물 소화 과정을 확인해야 합니다. 한편 삼성전자의 깜짝 호실적에도 불구하고 주가가 하락한 것은 엔비디아와 같은 창조자(0에서 1) 대비 단순 부품 공급자에 불과하다는 글로벌 펀드매니저들의 <span class=\"text-rose-400 font-medium\">직관적 저평가 왜곡(억가)</span>이 작동했기 때문입니다. 최우선 경계 리스크로 오라클 등 <span class=\"text-rose-400 font-medium\">빅테크 기업들의 신용부도스왑(CDS) 프리미엄 상승 추세</span>를 실시간 체크해야 합니다.",
      "key_claims": [
        "최태원 회장이 용인 투자 등을 위해 ADR 규모의 단계적 추가 확대를 공식화함에 따라 본주와의 차익 갭은 중장기적으로 확실하게 메워질 것입니다.",
        "국내 하이닉스 2배 레버리지 ETF 쏠림(본주 거래량의 최대 3배 기록)에 따른 수급적 꼬리 흔들기 교란은 향후 <span class=\"text-cyan-300 font-semibold\">하이닉스 액면 분할 단행</span> 및 당국 규제를 통해 점진적으로 완화될 수 있습니다.",
        "오라클(CDS 186 돌파) 및 메타, 아마존, 마이크로소프트의 <span class=\"text-rose-400 font-medium\">CDS 프리미엄 전고점 뚫기</span>는 무제한적 AI 투자가 기업 신용 등급에 가하는 장기 위험 요인을 신용 시장이 선제적으로 가격에 반영하고 있음을 의미합니다."
      ],
      "data_points": [
        "SK하이닉스 미국 ADR(SKY) 공모가 대비 마감 가격: 168달러 기록 (원화 약 252만 원선으로 본주 220만 원 대비 15% 프리미엄 형성)",
        "오라클(Oracle) 신용부도스왑(CDS) 프리미엄 지표: 최근 고점 200 터치 후 186 수준에서 등락하며 신용 위험 자극",
        "메타, 아마존, 구글, MS의 CDS 스프레드: 6월 들어 전고점을 모두 상향 돌파하며 빅테크 부채 리스크 반영 중"
      ],
      "signal": "neutral",
      "signal_reason": "ADR 흥행 호재 속에서도 하이닉스 2배 레버리지 ETF의 가격 교란, 9월 메모리 가격 전망 대기, 그리고 무엇보다 빅테크 기업들의 CDS 프리미엄 상승이라는 가려진 거시 신용 리스크를 균형 있게 경고하고 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "Oracle(ORCL)"],
      "insight": "삼성전자 주가에 가해진 글로벌 펀드의 홀대는 일시적인 네러티브 오류입니다. HBM 메모리 수급은 2030년까지 이어질 20년짜리 메가 프로젝트의 일부이며, 9월을 거치며 이익의 지속성이 증명되면 밸류에이션 오해는 빠르게 풀릴 것입니다. 오히려 우리가 더 경계해야 할 것은 빅테크의 무제한 부채 성장과 관련된 <span class=\"text-rose-400 font-medium\">빅테크 CDS 지표의 추가 급등 여부</span>입니다.",
      "action_point": "하이닉스 본주의 250만 원선 매물대 소화 조정 국면을 기다려 분할 진입하되, 오라클 및 메타 등 빅테크 <span class=\"text-rose-400 font-medium\">CDS 스프레드가 200선을 추가 돌파</span>할 경우 성장주 포트폴리오의 비중을 축소하고 일부 현금화하는 신용 리스크 대응 방안을 준비해야 합니다."
    }
  }
}

for vid, val in batch_data.items():
    save_and_delete(vid, val["primary_topic"], val["secondary_topics"], val["tags"], val["analysis"])
print("Batch 5 processing completed.")
