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

batch_7 = {
  "R067Gf1VmwM": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["코스피매수사이드카", "외국인2조순매수", "키옥시아급반등", "마이크론FCF호조", "8월8000포인트"],
    "analysis": {
      "summary": "7월 21일 클로징벨 라이브는 코스피가 매수 사이드카 발동과 함께 3.7% 폭등한 6,761선으로 마감했으며, 외국인과 기관이 개인의 2조 원 투매 물량을 그대로 수용하며 강한 이중 바닥을 다졌다고 보도했습니다. 마이크론의 잉여현금흐름(FCF) 호조와 일본 키옥시아의 급반등에 힘입어 반도체가 7,000pt 지지대를 구축하고 8월 8,000pt 탈환 랠리에 나설 것입니다.",
      "key_claims": [
        "개인 2조 원 매도세를 외국인과 기관이 전액 흡수하며 매수 사이드카를 발동시켰다.",
        "마이크론의 강력한 FCF(잉여현금흐름) 실적과 일본 키옥시아 폭등이 글로벌 반도체 투자 심리를 일제히 회복시켰다.",
        "7월 말 실적 발표 고비를 넘기면 7,000pt를 안착하고 8월 본격적인 8,000pt 탈환 장세가 시작된다."
      ],
      "data_points": [
        "지수 종가: 코스피 6,761pt (+3.7%), 코스닥 753pt (+0.5%)",
        "수급: 개인 2조 3,000억 원 순매도, 외국인 및 기관 동반 순매수"
      ],
      "signal": "positive",
      "signal_reason": "매수 사이드카 발동과 외국인·기관 2조 원대 수급 유입으로 바닥 반등이 확정되었고 8월 랠리의 기틀이 마련되었기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "Micron(MU)"],
      "insight": "개인 투매 물량을 외국인 액티브 자금이 싹쓸이한 자리가 강력한 반등 바닥입니다. FCF가 탄탄한 반도체 대형주 중심의 보유 전략이 맞습니다.",
      "action_point": "외국인이 매집을 재개한 삼성전자와 SK하이닉스 비중을 공고히 유지하고 8월 랠리를 준비해야 합니다."
    }
  },
  "EFo5oBfoI9c": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["포스코국민주1호", "철강이로기업", "2차전지소재", "국민주역사", "주주환원"],
    "analysis": {
      "summary": "1980년대 대한민국 국민주 1호로 출발한 포스코(POSCO)의 역사적 의의와 철강·2차전지 소재·친환경 인프라 그룹으로의 진화 과정을 되짚어본 인터뷰 영상입니다. 국가 기간 산업으로서 주주 가치 환원과 글로벌 가치 재평가를 추진 중입니다.",
      "key_claims": [
        "포스코는 대한민국 국민주 1호 기업으로서 80년대 국경 기업 이익을 국민에게 환원한 역사를 가지고 있다.",
        "철강 소재를 넘어 친환경 2차전지 및 리튬 공급망을 쥐고 국가 경쟁력을 견인하고 있다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "포스코 그룹의 역사와 국민주로서의 위상을 조명한 기업 가치관 해설로 단기 시세 변동성이 제한적이기 때문입니다.",
      "key_companies": ["POSCO홀딩스(005490)"],
      "insight": "대한민국 산업화의 기반이었던 포스코는 친환경 소재 및 리튬 밸류체인으로 그룹 체질을 재정비하고 있습니다.",
      "action_point": "포스코 그룹의 리튬 및 친환경 밸류체인 성과를 장기적 관점에서 모니터링합니다."
    }
  },
  "qsJXr2FAz3A": {
    "primary_topic": "economy",
    "secondary_topics": ["tech", "stock"],
    "tags": ["브라질Pix결제", "중앙은행즉시결제", "비자마스터독점붕괴", "탈달러화", "핀테크혁명"],
    "analysis": {
      "summary": "브라질 중앙은행이 출시한 수수료 0원의 국가 즉시 결제 인프라 '픽스(Pix)'가 폭발적 인기를 끌며 비자(Visa) 및 마스터카드(Mastercard) 등 전통 신용카드사의 결제 망 독점 구조를 뒤흔들고 있습니다. 인도의 UPI, 브라질의 Pix 등 중앙은행 주도의 무료 즉시 결제 망 확산은 카드 수수료 기반 글로벌 수수료 네트워크에 위협이 되고 있습니다.",
      "key_claims": [
        "브라질 중앙은행의 'Pix' 결제 시스템은 카드 수수료 0원 및 QR 기반 즉시 송금으로 신용카드 비중을 위축시켰다.",
        "국가 주도 무료 디지털 결제망 확산은 기존 글로벌 카드사(비자, 마스터)의 결제 수수료 독점 패권을 위협하고 있다."
      ],
      "data_points": [
        "브라질 카드 결제 비중: Pix 도입 후 기존 대비 급감 (무료 24시간 실시간 송금 대체)"
      ],
      "signal": "negative",
      "signal_reason": "글로벌 결제망 시장에서 국가 주도 무료 즉시 결제망(Pix, UPI)의 확산이 기존 카드 네트워크사(Visa, Mastercard)의 수수료 기반 결제 독점을 약화시키기 때문입니다.",
      "key_companies": ["Visa(V)", "Mastercard(MA)"],
      "insight": "중앙은행 주도의 무료 디지털 인프라는 핀테크 결제 지형을 송두리째 바꿉니다. 전통 결제 카드 네트워크사의 수수료 수혜 모델에 장기 균열이 발생하고 있습니다.",
      "action_point": "Visa 및 Mastercard 등 카드 네트워크사 비중을 조절하고, 국가 즉시 결제 인프라 솔루션 기업을 주목해야 합니다."
    }
  },
  "ZF8tP2P3YZU": {
    "primary_topic": "etc",
    "secondary_topics": ["tech"],
    "tags": ["미래에셋콘텐츠", "주키퍼스", "데이터미래", "어린이금융교육", "AI애니메이션"],
    "analysis": {
      "summary": "미래에셋 Smart Money 채널의 주키퍼스 AI 애니메이션 시리즈 3화로, 어린이 및 대중 대상의 데이터와 정보 가치 탐구 교육 콘텐츠입니다.",
      "key_claims": [
        "데이터는 미래 산업의 핵심 자산이며 정밀 문제 해결 능력이 필수적이다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "어린이 교양 AI 애니메이션 콘텐츠로 증시 수급에 직접적 영향이 없기 때문입니다.",
      "key_companies": ["미래에셋증권(006800)"],
      "insight": "금융 및 테크 교육의 대중화 시도가 AI 애니메이션 제작 기술과 결합하고 있습니다.",
      "action_point": "콘텐츠 교양 자료로 참고합니다."
    }
  },
  "8hI9cuKLeXM": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["하이닉스135원역사", "현대전자채권단", "블루칩프로젝트", "HBM재평가", "ROE90%극저평가"],
    "analysis": {
      "summary": "이효석 대표는 2003년 135원 동전주 시절과 2001~2005년 채권단 지배하의 혹독한 블루칩 프로젝트(비용 절감 절체절명 과제)를 극복해낸 SK하이닉스의 독보적인 생존 DNA를 회고했습니다. 현재 HBM 세계 1위 독점력과 ROE 90%를 기록하는 하이닉스가 18만~20만 원선에 거래되는 것은 역사적 최저 수준의 극심한 저평가이며 정면 돌파를 통한 가치 재평가가 신속히 이뤄질 것입니다.",
      "key_claims": [
        "SK하이닉스는 2003년 135원 동전주 위기와 채권단 지배하의 블루칩 프로젝트를 극복해낸 강인한 생존 DNA를 가진 기업이다.",
        "현재 HBM 시장 독점력과 ROE 90% 성과에도 불구하고 주가가 18만~20만 원선에 갇혀있는 것은 역사적 극저평가 상태이다."
      ],
      "data_points": [
        "SK하이닉스 역사적 최저가: 2003년 3월 135원 (현재 18만~20만 원선 거래)"
      ],
      "signal": "positive",
      "signal_reason": "역사적 위기를 극복해낸 하이닉스의 HBM 독점 체격과 ROE 90% 실적이 18만 원대 주가의 강력한 턴어라운드를 담보하기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)"],
      "insight": "135원 동전주 시절을 딛고 세계 최고의 HBM 독점 기업으로 올라선 하이닉스의 체력은 일시적 수급 노이즈로 훼손되지 않습니다.",
      "action_point": "SK하이닉스 18만 원대 저평가 구간에서 적극적인 비중 확대 및 강력 보유 전략을 지속 단행해야 합니다."
    }
  }
}

for vid, data in batch_7.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 7 completed!")
