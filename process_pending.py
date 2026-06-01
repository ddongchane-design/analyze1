import os
import json
import time
import random
import sys
from pathlib import Path
from dotenv import load_dotenv

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

from agents.analyzer import analyze_video
from agents.classifier import classify_video
from agents.orchestrator import render_dashboard
from highlight_existing import highlight_analysis

def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("GEMINI_API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요.")
        return

    pending_dir = Path("data/pending")
    topics = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))["topics"]
    valid_topic_ids = {t["id"] for t in topics}

    pending_files = list(pending_dir.glob("*.json"))
    if not pending_files:
        print("분석할 대기 영상(pending)이 없습니다.")
        return

    print(f"\n[API 분석 시작] 총 {len(pending_files)}개의 수집된 영상 분석 및 하이라이트 처리를 시작합니다...")

    for i, p_file in enumerate(pending_files, 1):
        try:
            data = json.loads(p_file.read_text(encoding="utf-8"))
            video = data["video"]
            transcript = data["transcript"]

            print(f"\n[{i}/{len(pending_files)}] [영상 분석] {video['title']}")
            
            # 1. API를 이용한 분석 수행
            analysis = analyze_video(video, transcript)
            if not analysis:
                print("  [retry] Gemini 오류 - 20초 후 재시도...")
                time.sleep(20)
                analysis = analyze_video(video, transcript)
            if not analysis:
                print("  [skip] 분석 실패 - 대기 상태 유지")
                continue

            # 2. 분류 수행
            classification = classify_video(analysis, topics)
            primary = classification.get("primary_topic", "etc")
            if primary not in valid_topic_ids:
                primary = "etc"

            # 3. 하이라이트 스타일 적용
            print(f"  [하이라이트 적용 중...]")
            analysis = highlight_analysis(analysis)

            # 4. 분석 결과 저장
            result_dir = Path(f"data/analyzed/{primary}")
            result_dir.mkdir(parents=True, exist_ok=True)
            result_path = result_dir / f"{video['id']}.json"
            result_path.write_text(
                json.dumps({"video": video, "analysis": analysis, "classification": classification},
                           ensure_ascii=False, indent=2),
                encoding="utf-8"
            )

            # 5. 대기 파일 삭제
            p_file.unlink()

            # 6. 해당 주제의 종합(synthesis) 캐시 제거하여 갱신 유도
            synthesis_cache = Path("data/synthesis") / f"{primary}.json"
            if synthesis_cache.exists():
                try:
                    synthesis_cache.unlink()
                    print(f"  [cache invalidation] '{primary}' 주제의 종합 캐시를 무효화했습니다.")
                except Exception as e:
                    print(f"  [warn] 캐시 파일 삭제 실패: {e}")

            print(f"  [done] {primary} | signal: {analysis.get('signal', '?')}")
            time.sleep(random.uniform(5, 8))

        except Exception as e:
            print(f"  [error] {p_file.name} 처리 중 오류 발생: {e}")
            time.sleep(5)

    # 7. 대시보드 갱신
    print("\n[렌더링] 모든 영상의 분석이 완료되었습니다. HTML 대시보드를 재생성합니다...")
    render_dashboard()
    print("\n[완료] 대시보드 갱신 완료!")

if __name__ == "__main__":
    main()
