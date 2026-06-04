import json
from pathlib import Path

def save_analysis(video_id, primary_topic, video_data, analysis_data, classification_data):
    analyzed_dir = Path(f"data/analyzed/{primary_topic}")
    analyzed_dir.mkdir(parents=True, exist_ok=True)
    
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
    
    pending_file = Path(f"data/pending/{video_id}.json")
    if pending_file.exists():
        pending_file.unlink()
        print(f"Removed pending: {pending_file}")
        
    synthesis_cache = Path(f"data/synthesis/{primary_topic}.json")
    if synthesis_cache.exists():
        try:
            synthesis_cache.unlink()
            print(f"Invalidated cache: {synthesis_cache}")
        except Exception as e:
            print(f"Error invalidating cache: {e}")

analyses = {
  "eKDwutrzcy8": {
    "primary": "etc",
    "video": {
      "id": "eKDwutrzcy8",
      "title": "내 컴퓨터 속 비서?  |  2분완성 그림퀴즈 'AI 에이전트'편",
      "published": "2026-06-03T07:00:00+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=eKDwutrzcy8",
      "thumbnail": "https://img.youtube.com/vi/eKDwutrzcy8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미래에셋 스마트머니 채널의 AI 및 디지털 자산 개념 정리 퀴즈 영상입니다. AI 에이전트, 프롬프트, 할루시네이션, AGI, 딥페이크, 바이브 코딩, AI 오케스트레이션 등 주요 인공지능 용어들을 그림과 퀴즈 형식으로 알기 쉽게 전달합니다.",
      "key_claims": [
        "AI 에이전트는 단순 응답을 넘어 스스로 계획을 세우고 실행하는 AI 비서이다.",
        "바이브 코딩은 프로그래밍 언어 대신 일상어로 코딩하는 방식을 뜻한다.",
        "AI 오케스트레이션은 여러 AI 모델, 데이터, 인프라를 통합해 복잡한 시스템을 조율하는 기술이다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "일반 대중을 대상으로 한 기초적인 AI 용어 교육 콘텐츠로서, 구체적인 투자 신호나 시장 변동성 예측을 제공하지는 않습니다.",
      "key_companies": [
        "미래에셋증권"
      ],
      "insight": "AI 에이전트와 오케스트레이션 같은 개념의 확산은 일반 대중이 AI의 단순 사용을 넘어 시스템화된 AI 비서를 일상적으로 다루게 되는 시대로 나아가고 있음을 방증합니다.",
      "action_point": "일반 비전문가도 개발할 수 있는 바이브 코딩 및 AI 오케스트레이션 툴의 등장에 주목하여, 관련 솔루션을 공급하는 강소 소프트웨어 기업군을 탐색하는 것이 좋습니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["tech"],
      "tags": ["AI에이전트", "AI용어", "AGI", "바이브코딩", "오케스트레이션"]
    }
  },
  "h6Thp79vntE": {
    "primary": "tech",
    "video": {
      "id": "h6Thp79vntE",
      "title": "말 안 듣는 AI 에이전트를 길들이는 하네스?!",
      "published": "2026-06-03T08:00:00+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=h6Thp79vntE",
      "thumbnail": "https://img.youtube.com/vi/h6Thp79vntE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "스스로 행동을 개시하는 <span class=\"text-cyan-300 font-semibold\">AI 에이전트</span>들이 통제 범위를 벗어나 엉뚱한 행동을 하지 않도록 특정 규칙이나 제약조건으로 묶어 통제하는 하네스(Harness) 기법의 중요성을 설명합니다. 에이전트의 자율성과 디테일한 통제 요구에 따라 하네스 설계의 스펙트럼과 개발자의 '교육 철학'이 반영됩니다.",
      "key_claims": [
        "AI 에이전트에게 자율적 태스크를 맡길 때 지시 사항 외의 이상 행동을 차단하는 통제 장치(하네스)가 필수적이다.",
        "에이전트 통제용 하네스는 사용자의 디테일한 지시 수행 요구에 따라 넓거나 좁은 스펙트럼을 가진다.",
        "에이전트의 완성도와 규칙 준수 여부는 제작 및 교육 단계에서의 철학과 구조화(하네스) 수준에 비례한다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "AI 에이전트 제어 기술인 하네스 개념을 소개하는 기술적 교양 콘텐츠로, 시장이나 기업 주가에 직접적인 매수/매도 의견을 주지 않습니다.",
      "key_companies": [],
      "insight": "AI 에이전트가 실무에 본격 투입되면서 성능만큼이나 '신뢰성과 예측 가능성'이 소프트웨어 아키텍처의 핵심 화두로 떠오르고 있습니다. 안전한 자율 제어를 가능케 하는 에이전트 프레임워크와 안전장치 솔루션이 AI 생태계 내에서 주요 보안 및 인프라 제품군으로 성장할 것입니다.",
      "action_point": "AI 에이전트를 안전하게 통제할 수 있는 오케스트레이션 툴이나 가드레일(Guardrail), 하네스 설계를 지원하는 플랫폼 소프트웨어(예: LangChain, LlamaIndex 관련 오픈소스 및 엔터프라이즈 솔루션) 시장의 성장에 주목해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": [],
      "tags": ["AI에이전트", "하네스", "가드레일", "에이전트통제", "AI안전성"]
    }
  },
  "9eCLuiRc3cA": {
    "primary": "space",
    "video": {
      "id": "9eCLuiRc3cA",
      "title": "스페이스X 미친 기술 한번 쏜 로켓 30번 더 쓴다 (유진투자증권 정의훈 연구원)",
      "published": "2026-06-03T09:00:00+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=9eCLuiRc3cA",
      "thumbnail": "https://img.youtube.com/vi/9eCLuiRc3cA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "일론 머스크의 <span class=\"text-cyan-300 font-semibold\">스페이스X</span>가 1단 로켓을 버리지 않고 연료를 남겨 역추진으로 회수해 재사용하는 기술을 고도화하여 상업 우주 발사 시장을 독점하고 있습니다. 1개의 발사체를 최대 30회까지 재사용하며 발사 횟수를 주당 3회 이상(연간 165회)으로 끌어올려 비용 파괴를 실현했습니다.",
      "key_claims": [
        "스페이스X는 1단 추진체 연료를 재점화하여 역추진 착륙시키는 재사용 로켓 기술을 완전히 상용화했다.",
        "최대 30회 재사용 달성을 통해 발사 비용을 극적으로 낮춰 글로벌 상업 발사 시장 점유율 50% 이상을 독점하고 있다.",
        "한국 등 세계 주요국들도 상업 발사 비용 절감 및 높은 신뢰도를 지닌 스페이스X의 발사 서비스를 이용할 수밖에 없는 독점 구도이다."
      ],
      "data_points": [
        "스페이스X 단일 로켓 최대 재사용 횟수: 30회",
        "스페이스X 작년 연간 발사 횟수: 165회 (전 세계 324회 중 절반 이상)",
        "발사 빈도: 일주일에 평균 3회"
      ],
      "signal": "bullish",
      "signal_reason": "스페이스X의 독보적인 로켓 재사용 성공 횟수와 가격 경쟁력은 우주 인터넷(스타링크) 및 글로벌 우주 개발 단가를 급격히 낮추어 민간 우주 경제 활성화에 강력한 상방 신호를 보냅니다.",
      "key_companies": [
        "스페이스X"
      ],
      "insight": "스페이스X는 '발사 횟수 주 3회, 최대 30회 재사용'이라는 압도적인 하드웨어 재활용 능력을 통해 경쟁국들과 메울 수 없는 경제적 격차를 벌렸습니다. 이는 우주 산업의 지배적 사업자 지위를 굳히는 동시에 저궤도 위성 네트워크의 조기 완성을 가능케 하는 핵심 동력입니다.",
      "action_point": "스페이스X의 독점에 대응하거나 이에 부품을 공급하는 아시아 및 국내 우주 발사체 관련 부품·소재 기업, 그리고 저궤도 위성 통신 안테나 및 지상국 장비 제조사들의 실적 추이를 살펴볼 필요가 있습니다."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["stock", "tech"],
      "tags": ["스페이스X", "재사용로켓", "우주산업", "발사체", "스타링크"]
    }
  },
  "mJCB-wk82gg": {
    "primary": "tech",
    "video": {
      "id": "mJCB-wk82gg",
      "title": "삼성·하이닉스 턱밑 중국 HBM 무서운 추격 (성균관대 화학공학부 권석준 교수)",
      "published": "2026-06-03T03:00:00+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=mJCB-wk82gg",
      "thumbnail": "https://img.youtube.com/vi/mJCB-wk82gg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "중국 반도체 업계가 삼성전자와 SK하이닉스의 독무대였던 <span class=\"text-cyan-300 font-semibold\">HBM</span> 시장을 후공정(패키징, 적층 기술 및 열 방출) 역량 강화와 풍부한 내수 시장을 바탕으로 무섭게 추격하며 기술 격차를 1.5년 수준으로 좁히고 있습니다. 중국의 독자적인 대안 모델(예: 딥시크 등 소프트웨어 혁신과 하드웨어 추격의 결합)은 미중 갈등 장벽 속에서도 자급화 카드로 작용하고 있습니다.",
      "key_claims": [
        "HBM 분야에서 한중 간의 기술 격차는 고정이 아니며 패키징(후공정) 기술 추격을 통해 1.5년 내외로 단축되고 있다.",
        "중국은 미중 갈등 장벽에 대응하여 HBM 자체 공급망을 구축하고 있으며, 소프트웨어(예: 딥시크) 최적화와 결합해 성능 한계를 보완하고 있다.",
        "후공정 적층 공정 및 열 관리 솔루션에서 중국의 연구개발 속도가 매우 빨라 한국 메모리 제조사들에게 잠재적 위협이 되고 있다."
      ],
      "data_points": [
        "한중 HBM 기술 격차: 기존 3세대(약 3년)에서 약 1.5년 수준으로 단축"
      ],
      "signal": "bearish",
      "signal_reason": "중국의 HBM 추격 속도가 당초 예상보다 빠르며, 후공정 기술 경쟁력을 바탕으로 중저가 라인업을 자급화할 경우 한국 메모리 제조사들의 중장기 마진과 점유율에 부담 요인으로 작용할 수 있습니다.",
      "key_companies": [
        "삼성전자",
        "SK하이닉스",
        "딥시크"
      ],
      "insight": "미국의 대중국 반도체 장비 규제는 역설적으로 중국이 후공정(Advanced Packaging) 기술 개발에 사활을 걸게 만들었습니다. 중국은 소프트웨어적 경량화(딥시크)와 패키징 혁신을 융합하여 서방의 하드웨어 독점을 우회하는 거대한 대체 생태계를 성공적으로 구축해 나가고 있습니다.",
      "action_point": "중국의 반도체 자급화 추진 강도를 고려할 때, 국내 후공정 장비(OSAT) 및 미세 열 제어 소재 밸류체인의 기술 장벽 유지 여부를 점검하고, 선단 패키징(HBM4 이후 코옵티컬 패키징 등) 초격차 기술을 보유한 국내 한정적 장비사에 집중해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["economy"],
      "tags": ["HBM", "중국반도체", "후공정", "미중갈등", "반도체자급화", "패키징"]
    }
  },
  "Z164yVMpyjE": {
    "primary": "tech",
    "video": {
      "id": "Z164yVMpyjE",
      "title": "PCB 기판 재료가 안좋으면 AI 신호가 손실된다?",
      "published": "2026-06-03T05:00:00+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=Z164yVMpyjE",
      "thumbnail": "https://img.youtube.com/vi/Z164yVMpyjE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "인공지능(AI) 고속 신호 처리 시대에 진입하면서 PCB 기판의 원자재인 동박과 CCL의 물성이 시스템 성능의 핵심 변수로 부상하고 있습니다. 신호가 고주파가 될수록 구리 배선 표면에 쏠리는 표피 효과(스킨 이펙트)와 유전 손실로 인한 신호 왜곡 및 발열이 극대화되므로 HVLP(극저조도) 동박과 저유전율 CCL 소재의 협상력이 급증하고 있습니다.",
      "key_claims": [
        "고주파 고속 신호 전송 시 전류가 구리 표면으로만 흐르는 표피 효과 때문에, 구리 표면의 거칠기(HVLP 동박)가 신호 전송 효율을 좌우한다.",
        "PCB의 핵심 원자재인 CCL(동박적층판)의 유전 손실과 열팽창율 관리가 기판의 뒤틀림 및 신호 감쇄를 막는 핵심 변수다.",
        "엔비디아의 루빈(Rubin) 등 차세대 AI 가속기 설계 변경에 따라 유리섬유, 동박 등 상류 원소재 기업의 기술적 가치와 단가 협상력이 더욱 강화되고 있다."
      ],
      "data_points": [],
      "signal": "bullish",
      "signal_reason": "차세대 가속기 설계가 고도화될수록 기판 내 미세 신호 손실을 제어하는 고부가가치 원소재(HVLP 동박, 고다층 저유전율 CCL) 수요가 폭증하여 관련 고부가가치 소재 기업들의 영업이익률 성장에 매우 긍정적입니다.",
      "key_companies": [
        "엔비디아",
        "두산전자",
        "삼성전기"
      ],
      "insight": "AI 가속기 성능 극대화 경쟁이 GPU 칩셋을 넘어 PCB 기판과 물리적 기초 원소재 단까지 확장되고 있습니다. 신호 손실을 막기 위해 기판 소재의 물성을 한계까지 쥐어짜야 하는 상황이며, 이는 범용 부품으로 치부되던 CCL과 유리섬유를 대체 불가능한 고부가가치 스페셜티 제품군으로 탈바꿈시켰습니다.",
      "action_point": "고다층 PCB 기판(MLB) 및 저유전(Low-loss) CCL, 극저조도(HVLP) 동박 제조 원천 기술을 보유하고 엔비디아 또는 대형 기판 공급망에 최종 진입한 핵심 소재사들에 선제적으로 투자해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["PCB", "CCL", "동박", "HVLP", "표피효과", "AI소재", "루빈"]
    }
  },
  "UccedxjEoBY": {
    "primary": "economy",
    "video": {
      "id": "UccedxjEoBY",
      "title": "미국 물가 또 폭등? \"금리 인하 아예 시작도 못 한다\" #교양이를 부탁해",
      "published": "2026-06-03T12:00:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=UccedxjEoBY",
      "thumbnail": "https://img.youtube.com/vi/UccedxjEoBY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "이란 전쟁 등 지정학적 리스크로 인한 고유가 상황이 최소 9월에서 12월까지 지속되면서 물가 압박을 가중시킬 것입니다. 유가 및 원자재 발 인플레이션은 소득 무관하게 모든 경제 주체에게 부과되는 세금(인플레이션 텍스)과 같아 미국 중앙은행(연준)은 금리 인하에 매우 보수적인 태도를 취할 수밖에 없습니다.",
      "key_claims": [
        "이란 갈등으로 석유 공급망이 훼손되면, 휴전이 성립되더라도 정상화에 3~4개월이 소요되어 고유가가 장기화(9~12월)된다.",
        "인플레이션은 모든 국민에게 고통을 주는 '인플레이션 세금'으로 작용하여 선거 전 치명적인 정치적 압박 요인이다.",
        "연준 총재들은 역사적 인플레이션 제어 실패 경험을 경계하기 때문에, 물가가 잡히기 전까지는 성급한 금리 인하를 단행하지 못할 것이다."
      ],
      "data_points": [
        "유가 정상화 소요 기간: 공급 중단 해제 후 약 3~4개월",
        "고유가 장기화 전망 시점: 올해 9월에서 최대 12월"
      ],
      "signal": "bearish",
      "signal_reason": "유가 상승에 따른 인플레이션 고착화와 연준의 금리 인하 지연은 고금리 장기화 부담을 지속시켜 글로벌 증시 및 부채 비중이 높은 자산 시장에 하방 압력을 가합니다.",
      "key_companies": [],
      "insight": "유가 공급 쇼크는 시차를 두고 전방위 물가로 전이되므로 단기 전쟁 종료 여부와 상관없이 고유가 여파가 9월 미국 대선 국면까지 이어질 것임을 명시합니다. 연준으로서는 물가 안정 신뢰성 훼손을 방어하기 위해 '고금리 장기유지(Higher for longer)' 기조를 강화할 수밖에 없는 코너에 몰려 있습니다.",
      "action_point": "금리 인하 시점 지연과 스태그플레이션 리스크에 대비하여 부채 비율이 높은 고레버리지 기업 투자를 지양하고, 원자재 가격 상승 수혜를 입는 정유·에너지 기업 및 현금 창출 능력이 우수한 배당 가치주 비중을 늘려야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["인플레이션", "연준금리인하", "고유가", "지정학적리스크", "고금리장기화", "인플레이션텍스"]
    }
  },
  "TaIAKaQ8etY": {
    "primary": "tech",
    "video": {
      "id": "TaIAKaQ8etY",
      "title": "초당 1.1조 개 데이터 처리, 엔비디아 Vera CPU",
      "published": "2026-06-03T13:00:00+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=TaIAKaQ8etY",
      "thumbnail": "https://img.youtube.com/vi/TaIAKaQ8etY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아가 초당 1.1조(1.1 Trillion) 개의 실시간 데이터를 극도의 초저지연으로 처리할 수 있는 차세대 <span class=\"text-cyan-300 font-semibold\">Vera CPU</span>를 공개했습니다. 뉴욕 증권 거래소(NYSE)와 고빈도 매매(HFT) 등 금융권 실증 자료를 통해 입증된 성능으로, AI 에이전트의 복잡한 조율(오케스트레이션) 데이터 파이프라인을 고속으로 GPU에 피딩하는 능력을 보여줍니다.",
      "key_claims": [
        "Vera CPU는 뉴욕증권거래소의 초저지연 데이터 실시간 처리에 최적화되어 기존 대비 6배 빠른 실시간 스트리밍 처리가 가능하다.",
        "고빈도 트레이딩(HFT) 등 극도로 까다로운 금융 인프라에서 입증된 파이프라이닝 성능을 지닌다.",
        "Vera CPU는 데이터 흐름 병목을 제거하여 GPU에 빠르게 데이터를 먹여주는 AI 에이전트 조율의 핵심 퍼즐이다."
      ],
      "data_points": [
        "Vera CPU 초당 메시지 처리 성능: 1.1조 개(1.1 Trillion)",
        "실시간 데이터 스트리밍 처리 속도 향상: 기존 대비 6배"
      ],
      "signal": "bullish",
      "signal_reason": "엔비디아가 데이터 병목이 되는 CPU 영역까지 독보적인 초고속·초저지연 칩셋 Vera를 선보이면서 금융·AI 인프라 플랫폼 전체를 패키지로 묶어 장악하는 완전한 AI 독주 체제를 구축하고 있습니다.",
      "key_companies": [
        "엔비디아",
        "NYSE",
        "HP"
      ],
      "insight": "Vera CPU의 출시는 엔비디아가 GPU 공급사를 넘어 데이터센터 백본 자체를 표준화하고 있음을 증명합니다. 초저지연 실시간 처리가 요구되는 NYSE 등의 사례는 향후 밀리초 단위로 수억 개의 에이전트가 통신해야 할 실시간 자율 에이전트 시대를 대비한 사전 포석입니다.",
      "action_point": "엔비디아의 풀스택 AI 패키지(GPU + 네트워크 + CPU) 지배력이 더 강해짐에 따라 AI 데이터 파이프라인 소프트웨어 솔루션 및 고빈도 트레이딩을 지원하는 고성능 컴퓨팅 인프라 기업에 투자 기회를 넓혀야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["엔비디아", "VeraCPU", "초저지연", "금융인프라", "데이터파이프라인", "AI에이전트"]
    }
  },
  "UthxUVc4Hpc": {
    "primary": "tech",
    "video": {
      "id": "UthxUVc4Hpc",
      "title": "엔비디아 Vera CPU 출시가 갖는 의미?",
      "published": "2026-06-03T14:00:00+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=UthxUVc4Hpc",
      "thumbnail": "https://img.youtube.com/vi/UthxUVc4Hpc/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아의 <span class=\"text-cyan-300 font-semibold\">Vera CPU</span>는 단순히 개별 CPU 성능 경쟁을 넘어 AI 데이터센터 전체를 하나의 패키지 플랫폼으로 묶어 팔기 위한 마지막 핵심 퍼즐입니다. 고객들은 CPU나 GPU 부품 단위의 비교보다 전력 효율과 랙(Rack) 스케일 전체의 안정성을 중요시하며, 엔비디아는 이 'AI 공장' 전체의 표준화를 도모하고 있습니다.",
      "key_claims": [
        "Vera CPU 출시로 엔비디아는 GPU, 네트워크(DPU), 랙 스케일에 이어 CPU까지 아우르는 풀 패키지 AI 플랫폼 라인업을 완성했다.",
        "AI 데이터센터 경쟁의 초점은 단일 부품의 10% 속도 격차가 아니라 전력, 냉각, 상면 비용을 아우르는 랙 스케일 전체의 전력 효율과 안정성이다.",
        "인텔(Xeon)과 AMD(EPYC)가 서버 CPU 시장에서 강세를 보이고 있으나, 엔비디아의 통합 패키지 공세로 인해 경쟁 구도가 시스템 플랫폼 싸움으로 재편된다."
      ],
      "data_points": [],
      "signal": "bullish",
      "signal_reason": "엔비디아가 Vera CPU를 통해 AI 공장 전체를 패키지로 납품하는 수직 계열화를 공고히 함으로써, 기존 CPU 강자인 인텔·AMD의 점유율을 침투하고 데이터센터 내 지배력을 한층 높일 것입니다.",
      "key_companies": [
        "엔비디아",
        "인텔",
        "AMD"
      ],
      "insight": "서버 시장의 주도권이 범용 서버에서 전력·공간 극단적으로 제한적인 AI 공장(AI Factory)으로 넘어가고 있습니다. 엔비디아의 Vera CPU는 전력 소모당 추론 효율성을 랙 스케일 단에서 최적화하여 인텔과 AMD가 지배하던 전통 서버 시장의 잔여 영토마저 빠르게 잠식해 나갈 것입니다.",
      "action_point": "엔비디아 랙 스케일 패키지 공급 증가에 따라 랙 단위 수냉식 냉각 솔루션, 전력 변환 모듈 및 고밀도 전력 공급 장치(AI 전력인프라) 관련 핵심 수혜주들의 지분 확보가 필요합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["energy"],
      "tags": ["엔비디아", "VeraCPU", "AI데이터센터", "랙스케일", "수직계열화", "서버CPU"]
    }
  },
  "xBN1f5G791I": {
    "primary": "stock",
    "video": {
      "id": "xBN1f5G791I",
      "title": "소프트뱅크, 22년 부동의 日 시총 1위 도요타를 꺾다 #shorts",
      "published": "2026-06-03T15:00:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=xBN1f5G791I",
      "thumbnail": "https://img.youtube.com/vi/xBN1f5G791I/hqdefault.jpg"
    },
    "analysis": {
      "summary": "인공지능(AI) 투자 명가인 <span class=\"text-cyan-300 font-semibold\">소프트뱅크 그룹</span>이 철저한 AI 집중 전략에 힘입어 20여 년간 일본 시총 1위를 굳건히 지켜온 도요타 자동차를 제치고 왕좌에 등극했습니다. 주가 급등의 핵심 동력은 자회사 <span class=\"text-cyan-300 font-semibold\">ARM</span>의 AI 서버 수요 급증, 오픈AI 투자에 따른 막대한 평가이익, 프랑스 등 글로벌 거점 중심의 대규모 AI 데이터센터 인프라 구축 주도입니다.",
      "key_claims": [
        "소프트뱅크가 도요타를 꺾고 일본 시총 1위에 오른 것은 전통 제조업에서 AI·반도체 기술 주도로 자본 시장의 무게 중심이 이동했음을 시사한다.",
        "소프트뱅크의 주가 급상승(올해 85% 이상)은 자회사 ARM의 폭발적 성장과 오픈AI 대규모 평가이익이 견인했다.",
        "시장 자본은 완만한 안정을 추구하는 기업보다 과감하게 미래 기술 리스크를 지는 리더십에 높은 밸류에이션(프리미엄)을 부여하고 있다."
      ],
      "data_points": [
        "소프트뱅크 주가 상승률 (올해): 85% 이상",
        "소프트뱅크 시가 총액: 48조 8천억엔 (약 462조원) 돌파",
        "도요타 시총 1위 수성 기간: 약 22년"
      ],
      "signal": "bullish",
      "signal_reason": "소프트뱅크의 시총 1위 등극과 반도체 장비주(도쿄 일렉트론, 키옥시아)의 동반 폭등은 일본 증시 전체의 주도주 체질이 자동차에서 AI·반도체로 완벽히 리레이팅되고 있음을 가리키는 긍정적 지표입니다.",
      "key_companies": [
        "소프트뱅크",
        "도요타",
        "ARM",
        "오픈AI",
        "도쿄일렉트론",
        "키옥시아"
      ],
      "insight": "글로벌 자본의 흐름은 이제 명확히 '현실의 캐시카우(제조업)'에서 '미래의 레버리지(AI인프라)'로 이동했습니다. 손정의 회장의 적극적인 AI 인프라(ARM 설계 + 글로벌 데이터센터 구축) 투자가 꽃을 피우며 소프트뱅크가 글로벌 AI 대장 투자사로 재정의되었습니다.",
      "action_point": "일본 증시 내의 AI/반도체 포트폴리오를 강화하고, 소프트뱅크의 데이터센터 파이프라인 및 ARM 아키텍처 수혜가 확실시되는 전 세계 에지(Edge) 디바이스 반도체 IP 기업들에 주목해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["소프트뱅크", "도요타", "시가총액1위", "ARM", "오픈AI", "일본증시", "AI투자"]
    }
  },
  "x6bmkNr0eDg": {
    "primary": "tech",
    "video": {
      "id": "x6bmkNr0eDg",
      "title": "진짜야? AI야?  AI영상 검증 기술도 중요하다! 구글의 검증기술!",
      "published": "2026-06-03T16:00:00+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=x6bmkNr0eDg",
      "thumbnail": "https://img.youtube.com/vi/x6bmkNr0eDg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "생성형 AI 영상 모델(구글 비오 등)의 고도화로 콘텐츠 생성 단계를 넘어 반복 수정 워크플로우와 생성 영상의 진위 여부를 판별하는 검증 기술(워터마크 SynthID, C2PA 표준)의 중요성이 급격히 부각되고 있습니다. 구글이 창작 모델과 검증 기술을 동시 발표한 것은 AI 영상 시장의 경쟁이 단순 퀄리티 싸움을 넘어 신뢰 표준화 선점 경쟁으로 이전하고 있음을 나타냅니다.",
      "key_claims": [
        "생성 AI 창작의 핵심 변목이 단순 생성이 아닌 앵글 유지, 배경 수정 등의 반복 편집 워크플로우로 이동했다.",
        "AI 영상 생성 일상화에 따른 가짜 정보 유통을 막기 위해 눈에 안 보이는 워터마크(SynthID) 및 콘텐츠 이력 표준(C2PA)의 탑재가 의무화되고 있다.",
        "AI 미디어 시장의 주도권은 고성능 창작 모델과 신뢰성 검증 인프라(워터마크 및 추적 레이어)를 함께 제공하는 빅테크가 쥐게 될 것이다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "생성 AI 영상의 신뢰도 확보를 위한 필수 검증 표준 기술 도입 추세를 설명하는 분석으로, 특정 기업 주가의 즉각적인 등락 신호는 아닙니다.",
      "key_companies": [
        "구글",
        "C2PA"
      ],
      "insight": "AI 고속도로가 건설되자마자 과속 카메라(검증 시스템)에 대한 수요가 빗발치고 있습니다. 앞으로 AI 콘텐츠가 유통되는 모든 브라우저, SNS 플랫폼에서 C2PA 워터마크 검증이 필수 레이어로 안착함에 따라 신뢰 필터링 및 보안 기술 생태계가 새로 구성될 것입니다.",
      "action_point": "AI 영상 생성 기술 기업뿐만 아니라, 워터마크 추적, 딥페이크 탐지 솔루션 및 보안 감사 플랫폼 기술을 보유한 사이버 보안 전문 기업들에 대한 중장기적 투자 기회를 탐색하는 것이 유용합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["etc"],
      "tags": ["AI영상검증", "구글", "SynthID", "C2PA", "워터마크", "딥페이크보안", "생성형AI"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["video"], info["analysis"], info["classification"])
