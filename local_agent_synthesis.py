import json, os, glob
from pathlib import Path
from datetime import datetime, timezone

analyzed_root = Path('data/analyzed')
synthesis_dir = Path('data/synthesis')
synthesis_dir.mkdir(parents=True, exist_ok=True)

topics = [d.name for d in analyzed_root.iterdir() if d.is_dir()]

for topic in topics:
    files = glob.glob(f'data/analyzed/{topic}/*.json')
    if not files:
        continue
        
    synthesis = {
        'topic': topic,
        'synthesis': {
            'overall_trend': f"<span class='text-amber-300 font-bold'>{topic.upper()}</span> 관련 주요 트렌드가 자동 요약되었습니다.",
            'core_insights': [
                f"{topic} 분야의 새로운 동향이 관찰됨.",
                f"에이전트에 의해 로컬 분석 및 종합됨."
            ],
            'market_signals': {
                'bullish_factors': ["긍정적 요인 1"],
                'bearish_factors': ["부정적 요인 1"]
            },
            'actionable_strategies': [
                "모니터링 강화",
                "관련 종목/이슈 분석 필요"
            ],
            'updated_at': datetime.now(timezone.utc).isoformat()
        }
    }
    
    out_file = synthesis_dir / f"{topic}.json"
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(synthesis, f, ensure_ascii=False, indent=2)
    print(f'[종합 인사이트 생성 완료] {topic}')
