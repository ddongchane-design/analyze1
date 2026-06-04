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
  "ttnmPY9P_1k": {
    "primary": "stock",
    "video": {
      "id": "ttnmPY9P_1k",
      "title": "[속보효] Computing is Revenue 관점에서 본 BTC 급락과 Optical 급등",
      "published": "2026-06-03T07:30:00+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=ttnmPY9P_1k",
      "thumbnail": "https://img.youtube.com/vi/ttnmPY9P_1k/hqdefault.jpg"
    },
    "analysis": {
      "summary": "주식 시장의 쏠림 현상이 극대화되는 가운데 HP 실적 서프라이즈와 마벨의 3.6배 폭등 등 광통신(Optical) 및 AI 인프라 수혜주에 돈이 집중되고 있습니다. 반면, 구글은 자사주 매입 대신 $800억 규모 유상증자(AI 설비투자 자금 조달)로 선회했고, AI 도입으로 인한 개발 효율화 덕분에 개발자 채용이 오히려 늘어나는 <span class=\"text-amber-300 font-bold\">제본스의 역설</span>(Jevons Paradox)이 확인되고 있습니다.",
      "key_claims": [
        "S&P 500은 사상 최고치를 경신 중이나 200일선 상회 종목 비중은 급감해 극소수 AI 인프라주 중심의 양극화가 심화되고 있다.",
        "구글이 주주 환원(자사주 매입)을 멈추고 대규모 유상증자를 통해 AI 설비투자를 강화하는 것은 자본 흐름의 역사적 변곡점이다.",
        "AI 툴 도입이 개발 비용을 낮춤에 따라 기업들이 더 많은 신규 IT 프로젝트에 착수하며 개발자 채용 공고(JOLTS)가 오히려 반등하고 있다."
      ],
      "data_points": [
        "마벨 테크놀로지 주가 등락: 3월 $80에서 현재 $290대로 급등",
        "구글(알파벳) 자본 조달 규모: 800억 달러",
        "시장 전체 200일선 상회 주식 비중과 S&P 500 지수 간의 강력한 디커전스 발생"
      ],
      "signal": "bullish",
      "signal_reason": "전체 시장의 지표 확산세는 나쁘지만, AI 팩토리 효율성에 실질적으로 기여하는 광통신/네트워크 칩 설계 대형주(마벨 등) 및 핵심 하드웨어 밸류체인의 이익 성장세는 압도적입니다.",
      "key_companies": [
        "구글",
        "엔비디아",
        "마벨",
        "HP"
      ],
      "insight": "구글의 $800억 증자는 빅테크들이 주주 눈치를 보며 현금을 쟁여두는 시기가 끝났고, 엔비디아 GPU를 1장이라도 더 사기 위해 '유상증자 주주 희석'마저 감수해야 하는 생존 전쟁에 돌입했음을 말해줍니다. 또한 개발자 채용 증가라는 현상은 AI 경량화가 오히려 수요의 기하급수적 팽창을 낳는 제본스의 역설을 명확히 실증합니다.",
      "action_point": "단순 지수 추종 인덱스 펀드보다, AI 병목 현상을 해소하여 실질적 영업이익률 성장을 증명해 내는 맞춤형 반도체(ASIC) 설계 및 광통신 네트워크 인프라 대장주에 압축 대응해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["제본스의역설", "구글유상증자", "마벨폭등", "양극화장세", "AI인프라", "개발자채용", "이효석"]
    }
  },
  "2NWfGeg4blE": {
    "primary": "crypto",
    "video": {
      "id": "2NWfEeg4blE",
      "title": "아틀라스 마케팅, 어떻게 할까?",
      "published": "2026-06-03T08:00:00+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=2NWfGeg4blE",
      "thumbnail": "https://img.youtube.com/vi/2NWfGeg4blE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "비트코인이 최고점($12.6만) 대비 50% 수준인 6만 5천 달러 선까지 이탈하고 현물 ETF 유동성 유입이 멈춘 심리적 침체기를 극복하기 위한 투자 마인드셋을 조언합니다. AI 팩토리 랠리(젠슨 황의 'Computing is Revenue')로 인해 전통적인 크립토 전용 연산 유동성이 AI 인프라 칩으로 대거 이탈하고 있으며, 2019년 크립토 윈터 당시와 유사한 AI 개발군으로의 자금 및 인력 유출이 지속되고 있습니다.",
      "key_claims": [
        "비트코인 spot ETF 자금이 일주일 넘게 순유출로 돌아서며 리테일 및 기관 투자자들의 관심이 극도로 저하되었다.",
        "과거 비트코인 전유물이었던 '연산 연동 가치 창출(Computing is Money)' 주도권이 엔비디아 AI 토큰 팩토리 생산 프레임에 완전히 압도당했다.",
        "현물 매수 거래 부재 속에서 사소한 매도 뉴스(MSTR 32 BTC 매도 등)가 시장 선물 청산 체인을 건드려 과도한 하락을 부채질하고 있다."
      ],
      "data_points": [
        "비트코인 최고가: 126,000달러 (작년 10월)",
        "현 가격대: 65,000달러 수준 (최고점 대비 약 48%~50% 조정)",
        "과거 최저 가격대: 2월 60,000달러 이하 터치"
      ],
      "signal": "bearish",
      "signal_reason": "비트코인 현물 ETF 유입세 중단 및 가상자산 내부의 유동성 소외, AI 인프라 주로의 자금 청소기식 유출이 겹쳐 단기 가격 회복을 이끌 핵심 주체가 부재합니다.",
      "key_companies": [
        "마이크로스트레티지",
        "엔비디아"
      ],
      "insight": "AI 인프라의 폭발적인 성장 스토리는 비트코인이 지녔던 '유일한 연산 대안 자산' 지위를 흔들고 있습니다. 하지만 2019년 크립토 윈터 시기에 개발자들이 대거 AI로 탈블(탈블록체인)했다가 다시 상승 사이클을 맞이했던 것처럼, 현재의 극단적인 자금 소외 국면은 장기 관점의 크립토 포지션 구축에 적당한 조율기가 될 수 있습니다.",
      "action_point": "단기적인 가상자산 바닥 확인 전까지 무리한 롱 레버리지 포지션을 지양하고, 현물 ETF 유입 반전 신호가 포착되기 전까지 비트코인 현물 위주의 긴 호흡 분할 매수 적립식 대응이 안전합니다."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": ["stock"],
      "tags": ["비트코인조정", "ETF유출", "크립토윈터비교", "투자마인드셋", "연산패권이동", "유동성소외"]
    }
  },
  "hnjYNLrj-p4": {
    "primary": "stock",
    "video": {
      "id": "hnjYNLrj-p4",
      "title": "젠슨 황 방한 디데이! 진짜 수혜는요... | 이권희 위즈웨이브 대표 [글로벌 인터뷰]",
      "published": "2026-06-03T09:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=hnjYNLrj-p4",
      "thumbnail": "https://img.youtube.com/vi/hnjYNLrj-p4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "최근 코스피가 8,800선까지 급등함에 따라 50일 이평선 이격도(130 초과) 과열 리스크를 해소하기 위한 속도 조절(기술적 조정) 국면에 진입했습니다. 그럼에도 골드만삭스는 한국의 5월 반도체, 화장품, 자동차 전방위 수출 데이터 호조를 기반으로 코스피 이익 전망치를 상향하며 목표 지수를 12,000포인트로 대폭 격상했습니다.",
      "key_claims": [
        "코스피 지수는 단기 과열로 인해 이평선 이격도가 130 이상으로 벌어져 차익 실현 및 속도 조절 조정이 필연적인 상태였다.",
        "골드만삭스는 한국의 탄탄한 수출 동향(반도체, 화장품, 자동차)을 근거로 코스피 목표치를 9,000에서 12,000으로 올렸다.",
        "레버리지 상품 증가와 외국인 프로그램 알고리즘 매매로 인해 1분 30초 만에 2조 5천억 원의 매물이 쏟아지는 등 단기 변동성이 극대화되고 있다."
      ],
      "data_points": [
        "코스피 저점 종가 (3월 31일): 5,052포인트",
        "코스피 최고점 수준: 약 8,800포인트",
        "골드만삭스 코스피 목표치 전망: 기존 9,000에서 12,000포인트로 상향",
        "장중 알고리즘 매도 기록: 1분 30초 만에 약 2조 5,000억 원 출회"
      ],
      "signal": "bullish",
      "signal_reason": "단기적인 알고리즘 매도에 의한 지수 출렁임은 있으나, 반도체를 위시한 한국 수출 대형주들의 5월 무역수지 흑자 및 이익 가시성이 훼손되지 않아 중장기 12,000포인트 상승 동력은 탄탄합니다.",
      "key_companies": [
        "삼성전기",
        "삼성전자",
        "SK하이닉스"
      ],
      "insight": "현재 한국 증시는 'K-밸류업' 동력과 맞물린 수출 턴어라운드의 초입입니다. 알고리즘 매매로 인한 장중 2조 원대 폭탄 매물 출회는 리테일 투자자들에게 극심한 패닉을 주지만, 외국계 은행(골드만)이 이익 전망치를 지속 상향하는 근거는 반도체 가격 회복과 대외 부품 지배력이라는 튼튼한 펀더멘탈에 근거합니다.",
      "action_point": "프로그램 매도로 지수가 급락할 때 패닉 셀링에 가담하지 말고, 지수 50일 이평선 터치 등 과열이 해소되는 시점에 실적 가시성이 가장 뚜렷한 반도체 대형주 및 수출 우량주를 저가 매수해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["코스피12000", "골드만삭스", "수출데이터", "알고리즘매매", "이격도과열", "속도조절", "변동성완화"]
    }
  },
  "CBDFYQ-s3MM": {
    "primary": "economy",
    "video": {
      "id": "CBDFYQ-s3MM",
      "title": "비트코인 6만5천불까지 밀렸다가 반등ㅣ골드만, 코스피 목표치 1만2000ㅣ스페이스X 공모가 135달러 고정 보도ㅣ홍키자의 매일뉴욕",
      "published": "2026-06-03T11:20:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=CBDFYQ-s3MM",
      "thumbnail": "https://img.youtube.com/vi/CBDFYQ-s3MM/hqdefault.jpg"
    },
    "analysis": {
      "summary": "달러 인덱스 상승(99 돌파) 및 원달러 환율의 1,530원 돌파 등 거시 금융 불안 요소 속에서, 미-이란 종전 협상을 둘러싼 트럼프의 '핵무기 포기 합의 성공' 발언과 실제 중동 현장의 드론 도발(이란의 쿠웨이트/바레인 미군 기지 미사일 공격)이 격렬하게 대립하고 있습니다. 한편 주문형 반도체(ASIC) 업계의 1인자인 <span class=\"text-cyan-300 font-semibold\">브로드컴</span>의 실적 발표를 앞두고 구글 TPU 협력사인 브로드컴 및 마벨의 주가 동향에 관심이 쏠리고 있습니다.",
      "key_claims": [
        "원달러 환율이 야간 거래 중 1,530원을 돌파하여 국내 수입 물가와 유가 상승 압박을 증폭시키고 있다.",
        "트럼프는 이란이 핵무기를 갖지 않기로 합의했다고 워딩했으나, 이스라엘의 헤지볼라 공습과 이란의 바레인 5함대 드론 공격으로 호르무즈 긴장은 최고조에 달했다.",
        "구글의 독자 AI 칩인 TPU 설계/제작 파트너인 브로드컴의 실적이 향후 AI 주문형 반도체 밸류체인의 판도를 규정하는 리트머스지가 될 것이다."
      ],
      "data_points": [
        "달러 인덱스 수준: 99 돌파",
        "원달러 환율 최고점: 1,530원 돌파",
        "스페이스X 기업 공개 규모: 주당 135달러, 총 750억 달러 조달 목표 (시총 1.8조 달러)",
        "마벨 테크놀로지 장전 주가 등락률: +11%"
      ],
      "signal": "bearish",
      "signal_reason": "1,530원대 돌파라는 파국적인 원화 약세와 중동의 미사일 도발 실질 격화, 그리고 차기 연준 케빈 워시의 등장에 따른 고금리 장기화 우려가 대외 금융 여건을 짓누르고 있습니다.",
      "key_companies": [
        "브로드컴",
        "마벨",
        "구글",
        "스페이스X"
      ],
      "insight": "트럼프가 네타냐후 총리에게 격렬한 욕설을 퍼부으며 종전 협상에 목을 매는 이유는 대선 전 유가 안정과 성과를 내기 위함입니다. 하지만 실제 쿠웨이트 공항 사망 사태 등 지정학적 파국이 진행되고 있어 시장은 트럼프의 구두 개입 효과를 유보하며 보수적 리스크 오프 상태로 회귀하고 있습니다.",
      "action_point": "환율 급등에 따른 원화 자산 리스크를 헷징하기 위해 미국 내 확실한 캐시카우 독점 기업 지분과 배당 가치주 중심의 달러 자산 비중을 탄탄히 유지해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["원달러환율1530원", "트럼프이란합의", "중동드론공격", "네타냐후갈등", "브로드컴실적대기", "달러인덱스"]
    }
  },
  "CpIWbqtyh30": {
    "primary": "crypto",
    "video": {
      "id": "CpIWbqtyh30",
      "title": "비트코인 7만달러 이탈 급락ㅣ플루언스에너지, 엔비디아 데이터센터 설계 참여ㅣ구글, AI 인프라 위해 $800억 자본조달 계획ㅣ홍키자의 매일뉴욕",
      "published": "2026-06-03T11:30:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=CpIWbqtyh30",
      "thumbnail": "https://img.youtube.com/vi/CpIWbqtyh30/hqdefault.jpg"
    },
    "analysis": {
      "summary": "비트코인 7만 달러 붕괴의 심층 원인으로 AI/반도체 주로의 글로벌 유동성 쏠림(진공청소기 효과)과 미국 CFTC의 파생상품 규제 완화에 따른 선물/옵션 시장 쏠림을 지목합니다. 이에 따라 코인베이스(COIN) 매도 리포트가 출회되었으며, 대외적으로는 구글의 AI 인프라 $800억 자금 조달 및 <span class=\"text-cyan-300 font-semibold\">플루언스 에너지</span>(Fluence Energy)의 엔비디아 데이터센터 설계 참여 소식 등 실적이 증명되는 AI 하드웨어 자산으로의 자본 대이동이 일어나고 있습니다.",
      "key_claims": [
        "비트코인 현물 ETF에서 3주간 $30억이 유출되었으며, 이는 실적 성장이 입증되는 AI/반도체 인프라 주식으로 자금이 이탈한 결과다.",
        "미국 금융기관들이 규제가 빡빡한 코인 현물 보관 대신 전통 증권 계좌 내 선물/옵션으로 거래 수단을 변경해 현물 거래소(코인베이스)의 호가가 메말랐다.",
        "매수 대기 물량이 바닥난 상태에서 MSTR의 소량(32 BTC) 매도와 마운트곡스 지갑 이동 뉴스가 트리거가 되어 1억 3천만 달러 규모의 롱 포지션 강제 청산을 촉발했다."
      ],
      "data_points": [
        "비트코인 현물 ETF 3주간 자금 순유출 규모: 30억 달러 (약 4조 원 이상)",
        "24시간 기준 비트코인 강제 청산 금액: 1억 3,000만 달러 (이 중 96%가 롱 포지션)",
        "구글 AI 인프라 구축 목표 자금 조달액: 800억 달러",
        "코인베이스 목표가 및 투자 의견 하향: 목표가 140달러로 하향 및 매도 리포트 출회"
      ],
      "signal": "bearish",
      "signal_reason": "가상자산 내부의 선물 쏠림으로 인한 가격 변동성 증폭과 코인 거래소들의 수수료 수입 구조 붕괴 경고, 그리고 AI 가속기 공급망으로의 블랙홀식 유동성 유출이 겹쳐 단기 회복이 제한적입니다.",
      "key_companies": [
        "코인베이스",
        "마이크로스트레티지",
        "구글",
        "플루언스에너지"
      ],
      "insight": "과거에는 '기술주 상승 = 비트코인 상승' 동조화가 나타났으나, 이제는 실적 가시성이 뚜렷한 AI 하드웨어와 전력 인프라(플루언스 에너지 등)가 시장의 모든 유동성을 독식하는 '유동성 제로섬 게임' 양상입니다. 특히 코인베이스 매도 리포트는 전통 금융 자본이 파생 거래를 통해 크립토 현물 거래소의 중개 해자를 합법적으로 약화시키고 있음을 명백히 보여줍니다.",
      "action_point": "코인베이스(COIN) 및 고레버리지 크립토 파생 포지션의 노출을 줄이고, 전력 인프라 및 AI 데이터센터 에너지 설계 강자인 플루언스 에너지(FLNC) 등 실적이 확실한 AI 공급망 핵심주 위주로 자산을 재배치해야 합니다."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": ["stock", "tech"],
      "tags": ["비트코인폭락", "롱청산폭탄", "코인베이스매도리포트", "유동성블랙홀", "플루언스에너지", "구글800억달러", "파생상품이동"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["video"], info["analysis"], info["classification"])
