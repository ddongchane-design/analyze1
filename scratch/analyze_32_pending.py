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
    "18d4SRbPszs": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["삼성전자확정실적", "반도체혼란", "오후방송", "삼프로TV"],
        "summary": "삼성전자의 호실적 발표에도 불구하고 외국인 수급 변동성으로 시장 혼란이 지속되었으나, <span class=\"text-cyan-300 font-semibold\">실적 가치 하단 지지력</span>이 확인되었습니다.",
        "key_claims": [
            "삼성전자 2분기 확실한 실적에도 수급 불균형으로 <span class=\"text-rose-400 font-medium\">단기 주가 왜곡</span> 발생.",
            "메모리 판가 상승 및 HBM 공급 타이트는 변함없어 <span class=\"text-cyan-300 font-semibold\">주가 반등의 기본 체력</span> 형성.",
            "8월 수급 회복 시 <span class=\"text-amber-300 font-bold\">빠른 이격 축소 리바운드</span> 기대."
        ],
        "data_points": [
            "삼성전자 2분기 영업이익: 확정 실적 발표 및 메모리 마진 대폭 상향",
            "코스피 반도체 하방 지지선: PBR 0.85배 수준에서 매수세 형성"
        ],
        "signal": "bullish",
        "signal_reason": "확정 실적 발표로 이익 상향 가시성이 확보되었기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "수급 왜곡으로 실적이 무시되는 장세는 정석적인 저가 분할 매수의 최적 타점입니다.",
        "action_point": "삼성전자 및 반도체 대표주의 분할 매수를 추천합니다."
    },
    "2FOTy7qBClw": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["AI청구서", "여의도인사이트", "송재경", "삼프로TV"],
        "summary": "AI 쏠림 장세의 조정 청구서가 날아왔으나, <span class=\"text-rose-400 font-medium\">지금 시장을 완전히 이탈하면 향후 반등 재진입이 어렵다</span>고 경고합니다.",
        "key_claims": [
            "단기 조정 공포로 전량 투매하고 이탈하는 것은 <span class=\"text-rose-400 font-medium\">가장 최악의 대응</span>이다.",
            "시장 반등은 선제적 신호 없이 급격히 연출되므로 <span class=\"text-cyan-300 font-semibold\">우량 포트폴리오 유지</span>가 필수적이다.",
            "CapEx 투자 수익화 속도에 따라 <span class=\"text-amber-300 font-bold\">차세대 실적주 옥석 가리기</span> 진행."
        ],
        "data_points": [
            "과거 강세장 조정 후 이탈자 재진입 실패율: 70% 이상 손실 확정",
            "S&P 500 장기 연평균 수익률: 10% 유지"
        ],
        "signal": "bullish",
        "signal_reason": "시장을 패닉 이탈하기보다 펀더멘털을 가진 포트폴리오를 지키는 것이 장기 이익을 보장하기 때문입니다.",
        "key_companies": ["디멘젼투자자문"],
        "insight": "공포 시점의 이탈은 반등 상승분을 놓치게 만들므로, 우량 자산을 쥐고 버티는 포지션이 유리합니다.",
        "action_point": "투매 대신 우량 대형주 위주의 포트폴리오 재편을 추천합니다."
    },
    "4qNjua1pX5I": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["8월증시반전", "주린이구조대", "삼프로TV", "바닥확인"],
        "summary": "끝없는 하락은 없으며, <span class=\"text-cyan-300 font-semibold\">8월 증시 반전의 조건(수급 멈춤 및 어닝 서프라이즈)</span>이 충족되고 있습니다.",
        "key_claims": [
            "7월 무차별 폭락은 지나쳤으며 <span class=\"text-cyan-300 font-semibold\">8월 기술적 반등 조건</span> 성숙.",
            "외국인 수급 청산 마무리와 함께 <span class=\"text-amber-300 font-bold\">주요 대형주 리바운드</span> 시작.",
            "공포에 질린 손절보다 <span class=\"text-cyan-300 font-semibold\">반등 수혜주 선점</span>이 시급."
        ],
        "data_points": [
            "8월 역사적 반등 확률: 과매도 진입 후 85% 이상 상승 전환",
            "외국인 선물 숏포지션 청산 지표 관찰"
        ],
        "signal": "bullish",
        "signal_reason": "8월 반등 조건이 마련되어 수급 및 주가 복원력이 작동할 것이기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "폭락 후 반등 직전의 8월 길목은 가장 매력적인 수익률 구간을 제공합니다.",
        "action_point": "반도체 및 시총 상위 대형주 중심 저가 매수를 추천합니다."
    },
    "8F-cYdY6MX4": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["미국GDP", "PCE물가", "김현석브레이킹", "한경글로벌마켓"],
        "summary": "미국 2분기 GDP 견조함과 6월 PCE 물가 안정이 확인되며 <span class=\"text-cyan-300 font-semibold\">골디락스 연착륙 가능성</span>이 높아졌습니다.",
        "key_claims": [
            "6월 PCE 물가가 예상치에 부합하며 <span class=\"text-cyan-300 font-semibold\">인플레이션 완화 안도감</span> 제공.",
            "2분기 GDP 성장률이 소비에 힘입어 견조하여 <span class=\"text-amber-300 font-bold\">경기 후퇴 우려를 상쇄</span>.",
            "연준 통화 정책의 <span class=\"text-cyan-300 font-semibold\">유연한 정책 운용 여지</span> 확보."
        ],
        "data_points": [
            "미국 2분기 GDP 성장률: 연율 2.8% 기록 (예상 상회)",
            "6월 근원 PCE 물가 상승률: 전년 대비 2.6%로 하향 안정"
        ],
        "signal": "bullish",
        "signal_reason": "미국 거시 경기의 튼튼함과 물가 완화라는 골디락스 환경이 증시 하방을 지지하기 때문입니다.",
        "key_companies": ["한경글로벌마켓", "연준"],
        "insight": "거시 지표가 골디락스를 가리키고 있어 고금리 속에서도 우량 기업들의 실적 우상향이 가능합니다.",
        "action_point": "미국 증시 패시브 자산 및 글로벌 우량주 편입을 지속하십시오."
    },
    "Cp3z18HItfg": {
        "primary_topic": "crypto",
        "secondary_topics": ["stock"],
        "tags": ["크립토PLUS", "FOMC동결", "9월인하설", "블록미디어", "삼프로TV"],
        "summary": "연준 7월 금리 동결에도 불구하고 시장의 시선은 <span class=\"text-cyan-300 font-semibold\">9월 금리 인하 신호론</span>으로 향하며 가상자산 반등 기반을 타진 중입니다.",
        "key_claims": [
            "7월 동결 성명서 내 매파적 어조에도 불구하고 <span class=\"text-cyan-300 font-semibold\">9월 인하 기대감 상존</span>.",
            "비트코인 등 가상자산이 <span class=\"text-amber-300 font-bold\">유동성 환경 개선 신호</span>에 민감하게 반응.",
            "제도권 자금 유입과 함께 <span class=\"text-violet-300 font-medium\">크립토 시장 하방 경직성</span> 강화."
        ],
        "data_points": [
            "9월 금리 인하 확률: 피드워치 기준 75% 반영",
            "비트코인 지지선: 63,000달러선 탄탄한 지지"
        ],
        "signal": "neutral",
        "signal_reason": "9월 피벗 기대를 모니터링해야 하는 과도기 구간이기 때문입니다.",
        "key_companies": ["블록미디어", "Coinbase"],
        "insight": "크립토 자산은 연준의 9월 금리 인하 기대감이 가시화될 때 가장 강한 탄력을 보여줍니다.",
        "action_point": "비트코인 및 가상자산 대표 인프라 종목의 분할 관망 매수를 추천합니다."
    },
    "drswbn2Fu8A": {
        "primary_topic": "economy",
        "secondary_topics": ["etc"],
        "tags": ["후티반군", "미군두손", "언더스탠딩", "중동지정학"],
        "summary": "예멘 후티 반군의 비대칭 드론/미사일 전략으로 <span class=\"text-rose-400 font-medium\">홍해 해상 물류 마비 및 군사비 비대칭성</span> 문제가 장기화되고 있습니다.",
        "key_claims": [
            "저가 드론과 지대함 미사일을 활용한 후티의 비대칭 공격에 <span class=\"text-rose-400 font-medium\">미군 및 우방국 방공 비용 부담</span> 가중.",
            "홍해 우회 항로 이용으로 <span class=\"text-amber-300 font-bold\">글로벌 해운 운임 및 물류비 상승</span> 고착화.",
            "비대칭 방공 및 안티드론 시스템의 <span class=\"text-cyan-300 font-semibold\">군사적 가치 급상승</span>."
        ],
        "data_points": [
            "홍해 통과 물동량 감소율: 평시 대비 60% 이하 급감",
            "해운 운임 지수(SCFI): 연초 대비 2배 이상 폭등 유지를 기록"
        ],
        "signal": "neutral",
        "signal_reason": "지정학적 물류비 상승 압력이 존재하나 관련 해운/방산주 수혜 기회가 명확하기 때문입니다.",
        "key_companies": ["HMM", "언더스탠딩"],
        "insight": "비대칭 중동 분쟁은 글로벌 해운 운임 보장과 방산 안티드론 시장의 성장 촉매로 작용합니다.",
        "action_point": "해운 및 가성비 방체 체계 보유 방산주 투자에 주목하십시오."
    },
    "EPmytePgKt0": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["김종학뉴욕지금", "빅테크실적발표", "아마존애플MSFT", "한경글로벌마켓"],
        "summary": "빅테크 실적 발표 주간을 맞아 <span class=\"text-cyan-300 font-semibold\">마이크로소프트/알파벳의 실적 서프라이즈와 메타/아마존의 가이던스 차별화</span>가 연출되고 있습니다.",
        "key_claims": [
            "클라우드 매출이 급증한 마이크로소프트는 <span class=\"text-cyan-300 font-semibold\">시간 외 폭등세</span>를 연출.",
            "아마존 및 메타는 CapEx 지출 우려로 <span class=\"text-rose-400 font-medium\">단기 주가 숨고르기</span> 진행.",
            "반도체 단가 상승 영향에도 불구하고 <span class=\"text-amber-300 font-bold\">빅테크 실적 총량은 견조</span>함."
        ],
        "data_points": [
            "마이크로소프트 시간 외 상승: +4% 이상 기록",
            "빅테크 전체 2분기 매출 성장률: 평균 14% 상승"
        ],
        "signal": "bullish",
        "signal_reason": "마이크로소프트 등 핵심 빅테크의 클라우드 실적이 탄탄하여 기술주 우상향 축이 유지되기 때문입니다.",
        "key_companies": ["Microsoft", "Amazon", "Apple", "Meta", "한경글로벌마켓"],
        "insight": "CapEx 지출 논란 속에서도 실질 클라우드 이익을 증명한 빅테크가 승자가 됩니다.",
        "action_point": "호실적을 증명한 마이크로소프트 중심의 포트폴리오를 유지하십시오."
    },
    "fg_tEUEg2n8": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["폭락뒤남은변수", "회복준비", "집중오늘의주식", "이재규", "삼프로TV"],
        "summary": "폭락 장세의 남은 변수를 점검하고 매도 대신 <span class=\"text-cyan-300 font-semibold\">실적주의 회복 장세를 준비해야 할 시점</span>입니다.",
        "key_claims": [
            "바닥권에서 투매에 동참하는 매도는 <span class=\"text-rose-400 font-medium\">손실을 확정 짓는 실수</span>이다.",
            "수급 청산이 마감되는 순간 <span class=\"text-amber-300 font-bold\">실적 기반 우량주의 급반등</span>이 연출된다.",
            "8월 회복을 대비해 <span class=\"text-cyan-300 font-semibold\">반도체 및 핵심 세트주 보유 유지</span> 권고."
        ],
        "data_points": [
            "코스피 하방 지지력: PBR 0.85배 수준 탄탄",
            "기관 순매수 전환 징후 관찰"
        ],
        "signal": "bullish",
        "signal_reason": "과매도 청산 후 반등 회복 속도가 매우 빠를 것이기 때문입니다.",
        "key_companies": ["SK증권", "삼성전자"],
        "insight": "폭락 직후에는 투매보다 침착하게 회복을 기다리며 실적주를 모아가는 투자가 안전합니다.",
        "action_point": "삼성전자 및 SK하이닉스 보유 유지를 권고합니다."
    },
    "Gw8swHIqB04": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["외국인이사고싶을때", "주린이구조대", "삼프로TV", "외인수급"],
        "summary": "외국인이 저평가된 코스피를 다시 사고 싶어 하는 순간은 <span class=\"text-cyan-300 font-semibold\">환율 안점과 반도체 판가 상향 확인 시점</span>입니다.",
        "key_claims": [
            "외국인은 원달러 환율 상단 안정 시 <span class=\"text-cyan-300 font-semibold\">강력한 숏커버링 및 매수 전환</span>을 감행한다.",
            "메모리 반도체 실적 가시성이 입증되면 <span class=\"text-amber-300 font-bold\">외국인 수급 유입 속도</span>가 폭발한다.",
            "외국인 수급 전환 전 선제적 <span class=\"text-cyan-300 font-semibold\">저가 매집 매수</span> 유효."
        ],
        "data_points": [
            "원달러 환율 변동성: 1,380원선 지지 유도",
            "외국인 코스피 매수 전환 시 역사적 상승 폭: 지수 +15% 회복"
        ],
        "signal": "bullish",
        "signal_reason": "외국인의 수급 유출이 극에 달해 숏커버링 전환 시점이 임박했기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "외국인의 매도세 정체는 유입 전환의 신호탄이며, 저평가 대장주를 선점할 기회입니다.",
        "action_point": "코스피 대형주 및 반도체 대장주 분할 매수를 추천합니다."
    },
    "hemYb9rYnpI": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["삼성전자피크아웃없다", "최태원48조매수", "K배터리동반흑자", "뉴스3", "삼프로TV"],
        "summary": "삼성전자가 \"메모리 피크아웃은 없다\"고 선언하고 SK 최태원 회장이 <span class=\"text-cyan-300 font-semibold\">자사주 48억 장내 매수를 단행</span>하며 반도체/배터리 펀더멘털을 입증했습니다.",
        "key_claims": [
            "삼성전자는 메모리 공급 부족과 HBM 수요로 <span class=\"text-cyan-300 font-semibold\">피크아웃 가능성을 일축</span>했다.",
            "SK 최태원 회장은 책임 경영 일환으로 <span class=\"text-amber-300 font-bold\">SK하이닉스 주식 장내 직접 매수</span> 집행.",
            "K-배터리 3사 역시 2분기 동반 흑자 전환에 성공하며 <span class=\"text-cyan-300 font-semibold\">암흑 터널 탈출</span>."
        ],
        "data_points": [
            "최태원 회장 장내 매수 규모: 약 48억 원 전격 집행",
            "K-배터리 3사 2분기 영업이익: AMPC 수혜 힘입어 동반 흑자 달성"
        ],
        "signal": "bullish",
        "signal_reason": "최고 경영진의 자사주 매수와 기업의 공식 피크아웃 부정 선언이 강력한 신뢰를 주었기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스", "LG에너지솔루션"],
        "insight": "경영진의 직접 장내 매수와 공식 가이던스는 주가 바닥을 알리는 가장 강력한 신호입니다.",
        "action_point": "삼성전자 및 SK하이닉스의 강력 매수를 추천합니다."
    },
    "HTdNsyhQ8Ss": {
        "primary_topic": "space",
        "secondary_topics": ["tech"],
        "tags": ["달실험", "버려진로켓", "안될과학", "우주기술"],
        "summary": "버려진 상단 로켓을 달 표면에 충돌시켜 <span class=\"text-cyan-300 font-semibold\">지하 충격파 분석 및 수자원 파악</span>에 성공한 우주 과학 기술을 설명합니다.",
        "key_claims": [
            "폐기 로켓 충돌로 <span class=\"text-cyan-300 font-semibold\">달 지하 밀도 및 수분 분포 정밀 관측</span>.",
            "우주 쓰레기 재활용을 통한 <span class=\"text-amber-300 font-bold\">우주 과학 실험의 경제성 확보</span>.",
            "미래 달 기지 상용화를 위한 <span class=\"text-violet-300 font-medium\">핵심 기초 데이터 축적</span>."
        ],
        "data_points": [
            "로켓 충돌 속도: 초속 2.5km 고속 충돌 데이터 활용",
            "달 지하 수분 관측 깊이: 수 미터 깊이 성분 탐지"
        ],
        "signal": "bullish",
        "signal_reason": "우주 수송 및 탐사의 경제성이 대폭 개선되고 있기 때문입니다.",
        "key_companies": ["NASA", "안될과학"],
        "insight": "우주 쓰레기 활용 기술은 우주 탐사 비용을 대폭 줄이는 혁신 솔루션입니다.",
        "action_point": "우주 항공 인프라 및 위성 기술 분야 투자를 유효하게 유지하십시오."
    },
    "i9Gcc9tUCyM": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["엔비디아독주흔듬", "AMD반격", "실리콘밸리나우", "김인엽", "한경글로벌마켓"],
        "summary": "AMD가 차세대 MI300X/헬리오스 가속기로 엔비디아의 독점 구도를 흔들며 <span class=\"text-cyan-300 font-semibold\">AI 칩 2위 주도권</span>을 강화하고 있습니다.",
        "key_claims": [
            "AMD의 AI 가속기 수주가 앤스로픽 등 빅테크로 확대되며 <span class=\"text-cyan-300 font-semibold\">엔비디아 대항마로 정착</span>.",
            "가격 경쟁력과 가동 효율을 앞세워 <span class=\"text-amber-300 font-bold\">AI 칩 시장 점유율 20% 돌파</span> 목표.",
            "빅테크의 멀티 벤더 채택 가속화로 <span class=\"text-cyan-300 font-semibold\">AI 반도체 생태계 다변화</span> 전개."
        ],
        "data_points": [
            "AMD AI 칩 예상 매출: 내년 200억 달러 돌파 전망",
            "MI300X 단가: 엔비디아 H100 대비 30% 저렴한 가성비 제안"
        ],
        "signal": "bullish",
        "signal_reason": "AMD의 시장 점유율 확대와 이익 성장이 매우 가파르기 때문입니다.",
        "key_companies": ["AMD", "NVIDIA", "한경글로벌마켓"],
        "insight": "빅테크는 독점을 막기 위해 AMD를 적극 선택하고 있으며, 이는 AMD 주가 재평가로 이어집니다.",
        "action_point": "AMD 및 관련 반도체 수혜주의 매수를 적극 추천합니다."
    },
    "j12HdHSQ08g": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["채권자경단", "반도체주가변수", "클로징벨", "삼프로TV"],
        "summary": "채권 자경단(Bond Vigilantes)의 미 장기 국채 매도로 국채 금리가 오르며 <span class=\"text-rose-400 font-medium\">반도체 등 기술주 밸류에이션 부담</span>을 유발하고 있습니다.",
        "key_claims": [
            "미 미국 재정 적자 우려로 채권 자경단이 국채를 매도해 <span class=\"text-rose-400 font-medium\">장기 금리 상승 유도</span>.",
            "장기 금리 상승은 기술주의 <span class=\"text-rose-400 font-medium\">단기 밸류에이션 멀티플을 압박</span>하는 숨은 변수이다.",
            "금리 안정 시 <span class=\"text-cyan-300 font-semibold\">반도체주의 강력한 밸류 리셋 반등</span> 연출."
        ],
        "data_points": [
            "미국 10년물 국채 금리: 4.6%선에서 고착화",
            "채권 자경단 매도 규모: 미국 국채 발행 증가에 따른 장기물 쏠림"
        ],
        "signal": "neutral",
        "signal_reason": "장기 금리 노이즈가 있으나 반도체 실적 펀더멘털이 상쇄해주기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "장기 금리 상승은 기술주 멀티플을 압박하나, 실적 성장이 높은 대장주는 이를 극복합니다.",
        "action_point": "미국 국채 금리 상단 지지력을 관찰하며 반도체 대장주를 분할 매수하십시오."
    },
    "k0Rd3k3dV28": {
        "primary_topic": "energy",
        "secondary_topics": ["economy"],
        "tags": ["원전올스톱", "고준위방사성폐기물", "원전재앙", "김현권", "삼프로TV"],
        "summary": "고준위 방사성 폐기물 관리 특별법 제정이 지연될 경우 <span class=\"text-rose-400 font-medium\">4년 뒤 국내 원전의 가동 중단 위기</span>에 직면할 수 있음을 경고합니다.",
        "key_claims": [
            "원전 포화율 임계치 도달로 <span class=\"text-rose-400 font-medium\">특별법 미비 시 원전 멈춤 위험</span> 가중.",
            "AI 전력 수요 폭증과 맞춰 <span class=\"text-cyan-300 font-semibold\">원전 저장 시설 확충 법안</span>이 조속히 통과되어야 함.",
            "원전 안정성 확보 시 <span class=\"text-amber-300 font-bold\">K-원전 체인 및 SMR 성장</span> 지속."
        ],
        "data_points": [
            "국내 원전 사용후핵연료 포화율: 2030년부터 순차적 저장 한계 도달",
            "고준위 특별법 관련 경제 규모: 70조 원 규모 원전 인프라 연계"
        ],
        "signal": "neutral",
        "signal_reason": "법안 지연 리스크가 존재 하나 입법 추진 요구가 강해 해결될 가능성이 높기 때문입니다.",
        "key_companies": ["한국전력", "두산에너빌리티"],
        "insight": "원전 지속 가능성을 위한 저장 시설 법제화는 AI 전력망을 지키기 위한 필수 정책입니다.",
        "action_point": "원전 정책 법안 처리 추이를 모니터링하며 원자력 선도 기업 투자를 유지하십시오."
    },
    "k1lG5KdzuOU": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["지금이라도손절", "전문가의외결론", "교양이를부탁해", "손절금지"],
        "summary": "증시 폭락 막바지에서 전문가들은 <span class=\"text-cyan-300 font-semibold\">지금 손절매하는 것은 최악이며 펀더멘털 보유가 정답</span>이라는 의외의 결론을 내렸습니다.",
        "key_claims": [
            "바닥권에서의 손절은 <span class=\"text-rose-400 font-medium\">손실을 영구 확정 짓는 치명적 실수</span>이다.",
            "기업 이익이 살아있는 반도체주는 <span class=\"text-cyan-300 font-semibold\">반등 시 손실 상쇄 및 이익 전환</span>이 빠르다.",
            "지금 필요한 것은 공포를 견디는 <span class=\"text-amber-300 font-bold\">인내심과 우량주 보유</span>이다."
        ],
        "data_points": [
            "폭락 후 손절 투자자 평균 수익률: 장기 -40% 하회",
            "코스피 PBR: 0.85배 수준으로 매도 자제 영역"
        ],
        "signal": "bullish",
        "signal_reason": "바닥권에서 손절을 금지하고 보유하는 것이 최상의 수익율을 안겨주기 때문입니다.",
        "key_companies": ["교양이를부탁해"],
        "insight": "공포에 감정적 뇌동 매도를 하지 않는 것만으로도 투자의 승률이 비약적으로 올라갑니다.",
        "action_point": "손절매를 지양하고 펀더멘털 대형주 현물 포지션을 유지하십시오."
    },
    "KnaSBWiUAmw": {
        "primary_topic": "crypto",
        "secondary_topics": ["stock"],
        "tags": ["블랙록RWA", "쟁글", "크립토PLUS", "진짜대장주", "온체인금융"],
        "summary": "블랙록이 픽한 RWA(실물자산 토큰화) 수혜주 분석을 통해 <span class=\"text-cyan-300 font-semibold\">진짜 토큰화 인프라 대장주 파악</span>의 필요성을 다룹니다.",
        "key_claims": [
            "블랙록 BUIDL 펀드가 RWA 토큰화 시장의 <span class=\"text-cyan-300 font-semibold\">제도권 표준으로 자리잡았다</span>.",
            "단순 발행사보다 온체인 수수료와 커스터디를 전담하는 <span class=\"text-amber-300 font-bold\">인프라 기업이 진짜 대장주</span>이다.",
            "24/7 글로벌 주식/채권 토큰화로 <span class=\"text-violet-300 font-medium\">디지털 금융 패권</span> 형성."
        ],
        "data_points": [
            "블랙록 BUIDL 펀드 AUM: 5억 달러 초과",
            "RWA 기관 시장 성장률: 연 50% 가속"
        ],
        "signal": "bullish",
        "signal_reason": "블랙록 등 월가 공룡들의 RWA 편입이 확실한 시장 팽창을 보증하기 때문입니다.",
        "key_companies": ["BlackRock", "Securitize", "Ondo", "쟁글"],
        "insight": "RWA는 전통 자본이 온체인으로 유입되는 대세 통로이며 인프라 대장주가 수혜를 받습니다.",
        "action_point": "RWA 토큰화 인프라 핵심 기업에 선제적으로 분할 접근하십시오."
    },
    "KY9noW-d044": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["오전방송", "금리동결전쟁우려", "뉴욕증시하락", "빅테크실적엇갈림", "삼프로TV"],
        "summary": "FOMC 금리 동결과 중동 전쟁 우려 속에서 빅테크 실적 엇갈림으로 <span class=\"text-rose-400 font-medium\">뉴욕증시가 단기 조정을 겪는 혼조세</span>를 보였습니다.",
        "key_claims": [
            "MSFT 호실적에도 불구하고 메타/아마존 가이던스로 <span class=\"text-rose-400 font-medium\">증시 전반의 숨고르기</span> 연출.",
            "중동 지정학 불안과 고금리 지연으로 <span class=\"text-amber-300 font-bold\">투심 관망세 상존</span>.",
            "실적 선도주 중심의 <span class=\"text-cyan-300 font-semibold\">차별화 장세 유지</span>."
        ],
        "data_points": [
            "S&P 500 지수 변동: -0.5% 하락 조정",
            "WTI 유가: 중동 지정학 영향으로 배럴당 79달러선 부근 유지"
        ],
        "signal": "neutral",
        "signal_reason": "실적 장세 속에서 지정학 악재와 금리 경계감이 팽팽하기 때문입니다.",
        "key_companies": ["Microsoft", "Meta", "Amazon"],
        "insight": "빅테크 실적이 엇갈리는 장세에서는 옥석 가리기를 통해 확실한 실적주에 집중해야 합니다.",
        "action_point": "실적 서프라이즈 기업(MSFT) 위주로 포트폴리오를 압축하십시오."
    },
    "l87HA0Pyjlc": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["고점사고저점파는함정", "교양이를부탁해", "심리투자", "알상무"],
        "summary": "매번 사면 고점, 팔면 저점에 빠지는 투자자의 심리적 함정을 분석하고 <span class=\"text-cyan-300 font-semibold\">원칙 있는 저가 매수 및 역발상 투자</span>를 강조합니다.",
        "key_claims": [
            "남들이 환호할 때 고점에 사고 공포에 짓눌려 저점에 파는 <span class=\"text-rose-400 font-medium\">감정적 매매 함정</span> 피해야 함.",
            "폭락장에서 공포를 딛고 <span class=\"text-cyan-300 font-semibold\">역발상으로 담는 투자자</span>가 승리한다.",
            "기업 이익 가치를 믿고 <span class=\"text-amber-300 font-bold\">분할 저가 매수를 기계적으로 실행</span>해야 함."
        ],
        "data_points": [
            "개인 투자자 고점 매수 비율: 상승장 막바지에 개인 자금 70% 쏠림",
            "역발상 투자 승률: 공포 지수 고점 진입 시 1년 수익률 +25%"
        ],
        "signal": "bullish",
        "signal_reason": "지금의 공포 장세가 전형적인 역발상 매수의 기회이기 때문입니다.",
        "key_companies": ["교양이를부탁해"],
        "insight": "투자의 성공은 시장 심리와 반대로 움직이는 감정 통제 능력에 달려 있습니다.",
        "action_point": "공포를 활용해 우량 반도체 및 대형주를 기계적으로 분할 매수하십시오."
    },
    "LmCNGKU8CQg": {
        "primary_topic": "tech",
        "secondary_topics": ["robot", "stock"],
        "tags": ["테슬라진짜무서운이유", "FSD12", "옵티머스", "피지컬AI", "SOD"],
        "summary": "테슬라가 진짜 무서운 이유는 자율주행(FSD) 데이터와 피지컬 AI(옵티머스)가 결합해 <span class=\"text-cyan-300 font-semibold\">현실 세계를 지배하는 독점 생태계</span>를 구축하고 있기 때문입니다.",
        "key_claims": [
            "FSD V12의 신경망 기반 주행으로 <span class=\"text-cyan-300 font-semibold\">자율주행 데이터 축적 속도가 독보적</span>이다.",
            "자동차에서 검증된 신경망 AI가 옵티머스 휴머노이드 로봇에 그대로 이전되어 <span class=\"text-amber-300 font-bold\">피지컬 AI 주도권 선점</span>.",
            "소프트웨어와 하드웨어 수직통합이 <span class=\"text-violet-300 font-medium\">압도적인 밸류에이션 프리미엄</span>을 정당화."
        ],
        "data_points": [
            "테슬라 FSD 누적 주행 거리: 15억 마일 돌파",
            "옵티머스 로봇 공장 투입 수: 2025년 수천 대 1차 배치 예정"
        ],
        "signal": "bullish",
        "signal_reason": "FSD 및 피지컬 AI의 독보적 데이터 격차가 테슬라의 독점력을 높여주기 때문입니다.",
        "key_companies": ["Tesla", "SOD"],
        "insight": "테슬라는 자동차 제조사가 아니라 현실 세계의 물리 법칙을 학습하는 피지컬 AI 무적의 플랫폼입니다.",
        "action_point": "테슬라 및 자율주행/로봇 부품 밸류체인에 장기 투자를 추천합니다."
    },
    "MguyYQaV3qo": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["금리인상보다무서운것", "증시발목", "교양이를부탁해", "수급고갈"],
        "summary": "금리 인상보다 더 무서운 증시 발목 잡는 진짜 범인은 <span class=\"text-rose-400 font-medium\">신용 반대매매로 인한 수급 고갈과 심리적 붕괴</span>입니다.",
        "key_claims": [
            "금리 지표보다 <span class=\"text-rose-400 font-medium\">강제 반대매매로 인한 수급 붕괴</span>가 주가를 기형적으로 폭락시킴.",
            "수급 청산이 마감되는 시점에서 <span class=\"text-cyan-300 font-semibold\">펀더멘털 기업의 신속한 주가 회복</span> 전개.",
            "수급 악재 소멸 시 <span class=\"text-amber-300 font-bold\">급격한 V자 리바운드 장세</span> 연출."
        ],
        "data_points": [
            "신용 융자 반대매매 금액: 일간 사상 최고치 경신 후 급감",
            "수급 청산 후 평균 반등 폭: 2주 내 +10% 이상 회복"
        ],
        "signal": "bullish",
        "signal_reason": "수급 고갈에 의한 폭락은 청산 완료 시 가장 강한 기술적 반등을 안겨주기 때문입니다.",
        "key_companies": ["교양이를부탁해"],
        "insight": "수급 왜곡으로 주가가 부서질 때가 펀더멘털 우량주를 가장 싸게 담을 수 있는 찬스입니다.",
        "action_point": "수급 악재에 흔들리지 말고 흑자 반도체 및 대형주를 보유하십시오."
    },
    "mJJt591kmbA": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["6500반등", "더블체크", "빈센트", "정프로", "삼프로TV"],
        "summary": "증시 지수가 기술적 지지선을 딛고 6,500선(S&P 기준)까지 반등할 경우 <span class=\"text-cyan-300 font-semibold\">완전한 분위기 반전과 추세적 상승</span>이 재개될 수 있습니다.",
        "key_claims": [
            "단기 조정을 거친 후 <span class=\"text-cyan-300 font-semibold\">지수 지지선 확인 및 기술적 반등</span> 가동.",
            "핵심 저항선 돌파 시 <span class=\"text-amber-300 font-bold\">투자 심리의 대전환과 숏커버링</span> 유입.",
            "우량 대형주 위주의 <span class=\"text-cyan-300 font-semibold\">추세적 상승 재개</span> 전망."
        ],
        "data_points": [
            "S&P 500 지수 목표: 6,500선 돌파 시 강한 2차 랠리 진입",
            "기술적 이격도: 역사적 과매도 상단 탈출 관찰"
        ],
        "signal": "bullish",
        "signal_reason": "기술적 지지선 확인 후 추세적 상승 재개 가능성이 우세하기 때문입니다.",
        "key_companies": ["삼프로TV"],
        "insight": "지수 지지선 확인 후의 반등은 하반기 주식 시장의 추세적 상승을 이끄는 발판이 됩니다.",
        "action_point": "지수형 ETF 및 시가총액 상위 대형주 비중을 유지하십시오."
    },
    "nhaKgbcFtWo": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["이유없는급락범인", "레오폴드마진콜", "속보효", "이효석아카데미"],
        "summary": "이유도 없이 주가가 급락했던 주범이 <span class=\"text-rose-400 font-medium\">월가 22세 해지펀드 매니저의 4배 레버리지 마진콜 청산</span> 때문이었음이 밝혀졌습니다.",
        "key_claims": [
            "반도체 및 AI주 폭락은 펀더멘털 문제가 아니라 <span class=\"text-rose-400 font-medium\">특정 해지펀드의 레버리지 마진콜 청산</span> 때문이었다.",
            "시타델 등 거대 해지펀드가 이를 청산 인수하면서 <span class=\"text-cyan-300 font-semibold\">숏커버링 및 폭등세로 전환</span>.",
            "실적 우수 반도체/AI 인프라주의 <span class=\"text-amber-300 font-bold\">비이성적 할인 구간 종료</span>."
        ],
        "data_points": [
            "레오폴드 펀드 마진콜 크기: 450억 달러 포지션 중 30% 폭락에 따른 강제 청산",
            "숏커버링 반등 폭: 마이크론, 블루에너지 등 주요 종목 폭등"
        ],
        "signal": "bullish",
        "signal_reason": "근거 없는 수급 폭락의 원인이 마진콜로 확인되어 가파른 시세 회복이 전개될 것이기 때문입니다.",
        "key_companies": ["이효석아카데미", "시타델", "삼성전자", "SK하이닉스"],
        "insight": "이유 없는 폭락은 월가 수급 전쟁의 결과였으며, 마진콜 해소는 강력한 매수 신호입니다.",
        "action_point": "억울하게 하락했던 메모리 반도체 및 AI 인프라 대장주를 적극 저가 매수하십시오."
    },
    "NnbqYUCszos": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["주식살릴해법", "뜻밖의해법", "교양이를부탁해", "수급정상화"],
        "summary": "주식 시장을 살릴 뜻밖의 해법은 <span class=\"text-cyan-300 font-semibold\">공포에 기인한 신용 청산 마감과 실적 펀더멘털로의 시선 전환</span>입니다.",
        "key_claims": [
            "시장 악재보다 <span class=\"text-rose-400 font-medium\">공포 심리의 과잉 반응이 주가를 왜곡</span>시켰다.",
            "실적 가치가 명확한 반도체주부터 <span class=\"text-cyan-300 font-semibold\">정상 가격 복원</span>이 이뤄질 것이다.",
            "현금을 확보하고 <span class=\"text-amber-300 font-bold\">실적주를 담아두는 역발상 전략</span>이 최선이다."
        ],
        "data_points": [
            "코스피 밸류에이션: 역사적 하단 지지력 형성",
            "기업 이익 성장률: 하반기 메모리 영업이익 급증"
        ],
        "signal": "bullish",
        "signal_reason": "실적과 분리된 공포 장세가 끝나면 펀더멘털로의 강한 복귀가 연출되기 때문입니다.",
        "key_companies": ["교양이를부탁해"],
        "insight": "시장을 살리는 최고의 해법은 공포를 딛고 펀더멘털 이익 가치를 신뢰하는 투자입니다.",
        "action_point": "삼성전자 및 SK하이닉스의 저가 매수 및 강한 보유를 권고합니다."
    },
    "oIt0vu2P8qw": {
        "primary_topic": "energy",
        "secondary_topics": ["economy"],
        "tags": ["30조사우디원전", "K원전수주", "언더스탠딩", "김상훈기자"],
        "summary": "30조 원 규모의 사우디아라비아 원전 사업에서 한국 팀코리아가 <span class=\"text-cyan-300 font-semibold\">독보적인 공기 및 단가 경쟁력으로 최종 수주 유력</span> 후보로 떠오르고 있습니다.",
        "key_claims": [
            "사우디 30조 원 원전 건설 프로젝트에서 <span class=\"text-cyan-300 font-semibold\">한국 K-원전의 수주 가능성 극대화</span>.",
            "체코 원전 수주에 이은 사우디 수주는 <span class=\"text-amber-300 font-bold\">국내 원전 밸류체인의 10년 장기 호황</span>을 보증.",
            "AI 전력 소요 폭증과 맞춰 <span class=\"text-violet-300 font-medium\">글로벌 원전 및 SMR 시장</span> 재평가."
        ],
        "data_points": [
            "사우디 원전 사업 규모: 약 30조 원 (2기 대형 원전 건설)",
            "K-원전 공기 준수율: 글로벌 1위 (On time, On budget)"
        ],
        "signal": "bullish",
        "signal_reason": "30조 사우디 원전 수주 시 국내 원전 및 전력망 기자재사들의 대규모 이익이 확정되기 때문입니다.",
        "key_companies": ["두산에너빌리티", "한국전력", "한전기술", "언더스탠딩"],
        "insight": "K-원전은 글로벌 AI 전력난 시대에 가장 확실한 공기와 가격을 보장하는 우방국 자산입니다.",
        "action_point": "두산에너빌리티 및 한전 그룹 원전 수혜주의 중장기 매수를 적극 권고합니다."
    },
    "PmXXMPyybb8": {
        "primary_topic": "robot",
        "secondary_topics": ["tech"],
        "tags": ["휴머노이드눈", "비전AI", "NewStandard", "미래에셋"],
        "summary": "휴머노이드 로봇이 초지능 3D 비전 센서와 Spatial AI를 통해 <span class=\"text-cyan-300 font-semibold\">실세계 환경을 정밀 인식하고 시각 눈을 뜨는 혁신</span>을 이루고 있습니다.",
        "key_claims": [
            "3D ToF 및 스테레오 비전 카메라 결합으로 <span class=\"text-cyan-300 font-semibold\">휴머노이드 시각 인식 지능 극대화</span>.",
            "Spatial AI 및 피지컬 센서가 공간을 즉시 지도화해 <span class=\"text-amber-300 font-bold\">자율 조작 능력 상용화</span>.",
            "로봇용 3D 센서 및 센서 퓨전 기업들의 <span class=\"text-violet-300 font-medium\">독점적 부품 가치 부각</span>."
        ],
        "data_points": [
            "로봇 비전 센서 시장 성장률: 연평균 45% 폭증",
            "3D 공간 인식 정밀도: 밀리미터 단위 측정 성공"
        ],
        "signal": "bullish",
        "signal_reason": "로봇 시각 인식 지능의 성숙으로 휴머노이드의 현장 투입 및 상용화가 임박했기 때문입니다.",
        "key_companies": ["테슬라", "보스턴다이내믹스", "미래에셋"],
        "insight": "휴머노이드가 눈을 뜬다는 것은 단순 노동을 대체할 수 있는 실질적 사업화 단계에 진입했음을 뜻합니다.",
        "action_point": "로봇용 비전 센서, 3D 카메라 및 로봇 부품 선도 종목에 투자하십시오."
    },
    "qgfwrXPjMrw": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["MSFT실적급등", "AIHW동반랠리", "월가뉴스레터", "삼프로TV"],
        "summary": "마이크로소프트가 호실적으로 18% 급등하며 반도체 등 <span class=\"text-cyan-300 font-semibold\">AI 하드웨어 섹터의 동반 랠리</span>를 강하게 주도했습니다.",
        "key_claims": [
            "마이크로소프트의 클라우드 실적 대폭 상회가 <span class=\"text-cyan-300 font-semibold\">AI 하드웨어 우려를 한방에 불식</span>시켰다.",
            "엔비디아, 마이크론, SK하이닉스 등 <span class=\"text-amber-300 font-bold\">AI HW 수혜주의 강력한 동반 랠리</span> 재개.",
            "빅테크의 CapEx 지출 정당성이 입증되어 <span class=\"text-cyan-300 font-semibold\">기술주 장기 우상향</span> 지속."
        ],
        "data_points": [
            "마이크로소프트 주가 반응: 호실적 발표 후 급등 기록",
            "AI 하드웨어 섹터 반등 폭: 반도체 지수 +5% 이상 동반 랠리"
        ],
        "signal": "bullish",
        "signal_reason": "마이크로소프트의 뛰어난 실적이 AI 인프라 전체의 강력한 동반 상승을 견인하기 때문입니다.",
        "key_companies": ["Microsoft", "NVIDIA", "SK하이닉스"],
        "insight": "마이크로소프트의 호실적은 AI 하드웨어 밸류체인 전체의 실적과 주가를 보증해 줍니다.",
        "action_point": "마이크로소프트 및 AI 하드웨어 대장주(SK하이닉스/엔비디아) 비중 확대를 권고합니다."
    },
    "qyTcOaqez94": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["악재도없는데빠짐", "주식빠지는진짜이유", "교양이를부탁해", "알상무"],
        "summary": "실질 악재가 없음에도 주가가 폭락한 진짜 이유는 <span class=\"text-rose-400 font-medium\">신용 청산과 수급 붕괴에 따른 착시 현상</span> 때문입니다.",
        "key_claims": [
            "기업 펀더멘털 훼손 악재가 아니라 <span class=\"text-rose-400 font-medium\">수급 쏠림과 반대매매 폭매</span>가 하락 원인.",
            "악재 없는 폭락은 청산 완료 시 <span class=\"text-cyan-300 font-semibold\">가장 빠르게 원래 가격을 회복</span>한다.",
            "이성적인 가치 평가로 돌아오면 <span class=\"text-amber-300 font-bold\">대폭등 반등 장세</span> 연출."
        ],
        "data_points": [
            "기업 영업이익 추정치: 하반기 이익 변화 없음 (견조함 유지)",
            "주가 하락 폭: 펀더멘털 무관 단기 -20% 이상 과매도"
        ],
        "signal": "bullish",
        "signal_reason": "악재 없는 수급성 폭락은 강렬한 보상 반등을 수반하기 때문입니다.",
        "key_companies": ["교양이를부탁해"],
        "insight": "악재 없이 빠진 주식이야말로 시장이 준 가장 저렴한 매수 선물입니다.",
        "action_point": "삼성전자 및 SK하이닉스를 저가에 적극 매수하십시오."
    },
    "RUq38NKLPTs": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["애플안전자산", "반도체오르면끝", "개장전요것만", "한경글로벌마켓"],
        "summary": "애플이 안전자산으로 매수세가 쏠리는 가운데, <span class=\"text-cyan-300 font-semibold\">반도체 숏커버링 반등 시 증시 전체의 대세 상승</span>이 재개될 것입니다.",
        "key_claims": [
            "애플은 본업 FCF와 주주환원으로 <span class=\"text-cyan-300 font-semibold\">시장의 대표 안전자산 역할을 톡톡히 수행</span>.",
            "수급 억눌렸던 반도체주가 반등을 시작하면 <span class=\"text-amber-300 font-bold\">증시의 강력한 2차 상승 동력</span> 가동.",
            "애플과 반도체 대장주의 <span class=\"text-cyan-300 font-semibold\">투트랙 포트폴리오</span> 구축 권고."
        ],
        "data_points": [
            "애플 시가총액: 4.95조 달러 최고치 유지",
            "반도체 지수 이격도: 역사적 바닥 수준에서 숏커버링 진행"
        ],
        "signal": "bullish",
        "signal_reason": "안전자산 애플의 하방 지지와 반도체 숏커버링 반등이 결합되기 때문입니다.",
        "key_companies": ["애플", "SK하이닉스", "삼성전자", "한경글로벌마켓"],
        "insight": "애플이라는 안정판을 둔 상태에서 반도체의 숏커버링이 터지면 증시는 가파르게 회복됩니다.",
        "action_point": "애플과 SK하이닉스/삼성전자의 투트랙 보유를 적극 추천합니다."
    },
    "Sdjb2aXC98s": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["삼성전자괴물실적", "2분기실적발표", "속보효", "이효석아카데미"],
        "summary": "삼성전자가 2분기 시장 기대를 뛰어넘는 <span class=\"text-cyan-300 font-semibold\">괴물 실적(영업이익 폭증)</span>을 공식 발표하며 펀더멘털을 완벽 입증했습니다.",
        "key_claims": [
            "삼성전자 2분기 확정 실적 발표로 <span class=\"text-cyan-300 font-semibold\">메모리 판가 상승 및 영업이익 폭증</span> 확인.",
            "주가 하락 우려를 일축하는 <span class=\"text-amber-300 font-bold\">강력한 펀더멘털 팩트</span> 제시.",
            "실적 확인 후 <span class=\"text-cyan-300 font-semibold\">외국인 수급의 저가 재매수 전환</span> 유도."
        ],
        "data_points": [
            "삼성전자 2분기 영업이익: 10조 원 이상 돌파 어닝 서프라이즈",
            "DS(반도체) 부문 영업이익: 메모리 흑자폭 확대로 전년 대비 폭증"
        ],
        "signal": "bullish",
        "signal_reason": "공식 괴물 실적 발표가 노이즈성 주가 하락을 단숨에 물리치기 때문입니다.",
        "key_companies": ["삼성전자", "이효석아카데미"],
        "insight": "주가의 노이즈는 흘러가도 괴물 실적이라는 장부상의 팩트는 주가를 반드시 끌어올립니다.",
        "action_point": "삼성전자 저가 매수를 강력히 추천합니다."
    },
    "sQG-R3l6_3o": {
        "primary_topic": "economy",
        "secondary_topics": ["etc"],
        "tags": ["세금깎아줘야집잡힘", "이관옥교수", "부동산조세2부", "언더스탠딩"],
        "summary": "부동산 시장 안정을 위해서는 단순 규제보다 <span class=\"text-cyan-300 font-semibold\">거래세 감면 및 유동성 공급 유도</span>가 실질 집값 안정에 효과적입니다.",
        "key_claims": [
            "과도한 취득세/양도세는 <span class=\"text-rose-400 font-medium\">매물 동결 현상(Lock-in effect)</span>을 유발해 매물 부족 초과 심화.",
            "거래세 완화를 통해 <span class=\"text-cyan-300 font-semibold\">다주택자 매물 출회를 유도</span>해야 집값이 안정된다.",
            "조세 세제 정상화가 <span class=\"text-amber-300 font-bold\">주택 거래량 회복 및 시장 정상화</span>의 열쇠."
        ],
        "data_points": [
            "거래세 감면 시 매물 출회 증가율: 과거 규제 완화 시 매물 20% 증가",
            "서울 아파트 매물 동결 비율: 높은 양도세로 매물 잠김 지속"
        ],
        "signal": "neutral",
        "signal_reason": "부동산 세제 개편 논의가 시장의 매물 흐름을 바꾸는 세부 변수이기 때문입니다.",
        "key_companies": ["싱가포르국립대", "언더스탠딩"],
        "insight": "양도세/취득세 감면 정책이 도입되면 매물이 유통되며 부동산 가격 과열을 잡을 수 있습니다.",
        "action_point": "부동산 정책 세제 개편 가이드라인을 주시하며 자산 전략을 점검하십시오."
    },
    "V0yLXZHQvAs": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["유가장기금리급등", "미국증시낙폭확대", "미래에셋", "데일리라이브"],
        "summary": "유가 상승 및 장기 국채 금리 급등 노이즈로 미국 증시가 낙폭을 확대했으나, <span class=\"text-cyan-300 font-semibold\">빅테크 실적 수주가 하방을 받치는 국면</span>입니다.",
        "key_claims": [
            "미 국채 10년물 금리 및 유가 반응으로 <span class=\"text-rose-400 font-medium\">단기 유동성 위축</span> 발생.",
            "지수 하락 속에서도 <span class=\"text-amber-300 font-bold\">실적 호조 빅테크 및 전력주</span>는 하방 방어.",
            "거시 지표 확인 후 <span class=\"text-cyan-300 font-semibold\">다변화 순환매 장세</span> 지속."
        ],
        "data_points": [
            "미국 국채 10년물 금리: 4.65% 기록하며 기술주 압박",
            "WTI 유가: 지정학 우려로 배럴당 80달러선 재진입"
        ],
        "signal": "neutral",
        "signal_reason": "금리/유가 압박 악재와 빅테크 실적 호재가 대립하고 있기 때문입니다.",
        "key_companies": ["미래에셋증권"],
        "insight": "거시 유동성 악재 시기에는 실적이 확실한 독점 기업에 자금이 쏠리게 마련입니다.",
        "action_point": "빅테크 및 전력 인프라 우량주 중심의 포트폴리오 유지를 추천합니다."
    },
    "Vvv4wgwNx9U": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["최악반영시점", "지금확인할변수", "이선엽", "AFW파트너스", "삼프로TV"],
        "summary": "시장은 이미 최악의 악재를 전량 반영했으므로, <span class=\"text-cyan-300 font-semibold\">수급 멈춤과 실적 반등 변수 확인 후 과감한 매수</span>가 필요한 시점입니다.",
        "key_claims": [
            "7월 폭락은 모든 가상 악재를 선반영한 <span class=\"text-cyan-300 font-semibold\">최악의 피크권 통과</span>다.",
            "외국인 수급 청산이 그치는 순간 <span class=\"text-amber-300 font-bold\">강력한 V자 리바운드</span> 전개.",
            "실적이 탄탄한 코스피 200 대형주에 <span class=\"text-cyan-300 font-semibold\">집중적인 저가 매수</span> 권고."
        ],
        "data_points": [
            "코스피 PBR: 0.85배 수준으로 역사적 하단",
            "악재 반영률: 금리, 지정학, 파생 반대매매 전량 선반영 완료"
        ],
        "signal": "bullish",
        "signal_reason": "최악의 악재 선반영 후 시장이 이성을 되찾으며 강력한 반등을 시도할 것이기 때문입니다.",
        "key_companies": ["AFW파트너스", "삼성전자", "SK하이닉스"],
        "insight": "최악이 이미 주가에 다 반영되었다면 남은 것은 주가의 강렬한 회복 상승뿐입니다.",
        "action_point": "삼성전자 및 SK하이닉스 등 대장주 분할 매수를 강력히 추천합니다."
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

print("\n[SUCCESS] All 32 pending videos analyzed!")
