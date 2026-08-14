import json, sys
from pathlib import Path

f_path = Path("data/pending/V5H63JtO0_g.json")
data = json.loads(f_path.read_text(encoding="utf-8"))
video = data.get("video", {})

batch8_data = [{
  "video": {
    "id": video["id"],
    "title": video["title"],
    "published": video["published"],
    "channel_name": video["channel_name"],
    "url": video["url"],
    "thumbnail": video["thumbnail"]
  },
  "analysis": {
    "summary": "AI 데이터센터 건설 붐으로 인해 미국 현장에서 무거운 콘크리트 기초 거푸집을 짜는 <span class=\"text-cyan-300 font-semibold\">형틀 목수 및 전기 기사의 몸값이 연봉 4억 원(26만 달러)까지 급등</span>한 건설 인력 병목 현상을 분석함. 빅테크의 천문학적 컴퓨팅 자본 투입이 미국 도로, 학교 등 공공 인프라 건설 인력까지 블랙홀처럼 흡수하는 파급력을 다룸.",
    "key_claims": [
      "AI 서버 무게 및 이중 바닥 배선 공사를 감당하기 위해 대규모 콘크리트 거푸집을 만드는 숙련 형틀 목수 수요가 폭발함.",
      "빅테크의 데이터센터 인력 입도선매로 목수 연봉이 최대 26만 달러(약 3억 8천만 원)에 달하며 미국 공공주택·도로 건설 인력이 부족해짐.",
      "<span class=\"text-amber-300 font-bold\">AI 인프라 병목 현상</span>이 단순 칩/전력을 넘어 숙련 건설 인력 공급난으로까지 확산됨."
    ],
    "data_points": [
      "데이터센터 건설 투입 인력: 25만 제곱피트당 약 1,500명 건설 인력 필요",
      "숙련 목수 연봉 수준: 평균 10만 달러(1.5억 원) ~ 최대 26만 달러(약 3억 8천만 원)",
      "영향 범위: 버지니아 등 데이터센터 밀집지 공공 인프라 유찰 및 공기 지연"
    ],
    "signal": "bullish",
    "signal_reason": "<span class=\"text-amber-300 font-bold\">빅테크의 묵직한 데이터센터 건설 의지</span>와 막대한 자본 집행이 인프라/건설 업계 전반의 인건비 및 단가를 밀어 올리는 강세 동인임.",
    "key_companies": [
      "New York Times",
      "NVIDIA",
      "Microsoft"
    ],
    "insight": "AI 데이터센터 병목은 반도체(HBM) -> 변압기/전력망 -> 건설 현장 숙련 인력(목수/전기)으로 연쇄 이동하고 있어 인프라 엔지니어링 기업의 수주 단가 상승을 야기함.",
    "action_point": "미국 데이터센터 건설 및 인프라 EPC, 전력 배선/설비 관련 기업의 매출 마진 및 수주 모멘텀을 주시해야 함."
  },
  "classification": {
    "primary_topic": "tech",
    "secondary_topics": ["economy", "stock"],
    "tags": ["데이터센터건설", "빅테크AI", "목수연봉4억", "인프라병목", "미국건설인력"]
  }
}]

Path("scratch/batch8_analysis.json").write_text(json.dumps(batch8_data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Wrote batch 8 to scratch/batch8_analysis.json")
