import os
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load env variables
load_dotenv()

# We can also check if GEMINI_API_KEY is in os.environ.
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Warning: GEMINI_API_KEY is not set in environment.")

client = genai.Client(api_key=api_key) if api_key else None

def parse_date(pub_str):
    if pub_str.endswith('Z'):
        pub_str = pub_str[:-1] + '+00:00'
    return datetime.fromisoformat(pub_str)

def get_recent_analyses(topic_id, synthesis_days):
    analyzed_dir = Path(f"data/analyzed/{topic_id}")
    if not analyzed_dir.exists():
        return []
    
    entries = []
    for json_file in analyzed_dir.glob("*.json"):
        try:
            data = json.loads(json_file.read_text(encoding="utf-8"))
            entries.append(data)
        except Exception as e:
            print(f"Error loading {json_file.name}: {e}")
            
    # Sort by published date descending
    entries.sort(key=lambda x: x["video"].get("published", ""), reverse=True)
    
    # Filter by synthesis_days limit
    cutoff = datetime.now(timezone.utc) - timedelta(days=synthesis_days)
    recent = []
    for entry in entries:
        pub_str = entry["video"].get("published", "")
        try:
            pub_dt = parse_date(pub_str)
            if pub_dt >= cutoff:
                analysis_with_date = dict(entry["analysis"])
                analysis_with_date["published_date"] = pub_str[:10]
                recent.append((pub_dt, analysis_with_date))
        except Exception as e:
            print(f"Error parsing date {pub_str} for {entry['video'].get('id')}: {e}")
            # Fallback
            analysis_with_date = dict(entry["analysis"])
            analysis_with_date["published_date"] = pub_str[:10] if pub_str else ""
            recent.append((datetime.min.replace(tzinfo=timezone.utc), analysis_with_date))
            
    # Sort by pub_dt descending
    recent.sort(key=lambda x: x[0], reverse=True)
    
    # Return top 10 analyses
    return [analysis for _, analysis in recent[:10]]

def synthesize_topic(topic_label, analyses):
    if not client:
        raise RuntimeError("GEMINI_API_KEY is missing, cannot call Gemini API.")
        
    prompt = f"""아래는 동일 주제({topic_label})에 대한 여러 영상 분석 결과입니다.
이를 종합하여 교차 인사이트를 도출해주세요.
각 분석 결과에는 영상의 발행 날짜(`published_date`)가 포함되어 있습니다.

## 절대 규칙
1. 최근 날짜의 영상에 더 높은 가중치를 부여하여 흐름을 파악하세요.
2. 분석 대상 기간 내에 시그널의 방향성(예: bearish에서 bullish로 전환 등)이나 컨센서스의 변화가 감지된다면 이를 `cross_insight`와 `divergence`에 명확하게 명시하세요.
3. 반드시 JSON으로만 답하세요.

분석 결과 목록:
{json.dumps(analyses, ensure_ascii=False, indent=2)}

응답 형식:
{{
  "cross_insight": "최근 흐름과 가중치를 반영하여 여러 영상에서 공통으로 나타나는 핵심 트렌드나 시그널 (시각 변화가 있다면 흐름 변화 추이 포함)",
  "consensus": "bullish | bearish | neutral | na",
  "divergence": "영상 간 시각 차이, 논쟁 포인트 혹은 기간 내 컨센서스의 변화 추이",
  "key_themes": ["공통 테마 1", "테마 2", "테마 3"],
  "watch_list": ["주목 종목/섹터 1", "종목 2"]
}}

* consensus 값은 반드시 bullish, bearish, neutral, na 중 하나여야 합니다."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    response_text = response.text
    match = re.search(r'\{.*\}', response_text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise ValueError(f"Failed to parse JSON response: {response_text}")

def main():
    topics = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))["topics"]
    synthesis_dir = Path("data/synthesis")
    synthesis_dir.mkdir(parents=True, exist_ok=True)
    
    for topic in topics:
        topic_id = topic["id"]
        topic_label = topic["label"]
        synthesis_days = topic.get("synthesis_days", 7)
        
        recent_analyses = get_recent_analyses(topic_id, synthesis_days)
        print(f"Topic '{topic_id}' ({topic_label}): found {len(recent_analyses)} analyses in the last {synthesis_days} days.")
        
        if len(recent_analyses) >= 2:
            print(f"Synthesizing topic '{topic_id}'...")
            try:
                synthesis_result = synthesize_topic(topic_label, recent_analyses)
                synthesis_path = synthesis_dir / f"{topic_id}.json"
                synthesis_path.write_text(json.dumps(synthesis_result, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"Saved synthesis to {synthesis_path}")
            except Exception as e:
                print(f"Error synthesizing topic '{topic_id}': {e}")
        else:
            print(f"Skipping topic '{topic_id}' (requires at least 2 analyses).")

if __name__ == "__main__":
    main()
