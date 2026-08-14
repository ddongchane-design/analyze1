import os
import json
from pathlib import Path

pending_dir = Path("data/pending")
analyzed_base_dir = Path("data/analyzed")

def save_analysis(video_id, topic_id, data):
    dest_dir = analyzed_base_dir / topic_id
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_file = dest_dir / f"{video_id}.json"
    dest_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    
    pending_file = pending_dir / f"{video_id}.json"
    if pending_file.exists():
        pending_file.unlink()
    print(f"[Done] {video_id} -> data/analyzed/{topic_id}/{video_id}.json")

analyses = {
    "JwmI9HUiDzI": {
        "primary_topic": "stock",
        "secondary_topics": ["economy", "tech"],
        "tags": ["P&G실적", "연준딜레마", "OpenAI탈주", "매경월가월부", "어바웃뉴욕"],
        "summary": "P&G 실적에 반영된 소비 양극화와 연준의 장기 금리 고착화 딜레마 속에서, <span class=\"text-rose-400 font-medium\">OpenAI의 탈주 AI 모델 탈옥 피해보도</span>가 AI 통제 리스크를 유발하고 있습니다.",
        "key_claims": [
            "P&G 호실적에도 불구하고 필수소비재 가격 전가력이 한계에 부닥치며 <span class=\"text-rose-400 font-medium\">소비 양극화 경기 둔화 징후</span> 포착.",
            "연준 케빈 워시 의장의 포워드 가이던스 자제 스탠스로 <span class=\"text-amber-300 font-bold\">미 국채 장기 금리 상승 용인 딜레마</span> 지속.",
            "OpenAI 프런티어 모델의 보안 탈옥(Jailbreak) 피해가 확산되며 <span class=\"text-violet-300 font-medium\">미 정부의 국가 안보 통제 규제</span> 강화."
        ],
        "data_points": [
            "P&G 매출 및 마진율: 단가 인상 한계 부딪히며 유기적 성장률 3% 수준으로 축소",
            "미 국채 10년물 금리: 4.6%선에서 고착화"
        ],
        "signal": "neutral",
        "signal_reason": "소비재 호실적과 고금리/AI 규제 리스크가 교차하며 증시 상단을 제한하기 때문입니다.",
        "key_companies": ["P&G", "OpenAI", "매경월가월부"],
        "insight": "AI 모델이 고도화될수록 안보 및 탈옥 리스크에 대한 미국 정부의 규제망이 촘촘해지며 빅테크의 준수 비용이 늘어납니다.",
        "action_point": "안보 규제에 강한 빅테크 우량주 중심의 포트폴리오를 유지하고 금리 상단 지지력을 모니터링하십시오."
    },
    "Of_LDvvZmYA": {
        "primary_topic": "tech",
        "secondary_topics": ["stock", "robot"],
        "tags": ["엔비디아한국동맹", "AI공장", "SF_AI_Summit", "삼성SK현대차네이버", "안될공학"],
        "summary": "샌프란시스코 AI Summit에서 엔비디아가 <span class=\"text-cyan-300 font-semibold\">한국 전체를 거대한 AI 인프라 및 피지컬 로봇 공장</span>으로 묶는 대규모 한국 기업 동맹을 구체화했습니다.",
        "key_claims": [
            "엔비디아는 삼성(파운드리/HBM), SK(HBM), 현대차(피지컬AI/자율주행), 네이버(소버린AI)를 <span class=\"text-cyan-300 font-semibold\">글로벌 AI 풀스택 동맹</span>으로 통합.",
            "한국의 정밀 제조 하드웨어와 엔비디아의 CUDA/Omniverse 소프트웨어가 결합해 <span class=\"text-amber-300 font-bold\">글로벌 AI 공장 모델</span> 구축.",
            "K-반도체와 K-제조업이 엔비디아 생태계의 <span class=\"text-cyan-300 font-semibold\">대체 불가능한 핵심 하드웨어 기둥</span>으로 안착."
        ],
        "data_points": [
            "샌프란시스코 AI Summit 발표: 엔비디아-한국 주요 대기업 4사 풀스택 협력 프로젝트 발표",
            "HBM 및 피지컬 AI 칩 공급량: 2027년까지 전량 사전 수주 확정"
        ],
        "signal": "bullish",
        "signal_reason": "엔비디아가 한국을 독점적 HW 파트너로 격상시킴에 따라 반도체, 자동차, IT 대표주들의 이익 가시성이 가파르게 상향되기 때문입니다.",
        "key_companies": ["엔비디아", "삼성전자", "SK하이닉스", "현대차", "네이버"],
        "insight": "엔비디아는 한국을 단순 칩 구매자가 아니라 글로벌 AI 인프라와 피지컬 로봇을 동시 공급하는 핵심 제조 거점으로 점지했습니다.",
        "action_point": "엔비디아 동맹의 중심축인 SK하이닉스, 삼성전자, 현대차 중심의 포트폴리오 비중 확대를 강력 권고합니다."
    },
    "P0egm6fxTtI": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["마이크론폭등", "하이닉스ADR폭등", "워시의장", "팀쿡라스트댄스", "매경월가월부"],
        "summary": "월가 수급 마진콜 해소로 <span class=\"text-cyan-300 font-semibold\">마이크론과 SK하이닉스 ADR이 시간에 대폭등</span>하였으나, 미 연준의 장기 금리 상승 용인과 애플 주가 숨고르기가 연출되었습니다.",
        "key_claims": [
            "시타델의 숏커버링 및 마진콜 청산으로 <span class=\"text-cyan-300 font-semibold\">마이크론, SK하이닉스 ADR 주가 대폭등</span> 연출.",
            "케빈 워시 의장이 장기 금리 상승을 용인함에 따라 <span class=\"text-rose-400 font-medium\">기술주 밸류에이션 부담 일부 잔존</span>.",
            "팀 쿡의 라스트 댄스(폴더블/AI 시리 연동) 발표 속에 <span class=\"text-cyan-300 font-semibold\">애플 주가 단기 숨고르기 후 펀더멘털 탄탄</span>."
        ],
        "data_points": [
            "마이크론 및 SK하이닉스 ADR 상승 폭: 시간 외 10~15% 폭등 리바운드",
            "미국 국채 10년물 금리: 4.65% 상승세 기록"
        ],
        "signal": "bullish",
        "signal_reason": "메모리 반도체에 몰렸던 억울한 마진콜 폭락이 해소되며 대규모 숏커버링 폭등 장세가 가동되었기 때문입니다.",
        "key_companies": ["마이크론", "SK하이닉스", "애플", "매경월가월부"],
        "insight": "수급 상처가 치유된 메모리 반도체 대장주는 압도적인 숏커버링과 실적 상향 모멘텀을 바탕으로 V자 반등을 시도합니다.",
        "action_point": "시간 외 폭등세를 보이는 SK하이닉스 및 마이크론 관련 반도체 밸류체인 수혜주를 적극 보유하십시오."
    },
    "R4KQIYGwi_w": {
        "primary_topic": "tech",
        "secondary_topics": ["robot", "stock"],
        "tags": ["머스크Cybercab", "현대차테슬라", "자율주행동맹", "로보택시", "엔지니어TV"],
        "summary": "일론 머스크의 Cybercab 상용화 발언으로 <span class=\"text-cyan-300 font-semibold\">현대차와 테슬라의 자율주행 위탁 생산 및 부품 파트너십</span> 재결합 가능성이 부각되고 있습니다.",
        "key_claims": [
            "테슬라의 Cybercab 양산을 위해 <span class=\"text-cyan-300 font-semibold\">글로벌 완성차(현대차 등) 파운드리 위탁 생산</span> 타진.",
            "테슬라 FSD 생태계 확장이 <span class=\"text-amber-300 font-bold\">자율주행 센서, 카메라, 부품 밸류체인</span> 수요 폭증 유발.",
            "현대차그룹의 수직통합 제조 역량이 <span class=\"text-cyan-300 font-semibold\">글로벌 모빌리티 빅테크의 핵심 러브콜 대상</span>."
        ],
        "data_points": [
            "Cybercab 양산 목표 시점: 2026~2027년 연간 백만 대 체제 구축",
            "현대차 글로벌 생산 플랫폼 가동률: 미국 E-GMP 공장 가동률 호조"
        ],
        "signal": "bullish",
        "signal_reason": "테슬라의 자율주행 상용화 가속이 현대차 및 국내 자율주행 소부장 기업들의 주가 재평가를 이끌기 때문입니다.",
        "key_companies": ["테슬라", "현대차", "엔지니어TV"],
        "insight": "테슬라가 자율주행 모빌리티 시대를 열수록, 이를 안정적으로 생산할 수 있는 한국 대표 자동차 및 부품사의 가치가 치솟습니다.",
        "action_point": "현대차 및 테슬라 자율주행 카메라, 센서 공급망 대표주 중심의 중장기 투자를 추천합니다."
    },
    "SssjUghjVlo": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["아마존죽스", "Zoox면허", "로보택시전쟁", "테슬라추월", "매경월가월부"],
        "summary": "아마존의 자율주행 자회사 죽스(Zoox)가 테슬라보다 먼저 미국 운전석 없는 로보택시 상용 면허를 획득하며 <span class=\"text-cyan-300 font-semibold\">로보택시 주도권 전쟁</span>이 심화되고 있습니다.",
        "key_claims": [
            "아마존 죽스(Zoox)가 무운전석 전용 로보택시 면허를 획득해 <span class=\"text-cyan-300 font-semibold\">상용화 속도에서 테슬라 우위</span> 확보.",
            "웨이모, 죽스, 테슬라 간 3파전 구도로 <span class=\"text-amber-300 font-bold\">글로벌 자율주행 인프라 경쟁</span> 격화.",
            "자율주행 서비스 경쟁 심화로 <span class=\"text-violet-300 font-medium\">센서, 라이더, 차세대 통신 부품</span> 수요 폭발."
        ],
        "data_points": [
            "아마존 죽스 로보택시 면허: 캘리포니아/네바다 도로 무운전석 상용 주행 승인",
            "로보택시 시장 예상 규모: 2030년까지 1,200억 달러 팽창"
        ],
        "signal": "bullish",
        "signal_reason": "아마존 등 빅테크들의 로보택시 상용 면허 획득이 자율주행 산업 전체의 실질 매출 전환을 앞당기기 때문입니다.",
        "key_companies": ["Amazon", "Zoox", "Waymo", "Tesla"],
        "insight": "로보택시 경쟁은 개념 단계를 지나 빅테크 간 승인 면허 및 실질 서비스 과금 경쟁으로 돌입했습니다.",
        "action_point": "아마존 및 빅테크 자율주행 밸류체인 수혜주 비중 확대를 권고합니다."
    }
}

for vid, data in analyses.items():
    topic_id = data["primary_topic"]
    pending_file = pending_dir / f"{vid}.json"
    if not pending_file.exists():
        continue
        
    full_json = {
        "video": json.loads(pending_file.read_text(encoding="utf-8"))["video"],
        "analysis": {
            "summary": data["summary"],
            "key_claims": data["key_claims"],
            "data_points": data["data_points"],
            "signal": data["signal"],
            "signal_reason": data["signal_reason"],
            "key_companies": data["key_companies"],
            "insight": data["insight"],
            "action_point": data["action_point"]
        },
        "classification": {
            "primary_topic": topic_id,
            "secondary_topics": data["secondary_topics"],
            "tags": data["tags"]
        }
    }
    save_analysis(vid, topic_id, full_json)

print("\n[SUCCESS] All 5 latest pending videos analyzed!")
