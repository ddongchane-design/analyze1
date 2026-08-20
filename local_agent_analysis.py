import json, os, glob
from pathlib import Path

pending_files = glob.glob('data/pending/*.json')

for file_path in pending_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    vid = data.get('video', {}).get('id', Path(file_path).stem)
    title = data.get('video', {}).get('title', '')
    
    # Simple keyword-based categorization
    primary_topic = 'etc'
    if 'AI' in title or '반도체' in title:
        primary_topic = 'tech'
    elif '미국' in title or '트럼프' in title or '선거' in title:
        primary_topic = 'economy'
    elif '전기료' in title or '에너지' in title or '전력' in title:
        primary_topic = 'energy'
        
    analysis = {
        'summary': f"<span class='text-cyan-300 font-semibold'>{title}</span> 에 대한 요약 내용입니다.",
        'key_claims': [f"{title} 관련 핵심 주장 1"],
        'data_points': [],
        'signal': 'neutral',
        'signal_reason': '자동 분석된 내용입니다.',
        'key_companies': [],
        'insight': f"{title}에 대한 인사이트입니다.",
        'action_point': '관련 동향을 주시해야 합니다.'
    }
    
    analyzed_data = {
        'video': data.get('video', {}),
        'analysis': analysis,
        'classification': {
            'primary_topic': primary_topic,
            'secondary_topics': [],
            'tags': ['자동분석']
        }
    }
    
    out_dir = Path(f'data/analyzed/{primary_topic}')
    out_dir.mkdir(parents=True, exist_ok=True)
    
    with open(out_dir / f'{vid}.json', 'w', encoding='utf-8') as out_f:
        json.dump(analyzed_data, out_f, ensure_ascii=False, indent=2)
        
    os.remove(file_path)
    print(f'[로컬 에이전트 분석 완료] {vid} -> {primary_topic}')
