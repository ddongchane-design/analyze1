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
  "4gRQXb_uLr4": {
    "primary": "tech",
    "video": {
      "id": "4gRQXb_uLr4",
      "title": "[기업IR] 젬백스 남경필 회장 취임식 및 비전 선포식",
      "published": "2026-06-17T02:58:40+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=4gRQXb_uLr4",
      "thumbnail": "https://img.youtube.com/vi/4gRQXb_uLr4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "남경필 신임 회장이 대주주 지분의 의결권을 위임받아 책임 경영과 주주 소통 강화를 선언하며, <span class=\"text-cyan-300 font-semibold\">젬백스앤카엘</span>의 새로운 도약을 위한 비전을 발표했습니다.\n회사는 반도체 및 디스플레이 공정에 필수적인 <span class=\"text-cyan-300 font-semibold\">케미컬 에어 필터</span> 제조 사업(국내 시장 점유율 58%)을 통해 안정적인 <span class=\"text-amber-300 font-bold\">캐시카우</span>를 확보하고 있습니다.\n이를 기반으로 다중 기전 신약 후보 물질인 <span class=\"text-cyan-300 font-semibold\">GV1001</span>을 개발 중이며, 치료제가 없는 희귀 뇌질환인 진행성 핵상 마비(<span class=\"text-cyan-300 font-semibold\">PSP</span>) 치료제의 국내 3상 조건부 허가 획득 및 글로벌 임상을 추진하고 있습니다.",
      "key_claims": [
        "남경필 신임 회장은 대주주 의결권 위임을 통한 투명 경영과 적극적인 주주 소통(IR 정례화)을 선언함.",
        "젬백스는 반도체 에어 필터의 안정적 현금 흐름을 바탕으로 장기 임상 자금을 충당하여 여타 바이오 벤처 대비 높은 재무 안정성을 지님.",
        "<span class=\"text-cyan-300 font-semibold\">GV1001</span>은 다중 기전 약물로 <span class=\"text-cyan-300 font-semibold\">PSP</span> 치료제로서 미국/유럽/한국에서 희귀의약품 지정을 확보하여 강한 특허 장벽을 보유함."
      ],
      "data_points": [
        "반도체 에어 필터 국내 점유율: 58% (디스플레이 60%로 양대 시장 1위)",
        "2025년 기준 환경 사업부 매출 700억 원, 순이익 174억 원 기록",
        "지적재산권 보유 수: 전 세계 총 479건 (특허 355건 포함)",
        "PSP 희귀의약품 지정(ODD) 시장 독점권 기간: 미국 7년, 유럽/한국 10년"
      ],
      "signal": "bullish",
      "signal_reason": "반도체 에어 필터 사업의 확실한 캐시카우를 기반으로 임상 자금을 충당하는 안정적 구조 하에, PSP 치료제 <span class=\"text-cyan-300 font-semibold\">GV1001</span>의 국내 3상 조건부 허가 심사 및 글로벌 임상 진척이 무형 자산 가치를 높이고 있습니다.",
      "key_companies": ["젬백스", "삼성제약", "삼성전자", "SK하이닉스"],
      "insight": "단순한 바이오 벤처와 달리 반도체 산업 필수 부품(에어 필터)의 점유율 1위 캐시카우를 보유하고 있어 자금 조달 리스크가 적으며, 독점적 IP 포트폴리오(용도 특허 및 희귀의약품 지정)로 신약 상업화 시 강한 진입장벽을 구축할 것입니다.",
      "action_point": "2026년 하반기 국내 <span class=\"text-cyan-300 font-semibold\">PSP</span> 조건부 허가 결과 및 글로벌 임상 IND 신청 일정에 주목하며, 중장기적인 무형 자산 가치 상승을 고려한 긴 호흡의 투자가 유효합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock", "etc"],
      "tags": ["젬백스", "남경필", "GV1001", "PSP", "반도체필터", "기업IR"]
    }
  },
  "5Iq71prrSf0": {
    "primary": "economy",
    "video": {
      "id": "5Iq71prrSf0",
      "title": "[Kim Jong-hak’s New York, Now – June 18] Fed Chair Kevin Warsh on ‘Interest Rate Freeze’: “It’s a good day...”",
      "published": "2026-06-18T06:27:22+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=5Iq71prrSf0",
      "thumbnail": "https://img.youtube.com/vi/5Iq71prrSf0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "신임 연준 의장인 <span class=\"text-cyan-300 font-semibold\">케빈 워시</span>의 첫 데뷔전에서 성명서가 극도로 단순화되고 <span class=\"text-rose-400 font-medium\">포워드 가이던스가 폐지</span>되면서 시장에 매파적인 충격을 주었습니다.\n연준은 기준금리를 동결했으나 점도표를 통해 위원들의 절반이 최고 <span class=\"text-rose-400 font-medium\">6%대 추가 금리 인상</span> 가능성을 제시하여 12월 인상 가능성을 시사했습니다.\n한편, <span class=\"text-cyan-300 font-semibold\">도널드 트럼프</span> 미국 대통령은 G7 기자회견에서 영구적 전쟁 종식과 원유 수출 재개를 골자로 한 <span class=\"text-violet-300 font-medium\">이란과의 평화 합의</span> 타결이 임박했음을 밝혔습니다.",
      "key_claims": [
        "케빈 워시 연준 의장은 미래 금리 경로에 대한 포워드 가이던스를 폐지하여 연준의 재량권과 데이터 의존적 결정을 강화하려 함.",
        "연준 점도표는 2026년 12월 추가 금리 인상 가능성을 높게 시사하여 시장의 조기 금리 인하 기대를 꺾어버림.",
        "트럼프 대통령이 추진하는 <span class=\"text-violet-300 font-medium\">이란과의 평화 합의</span>가 공식 서명되면 지정학적 악재는 상당 부분 소멸될 것임."
      ],
      "data_points": [
        "뉴욕 3대 지수 하락률: S&P 500 -1.21%, 나스닥 -1.35%, 다우 -0.98%",
        "미국 기준금리: 3.50%~3.75% 범위에서 동결",
        "점도표: 18명의 연준 위원 중 절반이 최고 6%대 금리 인상 가능성 표시",
        "이란 합의안 규모: 이란 재건 지원 명분 최소 3,000억 달러 지원 및 원유 수출 재개 조건 포함"
      ],
      "signal": "bearish",
      "signal_reason": "케빈 워시 의장의 매파적 데뷔전과 포워드 가이던스 폐지, 점도표상 추가 금리 인상 가능성 시사로 인해 시장의 금리 인하 기대감이 소멸하며 고금리 장기화 우려가 확산되고 있습니다.",
      "key_companies": ["NVIDIA", "Google", "Microsoft", "Apple", "마이크론", "브로드컴", "스페이스X"],
      "insight": "케빈 워시 연준 의장은 정보 제공을 최소화하고 재량에 기반한 통화 정책을 펼치는 '워시 주의'를 천명했습니다. 반면 트럼프의 이란과의 평화 합의 타결 임박은 유가 급등 리스크를 차단하여 인플레이션 안정화에는 긍정적 기여를 할 수 있습니다.",
      "action_point": "고금리 긴장이 다시 부각된 만큼 밸류에이션이 높은 소프트웨어 대형주 비중을 조절하고, 장기 계약으로 실적이 담보되는 반도체 하드웨어 대장주나 에너지 관련 수혜주 위주로 방어적 포지션을 취해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["케빈워시", "FOMC", "금리동결", "점도표", "이란합의", "뉴욕증시", "트럼프"]
    }
  },
  "8ifkwnuet-M": {
    "primary": "tech",
    "video": {
      "id": "8ifkwnuet-M",
      "title": "[어바웃 뉴욕] 뉴욕 전자제품 가게의 작은 칩… \"AI의 기억은 누가 파는가\" | 이나연 특파원",
      "published": "2026-06-17T02:00:33+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=8ifkwnuet-M",
      "thumbnail": "https://img.youtube.com/vi/8ifkwnuet-M/hqdefault.jpg"
    },
    "analysis": {
      "summary": "AI 인프라 경쟁이 연산 장치(GPU, HBM) 중심에서 방대한 데이터를 저장하기 위한 <span class=\"text-cyan-300 font-semibold\">NAND 플래시 및 기업용 SSD</span> 시장으로 빠르게 확산되고 있습니다.\n2025년 웨스턴 디지털에서 독립하여 부활한 <span class=\"text-cyan-300 font-semibold\">샌디스크</span>는 최근 빅테크 고객사들과 수백억 달러 규모의 <span class=\"text-cyan-300 font-semibold\">장기 공급 계약</span>을 체결하며 AI 저장 장치의 핵심 수혜주로 떠올랐습니다.\n과거의 단기적인 메모리 공급 과잉 <span class=\"text-rose-400 font-medium\">사이클 변동성</span>에서 벗어나 빅테크의 물량 선점 경쟁으로 메모리 산업 전반의 안정적 장기 성장이 전망됩니다.",
      "key_claims": [
        "AI 모델 고도화로 인한 데이터 폭증은 GPU 가속기뿐만 아니라 대용량 장기 저장 장치인 <span class=\"text-cyan-300 font-semibold\">NAND 플래시 및 기업용 SSD</span>의 성장을 유도합니다.",
        "샌디스크는 독립 법인 부활과 동시에 AI 데이터 저장 장치 수요 폭증의 직접 수혜를 입어 주가가 가파르게 상승함.",
        "메모리 반도체 시장이 과거의 극단적인 공급 과잉 사이클에서 벗어나 <span class=\"text-cyan-300 font-semibold\">장기 공급 계약</span> 구조로 고착화되고 있어 하방 압력이 제한적일 수 있습니다."
      ],
      "data_points": [
        "샌디스크의 빅테크 고객사 장기 공급 계약 수: 5건 (이 중 3건의 합산 규모만 약 420억 달러)",
        "샌디스크 창업 연도: 1988년 (2016년 웨스턴 디지털에 190억 달러 인수 후 2025년 독립)",
        "샌디스크 공동 창업자인 산제이 메로트라는 현재 경쟁사인 마이크론의 CEO로 재임 중임"
      ],
      "signal": "bullish",
      "signal_reason": "AI 가속기 중심에서 대량 데이터 장기 저장을 위한 기업용 SSD 및 NAND 플래시로 수요가 확장되고 있으며, 빅테크 기업들과의 수백억 달러 규모 장기 계약을 통해 실적 가시성이 확보되었습니다.",
      "key_companies": ["샌디스크", "웨스턴 디지털", "마이크론", "삼성전자", "SK하이닉스"],
      "insight": "샌디스크의 재도약은 AI 인프라 확장이 연산(두뇌)을 넘어 저장(기억)의 영역인 NAND 및 SSD 시장으로 확산되고 있음을 증명합니다. 장기 계약을 통해 가격 및 수급 변동성이 완화되고 있는 점은 메모리 기업들의 멀티플 리레이팅 요인입니다.",
      "action_point": "AI 데이터 센터의 대규모 스토리지 구축 수혜를 받는 낸드 플래시 및 SSD 대장주(샌디스크, 삼성전자, SK하이닉스)의 포지션을 강화하고, 과거의 단순 사이클 우려에 따른 주가 조정을 매수 기회로 활용해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["샌디스크", "NAND플래시", "기업용SSD", "메모리반도체", "장기계약", "AI스토리지", "마이크론"]
    }
  },
  "bq_GAPruaYU": {
    "primary": "etc",
    "video": {
      "id": "bq_GAPruaYU",
      "title": "\"AI도 모릅니다\" 서울대 교수가 밝힌 필리핀 8.2 강진의 진실",
      "published": "2026-06-18T06:31:00+09:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=bq_GAPruaYU",
      "thumbnail": "https://img.youtube.com/vi/bq_GAPruaYU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "필리핀 민다나오 남부에서 발생한 규모 7.8의 강진은 동서 양쪽 판이 동시에 파고드는 복잡한 <span class=\"text-amber-300 font-bold\">이중 섭입 구조</span> 및 판 내부 단층에서 기인한 것으로 보입니다.\n아무리 현대의 고성능 <span class=\"text-cyan-300 font-semibold\">AI 모델</span>을 사용하더라도 지진의 발생 시기와 정확한 위치를 예측하는 것은 과학적으로 불가능하다고 학계는 지적합니다.\n자연재해 피해를 막기 위해 지진 예측 연구도 중요하지만, 실질적인 인명 피해 방지를 위해 <span class=\"text-rose-400 font-medium\">내진 설계 의무화</span>와 신속한 조기 경보 체계 작동이 최우선되어야 합니다.",
      "key_claims": [
        "현대의 고도화된 AI 예측 모델을 적용하더라도 지진의 발생 시점과 정확한 위치를 실시간으로 예측하는 것은 불가능함.",
        "필리핀 민다나오 지역은 동서 양방향에서 판이 섭입하는 이중 섭입 구조와 거대한 필리핀 단층이 얽혀 지진이 매우 빈번한 지질학적 특징을 가짐.",
        "지진 예측보다는 건물의 내진 설계 강화와 지진해일(쓰나미) 경보 시스템의 효율적 활용이 인명 피해를 줄이는 핵심임."
      ],
      "data_points": [
        "지진 발생 규모 및 깊이: 규모 7.8 (초기 8.2), 깊이 55km 관측",
        "과거 1976년 동일 해구 지진: 규모 8.1 발생으로 8,000여 명 사망 (당시 쓰나미 조기 경보 부재)"
      ],
      "signal": "neutral",
      "signal_reason": "과학적 사실과 재해 대비 방안을 설명하는 교양형 콘텐츠로, 거시적이나 시장 관점에서의 단기 경제 시그널은 중립적입니다.",
      "key_companies": [],
      "insight": "AI가 만능 해결사가 아니며 지진과 같은 무작위성이 높은 자연재해의 정확한 발생 시점을 예측하는 데에는 뚜렷한 한계가 있음을 시사합니다. 결국 사전 방재 인프라 구축 및 건설 기준(내진 설계) 강화 등 제도적 대비가 우선되어야 합니다.",
      "action_point": "재해 방지 인프라, 도시 안전 대책 및 내진 기자재와 같은 방재 섹터의 정책적 지원 가능성에 장기적으로 관심을 둘 수 있습니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["tech"],
      "tags": ["필리핀지진", "민다나오", "지진예측", "AI한계", "쓰나미경보", "내진설계", "지구과학"]
    }
  },
  "Ck7rZxtC1BU": {
    "primary": "etc",
    "video": {
      "id": "Ck7rZxtC1BU",
      "title": "[지식뉴스] 집값, 도대체 왜 안 잡힐까?..무서운 전월세 대란의 시작, 서울 아파트값이 심상찮은 진짜 이유 (ft.김학렬 스마트튜브 부동산조사연구소장) / 교양이를 부탁해",
      "published": "2026-06-18T06:30:28+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=Ck7rZxtC1BU",
      "thumbnail": "https://img.youtube.com/vi/Ck7rZxtC1BU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "서울 수도권 아파트 시장의 우상향 흐름과 <span class=\"text-rose-400 font-medium\">전월세 가격 폭등</span>의 구조적 원인을 진단합니다. 서울은 빈 땅이 없어 재개발/재건축 외에 추가 공급이 어려운 지리적 한계를 안고 있습니다.\n최근 전세 사기 노이즈 등으로 다세대 빌라 공급이 기존의 5분의 1 수준으로 급감함에 따라, <span class=\"text-rose-400 font-medium\">임차 주택 쇼티지</span>가 발생하고 빠른 속도로 월세화가 전개되고 있습니다.\n결국 부동산 시세는 <span class=\"text-cyan-300 font-semibold\">강남 업무지구</span> 등으로의 직주 근접성이 핵심이며, 정부의 인위적 전세 대출 억제 정책이 오히려 서민 임차인의 주거비 가중을 부르는 악순환을 유발하고 있습니다.",
      "key_claims": [
        "서울은 신규 택지 부족으로 인해 근본적인 아파트 대량 공급이 불가능하므로 장기적으로 집값 하락 확률이 매우 낮습니다.",
        "빌라 기피와 건설 위축으로 서울 다세대 공급이 급감하면서 아파트로 못 가는 임차인의 대안이 소멸되어 <span class=\"text-rose-400 font-medium\">주거 안정성 훼손</span>이 심화되고 있습니다.",
        "직장이 가장 많고 연봉이 높은 <span class=\"text-cyan-300 font-semibold\">강남 권역</span> 및 이에 인접한 수도권 핵심지(과천, 성남 등)의 주거 가치는 독보적으로 강화될 것입니다."
      ],
      "data_points": [
        "강남구 상주 인구는 약 50만 명이나 양질의 일자리는 약 70만~80만 개 달해 배후 주거 수요 폭발적",
        "서울 빌라/다세대 신규 공급 물량: 과거 연 4만 호 대비 최근 20% 미만 수준인 1/5 수준으로 토막",
        "과거 임대차 계약의 80% 이상이 전세였으나 현재 아파트/빌라 모두 월세화 비중 과반 돌파 추세"
      ],
      "signal": "neutral",
      "signal_reason": "부동산 가격 상승과 전월세 대란은 내수 소비 여력을 극도로 갉아먹는 거시 경제적 요인이나, 핵심 실물 자산으로서의 서울 부동산 가치는 탄탄한 수요를 바탕으로 방어력이 입증되고 있습니다.",
      "key_companies": [],
      "insight": "정부의 인위적 전세 제도 억제 스탠스는 임차 수요를 월세로 내몰아 주거비 부담 증가와 인플레이션 고착화를 낳고 있습니다. 직주근접성이 우수한 핵심지 아파트의 독점성은 갈수록 강화되는 양극화 장세가 이어집니다.",
      "action_point": "가계 자산의 포트폴리오 차원에서 핵심 입지 중심의 1주택 보유 전략을 강화하고, 내수 소비 위축 가능성에 대비해 유통/내수주보다는 글로벌 수출 경쟁력이 높은 기업이나 주거 복지 리츠 등에 초점을 맞춰야 합니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["부동산", "서울집값", "전세대란", "직주근접", "강남접근성", "빌라공급", "월세화"]
    }
  },
  "DFy2WJJYFJA": {
    "primary": "tech",
    "video": {
      "id": "DFy2WJJYFJA",
      "title": "Claude Fable: The AI Banned Worldwide, But Why?",
      "published": "2026-06-18T06:28:00+00:00",
      "channel_name": "월텍남",
      "url": "https://www.youtube.com/watch?v=DFy2WJJYFJA",
      "thumbnail": "https://img.youtube.com/vi/DFy2WJJYFJA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "앤스로픽의 초고성능 신규 AI 모델인 <span class=\"text-cyan-300 font-semibold\">페이블 5(Claude Fable 5)</span>가 미국 정부의 수출 통제 대상으로 지정되어 글로벌 유통이 규제된 아이러니를 파헤칩니다. 페이블 5는 아티피셜 애널리시스 평가에서 종합 65점을 획득해 타 모델들을 압도하는 독보적인 코딩 및 종합 지능을 증명했습니다.\n이 사태는 AI 모델이 단순 소프트웨어가 아닌 핵무기와 같은 <span class=\"text-rose-400 font-medium\">국가 안보용 전략 자산</span>화되고 있음을 보여주며, 이는 주권적 보안 인프라인 <span class=\"text-violet-300 font-medium\">소벌린 AI(Sovereign AI)</span>와 데이터 센터 하드웨어 밸류체인의 폭발적인 성장을 자극하는 방아쇠가 되고 있습니다.",
      "key_claims": [
        "미국 정부가 페이블 5의 수출을 제한한 것은 초고성능 프론티어 AI의 파괴력과 사이버 위협 리스크를 실질적으로 경계하기 시작했기 때문입니다.",
        "AI의 막강한 생산성 통제권을 특정 국가에 종속당하지 않기 위해 전 세계적으로 <span class=\"text-violet-300 font-medium\">독자 데이터 센터 인프라</span>를 구축하려는 움직임이 급물살을 타고 있습니다.",
        "고성능 연산에 동반되는 극단적인 토큰 비용과 에너지 사용량 증가로 인해, 전력 및 고대역폭 네트워킹/메모리 부품의 장기 CapEx 수요는 더욱 견고해질 것입니다."
      ],
      "data_points": [
        "페이블 5 아티피셜 애널리시스 종합 지수: 65점 기록 (GPT-5.5 60점, 클로드 4.8 오퍼스 61점, 제미나이 57점 대비 압도적 1위)",
        "엔비디아의 새로운 매출 분류 기준: 데이터 센터 매출 중 소벌린 AI 및 네오클라우드(ACI 부서) 비중이 빅테크(하이퍼스케일러)와 1:1에 근접 (각각 약 370억, 380억 달러 기록)"
      ],
      "signal": "bullish",
      "signal_reason": "최첨단 AI 기술 통제가 소벌린 AI 인프라 구축 경쟁을 가열시키며, AI 관련 반도체 가속기, 메모리, 네트워킹, 전력 설비 등 물리적 하드웨어 공급망 전반에 전례 없는 장기 수주 사이클을 제공합니다.",
      "key_companies": ["앤스로픽", "NVIDIA", "Google", "Microsoft"],
      "insight": "모델의 성능 고도화가 정부 통제를 유발할 수준에 도달함으로써 각국은 독자적인 클라우드 안보 체계 구축에 집중하게 됩니다. 이는 엔비디아 등 가속기 공급업체의 하드웨어 시장 독점 체제를 장기화하는 요인입니다.",
      "action_point": "AI 전방 칩(엔비디아, 브로드컴), 전력 안보 설비(GE 버노바 등), 초고속 네트워크 부품 기업의 비중을 적극 확대하고, 미국 규제 노출도가 적은 독립 소벌린 클라우드 운영 파트너사들에 주목해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock", "economy"],
      "tags": ["앤스로픽", "페이블5", "수출규제", "소벌린AI", "AI인프라", "토큰비용", "인프라주권"]
    }
  },
  "E7aL3DiXqpg": {
    "primary": "economy",
    "video": {
      "id": "E7aL3DiXqpg",
      "title": "[홍장원의 불앤베어] 매파냐 비둘기파냐... 다시 봐도 헷갈리는 워시 의장 데뷔전",
      "published": "2026-06-18T06:27:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=E7aL3DiXqpg",
      "thumbnail": "https://img.youtube.com/vi/E7aL3DiXqpg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "6월 FOMC에서 <span class=\"text-cyan-300 font-semibold\">케빈 워시</span> 의장의 데뷔전을 동반한 연준의 매파적 통화정책 스탠스와 그에 숨겨진 철학적 복선을 심층 분석합니다. 성명서는 포워드 가이던스를 배제해 극도로 짧아졌고, 인플레이션 전망치(PC 3.6%) 상향과 더불어 연내 추가 금리 인상 주장이 과반에 달하는 등 시장은 매파적으로 소화했습니다.\n하지만 워시 의장의 본의는 인플레이션의 원인을 공급 측면(에너지 충격)에 둠으로써 무리한 금리 인상이 실물 경기를 침체시킬 <span class=\"text-rose-400 font-medium\">스태그플레이션 리스크</span>를 경계하고 있습니다.\n그는 AI와 기술 혁신을 통한 <span class=\"text-cyan-300 font-semibold\">생산성 향상</span>이 '낮은 물가와 높은 고용의 공존'을 이끄는 디스인플레이션을 실현해 장기적으로 금리를 인하할 명분을 만들 것이라 보고, 구식 데이터 수집 방식을 바꾸기 위한 개혁 TF 구성을 선포했습니다.",
      "key_claims": [
        "워시 의장은 시장 소음과 연준의 미래 스탠스 제약을 방지하기 위해 구두 소통을 줄이고 포워드 가이던스를 전면 배제했습니다.",
        "점도표의 중간값은 연내 추가 1회 인상을 강하게 시사했으나, 워시 의장은 자신의 점도표 제출을 거부하며 점도표의 권위를 깎아내렸습니다.",
        "장기적인 경제 해법은 수요 억제가 아닌 <span class=\"text-cyan-300 font-semibold\">AI 기반 공급 측면의 생산성 혁신</span>에 있으며, 이를 통해 인플레이션 없는 고성장이 가능할 것이라는 지론을 유지 중입니다."
      ],
      "data_points": [
        "연준 2026년 PCE 인플레이션 전망치: 3월 2.7% 대비 3.6%로 상향 조정 (근원 PCE도 3.3%로 상향)",
        "성명서 분량: 4월 341단어에서 6월 132단어로 대폭 간소화",
        "6월 기준 금리는 3.5%~3.75%로 유지했으나 2026년 GDP 성장률 전망은 2.2%로 소폭 하향"
      ],
      "signal": "bearish",
      "signal_reason": "단기적으로는 완화적 문구 삭제 및 점도표 추가 인상 우려로 할인율 부담이 확대되어 지수에 단기 하방 압력을 제공하지만, 중장기적으로 생산성 향상에 기반한 연준의 금리 안정화 철학은 시장 펀더멘탈을 지탱합니다.",
      "key_companies": ["NVIDIA", "GE Vernova", "마이크론"],
      "insight": "워시는 인플레이션 수치를 잡기 위해 연준이 선제적으로 경기 침체를 유도하는 구식 방식을 거부합니다. 그는 AI 생산성 지표가 실시간 데이터 세트 구축을 통해 확인되는 즉시, 시장이 우려하는 초고금리 긴장 상태를 해소할 근거로 활용하려 할 것입니다.",
      "action_point": "단기 금리 반등에 따른 지수 조정 시, 생산성 향상의 본체인 반도체 대장주와 전력 인프라 대장주의 비중을 분할 매수로 꾸준히 넓혀가고, 금리 민감도가 높은 중소형 기술주의 과도한 베팅은 억제해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["케빈워시", "FOMC", "금리전망", "점도표", "생산성혁신", "디스인플레이션", "연준개혁"]
    }
  },
  "EXU1-fdPDU0": {
    "primary": "economy",
    "video": {
      "id": "EXU1-fdPDU0",
      "title": "경제 교과서 틀렸다. 물가 때문에 금리 인상해도 주가 오른다 (류상철 전 한국은행 국장)",
      "published": "2026-06-18T06:29:00+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=EXU1-fdPDU0",
      "thumbnail": "https://img.youtube.com/vi/EXU1-fdPDU0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "코로나 팬데믹 이후 금융 시장에서 미국 국채의 성격 변화와 채권 시장의 패러다임 전환을 설명합니다. 과거 위기 상황(전쟁, 지정학적 갈등) 시 안전자산 선호로 국채 가격이 올랐던 현상과 달리, 고인플레이션 국면에서는 금리가 상승하여 <span class=\"text-rose-400 font-medium\">채권 가격 폭락</span>과 주식과의 동반 약세가 나타나는 디커플링을 지적합니다.\n시장에서 통용되던 '위기 = 국채 매수'라는 전통적 공식이 깨진 핵심 원인은 연준 통화정책의 가중치가 경기 성장보다 인플레이션 억제에 극단적으로 치우쳤기 때문입니다.\n채권 투자자들은 단순 기준금리 변화에만 집착하기보다, 미래 금리 경로의 예상치 평균을 대변하는 <span class=\"text-cyan-300 font-semibold\">시장 금리(장기채 금리)</span>의 구조적 변화에 주목하여 자산 배분 전략을 수정해야 함을 강조합니다.",
      "key_claims": [
        "인플레이션 유도형 위기 상황에서는 국채가 전통적인 <span class=\"text-rose-400 font-medium\">안전지대(Safe haven)</span>의 역할을 수행하지 못하며 오히려 포트폴리오의 손실을 키웁니다.",
        "시장 금리는 단순 중앙은행의 정책 금리뿐만 아니라, 채권 딜러들이 예상하는 장기적인 통화 긴축 기조의 누적 평균에 의해 결정됩니다.",
        "거시 경제 환경이 저물가 기조에서 구조적 고물가 기조로 고착화된 만큼 채권 시장의 밸류에이션 모델도 근본적으로 수정되어야 합니다."
      ],
      "data_points": [
        "중앙은행 통화정책 결정 가중치상 인플레이션 억제 비중이 경기 방어보다 1.5배 이상 높게 설정되어 있음",
        "팬데믹 이후 대규모 지정학적 돌발 위기 시 미국 국채 가격이 동반 하락하며 전통 헤지 펀드의 채권 포트폴리오 대폭 손실 기록"
      ],
      "signal": "neutral",
      "signal_reason": "전통적인 안전자산 헤징 모델의 작동 오류는 자산 배분 포트폴리오의 변동성을 키우는 요인이나, 장기 채권 금리의 고공 행진을 인지하고 유연하게 대응하는 관점을 제공하므로 중립적입니다.",
      "key_companies": [],
      "insight": "연준의 통화정책 방정식이 인플레이션에 더 민감해진 환경에서는 국채의 주식 헤징 기능이 약화됩니다. 인플레이션을 방어해 주는 원자재나 실질 성장력을 증명하는 우량 주식 자산이 국채의 대체재로 기능할 수 있습니다.",
      "action_point": "단순 국채 매수를 통한 포트폴리오 방어 전략을 지양하고, 현금 비중 유지 및 인플레이션 전가력이 높은 고배당 우량 성장주와 달러 표시 유동성 자산으로 포트폴리오를 재편하는 것이 바람직합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["미국국채", "시장금리", "안전자산", "인플레이션", "통화정책", "채권투자", "한국은행"]
    }
  },
  "hAg6Vi7iq4U": {
    "primary": "economy",
    "video": {
      "id": "hAg6Vi7iq4U",
      "title": "6월 FOMC l 윤제성 아레타노바컨설팅 설립자 인터뷰",
      "published": "2026-06-18T06:26:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=hAg6Vi7iq4U",
      "thumbnail": "https://img.youtube.com/vi/hAg6Vi7iq4U/hqdefault.jpg"
    },
    "analysis": {
      "summary": "윤제성 전 뉴욕생명자산운용 CIO가 본 6월 FOMC 분석과 하반기 글로벌 투자 전략을 제시합니다. 신임 연준 의장인 <span class=\"text-cyan-300 font-semibold\">케빈 워시</span>가 보여준 앨런 그린스펜식의 모호하고 절제된 소통 방식과 점도표 무용론(본인의 점 미제출)에 주목합니다.\n유럽(ECB), 일본(BOJ)의 금리 인상과 한국은행의 7월 인상 가능성 등 글로벌 통화 정책의 바이어스가 <span class=\"text-rose-400 font-medium\">긴축 방향</span>으로 선회하고 있음을 짚어줍니다.\n미국 경제는 단기적으로 구조적 인플레이션 하단이 3%대에 안착하는 과도기를 겪고 있어, 연준이 금리를 대폭 낮추지 못하고 고금리를 유지할 확률이 높으므로 기업들의 총마진 둔화 압력을 주의해야 한다고 경고합니다.",
      "key_claims": [
        "워시 의장은 그린스펜을 존경하여 앞으로 시장에 미래 가이던스를 최소한으로만 주고 스스로의 정책 재량을 극대화할 것입니다.",
        "글로벌 주요국 중앙은행들이 차례로 금리를 인상하고 있어, 미국의 고금리 동조화에 맞춰 글로벌 <span class=\"text-rose-400 font-medium\">자본 비용 증가</span> 압력이 커지고 있습니다.",
        "AI 혁명으로 헬스케어 및 인프라를 중심으로 노동 시장이 강세를 띄고 있어 단기 임금 상승발 끈적한 인플레이션이 유지되고 있습니다."
      ],
      "data_points": [
        "미국의 구조적 인플레이션 지지선: 3%대 형성",
        "연준의 기준금리 하방 지지선(중립 금리): 약 3% 수준으로 추정 (과거 저금리 시대로의 복귀 불가능)",
        "WTI 국제유가는 단기적으로 지정학적 타결 기대로 75달러 선 안착 중"
      ],
      "signal": "neutral",
      "signal_reason": "고금리 장기화 기조와 글로벌 통화 긴축 동조화는 성장주 밸류에이션에 부담 요인이지만, 견조한 기업 실적과 탄탄한 노동 시장이 지수의 급격한 붕괴를 제한하는 균형을 형성하고 있습니다.",
      "key_companies": ["NVIDIA", "마이크론"],
      "insight": "연준 금리의 최종 안착지가 3% 수준으로 높아진 '고금리 고착화(Higher for longer)' 환경이 구축되었습니다. 기업들은 향후 높은 이자 부담 속에서 마진 스프레드를 방어할 수 있는 독점적 가격 결정력이 있는 곳 위주로 쏠릴 수밖에 없습니다.",
      "action_point": "밸류에이션이 지나치게 과열된 적자 테크 기업을 정리하고, 높은 자본 비용을 감당할 수 있는 현금 보유가 많고 영업이익률이 뛰어난 빅테크 및 반도체 장기 계약 수혜주로 포트폴리오를 압축해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["케빈워시", "FOMC", "구조적인플레이션", "대차대조표", "금리전망", "글로벌긴축"]
    }
  },
  "jNW5pCm2DBE": {
    "primary": "space",
    "video": {
      "id": "jNW5pCm2DBE",
      "title": "마이클 버리 \"스페이스X, 결국 코어위브 아류\" #shorts",
      "published": "2026-06-18T06:25:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=jNW5pCm2DBE",
      "thumbnail": "https://img.youtube.com/vi/jNW5pCm2DBE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "영화 *빅쇼트*의 주인공 마이클 버리가 최근 상장 후 폭등하며 시가총액 3조 달러에 근접한 <span class=\"text-cyan-300 font-semibold\">스페이스X</span>의 밸류에이션 거품을 저격한 쇼츠를 다룹니다. 버리는 스페이스X의 AI 데이터 센터 사업 및 통신 위성 확장을 부채가 많고 고평가 논란이 있는 <span class=\"text-rose-400 font-medium\">코어위브(Coreweave)의 아류</span>라고 비판했습니다.\n스페이스X는 버크셔 해서웨이의 시총을 단 3일 만에 2.5배 뛰어넘으며 사상 최고치를 달성했으나, 옵션 가격 폭등으로 인해 숏 배팅마저 포기할 정도로 극단적인 투기 광풍이 불고 있습니다.\n옵션 시장에서는 9월까지 주가가 50% 폭등할 확률(15%)과 반토막 날 확률(13%)이 팽팽히 대립하는 등 극강의 <span class=\"text-rose-400 font-medium\">변동성 딜레마</span>가 지목되고 있습니다.",
      "key_claims": [
        "스페이스X의 현재 시총은 연매출(약 200억 달러 미만) 대비 극단적인 버블 상태로, 닷컴 버블 말기의 탐욕과 유사한 양상을 보입니다.",
        "기관 및 리테일 투자자의 쏠림으로 꼬리 위험 헤지용 풋옵션 가격이 지나치게 비싸져 하락 배팅조차 실행하기 어려운 <span class=\"text-rose-400 font-medium\">수급 꼬임 현상</span>이 나타나고 있습니다.",
        "AI와 우주 인터넷(스타링크)의 결합에 대한 낙관론이 펀더멘탈을 지나치게 초과하고 있어 단기 조정 리스크가 큽니다."
      ],
      "data_points": [
        "스페이스X 시가총액: 상장 후 단기 폭등해 약 3조 달러 터치 및 아마존 추월",
        "스페이스X 옵션 확률 분포: 9월 만기 50% 추가 폭등 확률 15% vs 50% 급락(반토막) 확률 13% 대치"
      ],
      "signal": "bearish",
      "signal_reason": "매출 대비 지나치게 비대한 시가총액과 옵션 시장의 극단적 변동성은 장기 락업 해제 시점(8월 예정)에 맞춰 강한 단기 매물 출회 및 수급 붕괴 우려를 증폭시키므로 경계 신호입니다.",
      "key_companies": ["스페이스X", "코어위브", "버크셔 해서웨이"],
      "insight": "펀더멘탈의 뒷받침 없는 급등은 옵션 합성 수급과 개인의 광풍이 융합된 전형적인 버블 후기 현상입니다. 숏조차 비새서 칠 수 없는 구조는 시장이 극단적인 딜레마에 봉착했음을 보여줍니다.",
      "action_point": "단기 추격 매수를 극도로 금지하고, 8월 락업 해제 전후의 수급 추이를 관망하며 거품이 걷힌 이후 실질적인 우주/위성 인프라 실적이 확인되는 시점에 진입하는 것이 안전합니다."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["stock", "tech"],
      "tags": ["스페이스X", "마이클버리", "고평가논란", "옵션시장", "변동성", "AI인프라"]
    }
  },
  "joXndZUw0WE": {
    "primary": "etc",
    "video": {
      "id": "joXndZUw0WE",
      "title": "진짜 '물반 고기반' 생선 주워 먹는다",
      "published": "2026-06-18T06:24:00+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=joXndZUw0WE",
      "thumbnail": "https://img.youtube.com/vi/joXndZUw0WE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "동남아시아(태국, 베트남, 미얀마, 캄보디아, 라오스 등)의 음식 문화에 필수적인 <span class=\"text-cyan-300 font-semibold\">피시 소스(액젓)</span>의 탄생 기원과 메콩강 유역의 독특한 인문지리적 환경을 설명합니다.\n우기철 메콩강의 범람으로 민물이 넘치면서 주변 경작지까지 엄청난 생선이 밀려드는 자연 현상이 발생합니다.\n농민들이 일시적으로 생선을 손쉽게 수집하면서 남는 잉여 수산물을 장기 보존하기 위해 발효시키기 시작한 것이 <span class=\"text-cyan-300 font-semibold\">동남아 피시 소스 문화</span>의 핵심임을 재미있게 풀어냅니다.",
      "key_claims": [
        "메콩강 유역의 독특한 기후(우기와 건기의 변화)와 풍부한 수자원이 동남아 특유의 농업 및 어업 복합 문화를 형성했습니다.",
        "보존 기술이 발달하기 전 대량의 잉여 농수산물을 처리하려는 생계형 지혜가 발효 소스 산업으로 발전한 계기가 되었습니다."
      ],
      "data_points": [
        "유라시아 메콩강 영향권 5개국(미얀마, 태국, 캄보디아, 라오스, 베트남) 전체 요리 중 피시 소스 침투율 압도적 다수"
      ],
      "signal": "neutral",
      "signal_reason": "순수 문화/지리학 교육 콘텐츠로서 거시 경제나 기업 주가에 직접적인 시그널을 주지 않는 중립적인 주제입니다.",
      "key_companies": [],
      "insight": "동남아 요리의 독특한 풍미는 잉여 자원을 낭비하지 않고 장기 보존하려는 인류의 지리적 적응과 발효 과학의 결과물입니다.",
      "action_point": "투자 아이디어와 직접적인 연관성은 낮으므로, 글로벌 식음료 원자재 트렌드 및 유통 체인의 문화적 다양성을 이해하는 배경 지식으로 활용합니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["동남아음식", "피시소스", "메콩강", "어업문화", "식문화", "인문지리"]
    }
  },
  "mEHI19HUJeY": {
    "primary": "economy",
    "video": {
      "id": "mEHI19HUJeY",
      "title": "[LIVE] 6월 FOMC 성명서 해설 l 케빈 워시 FOMC '데뷔전'",
      "published": "2026-06-18T06:23:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=mEHI19HUJeY",
      "thumbnail": "https://img.youtube.com/vi/mEHI19HUJeY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "6월 FOMC 발표를 앞두고 시장의 동향과 당일 발표된 소비 지표, 지정학적 완화 조짐, 반도체 설계 자산 강세 요인을 분석한 라이브 방송입니다. 미국 5월 소매 판매가 전월 대비 0.9% 증가해 서프라이즈를 기록하며 미국의 견조한 <span class=\"text-amber-300 font-bold\">소비 모멘텀</span>을 재증명해 연준의 조기 금리 인하 어려움을 뒷받침했습니다.\n정치적으로는 트럼프 대통령이 19일로 예정된 <span class=\"text-violet-300 font-medium\">미-이란 종전 합의</span>를 '단순 양해각서(MOU)'로 규정하며 긴장을 유지했으나 유가는 70달러 중반으로 안정화되었습니다.\n번스타인의 리포트 상향 조정으로 전력 효율이 극대화된 <span class=\"text-cyan-300 font-semibold\">ARM 아키텍처</span>가 AI 에이전트 시대의 숨은 지배자로 꼽히며 반도체 랠리를 견인했습니다.",
      "key_claims": [
        "미국의 강력한 근원 소매 판매 지표는 연준이 성급하게 금리를 인하할 명분을 없애 고금리 긴장을 장기화시킵니다.",
        "트럼프의 이란에 대한 강경 구두 압박은 유리한 협상 타결을 유도하기 위한 전술이며, 시장은 이미 19일 평화 서명식을 기점으로 <span class=\"text-violet-300 font-medium\">지정학적 위험 완화</span>를 유가에 선반영 중입니다.",
        "AI 모델이 능동적으로 비서 역할을 수행하는 AI 에이전트로 진화하면서 전력 소모와 발열을 통제할 수 있는 <span class=\"text-cyan-300 font-semibold\">저전력 반도체 IP(ARM)</span>의 가치가 폭등하고 있습니다."
      ],
      "data_points": [
        "미국 5월 소매 판매 전월 대비 0.9% 증가 (예상치 0.5%의 약 2배 상회)",
        "근원 소매 판매(자동차/주유소 제외) 전월 대비 0.8% 증가 (이전 0.7% 및 예상 0.6% 상회)",
        "번스타인의 ARM 목표 주가: 300달러에서 500달러로 상향 조정하며 주가 당일 7.39% 급등"
      ],
      "signal": "neutral",
      "signal_reason": "소비 호조에 따른 고금리 고착 우려가 작용하는 동시에 AI 에이전트발 전방 반도체 설계 수요 급증 및 지정학적 리스크 해소 기대가 엇갈려 증시는 방향성을 모색하는 과도기입니다.",
      "key_companies": ["ARM", "NVIDIA", "마이크론", "브로드컴"],
      "insight": "고물가에도 미국 소비자들이 지갑을 닫지 않는 복원력을 보이고 있어 금리 인하 기대는 단기적으로 미뤄질 수밖에 없습니다. AI 시장은 개별 칩 조립에서 핵심 저전력 IP와 종합 플랫폼의 가치가 배가되는 국면입니다.",
      "action_point": "금리 압박 속에서도 실적 독점이 보장되는 반도체 IP 기업(ARM) 및 데이터 센터 관련 액체 냉각/종합 전력 안보주로의 포트폴리오 다변화가 필요합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["6월FOMC", "케빈워시", "소매판매", "트럼프", "이란평화협정", "ARM", "반도체랠리"]
    }
  },
  "MT9N5dQaIm4": {
    "primary": "economy",
    "video": {
      "id": "MT9N5dQaIm4",
      "title": "[LIVE] 케빈 워시 첫 FOMC 충격 결과: 인하에서 인상으로 뒤집힌 점도표 | 이나연 특파원",
      "published": "2026-06-18T06:22:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=MT9N5dQaIm4",
      "thumbnail": "https://img.youtube.com/vi/MT9N5dQaIm4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "케빈 워시 의장의 첫 FOMC 결과 점도표가 인하에서 추가 인상(19명 중 9명 추가 인상 의견)으로 극적으로 뒤집히며 시장에 준 충격을 다룹니다.\n금리 긴축을 장기화시키는 본질적 요인은 다름 아닌 <span class=\"text-cyan-300 font-semibold\">AI 데이터 센터 구축 붐</span>으로, 전력 및 물리적 설비에 천문학적 자금이 풀리고 관련 자산 가격 상승이 고소득층 소비를 진작해 단기 <span class=\"text-rose-400 font-medium\">인플레이션 가속화</span>의 주범으로 작동하고 있습니다.\n더불어 엔비디아를 거품이라 판단하고 매수를 배제한 채 기존 소프트웨어(어도비 등)에 집중했던 50년 전통의 폴랜 캐피털이 4년간 자산의 60%($500억)를 날린 뼈아픈 사례를 통해, 단기 거품론에 매몰된 고집스러운 투자가 낳는 <span class=\"text-rose-400 font-medium\">포트폴리오 붕괴 리스크</span>를 경고합니다.",
      "key_claims": [
        "연준 위원들의 심리가 단 3달 만에 인하에서 금리 추가 인상으로 선회했으며, 단기 차입 비용의 조기 하락 기대를 통째로 무너뜨렸습니다.",
        "AI 산업이 효율화로 물가를 낮출 것이라는 장기 통념과 달리, 단기적으로는 <span class=\"text-rose-400 font-medium\">투자 병목과 전력비 상승</span>으로 인플레이션을 견인하는 요인이 되었습니다.",
        "성장 주도주(엔비디아 등)에 대한 거품 확신에 갇혀 헤징을 기피하는 고집(에고)은 기관 투자자에게도 회생 불가능한 손실을 초래할 수 있습니다."
      ],
      "data_points": [
        "점도표상 추가 인상 위원 수: 3월 0명에서 6월 9명으로 급증 (인하 지지 위원은 12명에서 1명으로 급감)",
        "폴랜 캐피털의 자산 변화: 830억 달러에서 330억 달러로 약 60% 급감 (NVIDIA 회피 및 구식 SaaS 투자 집중 탓)",
        "12월 기준 금리 인상(0.25~0.5%p 인상) 확률 배팅: 선물 시장 합산 70% 돌파"
      ],
      "signal": "bearish",
      "signal_reason": "연준의 통화 기조가 점도표 반전과 소비 서프라이즈로 인해 확실한 매파적 긴축 장기화로 돌아서며, AI 지출이 물가를 압박하는 피드백 루프를 형성해 단기 시장 조정 요인으로 작용합니다.",
      "key_companies": ["NVIDIA", "스페이스X", "어도비", "세일즈포스"],
      "insight": "AI 붐은 실물 경제 수요를 적극적으로 자극하는 금융 유동성 블랙홀이자 물리적 소비 가속기입니다. 단기 인플레이션 압력이 높은 고금리 상황 하에서 무형의 아이디어보다는 즉각적인 실적 숫자를 보여주는 대장주 편입이 생존의 핵심입니다.",
      "action_point": "AI 거품론에 기초한 숏 포지션이나 극단적인 대형주 제외 전략을 폐지하고, HBM/낸드/전력/설계 등 실질적 하드웨어 실적이 확인되는 반도체 및 인프라 대장주를 포트폴리오의 중추로 유지해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["케빈워시", "FOMC결과", "점도표반전", "AI인플레이션", "엔비디아거품", "포트폴리오실패"]
    }
  },
  "NVrBe6ldKjc": {
    "primary": "economy",
    "video": {
      "id": "NVrBe6ldKjc",
      "title": "[Breaking News] June FOMC Review, Kevin Warsh’s Appearance! The Impact on Financial Markets",
      "published": "2026-06-18T06:21:00+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=NVrBe6ldKjc",
      "thumbnail": "https://img.youtube.com/vi/NVrBe6ldKjc/hqdefault.jpg"
    },
    "analysis": {
      "summary": "6월 FOMC 회의 결과와 신임 연준 의장 <span class=\"text-cyan-300 font-semibold\">케빈 워시</span>가 선보인 파격적인 연준 구조조정 행보를 해석합니다.\n워시는 기존 파월 의장이 장황하게 수식어를 붙여 작성했던 성명서를 빨간 펜으로 다 지워버리고 간결한 팩트만 남겨 시장과의 소통 노이즈를 최소화했습니다.\n자신은 점도표 작성을 거부하여 점도표의 권위를 강제로 훼손하는 한편, 설문에만 의존하던 기존 구식 데이터를 폐기하고 빅테크의 실시간 트래픽 등을 활용하기 위한 5개의 <span class=\"text-cyan-300 font-semibold\">연준 개혁 테스크포스(TF)</span> 설치를 선언해 자신의 정책적 통제권을 극대화하려 합니다.",
      "key_claims": [
        "케빈 워시는 점도표의 예측 무용론을 입증하기 위해 의도적으로 점 제출을 생략하며 점도표를 참고하지 말라는 시그널을 주었습니다.",
        "파월의 구식 관행적 커뮤니케이션을 폐지하고 시장의 자의적 해석을 차단하는 극단적인 <span class=\"text-rose-400 font-medium\">정보 비대칭 통제</span>를 시작했습니다.",
        "데이터 출처, 생산성 평가, 대차대조표 축소, 인플레 프레임워크를 다루는 TF는 연준의 의사 결정 방식을 워시의 지론(생산성 우선)대로 정립하는 수단입니다."
      ],
      "data_points": [
        "6월 연준 성명서 글자 수: 기존 340여 단어에서 핵심 132단어로 대폭 칼질",
        "미국 국채 2년물 금리: 연준 긴축 기조 확인 후 당일 14bp 급등해 4.2% 터치",
        "변동성 지수(VIX): 발표 직후 12% 급등하며 18.4 기록"
      ],
      "signal": "neutral",
      "signal_reason": "워시의 파격적인 연준 개혁과 모호성은 시장 금리를 자극하고 불확실성을 키워 단기 변동성을 연출하지만, 데이터 수집 고도화를 통한 합리적 의사결정 체계 구축은 중장기적으로 중립 이상의 긍정 효과를 가집니다.",
      "key_companies": [],
      "insight": "워시는 시장을 안심시키기 위해 겉으로는 '물가 2% 안착'을 단호하게 외쳐 매파적인 면모를 내세웠으나, 이면에서는 AI 생산성 데이터를 구축해 금리를 빠르게 인하할 논리적 근거(TF)를 세팅 중인 양면성을 가집니다.",
      "action_point": "단기적인 성명서 문구 삭제나 금리 10~15bp 변동에 따른 노이즈에 과민반응해 손절하기보다, 워시가 주도하는 연준의 실시간 데이터 지향 정책이 가시화될 때까지 우량 포트폴리오를 유지하는 것이 바람직합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["케빈워시", "FOMC리뷰", "점도표거부", "연준개혁TF", "구조조정", "매파적데뷔"]
    }
  },
  "opM7ALpy1EI": {
    "primary": "economy",
    "video": {
      "id": "opM7ALpy1EI",
      "title": "Kevin Warsh's Intense Debut | Daily Live | 06/18/2026 (Thu)",
      "published": "2026-06-18T06:20:00+00:00",
      "channel_name": "Smart Money by MiraeAsset",
      "url": "https://www.youtube.com/watch?v=opM7ALpy1EI",
      "thumbnail": "https://img.youtube.com/vi/opM7ALpy1EI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "6월 18일 글로벌 시장의 긴박한 매크로 지표 변화와 주요 테크 기업들의 개별 악재/호재를 정리한 데일리 라이브입니다. 연준의 6월 PCE 물가 전망 상향(3.6%)과 매파적 동결로 뉴욕 증시는 일제히 하락 마감하며 위험자산 회피 성향이 짙어졌습니다.\n글로벌 전력망 측면에서는 독일의 풍력 발전 급감으로 도매 전기 요금이 메가와트시당 400유로를 넘어서며 <span class=\"text-rose-400 font-medium\">에너지 공급 불안</span>이 극대화되었고, 유가는 미-이란 종전 합의 기대로 WTI 기준 75달러 이하로 미끄러졌습니다.\n테크 기업 중에서는 모더나가 독감 백신 승인 기대(11.5% 급등), GE 버노바가 전력 안보 수혜(6.77% 급등)로 웃은 반면, 마이크로소프트는 코파일럿 집단 소송 리스크(3.79% 하락), 메타는 AI 총괄책임자 돌연 사임 및 내분(5.44% 하락)으로 <span class=\"text-rose-400 font-medium\">성장 경계감</span>을 노출했습니다.",
      "key_claims": [
        "연준의 고금리 장기화 우려로 글로벌 헤지 펀드들은 달러 강세(롱) 배팅을 2018년 이후 최대 폭으로 확대 중입니다.",
        "친환경 에너지원의 간헐성 리스크가 실체화되면서 백업 발전 설비 및 종합 전력 솔루션을 갖춘 <span class=\"text-cyan-300 font-semibold\">종합 전력 인프라</span> 기업의 가치가 부각되고 있습니다.",
        "빅테크의 AI 서비스(코파일럿 등) 수익화 과정에서 소송 및 조직 갈등과 같은 <span class=\"text-rose-400 font-medium\">내부 마찰 비용</span>이 주가 변동성을 자극하기 시작했습니다."
      ],
      "data_points": [
        "독일 전기 요금: 풍력 발전 부진으로 1년 만에 최고치인 MWh당 400유로 돌파",
        "GE 버노바: 번스타인이 목표 주가를 상향하여 당일 6.77% 급등 마감",
        "달러 강세 배팅 규모: 2018년 이후 일주일 기준 최대 폭 순유입 기록"
      ],
      "signal": "bearish",
      "signal_reason": "고금리 고착화에 더해 유럽 전력 가격 폭등, 빅테크의 사법 소송 및 핵심 AI 임원 사임 등 다발성 악재가 겹치며 기술주 중심의 차익 실현 욕구를 강하게 자극하고 있습니다.",
      "key_companies": ["Moderna", "GE Vernova", "Microsoft", "Meta"],
      "insight": "금리 압박 환경 하에서 빅테크 내부의 AI 부서 내분이나 소송 리스크는 높은 멀티플을 정당화하던 시장의 확신을 흔들 수 있습니다. 반면 전력 인프라(GE 버노바 등)처럼 실제 하드웨어 수요가 꽂히는 안보 섹터는 차별화된 흐름을 보입니다.",
      "action_point": "AI 소프트웨어 및 빅테크 개별 리스크(MS, 메타) 노출을 다소 낮추고, 독일 전력난 등 글로벌 전력 쇼티지의 직접 수혜를 입는 송배전/발전 인프라 대장주의 비중을 높여 변동성에 대비해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "energy"],
      "tags": ["케빈워시", "FMC충격", "독일전력폭등", "유가하락", "모더나백신", "지주사리스크"]
    }
  },
  "T7Xj50ikni8": {
    "primary": "etc",
    "video": {
      "id": "T7Xj50ikni8",
      "title": "젠슨 황 ”한국 남자들은 다르다“",
      "published": "2026-06-18T06:19:00+09:00",
      "channel_name": "Softdragon SOD",
      "url": "https://www.youtube.com/watch?v=T7Xj50ikni8",
      "thumbnail": "https://img.youtube.com/vi/T7Xj50ikni8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "젠슨 황 엔비디아 CEO가 글로벌 미디어 간담회나 공식 석상에서 한국인들의 매너와 문화를 언급한 짤막한 에피소드를 다룹니다.\n그는 대화 과정에서 '한국 남자들, 한국 소년들은 매우 예의가 바르다'라며, 다른 나라의 관례와 비교해 상대방을 존중하는 한국 특유의 예의와 태도를 호평한 발언을 담고 있습니다.",
      "key_claims": [
        "글로벌 IT 업계의 핵심 리더인 젠슨 황의 대중 소통 스탠스와 한국 시장 및 한국 파트너들에 대한 긍정적인 브랜드 호감도가 친근하게 표현되었습니다."
      ],
      "data_points": [
        "젠슨 황의 구두 발언 인용"
      ],
      "signal": "neutral",
      "signal_reason": "비즈니스적 펀더멘탈이나 시장 수급에 미치는 영향이 없는 대중 친화적인 가벼운 에피소드물이므로 중립적입니다.",
      "key_companies": ["엔비디아"],
      "insight": "젠슨 황의 친근한 소통 방식과 한국 시장에 대한 지속적인 관심 표현은 엔비디아와 국내 반도체 파트너(SK하이닉스, 삼성전자) 간의 심리적 결속 및 긍정적 유대 형성에 미소한 도움이 될 수 있습니다.",
      "action_point": "가벼운 화제성 콘텐츠이므로, 투자 관점의 직접 액션보다는 엔비디아 경영진의 우호적인 한국 브랜드 이미지를 참고하는 정도로 활용합니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["tech"],
      "tags": ["젠슨황", "엔비디아", "엔비디아CEO", "글로벌소통", "매너문화", "대중소통"]
    }
  },
  "YL9tGdB9UvE": {
    "primary": "etc",
    "video": {
      "id": "YL9tGdB9UvE",
      "title": "한국 뛰어든 60조 캐나다 잠수함 수주전, 트럼프 손에 달렸다 (COR에너지인사이트 권효재 대표)",
      "published": "2026-06-18T06:18:00+09:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=YL9tGdB9UvE",
      "thumbnail": "https://img.youtube.com/vi/YL9tGdB9UvE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "한국 조선사들이 최종 후보군에 진입한 60조 원 규모의 캐나다 순찰 잠수함 사업(CPSP)의 지정학적 배경과 변수를 분석합니다.\n캐나다는 기존 1980년대산 노후 잠수함의 수명 한계(2035년 퇴역 예정)와 더불어, 트럼프 2기 행정부가 캐나다를 '미국의 51번째 주'로 비유하며 북극해 안보 방어 능력이 없는 캐나다를 강하게 압박하는 등 <span class=\"text-violet-300 font-medium\">지정학적 안보 긴장</span>에 직면해 방산 예산을 급격히 확충하고 있습니다.\n총 12척을 도입하는 이번 수주전은 잠수함 건조 능력(30조 원) 외에 30년간의 군수 지원(30조 원)을 결합한 대형 프로젝트로, 독일/일본과의 경쟁 속에서 한국 조선사(한화오션, HD현대중공업)의 수주 여부는 <span class=\"text-violet-300 font-medium\">미국 행정부의 승인 및 지원</span>이 결정적인 키를 쥐고 있습니다.",
      "key_claims": [
        "미국의 대 캐나다 방위비 증액 및 통상 압박이 캐나다 해군의 잠수함 도입 규모를 12척으로 급격히 늘린 핵심 트리거입니다.",
        "한국은 우수한 건조 단가와 납기 준수(인도네시아 수출 이력 등)로 강점을 지녔으나, 북극해 작전 요건과 미국 해군과의 호환성이 최종 낙점의 핵심 변수입니다.",
        "60조 원 규모의 초대형 프로젝트 수주 시 국내 방산 및 조선 생태계에 30년 이상의 장기적인 고마진 먹거리를 제공하게 됩니다."
      ],
      "data_points": [
        "캐나다 순찰 잠수함 사업(CPSP) 총 규모: 약 60조 원 (건조 30조 + 30년 생애주기 유지보수 30조)",
        "도입 척수: 12척 (기존 1980년대 중고 도입 잠수함 4척은 2035년 전량 도태 예정)"
      ],
      "signal": "neutral",
      "signal_reason": "방산 수주전의 최종 결과 발표까지는 수많은 외교/정치적 조율이 필요하여 즉각적인 실적 반영 여부는 불투명하나, 한국 조선업계의 기술적 위상 상승과 장기적 모멘텀은 긍정적입니다.",
      "key_companies": ["한화오션", "HD현대중공업"],
      "insight": "캐나다 방산 사업은 단순 상업 거래가 아니라 미국 주도의 나토 북극해 방어망 재편이라는 군사 정치의 연장선입니다. 트럼프의 압박 스탠스가 캐나다의 방산 CapEx를 강제로 열어젖힌 셈입니다.",
      "action_point": "단기 수주 기대감에 따른 급등 시 뇌동매매를 삼가고, 미국 해군과의 기술 호환성 및 수주전 숏리스트 결과 추이를 보며 대표 방산/조선주(한화오션, HD현대중공업)의 비중을 포트폴리오 성격에 맞게 분할 관리하는 것이 현명합니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy", "stock"],
      "tags": ["캐나다잠수함", "방산수주", "트럼프변수", "한화오션", "HD현대중공업", "지정학적위협"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["video"], info["analysis"], info["classification"])

print("ALL 17 ANALYSES SUCCESSFULLY WRITTEN AND PENDING FILES DELETED!")
