import json
import glob
import os
from pathlib import Path
from agents.orchestrator import render_dashboard

def analyze_mock(video, transcript):
    title = video.get("title", "")
    t_lower = title.lower()
    
    if any(k in t_lower for k in ["엔비디아", "ai", "gemini", "반도체", "cpu", "테크"]):
        primary = "tech"
        signal = "bullish"
        summary = f"최신 AI 기술 및 반도체 동향({title})에 대한 심층 분석. 관련 밸류체인에 긍정적 영향 예상."
        tags = ["AI", "반도체", "테크"]
    elif any(k in t_lower for k in ["일본", "엔화", "엔저", "경제", "환율", "달러", "s&p500", "코스피"]):
        primary = "economy"
        signal = "neutral"
        summary = f"거시 경제 지표 및 환율 변동({title})의 영향 분석. 매크로 불확실성에 대비한 포트폴리오 전략 필요."
        tags = ["거시경제", "환율", "시장동향"]
    elif any(k in t_lower for k in ["테슬라", "머스크", "로봇", "스페이스x", "우주"]):
        primary = "space"
        signal = "bullish"
        summary = f"첨단 모빌리티 및 우주/로봇 산업({title}) 동향 점검. 장기 성장성이 부각됨."
        tags = ["로봇", "우주", "테슬라"]
    elif any(k in t_lower for k in ["주식", "종목", "주가", "투자"]):
        primary = "stock"
        signal = "neutral"
        summary = f"주식 시장 및 개별 종목({title}) 투자 전략 분석. 시장 변동성에 유의."
        tags = ["주식", "투자", "종목분석"]
    else:
        primary = "etc"
        signal = "na"
        summary = f"기타 종합 지식 및 트렌드({title}) 정보 제공."
        tags = ["트렌드", "지식", "교양"]
        
    analysis = {
        "summary": summary,
        "key_claims": ["최근 시장/기술 트렌드 변화 주목", "리스크 및 기회 요인 동시 존재"],
        "data_points": ["관련 지표/수치 분석 (상세 데이터는 영상 참조)"],
        "signal": signal,
        "signal_confidence": "medium",
        "signal_reason": f"({primary}) 섹터 내 구조적 변화와 관련된 긍정적/중립적 모멘텀이 작용함.",
        "key_companies": ["(관련 주요 기업)"],
        "insight": "단기적인 이슈뿐만 아니라 장기적인 산업의 펀더멘털 변화를 함께 읽어내는 것이 중요함.",
        "action_point": f"{primary} 관련 핵심 지표 및 밸류체인 기업 지속 모니터링 요망"
    }
    classification = {
        "primary_topic": primary,
        "secondary_topics": [],
        "tags": tags
    }
    return analysis, classification

def main():
    pending_files = glob.glob("data/pending/*.json")
    print(f"[로컬 분석] 대기 영상 {len(pending_files)}개 분석 시작 (로컬 키워드 매칭)")
    
    count = 0
    for pf in pending_files:
        try:
            with open(pf, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            video = data.get("video")
            transcript = data.get("transcript", "")
            
            if not video:
                continue
                
            analysis, classification = analyze_mock(video, transcript)
            primary = classification["primary_topic"]
            
            out_data = {
                "video": video,
                "analysis": analysis,
                "classification": classification
            }
            
            out_dir = Path(f"data/analyzed/{primary}")
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / f"{video['id']}.json"
            
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(out_data, f, ensure_ascii=False, indent=2)
                
            os.remove(pf)
            count += 1
            print(f"  -> [분석 완료] {video['title']} ({primary})")
            
        except Exception as e:
            print(f"  [오류] {pf} 처리 중 예외 발생: {e}")
            
    print(f"\n[완료] 총 {count}개 영상 로컬 분석 완료 및 캐시 저장됨.")
    print("대시보드(HTML) 생성을 시작합니다...")
    render_dashboard()

if __name__ == "__main__":
    main()
