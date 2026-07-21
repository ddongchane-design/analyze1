import json
import sys
from pathlib import Path

# Set stdout to UTF-8
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

analyses = {
  "-YSCQUpZmPU": {
    "primary": "tech",
    "video": {
      "id": "-YSCQUpZmPU",
      "title": "AI가 추억 속 게임까지 직접 만들어준다면?",
      "published": "2026-06-05T02:01:05+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=-YSCQUpZmPU",
      "thumbnail": "https://img.youtube.com/vi/-YSCQUpZmPU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "텍스트나 이미지 프롬프트를 입력하여 사용자가 직접 플레이할 수 있는 게임을 구현해 주는 <span class=\"text-amber-300 font-bold\">AI 게임 개발 기술</span>에 대해 다룹니다.",
      "key_claims": [
        "인터넷상의 이미지, 후기, 공략집 등을 종합하여 과거 게임의 메커니즘을 복원할 수 있다.",
        "단순한 이미지/영상 생성을 넘어 실제 동작하고 플레이 가능한 코드로 구현하는 혁신이 진행 중이다."
      ],
      "data_points": [
        "AI 기반 게임 엔진 소스코드 생성 속도 및 복원 가시성 개선"
      ],
      "signal": "bullish",
      "signal_reason": "생성형 AI가 코딩 영역을 넘어 직접 실행 가능한 고성능 콘텐츠를 설계 및 배포하는 능력이 검증되고 있습니다.",
      "key_companies": ["OpenAI", "Google"],
      "insight": "단순한 영상 생성 기술을 넘어 플레이 가능한 실시간 소프트웨어를 만드는 기술은 게임 산업의 제작 비용을 크게 낮출 것입니다.",
      "action_point": "게임 엔진 및 개발 자동화 솔루션을 제공하는 소프트웨어 개발주에 주목해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["etc"],
      "tags": ["AI게임개발", "개발자동화", "인공지능", "게임구현", "안될과학"]
    }
  },
  "4auwGpTQw-c": {
    "primary": "crypto",
    "video": {
      "id": "4auwGpTQw-c",
      "title": "코인판 돈 안 떠났다.... 총알 장전, 스테이블코인으로 바닥만 기다리는 고래들 | 서동주, 김동환, 최윤영 한화투자증권 팀장 [크립토 PLUS]",
      "published": "2026-06-05T04:39:40+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=4auwGpTQw-c",
      "thumbnail": "https://img.youtube.com/vi/4auwGpTQw-c/hqdefault.jpg"
    },
    "analysis": {
      "summary": "비트코인 현물 ETF 자금 유출에도 불구하고 <span class=\"text-amber-300 font-bold\">스테이블코인 점유율 상승</span>은 크립토 시장 자금이 이탈하지 않고 대기 중임을 보여주며, <span class=\"text-cyan-300 font-semibold\">마이크로스트레티지</span>(MSTR)의 4년 만의 첫 비트코인 매도 노이즈를 분석합니다.",
      "key_claims": [
        "비트코인을 테더(USDT)로 바꾼 대기 자금이 많아 크립토 시장의 펀더멘탈은 견조하다.",
        "마이크로스트레티지는 우선주(STRC) 배당 재원을 마련하기 위해 32 BTC를 매도했으나, 이는 전체 보유량의 극소수로 전략 변화가 아니다."
      ],
      "data_points": [
        "마이크로스트레티지 보유 비트코인 매도량: 32 BTC (4년 만의 최초 매도)",
        "MSTR 발행 영구 우선주 STRC 배당률: 11.5%"
      ],
      "signal": "neutral",
      "signal_reason": "MSTR의 비트코인 매도 소식이 단기 악재로 작용했으나, 스테이블코인 대기 자금 규모가 탄탄해 하방 지지가 가능해 보입니다.",
      "key_companies": ["MicroStrategy", "Coinbase"],
      "insight": "비트코인을 안 팔겠다는 약속을 깬 MSTR of 첫 매도는 자본 건전성 우선 메시지를 전달하여 단기 심리를 위축시켰으나, 우선주 배당 모델의 정상 작동 과정으로 평가됩니다.",
      "action_point": "MSTR의 추가 매도 여부와 우선주(STRC) 가격의 100달러 복구 여부를 관망하며 크립토 비중을 조절해야 합니다."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": ["stock"],
      "tags": ["비트코인", "스테이블코인", "마이크로스트레티지", "배당재원", "수요대기", "삼프로TV"]
    }
  },
  "5bl6E1vnm7o": {
    "primary": "stock",
    "video": {
      "id": "5bl6E1vnm7o",
      "title": "점점 과열되는 세기의 머니게임..그런데 구글이 일론 머스크의 뒤통수를 쳤다? | 월가백브리핑",
      "published": "2026-06-05T03:00:25+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=5bl6E1vnm7o",
      "thumbnail": "https://img.youtube.com/vi/5bl6E1vnm7o/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">알파벳</span>의 800억 달러 유상증자 추진이 <span class=\"text-cyan-300 font-semibold\">스페이스X</span>의 IPO를 앞두고 자금을 선점하려는 의도인지 분석하고, AI 설비 투자 과열 논란을 조명합니다.",
      "key_claims": [
        "구글의 대규모 유증은 향후 AI 인프라 수요 가시성이 뚜렷하다는 자신감의 방증이다.",
        "스페이스X IPO를 앞두고 구글이 시장 유동성을 선제적으로 흡수해 경쟁 구도를 심화시켰다.",
        "빅테크의 과도한 AI 투자가 실질적인 수익으로 회수되기까지는 시차가 존재하며 일부 거품 경고도 나오고 있다."
      ],
      "data_points": [
        "알파벳 유상증자 규모: 800억 달러 (버크셔 해서웨이 100억 달러 인수 포함)",
        "알파벳 클라우드 백로그: 4,600억 달러 (전 분기 대비 2배 증가)"
      ],
      "signal": "neutral",
      "signal_reason": "유동성 선점으로 단기 테크주 변동성이 커질 수 있으나, 구글의 수주 잔고 성장세가 확실해 장기 전망은 긍정적입니다.",
      "key_companies": ["Google", "SpaceX", "Berkshire Hathaway"],
      "insight": "투자를 너무 많이 해서 망하는 것이 덜 투자해서 뒤처지는 것보다 낫다는 빅테크의 합의가 대규모 자금 조달로 증명되고 있습니다.",
      "action_point": "단기적인 유동성 쏠림 노이즈를 활용해 밸류에이션 매력이 생긴 빅테크 및 클라우드 인프라 기업을 저가 매수해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["알파벳유증", "스페이스X상장", "AI자본전쟁", "수환매장세", "한경글로벌마켓"]
    }
  },
  "Cv_M2T0qEJs": {
    "primary": "stock",
    "video": {
      "id": "Cv_M2T0qEJs",
      "title": "K-컬처의 중심 ‘이곳’ 왜 주목해야 하나? | 김문정 하나증권 대구중앙WM센터 PB  [더블 크루]",
      "published": "2026-06-05T01:29:21+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=Cv_M2T0qEJs",
      "thumbnail": "https://img.youtube.com/vi/Cv_M2T0qEJs/hqdefault.jpg"
    },
    "analysis": {
      "summary": "백화점 유통업계의 구조적 변화와 <span class=\"text-cyan-300 font-semibold\">VIP 고객 매출 비중 확대</span>, 외국인 인바운드 소비 증가 및 반도체 대기업 성과급 낙수 효과를 전망합니다.",
      "key_claims": [
        "백화점 매출의 40% 이상을 VIP가 차지하며 소비의 양극화와 고착화가 나타나고 있다.",
        "백화점의 문화 공간 플랫폼화(리뉴얼)가 외국인 관광객 유입과 내수 소비를 촉진하고 있다.",
        "반도체 호황에 따른 대기업 성과급 지급이 인근 백화점(판교점, 사우스시티점 등)의 명품 소비로 이어지고 있다."
      ],
      "data_points": [
        "백화점 전체 매출 중 VIP 고객 기여율: 40% 수준"
      ],
      "signal": "bullish",
      "signal_reason": "고소득 VIP 및 외국인 인바운드 매출이 안정적으로 성장하고 있으며, 대기업 성과급 유입이 백화점 매출 상승의 강력한 모멘텀이 됩니다.",
      "key_companies": ["신세계", "현대백화점", "롯데쇼핑"],
      "insight": "백화점은 단순 쇼핑 공간에서 복합 문화 체험 플랫폼으로 진화해 인플레이션 고물가 시대에도 견조한 마진을 유지하고 있습니다.",
      "action_point": "점포 경쟁력과 VIP 해자를 확보한 신세계 및 리뉴얼 성과가 나타나는 현대백화점 중심의 저평가 유통주 매수를 추천합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["백화점유통", "VIP소비", "외국인관광객", "성과급소비", "삼프로TV"]
    }
  },
  "dKRRZvMxQng": {
    "primary": "stock",
    "video": {
      "id": "dKRRZvMxQng",
      "title": "코스피 6% 급락...무슨 일이 있길래?_26.06.05. | 박지훈, 소진웅, 여도은, 허재무 [아침N투자]",
      "published": "2026-06-05T02:56:25+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=dKRRZvMxQng",
      "thumbnail": "https://img.youtube.com/vi/dKRRZvMxQng/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 반도체주 급락 여파와 <span class=\"text-rose-400 font-medium\">역대급 반대매매 공포</span>로 국내 증시가 5~7%대 동반 폭락했으며, 젠슨 황 방한과 관련된 기대 수혜주의 차익 실현 현상을 짚어봅니다.",
      "key_claims": [
        "미 증시 반도체 차익 매물 출회 및 반도체 D램 고점 우려 보고서가 국내 반도체 투톱의 급락을 야기했다.",
        "국내 시장의 기술적 지지선 훼손과 선물 매도로 인해 기계적 매도가 출회되며 언더슈팅이 심화되었다.",
        "젠슨 황의 방한을 앞둔 '감성 매매' 테마주들의 대대적인 차익 실현(셀온뉴스)이 발생했다."
      ],
      "data_points": [
        "5월 국내 시장 누적 반대매매 대금: 8,500억 원 이상",
        "코스피 장중 하락률: 최고 7% 수준 폭락"
      ],
      "signal": "bearish",
      "signal_reason": "기계적 매도와 반대매매 물량이 꼬이면서 단기 수급 불안정이 극에 달해 있어 추가 하락 가능성을 염두에 두어야 합니다.",
      "key_companies": ["삼성전자", "SK하이닉스", "원익IPS"],
      "insight": "단기 패닉 셀링은 펀더멘탈 훼손이 아니며, 장기 CapEx 수혜를 직접 받는 KOSDAQ 전공정 소부장 장비 대표주들에겐 좋은 분할 매수 기회가 됩니다.",
      "action_point": "반도체 투톱은 미장 추이를 보며 재진입 타이밍을 관망하되, 낙폭이 과도한 기판 및 전공정 장비 우량주는 분할 매수를 검토하십시오."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["코스피폭락", "반대매매", "반도체조정", "수급교통정리", "삼프로TV"]
    }
  },
  "fTmcJlZ_mg8": {
    "primary": "economy",
    "video": {
      "id": "fTmcJlZ_mg8",
      "title": "‘금융위기 이후 최고치’…환율 왜 이런가? | 박병창 MP파트너스 대표 [마켓 인사이드]",
      "published": "2026-06-05T00:22:39+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=fTmcJlZ_mg8",
      "thumbnail": "https://img.youtube.com/vi/fTmcJlZ_mg8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국의 금리 불안과 외국인 매도 쏠림 속에서 <span class=\"text-rose-400 font-medium\">원·달러 환율이 1,540원</span>을 돌파하는 등 외환 변동성이 극대화되고 있으며, 테크 섹터의 빠른 조정 방식을 고찰합니다.",
      "key_claims": [
        "미 증시는 반도체 조정 속에서도 헬스케어, 금융 등 저베타 섹터로 순환매가 전개되며 하방을 지탱했다.",
        "원화 약세 심화에도 불구하고, 기업들의 2분기 수출 원화 환산 실적은 사상 최고치를 달성할 가능성이 높다.",
        "조정 국면에서는 천천히 빠지는 질질 흘러내리는 종목보다 급격히 빠지고 V자 반등을 하는 종목이 훨씬 유망하다."
      ],
      "data_points": [
        "원·달러 야간 환율: 1,540원 돌파 (17년 만의 최고 수준)",
        "삼성전자 2분기 영업이익 추정치: 약 10조 원 안팎 전망"
      ],
      "signal": "neutral",
      "signal_reason": "환율 급등에 따른 외국인 자본 유출 우려가 단기 악재이나, Q2 강력한 이익 성장 모멘텀이 하방을 지탱할 것입니다.",
      "key_companies": ["삼성전자", "SK하이닉스", "KB금융"],
      "insight": "고환율 국면은 수출 대기업들에겐 추가적인 환차익 어닝 서프라이즈를 안겨줄 수 있는 양날의 검입니다.",
      "action_point": "지수가 흔들릴 때 옆으로 버티거나 45도 하향하는 약세 종목은 매도하고, 급락 후 빠르게 아래꼬리를 다는 주도주 위주로 압축 대응해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["환율상승", "순환매장세", "반도체조정", "2분기실적기대", "삼프로TV"]
    }
  },
  "hfGLk0kd--4": {
    "primary": "economy",
    "video": {
      "id": "hfGLk0kd--4",
      "title": "외국인 매도 폭탄에 환율 1,540원…해외에선 ‘스파크플레이션’ 경고 | 권순우 삼프로TV 취재팀장 [뉴스3]",
      "published": "2026-06-04T23:37:18+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=hfGLk0kd--4",
      "thumbnail": "https://img.youtube.com/vi/hfGLk0kd--4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-rose-400 font-medium\">원·달러 환율 1,540원</span> 돌파와 외환 시장 패닉 속에서 해외의 <span class=\"text-rose-400 font-medium\">스파이크플레이션</span> 경고를 분석하고, <span class=\"text-cyan-300 font-semibold\">LG그룹</span>의 엔비디아 <span class=\"text-cyan-300 font-semibold\">블랙웰 GPU 1만 장</span> 확보 뉴스를 조명합니다.",
      "key_claims": [
        "외국인들이 19일 연속 코스피를 순매도하며 지수를 압박하고 환율 급등을 주도하고 있다.",
        "FT는 저물가 유지 후 갑자기 튀는 스파이크플레이션(Spikeflation) 위험을 경고했으며, 각국의 공공부채 비율 상승으로 위기 대처력이 약화되었다.",
        "LG그룹은 AI 연구와 휴머노이드 개발을 위해 약 7,000억 원 상당의 블랙웰 1만 장을 구매하기로 단독 보도되었다."
      ],
      "data_points": [
        "외국인 코스피 순매도 기간: 19거래일 연속",
        "LG 엔비디아 블랙웰 GPU 도입 규모: 1만 장 (약 7,000억 원 가치)"
      ],
      "signal": "bearish",
      "signal_reason": "글로벌 공공부채 및 고금리, 고유가 불확실성과 외환 시장의 급격한 약세가 한국 증시의 자금 이탈 압력을 키우고 있습니다.",
      "key_companies": ["LG전자", "NVIDIA", "삼성전자", "SK하이닉스"],
      "insight": "미국의 압박과 관세 협상 속에서도 국내 대기업들이 독자 AI 주도권 및 로보틱스 개발을 위해 공격적으로 최첨단 칩 인프라 확보에 나서고 있습니다.",
      "action_point": "환율 발작 국면에서는 무분별한 테크 추격은 자제하되, 실물 GPU 인프라와 피지컬 AI 로드맵을 지닌 대형 그룹주로 포트폴리오를 슬림화해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["환율폭등", "스파이크플레이션", "LG디바이스", "블랙웰도입", "삼프로TV"]
    }
  },
  "i8Ogs7dlH-0": {
    "primary": "stock",
    "video": {
      "id": "i8Ogs7dlH-0",
      "title": "꽉 잡고 계세요 반도체 조금 떨어졌다고 절대 지금 팔면 안됩니다 ㅣ한동희 SK 연구원",
      "published": "2026-06-05T05:14:10+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=i8Ogs7dlH-0",
      "thumbnail": "https://img.youtube.com/vi/i8Ogs7dlH-0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "과거 매크로 공식을 깨는 <span class=\"text-amber-300 font-bold\">독립적인 AI 메모리 사이클</span>을 규명하고, 내년 <span class=\"text-cyan-300 font-semibold\">HBM 가격의 대폭 상향</span> 전망을 근거로 반도체 주식의 보유 강화를 강력히 권고합니다.",
      "key_claims": [
        "과거와 달리 거시 경제 위축 속에서도 AI 투자가 메모리 독립 호황(호실적+양적완화 공존)을 이끌고 있다.",
        "HBM의 공급 유인을 유지하기 위해 대기업들은 내년 HBM 단가를 50% 이상 폭력적으로 인상할 것이다.",
        "실적 전망치는 폭증하는 반면 주가 상승이 이를 따라잡지 못해 국내 반도체 투톱의 PER은 비정상적으로 저렴하다."
      ],
      "data_points": [
        "내년 HBM 단가 인상 전망률: 전년 대비 50% 이상 추정",
        "마이크론 대비 국내 메모리 투톱의 상대적 PER 저평가 지속"
      ],
      "signal": "bullish",
      "signal_reason": "HBM의 단가 협상력 극대화와 독립적 실적 성장세가 견고하여, 단기 조정은 재평가 국면 직전의 절호의 매수 기회입니다.",
      "key_companies": ["SK하이닉스", "삼성전자", "마이크론"],
      "insight": "메모리는 더 이상 매크로에 종속된 커모디티가 아닙니다. 독점력과 단가 결정권을 쥔 선도 기업의 가치는 구조적으로 재평가받을 것입니다.",
      "action_point": "일시적인 수급 불안으로 급락할 때 반도체 선두 기업(특히 SK하이닉스)의 비중을 흔들림 없이 확대하십시오."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["반도체업사이클", "HBM단가인상", "재평가논리", "저평가매수", "이효석아카데미"]
    }
  },
  "ip2UiJsHvO4": {
    "primary": "crypto",
    "video": {
      "id": "ip2UiJsHvO4",
      "title": "비트코인 하락장, 손실만 104억 달러인 MSTR이 망할 수도 있다? 남은 준비금은 단 7개월 | 김동환, 서동주, 박상혁 디지털애셋 편집장 [크립토 PLUS]",
      "published": "2026-06-05T03:30:30+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=ip2UiJsHvO4",
      "thumbnail": "https://img.youtube.com/vi/ip2UiJsHvO4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">마이크로스트레티지</span>(MSTR)의 비트코인 매각과 영구 우선주(STRC)의 <span class=\"text-rose-400 font-medium\">배당 재원 한계(7개월)</span> 리스크를 짚어보고, STRC를 담보로 하는 <span class=\"text-rose-400 font-medium\">APX USD 디페깅 사태</span>를 분석합니다.",
      "key_claims": [
        "MSTR은 비트코인 평단가 하회로 104억 달러의 미실현 손실을 입었으며, 매달 1.4억 달러의 배당/이자를 줘야 해 현금 바닥 우려가 커졌다.",
        "STRC 우선주 가격이 100달러를 하회하면서 추가 조달에 제동이 걸려 비트코인 추가 매도 압박이 발생하고 있다.",
        "STRC를 담보로 발행된 스테이블코인 APX USD가 0.91달러로 디페깅되며 시장의 강제 청산 공포(청산 규모 3%)가 유입되었다."
      ],
      "data_points": [
        "MSTR 보유 비트코인 평균 단가: 75,701달러 (현재가 6.3만 달러 하회)",
        "MSTR 보유 달러 잔량 기준 배당 지급 가능 기간: 7개월",
        "APX USD 디페깅 최저가 기록: 0.91달러"
      ],
      "signal": "bearish",
      "signal_reason": "MSTR의 대규모 비트코인 조달 방식의 한계가 확인되었고, 스테이블코인과의 부채 연계 리스크로 인해 크립토 전반의 수급 불안이 예상됩니다.",
      "key_companies": ["MicroStrategy", "Coinbase"],
      "insight": "비트코인을 영원히 홀딩하겠다는 선언이 우선주 배당 고정비 압박으로 무너졌으며, 레버리지 구조의 균열이 시장 덤핑 우려를 키우고 있습니다.",
      "action_point": "MSTR의 현금 및 우선주 가격 추이가 복구될 때까지 비트코인 등 가상자산에 대한 보수적인 접근을 유지하고 관망하십시오."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": ["stock"],
      "tags": ["마이크로스트레티지", "비트코인매각", "우선주배당", "APXUSD디페깅", "삼프로TV"]
    }
  },
  "J8WIFxgirtQ": {
    "primary": "tech",
    "video": {
      "id": "J8WIFxgirtQ",
      "title": "메모리는 오히려 20%더 필요하다는 계산입니다.",
      "published": "2026-06-05T07:27:44+00:00",
      "channel_name": "월텍남",
      "url": "https://www.youtube.com/watch?v=J8WIFxgirtQ",
      "thumbnail": "https://img.youtube.com/vi/J8WIFxgirtQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아 베라루빈의 메모리 삭감 낭설의 실체를 밝히고, 오히려 <span class=\"text-cyan-300 font-semibold\">소캠 2(LPCAMM2) 소켓 다각화</span>와 오픈AI의 <span class=\"text-cyan-300 font-semibold\">장기 메모리 기술(드리밍, 크로니클)</span> 도입에 따른 초과 수요를 전망합니다.",
      "key_claims": [
        "베라루빈 스펙 중 192GB 용량이 96GB로 낮아졌으나, 소켓 장착 수가 4배로 늘어나 실질 메모리 수요는 10~20% 증가한다.",
        "오픈AI의 장기 기억 비서(Dreaming) 및 화면 실시간 캡처 코딩 에이전트(Chronicle)는 천천히 동작하는 텍스트 대비 천문학적인 DRAM/NAND 수요를 유발한다.",
        "구글 지니 3 등 실시간 가상 세계 모델(World Model) 구축에는 한계가 없는 메모리 용량이 필수적이다."
      ],
      "data_points": [
        "베라루빈 아키텍처 LPDDR5X (소캠 2) 메모리 수요 증가율: 기존 전망 대비 +10% ~ +20%",
        "ChatGPT 장기 메모리 정확도 개선도: 2024년 4%에서 2026년 75% 수준으로 급상승"
      ],
      "signal": "bullish",
      "signal_reason": "소프트웨어 에이전트들의 실시간 이미지/비디오 기반 학습과 베라루빈의 소캠 2 소켓 구조가 장기 메모리 쇼티지를 견인하고 있습니다.",
      "key_companies": ["NVIDIA", "OpenAI", "SK하이닉스", "삼성전자"],
      "insight": "메모리 감축 루머는 리포팅 와전에 따른 일시적 해프닝이며, 실시간 화면 처리를 동반한 에이전트 AI의 등장은 DRAM 업계에 엄청난 성장의 기회입니다.",
      "action_point": "일시적인 용량 삭감 노이즈로 메모리 반도체 대장주가 급락할 때 저가 매수에 동참해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["베라루빈스펙", "소캠2도입", "메모리수요증가", "오픈AI드리밍", "월텍남"]
    }
  },
  "K-k_HbGLgSA": {
    "primary": "space",
    "video": {
      "id": "K-k_HbGLgSA",
      "title": "싫으면 팔고 나가라 스페이스X 배짱 상장 (한겨레 박종오 기자)",
      "published": "2026-06-05T07:55:17+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=K-k_HbGLgSA",
      "thumbnail": "https://img.youtube.com/vi/K-k_HbGLgSA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">스페이스X IPO</span> 심사 서류 분석을 통해 공개된 극단적인 <span class=\"text-rose-400 font-medium\">차등의결권 지배 구조</span>와 일론 머스크의 셀프 성과급 주식 보상(10억 주) 실체를 조명합니다.",
      "key_claims": [
        "일론 머스크는 클래스 B 황금주(1주당 10표)를 통해 스페이스X 지분 12%만으로도 85%의 의결권을 완전히 독점하고 있다.",
        "화성에 100만 명 규모 식민지를 지을 경우 클래스 B 10억 주를 추가로 주는 계약을 머스크가 셀프 통과시켰다.",
        "SEC 신고서 위험 고지서에 '소송할 생각 말고 싫으면 투자하지 말라'는 식의 배짱 거버넌스를 명시했다."
      ],
      "data_points": [
        "스페이스X IPO 공모 비율: 전체 지분의 4% 내외 (750억 달러 상당)",
        "일론 머스크의 스페이스X 연봉: 연 8,000만 원 (5년째 동결)"
      ],
      "signal": "neutral",
      "signal_reason": "머스크의 극단적 거버넌스는 기관 투자자 소송의 뇌관이 될 수 있으나, 독보적인 우주 인프라 경쟁력과 패시브 자금 강제 유입으로 흥행은 확실해 보입니다.",
      "key_companies": ["SpaceX", "Tesla"],
      "insight": "스페이스X의 지배구조는 미국에서도 유례없는 배짱 거버넌스이나, 화성 개척이라는 원대한 비전 아래 주주들의 권리 포기를 종용하는 구조입니다.",
      "action_point": "지수 편입에 따른 패시브 수동 매수 유입은 긍정적이지만, 일론 머스크 리스크와 지배구조 경고를 감안해 상장 초기 고점 추격은 삼가야 합니다."
    },
    "classification": {
      "primary_topic": "space",
      "secondary_topics": ["stock", "economy"],
      "tags": ["스페이스X상장", "차등의결권", "황금주계약", "거버넌스리스크", "언더스탠딩"]
    }
  },
  "KEriHGR21zM": {
    "primary": "crypto",
    "video": {
      "id": "KEriHGR21zM",
      "title": "대한민국 크립토의 미래, CIS 2026에서 만나다",
      "published": "2026-06-05T04:38:13+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=KEriHGR21zM",
      "thumbnail": "https://img.youtube.com/vi/KEriHGR21zM/hqdefault.jpg"
    },
    "analysis": {
      "summary": "CIS 2026 행사를 통해 본 <span class=\"text-cyan-300 font-semibold\">하이퍼스케일 데이터</span>(GPUS)의 비트코인 채굴/담보 전략 및 <span class=\"text-cyan-300 font-semibold\">이더리움 재단</span>의 멀티 클라이언트 보안 안정성을 고찰합니다.",
      "key_claims": [
        "하이퍼스케일 데이터는 매주 비트코인을 적립하는 MSTR 유사 전략을 취하면서도, 미시간에 대형 AGI 봇 로봇 센터를 짓는 다각화를 진행한다.",
        "이더리움은 5개 이상의 다른 클라이언트 소프트웨어를 동시에 실행하여 10년 넘게 단 1초도 멈추지 않은 독보적 복원력을 증명했다.",
        "이더리움 현물 ETF 승인과 기관 자금 유입은 유동성을 공급하여 장기적으로 암호화폐의 변동성을 줄여줄 것이다."
      ],
      "data_points": [
        "하이퍼스케일 데이터(GPUS) 올해 매출 전망치: 2억 달러 이상 (전년 대비 2배 성장)",
        "이더리움 재단의 전체 이더리움 지분율: 1% 미만 수준"
      ],
      "signal": "bullish",
      "signal_reason": "블록체인의 기술적 안전성과 ETF를 통한 전통 금융 및 기관 투자자 유입이라는 대형 인프라 구조가 정착되고 있습니다.",
      "key_companies": ["HyperScale Data", "Zangle"],
      "insight": "암호화폐 시장은 단순 소매 시장 투기 단계에서 벗어나, 기관의 참여를 유도하는 디지털 신탁 및 글로벌 대체 담보 자산으로 성장하고 있습니다.",
      "action_point": "비트코인은 변동성을 활용한 적립식 매수를, 이더리움은 유동성 및 기술적 신뢰도 기반의 중장기 포트폴리오 편입을 추천합니다."
    },
    "classification": {
      "primary_topic": "crypto",
      "secondary_topics": ["robot", "stock"],
      "tags": ["비트코인담보", "이더리움멀티클라이언트", "크립토기관투자", "CIS2026", "삼프로TV"]
    }
  },
  "kIvD6ef83as": {
    "primary": "stock",
    "video": {
      "id": "kIvD6ef83as",
      "title": "[26.06.05 오전 방송 전체보기] 엔비디아 상승 속 반도체주 하락...다우지수 '사상 최고'",
      "published": "2026-06-05T03:20:15+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=kIvD6ef83as",
      "thumbnail": "https://img.youtube.com/vi/kIvD6ef83as/hqdefault.jpg"
    },
    "analysis": {
      "summary": "반도체 하락 속에 <span class=\"text-amber-300 font-bold\">다우지수가 사상 최고치</span>를 경신한 미국의 건강한 순환매 장세와 스페이스X 상장 대기 수급 노이즈를 요약합니다.",
      "key_claims": [
        "과열된 반도체 하드웨어에서 헬스케어, 금융 및 필수소비재 등 저베타 소외주로 수급이 확산되고 있다.",
        "스페이스X 상장 시 QQQ 등 지수 추종 패시브 펀드들의 매수 부담으로 기존 기술주 지분 매도가 발생할 수 있다.",
        "금은 단순 인플레이션 헤지 수단이 아닌 비트코인 같은 위험 자산의 성격으로 거래되며 단기 매수 과열에 직면해 있다."
      ],
      "data_points": [
        "스페이스X IPO 지분 매각 비율: 5% 미만 (약 750억 달러 규모)",
        "금값 저항선 지지 가격대: 온스당 4,000달러 부근 가능성"
      ],
      "signal": "neutral",
      "signal_reason": "주도 테크 섹터의 숨고르기와 소외 섹터로의 순환매는 장기적으로 시장을 건강하게 만들지만, 단기적으로 반도체 이격 조정은 피할 수 없습니다.",
      "key_companies": ["NVIDIA", "Broadcom", "Micron"],
      "insight": "시장 상승 일변도 국면에서는 옵션 해지 비용이 저렴하므로, 강세장 후반부로 갈수록 포트폴리오 다각화와 헬스케어 등 소외 방어주 편입이 중요합니다.",
      "action_point": "고베타 반도체 비중을 소폭 덜어내고, 밸류에이션 매력이 있는 대형 금융주와 헬스케어 비중을 유지하는 보수적 포트폴리오를 유지하십시오."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["다우사상최고", "수환매장세", "스페이스XIPO", "헬스케어분산", "삼프로TV"]
    }
  },
  "MzlDbKE7ihw": {
    "primary": "tech",
    "video": {
      "id": "MzlDbKE7ihw",
      "title": "“틱톡 베꼈다” 비웃음 샀던 메타, AI에 '217조' 쏟아붓는 이유 | 매일뉴욕 스페셜 | 홍성용 특파원",
      "published": "2026-06-05T03:00:26+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=MzlDbKE7ihw",
      "thumbnail": "https://img.youtube.com/vi/MzlDbKE7ihw/hqdefault.jpg"
    },
    "analysis": {
      "summary": "틱톡 차단 노이즈 속에서 인스타그램 <span class=\"text-cyan-300 font-semibold\">릴스</span>를 통해 광고 점유율을 늘리고 있는 <span class=\"text-cyan-300 font-semibold\">메타</span>의 압도적인 주주 수익성 및 <span class=\"text-cyan-300 font-semibold\">AI 설비 투자(1,450억 달러)</span>의 실질 성과를 조명합니다.",
      "key_claims": [
        "메타는 35억 명의 거대 소셜망과 20년 광고 인프라 해자를 통해 Reels의 카피캣 논란을 극복하고 틱톡을 이겼다.",
        "1분기 메타의 광고 단가와 노출수가 동반 상승(각각 12%, 19%)했으며, 이는 AI 타게팅 엔진 도입의 실질 어닝 기여 증거이다.",
        "메타는 인건비 30억 달러를 아껴 AI 인프라에 쏟았으나, 차세대 루빈 GPU의 발열 및 전력 과부하로 인프라 재건설 비용 부담이 존재한다."
      ],
      "data_points": [
        "메타 2026년 연간 Capex 가이던스: 최대 1,450억 달러 (전년 대비 2배 증액)",
        "메타 1인당 분기 매출액: 약 10억 8,000만 원 (삼성전자 대비 3배 이상의 고효율)",
        "Ray-Ban Meta 스마트 글래스 2025년 판매량: 700만 대 돌파"
      ],
      "signal": "bullish",
      "signal_reason": "AI 투자는 당장 광고 효율 증대로 결실을 맺고 있으며, 스마트 글래스 시장 선점으로 차세대 플랫폼 장악력이 높아지고 있습니다.",
      "key_companies": ["Meta", "NVIDIA", "Apple"],
      "insight": "카피캣 비난 속에서도 압도적인 유통/네트워크망을 지닌 선두 기업이 포맷만 얹으면 승리한다는 비즈니스 복제 성공 사례를 보여줍니다.",
      "action_point": "AI CapEx 증설 부담으로 인한 일시적인 주가 조정 국면은 메타 지분을 늘릴 수 있는 확실한 저가 매수 타이밍입니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["메타릴스", "AI광고효율", "인프라Capex", "스마트글래스", "매경월부"]
    }
  },
  "OhwJCAkbRdE": {
    "primary": "stock",
    "video": {
      "id": "OhwJCAkbRdE",
      "title": "떨어진다 떨지 말고  \"고개 들어 7월을 봐라\" | 빈센트 & 편다송 [더블 업]",
      "published": "2026-06-05T04:20:06+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=OhwJCAkbRdE",
      "thumbnail": "https://img.youtube.com/vi/OhwJCAkbRdE/hqdefault.jpg"
    },
    "analysis": {
      "summary": "금리 매크로 경계감으로 흔들리는 6월 증시의 성격과 다가올 <span class=\"text-amber-300 font-bold\">7월 2분기 반도체 어닝 서프라이즈</span> 대비 포트폴리오 비중 유지를 격려합니다.",
      "key_claims": [
        "6월 조정은 실적에서 금리/인플레 등 매크로 지표로 시장 관심이 전이되면서 발생한 일시적 노이즈이다.",
        "우리 대기업들의 이익 창출력과 반도체 펀더멘탈은 변한 것이 없다.",
        "7월 2분기 강력한 어닝 서프라이즈 확인과 함께 주가는 복원될 것이다."
      ],
      "data_points": [
        "SK하이닉스 주가 추이: 5월 말 200만 원 돌파 안착 성공"
      ],
      "signal": "bullish",
      "signal_reason": "반도체 펀더멘탈 및 이익 전망 상향이 굳건하므로, 6월의 변동성은 우량주를 싸게 담는 최적의 기간입니다.",
      "key_companies": ["SK하이닉스", "삼성전자"],
      "insight": "시장 하락에 휩쓸려 패닉 셀을 하기보다는, 어닝 시즌 개막 직전인 6월에 주도 섹터의 알짜 자산을 줍는 집중력이 필요합니다.",
      "action_point": "조정 시 공포에 떨지 말고 '밀리면 매수' 전략을 일관되게 고수하여 2분기 어닝 랠리를 대비하십시오."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["6월조정구간", "7월실적시즌", "반도체서프라이즈", "밀리면사라", "삼프로TV"]
    }
  },
  "P9iuVrfblnc": {
    "primary": "stock",
    "video": {
      "id": "P9iuVrfblnc",
      "title": "창신메모리 상장 임박, 한국 반도체에 진짜 위협일까? | 김경환 하나증권 리서치센터 팀장 [더블 업]",
      "published": "2026-06-05T02:10:10+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=P9iuVrfblnc",
      "thumbnail": "https://img.youtube.com/vi/P9iuVrfblnc/hqdefault.jpg"
    },
    "analysis": {
      "summary": "중국 상해 과창판에 상장 예정인 D램 1위 <span class=\"text-violet-300 font-medium\">창신메모리</span>(CXMT)의 1분기 대규모 어닝 서프라이즈와 상장 수급 영향이 한국 반도체에 미치는 영향을 고찰합니다.",
      "key_claims": [
        "중국 정부의 강력한 지원으로 CXMT(D램)와 YMTC(낸드)의 상장이 하반기에 급물살을 타고 있다.",
        "CXMT의 1분기 순이익이 약 6조 원 이상을 기록하며 지난 4년 누적 적자를 전부 만회하는 서프라이즈를 냈다.",
        "이번 IPO로 조달하는 자금은 저가용 LPDDR4 및 범용 DDR4 고도화 위주로 쓰여, 국내 대기업이 장악한 첨단 HBM 시장 위협은 낮아 불확실성 해소로 봐야 한다."
      ],
      "data_points": [
        "CXMT 1분기 실질 순이익 규모: 약 300억 위안 (약 6조 원 돌파, 배터리 1위 CATL 상회)",
        "CXMT 글로벌 D램 시장 점유율: 약 8% 수준"
      ],
      "signal": "neutral",
      "signal_reason": "중국의 메모리 추격 실체는 범용 시장에 국한되어 있어 국내 고부가가치 AI 포트폴리오의 실질 타격은 제한적입니다.",
      "key_companies": ["삼성전자", "SK하이닉스", "NVIDIA"],
      "insight": "중국의 자급화 및 특혜 상장 드라이브는 중국 반도체 장비 생태계(과창판 지수)에는 대형 호재이나, 선두 업체들의 HBM 장벽을 넘지는 못하고 있습니다.",
      "action_point": "중국의 상장 노이즈로 메모리 투톱 주가가 일시적으로 과조정될 경우, 오히려 HBM 독점력을 지닌 국내 반도체주의 저가 매수 비중을 확보해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["창신메모리IPO", "양쯔메모리", "과창판지수", "반도체불확실성해소", "삼프로TV"]
    }
  },
  "pYM-28VMlTI": {
    "primary": "stock",
    "video": {
      "id": "pYM-28VMlTI",
      "title": "[속보효] 메모리 주식 하락 사태, 어떻게 볼 것인가?",
      "published": "2026-06-05T00:42:32+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=pYM-28VMlTI",
      "thumbnail": "https://img.youtube.com/vi/pYM-28VMlTI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "국내 증시의 <span class=\"text-rose-400 font-medium\">서킷 브레이커/사이드카 발동</span> 및 삼성전자 7% 하락 속에서 5가지 기초 시황 용어를 통해 시장의 단기 수급 왜곡 현상을 진단합니다.",
      "key_claims": [
        "미 증시 반도체 급락은 펀더멘탈 훼손이 아닌, 단기 급등에 따른 헬스케어/금융 소외주로의 전형적 순환매이다.",
        "브로드컴의 하락 역시 실적 발표 이후 재료 소멸에 따른 일시적 차익 실현(Sell the News) 과정이다.",
        "메모리 사이클은 2분기 강력한 원화 환산 어닝 서프라이즈가 대기 중이므로 추세적 하락(끝)으로 갈 가능성은 매우 낮다."
      ],
      "data_points": [
        "국내 코스피 하락률: 장중 최고 4%대 급락 돌파",
        "원·달러 환율: 1,530원 돌파 상승세 지속"
      ],
      "signal": "bullish",
      "signal_reason": "시장의 본질적 어닝 창출 능력이 훼손되지 않았으므로, 레버리지 털어내기용 공포 하락 국면은 적극적인 우량주 바이더딥 기회입니다.",
      "key_companies": ["SK하이닉스", "삼성전자", "Broadcom"],
      "insight": "단기 레버리지 투자자들의 반대매매 공포로 지수가 과도하게 내려앉은 오버슈팅 구간은 장기 투자자들에게 최고의 진입 타점입니다.",
      "action_point": "공포감에 편승한 패닉 셀은 지양하고, 실적이 증명된 반도체 소부장 및 메모리 선두주의 포트폴리오 지분을 안전하게 지켜가야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["메모리급락사태", "사이드카발동", "순환매장세", "이효석아카데미"]
    }
  },
  "TLynEWWANt0": {
    "primary": "stock",
    "video": {
      "id": "TLynEWWANt0",
      "title": "삼전닉스, 플러스 알파를 찾아서 | RE포트 | 2026.6.5(금)",
      "published": "2026-06-05T00:00:33+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=TLynEWWANt0",
      "thumbnail": "https://img.youtube.com/vi/TLynEWWANt0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "삼성전기의 2029년 실적 선반영 및 <span class=\"text-cyan-300 font-semibold\">목표주가 280만 원 상향</span>, 알파벳 유상증자의 긍정적 AI 시그널, 삼성전자의 특별배당 매력, 그리고 <span class=\"text-cyan-300 font-semibold\">SK하이닉스의 미국 ADR 및 필반도체 지수 편입 가능성</span>을 요약합니다.",
      "key_claims": [
        "삼성전기는 AI MLCC ASP 10% 인상 및 FC-BGA 수요 4배 증가에 힘입어 2029년 실적 기준 목표가가 115% 대폭 상향되었다.",
        "삼성전자는 FCF 목표 초과 달성으로 2027년 3월 특별 배당금 기대(기본 수익률 3.7% ~ 최대 6.5%)가 높아졌다.",
        "SK하이닉스는 미국 SEC에 confidential ADR 신청서를 제출했으며, 상장 시 필라델피아 반도체 지수 편입을 통해 천문학적인 패시브 유입이 예상된다."
      ],
      "data_points": [
        "삼성전기 2030년 예상 매출액: 32.5조 원 (올해 13.5조 원 대비 2.4배 이상 급증)",
        "삼성전자 우선주 기대 배당 수익률 상단: 10.1% 수준",
        "SK하이닉스 미국 ADR 공모 규모: 최소 277억 달러 (약 40조 원 수준)"
      ],
      "signal": "bullish",
      "signal_reason": "삼성전기의 부품 가격 인상, 삼성전자의 대규모 배당 메리트, 하이닉스의 글로벌 ADR 지수 편입 수급 등 초대형 카탈리스트들이 대기하고 있습니다.",
      "key_companies": ["삼성전기", "삼성전자", "SK하이닉스", "Google"],
      "insight": "단기 지수 흔들림과 상관없이, 국내 IT 주도주들은 글로벌 AI 인프라 팽창과 연계된 구조적 실적 증명 및 해외 자본 유입 카드를 착실히 확보해 나가고 있습니다.",
      "action_point": "목표가가 급격히 상향되고 특별배당 및 해외 패시브 자금 수혜가 확실한 삼성전기, 삼성전자 우선주, SK하이닉스 비중을 견고히 확대하십시오."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["삼성전기목표가", "알파벳자본조달", "삼성전자특별배당", "SK하이닉스ADR", "미래에셋"]
    }
  },
  "ZcmlKKug0c4": {
    "primary": "etc",
    "video": {
      "id": "ZcmlKKug0c4",
      "title": "내한기념, 젠슨 황 옷 가격분석",
      "published": "2026-06-05T03:00:07+00:00",
      "channel_name": "Softdragon SOD",
      "url": "https://www.youtube.com/watch?v=ZcmlKKug0c4",
      "thumbnail": "https://img.youtube.com/vi/ZcmlKKug0c4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아 CEO 젠슨 황의 방한 기념으로 그의 시그니처 룩(에르메스 신발, 톰포드 자켓 등 약 1,200만 원 규모)의 비용과 자산 규모를 비교합니다.",
      "key_claims": [
        "젠슨 황이 착용한 에르메스 신발과 톰포드 자켓의 합산 가격은 약 1,200만 원 선으로 추산된다.",
        "자산이 200~300조 원에 달하는 젠슨 황에게 1,200만 원은 일반 직장인의 수십 원 정도의 가치에 불과하다."
      ],
      "data_points": [
        "젠슨 황 추산 자산 규모: 약 200조 ~ 300조 원 수준"
      ],
      "signal": "neutral",
      "signal_reason": "시황 정보라기보다 방한 전 가십성 정보를 전달하는 스케치형 비디오입니다.",
      "key_companies": ["NVIDIA"],
      "insight": "젠슨 황의 친화적인 방한 행보와 일상이 대중적으로 밈(Meme)화되어 큰 인기를 끌고 있음을 보여줍니다.",
      "action_point": "단순 흥미성 정보이므로 투자 결정에는 관여하지 마십시오."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["tech"],
      "tags": ["젠슨황옷", "에르메스신발", "톰포드자켓", "인터뷰", "Softdragon"]
    }
  },
  "ZI6boQxekzA": {
    "primary": "tech",
    "video": {
      "id": "ZI6boQxekzA",
      "title": "엔비디아가 메모리 50%감축? 진실은 이렇습니다",
      "published": "2026-06-05T05:05:07+00:00",
      "channel_name": "월텍남",
      "url": "https://www.youtube.com/watch?v=ZI6boQxekzA",
      "thumbnail": "https://img.youtube.com/vi/ZI6boQxekzA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아 베라루빈 칩의 메모리 용량 50% 감축 낭설에 대해 Semianalysis의 <span class=\"text-cyan-300 font-semibold\">딜런 파텔의 직접 해명</span>을 알리고, 오히려 메모리 수요는 견조함을 역설합니다.",
      "key_claims": [
        "Semianalysis 보고서의 과장 인용으로 인해 베라루빈 렉당 메모리 용량이 절반 삭감된다는 무서운 소문이 돌았으나 이는 사실이 아니다.",
        "보고서 발행자 딜런 파텔이 직접 '너무 자극적인 제목으로 와전된 낭설'이라며 소문을 직접 반박했다.",
        "중국 CXMT/YMTC의 저가 증설 및 스마트폰 피크아웃 우려는 고부가가치 AI 독점 메모리(HBM/LPDDR5X) 시장에는 아무런 타격을 주지 못한다."
      ],
      "data_points": [
        "베라루빈 메모리 설계 변경 오보: 기존 55TB에서 28TB 삭감 소문은 사실 무근으로 규명"
      ],
      "signal": "bullish",
      "signal_reason": "보고서 와전으로 인한 메모리 피크아웃 공포는 과도한 시장 오해이며, HBM 독점력을 지닌 국내 반도체 투톱의 펀더멘탈은 견고합니다.",
      "key_companies": ["SK하이닉스", "삼성전자", "NVIDIA"],
      "insight": "주가 고점 부근에서 시장의 공포 심리는 와전된 뉴스 하나에도 크게 반응하지만, 팩트를 검증해 보면 여전히 공급 과잉과는 거리가 멉니다.",
      "action_point": "와전된 뉴스에 따른 반도체 과도한 폭락은 적극적인 대장주 매수 기회로 활용해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["베라루빈소문", "딜런파텔해명", "LPDDR5X수요", "반도체노이즈", "월텍남"]
    }
  },
  "ZKedJwgAaVM": {
    "primary": "etc",
    "video": {
      "id": "ZKedJwgAaVM",
      "title": "아는 척 하다 걸리면 혼난다? | 2분완성 그림퀴즈 #shorts #ai",
      "published": "2026-06-05T04:04:57+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=ZKedJwgAaVM",
      "thumbnail": "https://img.youtube.com/vi/ZKedJwgAaVM/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미래에셋증권 채널의 AI 생성 이미지를 활용한 2분 완성 그림퀴즈 숏폼(Shorts) 콘텐츠입니다.",
      "key_claims": [
        "AI 기반 퀴즈 밈을 활용한 대중 친화적 콘텐츠"
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "유익한 경제 또는 기업 펀더멘탈 정보를 포함하지 않는 단순 가십성 퀴즈 숏폼 영상입니다.",
      "key_companies": ["미래에셋증권"],
      "insight": "금융회사들의 대중 친화력을 증대시키기 위한 숏폼 밈 마케팅 전략의 일환입니다.",
      "action_point": "투자 판단에 미치는 영향이 없으므로 투자 결정에서는 배제하시기 바랍니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["etc"],
      "tags": ["그림퀴즈", "AI퀴즈", "가십", "미래에셋"]
    }
  },
  "ZqFikAPuIhU": {
    "primary": "stock",
    "video": {
      "id": "ZqFikAPuIhU",
      "title": "반도체 조정장 기회일까? 진짜 핵심은… | 장우진 작가 [더블 체크]",
      "published": "2026-06-05T01:07:01+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=ZqFikAPuIhU",
      "thumbnail": "https://img.youtube.com/vi/ZqFikAPuIhU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "반도체 대형주의 조정 수급 분석과 환율 1,540원 돌파에 따른 <span class=\"text-rose-400 font-medium\">7월 기준금리 인상 가능성</span>, 지방선거 이후 <span class=\"text-rose-400 font-medium\">금투세/보유세 재점화 우려</span> 및 금융주 자사주 소각 랠리를 분석합니다.",
      "key_claims": [
        "어제 코스닥 소부장이 상한가 부근까지 폭등했으나, 오늘 급격한 매물이 쏟아진 것처럼 단기 급등주 20% 이상 추격은 위험하다.",
        "원·달러 환율이 1,540원을 돌파하여 7월 한국 기준금리 인상이 사실상 확정적인 압박으로 작용하고 있다.",
        "여당의 지방선거 대승 이후 8,000포인트가 넘은 코스피를 명분 삼아 금투세 도입 및 종부세/보유세 인상 논의가 제점화되며 시장에 심리적 부담을 준다.",
        "신영증권의 1조 원 대 규모 대형 자사주 매입 및 소각 발표가 메리트가 되어 배당/금융주 쏠림이 유입되고 있다."
      ],
      "data_points": [
        "코스피 지수 예상 위치: 8,100선 안팎 횡보",
        "신영증권 자사주 소각 규모: 시가총액 3조 원 중 약 1조 원 (기존 자사주의 60% 이상 소각)"
      ],
      "signal": "neutral",
      "signal_reason": "금리 인상 가능성과 금투세 부활 우려 등 거시 세금 악재가 존재하나, 금융주의 대대적 주주 환원과 반도체 펀더멘탈 지지로 하방은 막혀 있습니다.",
      "key_companies": ["삼성전자", "SK하이닉스", "신영증권", "KB금융"],
      "insight": "세제 개편과 환율 변동성은 시장의 단기 아킬레스건이나, 적극적으로 주주 환원(자사주 소각)을 발표하는 금융/증권사와 반도체 소부장의 밸류는 굳건합니다.",
      "action_point": "어제 급등했던 소부장의 급한 추격은 자제하되, 신영증권 및 메이저 금융주의 비중을 늘려 세제/환율 변동성 국면을 방어해야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["반도체조정장", "환율불안", "지방선거세제개편", "자사주소각", "삼프로TV"]
    }
  }
}

def main():
    synthesis_dir = Path("data/synthesis")
    if synthesis_dir.exists():
        for syn_file in synthesis_dir.glob("*.json"):
            try:
                syn_file.unlink()
                print(f"Removed cache: {syn_file}")
            except Exception as e:
                print(f"Error unlinking cache {syn_file.name}: {e}")
                
    for video_id, data in analyses.items():
        save_analysis(
            video_id=video_id,
            primary_topic=data["primary"],
            video_data=data["video"],
            analysis_data=data["analysis"],
            classification_data=data["classification"]
        )
        
    print("\nTriggering render_dashboard...")
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    from agents.orchestrator import render_dashboard
    render_dashboard()
    print("\nDone batch save and dashboard refresh!")

if __name__ == "__main__":
    main()
