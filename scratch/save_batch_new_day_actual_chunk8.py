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
        print(f"Invalidated cache: {synthesis_cache}")

batch_8 = {
  "dpK5W8XFat4": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["스타게이트프로젝트", "한국투자과밀", "GDP비교", "유동성쏠림", "금리인상요인"],
    "analysis": {
      "summary": "미국의 초대형 AI 인프라 프로젝트인 '스타게이트(5,000억 달러)'는 미국 GDP의 1.7% 수준인 반면, 대한민국이 공표한 반도체 및 인프라 투자 계획(5,000조 원 상당)은 국가 GDP의 2배에 달해 무리한 과밀 투자가 실패할 경우 돌이킬 수 없는 국가적 리스크를 초래할 수 있습니다. 자본이 반도체 하드웨어에 비정상적으로 집중되면서 시장 유동성이 마르고 금리 상승 압력으로 작용해 저성장·고금리 고착화 우려를 가중시키고 있습니다.",
      "key_claims": [
        "미국의 스타게이트 프로젝트는 실패해도 체력이 유지되는 GDP 1.7% 수준의 지출이나, 한국의 5,000조 원대 장기 인프라 계획은 GDP의 2배를 초과하는 극단적 베팅이다.",
        "자금이 반도체 하드웨어 한 축에만 독점 쏠림으로써 시중 자금 순환이 마르고, 화폐 및 신용 가치가 하락하며 결국 시중 금리를 자극해 올리는 원인이 되고 있다.",
        "글로벌 거시 경제가 저성장·저금리 시대에서 반도체 투자 쏠림에 따른 고성장·고물가·고금리 구조로 변형되며 가계와 중소기업의 부채 부담을 가중시키고 있다."
      ],
      "data_points": [
        "미국 스타게이트 프로젝트 투자액: 5,000억 달러 (미국 GDP의 약 1.7%)",
        "한국 총 투자 계획액: 약 5,000조 원 누적 전망 (한국 GDP의 2배 상당)"
      ],
      "signal": "negative",
      "signal_reason": "반도체 하드웨어 집중 투자가 국내 자금 유동성을 고사시키고 금리 하락을 방해하는 매크로 왜곡을 야기하며, 글로벌 대비 국가 GDP 대비 투자 규모가 지나치게 과대해 장기적인 국가 신용 리스크 요인이기 때문입니다.",
      "key_companies": [],
      "insight": "스타게이트는 미국의 방대한 경제 규모 속에서 흡수 가능한 리스크 범위 내에 있으나, 한국의 대형 하드웨어 베팅은 국가의 명운을 건 외줄타기입니다. 자금이 지나치게 반도체로 흡수되면서 다른 내수 산업의 자금난과 고금리 압박이 심화되고 있습니다.",
      "action_point": "장기 국채 금리의 상방 압력 지속에 대비하여 가계 채무 비율을 축소하고, 반도체 외의 내수 산업(소비재, 금융 등)의 유동성 위축 여부를 보수적으로 관리해야 합니다."
    }
  },
  "rIn924lOk1w": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["지정학적리스크", "후티해상봉쇄", "구글프로즌V2", "AMD에저도입", "애플차익실현"],
    "analysis": {
      "summary": "미래에셋증권 데일리 라이브는 뉴욕 증시가 예멘 후티 반군의 사우디 해상 봉쇄 선언 등 중동 지정학적 위기 고조와 유가 상승 여파로 하락 마감했다고 전했습니다. 다만 AMD의 마이크로소프트 에저 클라우드 AI 랙(헬리오스) 도입 공급 계약 체결과 구글의 추론 연산 효율을 10배 개선하는 '프로즌 V2(Frozen V2)' 칩 개발 성과 등 개별 테크사들의 AI 투자 효율화 노력은 활발히 진행 중입니다.",
      "key_claims": [
        "후티 반군이 홍해 및 아라비아 해의 핵심 길목인 바브엘만데브 해협에 대해 즉각적인 사우디 선박 봉쇄를 선언하면서 유가와 안전 자산 선호가 요동쳤다.",
        "마이크로소프트는 엔비디아의 독점을 견제하고 클라우드 마진을 개선하기 위해 AMD의 AI 랙 시스템 헬리오스를 자사 에저 플랫폼에 채택하기로 결정했다.",
        "구글은 제미나이의 연산 전력 효율성을 6~10배 향상하기 위해 추론 알고리즘을 실리콘 칩에 내재화한 신규 가속기 '프로즌 버전2'를 개발하고 있다."
      ],
      "data_points": [
        "주요 종목 종가: 마이크로소프트 +2.15%, AMD +1.58%, 알파벳 +1.51%, 애플 -2.14% (차익 실현 출회)"
      ],
      "signal": "neutral",
      "signal_reason": "후티 반군의 사우디 해상 봉쇄 선언에 따른 유가 인플레이션 우려라는 거시적 악재와, MS-AMD 협력 및 구글 신규 칩 등 빅테크들의 독점 견제 및 AI 비용 효율화 성과라는 호재가 혼재되어 시장이 팽팽한 대치를 보이고 있기 때문입니다.",
      "key_companies": ["Alphabet(GOOGL)", "AMD(AMD)", "Microsoft(MSFT)", "Apple(AAPL)"],
      "insight": "빅테크들의 생존 전략은 AI 비용(전력, 연산 칩 단가)의 극단적 인하입니다. 엔비디아 의존도를 줄이기 위해 AMD의 통합 랙을 대거 도입하고, 알고리즘을 칩에 아예 새겨버리는 '하드웨어 최적화(Frozen V2)'를 통해 마진을 방어하려 하고 있습니다.",
      "action_point": "유가 추이에 따라 정유주 등 헷지 자산을 확보하는 동시에, 엔비디아의 유일한 대안으로 부각되는 AMD와 저전력 추론 가속기 설계 밸류체인에 대해 중장기 관심을 가질 필요가 있습니다."
    }
  },
  "jIimadrlkns": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["네이버엔비디아", "브룩필드합작", "삼바폴리펩타이드", "GLP1비만약생산", "대형마트새벽배송"],
    "analysis": {
      "summary": "네이버 창업진이 캐나다 브룩필드 자산운용 및 실리콘밸리 젠슨 황 회장과의 연쇄 회동을 통해 조 단위 글로벌 AI 팩토리(데이터센터) 인프라 투자를 본격 조율하고 있으며, 삼성바이오로직스는 2.7조 원 규모의 글로벌 펩타이드 의약품 CDMO 강자인 '폴리펩타이드 그룹' 전량 인수를 추진하여 급성장하는 GLP-1 비만약 위탁생산 시장에 전격 진출했습니다. 또한 내수 유통 부문에서는 대형마트의 새벽 배송 허용을 골자로 하는 기본 계획안의 정부 조율이 시작되었습니다.",
      "key_claims": [
        "네이버는 150조 원 규모의 글로벌 AI 펀드를 운영하며 엔비디아와 긴밀히 협력하는 브룩필드(Brookfield) 및 젠슨 황 CEO를 만나 sovereign AI 인프라 자금 유치 및 협력을 추진한다.",
        "삼성바이오로직스는 기존 항체 위주의 포트폴리오를 넘어, 위고비·마운자로 등 글로벌 비만 치료제의 핵심 제제인 펩타이드(Peptide) 생산 역량을 세계 3~4위권인 폴리펩타이드 인수를 통해 확보한다.",
        "정부는 대형마트 영업 제한 완화 및 온라인 배송(새벽배송) 인프라 활용 허용 조치를 담은 유통산업 계획안 수립을 위해 의견 청취 및 유통 상생 기금(1,000억 원) 논의를 본격화했다."
      ],
      "data_points": [
        "삼성바이오로직스 인수액: 폴리펩타이드 그룹 지분 100% 공개 매수, 총 2.7조 원 조달 예정",
        "브룩필드 AI 펀드 자산 규모: 약 150조 원 수준 (쿠웨이트 투자청 및 엔비디아 파트너십 구축)"
      ],
      "signal": "positive",
      "signal_reason": "네이버의 글로벌 자본을 활용한 엔비디아 NCP 생태계 진입과 삼성바이오로직스의 2.7조 원 규모 비만약 CDMO 핵심 회사 인수를 통한 성장성 확보, 대형마트 규제 해소 기조 등 개별 우량사들의 강력한 신성장 동력이 구체화되었기 때문입니다.",
      "key_companies": ["삼성바이오로직스(207940)", "NAVER(035420)", "NVIDIA(NVDA)", "이마트(139480)"],
      "insight": "삼성바이오로직스의 폴리펩타이드 인수는 폭발하는 비만약 생산 수요(Q)를 단번에 흡수하는 신의 한 수입니다. 네이버 또한 자사의 재무 부담을 덜고 브룩필드의 자금과 엔비디아의 기술 지원을 받아 sovereign 데이터센터를 짓는 NCP 전략으로 생태계 내 확장을 꾀하고 있습니다.",
      "action_point": "비만약 파이프라인의 수혜주가 된 삼성바이오로직스와 장기 규제 해소 기대감이 유효한 대형마트(이마트 등)의 비중 확대를 추천하며, 네이버의 조 단위 자본 유치 성과를 면밀히 모니터링해야 합니다."
    }
  },
  "9hVM6IMciLs": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["반도체과밀쏠림", "소프트웨어고사", "스타트업자금난", "코스닥상장폐지규제", "낙수효과부재"],
    "analysis": {
      "summary": "대한민국 주식 시장의 자금이 반도체 하드웨어(삼성전자·SK하이닉스) 대형주로만 극단적으로 몰빵 쏠림 현상을 보이면서, 국내 AI 스타트업과 소프트웨어 생태계가 자금 고사 위기에 직면했습니다. 정부의 코스닥 규제 조치(동전주 퇴출, 300억 원 미만 퇴출 등)가 혁신적인 미래 가치를 지닌 적자 상태의 AI 스타트업들의 신규 자금 조달 창구를 원천 차단하여 IT 생태계 전반의 경쟁력을 좀먹고 있다는 경고가 제기됩니다.",
      "key_claims": [
        "반도체 호황의 낙수효과가 아래단에 있는 국내 AI 소프트웨어, 플랫폼, 솔루션 스타트업으로 흘러가지 못하고 반도체 칩셋 제조사 한 축에 묶여 있다.",
        "재무가 우량하고 영업이익이 나는 우량 기업마저 주가 폭락을 겪는 가운데, 적자 상태에서 기술 스케일업이 필요한 초기 AI 기업들의 투자 유치가 완전 차단되었다.",
        "금융당국의 코스닥 부실사 강제 퇴출 규제가 자금 회수 기간이 긴 스타트업들의 시장 연착륙을 가로막아 코스닥 지수의 만성적 하락과 양극화를 유발한다."
      ],
      "data_points": [
        "규제 기준: 시가총액 300억 원 미만 기업의 강제 퇴출 절차 검토 등 규제 강도 증가"
      ],
      "signal": "negative",
      "signal_reason": "하드웨어 쏠림의 장기화로 소프트웨어 생태계의 자금 공급이 중단되었으며, 규제 중심의 금융 정책이 적자 상태의 기술 혁신 스타트업들의 자본 조달 기회를 빼앗아 한국 테크 전반의 기초 체력을 저하시키기 때문입니다.",
      "key_companies": [],
      "insight": "반도체 칩만 만드는 나라에는 미래가 없습니다. 칩을 기반으로 작동할 AI 소프트웨어와 알고리즘 생태계가 함께 살아가야(공존) 낙수효과가 온전히 발현되는데, 현재 한국은 금융 규제와 수급 쏠림이 겹쳐 혁신 스타트업을 말라 죽이고 있습니다.",
      "action_point": "코스닥 적자 기술 상장사나 소형 테크 스타트업들에 대한 투자를 지양하고, 현금 창출력이 확실한 반도체 대형주 중심의 하드웨어 포트폴리오를 주축으로 삼되 국내 소프트웨어 섹터는 보수적인 관점으로 접근해야 합니다."
    }
  }
}

for vid, data in batch_8.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 8 completed!")
