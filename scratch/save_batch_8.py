import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

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
  "1y11tj_8LCw": {
    "primary": "tech",
    "video": {
      "id": "1y11tj_8LCw",
      "title": "전세계 기자들을 감동시킨 젠슨 황의 한마디",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "Softdragon SOD",
      "url": "https://www.youtube.com/watch?v=1y11tj_8LCw",
      "thumbnail": "https://img.youtube.com/vi/1y11tj_8LCw/hqdefault.jpg"
    },
    "analysis": {
      "summary": "젠슨 황 엔비디아 CEO가 기자들과의 대화에서 보여준 기업 가치관과 기술적 비전을 통해 AI 산업의 장기적인 리더십과 긍정적인 미래 전망을 제시합니다.",
      "key_claims": [
        "엔비디아의 기술 혁신은 단순한 하드웨어 공급을 넘어 전 세계 AI 기술 발전을 선도하고 있다.",
        "글로벌 기자단과의 소통을 통해 엔비디아의 인간 중심적 리더십과 파트너십 가치를 강조했다."
      ],
      "data_points": [
        "젠슨 황의 기조연설 및 기자 간담회 주요 발언 요약"
      ],
      "signal": "bullish",
      "signal_reason": "AI 하드웨어 독점력에 더해 글로벌 파트너 및 대중과의 강력한 신뢰 형성이 엔비디아의 브랜드 가치를 지속 지지합니다.",
      "key_companies": ["엔비디아"],
      "insight": "단순한 칩 제조사를 넘어 글로벌 IT 에코시스템의 핵심 리더로서 엔비디아의 비전이 공고해지고 있습니다.",
      "action_point": "엔비디아 중심의 독점적 AI 인프라 생태계 리더십을 신뢰하고 장기적인 투자 포지션을 유지해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["젠슨황", "엔비디아", "AI인프라", "테크비전", "글로벌리더십"]
    }
  },
  "_VtNplJ2AVg": {
    "primary": "stock",
    "video": {
      "id": "_VtNplJ2AVg",
      "title": "“삼성전자 PER이 말이 안 되는 이유” | 이학주 하나증권 원주지점 차장 [더블 크루]",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=_VtNplJ2AVg",
      "thumbnail": "https://img.youtube.com/vi/_VtNplJ2AVg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "글로벌 파운드리 및 메모리 시장에서 독보적인 경쟁력을 지닌 삼성전자가 해외 피어 그룹(TSMC 등) 대비 지나치게 낮은 주가수익비율(PER)에 거래되고 있음을 분석합니다.",
      "key_claims": [
        "삼성전자의 현재 PER(6~8배)은 TSMC(24배) 등 글로벌 반도체 기업들과 비교했을 때 극단적인 저평가 상태이다.",
        "HBM 납품 본격화 및 주주 친화 정책(밸류업)에 힘입어 밸류에이션 리레이팅이 나타날 시점이다."
      ],
      "data_points": [
        "삼성전자 현재 주가수익비율(PER) 수준: 6~8배 범위 내외",
        "글로벌 1위 파운드리 기업 TSMC PER 수준: 약 24배"
      ],
      "signal": "bullish",
      "signal_reason": "압도적인 저평가 상태에서 HBM3e/HBM4 테스트 진척 및 일반 서버 D램 가격 상승세가 겹쳐 밸류에이션 정상화 압력이 강해지고 있습니다.",
      "key_companies": ["삼성전자", "TSMC"],
      "insight": "메모리 반도체는 이제 단순한 범용 사이클 부품이 아니라 인프라 자산으로 격상되어야 하며, 이에 상응하는 밸류에이션 멀티플 부여가 정당합니다.",
      "action_point": "지나친 저평가 영역에 머물러 있는 삼성전자의 비중을 적극 확대하여 밸류에이션 갭 메우기 랠리에 대비해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["삼성전자", "저평가", "반도체밸류에이션", "PER비교", "TSMC", "삼프로TV"]
    }
  },
  "aFRZcx0c8Qo": {
    "primary": "stock",
    "video": {
      "id": "aFRZcx0c8Qo",
      "title": "아직도 떨어질 때마다 의심되나요? TSMC 보시면 됩니다  | 이학주 하나증권 원주지점 차장 [더블 크루]",
      "published": "2026-06-04T02:30:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=aFRZcx0c8Qo",
      "thumbnail": "https://img.youtube.com/vi/aFRZcx0c8Qo/hqdefault.jpg"
    },
    "analysis": {
      "summary": "안정적인 장기 계약과 높은 마진, 강력한 주주환원(배당)을 무기로 24배의 PER을 받는 TSMC처럼, 국내 메모리 대기업들도 장기 공급 체인 구축과 밸류업 수혜로 리레이팅을 받을 가능성이 높습니다. 한편, 최근 20% 조정을 겪은 전력 기기 대장주(효성중공업, LS일렉트릭 등)는 견조한 미국 생산자물가지수(PPI) 상승세를 통해 실적이 확인되므로 매수 기회로 평가됩니다.",
      "key_claims": [
        "TSMC는 파운드리 기반의 안정적 이익 구조와 고배당 프리미엄으로 높은 멀티플을 정당화하고 있다.",
        "삼성전자와 SK하이닉스도 과거와 달리 장기 계약 비중을 높이고 있어 밸류에이션 갭이 축소될 것이다.",
        "전력 기기 및 변압기 섹터의 단기 20% 조정은 주도주 사이클의 일시적 숨고르기이며, 미국 변압기 가격 지수(PPI)의 지속적 강세로 고마진이 보장된다."
      ],
      "data_points": [
        "TSMC 평균 PER: 약 24배",
        "삼성전자/SK하이닉스 PER: 6~8배 수준",
        "미국 변압기 PPI(생산자물가지수): 4월 기준 449 달성 (2021년 대비 폭발적 상승 및 높은 유지)"
      ],
      "signal": "bullish",
      "signal_reason": "전력 기기 섹터의 가격(PPI) 및 주문량이 탄탄하게 유지되는 상태에서, 반도체 대형주와 전력 기기 주도주들의 동반 리레이팅 모멘텀이 유지되고 있습니다.",
      "key_companies": ["TSMC", "삼성전자", "SK하이닉스", "효성중공업", "LS일렉트릭"],
      "insight": "변압기 가격의 안정적 우상향과 타이트한 수급(리드타임 장기화)은 원가 부담을 전가하고 높은 마진을 유지할 수 있게 해주는 구조적 성장 동력입니다. 주도 섹터의 20% 내외 조정은 역사적인 매수 기회였습니다.",
      "action_point": "단기 조정에 흔들리지 말고 전력 기기 대장주(효성중공업 등)를 저가 매수하고, 저평가 매력이 극대화된 국내 반도체 대표주의 홀딩 전략을 유지해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "energy"],
      "tags": ["TSMC", "반도체저평가", "변압기PPI", "전력기기조정", "효성중공업", "LS일렉트릭", "삼프로TV"]
    }
  },
  "bB4fAmsrdo0": {
    "primary": "crypto",
    "video": {
      "id": "bB4fAmsrdo0",
      "title": "세일러의 매도, ETF 유출까지…. 비트코인 역대급 대폭락과 마지막 희망은 '이것' | 서동주, 김동환, 김제이 블록미디어 편집장 [크립토 PLUS]",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=bB4fAmsrdo0",
      "thumbnail": "https://img.youtube.com/vi/bB4fAmsrdo0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "비트코인이 7만 달러 선을 내주고 6만 1천 달러 선까지 후퇴한 배경으로 현물 ETF 자금 유출 지속, 마이크로스트레티지(MSTR)의 매도세, 그리고 실적이 확실한 AI 주식으로의 글로벌 유동성 이탈(유동성 블랙홀 현상)이 지목되고 있습니다. 6만 달러의 기술적 저항선 사수가 시장의 단기 향방을 가를 주요 지지선이 될 전망입니다.",
      "key_claims": [
        "비트코인은 6월 들어 나스닥과 디커플링을 시작하며 약 10~15% 수준의 단기 급락세를 나타냈다.",
        "현물 ETF 순유입이 멈추고 자금이 이탈하는 동시에 글로벌 유동성이 엔비디아 등 고수익 AI 인프라주로 빨려 들어가고 있다.",
        "미-이란 중동 지정학적 충돌 우려에 따른 안전자산 회피 성향과 선물 옵션 청산 연쇄 반응이 하락을 증폭시켰다."
      ],
      "data_points": [
        "비트코인 최근 가격대: 61,000달러 수준으로 급락 (이전 저항선 70,000달러 이탈)",
        "최근 1주일간 비트코인 하락률: 약 10~15% 수준",
        "핵심 심리 지지선: 60,000달러"
      ],
      "signal": "bearish",
      "signal_reason": "현물 ETF 유입 모멘텀 상실, AI 기술주로의 자금 쏠림으로 인한 상대적 유동성 소외, 그리고 레버리지 선물 청산 체인이 하방 압력을 계속 자극하고 있습니다.",
      "key_companies": ["마이크로스트레티지", "엔비디아"],
      "insight": "과거의 위험선호 랠리와 달리 현재는 실적이 즉시 증명되는 AI 하드웨어 가속기 및 인프라 공급망으로만 자금이 쏠리는 '승자 독식' 구도입니다. 크립토의 투기 수급은 단기적으로 소외될 수밖에 없습니다.",
      "action_point": "6만 달러 지지선 붕괴 여부를 확인하기 전까지 고레버리지 마진 롱 포지션을 피하고, 현물 위주로 분할 대응하며 시장 안정화를 관망해야 합니다."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": ["economy"],
      "tags": ["비트코인폭락", "ETF자금유출", "유동성이동", "AI솔림", "마이크로스트레티지", "지정학적불안", "삼프로TV"]
    }
  },
  "ET8JB6VoT6w": {
    "primary": "tech",
    "video": {
      "id": "ET8JB6VoT6w",
      "title": "“반도체 아직 끝난 거 아닙니다… 진짜는 지금부터” | 김록호 하나증권 리서치센터 팀장 [더블 업]",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=ET8JB6VoT6w",
      "thumbnail": "https://img.youtube.com/vi/ET8JB6VoT6w/hqdefault.jpg"
    },
    "analysis": {
      "summary": "대만 컴퓨텍스 및 대형 테크 로드맵 확인을 바탕으로 반도체 AI 인프라 수요와 핵심 소부장(소재·부품·장비) 밸류체인의 이익 사이클이 여전히 성장 초입에 있음을 강변합니다.",
      "key_claims": [
        "AI 가속기(GPU/NPU) 수요 폭증에 따른 HBM 및 일반 서버향 D램 숏티지가 하반기에도 해소되지 않는다.",
        "반도체 사이클 우려에 따른 주가 흔들림은 일시적이며 실적 상향 조정이 주가 복원을 이끌 것이다."
      ],
      "data_points": [
        "글로벌 AI 서버 및 기업향 메모리 수요 증가율 지속 우상향"
      ],
      "signal": "bullish",
      "signal_reason": "실질적 주문 확대와 업황 가격 상승세가 든든하게 받쳐주고 있어 반도체 하드웨어 상승 동력은 유효합니다.",
      "key_companies": ["SK하이닉스", "삼성전자"],
      "insight": "반도체는 이제 경기 사이클 소비재가 아니라 디지털 혁명을 뒷받침하는 기간 인프라 자산으로 패러다임이 이동했습니다.",
      "action_point": "일시적인 매물 출회에 따른 주가 조정을 반도체 핵심 장비 및 부품주의 추가 비중 확대 기회로 삼아야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["반도체사이클", "소부장", "실적우상향", "HBM수요", "하나증권", "삼프로TV"]
    }
  },
  "G7_bg5hIg8c": {
    "primary": "stock",
    "video": {
      "id": "G7_bg5hIg8c",
      "title": "[26.06.04 오전 방송 전체보기] 중동 긴장 재고조 속 뉴욕증시 하락 마감...브로드컴 실적 발표",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=G7_bg5hIg8c",
      "thumbnail": "https://img.youtube.com/vi/G7_bg5hIg8c/hqdefault.jpg"
    },
    "analysis": {
      "summary": "중동 지정학적 충돌 우려(이란의 드론/미사일 타격으로 인한 호르무즈 긴장) 및 고금리 우려 재부각으로 미 증시는 5일 연속 사상 최고치 행진을 멈추고 하락 마감했습니다. 옵션 만기일 전후의 매물 출회가 일어나는 한편, 주도주인 브로드컴과 크라우드 스트라이크의 장후 실적 경계가 시장의 관망세를 이끌었습니다.",
      "key_claims": [
        "미국 지수는 고용 지표(ADP/JOLTS) 강세에 의한 고금리 우려와 중동 긴장 재확산으로 동반 하락했다.",
        "미 증시는 그간 9주 이상 지속 상승한 것에 따른 기술적 피로가 누적되어 단기 숨고르기가 필요한 시점이었다.",
        "주도주였던 브로드컴과 보안 대장주 크라우드 스트라이크의 실적 발표를 앞두고 차익 실현과 헤지성 매물이 증가했다."
      ],
      "data_points": [
        "미국 주요 지수 하락률: 다우 -1.2%, 나스닥 -0.9%, S&P 500 -0.7%",
        "원달러 환율: 야간 거래 중 1,530원선 돌파 시도 지속"
      ],
      "signal": "bearish",
      "signal_reason": "환율 급등, 중동 지정학적 마찰 격화, 고금리 긴장 누적이 안전자산 선호 심리를 자극하며 글로벌 증시 전반에 리스크 오프를 유도하고 있습니다.",
      "key_companies": ["브로드컴", "크라우드스트라이크", "NVIDIA"],
      "insight": "미 증시의 9주 연속 상승은 이격도가 심하게 벌어진 과열 상태를 만들었습니다. 중동의 군사 충돌과 환율 불확실성은 차익 매물 출회에 정당성을 부여하는 촉매제로 작용하고 있습니다.",
      "action_point": "빅테크 및 고밸류에이션 성장주의 비중을 소폭 덜어내어 현금을 확보하고, 방어적 가치주 및 달러 자산 기반의 헤지 포지션을 구축하는 것이 유리합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["뉴욕증시하락", "중동지정학", "환율불안", "브로드컴실적대기", "차익실현", "삼프로TV"]
    }
  },
  "gxt3mYJ-Apk": {
    "primary": "economy",
    "video": {
      "id": "gxt3mYJ-Apk",
      "title": "미, 60개국에 '강제노동 관세' 예고…한국은 12.5% | 젠슨 황 방한, 나흘 간 광폭 행보 | 권순우 삼프로TV 취재팀장 [뉴스3]",
      "published": "2026-06-04T00:05:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=gxt3mYJ-Apk",
      "thumbnail": "https://img.youtube.com/vi/gxt3mYJ-Apk/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 USTR(무역대표부)이 강제노동 연루 수입 거래 규제를 이행하지 않은 60개 국가에 10% 또는 12.5%의 강력한 보복 관세를 예고하며 보호무역 장벽을 공고히 했습니다. 한국은 12.5% 추가 관세 대상군에 포함되었습니다. 또한 젠슨 황의 방한 일정에 따른 국내 기업들의 AI 파트너십 구축 행보가 초미의 관심사로 떠올랐습니다.",
      "key_claims": [
        "미국은 강제노동 수입 제재 규정을 적극 수용하지 않거나 이행이 부진한 한국, 일본, 중국, 인도 등 60개 경제권에 최대 12.5%의 추가 관세를 검토 중이다.",
        "이는 기존의 임시 관세 성격을 띤 무역법 122조를 넘어서는 상시적인 자국 산업 보호 및 대외 공급망 통제 조치이다.",
        "젠슨 황 엔비디아 CEO의 나흘간 방한 및 대외 행보로 국내 대기업(삼성, LG, 두산 등)과의 실질적인 물리적 AI 및 패키징 파트너십 논의가 구체화될 것이다."
      ],
      "data_points": [
        "미국 무역대표부(USTR) 제시 보복 관세율: 10% (1그룹), 12.5% (2그룹 - 한국 포함)",
        "추가 관세 영향권 경제권 수: 총 60개 대상국"
      ],
      "signal": "bearish",
      "signal_reason": "미국의 '강제노동' 명분의 추가 보복 관세 조치는 국내 대미 수출 기업들의 원가 매력을 약화시키고, 글로벌 공급망 블록화를 가속화하는 보호무역주의 악재입니다.",
      "key_companies": ["삼성전자", "LG전자", "두산"],
      "insight": "미국의 관세 부과는 명분(강제노동)과 무관하게 재정 적자 축소와 자국 내 생산 유치를 위한 정치적 무기화 과정입니다. 수출 비중이 큰 한국 제조업 전반에 새로운 비용 장벽으로 작용할 가능성이 큽니다.",
      "action_point": "미국의 통상 제재 장벽을 회피할 수 있는 현지 생산 거점을 구축한 완성형 기업이나 대미 관세 노출도가 낮은 내수 독점적 기업 지분으로 자산을 분산해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["tech", "stock"],
      "tags": ["보복관세", "USTR", "강제노동제재", "보호무역주의", "젠슨황방한", "공급망블록화", "삼프로TV"]
    }
  },
  "JJbVYMbqBcg": {
    "primary": "etc",
    "video": {
      "id": "JJbVYMbqBcg",
      "title": "우리는 왜 배부른데도 계속 먹게 될까?",
      "published": "2026-06-04T02:00:00+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=JJbVYMbqBcg",
      "thumbnail": "https://img.youtube.com/vi/JJbVYMbqBcg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "포만감을 전달하는 장 분비 호르몬 GLP-1의 작용 기전과 비만 환자에게서 호르몬 분비가 저하되는 기전을 과학적으로 설명하고, 비만 치료제(위고비 등)의 약리학적 대안 가능성을 다룹니다.",
      "key_claims": [
        "GLP-1은 인슐린 분비를 촉진하고 뇌에 포만감 신호를 전달하여 과식을 막는 핵심 호르몬이다.",
        "가공식품과 비만은 호르몬 민감성을 저하시켜 포만 브레이크를 밀리게 하는 악순환을 형성한다."
      ],
      "data_points": [
        "위고비 등 비만 치료제 약리학적 타겟: GLP-1 유사체 수용체 작용제"
      ],
      "signal": "neutral",
      "signal_reason": "대중적 의학 지식 전달 콘텐츠로, 관련 신약 시장의 성장 가치와 현대 사회의 헬스케어 동향을 이해하는 기초 배경을 제공합니다.",
      "key_companies": ["노보노디스크"],
      "insight": "식욕 조절은 개인의 의지 문제가 아니라 생물학적 호르몬 및 현대 가공식품 유입에 따른 뇌 보상 체계의 결과이며, 이를 표적하는 GLP-1 치료제 생태계의 팽창 속도는 멈추지 않을 것입니다.",
      "action_point": "글로벌 비만 치료 및 헬스케어 생태계를 지배하는 독점 제약사 및 원료 공급 파트너망에 대한 장기 관점 투자를 검토해야 합니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["GLP-1", "포만감호르몬", "비만치료제", "위고비", "의학과학", "뇌보상체계", "안될과학"]
    }
  },
  "MMKadJnKziE": {
    "primary": "crypto",
    "video": {
      "id": "MMKadJnKziE",
      "title": "폭락한 비트코인, 하락장 끝낼 단 하나의 변수! 클래리티 법안 통과 시나리오 | 서동주, 김동환, 김준우 쟁글 대표 [크립토 PLUS]",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=MMKadJnKziE",
      "thumbnail": "https://img.youtube.com/vi/MMKadJnKziE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "벤처 캐피탈(VC) 자금이 과거 크립토 내부 순환 구조(L1/L2, 디파이 등)에서 이탈하여 AI 테마로 급격히 무빙하는 구조적 소외를 다룹니다. 거래소 내 기관급 매수 대기층 부재로 VC의 회수가 막히고 펀드 규모(a16z 등)가 반토막 난 상태에서, 스테이블코인 및 금융 인프라 제도를 정립할 '클래리티 법안' 통과가 하락세를 반전시킬 유일한 유동성 열쇠로 부각되고 있습니다.",
      "key_claims": [
        "크립토 벤처 캐피탈(VC) 자금 성격이 알트코인 내러티브 베팅에서 AI 및 실물 금융(RWA, 스테이블코인) 분야로 대거 이동했다.",
        "리테일에 전적으로 의존하는 회수 시장의 한계로 인해 기관 벤처 투자사들의 엑시 병목이 발생하여 투자 규모가 현격히 위축되었다.",
        "미 의회에서 논의 중인 스테이블코인 명문화 법안(클래리티 법안)의 통과는 전통 기관 자금의 공식 유입 루트를 뚫어줄 핵심 이정표다."
      ],
      "data_points": [
        "a16z 크립토 5호 펀드 모집 규모: 이전 대비 50% 이하 수준으로 급감",
        "비트코인 6만 달러 초반 유지 및 대형 알트코인의 VC 투자 축소 지속"
      ],
      "signal": "bearish",
      "signal_reason": "전형적인 리테일 설거지 구조에 한계를 느낀 VC 자금의 AI 이탈과 스테이블코인을 통한 전통 금융 인프라 통합으로의 체질 개선 과도기로, 단순 투기 알트코인의 가치 붕괴 리스크가 큽니다.",
      "key_companies": ["앤드리슨호로위츠(a16z)", "서클"],
      "insight": "가상자산 시장이 내러티브 위주에서 철저한 제도권 금융 유동성(스테이블코인, RWA) 위주로 성격이 전환되고 있습니다. 클래리티 법안 통과와 같이 달러 금융망이 공식 온체인화되기 전까지는 단순 유틸리티 토큰의 가격 회복은 지연될 것입니다.",
      "action_point": "가치 수렴이 모호한 알트코인 비중을 대폭 줄이고, 미국 제도권 법안 통과로 인해 유동성 허브가 될 규제 준수형 스테이블코인 및 미국 채권 RWA 프로젝트 위주로 포트폴리오를 압축해야 합니다."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": ["economy"],
      "tags": ["비트코인하락", "VC투자축소", "엑시병목", "a16z", "클래리티법안", "스테이블코인", "RWA", "삼프로TV"]
    }
  },
  "mv-rVXNIiTo": {
    "primary": "economy",
    "video": {
      "id": "mv-rVXNIiTo",
      "title": "환율 1500원 시대? 코스피 올라도 원화는 안오르는 이유 | \"페트로달러 말고 DRAM달러\" | 빈난새의 빈틈없이월가",
      "published": "2026-06-04T00:10:00+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=mv-rVXNIiTo",
      "thumbnail": "https://img.youtube.com/vi/mv-rVXNIiTo/hqdefault.jpg"
    },
    "analysis": {
      "summary": "국내 반도체 대호황에도 불구하고 원달러 환율이 1,500원 돌파 위기에 직면한 구조적 원인들을 파헤칩니다. 아시아 수입국들의 중동 에너지 결제 부담 증가, 한미 금리 역전차로 인한 외국인 투자자의 2% 캐리 수익 헷지 쏠림, 그리고 반도체 대기업들이 수출 대금을 원화로 바꾸지 않고 해외 달러 자산으로 재투자하는 'DRAM 달러' 유출이 결합된 결과입니다.",
      "key_claims": [
        "외국인들은 한국 반도체 주식을 대거 매수하지만, 한미 금리 차이(+2%)와 미래 원화 하락을 헷징하기 위해 적극적으로 원화를 선물 환매도하는 FX 해지를 동반하고 있다.",
        "미-이란 중동 갈등 장기화로 아시아 통화 가치가 동반 급락하며 환율 방어 비용이 급증했다.",
        "반도체 수출 흑자로 벌어들인 달러가 국내 원화 환전 수요로 들어오지 않고 해외 지분 및 설비 자산에 머무는 'DRAM 달러' 현상이 원화 약세를 유발한다."
      ],
      "data_points": [
        "원달러 환율 수준: 1,500원 이상 돌파 시도",
        "한미 기준금리 차이: 약 2% 내외 (한국 저금리, 미국 고금리)",
        "외국인 한국 주식 매수 대비 선물환 매도(환헤지 비율) 신규 유입분 급증"
      ],
      "signal": "bearish",
      "signal_reason": "원달러 환율 1,500원대 안착은 고비용 수입 인플레이션을 구조화하고, 내수 기업들의 마진 스프레드를 축소시키는 거시 경제적 악재입니다.",
      "key_companies": ["삼성전자", "SK하이닉스"],
      "insight": "과거에는 '수출 호조 = 원화 강세' 공식이 통했으나, 지금은 금리 역전차 때문에 주식을 사면서도 통화 가치는 헷징하여 원화를 매도하는 금융 메커니즘이 강하게 고착화되었습니다. 벌어들인 달러마저 본국으로 송환되지 않는 DRAM 달러 현상은 원화의 장기적 신뢰도 저하를 보여줍니다.",
      "action_point": "환율 급등에 따른 원화 가치 하락에 대응하여, 원자재 가격 전가력이 뛰어나며 원화 부채 비중이 낮은 대형 반도체 대기업 및 외화 자산(미국 주식, 달러 예금)의 비중을 대폭 늘려야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["원달러환율1500원", "환헤지", "한미금리차", "DRAM달러", "자본유출", "지정학적불안", "한경글로벌마켓"]
    }
  },
  "NhV39Nh0beE": {
    "primary": "stock",
    "video": {
      "id": "NhV39Nh0beE",
      "title": "[속보효] SpaceX 상장 앞두고, 한국 주식 매도? 초보탈출 9일차",
      "published": "2026-06-04T01:00:00+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=NhV39Nh0beE",
      "thumbnail": "https://img.youtube.com/vi/NhV39Nh0beE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미 증시가 9일 연속 상승 피로감으로 조정을 겪는 가운데, 국내 시장은 젠슨 황의 구두 모멘텀으로 올랐던 피지컬 AI 및 IT 대형주(LG전자 등)에서 빠른 차익 매물이 나왔습니다. 반면 소외받던 코스닥 IT 소부장(소재·부품·장비) 중소형주가 가파르게 되돌림(순환매)을 보이는 과도기입니다. 아울러 스페이스X의 상장 가격 제시로 개인 투자자들이 자금 확보를 위해 국내 주식을 매도하는 루머가 시장 수급에 작용하고 있습니다.",
      "key_claims": [
        "S&P 500과 나스닥이 단기 9일 연속 급등을 멈추고 옵션 만기를 앞두고 건전한 이격도 조정을 겪었다.",
        "젠슨 황 방한 및 밸류업 기대로 급등했던 대형 가치주(LG그룹 등)에서 빠른 수익 실현 매물이 나와 주가 변동성이 커졌다.",
        "스페이스X의 주당 $135 고정 공모 정보가 노출되면서, 미국 상장에 선제 참여하려는 개인 투자자들의 국장 탈출(매도) 심리가 포착되었다."
      ],
      "data_points": [
        "S&P 500 지수: 연속 9일 랠리 마감 후 첫 조정",
        "코스닥 지수 상승률: 대형주 매도 물량 유입 속 소부장 반등으로 +3% 가깝게 급등",
        "LG전자 주가 등락: 젠슨 황 언급 이후 +15% 급등 후 차익 실현으로 급락세"
      ],
      "signal": "neutral",
      "signal_reason": "대형 주도주의 단기 이격 과열 해소 조정과 스페이스X 공모 참여를 위한 머니무브 변동성이 혼재하지만, 소외되었던 KOSDAQ 소부장의 견조한 반등이 하방을 지지하고 있습니다.",
      "key_companies": ["스페이스X", "LG전자", "주성엔지니어링"],
      "insight": "실적이 입증되지 않은 채 젠슨 황의 말 한마디로 급등한 주식들은 필연적으로 가혹한 차익 실현에 노출됩니다. 개인 투자자들의 스페이스X 상장 대기 심리는 단순한 해외 투자를 넘어, 전 세계에서 가장 희소한 우주 독점 플랫폼 자산을 국장보다 선호하는 현상을 대변합니다.",
      "action_point": "구두 루머에 휩쓸려 급등한 대형 모멘텀주를 추격 매수하기보다, 장기적인 밸류에이션 매력이 높고 실적 턴어라운드가 확인되는 코스닥 반도체 및 디스플레이 핵심 소부장 종목으로 포트폴리오 균형을 맞춰야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["space", "tech"],
      "tags": ["조정장세", "소부장반등", "차익실현", "스페이스X상장", "머니무브", "LG전자급락", "이효석"]
    }
  },
  "r_6JQvfZ9cI": {
    "primary": "stock",
    "video": {
      "id": "r_6JQvfZ9cI",
      "title": "올 것이 왔다, 순환매 장세 어떻게 돌파할까? | 장우진 작가 [더블 체크]",
      "published": "2026-06-04T03:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=r_6JQvfZ9cI",
      "thumbnail": "https://img.youtube.com/vi/r_6JQvfZ9cI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "AI 테마의 쏠림이 진정되는 가운데, 시장은 단기 급등했던 모멘텀주(LG전자, 현대차 등)에서 차익 매물이 나와 10일선 지지를 테스트하고 있습니다. 반면 전력 쇼티지 우려 장기화로 조선 대형주(삼성중공업의 Floating Data Center 수주)와 발전용 엔진 대형사(HD현대중공업, 하나엔진)의 마진 급증(30-40% 수준) 기대감이 새로운 순환매 주도주로 부각되고 있으며, 소외받던 KOSDAQ 소부장 및 이차전지(LG엔솔 등)의 동반 반등세가 시작되었습니다.",
      "key_claims": [
        "젠슨 황 테마로 단기 급등했던 LG전자, 네이버 등은 숨고르기에 들어갔으나 10일 이동평균선 지지 여부에 따라 상승 추세 유지가 결정된다.",
        "육상 전력 부족 대안으로 삼성중공업의 해상 부유식 데이터센터(FDC) 및 HD현대중공업의 데이터센터용 발전 엔진(선박용 대비 5~6배 단가 상승으로 마진 30-40% 달성)이 각광받고 있다.",
        "KOSDAQ 시장은 지나친 낙폭 과대 인식 속에 반도체 장비(원익IPS, 이오테크니스 등)와 바이오, 2차전지가 동반 상승하며 빠른 키 맞추기가 진행 중이다."
      ],
      "data_points": [
        "HD현대중공업 데이터센터 발전 엔진 영업이익률 전망: 기존 선박용(10% 대) 대비 30~40% 수준으로 폭증",
        "조선/엔진 대형주 주가 상승률: 삼성중공업 장대 양봉 형성 및 한국카본 보행제 수주 증가로 목표가 6만원 상향 리포트 출회"
      ],
      "signal": "neutral",
      "signal_reason": "기존 대형 주도주의 가격 조정 국면이나, 해상 데이터센터 및 발전용 엔진 등 AI 전력 부족의 본질을 해결하는 조선/에너지 밸류체인과 코스닥 소외주들로의 활발한 순환매가 자금의 하방 경직성을 지탱합니다.",
      "key_companies": ["삼성중공업", "HD현대중공업", "한국카본", "원익IPS", "LG전자"],
      "insight": "AI 데이터센터의 전력 부족은 육상 그리드를 넘어 해상 부유식 데이터센터(FDC) 및 선박용 발전 엔진의 개조 수주라는 초유의 공급 마찰을 낳고 있습니다. 이는 단순 반도체보다 전력 부족이라는 병목 해결을 쥐고 있는 인프라 기업들의 가격 결정력과 영업마진이 극대화되는 국면입니다.",
      "action_point": "단기 급등한 테크 성장주를 무리하게 매수하기보다는, AI 인프라의 실질적 병목인 전력을 해결하는 조선 발전 엔진 및 LNG 보행제(한국카본 등) 저평가 기자재 우량주, 그리고 코스닥 대표 소부장 반등주로 자산을 분산 배치해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "energy"],
      "tags": ["순환매장세", "부유식데이터센터", "발전용엔진", "HD현대중공업", "삼성중공업", "한국카본", "소부장반등", "삼프로TV"]
    }
  },
  "rCY9Ds37MVY": {
    "primary": "stock",
    "video": {
      "id": "rCY9Ds37MVY",
      "title": "Risk-on, but flexible! #2026년 6월 고객자산배분전략 #shorts",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "Smart Money by MiraeAsset",
      "url": "https://www.youtube.com/watch?v=rCY9Ds37MVY",
      "thumbnail": "https://img.youtube.com/vi/rCY9Ds37MVY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미래에셋증권의 2026년 6월 고객자산배분전략 요약 숏츠로, 위험 자산 선호(Risk-on) 기조를 유지하되 시장 변동성 확대에 대응해 유연하고 분산된 배분 전략을 조언합니다.",
      "key_claims": [
        "6월 글로벌 금융 시장은 여전히 위험자산 강세(Risk-on) 우위를 지지한다.",
        "매크로 노이즈 및 이격 과열을 감안해 특정 단일 종목 집중보다 유연한(flexible) 자산배분 대응이 필수적이다."
      ],
      "data_points": [
        "미래에셋 모델 포트폴리오의 주식 및 대체 자산 편입비 권고"
      ],
      "signal": "neutral",
      "signal_reason": "전반적인 자산배분 가이드로, 개별 기술 지표보다 변동성 관리에 주안점을 두고 있어 중립적 관점을 유지합니다.",
      "key_companies": ["미래에셋증권"],
      "insight": "강세장 후기 국면일수록 단기 변동성에 흔들리지 않는 포트폴리오 내 다변화가 안정적인 장기 누적 수익률을 보장합니다.",
      "action_point": "한 분야에 쏠린 투자 자산을 일부 회수하고 지수형 및 자산배분형 글로벌 펀드로 분산 배치하여 안정성을 확보해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["자산배분전략", "미래에셋", "Risk-on", "변동성헤징", "분산투자"]
    }
  },
  "tHmlNTkYjy8": {
    "primary": "stock",
    "video": {
      "id": "tHmlNTkYjy8",
      "title": "코스피 1만 간다? 진짜 변수는 환율 | 박병창 MP파트너스 대표 [마켓 인사이드]",
      "published": "2026-06-04T01:30:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=tHmlNTkYjy8",
      "thumbnail": "https://img.youtube.com/vi/tHmlNTkYjy8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "원달러 환율 급등세가 아시아 비(非)산유국들의 통화 가치 하락 및 금융 시장 불안(인도네시아 국가 신용등급 우려 등)으로 전개되고 있습니다. 코스피는 외국인의 8조 원 매도를 개인 퇴직연금/예금 기반의 210조 원 ETF 자금이 전격 방어하며 높은 하방 지지력을 증명했으나, 장중 극심한 변동성은 매수세의 점진적 fatigue와 차익 압력을 시사하므로 속도 조절 경계가 필요한 국면입니다.",
      "key_claims": [
        "한미 금리차와 오일 의존적 통화 동조화 현상으로 원달러 환율이 위기 수준으로 치솟아 아시아 약한 고리의 디폴트 리스크를 확산시키고 있다.",
        "어제 국내 증시는 장중 1분 30초 만에 2.5조 원대 매물이 출회되어 지수가 -3.2%까지 폭락했다가 다시 전액 보복 매수로 회복되는 극단적인 변동성을 보였다.",
        "올해 외국인이 130조 원을 매도했음에도 불구하고, 연금 머니무브 등에 기인한 개인의 210조 원 규모 ETF 유입이 시장의 강력한 지지 해자 역할을 하고 있다."
      ],
      "data_points": [
        "올해 개인의 연금/대기성 자금 기반 ETF 신규 유입 규모: 210조 원",
        "올해 누적 외국인 매도 매물 규모: 130조 원",
        "장중 알고리즘 연쇄 청산에 의한 폭락 하락폭: 1분 30초 만에 코스피 -3.25% 기록 후 삼성전자 반등으로 전액 회복"
      ],
      "signal": "neutral",
      "signal_reason": "연금 자산의 구조적 장기 유입이 지수 하방을 든든하게 받치고 있으나, 1,500원대 환율 돌파가 국내 수입 물가와 기업 수익성에 미칠 부정적 충격과 장중 흔들림 강도를 감안해 중립적으로 대응해야 합니다.",
      "key_companies": ["삼성전자", "삼성생명", "삼성물산"],
      "insight": "코스피의 든든한 버팀목은 외국인도, 기관도 아닌 퇴직연금의 적립식 ETF 머니무브입니다. 그러나 장중 1분 30초 만에 3%가 요동치는 알고리즘 기습 청산은 전체 시장 참여자들의 불안을 보여주며, 대외 부실 신호(아시아 통화 위기)가 확산되면 일시적 충격을 피하기 어렵습니다.",
      "action_point": "무리한 레버리지 활용 및 신용 투자를 금지하고, 대형 지수 ETF 분할 매수 기조는 유지하되, 환율 상승에 따른 헷지용 달러 표시 가치주(삼성전자 등 수출 대형주)에 초점을 맞춰야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["코스피전망", "환율변수", "아시아통화위기", "ETF수급", "장중변동성", "알고리즘매매", "박병창", "삼프로TV"]
    }
  },
  "w7YYytQTVJ4": {
    "primary": "tech",
    "video": {
      "id": "w7YYytQTVJ4",
      "title": "\"끝도없이 올린다\" 더 무서운 건, 다 근거가 있다는 것 | 김록호 하나증권 리서치센터 팀장 [더블 업]",
      "published": "2026-06-04T04:14:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=w7YYytQTVJ4",
      "thumbnail": "https://img.youtube.com/vi/w7YYytQTVJ4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "SK하이닉스가 샌디스크와의 협업을 통해 차세대 HBF(High Bandwidth Foundry / 차세대 적층 메모리 기술) 리더십 확보를 조용히 추진하는 가운데, 청주 M15X 증설 및 내년 용인 클러스터 오픈(250k~300k 캐파)을 통한 HBM 5개년 생산 능력 증가는 충분히 가시적입니다. 한편, 삼성전자는 HBM4 샘플 출하 등으로 하이닉스와의 갭을 좁히는 동시에, 최근 IT 수급 소외에 따른 밸류에이션 리바운드가 기대되고 있습니다.",
      "key_claims": [
        "SK하이닉스는 샌디스크와 협력하여 HBF(적층 메모리) 관련 기술 우위를 구축하고 있으며, 청주 M15X(40k 추가 투자 가속)와 용인 공장 라인업으로 웨이퍼 증설 로드맵을 신뢰성 있게 증명하고 있다.",
        "삼성전자는 HBM4 샘플 발송 등을 기점으로 경쟁 격차가 좁아지며, 파업 이슈와 ETF 수급 왜곡으로 인한 극단적 소외 상태에서 빠른 주가 메이크업이 기대된다.",
        "일반 서버 D램 및 스마트폰 모바일 LPDDR 등 범용 메모리 가격이 4월 일시 조정 후 최근 3주간 전고점까지 재상승하여 반도체 투톱의 2분기 어닝 서프라이즈 가시성이 높아졌다."
      ],
      "data_points": [
        "SK하이닉스 M15X 캐파: 총 80k 공간 중 40k 장비 투자 조기 집행 중",
        "SK하이닉스 용인 클러스터 생산 능력: 내년 2월 완공 시 총 250k~300k 웨이퍼 캐파 공간 확보",
        "서버/모바일 D램 현물가 추이: 4월 조정 후 최근 3주간 전고점 수준 회복"
      ],
      "signal": "bullish",
      "signal_reason": "일반 D램 서버 칩의 타이트한 단가 우상향과 HBM 공급망 라인업의 가시적 생산 증가가 동시 실현되고 있어, 반도체 대형주 및 장비 체인의 이익은 꺾이지 않고 우상향할 것입니다.",
      "key_companies": ["SK하이닉스", "삼성전자", "샌디스크"],
      "insight": "하이닉스의 5개년 HBM 케파 증설 계획은 이미 완공된 M15X 공장 활용과 내년 용인 클러스터 가동으로 실현 가능한 데이터입니다. 삼성전자 역시 HBM 격차 해소와 일반 D램 호조세의 수혜를 고루 입어, 수급 소외를 벗어나 시세 메이크업에 나설 것입니다.",
      "action_point": "반도체 공급 과잉 우려를 덜고, 증설 수주가 즉시 꽂히는 HBM 검사/세정 장비 제조 강소기업 및 극단적으로 저평가된 삼성전자의 비중을 고르게 확대해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["HBM증설로드맵", "M15X공장", "HBF기술", "일반디램가격반등", "삼성전자소외탈출", "김록호", "삼프로TV"]
    }
  },
  "xoNt28yIwjI": {
    "primary": "stock",
    "video": {
      "id": "xoNt28yIwjI",
      "title": "AI 투자, 반도체만 보면 늦는다? 지금 주목할 수혜주는…_26.06.04. | 박현지, 여도은, 허재무 [아침N투자]",
      "published": "2026-06-04T02:30:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=xoNt28yIwjI",
      "thumbnail": "https://img.youtube.com/vi/xoNt28yIwjI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "AI 테마 자본 흐름이 반도체 하드웨어 중심에서 사이버 보안, AI 소프트웨어 및 데이터센터 물리적 인프라로 확산되고 있습니다. 특히 스노우플레이크(Snowflake)의 실적 호조가 클라우드 붕괴(사스포칼립스) 우려를 씻어내며 소프트웨어 반등의 신호탄이 되었고, 단일 레버리지 ETF 활성화에 따른 수급 쏠림 속에서 안전한 섹터 ETF(사이버보안, 데이터센터 등)로의 자금 재배치가 확인됩니다.",
      "key_claims": [
        "스노우플레이크가 호실적을 거두고 AWS와의 5개년 대규모 AI 플랫폼 계약을 맺으며 AI 소프트웨어 및 SaaS의 차별화된 반등을 주도했다.",
        "젠슨 황 방한 영향으로 LG그룹 등 물리적 AI 파트너십 기대 기업들이 급등 후 일시 조정을 보이나, 수혜 확산세 자체는 뚜렷하다.",
        "레버리지 상품에 대한 지수 레벨 부담으로 리테일 자금이 개별주에서 반도체, 사이버보안, 소프트웨어 ETF 등의 패시브 자금으로 우회 이동하고 있다."
      ],
      "data_points": [
        "스노우플레이크-AWS(아마존) 클라우드 AI 계약 기간: 5년 대형 계약 체결",
        "반도체 단기 과열로 인해 사이버보안 및 미국 AI 소프트웨어 ETF 수익률 상위권 랭크"
      ],
      "signal": "bullish",
      "signal_reason": "반도체 칩에만 국한되던 AI 모멘텀이 실적이 찍히는 사스(SaaS), 보안 소프트웨어, 에너지 에너지원 연계 인프라까지 전방위로 분산되며 시장 하방을 견고히 넓히고 있습니다.",
      "key_companies": ["구글", "마벨", "스노우플레이크", "LG전자"],
      "insight": "그동안 클라우드 성장 둔화로 과도하게 매를 맞았던 SaaS 소프트웨어주들이 실질적인 AI 플랫폼 비즈니스 계약으로 성장을 증명하고 있습니다. 개별 종목의 단기 레버리지 거품이 빠지는 구간에서 실적이 입증되는 소프트웨어와 인프라 패시브 자금으로의 무빙은 매우 건전한 신호입니다.",
      "action_point": "반도체 일변도의 포트폴리오에서 탈피하여, 글로벌 데이터센터 수혜를 받는 전력 및 사이버 보안/AI 사스(SaaS) 대표 ETF를 매입해 분산 투자를 구축해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["AI소프트웨어", "사이버보안", "스노우플레이크", "레버리지수급", "젠슨황효과", "ETF자금동향", "삼프로TV"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["video"], info["analysis"], info["classification"])
print("ALL BATCH 8 VIDEOS SUCCESSFULLY SAVED!")
