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
  "hZtJtpHzRGw": {
    "primary": "robot",
    "video": {
      "id": "hZtJtpHzRGw",
      "title": "아틀라스가 안 나온 진짜 이유 현대차 엔비디아 대만 GTC",
      "published": "2026-06-03T05:30:00+00:00",
      "channel_name": "엔지니어TV",
      "url": "https://www.youtube.com/watch?v=hZtJtpHzRGw",
      "thumbnail": "https://img.youtube.com/vi/hZtJtpHzRGw/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아의 로봇 OS/플랫폼 표준화 야망(그루트, 코스모스 3 등) 속에서 현대차가 인수한 보스턴 다이나믹스의 <span class=\"text-cyan-300 font-semibold\">아틀라스</span>(Atlas)가 엔비디아 메인 키노트에 직접 나서지 않은 이유를 조명합니다. 보스턴 다이나믹스는 단순 하드웨어 제조사를 넘어 자체 AI 연구소와 구글 기술을 융합하여 독자적인 '로봇 두뇌' 생태계를 유지하려는 독립적 전략적 포지션을 취하고 있습니다.",
      "key_claims": [
        "엔비디아의 궁극적인 목표는 모든 로봇 위에 얹어질 소프트웨어 OS와 AI 두뇌(코스모스, 그루트)의 표준화 장악이다.",
        "보스턴 다이나믹스는 엔비디아의 부품/자율주행 고객이지만, 휴머노이드 분야에서는 자체 피지컬 AI 연구 역량(rai 조직, 로봇 훈련소)을 보유해 전면 의존을 거부한다.",
        "엔비디아가 피규어, 유니트리 등을 표준 파트너로 세운 반면, 현대차는 아틀라스만의 독립적인 AI 월드 모델 구축을 추구하며 협력과 긴장 관계를 병행하고 있다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "엔비디아의 로봇 플랫폼 장악 전략과 보스턴 다이나믹스의 독자 노선 간의 역학 구도를 분석한 내용으로, 즉각적인 주가 상승이나 하락 신호보다는 업계 표준 선점 경쟁을 시사합니다.",
      "key_companies": [
        "엔비디아",
        "현대자동차",
        "보스턴다이나믹스",
        "유니트리"
      ],
      "insight": "엔비디아는 PC 시대의 윈도우(OS)처럼 로봇 시장 전체의 소프트웨어 표준을 독점하려 합니다. 하지만 대량의 실전 생산 인프라와 자체 로봇 AI 연구소(AI Institute)를 보유한 현대차-보스턴 다이나믹스는 엔비디아의 독점 생태계에 종속되지 않고 독자적인 월드 모델을 수립하려 하며, 이는 향후 로봇 표준화 주도권을 둘러싼 미묘한 전선 형성을 의미합니다.",
      "action_point": "엔비디아 로봇 연합에 참여해 즉각적인 양산 기회를 얻는 유니트리 등 중국 로봇 공급망의 수혜 가능성을 평가하고, 보스턴 다이나믹스 독자 생태계(현대차 그룹) 내의 감속기 및 전용 핵심 모터 수혜주들을 선별해야 합니다."
    },
    "classification": {
      "primary_topic": "robot",
      "secondary_topics": ["tech", "stock"],
      "tags": ["아틀라스", "보스턴다이나믹스", "엔비디아", "그루트", "로봇플랫폼", "피지컬AI", "현대자동차"]
    }
  },
  "olseOKUNniQ": {
    "primary": "tech",
    "video": {
      "id": "olseOKUNniQ",
      "title": "AI가 AI를 만든다. 이제 중요한 것은?｜유토피아ㅣ2026.6.3(수)",
      "published": "2026-06-03T10:00:00+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=olseOKUNniQ",
      "thumbnail": "https://img.youtube.com/vi/olseOKUNniQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "안드레 카파시의 앤스로픽(Anthropic) 합류를 기점으로 AI 연구 자동화(AI가 스스로 AI를 개선하는 재귀적 자기 개선)가 AI 패러다임의 핵심 화두로 부상했습니다. 이로 인해 AI 개발의 병목이 인간 연구원의 시간에서 컴퓨트, 데이터, 전력 등 <span class=\"text-cyan-300 font-semibold\">AI 인프라</span> 단으로 급격히 이전하고 있으며, 기업 업무 지식과 실질적 데이터 검증 권한을 틀어쥔 '딥 사스(Deep SaaS)'의 가치가 부각되고 있습니다.",
      "key_claims": [
        "AI가 다음 세대 AI를 개선하기 위해 코드를 읽고 실험을 자동 설계·수행하는 'AI 연구 자동화' 경쟁이 가속화되고 있다.",
        "실험 자동화는 개발 비용을 줄이는 것이 아니라 실험 횟수의 폭증을 가져와 GPU, HBM, 전력 등 물리적 인프라 수요를 추가 유발한다.",
        "UI 중심의 얕은 사스(Thin SaaS)는 AI로 도태되나, 팔란티어(온톨로지)나 시놉시스처럼 기업 핵심 데이터와 검증 시스템을 쥔 '딥 사스(Deep SaaS)'의 moats는 강화된다."
      ],
      "data_points": [
        "안드로 카파시 앤스로픽 합류 공식화",
        "클로드 코드(Claude Code) 어시스턴트 도입"
      ],
      "signal": "bullish",
      "signal_reason": "AI의 자기 개선 경쟁 심화는 일회성 소프트웨어 붐을 넘어 반도체, 전력, 데이터센터 인프라 지출 장기화로 이어지며, 독점적 업무 프로세스 지적재산권을 가진 딥 사스 기업들에게 큰 기회가 됩니다.",
      "key_companies": [
        "앤스로픽",
        "오픈AI",
        "팔란티어",
        "시놉시스",
        "엔비디아"
      ],
      "insight": "AI는 가벼운 소프트웨어처럼 보이지만 본질적으로는 전력과 하드웨어를 집어삼키는 제조업적 특성을 띱니다. 카파시의 행보는 기술적 한계 돌파구가 '인간 연구원의 머리'가 아니라 '자동화된 AI 인프라 실험 엔진'으로 전환되고 있음을 보여주며, 이는 데이터센터와 고부가가치 데이터 및 규칙을 통제하는 기업들의 협상력을 높여줄 것입니다.",
      "action_point": "단순 챗봇 서비스사 투자를 지양하고, 대규모 실험 폭증으로 전력 및 HBM 수요 수혜를 입는 인프라 대형주와 강력한 기업 데이터 록인을 지닌 팔란티어(PLTR) 등 딥 사스 강자에 장기 대응해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock", "energy"],
      "tags": ["안드레카파시", "앤스로픽", "재귀적자기개선", "딥사스", "팔란티어", "AI인프라", "클로드"]
    }
  },
  "TFTAXglmr2Y": {
    "primary": "tech",
    "video": {
      "id": "TFTAXglmr2Y",
      "title": "\"2배 이상 올린다\" 최태원 폭탄 선언, 세계 AI 판도 바꾼 하이닉스 🇹🇼Computex",
      "published": "2026-06-03T11:00:00+00:00",
      "channel_name": "Softdragon SOD",
      "url": "https://www.youtube.com/watch?v=TFTAXglmr2Y",
      "thumbnail": "https://img.youtube.com/vi/TFTAXglmr2Y/hqdefault.jpg"
    },
    "analysis": {
      "summary": "대만 컴퓨텍스 현장에서 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>가 엔비디아 젠슨 황의 전폭적인 지지(\"Please make more HBM\")와 친필 서명을 받으며 AI 팩토리의 독보적 파트너임을 재입증했습니다. AI 생산성(에이전트 구동)을 결정짓는 핵심 병목인 열 제어(Advanced MR-MUF) 기술 경쟁력을 통해, 하이닉스는 단순 부품 공급사를 넘어 AI 성능을 좌우하는 인프라 설계자로 입지를 굳혔습니다.",
      "key_claims": [
        "엔비디아 젠슨 황 CEO는 메모리 병목 심화를 해결하기 위해 하이닉스 부스에 가장 오랜 시간 머무르며 HBM 대량 증산을 거듭 요청했다.",
        "HBM 고단 적층 시 발생하는 발열과 TSV 신호 왜곡을 완벽히 해결한 하이닉스의 열 제어 패키징 기술이 엔비디아 독점 공급망의 최대 무기이다.",
        "HBM4(2048-bit) 도입에 따라 대역폭이 2.9TB/s로 기하급수적으로 폭증하며, SK하이닉스는 하이퍼스케일러들의 전력·성능 한계를 뚫어주는 인프라사로 격상되었다."
      ],
      "data_points": [
        "현행 HBM 속도: 1.2TB/s → HBM4 목표 속도: 2.9TB/s에서 최대 4.0TB/s",
        "HBM4 I/O 수: 1024-bit에서 2048-bit로 확장",
        "HBM 밀도 및 대역폭 증가폭: 33% ~ 38%"
      ],
      "signal": "bullish",
      "signal_reason": "메모리가 AI 데이터센터 전체 성능과 전력 마진의 병목(Bottleneck)이 됨에 따라 독점적 1위인 SK하이닉스의 가격 결정력과 영업이익 마진 40%대 안착 가능성은 매우 높습니다.",
      "key_companies": [
        "SK하이닉스",
        "엔비디아",
        "TSMC"
      ],
      "insight": "과거 데이터센터 시대의 D램은 단순 부품이었으나, AI 팩토리 시대의 HBM은 GPU 패키징(CoWoS)에 밀착되어 시스템 구동 한계를 규정하는 인프라입니다. 최태원 회장의 증산 기조 선언과 젠슨 황의 구애는 하이닉스가 독점적 HBM 패키징 기술력을 레버리지하여 메모리 업계의 주도권을 완전히 장악했음을 방증합니다.",
      "action_point": "SK하이닉스의 HBM4 선제 개발 수혜를 염두에 두고 관련 장비 공급망(MR-MUF 리플로우 장비, TSV 세정 및 검사 장비사)의 지분을 지속 확보해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["SK하이닉스", "HBM4", "엔비디아", "발열제어", "MR-MUF", "컴퓨텍스", "AI인프라"]
    }
  },
  "D47e_f8lM8A": {
    "primary": "stock",
    "video": {
      "id": "D47e_f8lM8A",
      "title": "[LIVE] 어플라이드 에어로스페이스, '우주 IPO 러시' 신호탄? | 이나연 특파원",
      "published": "2026-06-03T11:30:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=D47e_f8lM8A",
      "thumbnail": "https://img.youtube.com/vi/D47e_f8lM8A/hqdefault.jpg"
    },
    "analysis": {
      "summary": "우주 국방 항공 관련 기업들의 연쇄 IPO가 지속되는 가운데, 사모펀드 엑시트 성격의 어플라이드 에어로스페이스가 상장 첫날 공모가 상단 부근 시초가 대비 -4.95% 하락 마감했습니다. 이는 기관의 높은 수요에도 불구하고 일반 시장의 차익 실현 경향이 뚜렷함을 보여주며, 다가오는 6월 12일 <span class=\"text-cyan-300 font-semibold\">스페이스X</span>의 초대형 나스닥 상장을 앞두고 신중한 접근이 필요함을 시사합니다. 한편 워런 버핏의 후계자 그랙 아벨은 전통적 스타일과 달리 테일러 모리슨 인수를 통한 옛 시거버트(싼 기업 줍기) 회귀 및 구글에 $100억 규모 AI 자금 추가 배팅(FOMO 회피)을 감행해 주목받고 있습니다.",
      "key_claims": [
        "어플라이드 에어로스페이스, 호크아이 360 등 사모펀드 자금이 회수 단계에 들어서며 우주 국방 섹터의 IPO 러시가 이어지고 있다.",
        "어플라이드 에어로스페이스의 첫날 종가 하락(-4.95%)은 적자 지속 및 대주주 락업 해제 시의 물량 부담 우려가 작용한 결과다.",
        "버크셔의 그랙 아벨은 버핏의 불간섭 원칙과 달리 피인수 주택 회사들의 사업 통합 시너지와 미검증 AI 기술 참여(구글 $100억 투자)에 전향적 자세를 보였다."
      ],
      "data_points": [
        "어플라이드 에어로스페이스 공모가: 20달러 (가이던스 $18~$21의 상단 부근)",
        "어플라이드 에어로스페이스 첫날 종가 등락률: -4.95% (시초가는 +3.75% 상승 출발)",
        "스페이스X 기업 가치 평가액: 1조 7,500억 달러 (어플라이드의 약 500배)",
        "스페이스X 나스닥 상장 예정일: 2026년 6월 12일 (로드쇼 6월 4일 시작)",
        "그랙 아벨의 테일러 모리슨 인수 금액: 68억 달러 (현금 인수)",
        "버크셔의 구글(알파벳) 추가 투자액: 100억 달러 (기존 $170억 지분에 추가)"
      ],
      "signal": "neutral",
      "signal_reason": "우주/국방 섹터의 IPO 활성화는 장기적으로 산업 개화에 긍정적이나 첫날 단기 급락은 신규 상장주에 대한 경계감을 높입니다. 버크셔의 행보는 테크 및 자산 배분 변화 흐름을 뒷받침합니다.",
      "key_companies": [
        "스페이스X",
        "어플라이드에어로스페이스",
        "구글",
        "버크셔해서웨이",
        "테일러모리슨"
      ],
      "insight": "사모펀드 Greenbriar의 어플라이드 에어로스페이스 상장 구도는 전형적인 고평가 엑시트 시도에 가깝습니다. 하지만 스페이스X는 시총 규모(1조 7500억 달러)가 비교 불가능하게 크고 글로벌 우주 패권을 쥔 독보적 독점주이므로, 초기 단기 변동성을 지나면 강력한 자금 유입이 기대됩니다. 버크셔 아벨의 알파벳 투자는 4,000억 달러의 현금 잉여를 배분하기 위해 'AI 불참 리스크(FOMO)'를 방어하려는 2세대 리더십의 실용적 변화를 나타냅니다.",
      "action_point": "6월 12일로 예정된 스페이스X 상장 전후로 국내 저궤도 위성 안테나 및 항공우주 부품사들의 주가 동조화 가능성을 주시하고, 단기 신규상장 우주주의 낙폭 과대 시 분할 매수를 검토할 수 있습니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["space", "tech"],
      "tags": ["스페이스X상장", "우주산업IPO", "어플라이드에어로스페이스", "그랙아벨", "버크셔해서웨이", "구글추가투자"]
    }
  },
  "wieaUTwTpiY": {
    "primary": "stock",
    "video": {
      "id": "wieaUTwTpiY",
      "title": "부족해도 너무 부족한 AI발 전력난, 조선업에 해결의 실마리가 있습니다ㅣ엄경아 신영증권 연구위원 [1부]",
      "published": "2026-06-03T09:00:00+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=wieaUTwTpiY",
      "thumbnail": "https://img.youtube.com/vi/wieaUTwTpiY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "국제해사기구(IMO)의 환경 규제 강화와 전 세계 에너지 패러다임 변화에 따라, 한국 조선업계가 단순 화석연료 선박 제조에서 수소 연료전지, 암모니아 추진선, SMR(소형 모듈 원자로) 탑재 선박 등 차세대 친환경 선박 기술을 중심으로 구조적 롱사이클 초입에 진입했습니다. 특히 신영증권 엄경아 위원은 지주사 격인 HD한국조선해양을 수소 연료전지 및 무탄소 에너지 전환 자회사 가치를 온전히 누릴 수 있는 장기 최선호주로 꼽았습니다.",
      "key_claims": [
        "한국 조선업은 다년간의 침체기를 지나 선가 상승과 친환경 교체 수요가 맞물린 장기 수주 사이클의 이제 막 출발선에 서 있다.",
        "IMO의 넷제로 규제 대응을 위해 선박 추진 에너지원이 LNG를 거쳐 무탄소(수소, 암모니아, SMR 원자력)로 급격히 전환되고 있다.",
        "HD한국조선해양은 100% 지분을 보유한 비상장 차세대 수소 연료전지 자회사를 통해 미래 친환경 선박 시장의 핵심 특허와 기술력을 내재화하고 있다."
      ],
      "data_points": [
        "조선업 최선호주 선정: HD한국조선해양",
        "글로벌 친환경 선박 배출 제로 규제 기관: IMO (국제해사기구)"
      ],
      "signal": "bullish",
      "signal_reason": "전 세계적인 탄소 규제 장기화로 노후 선박들의 무탄소 연료선 교체 사이클이 도래했고, 독점적 고난도 선박 제조 역량을 가진 국내 대형 조선3사(특히 HD현대 계열)의 수주 잔고와 선가 상승세가 장기적으로 우상향을 지지합니다.",
      "key_companies": [
        "HD한국조선해양",
        "HD현대중공업"
      ],
      "insight": "조선업은 오랜 고정비 부담을 이겨내고 선별 수주가 가능한 판매자 우위 시장(Seller's Market)으로 돌아섰습니다. 특히 단순한 조립 공장이 아닌 미래 해상 SMR 발전선이나 수소 추진 밸류체인의 원천 지식과 자회사를 틀어쥔 지주사(HD한국조선해양)에 투자하는 것이 양적 성장을 넘어 질적 고부가가치 마진을 온전히 획득하는 가장 확실한 전략입니다.",
      "action_point": "전통 디젤엔진 부품 중심에서 친환경 메탄올·암모니아 기자재 및 무탄소 선박 기자재(예: 보냉재, 고압 밸브, 극저온 가스 밸브사) 특화 기업들로 포트폴리오를 전환하고, 한국조선해양 지분을 점진적으로 분할 매집해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["energy", "tech"],
      "tags": ["조선업사이클", "HD한국조선해양", "친환경선박", "IMO환경규제", "수소연료전지", "SMR선박", "엄경아"]
    }
  },
  "jyU-nJNYOqQ": {
    "primary": "crypto",
    "video": {
      "id": "jyU-nJNYOqQ",
      "title": "비트코인 32개 매도, 끝이 아닙니다. JP모건이 필사적으로 숨기려는 '진짜 속내'",
      "published": "2026-06-03T11:40:00+00:00",
      "channel_name": "디파이 농부 조선생 | Professor Jo",
      "url": "https://www.youtube.com/watch?v=jyU-nJNYOqQ",
      "thumbnail": "https://img.youtube.com/vi/jyU-nJNYOqQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "마이크로스트레티지(MSTR)의 32 BTC($250만) 소량 매도로 비트코인 시장이 흔들렸으나, 이는 신념 약화가 아닌 주당 보유 비통코인 지표인 BPS(Bitcoin Per Share)를 지키기 위한 정교한 자본 조달 결정이었습니다. MSTR의 부채 및 우선주 선순위 구조를 고려할 때, NAV 프리미엄이 **1.22** 임계점 부근으로 내려오면 보통주 추가 증자(ATM) 대신 비트코인을 소량 매도해 자금을 조달하는 것이 주주 가치 훼손을 최소화하는 최선책입니다.",
      "key_claims": [
        "MSTR의 32개 비트코인 매도는 운영비 조달을 위해 주주 가치 BPS를 극대화하려는 금융 논리적 선택이었다.",
        "MSTR은 부채와 우선주가 보통주에 선순위하는 복합 금융 구조를 지녀, 단순 NAV 배수가 높은 수준을 유지해야 증자 혜택을 누릴 수 있다.",
        "주당 가치를 가늠하는 NAV 프리미엄 임계점은 **1.22**이며, 이 수치보다 높을 때는 ATM 보통주 발행을 통해 코인을 매수하고, 낮을 때는 코인을 팔아 현금을 확보하는 밴드 트레이딩 구조다."
      ],
      "data_points": [
        "MSTR 비트코인 매도 물량: 32 BTC (약 250만 달러 상당)",
        "매도 보도 시점의 비트코인 시총 증발액: 약 420억 달러",
        "ATM 증자 유리성 NAV 프리미엄 임계선: 1.22 (현재 NAV 수준 약 1.25)"
      ],
      "signal": "bullish",
      "signal_reason": "시장은 MSTR의 코인 매도를 악재로 오해했으나, 이는 BPS 주당 비트코인 보유 가치를 최대로 보호하려는 정밀한 재무 최적화의 결과이며 MSTR의 자금 조달 및 보유고 성장 방정식은 견고하게 유지되고 있습니다.",
      "key_companies": [
        "마이크로스트레티지",
        "JP모건"
      ],
      "insight": "마이크로스트레티지는 단순한 비트코인 보유 금고가 아니라, 부채와 보통주 차익거래(Arbitrage)를 통해 주당 비트코인 보유량(BPS)을 지속적으로 증식하는 복합 레버리지 금융공학 회사입니다. NAV 프리미엄 1.22 임계선을 활용한 그들의 동적 자본 배분 전략은 하락장과 정체기에도 주당 가치를 지켜내는 영리한 해자입니다.",
      "action_point": "MSTR의 코인 매도를 단순 악재로 해석한 대중의 패닉 셀링 기회를 비트코인 현물 및 MSTR 주식의 분할 저점 매수 기회로 포착하고, MSTR의 분기별 NAV 배수가 1.22 지지선 위에서 안착하는지를 계속 모니터링해야 합니다."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": ["stock"],
      "tags": ["마이크로스트레티지", "MSTR", "BPS", "NAV프리미엄", "비트코인매도", "금융공학", "자본조달"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["video"], info["analysis"], info["classification"])
