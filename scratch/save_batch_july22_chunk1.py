import json
from pathlib import Path

def save_and_delete(video_id, primary_topic, secondary_topics, tags, analysis_data):
    pending_path = Path(f"data/pending/{video_id}.json")
    if not pending_path.exists():
        print(f"Error: {pending_path} does not exist.")
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
    if synthesis_cache.exists():
        synthesis_cache.unlink()

batch_1 = {
  "1kRudjW7vWE": {
    "primary_topic": "tech",
    "secondary_topics": ["economy", "stock"],
    "tags": ["닷컴버블교훈", "제본스의역설", "광케이블파산사례", "인프라과잉투자", "플랫폼수혜론"],
    "analysis": {
      "summary": "1990년대 닷컴 버블 당시 인터넷 트래픽 폭증이라는 '방향성'은 옳았으나, 해저 광케이블 기업들이 과도한 부채와 조기 과잉 투자로 인프라 수익화를 기다리지 못하고 파산하고 인프라를 저가 매수한 아마존·구글·애플이 최종 승자가 되었던 역사적 교훈이 재조명됩니다. 현재 AI 인프라 구축 사이클 또한 기술의 방향성은 맞으나 하드웨어 과밀 투자로 인한 단기 교착 및 파산 리스크를 유의하고 최종 플랫폼 수혜 기업을 가려내야 합니다.",
      "key_claims": [
        "1990년대 월드컴 등 해저 광케이블 기업들은 인터넷 폭증이라는 방향성은 맞았으나 수익 실현 전 과도한 부채를 견디지 못하고 파산했다.",
        "파산한 인프라를 저렴하게 인수하여 유용한 서비스를 올린 애플, 구글, 아마존 등 2차 소프트웨어/플랫폼 기업들이 최종 부를 독점했다.",
        "AI 반도체 및 하드웨어 역시 제본스의 역설로 수요는 늘지만, 과도한 CAPEX 집행 시 단기 둔화 및 하드웨어 공급사의 마진 압박으로 나타날 수 있다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "AI 인프라의 거시적 방향성은 명확하나, 하드웨어 구축 기업의 과도한 부채와 설치 속도가 실질 수익화를 상회할 경우 버블 조정 및 플랫폼 기업으로의 부의 이전이 일어날 수 있기 때문입니다.",
      "key_companies": ["Amazon(AMZN)", "Alphabet(GOOGL)", "Apple(AAPL)"],
      "insight": "하드웨어를 무리하게 짓는 인프라 건설사보다, 차후 파산 및 저가로 나온 인프라 레이어를 딛고 올라서는 빅테크 플랫폼 서비스 기업의 장기 ROI가 훨씬 뛰어날 수 있습니다.",
      "action_point": "순수 인프라/하드웨어 단일 종목의 부채 비율과 이익 창출 속도를 점검하고, 인프라를 활용해 과금 모델을 수직계열화하는 2차 AI 소프트웨어/플랫폼 기업의 비중을 확충해야 합니다."
    }
  },
  "MwGd-iyja1I": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["빅테크실적전망", "계약잔고RPO", "단수명자산", "마이크로소프트자금력", "코스피매물대"],
    "analysis": {
      "summary": "신영증권 김효진 박사는 빅테크 실적 발표를 앞두고 4대 하이퍼스케일러의 계약 잔고(RPO)가 연간 CAPEX의 2.5배(약 1,000조 원 이상)에 달해 AI 투자 철회 우려는 과도하다고 분석했습니다. 특히 현금 여력이 가장 높고 자산 대비 투자 비율이 57%로 낮은 마이크로소프트(MSFT)가 AI 투자를 주도할 것이며, 실적 발표 시 GPU·서버 등 '단수명 자산(Short-life assets)' 비중이 유지·상승하는지가 반도체 수혜의 핵심 관전 포인트입니다. 한편 코스피는 7,600~8,400선에 쌓인 약 10조 원 규모의 개인 매물 소화 과정에서 지글거리는 횡보 반등을 나타낼 전망입니다.",
      "key_claims": [
        "빅테크 4사의 수주 잔고(RPO)는 1,000조 원을 초과하며 클라우드 매출의 2~6년치가 이미 확정되어 있어 단기 CAPEX 감축 가능성은 매우 낮다.",
        "마이크로소프트는 영업 현금 대비 CAPEX 비율이 57%로 4사 중 가장 낮아 추가 투자 여력이 가장 우수하며, 가장 친절하고 상세한 실적 가이드라인을 제공한다.",
        "투자의 내용 중 GPU, CPU, 서버 등 교체 주기가 짧은 '단수명 자산' 비중(현재 약 2/3 수준)이 유지되는지가 메모리(HBM/DRAM) 업황의 실질 잣대이다."
      ],
      "data_points": [
        "빅테크 4사 수주 잔고(RPO): 약 1,000조 원 이상 (연간 CAPEX의 2.5배 수준)",
        "코스피 매물대 수급: 7,600~7,800선 (2.5조 원), 8,200~8,400선 (4.5조 원), 8,400~8,600선 (3조 원 보유)",
        "마이크로소프트 잉여 현금 대비 CAPEX 비율: 57% (빅테크 중 가장 우량)"
      ],
      "signal": "bullish",
      "signal_reason": "빅테크의 견고한 수주 잔고와 마이크로소프트 중심의 풍부한 현금 여력이 AI 반도체 투자 하방을 든든히 받치고 있어 실적 발표 후 불확실성 해소가 기대되기 때문입니다.",
      "key_companies": ["Microsoft(MSFT)", "Alphabet(GOOGL)", "Amazon(AMZN)", "Meta(META)"],
      "insight": "단순 CAPEX 금액의 증감보다 서버/GPU 등 단수명 자산에 얼마의 예산이 할당되었는지가 핵심입니다. 가장 탄탄한 재무구조를 지닌 마이크로소프트의 컨퍼런스 콜이 반도체 밸류체인의 이정표가 될 것입니다.",
      "action_point": "마이크로소프트의 실적 성명서 내 단수명 자산 비율 및 RPO 증가율을 확인한 후, 메모리 반도체 및 고성능 서버 기판 섹터에 대해 적극적인 눌림목 매수 관점을 유지해야 합니다."
    }
  },
  "cQfEvqtzO3g": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["필라델피아반도체급등", "중동지정학위험", "베라루빈양산", "중국AI기술탈취조사", "TSMC가격을상"],
    "analysis": {
      "summary": "뉴욕 증시는 반도체 지수(SOX)가 5.21% 급등하고 마이크론(+12.17%), AMD(+8%)가 폭등하며 4일 만에 강한 반등세를 시도했습니다. 엔비디아의 차세대 '베라 루빈(Vera Rubin)' AI 가속기 양산 및 4대 클라우드 공급 소식과 UBS의 S&P 500 목표가 상향(8,100pt)이 호재로 작용한 반면, 중동 유가 급등(WTI $84.9, 브렌트 $90 돌파)과 미국 재무부의 중국 AI 모델 기술 탈취 조사 착수 및 TSMC의 10% 가격 인상 방침이 지정학적·비용적 리스크로 대립하고 있습니다.",
      "key_claims": [
        "엔비디아가 차세대 베라 루빈(Vera Rubin) AI 플랫폼의 완전 양산 및 구글, 마이크로소프트, 오라클 공급을 공식 발표하여 기술주 심리를 반등시켰다.",
        "미국 재무장관 스콧 베센트가 중국 AI 모델(Kimi K3 등)의 미국 프런티어 모델 기술 및 데이터 무단 탈취 조사 및 제재 방침을 전격 발표했다.",
        "TSMC가 원자재·전력비 상승과 미국 공장 대규모 투자 비용 보전을 위해 2027년부터 성숙·첨단 공정 가격을 최대 10% 인상하기로 결정했다."
      ],
      "data_points": [
        "주요 지수: 나스닥 +1.29%, 필라델피아 반도체 지수 +5.21%, S&P 500 +0.89%",
        "주요 종목: 마이크론 +12.17%, AMD +1.58%, 인텔 +8.6%, 샌디스크 +14%, 아마존 -0.98%",
        "원자재 및 환율: WTI 유가 $84.9 (+2%), 브렌트유 $90 돌파, 엔달러 환율 163.21엔"
      ],
      "signal": "positive",
      "signal_reason": "엔비디아 베라 루빈의 본격 양산 출하와 메모리 반도체 저가 매수세 유입, S&P 500 상향 조정 등 기술주 중심의 실적 모멘텀이 유동성 리스크를 압도하고 있기 때문입니다.",
      "key_companies": ["NVIDIA(NVDA)", "Micron(MU)", "AMD(AMD)", "TSMC(TSM)", "Intel(INTC)"],
      "insight": "TSMC의 10% 단가 인상은 빅테크의 반도체 조달 비용을 높이지만, 역설적으로 반도체 제조사의 강력한 가격 결정력을 증명합니다. 엔비디아 베라 루빈으로의 세대 교체는 차세대 HBM4 수요를 조기 자극할 것입니다.",
      "action_point": "마이크론 및 엔비디아 밸류체인(HBM, 초고속 메모리) 중심의 매수세를 강화하고, 유가 상방 압력에 따른 에너지 헷지 포트폴리오를 일부 병행하는 것이 유리합니다."
    }
  },
  "OaIcmzUOYqI": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["구축효과", "유동성집중", "금리인상가능성", "코스닥한계기업", "한은기준금리"],
    "analysis": {
      "summary": "국가 GDP의 2배에 달하는 대규모 유동성이 반도체·하드웨어 단 한 축으로 과밀 집중되면서 시중 자금을 고사시키는 '구축 효과(Crowding-out effect)'가 발생하고 있습니다. 이로 인해 한국은행이 기준금리를 최고 5% 수준까지 인상해야 할 압박에 직면해 저금리 시대가 종료되었으며, 코스닥 상장사 중 30%(600여 개사)에 달하는 한계기업(영업이익으로 이자도 못 갚는 기업)의 연쇄 구조조정 및 부실 폭탄 위기가 가시화되고 있습니다.",
      "key_claims": [
        "반도체 단일 산업으로의 막대한 자금 쏠림이 시중 유동성을 고갈시켜 금리 상승을 유발하는 구축 효과가 가속화되고 있다.",
        "고성장·고물가·고금리 구조로의 이행에 따라 한국은행이 기준금리를 5% 수준까지 상향 조율할 가능성이 높아지고 있다.",
        "코스닥 1,800개 상장사 중 30%에 해당하는 600여 개 기업이 영업이익으로 이자도 감당하지 못하는 한계기업으로 금리 폭탄의 직접 충격을 받게 된다."
      ],
      "data_points": [
        "코스닥 한계기업 비중: 전체 1,800여 개 기업 중 약 30% (600개 이상)"
      ],
      "signal": "negative",
      "signal_reason": "하드웨어 투자 쏠림에 따른 구축 효과로 시중 금리가 고착화되고, 코스닥 한계기업 30%의 구조적 부실 위험이 금융 시장 전반의 체력을 약화시키기 때문입니다.",
      "key_companies": [],
      "insight": "자금이 특정 대형 산업으로만 쏠리면 나머지 내수 기업들은 고금리와 자금 가뭄의 이중고를 겪습니다. 부채 비율이 높고 현금 흐름이 적자인 소형 코스닥 기업들의 생존 확률이 급속히 낮아지고 있습니다.",
      "action_point": "이자보상배율이 1 미만인 코스닥 적자 한계 기업 및 고부채 중소형주를 포트폴리오에서 즉시 제외하고, 무부채 우량 대형주 중심의 리밸런싱을 단행해야 합니다."
    }
  },
  "8Yx2c_tozP0": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["월가뉴스레터", "반도체저가매수", "국채금리4.6%", "키미K3기술조사", "오픈AI_MAU천만"],
    "analysis": {
      "summary": "월가 뉴스레터 브리핑은 반도체 섹터의 폭발적인 저가 매수세(마이크론 +12%, AMD +8%, 인텔 +8.6%, 샌디스크 +14%)로 뉴욕 증시가 일제히 급반등했다고 전했습니다. 그러나 유가 상승(WTI $84.5, 브렌트 $90)으로 미국 10년물 국채 금리가 4.63%를 돌파하고 비트코인이 $66,000선으로 치솟는 등 통화 긴축 경계감도 공존합니다. 한편 미국 재무부가 중국 Kimi K3의 앤스로픽 기술 도용 조사에 착수하고, 샘 알트만이 다음 주 국회/백악관에 차세대 GPT-6 모델을 직접 브리핑하는 등 글로벌 AI 주도권 행보가 무더기로 전개 중입니다.",
      "key_claims": [
        "마이크론, AMD, 인텔, 샌디스크 등 반도체 주도주가 일제히 8~14% 폭등하며 기술주 심리를 강하게 견인했다.",
        "유가 상승 여파로 미 10년물 국채 금리가 4.63%까지 치솟고 금값($4,082)과 비트코인($66,000)이 일제히 신기록을 경신했다.",
        "샘 알트만이 다음 주 미국 정부 및 의회 인사들에게 직접 차세대 AI 모델(GPT-6)을 브리핑하며, 5.6 Sol 업데이트 이후 ChatGPT MAU가 1,000만 명을 급격히 돌파했다.",
        "모건스탠리는 소프트웨어 과매도 속에서도 8대 우량주(MSFT, Palo Alto, CrowdStrike, Cloudflare, Datadog, ServiceNow, Snowflake, Shopify)는 독점 해자로 살아남을 것을 확언했다."
      ],
      "data_points": [
        "주요 종목 상승률: 마이크론 +12.17%, 샌디스크 +14%, 웨스턴디지털 +12%, 인텔 +8.6%, AMD +8%, 마벨 +6.7%",
        "금리 및 자산: 미 10년물 국채 금리 4.63%, 금 선물 $4,082/oz, 비트코인 $66,000",
        "슈퍼마이크로컴퓨터(SMCI): 마진율 15~17%로 시장 예상치(8.2%) 2배 달성하며 시간외 +10% 급등"
      ],
      "signal": "positive",
      "signal_reason": "반도체주에 대한 글로벌 기관들의 전폭적인 저가 매입 유입과 슈퍼마이크로컴퓨터의 마진 2배 폭증, ChatGPT 사용자 폭발 등 AI 실질 수요의 가시성이 국채 금리 상승 악재를 압도했기 때문입니다.",
      "key_companies": ["Micron(MU)", "AMD(AMD)", "Intel(INTC)", "Super Micro Computer(SMCI)", "Microsoft(MSFT)"],
      "insight": "SMCI의 마진이 8%에서 17%로 2배 폭등한 것은 AI 서버 및 CPU 쇼티지가 얼마나 극심한지를 보여주는 empircal 증거입니다. 국채 금리가 4.6%로 높아져도 확실한 이익 폭증을 보여주는 반도체/서버 밸류체인으로 수급이 블랙홀처럼 빨려 들어가고 있습니다.",
      "action_point": "상승세를 탄 반도체(마이크론, 인텔, AMD) 및 슈퍼마이크로컴퓨터 관련 서버 부품사에 대한 보유 비중을 늘리고, 모건스탠리가 선정한 8대 우량 AI 소프트웨어(보안, 데이터 플랫폼)주를 골라 담아야 합니다."
    }
  }
}

for vid, data in batch_1.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 1 completed!")
