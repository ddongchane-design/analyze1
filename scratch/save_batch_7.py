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
  "SPXhamNPf6Q": {
    "primary": "economy",
    "video": {
      "id": "SPXhamNPf6Q",
      "title": "(1부) 이란 전쟁 오늘 끝나도 유가 9월까지 뛴다 (COR에너지인사이트 권효재 대표)｜2026년 06월 01일 녹화",
      "published": "2026-06-02T07:55:07+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=SPXhamNPf6Q",
      "thumbnail": "https://img.youtube.com/vi/SPXhamNPf6Q/hqdefault.jpg"
    },
    "analysis": {
      "summary": "중동 지정학적 위기가 실질적인 물류 마찰로 전이되며, <span class=\"text-amber-300 font-bold\">유가</span>와 석유 제품 가격의 상승 압력이 장기화되고 있습니다. 특히 호르무즈 해협을 우회하는 해상 운송로의 물리적 시차(3~4개월)로 인해, 설령 오늘 <span class=\"text-violet-300 font-medium\">이란</span>과의 전쟁이 종식되더라도 공급망 정상화 시점인 9월까지는 고유가 기조가 유지될 전망입니다.",
      "key_claims": [
        "호르무즈 해협 우회로 인한 유조선 운송 거리 증가로 해상 물류의 공급망 지연 및 운임 급등이 유발되었다.",
        "국내 수입 석유 제품 가격은 싱가포르 현물 가격과 연동되는데, 공급망 시차로 인해 약 3~4개월의 가격 지연 반영(Lag time)이 발생한다.",
        "미국의 셰일 오일 증산에도 불구하고 경질유 중심 공급이어서 정제 마진이 높은 중질유 제품군의 숏티지는 해소되기 어렵다."
      ],
      "data_points": [
        "해상 운임 및 석유 제품(휘발유/항공유 등) 가격: 이전 대비 약 100% 상승",
        "공급망 우회로 인한 물리적 운송 소요 시차: 최소 3~4개월"
      ],
      "signal": "bearish",
      "signal_reason": "유가 상승 및 운송 마찰 장기화는 글로벌 제조업의 인플레이션 압력을 다시 고조시키며, 각국 중앙은행의 <span class=\"text-amber-300 font-bold\">금리 인하</span> 시점을 늦추는 강력한 매크로 악재입니다.",
      "key_companies": [
        "SK이노베이션",
        "S-Oil"
      ],
      "insight": "지정학적 협상 타결이라는 정치적 뉴스만으로 유가 하락을 예단해서는 안 됩니다. 해운 물류의 병목은 물리적 거리가 늘어난 만큼의 톤-마일(Ton-mile) 증가를 야기하며, 이는 유통 공급망 전체에 최소 한 분기 이상의 시차를 두고 누적 가격 상승을 유발하는 구조적 요인입니다.",
      "action_point": "원자재 및 에너지 운송 비중이 높은 해운/물류주 및 정제 마진 수혜가 기대되는 정유 대형주 위주로 단기 헤지 포지션을 설정하고, 유가 연동 비용 부담이 큰 화학/항공 업종의 비중을 축소해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["energy", "etc"],
      "tags": ["유가상승", "호르무즈해협", "지정학적리스크", "이란전쟁", "공급망지연", "석유제품", "언더스탠딩"]
    }
  },
  "KdLZthSQ_kA": {
    "primary": "stock",
    "video": {
      "id": "KdLZthSQ_kA",
      "title": "금리 인상 우려 속 사모신용 불안…비트코인 급락세, 유동성 이슈 부각 [월가 뉴스레터]",
      "published": "2026-06-03T22:20:05+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=KdLZthSQ_kA",
      "thumbnail": "https://img.youtube.com/vi/KdLZthSQ_kA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "매크로 지표 강세에 따른 <span class=\"text-amber-300 font-bold\">고금리 장기화</span> 우려 속에서, 미국 사모신용(Private Credit) 시장의 연체율 상승 등 금융 불안 징후가 포착되었습니다. 주식 시장은 장 후반 <span class=\"text-rose-400 font-medium\">급락</span> 마감했으며, 코인 시장 역시 <span class=\"text-cyan-300 font-semibold\">코인베이스</span>의 매도 리포트와 선물 청산이 겹치며 <span class=\"text-rose-400 font-medium\">급락세</span>를 보였습니다.",
      "key_claims": [
        "고금리 장기화로 인해 은행 대체 금융인 사모신용 자산의 부실 채권 및 연체 리스크가 수면 위로 올라오고 있다.",
        "코인 시장은 기관들이 현물 매수 대신 장외 및 파생상품 시장으로 이탈하면서 현물 유동성이 급격히 말라 가격 변동성이 극대화되었다.",
        "장 마감 후 실적을 발표한 브로드컴과 크라우드 스트라이크는 양호한 성적에도 불구하고 단기 과열에 따른 차익 매물로 하락했다."
      ],
      "data_points": [
        "3대 지수 하락률: 다우 -1.2%, 나스닥 -0.9%, S&P500 -0.7%",
        "브로드컴 시간외 하락률: -6%",
        "크라우드 스트라이크 시간외 하락률: -10%"
      ],
      "signal": "bearish",
      "signal_reason": "금융 시장의 숨은 뇌관인 사모신용 불안과 빅테크들의 눈높이 과열 조정, 원달러 환율의 1,530원 돌파 등 리스크 오프 요인이 동시다발적으로 누적되고 있습니다.",
      "key_companies": [
        "코인베이스",
        "브로드컴",
        "크라우드스트라이크"
      ],
      "insight": "주식과 크립토 모두 단기 가격 상승에 따른 피로 누적 상태에서 매크로 경계감이 작용하고 있습니다. 특히 사모신용 리스크는 중소형 한계 기업들의 디폴트 위험을 높여 중소형주 위주의 러셀 2000 지수에 직접적인 타격을 줄 가능성이 큽니다.",
      "action_point": "단기 과열로 이격도가 벌어진 고밸류 빅테크 성장주 및 가상자산 관련주의 신규 진입을 자제하고, 현금 비중을 확보한 채 대형 가치주나 실적주 중심으로 방어 포트폴리오를 구성해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "crypto"],
      "tags": ["사모신용", "금리우려", "비트코인급락", "코인베이스", "브로드컴실적", "크라우드스트라이크", "삼프로TV"]
    }
  },
  "aaDNXBXXOH0": {
    "primary": "stock",
    "video": {
      "id": "aaDNXBXXOH0",
      "title": "코스피 1만포인트? 진짜 변수는 선거가 아니다 | 박병창 MP파트너스 대표",
      "published": "2026-06-03T00:04:15+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=aaDNXBXXOH0",
      "thumbnail": "https://img.youtube.com/vi/aaDNXBXXOH0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "국내 주식 시장이 퇴직연금(DB에서 DC/IRP로의 이전) 및 부동산 대기 자금의 머니무브에 힘입어 대형 <span class=\"text-amber-300 font-bold\">ETF 시대</span>로 본격 진입했습니다. 한국 증시의 총 운용자산(AUM)이 500조 원을 돌파하는 등 막강한 내수 기관화 자금이 유입되면서, 과거 외국인 수급에 전적으로 휘둘리던 천수답 장세에서 벗어나 지수의 하방 경직성을 강하게 지지하고 있습니다.",
      "key_claims": [
        "국내 주식 시장은 외국인 매도 공세보다 연금 자산의 구조적 유입에 따른 내수 유동성이 지수를 지탱하는 핵심 동력으로 부상했다.",
        "퇴직연금 내 주식형/자산배분형 ETF 편입 규정 변화가 코스피 대형주 및 밸류업 수혜주로의 지속적인 매수세를 창출하고 있다.",
        "선거 등 단기 정치적 이벤트보다 대형 펀드들의 자금 배분 및 구조적 연금 머니무브가 시장의 중장기 향방을 가른다."
      ],
      "data_points": [
        "한국 연금 및 예금 대기성 유동성 자산 규모: 약 500조 원 수준 추정",
        "개인 투자자들의 연금 계좌 내 주식/ETF 편입 비율 지속 증가세"
      ],
      "signal": "bullish",
      "signal_reason": "국내 증시의 수급 체질이 단순 개인 단기 매매에서 연금 기반의 장기 적립식 ETF 자본으로 변화하면서, 거시 위기 시 지수의 버팀목 역할을 든든히 해주고 있습니다.",
      "key_companies": [
        "삼성자산운용",
        "미래에셋자산운용"
      ],
      "insight": "서학개미와 부동산 쏠림으로 외면받던 국장이 자산배분형 퇴직연금(DC/IRP)의 의무 유입 채널을 확보하며 든든한 밑바탕을 마련했습니다. 지수형 대형 ETF와 밸류업 배당 ETF로의 안정적 자본 유입은 지수의 펀더멘탈을 한 단계 레벨업하는 밑거름이 될 것입니다.",
      "action_point": "외국인 수급에 따른 단기 변동성에 흔들리지 말고, 연금 계좌를 통해 배당 및 자산가치가 확실한 코스피 대표 밸류업 ETF 및 우량주를 꾸준히 분할 적립하는 전략이 유효합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["ETF시대", "퇴직연금", "머니무브", "코스피전망", "수급개선", "박병창", "삼프로TV"]
    }
  },
  "EboqEWatLV8": {
    "primary": "stock",
    "video": {
      "id": "EboqEWatLV8",
      "title": "반도체가 많아도, 주도주가 있어도 혹은 바이오에 울고 있어도 무조건 버티고 지켜볼 것 | 장우진 작가",
      "published": "2026-06-03T00:51:39+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=EboqEWatLV8",
      "thumbnail": "https://img.youtube.com/vi/EboqEWatLV8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "국내 증시가 초과적인 <span class=\"text-cyan-300 font-semibold\">반도체</span> 쏠림 현상으로 극단적인 양극화를 보이고 있으나, 6월 11일 선물옵션 동시만기일을 기점으로 소외되었던 비(非)반도체 섹터의 평균 회귀(Mean Reversion)가 나타날 가능성이 높습니다. 과도한 고점 추격 매수 대신 가격 매력이 돋보이는 자동차, 금융, 바이오 등 밸류업 및 낙폭과대 대형주에 대한 인내심 있는 보유 전략을 권고합니다.",
      "key_claims": [
        "한국 증시는 현재 반도체 및 특정 주도 섹터의 시가총액 비중이 극단적으로 쏠려 있어 기술적 피로감이 한계에 달했다.",
        "과거 경험상 이러한 쏠림 장세는 분기 만기일(6월 11일) 전후의 파생상품 포지션 청산과 함께 섹터 간 키 맞추기로 순환매가 전개된다.",
        "실적 개선세가 뚜렷함에도 주가수익비율(PER)이 지나치게 낮은 자동차 등 밸류업 종목들의 밸류에이션 매력이 부각될 시점이다."
      ],
      "data_points": [
        "주요 자동차/밸류업 종목 PER 수준: 약 5~7배 수준으로 저평가",
        "특정 반도체 및 테크 독점주 PER 수준: 50~65배 수준까지 상승",
        "6월 선물옵션 동시만기일: 2026년 6월 11일"
      ],
      "signal": "neutral",
      "signal_reason": "반도체의 장기 펀더멘탈은 굳건하나, 수급 과열에 따른 단기 숨고르기와 소외 섹터로의 순환매 흐름이 나타나 지수 자체는 박스권 등락을 보일 가능성이 큽니다.",
      "key_companies": [
        "현대자동차",
        "기아",
        "삼성전기"
      ],
      "insight": "주도주 쏠림의 정점에서는 공포감에 소외주를 매도하고 반도체 고점에 동참하는 우를 범하기 쉽습니다. 밸류에이션 매력과 배당 매력이 튼튼한 밸류업 섹터(자동차 등)는 결국 시장의 수급 균형이 맞춰지는 과정에서 가장 먼저 반등할 기초 체력을 지니고 있습니다.",
      "action_point": "포트폴리오 내 반도체 비중의 무리한 확대는 자제하고, 저PER 고배당 특성을 가진 자동차, 지주사, 그리고 실적이 동반되는 낙폭과대 헬스케어 대형주를 인내심 있게 홀딩하거나 저가 분할 매수해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["쏠림장세", "선물옵션만기일", "순환매", "밸류에이션", "현대차", "평균회귀", "삼프로TV"]
    }
  },
  "pcx-b_l2bQQ": {
    "primary": "tech",
    "video": {
      "id": "pcx-b_l2bQQ",
      "title": "만스피 가능하다? 핵심은 반도체 투자전쟁 | 김장열 유니스토리자산운용 리서치센터장",
      "published": "2026-06-03T01:21:12+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=pcx-b_l2bQQ",
      "thumbnail": "https://img.youtube.com/vi/pcx-b_l2bQQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "글로벌 빅테크 기업들이 AI 리더십을 잃지 않기 위해 유상증자까지 단행하며 설비투자(CAPEX)를 늘리는 '기호지세(호랑이 등에 탄 형국)'의 죄수의 딜레마에 처해 있습니다. 이는 메모리 및 AI 반도체 공급망을 장악한 한국 반도체 기업들에 사상 최대의 실적 수혜 환경을 제공하고 있으며, 코스피 지수의 장기 상승 잠재력을 대폭 끌어올리고 있습니다.",
      "key_claims": [
        "구글, 마이크로소프트 등 빅테크들은 주주 희석 우려에도 불구하고 생존을 위해 대규모 자금 조달을 통한 AI 인프라 투자를 지속할 수밖에 없다.",
        "메모리 반도체(HBM 및 고용량 DDR5) 가격 상승세와 빅테크의 공격적인 주문 증가로 국내 반도체 양사의 2분기 및 하반기 실적 전망치가 가파르게 상향되고 있다.",
        "코스피 지수가 역사적 고점을 뚫고 장기 상승하기 위해서는 반도체 업종의 이익 기여도가 절대적인 비중을 차지해야 한다."
      ],
      "data_points": [
        "구글의 AI 인프라 전용 자금 조달 계획 규모: 800억 달러",
        "메모리 고정거래가격 상승률 및 국내 HBM 점유율의 견조함 지속"
      ],
      "signal": "bullish",
      "signal_reason": "빅테크의 무한 설비투자 경쟁은 글로벌 반도체 장비 및 메모리 밸류체인에 장기적이고 확실한 매출 성장을 보장하는 최고의 촉매제입니다.",
      "key_companies": [
        "삼성전자",
        "SK하이닉스",
        "구글"
      ],
      "insight": "빅테크들의 CAPEX 투자는 이제 단순한 선택의 영역이 아니라 생존 게임입니다. 투자 규모가 커질수록 한국의 메모리 반도체 생태계(HBM, 고용량 eSSD 등)는 단가 협상력과 공급 지배력을 높여, 지수의 지속적인 우상향을 견인할 견고한 실적 해자를 확보하게 됩니다.",
      "action_point": "단기적인 환율 급등이나 거시 지표 흔들림으로 인한 반도체 대형주의 조정 발생 시, 이를 비중 확대 기회로 적극 활용하여 포트폴리오의 주축으로 유지해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock", "economy"],
      "tags": ["빅테크CAPEX", "죄수의딜레마", "반도체투자전쟁", "HBM", "코스피전망", "김장열", "삼프로TV"]
    }
  },
  "QeT-DeK5L2c": {
    "primary": "space",
    "video": {
      "id": "QeT-DeK5L2c",
      "title": "신이 주신 기회가 올 수 있습니다, 테슬라·스페이스X 합병이 무서운 이유ㅣ정주용 의장 [풀영상]",
      "published": "2026-06-03T08:00:21+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=QeT-DeK5L2c",
      "thumbnail": "https://img.youtube.com/vi/QeT-DeK5L2c/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">스페이스X</span>의 주당 $135 고정 IPO 추진 소식과 더불어, 저궤도 우주 영토 선점(스타링크) 및 17세기 네덜란드 동인도회사(VOC)에 비견되는 우주 독점 지배력의 가치가 재평가받고 있습니다. 나아가 미래에 <span class=\"text-cyan-300 font-semibold\">테슬라</span>와의 합병 시너지가 발휘될 경우 모빌리티와 우주 통신망이 결합된 독보적인 플랫폼 제국이 탄생할 것으로 전망됩니다.",
      "key_claims": [
        "스페이스X는 압도적인 발사체 재사용 기술을 바탕으로 경쟁사 대비 10배 이상 저렴한 비용 구조를 구축하여 저궤도 위성망을 사실상 독점하고 있다.",
        "일론 머스크의 우주 영토 선점은 단순한 통신 사업을 넘어, 지구 전체의 실시간 물리 데이터 및 자율주행 모빌리티 백본망을 통제하는 권력으로 진화하고 있다.",
        "스페이스X의 상장 가격 제시는 미국 개인 투자자들의 투자 열기를 극대화하고 있으며, 향후 테슬라와의 합병 시너지 루머가 주가 변동성을 이끌 수 있다."
      ],
      "data_points": [
        "스페이스X IPO 제시 가격: 주당 135달러 수준 고정 보도",
        "경쟁사 대비 스페이스X 발사당 비용 수준: 약 10분의 1 수준으로 저렴"
      ],
      "signal": "bullish",
      "signal_reason": "우주 인프라 및 스타링크의 독점력은 대체 불가능한 국가 안보급 인프라 자산으로 성장하고 있으며, 관련 밸류체인의 장기 성장 가치는 무궁무진합니다.",
      "key_companies": [
        "스페이스X",
        "테슬라"
      ],
      "insight": "스페이스X를 단순한 로켓 회사가 아닌 우주 시대의 '네덜란드 동인도회사'로 바라보아야 합니다. 스타링크의 글로벌 통신 인프라 독점은 미래 FSD 자율주행 및 휴머노이드 로봇 생태계의 전 지구적 통신 기지를 완성하는 마지막 퍼즐 조각이며, 테슬라와의 자산 통합 가능성은 엄청난 미래 밸류에이션 프리미엄을 정당화합니다.",
      "action_point": "국내 우주항공 관련 부품/안테나 강소기업 및 자율주행 통신 핵심 기술을 보유한 우량 밸류체인 기업들을 발굴하여 장기 포트폴리오로 편입해 나가는 전략이 바람직합니다."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["tech", "stock"],
      "tags": ["스페이스X", "스타링크", "테슬라합병", "우주항공", "동인도회사", "발사체기술", "이효석"]
    }
  },
  "ujT_gtB4lRA": {
    "primary": "etc",
    "video": {
      "id": "ujT_gtB4lRA",
      "title": "증상 없는 만성 염증 어느 날 '급사' 부른다 | 북언더스탠딩 | 착한 염증 나쁜 염증 | 서울대병원 이승훈 교수 | 2부",
      "published": "2026-06-02T12:25:25+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=ujT_gtB4lRA",
      "thumbnail": "https://img.youtube.com/vi/ujT_gtB4lRA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "현대인의 급사 원인 중 하나인 만성 염증의 위험성과 의학적 기전을 탐구하고, 과거 대규모 임상 연구(JUPITER, CANTOS)를 통해 입증된 항염증 치료제의 약가 책정 및 FDA 승인을 둘러싼 경제적 이해관계를 해설합니다. 특히 제약사의 고가 마케팅 전략과 국가 보건 재정 부담 간의 갈등 속에서 대체 저가 의약품(콜키신)의 재발견 사례를 통해 바이오 산업의 이면을 분석합니다.",
      "key_claims": [
        "만성 염증은 심혈관 질환 등 현대 성인병의 숨겨진 유발 요인으로, 자각 증상 없이 혈관 벽을 파괴하여 돌연사를 초래한다.",
        "노바티스의 만성 염증 치료제 캔에키누맙(CANTOS 임상)은 뛰어난 효능에도 불구하고 1년 약가 2천만 원이 넘는 고비용 구조로 인해 대중화 및 FDA 승인 과정에서 큰 장벽에 직면했었다.",
        "결국 보건 재정 수용성을 감안하여 값싼 기존 통풍 치료제인 콜키신을 저용량으로 재창출하는 방식이 심혈관 항염증 치료에 승인되는 반전이 일어났다."
      ],
      "data_points": [
        "캔에키누맙(Canakinumab) 연간 약가: 약 20,000달러 수준의 고가",
        "콜키신(Colchicine) 1정 가격: 수십~수백 원 수준의 매우 저렴한 가격대"
      ],
      "signal": "neutral",
      "signal_reason": "바이오/제약 산업은 임상적 효능뿐만 아니라 약가 책정과 국가 건강보험 재정 수용성이라는 경제학적 현실이 승인 여부를 좌우하는 복합적인 비즈니스 모델을 갖고 있습니다.",
      "key_companies": [
        "노바티스"
      ],
      "insight": "신약 개발의 위대함 뒤에는 '누가 비용을 감당할 것인가'라는 경제적 질문이 있습니다. 고가 바이오 의약품의 임상 성공이 곧장 주주 가치 극대화로 이어지지 않는 이유는 약가 승인을 지연시키는 정부와 보험사들의 강력한 예산 통제권 때문이며, 오히려 약물 재창출(Drug Repurposing)을 통한 저비용 대안이 시장의 선택을 받는 실리적 흐름이 커지고 있습니다.",
      "action_point": "신약 파이프라인의 단순 임상 결과에만 환호하지 말고, 해당 약물이 상용화될 때 보건당국이 승인할 수 있는 현실적인 약가 범위를 계산하여 바이오 투자 포지션을 조율해야 합니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["만성염증", "임상시험", "FDA승인", "약가결정", "노바티스", "콜키신", "의학경제학", "언더스탠딩"]
    }
  },
  "qQi3skDY6ns": {
    "primary": "stock",
    "video": {
      "id": "qQi3skDY6ns",
      "title": "[빈난새의 개장전요것만-6월3일] 트럼프 \"하메네이 만나고파\" | 스페이스X 상장이 다른점 | 비트코인 약세 이유 | 마벨 인텔 팔로알토 샌디스크 메타 IBM 이리듐 애플 아이렌",
      "published": "2026-06-03T14:43:55+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=qQi3skDY6ns",
      "thumbnail": "https://img.youtube.com/vi/qQi3skDY6ns/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국의 5월 ADP 민간고용이 예상치(12만 개)를 웃돈 12만 2천 개로 집계되며 여전히 견조한 고용 시장을 입증했습니다. 중동에서는 <span class=\"text-violet-300 font-medium\">이란</span> 혁명수비대가 <span class=\"text-violet-300 font-medium\">쿠웨이트</span>와 <span class=\"text-violet-300 font-medium\">바레인</span> 내 미군 기지를 드론으로 타격하며 지정학적 불안을 자극했고, 반도체 부문에서는 <span class=\"text-cyan-300 font-semibold\">구글</span>의 자체 네트워킹 칩을 <span class=\"text-cyan-300 font-semibold\">마벨</span>이 설계하고 <span class=\"text-cyan-300 font-semibold\">인텔</span>이 18A 공정 파운드리로 수주할 것이라는 메가톤급 루머가 유입되었습니다.",
      "key_claims": [
        "5월 ADP 민간고용 호조로 인플레이션 우려 및 고금리 장기화 네러티브가 다시 강화되며 채권 시장 경계감이 높아졌다.",
        "미국이 호르무즈 해협 우회 유조선 탈출을 지원하는 프로젝트 프리덤을 재개하자, 이란이 미군 기지를 직접 보복 타격하여 충돌이 격화되었다.",
        "구글 자체 AI 가속기(TPU)의 네트워크 칩 협업 루머로 마벨이 장중 급등하고 인텔 파운드리 신뢰도가 급증하고 있다."
      ],
      "data_points": [
        "5월 ADP 민간 고용 지표: 122,000명 증가 (예상 120,000명 상회)",
        "마벨 주가 등락: 루머 영향으로 장중 +10% 이상 급등",
        "인텔 주가 등락: 18A 파운드리 수주 루머로 +6% 이상 급등"
      ],
      "signal": "neutral",
      "signal_reason": "빅테크 칩 협력 루머 등 개별 테크 호재가 돋보이나, 중동 전쟁의 전면전 위기 고조와 탄탄한 고용 지표에 따른 고금리 압박이 시장 상방을 제한하고 있습니다.",
      "key_companies": [
        "마벨",
        "인텔",
        "구글",
        "스페이스X"
      ],
      "insight": "구글-마벨-인텔의 삼각 협업 루머는 엔비디아의 AI 하드웨어 독점을 견제하려는 빅테크 진영의 몸부림을 나타냅니다. 인텔의 18A 공정이 구글 칩 제작에 실질적으로 채택된다면, 이는 대만 파운드리 의존도를 낮추고 미국 중심의 공급망 자립을 이루려는 정치적/경제적 이정표가 될 것입니다.",
      "action_point": "인텔 파운드리 18A 성과를 지속적으로 추적하고, 글로벌 ASIC(주문형 반도체) 생태계에서 독보적인 가교 역할을 하는 설계 자산(IP) 및 디자인하우스 기업들을 선별하여 투자 비중을 늘려야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech", "crypto"],
      "tags": ["ADP민간고용", "이란보복타격", "프로젝트프리덤", "구글자체칩", "마벨설계", "인텔18A", "스페이스X공모가", "한경글로벌마켓"]
    }
  },
  "AxXsOzux7zQ": {
    "primary": "energy",
    "video": {
      "id": "AxXsOzux7zQ",
      "title": "(2부) 싼 전기 시대 끝났다, 프랑스·독일의 미친 결정 (COR에너지인사이트 권효재 대표)｜2026년 06월 01일 녹화",
      "published": "2026-06-03T07:55:04+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=AxXsOzux7zQ",
      "thumbnail": "https://img.youtube.com/vi/AxXsOzux7zQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "유럽의 에너지 전환이 물리적 병목과 고비용 장벽에 부딪히자, 독일은 해상풍력 인허가 기간을 4년에서 1년으로 단축하는 초법적 신속 법안을 가결했습니다. 이는 재생에너지 인프라 구축의 급박함을 반증하며, 저가 패널 등 일반 제조업(하드웨어)을 장악한 중국과의 경쟁을 피해 전력망 안정화(Grid Stabilization) 및 가상발전소(VPP) 시스템 소프트웨어를 장악하려는 서방 기업(<span class=\"text-cyan-300 font-semibold\">지멘스</span>, <span class=\"text-cyan-300 font-semibold\">ABB</span> 등)의 고부가가치 시스템 베팅을 보여줍니다.",
      "key_claims": [
        "독일은 원전 폐기 이후 치솟는 소매 전기료 고통을 재생에너지의 급속 보급을 통한 원료비 제로(0)화로 돌파하고자 한다.",
        "태양광 패널 등 범용 하드웨어 제조는 중국이 압도하고 있으나, 수백만 분산 전원을 통합 관리하는 전력망 관리 하드웨어 및 소프트웨어 분야는 안보 이슈로 중국 침투가 불가능하다.",
        "독일은 지붕 태양광과 가정용 ESS 네트워크를 VPP(가상발전소) 주체로 활용하여 실시간 전력 거래 및 다이내믹 프라이싱을 고도화하고 있다."
      ],
      "data_points": [
        "독일 해상풍력 인허가 심사 기간 단축 법안: 기존 4년에서 1년으로 대폭 단축 가결",
        "독일의 루프탑 태양광 보급률: 한국 대비 약 20배 수준의 고밀도 보급"
      ],
      "signal": "bullish",
      "signal_reason": "송배전망의 급격한 노후화와 재생에너지 전력 불안정성으로 인해, 전력망 안정화 제어 솔루션 및 에너지 저장 장치(ESS) 인프라 기업들의 장기 이익 성장세가 매우 뚜렷합니다.",
      "key_companies": [
        "지멘스",
        "ABB",
        "효성중공업",
        "LS일렉트릭"
      ],
      "insight": "태양광 패널 제조 단가 싸움에서 중국에 패배한 서방 국가들은 '전력 시스템 제어 및 안정화 소프트웨어'라는 안보 장벽 뒤에 숨은 캐시카우 산업에 올인하고 있습니다. 재생에너지가 늘어날수록 전력망 난이도가 기하급수적으로 올라가며, 전력 공급망 전체를 최적화하는 VPP 솔루션과 초고압 송전 시스템을 쥔 자들이 최후의 승자가 될 것입니다.",
      "action_point": "단순 신재생 발전(태양광/풍력) 업체 투자보다, 국가적 인프라 투자의 본질인 전력망 안정화 핵심 기기 제조사(초고압 변압기 등) 및 스마트 그리드 관리 플랫폼 기업에 압도적인 비중을 두어야 합니다."
    },
    "classification": {
      "primary_topic": "energy",
      "secondary_topics": ["economy", "tech"],
      "tags": ["독일해상풍력", "인허가단축", "전력망안정화", "스마트그리드", "지멘스", "ABB", "VPP", "언더스탠딩"]
    }
  },
  "ooyhI2HDUY8": {
    "primary": "stock",
    "video": {
      "id": "ooyhI2HDUY8",
      "title": "[26.06.03 오전 방송 전체보기] AI발 상승세 지속, 뉴욕증시 5일째 최고가...마벨 +33% 급등, 왜?",
      "published": "2026-06-03T00:08:36+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=ooyhI2HDUY8",
      "thumbnail": "https://img.youtube.com/vi/ooyhI2HDUY8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">구글</span>이 AI 데이터센터 설비투자 재원 확보를 위해 부채 대신 주주 지분이 희석되는 $800억 규모 대규모 유상증자 결정을 내렸습니다. 이례적인 주식 발행 딜에 워런 버핏의 후계자 그렉 아벨이 이끄는 <span class=\"text-cyan-300 font-semibold\">버크셔 해서웨이</span>가 $100억 규모 참여 의사를 밝히며 신뢰를 더했고, 대외적으로는 미국의 5월 구인 건수(JOLTS) 상승으로 견조한 경기 연착륙 기대감이 높아졌습니다. 한편, 미국의 반도체 수출 통제 속에서 <span class=\"text-cyan-300 font-semibold\">화웨이</span>가 칩을 겹쳐 쌓는 3D 스택 공법을 대안으로 제시했으나, <span class=\"text-cyan-300 font-semibold\">ASML</span> 장비 부족으로 인한 수율 저하(20% 수준) 극복이 불가능하다는 보도가 나왔습니다.",
      "key_claims": [
        "구글의 $800억 유상증자는 원금 상환 부담을 없애고 AI 투자 속도전을 벌이려는 빅테크들의 자본 조달 패러다임 변화를 의미한다.",
        "버크셔 해서웨이는 구글 증자 참여와 별개로, 주택 시장 부족 리스크에 대응해 주택 건설사 테일러 모리슨을 68억 달러에 전격 인수(PER 7배 수준의 가치 투자)했다.",
        "중국 화웨이의 3D 반도체 패키징 적층 기술은 고급 리소그래피(ASML EUV) 장비 규제 회복을 위한 고육지책이며, 20% 수준의 극악의 수율 장벽에 가로막혀 있다."
      ],
      "data_points": [
        "구글(알파벳) 유상증자 조달 규모: 800억 달러 (이 중 버크셔 해서웨이가 100억 달러 전격 참여)",
        "버크셔 해서웨이의 테일러 모리슨 인수 금액: 68억 달러 (EV/EBITDA 약 7배 이하)",
        "화웨이 신형 칩 수율: 약 20% 수준으로 불량률이 80%에 달함"
      ],
      "signal": "bullish",
      "signal_reason": "빅테크들의 투자 딜에 버크셔 등 스마트머니가 역대급 현금을 꽂아주고 있으며, 견조한 고용 지표(JOLTS) 상승과 미국의 첨단 반도체 패권 격차가 중국의 수율 파국으로 확인되며 미 증시의 중장기 상승 동력을 뒷받침합니다.",
      "key_companies": [
        "구글",
        "버크셔해서웨이",
        "테일러모리슨",
        "화웨이",
        "ASML"
      ],
      "insight": "구글의 증자는 자사주 매입에 안주하던 빅테크들이 '투자하지 않으면 죽는다'는 절박함에 주주 눈치를 보지 않고 행동함을 대변합니다. 중국 반도체 산업은 장비 규제로 인해 3D 스태킹 등 설계 우회로를 찾고 있으나, 누적 수율이 20%에서 추가 악화되는 공학적 한계에 봉착하여 실질적인 대량 생산 및 위협이 되지 못하고 있음이 드러났습니다.",
      "action_point": "버핏의 발자취를 따라 저평가 주택 건설 등 견고한 미국의 자산 가치주에 동참하거나, 미국의 대중 제재로 장기적 수혜와 해자가 깊어지는 ASML, TSMC 등 독점적 테크 공급망 장장에 투자를 집중해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["구글유상증자", "버크셔해서웨이", "테일러모리슨인수", "화웨이수율파국", "3D스태킹", "JOLTS", "삼프로TV"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["video"], info["analysis"], info["classification"])
print("ALL BATCH 7 VIDEOS SUCCESSFULLY SAVED!")
