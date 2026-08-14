import json, sys
from pathlib import Path

f_path = Path("data/pending/knhBfqIUI_w.json")
data = json.loads(f_path.read_text(encoding="utf-8"))
video = data.get("video", {})

batch9_data = [{
  "video": {
    "id": video["id"],
    "title": video["title"],
    "published": video["published"],
    "channel_name": video["channel_name"],
    "url": video["url"],
    "thumbnail": video["thumbnail"]
  },
  "analysis": {
    "summary": "역대 연준 의장들의 키(폴 볼커 201cm부터 자넷 옐런 152cm까지)와 기준 금리 추이 간의 오랜 월가 밈(Meme)과 함께 차기 연준 의장 지망 후보 <span class=\"text-cyan-300 font-semibold\">케빈 워시(Kevin Warsh, 키 185cm)</span>의 통화 정책 성향을 위트 있게 분석함. 케빈 워시의 매파적/비둘기파적 스탠스와 연준 지배구조에 미치는 영향을 전망함.",
    "key_claims": [
      "폴 볼커 시대 고금리부터 자넷 옐런 시대 제로금리까지 연준 의장의 신장 변화와 기준금리 동향을 연결 짓는 월가의 유머러스한 비하인드 스토리가 화제임.",
      "제롬 파월의 뒤를 이을 지명 후보로 거론되는 케빈 워시(185cm) 전 연준 이사의 정책 색깔과 통화 정책 미학을 조명함.",
      "<span class=\"text-amber-300 font-bold\">차기 연준 의장 지명 및 금리 향방</span>이 연준 독립성과 금융 시장의 새로운 변수가 될 것임."
    ],
    "data_points": [
      "역대 연준 의장 신장: 폴 볼커(201cm), 앨런 그린스펀(180cm), 벤 버냉키(173cm), 재닛 옐런(152cm)",
      "케빈 워시 신장: 185cm (제롬 파월보다 소폭 큼)",
      "관련 후보: 케빈 워시 전 연준 이사"
    ],
    "signal": "neutral",
    "signal_reason": "월가 밈과 차기 연준 의장 인물 성향 분석 콘텐츠로 시장 시그널은 중립임.",
    "key_companies": [
      "Federal Reserve",
      "언더스탠딩"
    ],
    "insight": "연준 의장의 교체 시점마다 인물 성향 분석과 정책 기조(매파 vs 비둘기파)에 대한 월가의 신호 해석이 매크로 자산 시장의 핵심 변동성을 유발함.",
    "action_point": "차기 연준 의장 지명 인물들의 발언과 통화정책 스탠스를 주시하며 금리 피벗 방향성에 대비해야 함."
  },
  "classification": {
    "primary_topic": "economy",
    "secondary_topics": ["etc"],
    "tags": ["연준의장", "케빈워시", "폴볼커", "기준금리", "월가밈"]
  }
}]

Path("scratch/batch9_analysis.json").write_text(json.dumps(batch9_data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Wrote batch 9 to scratch/batch9_analysis.json")
