import json
from pathlib import Path

batch6 = [
    {
        "video": {
            "id": "kHk-7FPHA3w",
            "title": "[어바웃 뉴욕] 미국 젊은이들이 콜라 대신 마시는 것 | 펩시는 2조를 냈고, 코카콜라는 따라 만들었다 | 이나연 특파원",
            "published": "2026-08-01T03:00:07+00:00",
            "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=kHk-7FPHA3w",
            "thumbnail": "https://img.youtube.com/vi/kHk-7FPHA3w/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미국 MZ세대를 기점으로 탄산음료 대신 프리바이오틱스 및 저당 유기농 음료(<span class=\"text-cyan-300 font-semibold\">올리팝 Olipop / 포비 오비 Poppi</span>) 시장이 폭발적으로 성장하는 트렌드를 전함. 펩시코와 코카콜라 등 글로벌 기성 음료 거인들이 조 단위 M&A 및 미투 제품으로 신흥 건강 탄산음료 시장을 선점하려는 전쟁을 다룸.",
            "key_claims": [
                "미국 젊은 층의 탈(脫)설탕 건강 음료 선호가 펩시/코카콜라의 전통 콜라 매출을 위협함.",
                "기성 음료 빅테크 기업들이 프리바이오틱스 신생 음료 브랜드를 인수하거나 자체 라인업을 강화하며 소비재 재편 진행 중."
            ],
            "data_points": [
                "올리팝/포비 매출 성장률 및 인수 제안 규모: 약 2조 원(20억 달러) 평가"
            ],
            "signal": "bullish",
            "signal_reason": "웰빙 헬스케어 음료라는 확실한 소비 패턴 변화로 신흥 음료 및 펩시/코카콜라의 신사업 인수 모멘텀이 발생하기 때문임.",
            "key_companies": ["코카콜라(KO)", "펩시코(PEP)", "올리팝(Olipop)", "포비(Poppi)"],
            "insight": "소비재 트렌드는 설탕 과다 음료에서 대사 건강을 돕는 기능성 음료로 이동하고 있으며, 이는 필수 소비재 거인들의 지형을 바꾸는 M&A 촉매임.",
            "action_point": "코카콜라, 펩시코 등 글로벌 소비재 기업들의 신규 브랜딩/인수 행보와 웰빙 음료 기업 밸류체인 체크."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["미국소비재", "올리팝", "코카콜라", "펩시코", "프리바이오틱스"]
        }
    },
    {
        "video": {
            "id": "n0EKpePXvFE",
            "title": "슈퍼태풍을 만드는 바다의 비밀?!",
            "published": "2026-08-01T11:00:31+00:00",
            "channel_name": "안될과학 Unrealscience",
            "url": "https://www.youtube.com/watch?v=n0EKpePXvFE",
            "thumbnail": "https://img.youtube.com/vi/n0EKpePXvFE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "지구 온난화로 인한 해수면 온도 상승이 슈퍼태풍의 에너지원이 되어 발풍 강도와 파괴력을 극대화하는 수온 대류 메커니즘을 설명함. 기후 변화에 따른 열대성 저기압의 이상 급증 현상을 다룸.",
            "key_claims": [
                "해수면 온도가 26.5°C 이상 유지될 때 슈퍼태풍으로 성장할 대규모 수증기 에너지가 공급됨.",
                "지구 온난화가 가속될수록 태풍의 이동 속도가 둔화되고 강수량이 극대화되어 피해가 심화됨."
            ],
            "data_points": [
                "슈퍼태풍 발달을 위한 해수면 임계 온도: 26.5°C 이상"
            ],
            "signal": "na",
            "signal_reason": "기상학 및 기후 이상 현상을 설명하는 순수 과학 숏폼 지식 영상임.",
            "key_companies": [],
            "insight": "해수면 온도 상승에 따른 슈퍼태풍 위협 증대는 기후 재난 방재 시스템 및 수해 예방 인프라 수요를 지속적으로 강화함.",
            "action_point": "기후 재해 방재 및 환경 인프라 관련 모멘텀 상식 수준 참고."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": ["energy"],
            "tags": ["슈퍼태풍", "해수면온도", "지구온난화", "기후재난"]
        }
    },
    {
        "video": {
            "id": "oHUsR6mnN70",
            "title": "\"적게 먹는데 왜 안 빠지지?\" 양보다 '이것'을 줄이세요 #교양이를부탁해 #비만 #다이어트 #체중감량",
            "published": "2026-08-02T11:00:20+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=oHUsR6mnN70",
            "thumbnail": "https://img.youtube.com/vi/oHUsR6mnN70/hqdefault.jpg"
        },
        "analysis": {
            "summary": "칼로리 섭취 양보다 <span class=\"text-rose-400 font-medium\">액상당과 정제 탄수화물 비율</span>이 혈당 스파이크 및 지방 축적을 직접 유발함을 지적함. 대사율을 떨어뜨리지 않으면서 감량하기 위한 식단 영양소 조율의 중요성을 해설함.",
            "key_claims": [
                "식사량을 극단적으로 줄이면 인체가 방어 모드로 전환되어 기초대사량이 폭락함.",
                "액상과당 섭취 차단이 혈당 스파이크와 체지방 합성 억제의 핵심 열쇠임."
            ],
            "data_points": [],
            "signal": "na",
            "signal_reason": "식단 조절 및 대사 질환 예방 지식을 다루는 숏폼 바이럴 콘텐츠임.",
            "key_companies": [],
            "insight": "식품 소비 트렌드가 칼로리 수치보다 저당/제로 당류 위주로 고착화되는 대사 건강 패러다임을 반영함.",
            "action_point": "대사 건강 식품 및 저당 헬스케어 관련 소비재 흐름 체크."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["액상과당", "혈당스파이크", "다이어트", "대사건강"]
        }
    },
    {
        "video": {
            "id": "qEE3rkGo8AY",
            "title": "현대차 아틀라스 공장이 끝이 아니다… 다음 목적지는 주방",
            "published": "2026-08-02T10:14:19+00:00",
            "channel_name": "엔지니어TV",
            "url": "https://www.youtube.com/watch?v=qEE3rkGo8AY",
            "thumbnail": "https://img.youtube.com/vi/qEE3rkGo8AY/hqdefault.jpg"
        },
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">현대차그룹 보스턴다이나믹스</span>의 차세대 휴머노이드 로봇 아틀라스(Atlas)가 자동차 제조 공장 투입을 넘어, 주방 및 가정/서비스 산업으로 적용 범위를 조기 확장을 추진 중임을 해설함. 구글 Gemini Robotics 2 등 최첨단 물리 AI 모델 탑재와 결합하여 범용 가정/상업용 로봇으로 상용화 속도를 올리고 있음.",
            "key_claims": [
                "아틀라스의 목적지는 단순 현대차 공장 자동화를 넘어 주방 및 가정용 범용 서비스 로봇임.",
                "전동식 파워트레인 도입으로 유압식의 단점(소음, 오일 누유)을 완벽히 극복하여 가정 진입 여건이 완성됨."
            ],
            "data_points": [
                "보스턴다이나믹스 전동식 아틀라스 관절 가동 범위 및 탑재 피지컬 AI 모델 규격"
            ],
            "signal": "bullish",
            "signal_reason": "휴머노이드 로봇의 적용 처가 공장에서 주방/가정으로 급격히 확대되며 현대차그룹의 피지컬 AI 가치가 급상승하기 때문임.",
            "key_companies": ["현대차(005380)", "보스턴다이나믹스", "구글(GOOGL)"],
            "insight": "현대차는 자동차 제조사를 넘어 보스턴다이나믹스의 전동식 휴머노이드와 구글 브레인을 결합한 글로벌 피지컬 AI 로봇 거인으로 재평가됨.",
            "action_point": "현대차그룹의 로봇 상용화 로드맵과 보스턴다이나믹스 밸류체인(부품/액추에이터) 매수 관점 접근."
        },
        "classification": {
            "primary_topic": "robot",
            "secondary_topics": ["stock", "tech"],
            "tags": ["아틀라스", "보스턴다이나믹스", "현대차", "서비스로봇", "피지컬AI"]
        }
    },
    {
        "video": {
            "id": "sb6Xd3Wj_eA",
            "title": "[지식뉴스] “AI가 무너진 게 아니다, 빚투가 무너진 것”…빅테크는 그렇게 쉽게 끝나지 않는다, 지금부터 놓치면 안 될 진짜 신호 / 교양이를 부탁해",
            "published": "2026-08-02T00:06:15+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=sb6Xd3Wj_eA",
            "thumbnail": "https://img.youtube.com/vi/sb6Xd3Wj_eA/hqdefault.jpg"
        },
        "analysis": {
            "summary": "최근 AI 거품론과 주가 급락의 본질이 AI 기술의 한계가 아니라, 과도하게 레버리지를 일으킨 <span class=\"text-rose-400 font-medium\">파생 상품 및 빚투 수급의 붕괴(마진콜)</span>였음을 명쾌히 입증함. 엔비디아, 아마존, 마이크로소프트 등 독점적 현금 창출력을 지닌 빅테크는 비즈니스 모델이 견고하며 수급 청산 후 주가가 재반등할 핵심 신호를 제시함.",
            "key_claims": [
                "AI 실적이나 기술이 무너진 것이 아니라 레버리지 롱 포지션 청산으로 인한 과도한 주가 가곡 현상임.",
                "빅테크들의 AI 설비 투자(CapEx)와 클라우드 매출 성장은 역사적 고점 기조를 유지함.",
                "수급 노이즈가 걷히면 진성 이익을 내는 빅테크 및 메모리 반도체가 가장 먼저 랠리를 재개할 것임."
            ],
            "data_points": [
                "미국 레버리지 ETF 및 수급 청산액 통계",
                "빅테크 4사(M7) 누적 현금 보유액 및 영업이익률"
            ],
            "signal": "bullish",
            "signal_reason": "레버리지 수급 붕괴가 마무리되고 실적 기반 빅테크 펀더멘털로 매수세가 강력히 재유입될 타점이기 때문임.",
            "key_companies": ["엔비디아(NVDA)", "아마존(AMZN)", "마이크로소프트(MSFT)", "SK하이닉스(000660)"],
            "insight": "시장의 투매는 '빚투 수급'의 청산에서 비롯되었으며, 펀더멘털이 짱짱한 빅테크에게 이번 폭락은 훌륭한 바겐세일 기회를 제공함.",
            "action_point": "공포 심리로 인한 하락 구간에서 엔비디아 및 실적 우량 기술주 포트폴리오 비중 확대."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["AI빚투붕괴", "마진콜청산", "빅테크펀더멘털", "교양이를부탁해", "기술주반등"]
        }
    },
    {
        "video": {
            "id": "y_plKrU-Qk4",
            "title": "인간의 뇌는 원래 주식하면 망하게 설계됐다 (김나영 경제전문작가)",
            "published": "2026-08-02T11:55:32+00:00",
            "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=y_plKrU-Qk4",
            "thumbnail": "https://img.youtube.com/vi/y_plKrU-Qk4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "행동경제학과 뇌과학 관점에서 인간의 편향(손실 회피 심리, 처분 효과, 군중 심리)이 주식 투자 시 <span class=\"text-rose-400 font-medium\">손실을 극대화하는 본능적 오류</span>를 일으킴을 설명함. 뇌의 본능을 역행하여 원칙 기반의 시스템 매매와 장기 투자 규율을 확립하는 방법을 솔루션으로 제시함.",
            "key_claims": [
                "인간의 뇌는 손실의 고통을 이익의 기쁨보다 2배 이상 크게 느껴 이익은 조기 확정하고 손실은 끝까지 방치함(처분 효과).",
                "투자의 성공은 뇌의 본능(군중 추종, 뇌동매매)을 극복하고 규칙에 따라 원칙 매매를 집행하는 능력에 달렸음."
            ],
            "data_points": [
                "행동경제학 손실 회피 계수 (약 2.25배 손실 고통 인식)"
            ],
            "signal": "neutral",
            "signal_reason": "행동경제학 및 투자 심리 원칙을 전하는 교육적 내용임.",
            "key_companies": [],
            "insight": "투자에서 가장 큰 적은 외부 시장이 아닌 인간 본능의 뇌 편향이며, 이를 통제하는 시스템 규율이 성공적인 장기 성과를 결정함.",
            "action_point": "뇌동매매 방지를 위한 손절/익절 원칙 수립 및 적립식 자동화 매매 프로세스 도입."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["행동경제학", "투자심리", "처분효과", "김나영", "뇌동매매방지"]
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
    save_batch(batch6)
