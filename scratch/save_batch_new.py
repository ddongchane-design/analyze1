import json
from pathlib import Path

def save_analysis(video_id, primary_topic, video_data, analysis_data, classification_data):
    # Create analyzed directory
    analyzed_dir = Path(f"data/analyzed/{primary_topic}")
    analyzed_dir.mkdir(parents=True, exist_ok=True)
    
    # Save file
    result_path = analyzed_dir / f"{video_id}.json"
    result_path.write_text(
        json.dumps({
            "video": video_data,
            "analysis": analysis_data,
            "classification": classification_data
        }, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"Saved: {result_path}")
    
    # Remove from pending
    pending_file = Path(f"data/pending/{video_id}.json")
    if pending_file.exists():
        pending_file.unlink()
        print(f"Removed pending: {pending_file}")
        
    # Invalidate synthesis cache
    synthesis_cache = Path(f"data/synthesis/{primary_topic}.json")
    if synthesis_cache.exists():
        try:
            synthesis_cache.unlink()
            print(f"Invalidated cache: {synthesis_cache}")
        except Exception as e:
            print(f"Error invalidating cache: {e}")

analyses = {
  "j_pBV080t7A": {
    "primary": "etc",
    "video": {
      "id": "j_pBV080t7A",
      "title": "긴 터널은 왜 일부러 S자로 만들까?",
      "published": "2026-06-13T11:00:01+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=j_pBV080t7A",
      "thumbnail": "https://img.youtube.com/vi/j_pBV080t7A/hqdefault.jpg"
    },
    "analysis": {
      "summary": "터널 주행 시 발생할 수 있는 <span class=\"text-amber-300 font-bold\">고속도로 최면 현상</span>(가수면 상태)을 방지하기 위해 터널을 일부러 S자 형태로 설계합니다. 또한, 밝은 곳에서 어두운 곳으로 들어갈 때(블랙홀 현상)와 나올 때(화이트 현상) 운전자의 눈이 적응하도록 진입부 조명을 밝게 설계하는 등 <span class=\"text-cyan-300 font-semibold\">안전 설계 기술</span>이 반영되어 있습니다.",
      "key_claims": [
        "동일한 풍경의 터널을 지속해서 달릴 때 발생하는 <span class=\"text-amber-300 font-bold\">고속도로 최면 현상</span>을 방지하고자 일부러 터널을 S자로 설계한다.",
        "터널 진입 및 진출 시 발생하는 블랙홀·화이트 현상에 대비해 <span class=\"text-cyan-300 font-semibold\">진입로 조명</span>을 밝게 설계해 운전자의 시각 적응을 돕는다."
      ],
      "data_points": [
        "S자 형태의 대표적 예: 인제양양터널 (핸들을 S자로 네 번 꺾도록 설계)"
      ],
      "signal": "neutral",
      "signal_reason": "터널 설계 및 안전 공학에 대한 순수 지식 제공 영상으로, 특정 기업이나 금융 시장에 미치는 직접적 영향은 중립적입니다.",
      "key_companies": [],
      "insight": "고속도로 터널 설계는 단순 최단 거리 연결이 아니라 운전자의 생리적 인지 한계와 도로 안전을 종합적으로 고려한 고도의 <span class=\"text-cyan-300 font-semibold\">인간공학적 설계</span> 결과물입니다.",
      "action_point": "터널 주행 시에는 <span class=\"text-cyan-300 font-semibold\">크루즈 컨트롤</span>에만 의존하지 말고 가벼운 환기나 시선 이동을 통해 고속도로 최면 현상을 스스로 예방하는 안전 운전 습관이 필요합니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": [],
      "tags": ["고속도로최면", "터널설계", "안전공학", "인제양양터널", "교통안전"]
    }
  },
  "jgxEUXsCna8": {
    "primary": "etc",
    "video": {
      "id": "jgxEUXsCna8",
      "title": "그 말이 왜 이렇게 아팠을까 | 지금부터, 미래 #shorts",
      "published": "2026-06-13T05:15:00+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=jgxEUXsCna8",
      "thumbnail": "https://img.youtube.com/vi/jgxEUXsCna8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "청년들의 진로 선택과 <span class=\"text-amber-300 font-bold\">대기업 선호 현상</span>에 대한 고민을 다룬 숏폼 영상으로, 남들이 알아주는 대기업만이 정답이 아닐 수 있다는 메시지를 던집니다.",
      "key_claims": [
        "대기업 선호의 주된 이유가 '남들의 평판' 때문일 수 있다.",
        "대기업 입사만이 인생의 유일한 정답이나 목표가 아닐 수 있다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "개인의 진로 선택 및 가치관에 관한 숏폼 에세이 영상으로 시장이나 특정 종목에 미치는 영향은 없습니다.",
      "key_companies": [
        "미래에셋증권"
      ],
      "insight": "성공의 기준을 타인의 시선이나 대기업 입사라는 획일적인 기준에 맞추기보다, 주도적으로 본인의 <span class=\"text-cyan-300 font-semibold\">커리어 경로</span>를 탐색하는 자세의 중요성을 환기합니다.",
      "action_point": "획일적인 진로 고민에서 벗어나 장기적인 관점에서 개인의 역량을 강화하고 가치관에 맞는 <span class=\"text-cyan-300 font-semibold\">커리어 설계</span>를 해야 합니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": [],
      "tags": ["진로고민", "커리어", "대기업선호", "동기부여", "미래에셋"]
    }
  },
  "myxeGj0bCC4": {
    "primary": "robot",
    "video": {
      "id": "myxeGj0bCC4",
      "title": "로봇 스포츠...생각보다 빨리온다 현대차 아틀라스 월드컵",
      "published": "2026-06-13T10:53:13+00:00",
      "channel_name": "엔지니어TV",
      "url": "https://www.youtube.com/watch?v=myxeGj0bCC4",
      "thumbnail": "https://img.youtube.com/vi/myxeGj0bCC4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "유니트리, 피규어 AI, 보스턴 다이내믹스 등 글로벌 휴머노이드 로봇들의 축구, 격투기(UFC) 등 <span class=\"text-amber-300 font-bold\">로봇 스포츠 경연</span> 시연이 예상보다 빠르게 다가오고 있습니다. 하드웨어 완성도가 높아짐에 따라 AI 학습(<span class=\"text-cyan-300 font-semibold\">월드 모델</span>)을 통한 행동 제어가 고도화되고 있으며, 이는 로봇 산업의 새로운 촉매제가 될 것입니다.",
      "key_claims": [
        "휴머노이드의 보행과 주행 성능이 안정화되면서 <span class=\"text-cyan-300 font-semibold\">로봇 축구</span>와 <span class=\"text-cyan-300 font-semibold\">로봇 격투기</span>가 현실화되고 있다.",
        "중국의 유니트리, 엔진 AI, 그리고 현대차 산하의 보스턴 다이내믹스(아틀라스) 등이 스포츠 분야 시연 경쟁을 벌이고 있다.",
        "피규어 AI(Figure AI)는 라이다 없이 <span class=\"text-cyan-300 font-semibold\">비전 카메라</span>만으로 계단을 오르내리는 11분 분량의 무편집 실주행 영상을 공개했다."
      ],
      "data_points": [
        "피규어 AI 계단 보행 주행 시간: 11분 (라이다 없이 카메라 비전만 사용)",
        "중국 로봇 전시회 및 로봇 올림픽 개최 시기: 8월"
      ],
      "signal": "bullish",
      "signal_reason": "휴머노이드 로봇의 스포츠 분야 적용 및 비전 기반 AI 제어 기술(피규어 AI 등)의 급진적 발전은 <span class=\"text-cyan-300 font-semibold\">로봇 하드웨어</span> 및 인공지능 제어 부품 시장의 성장을 가속화합니다.",
      "key_companies": [
        "현대자동차",
        "보스턴다이내믹스",
        "유니트리",
        "피규어AI",
        "엔진AI"
      ],
      "insight": "로봇의 스포츠 경연이나 일상생활 경연은 단순한 쇼를 넘어, 복잡한 환경에서의 실시간 비전 처리, <span class=\"text-cyan-300 font-semibold\">월드 모델 AI</span>, 균형 제어 등 최고 난도의 <span class=\"text-cyan-300 font-semibold\">피지컬 AI</span> 기술이 집약된 실증 무대입니다.",
      "action_point": "8월 예정된 <span class=\"text-cyan-300 font-semibold\">중국 로봇 올림픽</span>과 보스턴 다이내믹스의 아틀라스 월드컵 시연 가능성을 주시하며, 로봇 부품(<span class=\"text-cyan-300 font-semibold\">감속기</span>, 모터) 및 AI 비전 카메라 밸류체인에 주목해야 합니다."
    },
    "classification": {
      "primary_topic": "robot",
      "secondary_topics": [
        "tech",
        "stock"
      ],
      "tags": ["휴머노이드", "아틀라스", "피지컬AI", "피규어AI", "유니트리", "로봇축구", "보스턴다이내믹스"]
    }
  },
  "uYF8dtaF-zg": {
    "primary": "tech",
    "video": {
      "id": "uYF8dtaF-zg",
      "title": "이제 Zoom에서 Google Meet로? 구글 실시간 번역 기술 ㄷㄷ",
      "published": "2026-06-13T10:38:23+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=uYF8dtaF-zg",
      "thumbnail": "https://img.youtube.com/vi/uYF8dtaF-zg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "구글이 <span class=\"text-cyan-300 font-semibold\">Google Meet</span> 등 다양한 플랫폼에 API 형태로 실시간 음성 통역 기술을 탑재하면서 언어 인프라 시장 장악력을 넓히고 있습니다. 이는 기존 개인용 번역 앱 수준을 넘어 B2B 온라인 회의, 교육, 콜센터 등의 대규모 비즈니스 영역에서 비용 절감과 함께 고성능 <span class=\"text-cyan-300 font-semibold\">번역 API</span> 수요를 촉진하고 있습니다.",
      "key_claims": [
        "구글은 단순 번역 결과 제공을 넘어 실시간 음성 입출력 전체를 처리하는 <span class=\"text-cyan-300 font-semibold\">실시간 언어 인프라</span> 레이어가 되고자 한다.",
        "Google Meet 내에 실시간 통역이 내장되면 전문 통역사 섭외비 등 높은 <span class=\"text-rose-400 font-medium\">B2B 통역 비용</span>을 혁신적으로 절감할 수 있다.",
        "개인용 앱과 달리 API 기반 서비스는 기업, 개발자, 플랫폼 단위 과금이 이루어지므로 사용량과 수익 규모가 기하급수적으로 확대된다."
      ],
      "data_points": [],
      "signal": "bullish",
      "signal_reason": "구글의 B2B 실시간 음성 통역 인프라 확장은 기존 줌(Zoom) 등 화상회의 시장 판도를 바꾸고, <span class=\"text-cyan-300 font-semibold\">AI API</span> 시장의 거대한 신규 비즈니스 매출 모델을 증명하고 있습니다.",
      "key_companies": [
        "구글",
        "Zoom"
      ],
      "insight": "번역 서비스의 중심이 '독립형 앱'에서 '기존 커뮤니케이션 도구 내 <span class=\"text-cyan-300 font-semibold\">API 임베딩</span>'으로 이동하면서 AI 음성 솔루션이 단순 편의 도구에서 기업의 필수 인프라로 자리 잡고 있습니다.",
      "action_point": "화상회의 및 콜센터 등 B2B 솔루션 시장에서 독점적 언어 모델 인프라를 구축하는 구글의 생태계 확장과 이를 활용하는 국내 <span class=\"text-cyan-300 font-semibold\">AI 애플리케이션</span> 개발사의 서비스 다변화를 주시해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": [
        "stock"
      ],
      "tags": ["구글미트", "실시간번역", "음성통역API", "Zoom", "B2BAI"]
    }
  },
  "xiW627IU6wo": {
    "primary": "economy",
    "video": {
      "id": "xiW627IU6wo",
      "title": "토큰값 떨어지면 AI 인프라·반도체 사이클도 끝날까 | 빈난새의 빈틈없이월가",
      "published": "2026-06-13T01:00:18+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=xiW627IU6wo",
      "thumbnail": "https://img.youtube.com/vi/xiW627IU6wo/hqdefault.jpg"
    },
    "analysis": {
      "summary": "AI 모델 고도화 and 칩 효율 향상으로 <span class=\"text-amber-300 font-bold\">토큰 단가</span>가 하락하고 있으나, 이는 수요 둔화가 아닌 기술 보급 확대를 의미하는 <span class=\"text-amber-300 font-bold\">재본스의 역설</span>(Jevons' Paradox)로 해석해야 합니다. 빅테크들의 <span class=\"text-amber-300 font-bold\">설비투자(CAPEX)</span>는 사상 최대 수준을 경신하고 있으며, 이에 따른 <span class=\"text-rose-400 font-medium\">감가상각 부담</span>과 <span class=\"text-rose-400 font-medium\">투자수익률(ROI) 논쟁</span>이 시장 변동성을 키우는 요인이 되고 있습니다.",
      "key_claims": [
        "최근 AI 토큰 단가 하락은 수요 급감이 아니라 추론 비용의 97% 급감 및 저가 소형 모델 사용 다변화에 기인한 대중화 신호다.",
        "5대 빅테크(MS, 아마존, 메타, 구글, 오라클)의 매출 대비 <span class=\"text-amber-300 font-bold\">설비투자(CAPEX)</span> 비율은 2027년 44%까지 올라 <span class=\"text-rose-400 font-medium\">닷컴버블 고점</span>(32%)을 상회할 것으로 전망된다.",
        "골드만삭스는 수요가 견조하며 물리적 병목(전력, 메모리, 전력 인프라 등)이 핵심으로 내년 CAPEX 전망치를 시장 컨센서스보다 훨씬 높은 9,940억 달러로 상향 조정했다.",
        "AI 인프라 주식들의 밸류에이션 부담이 가중되는 가운데, 미래 이익 지속성 기대치가 <span class=\"text-cyan-300 font-semibold\">광 연결</span>(Optical Interconnect)은 높은 반면 사이클 산업인 <span class=\"text-cyan-300 font-semibold\">메모리 반도체</span>는 상대적으로 낮게 나타나고 있다."
      ],
      "data_points": [
        "GPT-4 출시 이후 현재까지 AI 추론 비용 감소율: 97%",
        "5대 하이퍼스케일러 매출 대비 CAPEX 전망: 2026년 36%, 2027년 44%",
        "닷컴 버블 당시 통신 장비 업종 매출 대비 CAPEX 역사적 고점: 32%",
        "오라클 2027년 매출 대비 CAPEX 비율 전망 (금융 리스 포함 시): 189%",
        "구글의 월 토큰 처리량: 3경 개 이상 (1년 만에 7배 증가)",
        "골드만삭스 공식 내년 빅테크 CAPEX 전망치: 9,940억 달러 (시장 컨센서스는 9,200억 달러)",
        "AI 인프라 주식 주가수익비율(PER) 중위값: 26배"
      ],
      "signal": "neutral",
      "signal_reason": "토큰 단가 하락이 수요 확대라는 긍정적 지표와 빅테크의 과도한 설비투자에 따른 <span class=\"text-rose-400 font-medium\">ROI 우려</span> 및 감가상각 마진 훼손 리스크가 공존하고 있기 때문입니다.",
      "key_companies": [
        "엔비디아",
        "오픈AI",
        "앤스로픽",
        "구글",
        "아마존",
        "마이크로소프트",
        "오라클",
        "시타델"
      ],
      "insight": "AI 시장이 단순 기대감 중심의 투자에서 실제 토큰 지출 단가와 사용성 최적화(토크노믹스)를 따지는 효율성 국면으로 진입하고 있으며, 하드웨어 효율 증가는 오히려 전체 토큰 소비량을 증가시키는 <span class=\"text-amber-300 font-bold\">재본스의 역설</span>을 촉발하고 있습니다.",
      "action_point": "단기적 기대감이 높은 인프라 주식들의 <span class=\"text-rose-400 font-medium\">밸류에이션 오버슈팅</span>에 유의하며, 실질적인 매출 성장과 이익을 입증하는 저평가 <span class=\"text-cyan-300 font-semibold\">메모리 반도체</span> 밸류체인 및 전력 인프라, 효율적 모델 제어(<span class=\"text-cyan-300 font-semibold\">라우팅 소프트웨어</span>, 광 연결) 핵심 기술을 탑재한 기업 위주로 접근해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": [
        "stock",
        "tech"
      ],
      "tags": ["토크노믹스", "재본스의역설", "설비투자", "CAPEX", "감가상각비", "하이퍼스케일러", "메모리반도체", "광연결"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["video"], info["analysis"], info["classification"])
