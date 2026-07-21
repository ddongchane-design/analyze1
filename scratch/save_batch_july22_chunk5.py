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

batch_5 = {
  "oZ94ARjpBPQ": {
    "primary_topic": "tech",
    "secondary_topics": ["economy", "stock"],
    "tags": ["24시간에이전트", "토큰사용량폭증", "하드웨어몰빵위험", "소프트웨어약세", "미국AI종속"],
    "analysis": {
      "summary": "AI 에이전트가 개발자의 야간 24시간 자율 가동 체제로 진화하면서 토큰 소비량이 폭증하고 있으나, 한국이 반도체 판매로 번 자금이 미국 빅테크의 API 결제 대금으로 전액 환수되는 종속 구조가 심화되고 있습니다. 특히 모태펀드 등 국내 VC 자금이 정부 정책을 따라 반도체 하드웨어로만 전격 쏠림으로써, 정작 고부가가치 AI 소프트웨어·모델 생태계가 고사하는 '하드웨어 몰빵 국가'의 위험성이 제기됩니다.",
      "key_claims": [
        "개발자가 밤새 AI 에이전트를 가동하는 24시간 근무 체제로 전환되면서 토큰 소비량이 직전 대비 3배 이상 폭증하고 있다.",
        "한국이 반도체 수출로 번 돈이 오픈AI, 클로드 등 미국 플랫폼 기업의 결제 대금으로 도로 유출되는 부의 종속이 지속된다.",
        "국내 투자 자금이 반도체·하드웨어 메가 프로젝트로만 집중되어 AI 소프트웨어 파워 및 독자 모델 생태계가 자금 가뭄에 시달리고 있다."
      ],
      "data_points": [],
      "signal": "negative",
      "signal_reason": "하드웨어 비중 편중으로 국내 AI 소프트웨어 생태계가 고사하고, 반도체 이익이 미국 빅테크의 토큰 비용으로 환수되는 매크로 불균형이 커지고 있기 때문입니다.",
      "key_companies": ["OpenAI", "Anthropic", "Alphabet(GOOGL)"],
      "insight": "반도체 칩만 판 돈으로 미국 AI 빅테크의 토큰 비용을 대주는 구조를 탈피하려면 국내 소프트웨어 생태계육성과 엔터프라이즈 AI 서비스 수직계열화가 시급합니다.",
      "action_point": "단순 국내 소형 IT 소프트웨어 기업 투자는 보수적으로 임하되, 미국 독점 LLM 플랫폼 및 글로벌 비즈니스 SaaS 기업 중심의 포트폴리오를 유지해야 합니다."
    }
  },
  "GvufwAgVwSA": {
    "primary_topic": "etc",
    "secondary_topics": ["tech"],
    "tags": ["외모와취업률", "사회심리학", "비만율분석", "데이터분석"],
    "analysis": {
      "summary": "체중 관리와 첫인상이 사회적 결혼 확률(29%p 증가) 및 1.5년 후 취업률(26.9%p 증가)에 미치는 정량적 영향을 사회 심리학 데이터로 분석한 교양 숏폼 영상입니다.",
      "key_claims": [
        "체중 관리를 통한 외모 개선이 결혼 및 취업 확률을 25%p 이상 유의미하게 급증시키는 통계적 결과가 확인되었다."
      ],
      "data_points": [
        "결혼/연애 확률 영향: 체중 관리 시 29%p 급증",
        "1.5년 후 취업률 영향: 26.9%p 급증"
      ],
      "signal": "neutral",
      "signal_reason": "사회심리학적 통계 교양 콘텐츠로 금융 시장에 직접적인 영향이 없기 때문입니다.",
      "key_companies": [],
      "insight": "자기 관리 및 헬스케어 메가트렌드(GLP-1 등)가 개인의 사회적 생산성 지표와 정밀 연동되고 있음을 보여줍니다.",
      "action_point": "개인 건강 관리 및 글로벌 헬스케어 유관 지표를 참고합니다."
    }
  },
  "qMMTZ7x5z7I": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["트럼프반도체40%", "HBM대미의존", "미국공장강제", "제조업데이터종속", "옴니버스락인"],
    "analysis": {
      "summary": "SK하이닉스 HBM 매출의 80%가 미국에 집중된 상황에서, 트럼프 행정부가 글로벌 반도체 생산의 40%를 미국 본토로 회수하려는 강경책을 펼침에 따라 국내 투자 축소 및 미국 공장(인디애나 등) 증설이 강제되고 있습니다. 또한 미국이 한국에 GPU 26만 장을 할당하는 대가로 엔비디아의 코스모스(월드 모델) 및 옴니버스(디지털 트윈) 사용을 조건으로 걸어, K-제조업 핵심 데이터가 미국 AI 시스템에 락인(Lock-in)되는 안보적 딜레마가 고조되고 있습니다.",
      "key_claims": [
        "트럼프의 목표는 전 세계 반도체의 40%를 미국에 짓는 것이며, 매출 80%를 미국에 의존하는 삼성과 하이닉스가 미국의 본토 투자 압박을 집중 수용하고 있다.",
        "미국이 한국에 GPU 26만 장을 공급한 배경에는 엔비디아의 월드 모델(코스모스) 및 디지털 트윈(옴니버스) 플랫폼을 사용하게 만들어 한국 제조업 데이터를 미국 AI로 흡수하려는 락인 전략이 존재한다."
      ],
      "data_points": [
        "SK하이닉스 HBM 매출의 대미 의존도: 70~80%",
        "트럼프 반도체 본토 생산 목표치: 전 세계 공급량의 40%"
      ],
      "signal": "negative",
      "signal_reason": "미국 공장 강제 신설에 따른 인건비·CapEx 부담 증가와 대미 제조업 데이터 종속 리스크가 한국 반도체 기업의 장기 마진을 위협하기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "NVIDIA(NVDA)"],
      "insight": "미국의 GPU 공급은 호의가 아닌 '제조업 데이터 락인' 전략입니다. 하이닉스와 삼성전자는 미국 공장 증설에 따른 고비용 구조를 극복해야 하는 과제를 안고 있습니다.",
      "action_point": "미국 인디애나 등 현지 공장 설립 수혜를 입는 반도체 장비/패키징 업체와 엔비디아 옴니버스 생태계 파트너사를 선별적으로 매수해야 합니다."
    }
  },
  "jO-pL17erjY": {
    "primary_topic": "robot",
    "secondary_topics": ["stock", "tech"],
    "tags": ["쿠팡로봇24시간", "전고체배터리필수", "AMR소팅로봇", "보스턴스트레치", "물류자율화"],
    "analysis": {
      "summary": "인천 쿠팡 물류센터 화재 사건을 계기로 축구장 4배 크기의 물류 현장에 24시간 가동되는 수백 대의 자율 이동 로봇(AMR)과 소팅(Sorting) 로봇의 가치가 조명되었습니다. 로봇 1대당 5kWh(전기차 20대 분량) 배터리가 탑재되는 만큼, 화재 위험이 없는 '전고체 배터리' 도입 필요성이 급부상했으며, 보스턴다이내믹스의 스트레치(Stretch) 및 레인보우로보틱스 양팔 로봇의 투입으로 물류 현장의 완벽한 100% 무인화가 눈앞에 다가왔습니다.",
      "key_claims": [
        "쿠팡 물류창고에 수백 대의 AMR 및 소팅 로봇이 24시간 실시간 가동 중이며, 리튬배터리 화재 위험을 완쇄하기 위한 전고체 배터리 수요가 부각된다.",
        "보스턴다이내믹스의 트럭 하역 로봇 스트레치(Stretch)와 레인보우로보틱스의 양팔 상체 로봇이 상용화되어 물류 상하차 및 하차 공정이 완전 자동화되고 있다."
      ],
      "data_points": [
        "물류 로봇 탑재 배터리 용량: 1대당 약 5kWh (수백 대 가동 시 전기차 20대 분량)"
      ],
      "signal": "positive",
      "signal_reason": "쿠팡 등 물류 거점의 24시간 로봇 풀 가동 실증과 스트레치·휴머노이드 상용화로 물류 로봇 및 전고체 배터리 시장의 구조적 성장이 명확해졌기 때문입니다.",
      "key_companies": ["레인보우로보틱스(277810)", "현대차(005380)", "삼성SDI(006400)"],
      "insight": "물류 창고는 휴머노이드와 AMR 로봇이 가장 빠르게 인건비를 대체하는 전초기지입니다. 로봇 안전성 유지를 위한 전고체 배터리와 자율 이동 소프트웨어가 핵심 기술입니다.",
      "action_point": "물류 자율화 로봇 대장주(레인보우로보틱스, 현대차 보스턴다이내믹스 밸류체인)와 안전 배터리(전고체) 공급사의 비중을 확충해야 합니다."
    }
  },
  "Av1yzHS6-RQ": {
    "primary_topic": "tech",
    "secondary_topics": ["stock"],
    "tags": ["하네스엔지니어링", "AI에이전트원년", "토큰사용량100배", "골드만삭스예측", "연산메모리폭증"],
    "analysis": {
      "summary": "AI 엔지니어링의 패러다임이 프롬프트/컨텍스트를 넘어 10~100개의 에이전트를 동시 조율하여 환각을 없애고 자율 과제를 완수하는 '하네스 엔지니어링(Harness Engineering)'으로 전격 진화했습니다. 에이전트가 과제당 수십 번의 추론 연산을 수행함에 따라 개별 개발자의 토큰 사용량이 100배 폭증했으며, 골드만삭스(25배 증가 예측) 등 글로벌 기관들은 연산 및 메모리 하드웨어의 무제한 팽창을 전망하고 있습니다.",
      "key_claims": [
        "AI 프롬프트 시대를 지나 수십 개 에이전트를 유기적으로 통제해 생산성을 극대화하는 '하네스 엔지니어링'이 테크의 핵심 화두로 정착했다.",
        "자율 목표를 수행하는 에이전틱 AI의 특성상 추론 연산과 메모리 사용량이 직전 대비 25~100배 폭증하고 있다."
      ],
      "data_points": [
        "골드만삭스 에이전트 토큰 사용량 예측: 25배 폭증",
        "개별 개발자 실제 토큰 사용량 증가: 100배 폭증"
      ],
      "signal": "positive",
      "signal_reason": "하네스 엔지니어링 및 에이전틱 AI 도입으로 인한 토큰 및 메모리 사용량의 25~100배 폭증이 AI 하드웨어와 반도체 업계의 초장기 슈퍼사이클을 보장하기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "NVIDIA(NVDA)", "Microsoft(MSFT)"],
      "insight": "단순 질문-답변 시대는 끝났습니다. 수십 개의 에이전트가 24시간 독립 연산을 수행하는 하네스 엔지니어링 시대의 개막은 메모리와 GPU의 기하급수적 소비를 의미합니다.",
      "action_point": "에이전틱 AI 구동에 필수적인 초고속 HBM, 고용량 DDR5 및 에이전트 오케스트레이션 플랫폼 기업(MSFT)을 장기 매수해야 합니다."
    }
  }
}

for vid, data in batch_5.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 5 completed!")
