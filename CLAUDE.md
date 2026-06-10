# YouTube Insight - AI Agent Guide

이 저장소는 유튜브 자막을 AI 에이전트로 분석하여 대시보드 웹페이지를 구성하는 프로젝트입니다. 에이전트는 대화 시작 시 이 가이드를 숙지하고 지침에 따라 개발 및 데이터 처리를 진행해야 합니다.

## 1. 자주 사용하는 명령 (Build & Run Commands)
* **환경 이동**: 모든 작업 및 실행 스크립트는 `youtube-insight` 디렉토리 내부에서 실행합니다. (명령어 실행 전 해당 디렉토리로 이동/지정 필수)
* **대시보드 렌더링**: `python main.py --render` 또는 `python render_only.py`
* **의존성 설치**: `pip install -r requirements.txt`
* **깃 동기화**: `git pull`, `git add output/ data/`, `git commit -m "update: ..."`, `git push`

## 2. youtube-insight 작업 워크플로우 (Daily Analysis Workflow)
사용자가 `data/pending/`에 미분석 자막 JSON 파일을 넣어두고 분석을 요청하면 아래 순서로 병렬 처리합니다.

1. **병렬 서브에이전트 기동**: `data/pending/` 목록을 읽고, 한 번에 대량 분석 시 타임아웃이 발생하므로 **4~5개씩 그룹(Batch)으로 분할**하여 `invoke_subagent` 툴로 병렬 처리합니다.
2. **분석 파일 저장**: 서브에이전트는 분석 완료 후 결과를 `data/analyzed/{primary_topic}/{video_id}.json`에 저장하고, 기존 pending 폴더의 해당 파일을 삭제합니다.
3. **종합 인사이트 갱신**: 분석 완료 후 누락된 토픽의 종합 인사이트(`data/synthesis/`)를 갱신합니다. (※ `economy.json`은 사용자가 수동 수정한 경우 덮어쓰지 않도록 주의합니다.)
4. **렌더링 및 푸시**: `python main.py --render` 명령어로 대시보드를 빌드하고 변경사항을 깃허브에 커밋 & 푸시합니다.

## 3. 데이터 포맷 및 스타일 규칙 (Data & Style Rules)

### [A] 영상 분석 아웃풋 규격 (JSON)
영상 분석 결과는 반드시 다음 형식을 준수해야 합니다.
```json
{
  "summary": "3줄 핵심 요약",
  "key_claims": ["핵심 주장 1", "핵심 주장 2", "핵심 주장 3"],
  "data_points": ["언급된 수치/데이터 1", "수치 2"],
  "signal": "bullish", // bullish, bearish, neutral 중 하나
  "signal_reason": "시그널 판단 근거 1~2줄",
  "key_companies": ["언급 기업/종목 1", "종목 2"],
  "insight": "단순 요약이 아닌 핵심 인사이트 (왜 중요한지, 어떤 의미인지)",
  "action_point": "이 영상을 보고 투자자가 주목해야 할 행동 포인트"
}
```

### [B] HTML 하이라이팅 클래스 적용 규칙 (텍스트 강조용)
분석 결과의 `summary`, `insight`, `action_point`, `signal_reason`, `key_claims` 항목 내 핵심 단어들에 아래 태그를 감싸줍니다. (단락당 2~3개 제한)
* **거시 흐름/원인**: `<span class="text-amber-300 font-bold">강조단어</span>`
* **핵심 기업/부품/기술**: `<span class="text-cyan-300 font-semibold">강조단어</span>`
* **시장 경고/리스크**: `<span class="text-rose-400 font-medium">강조단어</span>`
* **지정학 이슈/공급망**: `<span class="text-violet-300 font-medium">강조단어</span>`

### [C] 주제 분류 (Primary Topic ID)
* `robot`(로봇/피지컬AI), `economy`(경제/매크로), `tech`(테크/AI), `stock`(주식/투자), `energy`(에너지), `crypto`(크립토/암호화폐), `space`(우주산업), `etc`(기타)
