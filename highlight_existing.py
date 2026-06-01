import os
import json
import time
import random
import re
from pathlib import Path
from google import genai
from dotenv import load_dotenv

load_dotenv()

HIGHLIGHT_PROMPT = """
당신은 제공되는 JSON 오브젝트 내부의 텍스트 값들에 대해 주요 핵심 키워드에 HTML 강조 태그를 씌우는 데이터 정제 전문가입니다.
입력으로 주어지는 JSON 데이터의 구조, 내용, 단어는 절대로 단 1자도 수정하거나 왜곡하지 말고, 오직 중요한 단어나 구절에만 아래의 스펙에 맞는 HTML span 태그를 씌워서 결과만 반환하세요.

[강조 스타일 스펙]
1. 메가 트렌드, 거시 흐름, 핵심 현상/원인: <span class="text-amber-300 font-bold">강조할단어</span>
2. 구체적인 수혜 품목, 세부 기술, 핵심 기업명, 신성장 섹터, 디바이스: <span class="text-cyan-300 font-semibold">강조할단어</span>
3. 시장 경고, 리스크, 투자 위험, 변동성 등 부정 신호: <span class="text-rose-400 font-medium">강조할단어</span>
4. 미중 갈등, 중국 측 자급화 등 지정학적 변화: <span class="text-violet-300 font-medium">강조할단어</span>

주의: 
- 각 문장 전체에 너무 남발하여 태깅하지 말고, 문장이나 문단당 가장 중요도가 높은 단어나 어구 2~3개만 핵심적으로 태깅하세요.
- 마크다운 문법(예: ```json 등)이나 기타 추가 설명 없이 오직 가공이 끝난 유효한 JSON 오브젝트 자체만 그대로 반환하세요.

[대상 JSON 오브젝트]
{json_data}
"""

_client = None

def get_client():
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    return _client

def highlight_analysis(analysis_data: dict) -> dict:
    # API 호출 최소화를 위해 필요한 필드들만 하나의 딕셔너리로 묶어서 보냅니다.
    payload = {
        "summary": analysis_data.get("summary", ""),
        "insight": analysis_data.get("insight", ""),
        "action_point": analysis_data.get("action_point", ""),
        "signal_reason": analysis_data.get("signal_reason", ""),
        "key_claims": analysis_data.get("key_claims", [])
    }
    
    client = get_client()
    prompt = HIGHLIGHT_PROMPT.format(json_data=json.dumps(payload, ensure_ascii=False, indent=2))
    
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            res_text = response.text.strip()
            
            # JSON만 추출하기 위한 정규식 파싱
            match = re.search(r'\{.*\}', res_text, re.DOTALL)
            if match:
                res_text = match.group()
                
            processed_data = json.loads(res_text)
            
            # 원본 데이터에 덮어쓰기
            for k in payload.keys():
                if k in processed_data:
                    analysis_data[k] = processed_data[k]
            return analysis_data
        except Exception as e:
            print(f"    [warn] Gemini API 호출 오류 (시도 {attempt+1}/3): {e}")
            time.sleep(5)
            
    return analysis_data

def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("GEMINI_API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요.")
        return

    analyzed_dir = Path("data/analyzed")
    if not analyzed_dir.exists():
        print("data/analyzed 폴더가 존재하지 않습니다.")
        return

    json_files = list(analyzed_dir.glob("**/*.json"))
    total_files = len(json_files)
    print(f"총 {total_files}개의 분석 JSON 파일을 찾았습니다. 일괄 효율적 하이라이트 처리를 시작합니다...")

    for i, file_path in enumerate(json_files, 1):
        try:
            raw_text = file_path.read_text(encoding="utf-8")
            # 이미 강조 태그가 포함되어 있다면 스킵 (중복 처리 방지)
            if "text-amber-300" in raw_text or "text-cyan-300" in raw_text or "text-rose-400" in raw_text:
                print(f"[{i}/{total_files}] {file_path.relative_to(analyzed_dir)} - 이미 강조 적용됨 (스킵)")
                continue

            data = json.loads(raw_text)
            analysis = data.get("analysis", {})
            if not analysis:
                continue

            print(f"[{i}/{total_files}] {file_path.relative_to(analyzed_dir)} 처리 중...")
            
            # 일괄로 한 번에 API 호출하여 처리
            data["analysis"] = highlight_analysis(analysis)
            
            # 파일 저장
            file_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"  [완료] 저장됨.")
            
            # API 제한(Rate Limit) 방지를 위해 짧은 대기
            time.sleep(random.uniform(3, 5))
            
        except Exception as e:
            print(f"  [오류] {file_path.name} 처리 중 에러: {e}")
            time.sleep(5)

    # 대시보드 재렌더링
    print("\n[렌더링] 모든 파일 가공 완료. HTML 대시보드를 재생성합니다...")
    from agents.orchestrator import render_dashboard
    # 렌더링 시 기존 종합(synthesis) 캐시를 제거하여 새로고침 되도록 유도
    synthesis_dir = Path("data/synthesis")
    if synthesis_dir.exists():
        for syn_file in synthesis_dir.glob("*.json"):
            try:
                syn_file.unlink()
            except Exception:
                pass
    
    render_dashboard()
    print("\n[완료] 모든 대시보드가 성공적으로 갱신되었습니다!")

if __name__ == "__main__":
    main()

