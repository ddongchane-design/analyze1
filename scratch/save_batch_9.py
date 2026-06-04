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
  "14VTMbQ3roA": {
    "primary": "tech",
    "video": {
      "id": "14VTMbQ3roA",
      "title": "최태원 회장 소름돋는 인터뷰 ㄷㄷ",
      "published": "2026-06-05T00:00:00+00:00",
      "channel_name": "Softdragon SOD",
      "url": "https://www.youtube.com/watch?v=14VTMbQ3roA",
      "thumbnail": "https://img.youtube.com/vi/14VTMbQ3roA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "최태원 SK그룹 회장의 최근 외신/대외 인터뷰를 통해 본 HBM 및 AI 메모리 인프라 부문의 장기 증설 로드맵과 미래 경영 비전을 간략히 조명합니다.",
      "key_claims": [
        "SK하이닉스는 5개년 로드맵 하에 AI 가속기 웨이퍼 캐파를 공격적으로 증설할 준비가 완료되었다.",
        "글로벌 빅테크의 요청에 신속히 대응할 수 있는 생산 구조 구축을 최우선으로 둔다."
      ],
      "data_points": [
        "SK그룹의 향후 5개년 반도체 대규모 설비 투자 방침"
      ],
      "signal": "bullish",
      "signal_reason": "그룹 최고 의사 결정권자의 강력한 HBM 투자 지속 지지 의사는 반도체 벨류체인의 장기 성장 신뢰도를 높여줍니다.",
      "key_companies": ["SK하이닉스"],
      "insight": "경쟁사 대비 선제적인 투자 유연성과 로드맵 제시가 SK의 지배력을 지탱하고 있습니다.",
      "action_point": "SK하이닉스 중심의 HBM 장비 수주 벨류체인 핵심 우량주 비중을 유지해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["최태원", "SK하이닉스", "HBM증설", "AI인프라", "경영비전"]
    }
  },
  "1nsjC0_gTOA": {
    "primary": "tech",
    "video": {
      "id": "1nsjC0_gTOA",
      "title": "간담이 서늘해지는 회장님 돌발 질문 ㄷㄷ",
      "published": "2026-06-05T00:00:00+00:00",
      "channel_name": "Softdragon SOD",
      "url": "https://www.youtube.com/watch?v=1nsjC0_gTOA",
      "thumbnail": "https://img.youtube.com/vi/1nsjC0_gTOA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "최태원 회장의 경영 지침과 돌발 인터뷰 상황을 통해 본 조직적 유연성 및 대미 통상 정책 대처의 필요성을 다룹니다.",
      "key_claims": [
        "변화하는 글로벌 무역 마찰 속에서 반도체 공급망 리스크에 민첩하게 대처해야 한다.",
        "R&D 기술력 축적을 넘어 수급의 정치학을 이해하는 조직적 민첩성이 생존 요건이다."
      ],
      "data_points": [
        "SK그룹 반도체 수급 위기 대응 매뉴얼 및 전략 흐름"
      ],
      "signal": "neutral",
      "signal_reason": "대외 지정학 통상 리스크에 대응하려는 국내 기업의 의지를 단편적으로 보여줍니다.",
      "key_companies": ["SK하이닉스"],
      "insight": "기술 개발 이상으로 공급망 안보 및 미국의 무역 장벽(보복 관세 등)을 헷징하려는 지정학적 전략 수립이 중요합니다.",
      "action_point": "단기 경영 잡음보다 장기적인 대미 현지 생산 전략 및 수주 유효성을 관망해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["economy"],
      "tags": ["최태원", "공급망리스크", "의사결정", "대미무역", "SK그룹"]
    }
  },
  "8po_Mp0QPxs": {
    "primary": "stock",
    "video": {
      "id": "8po_Mp0QPxs",
      "title": "[김종학의 뉴욕, 지금-6월5일] 이란과 휴전 지속…트럼프 “하메네이 만날 수 있다” | 브로드컴, 마벨, TSMC, 크라우드스트라이크, 골드만삭스, 코인베이스, 블랙스톤, 메타",
      "published": "2026-06-05T00:00:00+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=8po_Mp0QPxs",
      "thumbnail": "https://img.youtube.com/vi/8po_Mp0QPxs/hqdefault.jpg"
    },
    "analysis": {
      "summary": "트럼프의 중동 합의 성공 발언 및 하메네이 회동 의사 타진 등 지정학적 종전 기대감이 이어지는 가운데, 뉴욕 증시는 브로드컴의 TPU 공급 다각화 발언으로 촉발된 하드웨어 기술적 매물 출회 및 옵션 만기 경계로 혼조를 보였습니다. 에드 야데니 등 월가 강세론자들의 단기 긴축 경계로 인한 6월 숨고르기 의견이 작용하고 있습니다.",
      "key_claims": [
        "트럼프는 대선 전 성과를 내기 위해 이란 지도자 하메네이와의 적극 회동 및 휴전 성사 노력을 피력하고 있다.",
        "미 증시는 브로드컴의 구글 멀티벤더 가이던스로 하드웨어 차익 매물이 나왔으나, 소외 소프트웨어(오라클, 구글)로 순환매가 전개되며 지수 급락을 방어했다.",
        "연준 독립성 논쟁과 국채 금리 4.49%대 횡보 속에서 6월 옵션 만기를 앞두고 기관들의 적극적 헷지 거래가 나타나고 있다."
      ],
      "data_points": [
        "WTI 유가: 배럴당 92.8달러 선으로 소폭 하락 안정화",
        "미국 국채 10년물 금리 수준: 4.49%대 부근 횡보"
      ],
      "signal": "neutral",
      "signal_reason": "하드웨어 피로감 해소 및 중동 합의 기대감이 공존하여 지수는 방향성을 즉시 정하기보다 6월 선물옵션 만기 전까지 기간 조정을 이어갈 전망입니다.",
      "key_companies": ["브로드컴", "마벨", "NVIDIA", "구글"],
      "insight": "시장의 변동성은 AI 펀더멘탈의 훼손이 아닌, 단기 이격 과열과 6월 매크로(FOMC) 경계감이 맞물려 나타나는 일시적 현상입니다. 하드웨어에서 소프트웨어로의 수급 이동이 시장의 하방을 넓히고 있습니다.",
      "action_point": "반도체 비중의 공격적 확대는 자제하되, 실적이 동반되는 인프라 소프트웨어 및 클라우드 서비스 기업들의 저가 매수 기회를 노려야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["중동휴전", "트럼프", "브로드컴하락", "순환매장세", "옵션만기", "야데니신중론", "한경글로벌마켓"]
    }
  },
  "_Z9FMacSwbE": {
    "primary": "stock",
    "video": {
      "id": "_Z9FMacSwbE",
      "title": "젠승 황 호재에도 급락한 LG그룹주-네이버...그렇다면 오히려 지금이 '역대급 매수 타이밍'?ㅣ이재규 SK증권 PB 차장 [집중 오늘의 주식]",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=_Z9FMacSwbE",
      "thumbnail": "https://img.youtube.com/vi/_Z9FMacSwbE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "젠슨 황의 방한 구두 랠리로 급등했던 LG전자, 네이버 등 테마주들이 가파른 차익 매물로 하락했으나, 코스피 지수의 대형 상승 추세는 깨지지 않았습니다. 한편 KOSDAQ은 거래대금이 전일 대비 79% 수준으로 완연히 실리지 않아 완전한 하락 추세 전환으로 보기는 어렵지만 반도체 소부장을 중심으로 한 단기 되돌림이 진행 중입니다.",
      "key_claims": [
        "코스피는 장기 상승 추세가 살아 있어 눌림 시 복구 탄력이 높으나, 코스닥은 거래 대금 부족으로 여전히 반도체 소부장 중심의 차별적 랠리만 허용한다.",
        "젠슨 황 방한 루머가 확산되면서 관련주의 희소성이 떨어지고 빠른 차익 실현이 나왔지만 5일/10일선 지지 시 추세 훼손으로 보기는 어렵다.",
        "외환 시장의 원달러 환율이 1,530원대를 상회하는 상태에서도 증시가 견조한 것은 AI 메가 내러티브가 다른 거시 리스크를 압도하기 때문이다."
      ],
      "data_points": [
        "코스닥 당일 거래대금 증가율: 전일 대비 약 79% 수준으로 저조",
        "미국 국채 10년물 저항선 상단: 4.55% (현재 4.49%로 하방 제어됨)"
      ],
      "signal": "bullish",
      "signal_reason": "대형 상승 트렌드 내의 이격 조정 국면으로, 5일 및 10일 이동평균선이 지탱되는 한 주도 섹터의 우상향은 여전히 신뢰할 수 있습니다.",
      "key_companies": ["LG전자", "NAVER", "삼성전자", "SK하이닉si"],
      "insight": "상승장 초입에서는 고점 매수를 두려워하기보다 추세가 살아있는 섹터의 눌림목 매수에 동참해야 합니다. 특히 원화 약세를 극복하는 유일한 테마는 반도체 독점 지배력입니다.",
      "action_point": "급락한 LG전자 등 피지컬 AI 테마주의 10일선 지지 여부를 체크하고, 거래대금이 실리는 KOSDAQ 대표 반도체 소부장(증착/식각 전공정 장비) 기업들 위주로 포트폴리오를 구성해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["상승추세", "코스닥반등", "거래대금부족", "LG전자조정", "환율방어", "이동평균선", "삼프로TV"]
    }
  },
  "aoMNqAoPYTw": {
    "primary": "tech",
    "video": {
      "id": "aoMNqAoPYTw",
      "title": "젠슨 황 방한 전 급등한 피지컬AI?! 큰 그림 그려야 합니다! | 이선엽 AFW파트너스 대표 [글로벌 인터뷰]",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=aoMNqAoPYTw",
      "thumbnail": "https://img.youtube.com/vi/aoMNqAoPYTw/hqdefault.jpg"
    },
    "analysis": {
      "summary": "젠슨 황의 방한 목적은 관광이 아닌 아시아 내 제조 파트너십 구축이며, 특히 물리적인 공간에서 소프트웨어가 동작하는 피지컬 AI(로보틱스 및 제조 공정 자동화) 부문이 핵심 아젠다입니다. 일시적인 6월의 매크로/수급 조정을 포트폴리오 내 비(非)주도주를 정리하고 인프라 코어(Core) 자산으로 이동하는 기회로 활용할 것을 조언합니다.",
      "key_claims": [
        "젠슨 황의 방한은 엔비디아의 차세대 먹거리인 피지컬 AI 및 제조 혁신을 위한 한국 파트너(LG, 두산 등)들과의 실무 미팅이다.",
        "6월 증시의 변동성은 거치식이 아닌 분할 매수 대응 구간이며, 스페이스X IPO 자금 블랙홀 노이즈로 펀더멘탈 훼손은 없다.",
        "매크로 hawkish 연준 위원들의 구두 개입이 있으나 하반기 웰스 팽창 흐름을 꺾을 수준의 위험은 아니다."
      ],
      "data_points": [
        "엔비디아가 추진하는 피지컬 AI 협력사 규모 및 장기 로드맵 논의 개시"
      ],
      "signal": "bullish",
      "signal_reason": "피지컬 AI는 향후 수년 간 제조업 전체의 스마트화 및 로보틱스 전환을 견인할 대형 메가트렌드이며, 핵심 파트너로 낙점된 국내 제조 대형주의 장기 성장이 뚜렷합니다.",
      "key_companies": ["NVIDIA", "LG전자", "두산로보틱스"],
      "insight": "주식 투자의 성공은 메가 트렌드의 종착역을 신뢰하는 데 있습니다. 젠슨 황의 방한은 한국의 제조/패키징 파트너십 가치를 글로벌 밸류체인에 각인시키는 촉매제가 될 것입니다.",
      "action_point": "단기 차익 실현으로 급조정된 LG전자, 현대차, 두산 등 로봇 및 공정 제어 수혜주의 비중을 분할 적립하고 포트폴리오를 AI 핵심주 위주로 압축해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock", "robot"],
      "tags": ["피지컬AI", "젠슨황방한", "제조자동화", "포트폴리오압축", "6월조정", "삼프로TV"]
    }
  },
  "bgZr7iwWAVA": {
    "primary": "stock",
    "video": {
      "id": "bgZr7iwWAVA",
      "title": "[홍장원의 불앤베어] 증시 주도주 큰 물결 바뀌나. 골드만삭스 \"바이더딥 유지하라\"",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=bgZr7iwWAVA",
      "thumbnail": "https://img.youtube.com/vi/bgZr7iwWAVA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "레이먼드 제임스의 칼 에커먼 애널리스트가 중국 창신메모리(CXMT) 및 양쯔메모리(YMTC)의 공격적인 범용 메모리 팹 증산과 스마트폰 수요 파괴(14% 감소 우려)로 인해 D램/낸드 평균 판매가(ASP)가 올해 중반에 조기 피크아웃할 수 있다고 경고했습니다. 그럼에도 골드만삭스 등 대형 IB들은 '바이 더 딥(Buy the dip)'을 주문하고 있습니다.",
      "key_claims": [
        "중국 CXMT는 상하이에 본사 대비 3배 규모의 펩을 지어 범용 메모리 점유율을 14% 수준까지 올릴 준비를 하고 있다.",
        "삼성/하이닉스가 마진이 높은 AI용 HBM 및 eSSD에 집중하면서 발생한 범용 D램 숏티지 틈새를 중국 업체들이 치고 들어와 전체 ASP 하락 압력을 가할 수 있다.",
        "글로벌 스마트폰 출하량이 고부가가치 메모리 가격 단가 상승 부담으로 14% 수준 급감하며 전형적인 사이클 정점 신호를 보내고 있다."
      ],
      "data_points": [
        "창신메모리(CXMT) 글로벌 D램 점유율 전망: 기존 11%에서 올해 13.9%로 증가",
        "올해 글로벌 스마트폰 출하량 전망 감소율: 카운터포인트 리서치 기준 -14%"
      ],
      "signal": "neutral",
      "signal_reason": "AI 메모리는 극심한 공급 부족이나, 중국의 대규모 범용 팹 증설과 모바일 단가 전가 한계에 따른 전체 메모리 정점 우려가 유입되며 섹터 간 디커플링이 지속될 것입니다.",
      "key_companies": ["삼성전자", "SK하이닉스", "마이크론"],
      "insight": "메모리 사이클은 향후 '고부가 AI 전용 스택'과 '저가용 범용 마켓'의 양극화 체제로 갈릴 것입니다. 중국의 범용 시장 침투는 전체 평균 단가(ASP)에는 악재이나, 독점적 지위를 가진 HBM 공급망에는 실질적 타격이 되지 못합니다.",
      "action_point": "중국의 진입이 어려운 HBM, TSV 패키징, 특화 eSSD 장비 공급사 중심의 압축 투자를 유지하고, 중국의 물량 공세 리스크가 노출된 범용 D램 의존주들은 비중을 조절해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["범용메모리", "창신메모리", "양쯔메모리", "피크아웃논란", "스마트폰수요파괴", "바이더딥", "매경월부"]
    }
  },
  "CYIsi51i1GE": {
    "primary": "economy",
    "video": {
      "id": "CYIsi51i1GE",
      "title": "AI부터 양말까지 싹쓸이 포스트 중국은 없다 (해담경제연구소 어예진 소장) (1부)",
      "published": "2026-06-04T08:00:00+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=CYIsi51i1GE",
      "thumbnail": "https://img.youtube.com/vi/CYIsi51i1GE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "동아시아의 전통적인 안행형 발전 모델(Flying Geese Paradigm: 일본->한국/대만->중국 순의 제조업 이관)에 따라 포스트 중국 제조 허브(베트남, 방글라데시, 인도 등)의 성장이 기대되었으나, 실제 데이터 재산정 결과 완제품 완제 공정이 넘어가도 실질적인 부가가치(실, 단추, 부자재, 제봉틀 등)의 60% 이상은 여전히 중국산에 의존하고 있어 '완벽한 탈중국 대체제'는 부재함을 고찰합니다.",
      "key_claims": [
        "미국이나 서방 패션/테크 브랜드들이 베트남이나 방글라데시로 공장을 대거 이전하여 겉으로는 중국 비중이 급감한 듯 보인다.",
        "그러나 실질 부가가치 원산지 기준으로 원자재와 중간재를 역추적하면 중국의 실질 공급 지배력은 60% 이상으로 공고하다.",
        "중국은 범용 원부자재 및 기계 부품 에코시스템의 압도적 비용 해자를 구축해 신흥 개도국이 중국의 서플라이 체인망 없이 수출하는 것을 불가능하게 만든다."
      ],
      "data_points": [
        "개도국 섬유/완제품 생산에서 중국산 원부자재 및 기계의 실질 부가가치 점유율: 60% 이상 초과 유지"
      ],
      "signal": "neutral",
      "signal_reason": "서방의 인위적인 공급망 탈중국(Friend-shoring) 드라이브의 속도는 계속되고 있으나, 중국 제조업의 부품 생태계 지배력이 유지되어 장기적인 비용 인플레를 유발하고 있습니다.",
      "key_companies": ["언더스탠딩"],
      "insight": "탈중국(De-risking)은 정치적 네러티브일 뿐, 물리적 제조업의 밑단은 중국의 공급망 해자를 대체하지 못했습니다. 신흥 제조 허브로 분류되는 국가들의 밸류체인도 결국 중국 중간재 수입 확대로 수혜를 입는 의존 관계입니다.",
      "action_point": "베트남/인도 등의 완제품 조립 공장 테마주에 대한 과도한 프리미엄은 경계하고, 오히려 글로벌 공급망의 유일한 중간 부품 기지이자 비용 전가력이 있는 제조 강자들의 지분을 지켜봐야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["etc"],
      "tags": ["안행형발전모델", "탈중국허구", "원부자재의존", "공급망지배력", "베트남방글라데시", "비용인플레이션", "언더스탠딩"]
    }
  },
  "d8Uxeqq7bpA": {
    "primary": "economy",
    "video": {
      "id": "d8Uxeqq7bpA",
      "title": "도이치뱅크, 브로드컴 목표가 515달러로 상향ㅣ원·달러환율 야간거래 1540원 넘겨ㅣ비트코인 4개월만 최저치 6만1천불 터치ㅣ홍키자의 매일뉴욕",
      "published": "2026-06-04T11:20:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=d8Uxeqq7bpA",
      "thumbnail": "https://img.youtube.com/vi/d8Uxeqq7bpA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "도이치뱅크의 브로드컴 목표가($515) 상향에도 불구하고, 구글의 TPU 공급망 멀티벤더 가이던스가 트리거가 되어 브로드컴의 주가는 급락했습니다. 한편, 거시 지표로는 원달러 환율이 야간 거래 중 1,540원을 상회하며 외환 불안이 심화되었고, 비트코인은 유동성의 AI 이탈로 인해 4개월 만에 6만 1천 달러 선까지 이탈했습니다.",
      "key_claims": [
        "브로드컴은 구글의 AI TPU를 10년 간 독점 개발해왔으나, 구글이 800억 달러 증자 후 공급망 다각화(마벨 등의 진입 허용)를 언급하며 독점 프리미엄이 훼손되었다.",
        "미국의 금리 역전차와 중동 리스크가 누적되며 원달러 야간 환율이 1,540원을 돌파하여 수입 물가 압박이 극대화되고 있다.",
        "비트코인은 가상자산 내부 모멘텀의 부재와 글로벌 패시브 자금의 AI 인프라 쏠림 진공청소기 효과로 6만 1천 달러 대의 저점을 다시 터치했다."
      ],
      "data_points": [
        "도이치뱅크 제시 브로드컴 목표주가: 515달러",
        "원달러 야간 환율 최고치 기록: 1,540원 초과 돌파",
        "비트코인 저점 가격: 61,000달러 선 터치"
      ],
      "signal": "bearish",
      "signal_reason": "1,540원대의 파국적 환율 약세와 크립토의 유동성 소외, 그리고 독점 테크 대장주의 공급망 분열 우려가 시장의 불안 심리를 높이고 있습니다.",
      "key_companies": ["브로드컴", "마벨", "구글", "코인베이스"],
      "insight": "아무리 높은 실적 증가율(+48%)을 기록하더라도 독점 해자(Monopoly Moat)의 균열은 고배수 멀티플 테크주에 치명적입니다. 또한, 환율 1,540원선 돌파는 한국 금통위의 운신 폭을 좁히며 경제 전반에 큰 비용 고통을 강제합니다.",
      "action_point": "환율 급등에 따른 자산 가치 하락을 헷징하기 위해 달러 기반 국채 및 실적이 깨지지 않는 반도체 선두 장비주 위주의 보수적 방어벽을 쳐야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "crypto"],
      "tags": ["브로드컴급락", "원달러환율1540원", "비트코인붕괴", "멀티벤더전략", "구글TPU", "매경월부"]
    }
  },
  "DiJGYBMPLtM": {
    "primary": "tech",
    "video": {
      "id": "DiJGYBMPLtM",
      "title": "“EUV 장비 없이 1.4나노 성공?” 美 규제에 화웨이가 던진 승부수 #교양이를부탁해",
      "published": "2026-06-05T00:00:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=DiJGYBMPLtM",
      "thumbnail": "https://img.youtube.com/vi/DiJGYBMPLtM/hqdefault.jpg"
    },
    "analysis": {
      "summary": "화웨이가 네덜란드 ASML의 최첨단 노광 장비(EUV) 수출 제재를 피하기 위해 독자적인 3D 칩 스태킹(적층 및 다차원 본딩) 방식을 도입해 1.4나노급 성능 돌파를 시도하고 있으나, 극악의 누적 수율 문제로 양산 한계에 봉착해 있음을 분석합니다.",
      "key_claims": [
        "중국은 미국의 EUV 장비 차단에 대응하여 칩을 위로 겹쳐 쌓아 신호 거리를 단축하는 3D 스택 패키징 기술을 우회로로 삼았다.",
        "장비 한계로 인한 개별 칩의 수율(20% 수준)이 낮아, 두 개 이상을 적층하는 본딩 공정까지 거칠 경우 완제품의 실제 누적 수율은 10% 미만으로 떨어지는 엔지니어링 병목에 갇혀 있다."
      ],
      "data_points": [
        "화웨이 독자 반도체 시제품 개별 수율 수준: 약 20% 수준 (불량률 80%)",
        "3D 패키징 적층 시 완제품 예상 수율 수준: 10% 이하 추정"
      ],
      "signal": "bearish",
      "signal_reason": "중국의 반도체 자급화 내러티브는 화려하나, 최첨단 리소그래피 장비 부재에 따른 수율 저하라는 물리적 장벽에 부딪혀 글로벌 첨단 공급망을 실질적으로 위협하기 어렵습니다.",
      "key_companies": ["화웨이", "ASML", "TSMC"],
      "insight": "EUV 노광 장비 없이 칩 성능을 올리려는 3D 스태킹은 불량률이 누적 곱 연산으로 축적되는 수학적 한계를 지닙니다. 미국의 장비 차단 제재 효과가 강력하게 작동하고 있음을 보여주는 사례입니다.",
      "action_point": "중국의 추격 우려에 따른 첨단 파운드리/장비 대장주들의 센티멘트 흔들림 발생 시, ASML 및 TSMC와 같은 핵심 제재 수혜주의 장기 보유 강도를 강화해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["economy"],
      "tags": ["화웨이수율", "3D스태킹", "EUV장비제한", "ASML독점", "반도체수출통제", "교양이를부탁해"]
    }
  },
  "EWAVhfjl304": {
    "primary": "tech",
    "video": {
      "id": "EWAVhfjl304",
      "title": "아틀라스 발보면 기술력 보인다 현대차 테슬라",
      "published": "2026-06-05T00:00:00+00:00",
      "channel_name": "엔지니어TV",
      "url": "https://www.youtube.com/watch?v=EWAVhfjl304",
      "thumbnail": "https://img.youtube.com/vi/EWAVhfjl304/hqdefault.jpg"
    },
    "analysis": {
      "summary": "보스턴 다이내믹스의 신형 전기 아틀라스 로봇(현대차 소유)의 발과 관절 메커니즘을 정밀 분석합니다. 고난도 축구 슛 동작(고스트 라보나)을 통해 80-90%의 전신 체중을 한 다리로 지탱하고 착지 시의 동적 균형 제어와 발목 액추에이터의 댐핑 성능을 입증했습니다. 특히 좌우 대칭이 동일하여 양산 및 수리가 극대화된 설계가 돋보입니다.",
      "key_claims": [
        "신형 아틀라스는 좌우 다리 및 발의 설계가 완벽히 동일한 대칭형 부품 구조를 채택하여 대량 생산과 부품 교체의 편의성을 2배 높였다.",
        "테슬라 옵티머스는 사람의 발가락 관절 구조를 모방해 고장이 잦고 유지보수가 어려운 반면, 아틀라스는 복잡성을 덜고 기계적 효율성을 확보했다.",
        "한 발목에 순간적인 고속 회전력과 착지 시 충격 흡수를 제어하는 액츄에이터 동적 제어 기술이 보스턴 다이내믹스의 최대 하드웨어 강점이다."
      ],
      "data_points": [
        "순간 한 다리 지지율: 전신 하중의 80~90% 순간 부하 분산 제어 성공"
      ],
      "signal": "bullish",
      "signal_reason": "현대차 그룹이 보유한 보스턴 다이내믹스의 로봇 메카트로닉스 설계 효율성과 기계적 신뢰성이 테슬라 등 경쟁사를 압도하고 있음을 보여줍니다.",
      "key_companies": ["현대자동차", "테슬라"],
      "insight": "휴머노이드 로봇의 상용화 성공은 화려한 보행보다 '대량 생산 단가'와 '유지보수 신뢰성'에 달려 있습니다. 아틀라스의 좌우 동일 다리 설계는 자동차 양산 DNA가 결합된 실용적 제조 디자인의 승리입니다.",
      "action_point": "피지컬 AI의 핵심이 될 보스턴 다이내믹스에 부품 및 엑츄에이터 모터 기술을 공급하는 관련 부품 공급 체인을 선점해 나갈 필요가 있습니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["robot", "stock"],
      "tags": ["아틀라스로봇", "보스턴다이내믹스", "현대차로봇", "발목관절설계", "양산편의성", "옵티머스비교", "엔지니어TV"]
    }
  },
  "f20kF9HLqeU": {
    "primary": "energy",
    "video": {
      "id": "f20kF9HLqeU",
      "title": "벽돌보다 태양광이 싸다 유럽의 '기괴한 담장' (권효재 대표)",
      "published": "2026-06-05T00:00:00+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=f20kF9HLqeU",
      "thumbnail": "https://img.youtube.com/vi/f20kF9HLqeU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "유럽에서 중국산 태양광 패널 공급 과잉으로 인해 패널 단가가 벽돌보다 저렴해져, 태양광 패널을 정원 담장이나 벽면에 그대로 박아 넣는 '태양광 담장' 기현상과 이로 인한 전력 계통 수용성 문제를 간략히 짚어봅니다.",
      "key_claims": [
        "중국 기업들의 태양광 모듈 덤핑으로 가격이 폭락하여 일반 건축 자재보다 저렴하게 소비되는 전도 현상이 발생했다.",
        "무분별한 개인 태양광 보급은 한낮 송전망 전압 불균형 등 전력망 안정성 위기를 심화시키고 있다."
      ],
      "data_points": [
        "중국산 범용 태양광 모듈 단가의 지속적 가격 하향세 지속"
      ],
      "signal": "neutral",
      "signal_reason": "태양광 패널 시장 자체의 마진은 중국의 공급 과잉으로 박살 났으나, 이로 인해 송배전망 그리드 통제 및 ESS 전력 안정화 장비에 대한 수요는 더욱 커지고 있습니다.",
      "key_companies": ["지멘스", "ABB"],
      "insight": "하드웨어 단가의 폭락은 시스템 복잡성을 급격히 끌어올리며, 최후의 마진은 시스템을 최적화하는 제어 기기와 송전 안보에 수렴합니다.",
      "action_point": "태양광 패널 제조사 투자는 피하고, 전력망 과부하를 해소할 배전 기기 및 송전망 관리 솔루션 선도주에 대한 투자 포커스를 유지해야 합니다."
    },
    "classification": {
      "primary_topic": "energy",
      "secondary_topics": ["economy"],
      "tags": ["태양광패널과잉", "태양광담장", "유럽전력망", "그리드제어", "중국공급과잉", "언더스탠딩"]
    }
  },
  "Fiue-j_K41s": {
    "primary": "stock",
    "video": {
      "id": "Fiue-j_K41s",
      "title": "[6월 4일 마감시황] 코스닥도 결국 반도체였다…소부장 급반등 속 삼전닉스는 왜 걱정 없나ㅣ홍선애, 이권희, 김장열 [클로징벨 라이브]",
      "published": "2026-06-04T08:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=Fiue-j_K41s",
      "thumbnail": "https://img.youtube.com/vi/Fiue-j_K41s/hqdefault.jpg"
    },
    "analysis": {
      "summary": "코스피 대형주가 쉬어가는 틈을 타 코스닥 반도체 전공정(증착/식각 등) 장비 소부장(원익IPS, 이오테크니스, 유진테크 등) 기업들이 급반등을 주도했습니다. 이는 최태원 회장의 5개년 HBM 및 전공정 대규모 설비 투자 가시화와 일본 키옥시아(Kioxia)의 낸드/디램 투자 재개 발표가 촉매제가 되었으며, 정부의 코스닥 활성화 정책 기대가 더해졌습니다.",
      "key_claims": [
        "코스피 상승 피로로 코스닥 소부장으로 수급이 순환되어 전공정 대형 장비사들이 상한가 및 두 자릿수 상승을 보였다.",
        "SK그룹의 향후 5개년 설비 투자 의지와 키옥시아의 팹 가동/투자 재개 소식이 장비 제조사들의 장기 수주 신뢰도를 복원했다.",
        "젠슨 황 관련 테마주들은 미팅 업체 증가(LG CNS, 크래프톤, 방산 등)로 희소성 프리미엄이 옅어지며 단기 차익 실현 조정을 겪고 있다."
      ],
      "data_points": [
        "주요 전공정 장비 상승률: 원익IPS, 유진테크 등 급등 및 대량 거래 유입",
        "코스닥 지수 상승률: 반도체 밸류체인 견인으로 코스피 대비 강한 아웃퍼폼 마감"
      ],
      "signal": "bullish",
      "signal_reason": "단기적인 시총 상위 투톱의 쉬어감 속에서도, 실질 장기 CapEx 수혜를 직접 입는 전공정 장비 섹터로 수급이 확산되어 장기 반도체 사이클이 튼튼함을 방증합니다.",
      "key_companies": ["원익IPS", "유진테크", "이오테크닉스", "SK하이닉스"],
      "insight": "그간 후공정(HBM 패키징)에 가려져 심각하게 소외되었던 전공정(Deposition/Etch) 장비주들은 키옥시아 투자 재개와 SK의 설비 투자 로드맵을 통해 최악의 터널을 벗어났습니다. 쏠림 해소 국면의 전형적인 수혜주입니다.",
      "action_point": "차익 실현에 노출된 고밸류 후공정 주식 비중을 일부 조율하고, 밸류에이션 매력이 크고 실적 턴어라운드가 확인되는 전공정 증착/세정 대표 장비주로 비중을 재배치해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["코스닥반등", "소부장급등", "전공정장비주", "원익IPS", "유진테크", "키옥시아투자", "젠슨황방한", "삼프로TV"]
    }
  },
  "HbR-MdMx2U8": {
    "primary": "stock",
    "video": {
      "id": "HbR-MdMx2U8",
      "title": "[26.06.04 오후 방송 전체보기] 이제 온기는 코스닥으로? 소부장 몸값 '껑충'...젠슨 황 방한 D-1 \"바쁘다 바빠\" [클로징벨 라이브]",
      "published": "2026-06-04T09:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=HbR-MdMx2U8",
      "thumbnail": "https://img.youtube.com/vi/HbR-MdMx2U8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "코스피의 숨고르기 속에 코스닥 지수가 IT 소부장 장비주들의 강세로 전방위 반등에 성공했습니다. 최태원 회장의 설비 투자 확대 및 일본 키옥시아의 반도체 투자 재개 로드맵이 한국 전공정 장비 업계에 훈풍을 주었으며, 내일 오후 젠슨 황 엔비디아 CEO의 방한을 앞두고 다수의 국내 기업(LG CNS, 크래프톤 등)과의 미팅이 거론되는 등 AI 수혜 확산세가 뚜렷합니다.",
      "key_claims": [
        "외국인의 코스피 매도에도 불구하고, 대기 연금 자금과 코스닥 장비주의 대대적 숏커버/매수 유입이 지수 반전을 견인했다.",
        "미국의 반도체 장비 랠리에 동조하며, 그간 낙폭이 깊었던 증착/식각(원익IPS, 유진테크 등) 전공정 대표주에 거래대금이 쏠렸다.",
        "젠슨 황 방한 미팅 후보군이 확대되면서 특정 단일 기업의 독점 테마성 랠리는 차익 실현으로 제한되고, 실질적인 AI 인프라 수혜 기업군으로 시장의 옥석 가리기가 전개되고 있다."
      ],
      "data_points": [
        "코스닥 전공정 주요 장비주 상승폭: 상한가 및 10%대 이상 대거 분포",
        "젠슨 황 입국 예정 시점: 전세기 편으로 내일(6일 금요일) 오후 김포공항 입국 보도"
      ],
      "signal": "bullish",
      "signal_reason": "그간 반도체 랠리에서 철저히 소외되었던 코스닥 소부장이 전방 설비투자 회복 모멘텀을 안고 대거 상승 추세로 복귀하여 지수의 다변화와 안정을 이끌고 있습니다.",
      "key_companies": ["SK하이닉스", "원익IPS", "유진테크", "LG전자"],
      "insight": "반도체 주도권의 핵심은 '투자 재개'입니다. 키옥시아의 낸드 가동률 상승 및 SK의 장기 로드맵은 전공정 장비사들의 미래 실적 추정치를 상향시키는 팩트입니다. 젠슨 황의 방한 행보는 AI 확산 테마를 실물 비즈니스 레벨로 전이시키고 있습니다.",
      "action_point": "단기 급등 후 눌리는 대형 피지컬 AI주를 10일선 부근에서 분할 매수 수집하고, 전공정 회복 모멘텀이 살아있는 중대형 장비 대표주를 포트폴리오의 중축으로 확대해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["코스닥반등", "전공정장비", "키옥시아", "젠슨황입국일정", "LG그룹조정", "순환매장세", "삼프로TV"]
    }
  },
  "hwumaVGqY40": {
    "primary": "etc",
    "video": {
      "id": "hwumaVGqY40",
      "title": "요즘 대학생들의 한달 생활비 공개! | 공강 | How many?",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "Smart Money by MiraeAsset",
      "url": "https://www.youtube.com/watch?v=hwumaVGqY40",
      "thumbnail": "https://img.youtube.com/vi/hwumaVGqY40/hqdefault.jpg"
    },
    "analysis": {
      "summary": "요즘 대학생들의 한달 평균 생활비, 지출 구조, 주거비 부담 등 청년층의 소비 행태와 라이프스타일을 인터뷰 형식으로 입체적으로 조명합니다.",
      "key_claims": [
        "식비와 주거비의 가파른 상승으로 인해 대학생들의 고정 비용 지출 부담이 과거 대비 크게 심화되었다.",
        "청년층은 한정된 소득 내에서 서포터즈 활동, 파트타임 등 능동적인 재원 확보와 더불어 효율적 소비를 도모하고 있다."
      ],
      "data_points": [
        "대학생들이 밝힌 평균 월 생활비 수준 및 주거비 비율 분포"
      ],
      "signal": "neutral",
      "signal_reason": "생활 경제 및 대중 소비 패턴 스케치 영상으로, 청년 경제 여건을 파악할 수 있는 정성적 데이터를 제공합니다.",
      "key_companies": ["미래에셋증권"],
      "insight": "고물가 기조는 청년 세대의 가처분 소득을 강하게 제약하고 있으며, 이는 저가형 가공식품, 실용적 플랫폼 서비스 소비 쏠림으로 이어집니다.",
      "action_point": "청년층의 고정 비용 부담을 감안하여 저비용 가치 지향적 플랫폼 기업 및 필수 소비재 브랜드 중심의 기초 소비 시장을 분석해 둘 필요가 있습니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["대학생생활비", "고물가영향", "청년소비패턴", "인터뷰", "미래에셋증권"]
    }
  },
  "jSozCEgwl4I": {
    "primary": "stock",
    "video": {
      "id": "jSozCEgwl4I",
      "title": "브로드컴, 가이던스 부진에 급락…반도체, 광통신 등 AI H/W 대거 차익실현 [월가 뉴스레터]",
      "published": "2026-06-04T22:20:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=jSozCEgwl4I",
      "thumbnail": "https://img.youtube.com/vi/jSozCEgwl4I/hqdefault.jpg"
    },
    "analysis": {
      "summary": "브로드컴이 총매출(+48%) 및 AI 반도체 매출(+143%)의 높은 어닝 서프라이즈를 달성했음에도, 구글의 멀티벤더(공급망 다각화) 채택 가능성 언급으로 인해 독점 지위 약화 우려가 유입되며 주가는 급락했습니다. 이는 마이크론(-8%) 등 그간 급등했던 반도체 및 AI 하드웨어 밸류체인 전반의 대대적인 차익 실현을 유발했습니다.",
      "key_claims": [
        "브로드컴은 높은 실적에도 불구하고 구글 TPU 독점 체제 붕괴 우려(마벨 등 경쟁사의 잠재적 점유율 침투)로 인해 멀티플 조정을 겪었다.",
        "미 증시는 반도체 과열을 끄는 동안 다우 지수와 러셀 2000이 상승하고 오라클, 구글 등의 소프트웨어주가 반등하는 등 활발한 업종 순환매를 보였다.",
        "달러 인덱스가 99 수준까지 상승하고 원달러 환율이 1,540원 대를 노크하는 등 대외 외환 리스크가 여전히 잔존해 자본 유입에 걸림돌이 되고 있다."
      ],
      "data_points": [
        "브로드컴 장중/시간외 하락폭: 최고 -15% 수준 급락 마감",
        "달러 인덱스 수준: 99 부근 돌파 시도",
        "비트코인 등락: 하방 압력 지속되며 61,000달러 선 사수 테스트"
      ],
      "signal": "bearish",
      "signal_reason": "반도체 하드웨어 독점 해자의 훼손 가능성과 환율의 파국적 급등(1,540원), 크립토의 동반 약세로 인해 당분간 보수적인 주도주 이격 조정이 예상됩니다.",
      "key_companies": ["브로드컴", "마벨", "구글", "마이크론"],
      "insight": "주가가 신고가 부근일 때는 완벽한 실적만으로는 부족하며 독점력 유지가 핵심입니다. 구글의 멀티벤더 언급은 업계 2인자 마벨 테크놀로지에게 기회가 될 것이며, 주도권의 분산은 고점 밸류에이션 부담을 높이는 신호입니다.",
      "action_point": "브로드컴에 대한 단기 무리한 저가 매수 참여는 지양하되, 독점 다각화의 실질적 수혜자가 될 마벨의 점유율 추이를 모니터링하고 소프트웨어 및 방어주 비중을 유지해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["브로드컴급락", "구글멀티벤더", "차익실현", "달러인덱스99", "순환매장세", "삼프로TV"]
    }
  },
  "K3O3k0cqpr4": {
    "primary": "stock",
    "video": {
      "id": "K3O3k0cqpr4",
      "title": "삼전닉스 쉬어간다고 끝난 건 아닙니다. 조정장에서 봐야 할 진짜 신호ㅣ정프로, 박가영, 유창희 [주린이 구조대]",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=K3O3k0cqpr4",
      "thumbnail": "https://img.youtube.com/vi/K3O3k0cqpr4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "삼성전자와 SK하이닉스 등 반도체 투톱의 일시적인 조정세는 펀더멘탈 훼손이 아닌, 단기 과열 해소 및 미국 빅테크 변동성에 동조한 일시적 매물 출회입니다. 일반 서버 D램 가격의 강력한 반등과 설비투자 로드맵을 신뢰할 때, 조정 구간에서 봐야 할 핵심 신호는 HBM 장비 수주 지속성입니다.",
      "key_claims": [
        "반도체 대형주의 단기 조정은 대세 상승 추세 속의 자연스러운 5일선/10일선 이격 메우기 과정이다.",
        "일반 서버 D램 및 고용량 모바일 칩의 공급 부족으로 국내 대형 반도체사의 2분기 호실적 컨센서스는 계속 상향되고 있다.",
        "후공정에만 한정되던 수혜가 키옥시아 투자 및 하이닉스 증설을 바탕으로 전공정 핵심 장비사로의 확산이 뚜렷하다."
      ],
      "data_points": [
        "삼성전자/SK하이닉스 주요 이동평균선 격차 축소세 지속"
      ],
      "signal": "bullish",
      "signal_reason": "메모리 반도체 단가와 수요의 우상향 흐름이 단단하고, 설비투자가 실제 집행되기 시작하여 조정 시 저가 분할 매수 메리트가 높습니다.",
      "key_companies": ["삼성전자", "SK하이닉스"],
      "insight": "반도체 주가의 멈춤을 두려워할 필요가 없습니다. 본질인 어닝 가시성(DRAM 가격 상승세)과 대규모 설비 증설 로드맵이 실현되고 있으므로, 수급 이탈 노이즈는 좋은 저가 포지션 구축 기회입니다.",
      "action_point": "일시적 급락 시 대형 반도체 지분을 안정적으로 모아가고, 수주 확장이 확인되는 전공정/후공정 대표 소부장 장비주들의 포트폴리오를 유지해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["반도체조정", "이격메우기", "DRAM어닝", "설비투자", "소부장수혜", "삼프로TV"]
    }
  },
  "MHmvEMCMxcA": {
    "primary": "economy",
    "video": {
      "id": "MHmvEMCMxcA",
      "title": "[지식뉴스] \"돈 풀다 멈추면 미국 무너져요\" 돈 급한데 누가 국채 더 사줄까, 애타는 트럼프의 위험한 승부수 (ft.유신익 KB WM 수석 이코노미스트) / 교양이를 부탁해",
      "published": "2026-06-05T00:00:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=MHmvEMCMxcA",
      "thumbnail": "https://img.youtube.com/vi/MHmvEMCMxcA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 재정 적자 누적에 따른 국채 발행 부담을 해결하기 위해, 트럼프 및 자본 시장이 스테이블코인(클래리티 법안 통과 예정)의 미국 국채 토큰화 결합 시나리오를 가동하고 있습니다. 전 세계 소액 사학 세력들의 달러 이자부 자산(스테이블코인) 매수를 유도해 국채 수요를 확보하는 전략이나, 24시간 실시간 출금 속도와 전통 채권 유동화 간의 시차(SBB 파산과 유사한 유동성 불일치 리스크)가 잠재적 위협 요소입니다.",
      "key_claims": [
        "미국은 막대한 부채 롤오버(만기 연장)를 위해 전통 채권 매수층을 넘어 전 세계 개인 자금을 끌어들일 국채의 디지털 토큰화가 시급하다.",
        "USDC 등 스테이블코인의 발행사가 국채를 대거 편입하고, 법안(클래리티 법안)을 통해 소액 소지자에게 이자 성격의 보상을 제공하는 유통 구조가 핵심이다.",
        "민간 주도의 디지털 달러 유통이 급팽창(M2의 상당 비중인 5조~10조 달러 도달 가능)할 경우 무제한 레버리지로 글로벌 자산 가격 팽창을 유도하나, 긴급 런 발생 시 담보 채권 매각 시차의 불일치 뇌관이 존재한다."
      ],
      "data_points": [
        "미국 전체 통화량 M2 규모: 약 22조 달러",
        "스테이블코인의 잠재적 발행 팽창 목표 규모: 약 5조~10조 달러 수준 전망"
      ],
      "signal": "bearish",
      "signal_reason": "단기적으로는 글로벌 자금을 달러로 무한 빨아들여 자산 가격 상승 동력을 제공하나, 만기/유동성 불일치(SVB 사태의 디지털 버전)의 파국적 금융 시스템 뇌관을 깊게 심는 구조적 위험입니다.",
      "key_companies": ["서클", "블랙록"],
      "insight": "미국의 국채 토큰화 및 스테이블코인 이자화는 달러 패권을 디지털 온체인으로 무한 확장해 부채를 해결하려는 '현대 화폐 이론(MMT)'의 변형입니다. 24시간 거래되는 빠른 온체인과 느린 오프라인 국채 청산 간의 불일치는 언제든 시스템적 런(Run) 리스크를 내포합니다.",
      "action_point": "스테이블코인의 규제 법제화로 수혜를 입을 미국 채권 연계 RWA 플랫폼 기업 및 규제 통제를 넘어서는 실물 희소 자산(금, 대형 가치주)의 비중을 든든하게 보유해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["crypto", "stock"],
      "tags": ["미국국채", "토큰화", "스테이블코인", "클래리티법안", "유동성불일치", "양극화심화", "교양이를부탁해"]
    }
  },
  "O7Gkf2llIP8": {
    "primary": "stock",
    "video": {
      "id": "O7Gkf2llIP8",
      "title": "[빈난새의 개장전요것만-6월4일] 브로드컴 실적이 보여준것 | 감원도 구인도 많다 | 원유재고 바닥 | 협상 올인하는 트럼프 | 마이크론 크라우드스트라이크 시에나 팔란티아 AADX",
      "published": "2026-06-04T14:35:00+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=O7Gkf2llIP8",
      "thumbnail": "https://img.youtube.com/vi/O7Gkf2llIP8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "브로드컴의 높은 실적 서프라이즈에도 불구하고 구글 TPU 멀티벤더 도입 우려에 따른 하락세와, 미국 신규 실업수당 증가 등 고용 둔화 팩트가 시장의 6월 조정을 주도하고 있습니다. 한편 미국 원유 재고 감소세가 심화되며 트럼프가 대선 유가 통제를 위해 이란과의 합의 성사에 목을 매고 있는 지정학적 상황과, 메모리 고단가 지속이 완제품 수요를 파괴하는 '칩플레이션(Chipflation)' 리스크가 부각되고 있습니다.",
      "key_claims": [
        "브로드컴의 구글 독점 구도 약화 가능성(마벨의 침투)이 밸류에이션 부담 완화를 위한 빌미로 작용해 반도체 전반의 차익 실현을 야기했다.",
        "미국의 원유 재고 바닥 우려와 중동 긴장이 겹치며 유가 통제에 실패할 경우, 고금리 장기화를 이끌 긴축적인 연준 구두 개입이 7월부터 강화될 수 있다.",
        "모건스탠리는 메모리 고단가 부담으로 다운스트림 디바이스(스마트폰 등)의 생산 원가 부담이 한계에 도달해 가격 조정 압력(칩플레이션)이 누적되고 있다고 지적했다."
      ],
      "data_points": [
        "구글의 자금 조달 업사이징 규모: 최종 847억 달러 유상증자 완료",
        "미국 원유 재고 감소율 및 신규 실업수당 신청 건수의 완만한 증가세 기록"
      ],
      "signal": "bearish",
      "signal_reason": "칩플레이션에 따른 스마트폰 등 전방 IT 수요 파괴 징후와 원유 재고 감소에 따른 에너지 물가 압박, 그리고 연준의 매파적 금리 정책 유지 가능성이 복합 악재로 결합되고 있습니다.",
      "key_companies": ["브로드컴", "마벨", "구글", "NVIDIA"],
      "insight": "반도체의 초격차 어닝 뒤에는 전방 IT 제조사들이 단가 상승을 더 이상 감당하지 못하는 칩플레이션의 역효과가 누적되고 있습니다. 유가 통제를 위해 이란 핵합의를 서두르는 트럼프의 행보도 거시 금융 시장의 타이트한 한계를 보여줍니다.",
      "action_point": "원가 부담을 스스로 전가할 수 있는 완성형 소프트웨어 및 클라우드 빅테크로 자산을 배분하고, 단가 급등 부작용 리스크가 있는 메모리 반도체 하드웨어 비중을 적절히 조율해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["브로드컴실적", "구글TPU", "칩플레이션", "원유재고감소", "이란핵협상", "실업수당청구", "한경글로벌마켓"]
    }
  },
  "pRrxRPnY9Oc": {
    "primary": "economy",
    "video": {
      "id": "pRrxRPnY9Oc",
      "title": "삼성전자 번 돈 우리도 나눠달라. 불붙은 '초과이익 배분' 논란 (언더스탠딩 백종훈 기자)｜2026년 06월 02일 녹화",
      "published": "2026-06-04T07:55:00+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=pRrxRPnY9Oc",
      "thumbnail": "https://img.youtube.com/vi/pRrxRPnY9Oc/hqdefault.jpg"
    },
    "analysis": {
      "summary": "삼성전자 노조의 파업과 임금 협상 국면 속에서, 고용노동부 장관이 제안한 '초과 이익의 원·하청 상생 연대 임금 배분' 화두를 둘러싸고 국가적 정책 논쟁이 격화되고 있습니다. 산업통상자원부 장관과 학계는 초격차 유지를 위해 반도체 이익의 70%를 R&D 및 설비에 재투자해야 한다고 맞서며, 노동 사회 정책과 국가 산업 패권 전략이 정면 충돌하고 있습니다.",
      "key_claims": [
        "노동부 장관은 삼성전자의 거대 이익이 정부의 대규모 세액 공제(K-칩스법 등)와 공공 인프라(용수/전력) 지원의 합작품이므로 협력사와 분배해야 한다고 제안했다.",
        "산업부 장관과 학계는 글로벌 반도체 속도전 상황에서 이윤 분배에 치중하는 배분주의는 기술 초격차를 잃게 만드는 자멸책이라며 즉각 반대했다.",
        "노조의 파업 영향과 원칙 없는 보너스 배분 관행이 대기업 내부 정규직과 협력사 근로자 간의 임금 양극화 논쟁으로 비화되었다."
      ],
      "data_points": [
        "반도체 세액 공제 비율: 최대 20% 수준 (K-칩스법 기준)",
        "반도체 이익의 재투자 권고 비율: 김정호 교수 기준 최소 70% 이상 (R&D 및 설비)"
      ],
      "signal": "neutral",
      "signal_reason": "이윤 분배 논란은 국내 대기업의 비용 구조 및 투자 집중도를 떨어뜨릴 수 있는 잠재적 리스크 요인이 될 수 있어 중립적인 관찰이 요구됩니다.",
      "key_companies": ["삼성전자", "SK하이닉스"],
      "insight": "반도체 이익은 상수가 아닌 글로벌 치킨 게임과 혁신의 결과입니다. 세액 공제를 빌미로 기업의 사적 이윤을 연대 임금 형태로 사회화하려는 정책 시도는 반도체 경쟁 안보라는 거대한 패권 국면과 충돌을 피할 수 없습니다.",
      "action_point": "임금 협상 및 파업 장기화에 따른 단기 수급 차질 여부와 국내 반도체 대기업들의 설비 투자 집행률 변동 가능성을 추적하며 포지션을 관리해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["삼성전자파업", "초과이익배분", "연대임금", "노동부장관", "재투자비율", "반도체초격차", "언더스탠딩"]
    }
  },
  "uBjyIom3kOA": {
    "primary": "space",
    "video": {
      "id": "uBjyIom3kOA",
      "title": "스페이스X 때문에 들썩이는 우주항공주, 지금 주목해야 할 종목은?ㅣ정프로, 박가영, 최창규 [주린이 구조대]",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=uBjyIom3kOA",
      "thumbnail": "https://img.youtube.com/vi/uBjyIom3kOA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "스페이스X가 $135 고정 공모가로 IPO 로드쇼에 들어가며 시가총액 1.75조~2조 달러(한화 약 2,500조 원 이상) 가치 평가 논의가 본격화되었습니다. 나스닥, MSCI, S&P 500 등 글로벌 주요 지수 편입에 따른 패시브 인덱스 추종 자금(약 50조~100조 원 예상)의 무조건적 매수세 유입이 전망되며, 미국 개인 투자자들에게 20~30% 배정하는 이례적 리크루팅이 진행 중입니다.",
      "key_claims": [
        "스페이스X 상장 시 패시브 인덱스 자금(MSCI, FTSE, S&P 500 등)의 강제 매수가 50조~100조 원 규모로 발생해 타 자산의 유동성을 청소기처럼 흡수할 것이다.",
        "현재 영업이익은 스타링크 및 발사체 감가상각과 대규모 CAPEX로 마이너스 상태이나, 감가상각 전 조정 EBITDA는 65억 달러 이상으로 현금 창출력이 검증되었다.",
        "2조 달러 시가총액은 8년치 베스트 시나리오(발사 실패 제로, 스타링크 침투율 폭증)를 선반영한 멀티플로 다소 밸류에이션 부담이 있다."
      ],
      "data_points": [
        "스페이스X IPO 예정 공모가: 주당 135달러 고정 제시",
        "스페이스X 시가총액 목표 범위: 1.75조 달러 ~ 2조 달러 수준",
        "2025년 기준 매출액: 186억 달러 (EBITDA 조정치는 약 65.8억 달러 기록)",
        "공모 물량 중 리테일(개인) 배정 비율: 이례적인 20~30% 배정"
      ],
      "signal": "bullish",
      "signal_reason": "글로벌 상장 지수 펀드들의 대규모 패시브 의무 유입세와 독보적인 민간 우주 통신(스타링크) 지배력의 가치 입증이 우주항공 섹터 전반에 장기 성장 에너지를 불어넣고 있습니다.",
      "key_companies": ["스페이스X", "테슬라"],
      "insight": "스페이스X 상장은 현대 금융 역사상 가장 큰 우주인프라 독점 플랫폼의 상장입니다. 지수 편입에 따른 패시브 매수 자금 규모가 50조 원을 넘기 때문에, 글로벌 기관들은 이미 타 자산(신흥국 주식 등)을 덜어내고 스페이스X 매입을 위한 달러 현금 실탄을 장전하고 있습니다.",
      "action_point": "스페이스X IPO로 인해 수급 수혜 및 프록시 프리미엄을 공유할 국내 우주항공 안테나 및 위성 통신용 핵심 기자재 수출 강소기업들을 발굴하여 장기 보유해야 합니다."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["stock", "tech"],
      "tags": ["스페이스X", "스타링크", "IPO공모가", "패시브자금", "지수편입", "밸류에이션논란", "EBITDA", "삼프로TV"]
    }
  },
  "UulRoRcqruU": {
    "primary": "etc",
    "video": {
      "id": "UulRoRcqruU",
      "title": "이집트 미라와 완전히 다르다? 내부 장기까지 보존된 한국 미라의 정체",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=UulRoRcqruU",
      "thumbnail": "https://img.youtube.com/vi/UulRoRcqruU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "인위적으로 장기를 제거하고 약품 처리하는 이집트 미라와 달리, 회곽묘라는 조선 시대의 독특한 묘제 양식과 기후적 특성에 의해 장기와 의복이 자연 보존된 '한국 미라'의 고병리학적(Paleopathology) 가치와 유전자 분석 과학을 소개합니다.",
      "key_claims": [
        "한국 미라는 회(석회), 모래, 황토를 섞어 굳힌 회벽곽이 외부 공기 및 수분을 완전 차단하고, 내부 유기물이 자연 건조/밀폐되어 보존된다.",
        "미라 내부 장기의 병리학적 분석을 통해 수백 년 전 한국인의 질병 역사(간흡충증, 결핵 등)와 식습관 데이터를 역추적할 수 있다."
      ],
      "data_points": [
        "조선 시대 묘제 회곽묘 구조 및 한국 미라 보존 상태 고찰"
      ],
      "signal": "neutral",
      "signal_reason": "대중적 역사 과학 콘텐츠로, 한국 고유의 고병리학 연구 성과와 바이오 유전자 해독 기술의 고고학적 도입을 소개하는 정성적 배경을 제공합니다.",
      "key_companies": [],
      "insight": "한국의 미라는 과거 세대의 생물학적 기록물(유전자 뱅크)이며, 유전자 시퀀싱 기술 발달로 수백 년 전 인류의 질병 기전과 항체 저항성 정보를 연구하는 귀중한 데이터 원천이 됩니다.",
      "action_point": "유전자 시퀀싱(NGS) 및 정밀 고병리 진단 기술을 보유한 바이오 분석 장비 제조 업계의 장기적 학술 및 산업적 쓰임새 확장을 지켜봐야 합니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["한국미라", "회곽묘", "고병리학", "장기보존", "유전자시퀀싱", "안될과학"]
    }
  },
  "wA3eCk7ztJA": {
    "primary": "tech",
    "video": {
      "id": "wA3eCk7ztJA",
      "title": "브로드컴 쇼크..AI 반도체 이대로 꺾이나?",
      "published": "2026-06-05T00:00:00+00:00",
      "channel_name": "월텍남",
      "url": "https://www.youtube.com/watch?v=wA3eCk7ztJA",
      "thumbnail": "https://img.youtube.com/vi/wA3eCk7ztJA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "구글의 독점적 파트너였던 브로드컴이 TPU 가이던스 발표 시 공급 다각화 가능성을 제기하면서 시간외 -15% 급락했습니다. 이는 AI 가속기 독점의 붕괴 우려를 가중시켰으나, 장기적인 클라우드 빅테크의 반도체 투자 속도와 소프트웨어 확산세는 견조하여 단기 이격 과열 해소로 해석됩니다.",
      "key_claims": [
        "구글이 TPU 공급망에 마벨 등 제2의 벤더들을 진입시킬 여지를 준 것이 브로드컴의 고점 밸류에이션 조정 요인으로 작용했다.",
        "하지만 구글의 $847억 대형 유상증자를 비롯한 빅테크의 공격적인 설비투자 규모는 변함없이 반도체 소부장의 주문량을 지지한다."
      ],
      "data_points": [
        "브로드컴 주가 하락폭: 장외 시장에서 약 15% 하락 마감"
      ],
      "signal": "neutral",
      "signal_reason": "구글 TPU 독점 체제 붕괴라는 개별 리스크가 유입되었으나, 전체 AI 인프라 장기 수요가 축소되는 것은 아니며 쏠림의 다각화 과정이기 때문에 중립적 관점을 유지합니다.",
      "key_companies": ["브로드컴", "구글", "마벨"],
      "insight": "AI 반도체 시장이 엔비디아/브로드컴 중심의 독점 국면에서 개별 맞춤형 칩(ASIC)의 멀티 공급망으로 다변화되고 있습니다. 독점 프리미엄 축소에 따른 단기 조정 이후, 신규 참여자(마벨, 인텔 등)의 수혜가 커지는 변화에 주목해야 합니다.",
      "action_point": "브로드컴의 독점 비중 노출을 줄이고, 다각화 수혜주인 마벨 테크놀로지 및 대만/한국의 디자인하우스 및 파운드리 대장주로 자산을 분산하여 위험을 헷징해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["브로드컴쇼크", "구글TPU", "멀티벤더전략", "AI반도체조정", "디자인하우스", "월텍남"]
    }
  },
  "WSyUnaJZMQA": {
    "primary": "stock",
    "video": {
      "id": "WSyUnaJZMQA",
      "title": "지금 당장 '가지치기' 할 종목?...주도주에 2등, 3등은 없다!ㅣ홍선애, 박병창 MP파트너스 대표 [여의도 인사이트]",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=WSyUnaJZMQA",
      "thumbnail": "https://img.youtube.com/vi/WSyUnaJZMQA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "주도 장세의 후기 국면으로 갈수록 실적이 검증되는 1등 주도 대형주에만 자금이 유입되며, 경쟁력이 없는 2등/3등 후발 기업들은 철저히 소외되는 양극화가 심화되고 있습니다. 무분별한 종목 백화점식 투자 대신 주도 섹터의 핵심 대장주로 포트폴리오를 '가지치기'하여 슬림화해야 할 시점임을 강조합니다.",
      "key_claims": [
        "시장의 유동성이 금리/환율 불안으로 타이트해질수록, 가격 전가력을 가진 1등 기업으로만 쏠리는 승자독식(Winner-take-all) 현상이 뚜렷하다.",
        "반도체, 전력기기 등 주도 섹터 내부에서도 HBM 선두주자 및 초고압 변압기 대장주 외의 후발 부품사들은 이윤율 차이로 주가 차별화가 심해진다.",
        "개인의 연금 유입 수급이 대형 지수 및 대표 우량주 위주의 ETF로만 편중되어 중소형 후발주들의 유동성 고갈이 지속되고 있다."
      ],
      "data_points": [
        "주요 업종 내 1등 기업과 2/3등 후발주 간의 영업이익률(OPM) 및 멀티플 갭 지속 확대"
      ],
      "signal": "neutral",
      "signal_reason": "지수의 상방은 열려 있으나 개별 종목별 양극화가 극심해지므로, 무분별한 분산투자보다 포트폴리오 슬림화 관리가 유일한 생존 전략이기 때문입니다.",
      "key_companies": ["삼성전자", "SK하이닉스", "효성중공업"],
      "insight": "강세장의 성숙기에는 '싸다고 후발주를 사는 실수'를 범해서는 안 됩니다. 1등 기업의 독점 Moat와 실적 증명이 더욱 부각되며, 후발주들은 단가 전가 능력 부재로 마진 스퀴즈를 겪어 소외될 뿐입니다.",
      "action_point": "포트폴리오를 재점검하여 주도 섹터 내 2등, 3등 한계 기업 및 실적이 찍히지 않는 테마성 중소형주를 과감히 정리(가지치기)하고, 1등 대장주 및 대표 패시브 ETF로 자금을 압축 배치해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["주도주집중", "가지치기전략", "양극화장세", "승자독식", "포트폴리오슬림화", "박병창", "삼프로TV"]
    }
  },
  "zOUUFrMGwEg": {
    "primary": "tech",
    "video": {
      "id": "zOUUFrMGwEg",
      "title": "모든 AI 병목에 NVIDIA가 있다 | 젠슨황 키노트 발표에 AI 투자의 흐름이 보인다",
      "published": "2026-06-04T00:00:00+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=zOUUFrMGwEg",
      "thumbnail": "https://img.youtube.com/vi/zOUUFrMGwEg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "대만 컴퓨텍스에서 젠슨 황 엔비디아 CEO의 키노트를 분석하여, 모든 AI 하드웨어 연산 병목(Bandwidth, Interconnect, Power, Cooling)에 엔비디아가 제시하는 규격과 패키징 솔루션이 표준으로 고착화되고 있음을 조명합니다.",
      "key_claims": [
        "엔비디아는 단순 GPU 칩 설계가 아니라 네트워킹(InfiniBand, Spectrum-X)과 초고속 상호연결(NVLink)을 장악해 연산 병목을 해결하고 있다.",
        "블랙웰(Blackwell) 플랫폼 및 차세대 로드맵(Rubin)은 온칩 HBM 탑재를 늘려 대역폭 한계를 돌파하며, 액체 냉각(Liquid Cooling) 규격을 수립하고 있다.",
        "인터커넥트 및 네트워킹 스위치 칩 시장에서 엔비디아의 생태계 지배력이 더욱 강화되어 경쟁사들의 침투 장벽을 높였다."
      ],
      "data_points": [
        "블랙웰 및 차세대 루빈(Rubin) 플랫폼의 차기 HBM 탑재량 증가 로드맵 공식 발표"
      ],
      "signal": "bullish",
      "signal_reason": "AI 하드웨어 가속기뿐만 아니라 네트워크, 스위치, 인터커넥트 인터페이스 표준 전체를 엔비디아가 선제 규정하여 장기 독점력을 강화하고 있습니다.",
      "key_companies": ["NVIDIA", "SK하이닉스"],
      "insight": "엔비디아의 진짜 해자는 GPU 코어가 아니라 칩과 칩을 이어 붙이는 NVLink 및 네트워킹 하이브리드 인터페이스 규격입니다. 모든 AI 인프라 병목을 자사 생태계로 해결해 주는 한, 일극 체제 지배력은 공고합니다.",
      "action_point": "엔비디아의 블랙웰/루빈 패키징 규격(액체 냉각, 고성능 HBM, 고대역 네트워킹)에 필수 기자재 및 부품을 독점 납품하는 글로벌 1등 공급망 지분을 홀딩해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["젠슨황키노트", "블랙웰", "루빈플랫폼", "NVLink", "네트워킹", "AI병목", "안될공학"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["video"], info["analysis"], info["classification"])
print("ALL BATCH 9 VIDEOS SUCCESSFULLY SAVED!")
