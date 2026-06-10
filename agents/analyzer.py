import json
import re
import os
from google import genai

ANALYZE_PROMPT = """
당신은 테크/투자 전문 분석가입니다.
아래 유튜브 영상 자막을 분석해서 반드시 JSON 형식으로만 답하세요.

## 절대 규칙
1. 자막에 명시적으로 나온 내용만 사용하세요. 자막에 없는 수치, 기업명, 사실을 추가하지 마세요. (환각 방지)
2. 해당 항목이 자막에 없으면 빈 배열 [] 또는 빈 문자열로 두세요. 억지로 채우지 마세요.
3. key_claims는 "발화자의 주장/의견"이고, data_points는 "검증 가능한 수치/사실"입니다. 둘을 명확히 구분하여 섞지 마세요.
4. data_points의 수치는 자막에 나온 표현 그대로 적으세요 (예: "매출 300% 증가").
5. key_companies는 "기업명(티커)" 형식으로 적으세요. 티커를 모르면 기업명만 적으세요. (예: "테슬라(TSLA)", "스페이스X")

영상 제목: {title}
채널: {channel}
자막: {transcript}

응답 형식 (반드시 유효한 JSON 형식으로만 응답하고, 다른 텍스트는 포함하지 마세요):
{{
  "summary": "3줄 핵심 요약",
  "key_claims": ["발화자의 주장/의견 1", "주장 2"],
  "data_points": ["검증 가능한 수치/사실 1", "수치 2"],
  "signal": "bullish | bearish | neutral | na",
  "signal_confidence": "high | medium | low",
  "signal_reason": "시그널 판단 근거 1~2줄",
  "key_companies": ["기업명(티커) 1", "기업명 2"],
  "insight": "단순 요약이 아닌 핵심 인사이트 (왜 중요한지, 어떤 의미인지)",
  "action_point": "이 영상을 보고 투자자가 주목해야 할 행동 포인트"
}}

* signal은 투자와 무관하거나 순수 기술 소개 영상인 경우 "na"로 설정하세요.
"""

_client = None


def get_client():
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    return _client


def analyze_video(video: dict, transcript: str) -> dict:
    client = get_client()
    prompt = ANALYZE_PROMPT.format(
        title=video["title"],
        channel=video["channel_name"],
        transcript=transcript[:100000]
    )
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={"response_mime_type": "application/json"}
        )
    except Exception as e:
        print(f"  [warn] Gemini 분석 오류: {e}")
        return {}

    try:
        return json.loads(response.text)
    except (json.JSONDecodeError, TypeError) as e:
        print(f"  [warn] JSON 파싱 오류: {e}")
        return {}
