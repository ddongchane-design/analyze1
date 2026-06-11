import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# 윈도우 환경 등에서 유니코드 출력 시 cp949 인코딩 에러 방지
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# .env 파일에서 환경변수 로드
load_dotenv()

from agents.orchestrator import run, collect_pending, render_dashboard

if __name__ == "__main__":
    if "--collect" in sys.argv:
        collect_pending()
    elif "--render" in sys.argv:
        render_dashboard()
    else:
        if not os.environ.get("GEMINI_API_KEY"):
            print("[경고] GEMINI_API_KEY가 설정되지 않았습니다. API가 필요한 비디오 분석 단계는 스킵되며, 신규 영상 수집 및 대시보드 렌더링만 진행됩니다.")
            collect_pending()
            render_dashboard()
        else:
            run()
