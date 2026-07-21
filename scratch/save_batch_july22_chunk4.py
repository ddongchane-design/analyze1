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

batch_4 = {
  "jBK9j9d1c2I": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["신용융자1.4조달러", "오라클신용강등", "BBB-투기직전", "반대매매리스크", "외국인차익실현"],
    "analysis": {
      "summary": "미국 신용 융자 잔고가 GDP 수준인 1.4조 달러로 폭증하며 닷컴버블(1999) 및 금융위기(2007) 직전과 유사한 강제 청산(마진콜) 위기 경보가 발령되었습니다. 무리한 채권 발행으로 데이터센터를 짓던 오라클의 신용등급이 투기 등급 직전인 'BBB-'로 강등되며 소프트뱅크와 함께 주가가 3월 수준으로 폭락했습니다. 외국인들은 한국 반도체 기업의 피를 흘리는 적자 구간에 지분을 사들여 고수익 흑자 구간에서 차익 실현하는 패턴을 재현하고 있습니다.",
      "key_claims": [
        "미국 주식 담보 대출(Margin Debt)이 1.4조 달러로 폭증해 전년 대비 50% 이상 늘어난 역대 4번째 구간 진입 (과거 3번은 -40% 폭락 유발).",
        "S&P가 무리한 CAPEX 채권 발행을 감행한 오라클의 신용등급을 정크펀드 직전인 BBB-로 강등해 빅테크 채권 리스크를 촉발했다.",
        "외국인 투자자들은 국내 반도체가 장기 적자 상태일 때 50% 이상 지분을 확보해 최적의 흑자 고점 구간에서 차익을 실현하는 박스피 매매를 반복 중이다."
      ],
      "data_points": [
        "미국 주식 담보 대출 규모: 1.4조 달러 (미국 GDP 상당 수준)",
        "오라클 신용등급: BBB- (투기 등급 바로 전 단계로 강등)"
      ],
      "signal": "negative",
      "signal_reason": "미국 신용 융자의 역사적 고점 도달에 따른 반대매매 청산 위험과 오라클 등 빅테크 채권 신용등급 강등에 따른 금융 경색 우려가 높아졌기 때문입니다.",
      "key_companies": ["Oracle(ORCL)", "SoftBank(9984.T)", "Samsung(005930)"],
      "insight": "레버리지 비율이 GDP 수준까지 오른 장세는 작은 악재에도 시장가 반대매매 청산 도미노를 유발합니다. 특히 신용등급이 강등된 오라클의 채권 부실화에 유의해야 합니다.",
      "action_point": "고부채 테크 채권 및 레버리지 상품의 비중을 대폭 낮추고, 펀더멘탈이 확실한 무부채 반도체 대형주 중심의 안정성을 확보해야 합니다."
    }
  },
  "PmeCeihxEQA": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["키미K3오픈웨이트", "자체서버호스팅", "KVCache부족", "HBM수요증가", "메모리TAM확대"],
    "analysis": {
      "summary": "유니스토리자산운용 김장열 센터장은 중국 Kimi K3가 코드 전체를 주는 오픈소스가 아닌 가중치만 제공하는 '오픈 웨이트(Open-Weight)' 모델임을 명확히 분석했습니다. 기업들이 이를 다운받아 자체 GPU 서버에 호스팅함에 따라 중앙 집중형 대비 메모리(HBM/DRAM)의 전체 시장(TAM)이 오히려 크게 확대됩니다. 2.8조 파라미터를 저장하느라 HBM의 75% 이상이 소진되어 KV 캐시 용량이 부족해지므로, 시스템 DDR5 및 eSSD로의 메모리 확장 수요가 더욱 비약적으로 늘어납니다.",
      "key_claims": [
        "Kimi K3는 오픈소스가 아닌 '오픈 웨이트' 모델로, 기업들이 자체 서버에 다운로드하여 독자 호스팅하므로 엔드포인트별 독립적 HBM/DRAM 수요를 폭증시킨다.",
        "MoE(전문가 혼합) 구조가 단위당 연산량은 줄여주지만, 2.8조 파라미터를 기억하기 위해 HBM 용량(2TB 중 1.5TB)을 독점하므로 대화 임시 메모리(KV 캐시) 고사를 방지하기 위해 외장 DDR5/eSSD 추가 구매가 필연적이다."
      ],
      "data_points": [
        "Kimi K3 파라미터 수: 2.8조 개 (이전 모델 대비 4배 증가)",
        "HBM 용량 할당: 2TB 용량 중 1.5TB가 파라미터 기억용으로 즉시 소진"
      ],
      "signal": "positive",
      "signal_reason": "Kimi K3 오픈 웨이트 모델의 보급이 기업들의 독립적인 HBM 및 외장 DDR5/eSSD 메모리 탑재 수요를 획기적으로 늘리는 촉매제임이 입증되었기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "오픈 웨이트 모델의 유행은 각 기업마다 개별 AI 서버를 구축하도록 만들어 메모리 시장의 전체 파이(TAM)를 키웁니다. 파라미터가 커질수록 HBM과 eSSD의 병목 현상은 심화됩니다.",
      "action_point": "Kimi K3 등 오픈 웨이트 모델 확산에 따른 고용량 서버용 DDR5 및 eSSD 제조업체(SK하이닉스, 삼성전자)의 중장기 비중을 확대해야 합니다."
    }
  },
  "4X8hIvke3oc": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["반도체선반영오류", "JP모건보고서", "PR3.8배역대최저", "2028년쇼티지지속", "밸류에이션극저평가"],
    "analysis": {
      "summary": "월텍남 분석은 시장이 2027~2028년 하반기 공급 과잉 우려를 5~6개 분기나 성급하게 선반영하여 메모리 주가를 과도하게 하락시켰다고 지적했습니다. JP모건 리포트 역시 2028년 전까지 의미 있는 공급 확대가 없으며 마이크론(PER 5.8배), 하이닉스·삼성전자(PER 3.8배) 등 밸류에이션이 역대 최저 수준으로 떨어져 있어 실적 발표를 기점으로 강력한 랠리가 올 것을 선언했습니다.",
      "key_claims": [
        "반도체 사이클은 통상 2~3분기 앞서 선반영하나, 현재 시장은 2027~2028년 증설 우려를 6분기 이상 지나치게 빨리 반영하는 오류를 범했다.",
        "JP모건 미슬라브 마테이커 팀은 2028년 전까지 대규모 공급 추가가 불가능하므로 현 시점의 주가 하락 반영은 비논리적이며 밸류에이션 매력이 극대화되었다고 진단했다.",
        "과거 메모리 턴어라운드와 달리 이번 사이클은 적자 전환 없이 2028년까지 하이닉스 400조 원대, 삼성전자 800조 원대의 훌륭한 영업이익이 지속된다."
      ],
      "data_points": [
        "메모리 포워드 PER: 마이크론 5.8배, SK하이닉스 3.8배, 삼성전자 3.8배 (역사적 바닥권)",
        "빅테크 기술주 포워드 PER: 평균 12배 수준 (5년 평균 27배 대비 반토막 저평가)"
      ],
      "signal": "positive",
      "signal_reason": "메모리 포워드 PER 3.8배라는 역사적 과매도 상태와 2028년까지 꺾이지 않는 실적 전망, JP모건의 강한 바닥 진단이 강력한 주가 반등을 담보하기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "Micron(MU)", "NVIDIA(NVDA)"],
      "insight": "과거 메모리 반도체는 적자를 반영해 PER 3배일 때 고점이었으나, 이번 사이클은 HBM과 AI 장기 계약 덕분에 막대한 흑자가 유지되는 PER 3.8배의 절호의 저가 매수 기회입니다.",
      "action_point": "과도한 5분기 선반영으로 주가가 짓눌린 SK하이닉스, 삼성전자 및 마이크론을 적극 저가 매수하여 밸류에이션 정상화 랠리에 대비해야 합니다."
    }
  },
  "Rl2FNhq2njc": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["클로징벨", "매수사이드카", "코스피3.7%상승", "마이크론FCF호조", "8월8000포인트랠리"],
    "analysis": {
      "summary": "클로징벨 라이브는 코스피가 매수 사이드카 발동과 함께 3.7% 폭등한 6,761선으로 마감했으며 외국인과 기관이 2조 원 넘게 동반 순매수했다고 전했습니다. 마이크론의 잉여현금흐름(FCF) 호조로 자사주 매입 및 배당 확주 가시성이 높아진 가운데, 시장은 7월 중 7,000 포인트를 회복하고 8월 중 8,000 포인트를 노리는 잔잔한 추세 랠리로 진입할 전망입니다.",
      "key_claims": [
        "코스피 지수가 3.7% 폭등하며 매수 사이드카가 발동되었고, 외국인과 기관이 2조 원 이상을 동반 매수하며 저점 반등을 완성했다.",
        "마이크론의 잉여현금흐름(FCF)이 대폭 개선되어 주주 환원 여력이 확충됨에 따라 빅테크 대비 현금 창출력이 뛰어난 반도체로 자금이 쏠리고 있다.",
        "7월 말 실적 시즌을 거쳐 지수가 7,000선에 안착한 뒤 8월부터 본격적인 8,000pt 탈환 랠리가 전개될 것이다."
      ],
      "data_points": [
        "지수 종가: 코스피 6,761pt (+3.7%), 코스닥 753pt (+0.5%)",
        "수급: 개인 2조 원 순매도, 외국인·기관 동반 2조 원 이상 순매수"
      ],
      "signal": "positive",
      "signal_reason": "매수 사이드카 발동과 외국인·기관 2조 원 동반 순매수로 수급 악재가 완벽히 소멸하고 8월 랠리의 발판이 마련되었기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "Micron(MU)"],
      "insight": "개인 투매 물량 2조 원을 외국인과 기관이 완전히 삼키며 지수 추세 전환의 기틀이 완성되었습니다. 현금 흐름이 훌륭한 반도체 대형주가 반등을 주도합니다.",
      "action_point": "매수 사이드카가 발동한 반도체 주도주 비중을 유지하고, 8월 랠리를 목표로 코스피 대형 우량주 포트폴리오를 공고히 해야 합니다."
    }
  },
  "2otaEljkFPc": {
    "primary_topic": "etc",
    "secondary_topics": ["tech"],
    "tags": ["초전도체역사", "저항0실증", "카메를링오너스", "지속유도전류실험", "BCS이론"],
    "analysis": {
      "summary": "안될과학 교양 특강은 1911년 카메를링 오너스가 액체 헬륨으로 4.2K 극저온에서 수은의 전기저항이 완전한 '0'이 되는 초전도 현상을 발견한 과학적 역사와 실증 실험을 해설했습니다. 격자 진동이 정지하여 전자가 저항 없이 흐르는 초전도체 특성은 100년 넘게 물리학의 노벨상을 배출하며 차세대 양자 컴퓨팅, 초고속 전력망 및 초전도 자석 기술의 기초를 형성하고 있습니다.",
      "key_claims": [
        "1911년 오너스는 액체 헬륨 극저온 환경에서 수은의 저항이 서서히 줄어드는 것이 아니라 4.2K에서 뚝 떨어져 정밀하게 '0'이 됨을 발견했다.",
        "초전도 상태에서는 폐회로에 유도된 전류가 저항 없이 영구히 지속되는 무저항 특성을 보이며 현대 초전도 영구자석 및 양자 소자의 기초가 되었다."
      ],
      "data_points": [
        "수은 임계 온도: 4.2 Kelvin (저항 0 도달)"
      ],
      "signal": "neutral",
      "signal_reason": "초전도체의 역사적 발견과 원리를 소개하는 학술 교양 콘텐츠로 시장에 직접적인 단기 수급 영향을 미치지 않기 때문입니다.",
      "key_companies": [],
      "insight": "저항 '0'의 초전도 현상은 양자 컴퓨터(Qubit) 및 AI 데이터센터 전력 손실을 제로화할 수 있는 인류 기술의 최종 지향점입니다.",
      "action_point": "초전도 및 초저온 정밀 장비 관련 장기 R&D 파이프라인의 학술적 진척을 교양 차원에서 모니터링합니다."
    }
  }
}

for vid, data in batch_4.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 4 completed!")
