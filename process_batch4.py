import json
from pathlib import Path

batch4 = [
    {
        "video": {
            "id": "PnBKOqhrN6Q",
            "title": "양산 42.5°C ‘극한폭염‘ 대한민국 역대 최고기록! 이번주는 중부지방 폭염시작! 무엇이 대한민국을 끓게 만드나?",
            "published": "2026-08-02T00:00:21+00:00",
            "channel_name": "안될과학 Unrealscience",
            "url": "https://www.youtube.com/watch?v=PnBKOqhrN6Q",
            "thumbnail": "https://img.youtube.com/vi/PnBKOqhrN6Q/hqdefault.jpg"
        },
        "analysis": {
            "summary": "경남 양산 42.5°C 등 대한민국 관측 이래 최악의 <span class=\"text-rose-400 font-medium\">극한 폭염 기후 위기</span>가 기조적으로 발생한 원인을 기열 해수면 온도 상승, 열돔 현상, 기후 변화 기조 관점에서 기상학적으로 정밀 해설함. 전력 피크 수요 경신과 기후 적응 인프라 및 친환경 에너지 전환 필요성이 급부상함.",
            "key_claims": [
                "북태평양 고기압과 티베트 고기압의 이중 열돔(Heat Dome) 형성이 기온 폭등의 직접적 원인임.",
                "지구 온난화에 따른 기후 이상은 단순 일회성 여름 폭염이 아닌 재난 수준의 인프라 위기로 고착화되는 중임."
            ],
            "data_points": [
                "경남 양산 일일 최고 기온: 42.5°C (대한민국 역대 최고 관측 기록 경신)"
            ],
            "signal": "neutral",
            "signal_reason": "기후재난 리스크가 증대하는 가운데 전력 수급 및 기후 적응 인프라 관련 수요가 발생하는 대립 구간임.",
            "key_companies": ["한국전력(015760)"],
            "insight": "극한 기후의 고착화는 국가 전력망 과부하와 피크 전력 관리, 스마트 그리드 및 원전·신재생 에너지 벨류체인의 구조적 가치를 재평가하게 함.",
            "action_point": "전력망 확충 및 냉방/에너지 효율화 관련 기업들의 계절적 및 구조적 모멘텀 체크."
        },
        "classification": {
            "primary_topic": "energy",
            "secondary_topics": ["etc", "economy"],
            "tags": ["극한폭염", "열돔현상", "양산42.5도", "기후위기", "전력피크"]
        }
    },
    {
        "video": {
            "id": "SHE76Ss4dPE",
            "title": "\"딱 이것만\" 해주면 20년뒤 당신의 자녀는 억단위 자산가가 됩니다",
            "published": "2026-08-01T05:22:47+00:00",
            "channel_name": "이효석아카데미",
            "url": "https://www.youtube.com/watch?v=SHE76Ss4dPE",
            "thumbnail": "https://img.youtube.com/vi/SHE76Ss4dPE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "장기 적립식 주식 투자의 복리 효과와 글로벌 시장 1등 자산(<span class=\"text-cyan-300 font-semibold\">미국 빅테크 S&P500/나스닥 ETF</span>)을 장기 적립하는 자녀 증여 및 자산 배분 노하우를 공개함. 단기 시장 변동성에 흔들리지 않고 자본주의 성장의 결실을 장기 보유하는 복리의 위력을 실증 사례로 설명함.",
            "key_claims": [
                "자녀 명의의 지수 연동 ETF 장기 적립식 배분은 복리 시간 가치를 극대화하는 최고의 증여 전략임.",
                "개별 종목의 단기 노이즈보다 글로벌 우상향 시장 인덱스를 20년 이상 꾸준히 모아가는 실행력이 결정적임."
            ],
            "data_points": [
                "월 10~30만 원 20년 복리적립 투자 시 예상 자산 형성 스케일 (복리 수익률 10% 가정)"
            ],
            "signal": "bullish",
            "signal_reason": "글로벌 대표 기술주 및 인덱스 장기 투자 펀더멘털의 구조적 유효성을 재확인해주기 때문임.",
            "key_companies": ["애플(AAPL)", "엔비디아(NVDA)", "마이크로소프트(MSFT)"],
            "insight": "투자의 핵심 비밀은 타이밍 잡기가 아닌 '시간과 복리'에 있으며, 글로벌 독점기업 장기 보유가 자산 격차를 극복하는 가장 강력한 수단임.",
            "action_point": "자녀 증여 계좌 활용 S&P500 / 미국 빅테크 ETF 장기 적립식 스케줄 실행."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["장기투자", "복리효과", "자녀증여", "S&P500", "이효석"]
        }
    },
    {
        "video": {
            "id": "SNkD-olCMXY",
            "title": "미국 레버리지 펀드의 몰락…반도체 랠리 다시 시작되나 | 반도체만 있는게 아니다 선박·뷰티까지…수출, 1조 달러 가시화 | 권순우 삼프로TV 취재팀장 [뉴스3]",
            "published": "2026-08-02T23:06:42+00:00",
            "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=SNkD-olCMXY",
            "thumbnail": "https://img.youtube.com/vi/SNkD-olCMXY/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미국 증시에서 과도한 레버리지 펀드 물량이 청산되며 청신호가 켜진 가운데, 반도체 랠리 재개 가능성과 더불어 <span class=\"text-cyan-300 font-semibold\">한국의 조선(선박) 및 K-뷰티</span> 등 다각화된 호조로 대한민국 연간 수출 1조 달러 달성 호재를 정밀 진단함.",
            "key_claims": [
                "레버리지 매도 수급 청산 완료로 반도체 랠리의 제약 요인이 해소됨.",
                "한국 수출 호조는 반도체 외에도 K-조선 수주잔고와 뷰티/의료기기 해외 침투율 확대로 체질이 강화되고 있음."
            ],
            "data_points": [
                "대한민국 연간 누적 수출 목표치: 1조 달러 가시화",
                "조선업종 고가 선가 수주잔고 확보 기간: 3.5년 치 달성"
            ],
            "signal": "bullish",
            "signal_reason": "레버리지 수급 청산 및 반도체·조선·K뷰티 전반의 강력한 수출 실적 펀더멘털이 동반 확인되기 때문임.",
            "key_companies": ["SK하이닉스(000660)", "HD한국조선해양(009540)", "HD현대중공업(329180)", "실리콘투(257720)"],
            "insight": "한국 증시의 상승 동력은 반도체 단일 엔진을 넘어 조선, 뷰티, 방산 등으로 다변화되어 주가 펀더멘털 하단이 한층 견고해짐.",
            "action_point": "반도체 주도주와 함께 조선 업황(고선가 수주) 및 글로벌 뷰티 수출 수혜주 포트폴리오 다변화."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["레버리지청산", "반도체랠리", "수출1조달러", "K조선", "권순우"]
        }
    },
    {
        "video": {
            "id": "Sv5FxR_k00E",
            "title": "구글 Gemini Robotics 2 공개... 다음은 아틀라스일까?",
            "published": "2026-08-01T10:22:41+00:00",
            "channel_name": "엔지니어TV",
            "url": "https://www.youtube.com/watch?v=Sv5FxR_k00E",
            "thumbnail": "https://img.youtube.com/vi/Sv5FxR_k00E/hqdefault.jpg"
        },
        "analysis": {
            "summary": "구글 딥마인드가 발표한 차세대 물리 AI 모델 <span class=\"text-cyan-300 font-semibold\">Gemini Robotics 2 (ER)</span>의 실체를 다룸. 정밀 양손 조작(쓰레기봉투 묶기, 전구 교체, 지퍼백 제어)과 전신 제어(Whole Body Control) 능력을 시연하며, 하드웨어 중립적 안드로이드 방식 로봇 OS 플랫폼으로 보스턴다이나믹스 아틀라스(Atlas) 등 다양한 휴머노이드에 이식될 가능성을 분석함.",
            "key_claims": [
                "구글 Gemini Robotics 2는 비정형 유체/물체에 대한 정밀 촉각·시각 교차 피드백 제어에서 비약적 진전을 이룸.",
                "테슬라(수직통합 아이폰 방식)와 달리 구글은 다양한 로봇 하드웨어 파트너에 범용 Brain을 공급하는 '로봇판 안드로이드' 전략을 추진함."
            ],
            "data_points": [
                "Gemini Robotics 2 시연 성능: 자율 1배속 실제 환경 정밀 양손 조작 성공"
            ],
            "signal": "bullish",
            "signal_reason": "피지컬 AI 브레인 파운데이션 모델의 상용화가 임박함에 따라 휴머노이드 로봇 생태계 확장이 가속화될 것이기 때문임.",
            "key_companies": ["구글(GOOGL)", "보스턴다이나믹스", "현대차(005380)", "Apptronik"],
            "insight": "구글의 로봇 OS 플랫폼 진입은 휴머노이드 하드웨어 제조사들에게 신속한 범용 지능 탑재 기회를 제공하여 상용화 시점을 앞당김.",
            "action_point": "구글 피지컬 AI 파트너십을 맺은 로봇 하드웨어/액추에이터 및 현대차 그룹(보스턴다이나믹스) 모멘텀 주목."
        },
        "classification": {
            "primary_topic": "robot",
            "secondary_topics": ["tech", "stock"],
            "tags": ["GeminiRobotics2", "구글딥마인드", "피지컬AI", "아틀라스", "휴머노이드"]
        }
    },
    {
        "video": {
            "id": "UxVSXWFny7A",
            "title": "레버리지 청산 끝..이 모든 건 시타델의 작전이었던 걸까 | 월가백브리핑",
            "published": "2026-08-01T03:00:28+00:00",
            "channel_name": "한경 글로벌마켓",
            "url": "https://www.youtube.com/watch?v=UxVSXWFny7A",
            "thumbnail": "https://img.youtube.com/vi/UxVSXWFny7A/hqdefault.jpg"
        },
        "analysis": {
            "summary": "월가 헤지펀드(시타델 등)의 수급 플레이와 대규모 레버리지 파생상품 청산이 단기 기술주 급락을 유발한 메커니즘을 분석함. 청산 폭풍이 마무리 단계에 접어들며 수급 악재가 소멸하고, 빅테크 펀더멘털로의 <span class=\"text-amber-300 font-bold\">주가 회귀 및 매수세 유입</span>이 가시화됨을 설명함.",
            "key_claims": [
                "시타델 등 대형 헤지펀드의 옵션 변동성 매매와 레버리지 청산이 과도한 낙폭을 유발했음.",
                "수급성 폭락 종료 후 펀더멘털 실적이 뛰어난 반도체 및 빅테크 종목 중심으로 급반등이 전개될 것임."
            ],
            "data_points": [
                "월가 레버리지 청산 규모 및 VIX 지수 변동폭 데이터"
            ],
            "signal": "bullish",
            "signal_reason": "인위적 파생 수급 악재 청산이 완료됨에 따라 억눌렸던 빅테크 매수세가 재개될 구간이기 때문임.",
            "key_companies": ["시타델", "엔비디아(NVDA)", "애플(AAPL)"],
            "insight": "월가 헤지펀드의 포지션 청산은 단기 주가 가곡현상을 만들지만, 수급 안개 소멸 후 주가는 본래의 기업 실력(EPS)으로 수렴함.",
            "action_point": "헤지펀드 수급 청산 종료 시점을 기술주 저점 매수 기회로 삼는 대응 권장."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["월가백브리핑", "시타델", "레버리지청산", "헤지펀드", "변동성매매"]
        }
    },
    {
        "video": {
            "id": "VrloORxOLoA",
            "title": "구글 로봇 경쟁자는 테슬라가 아닙니다... Gemini Robotics 2에서 밝혀진, 로봇판 안드로이드 등장",
            "published": "2026-08-01T09:18:24+00:00",
            "channel_name": "안될공학 - IT 테크 신기술",
            "url": "https://www.youtube.com/watch?v=VrloORxOLoA",
            "thumbnail": "https://img.youtube.com/vi/VrloORxOLoA/hqdefault.jpg"
        },
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">구글 Gemini Robotics 2</span>의 핵심 경쟁력이 특정 수직통합 하드웨어(테슬라 방식)가 아닌, 다양한 로봇 폼팩터에 이식 가능한 <span class=\"text-cyan-300 font-semibold\">'로봇판 안드로이드(범용 VLA 모델)'</span> 생태계 구축에 있음을 분석함. 전신 제어(Whole Body Intelligence)와 정밀 양손 조작 능력이 공장 및 가정용 휴머노이드 상용화를 가속화할 것임.",
            "key_claims": [
                "구글은 로봇 하드웨어 직접 제조보다 범용 피지컬 AI 파운데이션 모델(VLA)을 공급하는 플랫폼 거인이 되고자 함.",
                "테슬라의 옵티머스 수직통합 모델에 대항하여, 현대차 아틀라스 및 글로벌 로봇 폼팩터들이 구글 브레인 생태계로 진입 중임."
            ],
            "data_points": [
                "Gemini Robotics 2 기반 VLA 추론 및 전신 제어 모듈 반응 속도 데이터"
            ],
            "signal": "bullish",
            "signal_reason": "범용 로봇 OS 및 VLA 파운데이션 모델 경쟁 가열로 피지컬 AI 분야 투자가 폭발할 것이기 때문임.",
            "key_companies": ["구글(GOOGL)", "테슬라(TSLA)", "현대차(005380)"],
            "insight": "스마트폰 시장에서 iOS 대 안드로이드 구도가 형성되었듯, 휴머노이드 로봇 시장에서도 테슬라 수직통합과 구글 범용 OS 동맹의 양강 체제가 개막됨.",
            "action_point": "구글 로봇 OS 오픈 생태계에 참여하는 로봇 부품사(감속기, 액추에이터, 센서) 중심 투자 검토."
        },
        "classification": {
            "primary_topic": "robot",
            "secondary_topics": ["tech", "stock"],
            "tags": ["GeminiRobotics2", "로봇안드로이드", "안될공학", "피지컬AI", "VLA"]
        }
    }
]

def save_batch(batch):
    for item in batch:
        primary = item["classification"]["primary_topic"]
        vid = item["video"]["id"]
        out_dir = Path(f"data/analyzed/{primary}")
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{vid}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
        print(f"[저장 완료] {out_file}")
        
        pending_file = Path(f"data/pending/{vid}.json")
        if pending_file.exists():
            pending_file.unlink()
            print(f"[삭제 완료] {pending_file}")

if __name__ == "__main__":
    save_batch(batch4)
