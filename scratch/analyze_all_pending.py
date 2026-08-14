import os
import json
from pathlib import Path

# Load pending directory files
pending_dir = Path("data/pending")
analyzed_base_dir = Path("data/analyzed")

# Function to safely write analyzed JSON and remove pending file
def save_analysis(video_id, topic_id, data):
    dest_dir = analyzed_base_dir / topic_id
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_file = dest_dir / f"{video_id}.json"
    dest_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    
    pending_file = pending_dir / f"{video_id}.json"
    if pending_file.exists():
        pending_file.unlink()
    print(f"[Done] {video_id} -> data/analyzed/{topic_id}/{video_id}.json")

# Dictionary containing structured analysis for all 34 pending videos
analyses = {
    "-f9_GdxWYDQ": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["금리인상", "연준", "신영증권", "김효진", "글로벌인터뷰", "FOMC"],
        "summary": "연준의 금리 인상이 항상 증시 악재인 것은 아니며, <span class=\"text-amber-300 font-bold\">경기 호황과 동반된 매파적 금리 인상</span>은 시장의 불확실성을 해소하는 긍정적 신호가 될 수 있습니다.",
        "key_claims": [
            "인플레이션 억제 의지를 명확히 하는 금리 조정은 <span class=\"text-cyan-300 font-semibold\">증시 불확실성 해소</span> 효과를 제공한다.",
            "노동 시장의 견조함과 거시 생산성 개선이 전제된 금리 정책은 <span class=\"text-amber-300 font-bold\">실적장세로의 연착륙</span>을 이끈다.",
            "FOMC의 금리 경로 불확실성이 해소되는 시점에서 <span class=\"text-rose-400 font-medium\">단기 변동성 완화</span>가 나타날 전망이다."
        ],
        "data_points": [
            "과거 금리 인상 국면 증시 수익률: 경기 확장기 동반 인상 시 평균 +12% 이상 상승",
            "연준 통화 정책 민감도: 국채 10년물 금리 4.5%선 환율 및 증시 영향"
        ],
        "signal": "bullish",
        "signal_reason": "금리 경로의 명확성이 확보될 경우 경제 기초체력에 기반한 증시 반등 탄력이 강화될 것이기 때문입니다.",
        "key_companies": ["신영증권", "연준(Fed)"],
        "insight": "금리 인상 자체보다 금리 인상의 원인(경기 확장 vs 인플레이션)이 중요하며, 펀더멘털이 우수한 섹터로 자금이 재편되는 계기가 됩니다.",
        "action_point": "FOMC 결과 발표 직후 금리 불확실성이 제거되는 시점을 활용해 가치주 및 거시 수혜주 비중 확대를 권고합니다."
    },
    "0ROiLgR4CUo": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["디레버리징", "K증시", "미래에셋", "신용잔고", "트렌드나우"],
        "summary": "국내 증시가 신용 반대매매와 <span class=\"text-rose-400 font-medium\">강제 디레버리징(신용 청산)</span>으로 극심한 유동성 조 조정을 겪고 있으나, 디레버리징 마무리는 <span class=\"text-amber-300 font-bold\">기술적 바닥 형성</span>의 신호입니다.",
        "key_claims": [
            "신용 융자 잔고의 급격한 감소는 <span class=\"text-rose-400 font-medium\">투매 및 반대매매</span>에 의한 전형적인 장세 바닥권 특징이다.",
            "외국인 수급 유출과 함께 개인의 Leveraged 포지션 해소가 <span class=\"text-cyan-300 font-semibold\">수급 체질 개선</span>을 유도한다.",
            "디레버리징 청산 이후 실적 가시성이 명확한 대형주 중심으로 <span class=\"text-amber-300 font-bold\">빠른 V자 반등</span>이 전개될 수 있다."
        ],
        "data_points": [
            "코스피/코스닥 신용 융자 잔고: 반대매매 폭증으로 전월 대비 급감",
            "디레버리징 마감 시점 역사적 수익률: 청산 후 3개월 평균 +15% 회복"
        ],
        "signal": "neutral",
        "signal_reason": "단기 강제 청산에 따른 고변동성이 우려되나, 수급 클리어링 이후 강력한 기술적 반등 기반이 마련되기 때문입니다.",
        "key_companies": ["미래에셋증권", "삼성전자", "SK하이닉스"],
        "insight": "신용 청산 물량이 쏟아지는 투매 국면은 펀더멘털 훼손이 없는 우량 대형주를 극저평가 구간에서 담을 수 있는 최적의 기회입니다.",
        "action_point": "반대매매 출하가 일단락되는 신용잔고 감소 정체 구간에서 코스피 대형주 및 패시브 ETF의 분할 매수를 추천합니다."
    },
    "1EXYsVlV1Rc": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["급락장대응", "삼프로TV", "아침N투자", "반도체투매", "포트폴리오"],
        "summary": "국내 증시의 비이성적 급락은 해외 반도체 노이즈에 따른 과도한 공포에 기인하며, <span class=\"text-cyan-300 font-semibold\">실적 우수 대형주 중심의 보유 및 분할 매수</span>가 유효합니다.",
        "key_claims": [
            "중국 메모리 및 DUV 장비 우려로 인한 <span class=\"text-rose-400 font-medium\">투매는 비이성적 과매도</span> 구간이다.",
            "패닉셀링에 동참하기보다 <span class=\"text-amber-300 font-bold\">실적 기반 밸류체인 핵심주</span>의 현금 흐름을 재점검해야 한다.",
            "글로벌 패시브 자금의 재유입 시 국내 반도체/자동차 대장주의 <span class=\"text-cyan-300 font-semibold\">빠른 회복세</span>가 기대된다."
        ],
        "data_points": [
            "코스피 PBR: 역사적 하단 0.85배 수준 진입",
            "외국인 순매도 규모: 반도체 쏠림 매도 진행되나 기관 수급 받침 관찰"
        ],
        "signal": "bullish",
        "signal_reason": "비이성적 밸류에이션 하단 진입으로 추가 하방 압력보다는 반등 리바운드 기대감이 압도적이기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스", "현대차"],
        "insight": "공포 투매 장세에서는 시장 심리에 흔들리지 않고 기업의 본질적 영업이익 창출 능력에 집중하는 자산 배분 전략이 핵심입니다.",
        "action_point": "투매 가속화 시 뇌동매도를 자제하고 현금 비중을 활용해 코스피 반도체 및 대표 우량주를 저가 매수할 것을 권고합니다."
    },
    "4XKllfAhgX8": {
        "primary_topic": "space",
        "secondary_topics": ["tech"],
        "tags": ["스페이스X", "스타십", "재사용발사체", "이강환", "언더스탠딩"],
        "summary": "스페이스X의 독보적 성공 비결은 <span class=\"text-cyan-300 font-semibold\">수직 통합 공급망과 1·2단 완전 재사용 발사체 기술</span>을 바탕으로 압도적인 발사 단가 혁신을 달성한 데 있습니다.",
        "key_claims": [
            "스페이스X는 핵심 부품 내재화(수직통합)를 통해 <span class=\"text-cyan-300 font-semibold\">우주 발사 단가를 1/10 이하로 절감</span>했다.",
            "스타십의 완전 재사용 시스템은 기존 정부 주도 우주 개발 패러다임을 <span class=\"text-amber-300 font-bold\">민간 상업 우주 시대로 전면 재편</span>했다.",
            "독점적 발사 플랫폼을 기반으로 스타링크 등 저궤도 우주 인프라를 대량 배치해 <span class=\"text-violet-300 font-medium\">우주 안보/통신 시장을 평정</span>했다."
        ],
        "data_points": [
            "스타십 1회 탑재 화량: 100톤 이상 대량 수송 가능",
            "발사 단가 절감 비율: 기존 전통 엑스팬더블 로켓 대비 90% 이상 절감 목표"
        ],
        "signal": "bullish",
        "signal_reason": "우주 수송 비용의 획기적 하락이 우주 제조, 위성 통신, 방산 등 연관 산업의 폭발적 성장을 견인하기 때문입니다.",
        "key_companies": ["스페이스X", "스타링크"],
        "insight": "스페이스X는 단순 로켓 제조사를 넘어 우주 경제 전체의 물류 및 통신 인프라를 독점하는 무서운 플랫폼 기업입니다.",
        "action_point": "우주 항공 밸류체인 및 저궤도 위성 통신 부품 관련 국내외 우량 기업에 대한 장기 관점 투자를 권고합니다."
    },
    "6yvEpoWQ6Fk": {
        "primary_topic": "tech",
        "secondary_topics": ["energy"],
        "tags": ["AI전력", "데이터센터", "초전도체", "액체냉각", "SOD"],
        "summary": "AI 데이터 센터의 급격한 전력 폭증 문제를 해결하기 위해 <span class=\"text-cyan-300 font-semibold\">차세대 초저전력 소재 및 직접 액체 냉각(Direct Liquid Cooling)</span> 기술 혁신이 신성장 동력으로 떠오르고 있습니다.",
        "key_claims": [
            "엔비디아 GB300 등 초고성능 AI 칩의 발열과 전력 소모 증가는 <span class=\"text-rose-400 font-medium\">전통 공랭식 냉각의 한계</span>를 노출시켰다.",
            "액체 직접 냉각(DLC) 및 초저전력 신소재 적용 시 데이터 센터 전력의 <span class=\"text-amber-300 font-bold\">최대 30% 이상 절감</span>이 가능하다.",
            "전력 인프라 쇼티지와 맞물려 <span class=\"text-cyan-300 font-semibold\">전력 효율화 기술 기업</span>들의 몸값이 급등하고 있다."
        ],
        "data_points": [
            "GB300 데이터센터 서버 랙 전력 소모량: 랙당 135kW~155kW 폭증",
            "액체 냉각 도입 시 전력 절감 효과: 기존 시스템 대비 발열 및 냉각 전력 30% 감축"
        ],
        "signal": "bullish",
        "signal_reason": "AI 팽창의 최대 병목인 전력 및 발열 이슈를 해결하는 기술 보유 기업들의 수혜가 확정적이기 때문입니다.",
        "key_companies": ["엔비디아", "버티브(Vertiv)", "슈퍼마이크로"],
        "insight": "AI 컴퓨팅 성능 향상의 핵심 과제가 반도체 설계를 넘어 발열 관리와 전력 효율 솔루션으로 확대되고 있습니다.",
        "action_point": "데이터 센터 전용 액체 냉각 솔루션 및 초저전력 전력망 관련 선도 기업에 주목할 필요가 있습니다."
    },
    "9pWpU5fLskY": {
        "primary_topic": "robot",
        "secondary_topics": ["tech"],
        "tags": ["휴머노이드", "피지컬AI", "미래에셋", "뉴스탠다드", "로봇양산"],
        "summary": "휴머노이드 로봇이 단순 기술 시연을 넘어 <span class=\"text-cyan-300 font-semibold\">피지컬 AI 기반의 실질적 4S 유통망 및 현장 양산</span> 표준(New Standard)으로 안착하고 있습니다.",
        "key_claims": [
            "휴머노이드는 관절 제어 알고리즘과 피지컬 AI의 결합으로 <span class=\"text-cyan-300 font-semibold\">공장/서비스 현장에 직접 투입</span> 가능한 수준으로 도약했다.",
            "양산 램프업을 이끄는 <span class=\"text-amber-300 font-bold\">정밀 모듈형 액추에이터와 관절 부품</span>이 로봇 기업의 경쟁력을 좌우한다.",
            "산업 현장 적용 확대로 <span class=\"text-violet-300 font-medium\">글로벌 로봇 밸류체인 주도권 다툼</span>이 격화되고 있다."
        ],
        "data_points": [
            "휴머노이드 로봇 시장 성장률: 연평균 40% 이상 가속화",
            "핵심 원가 비중: 액추에이터 및 정밀 감속기가 전체 제조 원가의 60% 차지"
        ],
        "signal": "bullish",
        "signal_reason": "피지컬 AI의 상용화가 임박함에 따라 로봇 완성품 및 핵심 부품 제조사들의 장기 이익 성장이 뚜렷하기 때문입니다.",
        "key_companies": ["테슬라", "보스턴다이내믹스", "유닛트리"],
        "insight": "휴머노이드 표준화의 핵심은 소프트웨어 지능과 고밀도 하드웨어 액추에이터의 완벽한 융합에 있습니다.",
        "action_point": "로봇 완성사 및 정밀 감속기, 모터, 관절 센서 분야의 핵심 소부장 종목 비중 확대를 권고합니다."
    },
    "Ae1VrybpCao": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["하이퍼스케일러", "CapEx", "AI버블", "교양이를부탁해", "반도체네러티브"],
        "summary": "빅테크 하이퍼스케일러들의 AI CapEx 폭증과 자금 조달 비용 상승으로 인한 <span class=\"text-rose-400 font-medium\">투자 수익성(ROI) 의구심</span>이 시장의 단기 조정을 유발하고 있습니다.",
        "key_claims": [
            "클라우드 서비스 및 AI 인프라 구축 비용 급증으로 <span class=\"text-rose-400 font-medium\">빅테크의 FCF(자유현금흐름) 압박</span> 가중.",
            "단기 과도한 AI 투자가 실질적 매출로 전환되는 시점에 대한 <span class=\"text-amber-300 font-bold\">시장의 엄격한 검증 국면</span> 진입.",
            "반도체 쏠림 해소와 함께 실질 현금흐름 창출 기업으로의 <span class=\"text-cyan-300 font-semibold\">자금 이동 전개</span>."
        ],
        "data_points": [
            "빅테크 자본지출(CapEx) 성장률: 연간 전년 대비 40% 초과",
            "하이퍼스케일러 채권 발행 및 CDS 프리미엄: 최근 사상 최고치 경신"
        ],
        "signal": "neutral",
        "signal_reason": "AI 장기 생태계 확장은 유효하나, 단기 CapEx 과열 노이즈로 인한 기술주 밸류에이션 리셋이 불가피하기 때문입니다.",
        "key_companies": ["마이크로소프트", "메타", "알파벳", "엔비디아"],
        "insight": "AI 투자 검증 국면에서는 단순 설비증설 기업보다 과금 모델과 플랫폼 수익화 기반을 입증한 기업이 승자가 됩니다.",
        "action_point": "AI 수익화 비즈니스 모델을 확보한 소프트웨어 및 플랫폼 우량주 중심의 포트폴리오 재편이 유효합니다."
    },
    "B5jTPYMZCm4": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["CXMT", "중국반도체", "과창판", "DUV", "SOD"],
        "summary": "중국 창신메모리(CXMT)의 과창판 상장과 주가 폭등은 이슈화되었으나, <span class=\"text-violet-300 font-medium\">레거시 공정 한계와 기술 격차</span>로 글로벌 첨단 메모리 시장 위협은 과장된 수준입니다.",
        "key_claims": [
            "CXMT의 과창판 상장 및 DUV 장비 도입은 <span class=\"text-amber-300 font-bold\">중국 내수용 레거시 자립</span>에 국한된다.",
            "20년 이상의 기술 격차와 EUV 부재로 인해 <span class=\"text-cyan-300 font-semibold\">HBM 및 첨단 DRAM 시장 침투는 불가능</span>하다.",
            "중국발 과도한 공급 과잉 공포는 국내 반도체 대장주에 대한 <span class=\"text-rose-400 font-medium\">단기 과매도 노이즈</span>일 뿐이다."
        ],
        "data_points": [
            "CXMT 과창판 상장 당일 주가 상승률: 466% 폭등",
            "글로벌 DRAM 점유율: CXMT 약 8~9% 수준으로 레거시 제품에 집중"
        ],
        "signal": "bullish",
        "signal_reason": "CXMT 우려가 과도한 기우로 확인됨에 따라 억눌렸던 SK하이닉스 및 삼성전자의 밸류에이션 리바운드가 기대되기 때문입니다.",
        "key_companies": ["CXMT", "SK하이닉스", "삼성전자", "마이크론"],
        "insight": "중국 반도체 굴기 노이즈는 레거시 영역에 한정되며, 첨단 HBM 생태계를 독점한 국내 기업의 실적 펀더멘털은 훼손되지 않았습니다.",
        "action_point": "CXMT 노이즈로 급락한 국내 메모리 반도체 및 HBM 밸류체인 대표 종목의 저가 매수를 권고합니다."
    },
    "CQ7VIUJsftM": {
        "primary_topic": "energy",
        "secondary_topics": ["tech"],
        "tags": ["에너지패러다임", "AI전력", "미래에셋", "애널리스트리포트", "SMR"],
        "summary": "AI 빅테크의 전력 수요 폭증으로 에너지 패러다임이 친환경 재생에너지에서 <span class=\"text-amber-300 font-bold\">원자력, SMR, 독립 전력망</span> 중심으로 급속히 전환되고 있습니다.",
        "key_claims": [
            "AI 데이터센터 전력 소요량 급증으로 <span class=\"text-cyan-300 font-semibold\">24/7 기저 전력원(원자력/SMR)</span>의 가치가 급상승했다.",
            "전력 송배전망 기기 및 VPP(가상발전소) 제어 솔루션 수요가 <span class=\"text-amber-300 font-bold\">구조적 장기 호황</span>에 진입했다.",
            "친기업적 세제와 독립 전력망을 갖춘 지역(텍사스 등)으로 <span class=\"text-violet-300 font-medium\">빅테크 AI 인프라 유입</span>이 집중된다."
        ],
        "data_points": [
            "AI 데이터센터 2030 전력 예상 소모량: 현재 대비 3배 이상 증가",
            "SMR 및 원전 관련 전력망 기기 수주 잔고: 연간 25% 이상 성장"
        ],
        "signal": "bullish",
        "signal_reason": "AI 인프라 확장에 필수적인 전력원 및 송배전 설비사들의 수주 가시성이 매우 명확하기 때문입니다.",
        "key_companies": ["지멘스", "GE에어로스페이스", "HD현대일렉트릭", "두산에너빌리티"],
        "insight": "AI 산업 혁명의 실질적 최대 수혜 분야는 컴퓨팅 칩을 넘어 지속 가능한 고효율 전력 인프라 산업입니다.",
        "action_point": "원자력/SMR 관련주 및 초고압 변압기, 송배전 기기 선도 종목 중심의 중장기 투자를 추천합니다."
    },
    "DaaqJSNcWqU": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["삼성전자", "SK하이닉스", "과도한낙폭", "삼프로TV", "김장열"],
        "summary": "중국 반도체 투자 둔화 및 AI 피크아웃 우려가 선반영되어 <span class=\"text-cyan-300 font-semibold\">삼성전자와 SK하이닉스 주가가 펀더멘털 대비 과도하게 하락</span>한 극저평가 구간입니다.",
        "key_claims": [
            "HBM 공급 부족과 레거시 DRAM 판가 상승 기조는 견조하며 <span class=\"text-cyan-300 font-semibold\">영업이익 호조세</span>는 지속된다.",
            "중국 DUV 우려 및 빅테크 CapEx 속도조절론은 시장의 <span class=\"text-rose-400 font-medium\">과도한 감정적 투매</span>를 유발했다.",
            "현재 주가 수준은 실적 가시성 대비 <span class=\"text-amber-300 font-bold\">강력한 가격 메리트</span>를 제공한다."
        ],
        "data_points": [
            "SK하이닉스 PBR: 최근 낙폭 과대로 역사적 평균 이하 하락",
            "메모리 반도체 2분기 영업이익률: HBM 비중 확대로 35% 이상 폭증"
        ],
        "signal": "bullish",
        "signal_reason": "실적 호조에도 불구하고 심리적 투매로 주가가 급락한 현 시점은 매우 매력적인 저가 매수 기회이기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스", "유니스토리자산운용"],
        "insight": "노이즈에 의한 일시적 투매 국면은 실적 펀더멘털이 확실한 반도체 대장주의 지분을 확대할 최적의 타이밍입니다.",
        "action_point": "삼성전자 및 SK하이닉스의 분할 저가 매수를 적극 추진할 것을 권고합니다."
    },
    "FcYxNJkNg9Y": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["국장탈출", "미국증시", "부동산", "삼프로TV", "김민수"],
        "summary": "국내 증시의 구조적 변동성과 세제 불확실성으로 인해 <span class=\"text-cyan-300 font-semibold\">미국 우량주 및 부동산 자산으로의 자금 이동</span> 트렌드가 가속화되고 있습니다.",
        "key_claims": [
            "국내 증시의 고질적인 디스카운트와 지배구조 이슈로 <span class=\"text-rose-400 font-medium\">개인 자금의 해외 탈출</span>이 지속된다.",
            "확실한 현금흐름과 주주환율이 보장되는 <span class=\"text-amber-300 font-bold\">미국 빅테크 및 패시브 자산</span> 선호도 심화.",
            "국내 주식은 철저히 실적 성장주 및 정책 수혜주에 한정된 <span class=\"text-cyan-300 font-semibold\">선별적 접근</span>이 필요하다."
        ],
        "data_points": [
            "서학개미 미국 주식 보유액: 사상 최대치 1,000억 달러 육박",
            "코스피 대형주 주주환원율: 미국(70%) 대비 30% 수준으로 정체"
        ],
        "signal": "neutral",
        "signal_reason": "국내 증시 수급 이탈 우려가 크나, 미국 우량자산 편입 확대를 통한 글로벌 자산 다변화 계기가 되기 때문입니다.",
        "key_companies": ["레몬리서치", "삼성전자", "애플", "마이크로소프트"],
        "insight": "자산 보유자는 국장 쏠림에서 벗어나 주주가치가 보장되는 글로벌 우량 자산으로의 포트폴리오 재편이 필수적입니다.",
        "action_point": "미국 시장 패시브 ETF(QQQ, SPY) 및 주주환원이 명확한 미국 우량 기술주 비중 확대를 권고합니다."
    },
    "fuEirRHNXcs": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["반도체끝났다", "AI네러티브", "교양이를부탁해", "알상무", "실적선행"],
        "summary": "반도체 피크아웃 피로감에도 불구하고, <span class=\"text-cyan-300 font-semibold\">실질 AI 비즈니스 ROI와 실적 선행성</span>을 바탕으로 AI 네러티브의 2차 성장이 진행 중입니다.",
        "key_claims": [
            "AI 랠리 종료 우려는 <span class=\"text-rose-400 font-medium\">단기 주가 조정에 따른 착시</span>일 뿐 펀더멘털은 탄탄하다.",
            "엔비디아, TSMC, 메모리 삼사의 <span class=\"text-amber-300 font-bold\">실적 선행 지표</span>는 하반기에도 견조한 성장을 입증한다.",
            "단순 기대감 장세에서 <span class=\"text-cyan-300 font-semibold\">실제 수주 및 현금 흐름 창출 기업</span> 중심의 옥석 가리기가 진행된다."
        ],
        "data_points": [
            "TSMC 및 메모리 공급사 수주 잔고: 2027년 물량까지 타이트한 계약 체결",
            "AI 반도체 전방 수요 성장률: 서버용 HBM 및 컴퓨팅 칩 연 35% 성장"
        ],
        "signal": "bullish",
        "signal_reason": "AI 네러티브가 실질 기업 이익으로 입증되고 있어 기술주 장기 우상향 추세가 훼손되지 않았기 때문입니다.",
        "key_companies": ["TSMC", "엔비디아", "SK하이닉스"],
        "insight": "시장의 노이즈성 비관론을 뚫고 실적 데이터가 보여주는 AI 펀더멘털의 실체에 주목해야 합니다.",
        "action_point": "반도체 조정으로 인한 주가 눌림목을 활용해 TSMC 및 HBM 수혜주 매수를 추천합니다."
    },
    "FzbdP5RBPos": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["애플", "삼성전자", "격차분석", "록펠러전략", "SOD"],
        "summary": "애플이 높은 마진과 본업 중심 '록펠러 전략'으로 <span class=\"text-cyan-300 font-semibold\">삼성전자와의 영업이익 및 시가총액 격차</span>를 지속적으로 벌려나가고 있습니다.",
        "key_claims": [
            "애플은 서비스 수익화와 자체 칩셋(M시리즈) 생태계로 <span class=\"text-amber-300 font-bold\">압도적인 영업이익률(30%+)</span>을 유지한다.",
            "삼성전자는 파운드리 및 메모리 변동성으로 인해 세트 부문의 <span class=\"text-rose-400 font-medium\">수익성 기복</span>을 경험하고 있다.",
            "소프트웨어 패권과 브랜딩 결합이 <span class=\"text-cyan-300 font-semibold\">글로벌 시총 1위 복귀</span>의 핵심 원동력이다."
        ],
        "data_points": [
            "애플 서비스 부문 매출 비중: 전체 매출의 25% 돌파하며 고마진 유지",
            "시가총액 격차: 애플 4.9조 달러 vs 삼성전자 4,000억 달러 안팎"
        ],
        "signal": "bullish",
        "signal_reason": "애플의 수직 통합 생태계와 안정적인 FCF 창출 능력이 독보적 주가 프리미엄을 정당화하기 때문입니다.",
        "key_companies": ["애플", "삼성전자"],
        "insight": "하드웨어 단가 경쟁보다 소프트웨어 생태계와 락인 효과를 거둔 기업이 장기 밸류에이션 재평가를 받습니다.",
        "action_point": "애플 중심의 글로벌 플랫폼 성장주 포트폴리오 유지를 적극 권고합니다."
    },
    "gjGzwyFMiMA": {
        "primary_topic": "economy",
        "secondary_topics": ["etc"],
        "tags": ["이란", "트럼프", "중동지정학", "호르무즈", "언더스탠딩", "박현도", "성일광"],
        "summary": "미국-이란 간 호르무즈 해협 지정학적 갈등과 중동 복잡성이 <span class=\"text-violet-300 font-medium\">유가 변동성 및 미국 외교 통상 압박</span>으로 작용하고 있습니다.",
        "key_claims": [
            "이란과의 무력 충돌 장기화는 트럼프 행정부의 <span class=\"text-rose-400 font-medium\">외교적 덫과 유가 상승 압력</span>을 가중시킨다.",
            "중제국(오만 등)을 통한 해협 관리 타결 여부가 <span class=\"text-cyan-300 font-semibold\">글로벌 에너지 인플레 완화</span>의 분수령이다.",
            "중동 불안정이 장기화될 경우 <span class=\"text-amber-300 font-bold\">글로벌 공급망 및 방산 수요</span>에 직간접적 영향을 준다."
        ],
        "data_points": [
            "호르무즈 해협 원유 수송량: 전 세계 원유 유통량의 20% 담당",
            "유가 변동 폭: 사태 진전 따라 배럴당 75~85달러 박스권 형성"
        ],
        "signal": "neutral",
        "signal_reason": "외교적 타결 시도가 전개되어 극단적 유가 폭등 가능성은 낮으나 지정학적 잔여 리스크가 존재하기 때문입니다.",
        "key_companies": ["서강대유로메나연구소"],
        "insight": "중동 지정학 이슈는 단기 유가 노이즈를 일으키나, 대화 모색 국면 진입 시 금융 시장은 안도감을 찾게 됩니다.",
        "action_point": "국제유가 80달러 이하 유지 여부를 관찰하며 지정학 위험 완화 수혜주 및 방산주 비중을 조절할 필요가 있습니다."
    },
    "GmdsiH1t-MQ": {
        "primary_topic": "etc",
        "secondary_topics": ["tech"],
        "tags": ["AI애니메이션", "ZooRangers", "미래에셋", "콘텐츠자동화"],
        "summary": "생성형 AI 애니메이션 및 멀티미디어 제작 도구가 발전하면서 <span class=\"text-cyan-300 font-semibold\">콘텐츠 생산 비용의 획기적 하락과 제작 자동화</span>가 가속화되고 있습니다.",
        "key_claims": [
            "AI 기반 영상/애니메이션 생성 기술로 <span class=\"text-amber-300 font-bold\">제작 기간 및 비용 80% 감축</span>.",
            "미디어/엔터테인먼트 산업의 <span class=\"text-cyan-300 font-semibold\">콘텐츠 생성 패러다임 변화</span> 전개.",
            "소형 크리에이터 및 기업들의 <span class=\"text-violet-300 font-medium\">브랜드 마케팅 생산성 극대화</span>."
        ],
        "data_points": [
            "AI 애니메이션 렌더링 속도: 기존 대비 10배 이상 향상",
            "제작 단가 절감 비율: 분당 영상 제작 비용 기존 1/5 수준 감소"
        ],
        "signal": "bullish",
        "signal_reason": "AI 멀티미디어 솔루션 도입으로 디지털 콘텐츠 기업들의 이익률 개선이 뚜렷하기 때문입니다.",
        "key_companies": ["미래에셋", "OpenAI", "Runway"],
        "insight": "생성형 AI는 텍스트를 넘어 고화질 영상 및 애니메이션 영역으로 확장되어 미디어 생산성을 대폭 높이고 있습니다.",
        "action_point": "AI 콘텐츠 제작 솔루션 및 미디어 플랫폼 우량 기업에 대한 관심을 추천합니다."
    },
    "h9qH9ObG_oM": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["유가급락", "증시혼조", "미래에셋", "데일리라이브", "FOMC경계"],
        "summary": "국제 유가 급락에도 불구하고 <span class=\"text-rose-400 font-medium\">FOMC 금리 경계감과 반도체 실망 매물</span>로 인해 증시가 상승 탄력을 얻지 못하고 혼조세를 보였습니다.",
        "key_claims": [
            "유가 하락으로 인플레이션 압력은 완화되었으나 <span class=\"text-rose-400 font-medium\">통화 정책 불확실성</span>이 증시를 압박했다.",
            "반도체주 약세에도 불고하고 <span class=\"text-cyan-300 font-semibold\">산업재·소비재 순환매</span>가 지수 하방을 받쳤다.",
            "FOMC 발표 전까지 <span class=\"text-amber-300 font-bold\">관망세 및 분목 차별화 장세</span>가 유지될 전망이다."
        ],
        "data_points": [
            "WTI 유가 하락률: 배럴당 79달러선으로 6% 이상 급락",
            "증시 지수 변동: 다우 상승 vs 나스닥 약보합"
        ],
        "signal": "neutral",
        "signal_reason": "에너지 비용 하락이라는 긍정적 요인과 반도체 조정이라는 악재가 팽팽히 대립하고 있기 때문입니다.",
        "key_companies": ["미래에셋증권"],
        "insight": "유가 안정은 소비 여력을 높여주므로 순환매 장세에서 소비자 및 산업재 종목이 우수한 성과를 냅니다.",
        "action_point": "FOMC 결과 확인 전까지 유가 하락 수혜주(항공/소비재) 중심의 제한적 접근을 추천합니다."
    },
    "jgsZfXZBkuk": {
        "primary_topic": "crypto",
        "secondary_topics": ["stock"],
        "tags": ["비트코인", "반도체동반하락", "크립토PLUS", "블록미디어", "FOMC변수"],
        "summary": "비트코인과 반도체 섹터의 동반 하락은 <span class=\"text-rose-400 font-medium\">위험자산 전반의 단기 유동성 위축</span>을 반영하며, 7월 FOMC 결과가 최대 변수입니다.",
        "key_claims": [
            "비트코인 63,000달러선 유동성과 기술주 조정이 결합되어 <span class=\"text-rose-400 font-medium\">위험자산 회피 심리</span> 형성.",
            "MSTR(마이크로스트레티지) 등 비트코인 트레저리 기업들의 <span class=\"text-cyan-300 font-semibold\">하방 지지력 유효</span>.",
            "FOMC 통화 정책 신호에 따라 <span class=\"text-amber-300 font-bold\">크립토 및 반도체의 동시에 반등</span> 가능성 타진."
        ],
        "data_points": [
            "비트코인 가격: 63,000달러선 보합권 형상",
            "MSTR 전환사채 조달: BPS 성장 연계 자금 집행 지속"
        ],
        "signal": "neutral",
        "signal_reason": "FOMC 정책 지표에 따라 단기 유동성 흐름이 재결정되는 길목에 서 있기 때문입니다.",
        "key_companies": ["블록미디어", "MSTR", "Coinbase"],
        "insight": "크립토와 기술주는 글로벌 유동성에 함께 연동되므로, 거시 금리 정책의 완화 신호가 시장 반등의 핵심 촉매입니다.",
        "action_point": "FOMC 발표 전 비트코인 및 크립토 관련 자산의 관망세 유지 및 눌림목 매수 전략을 권고합니다."
    },
    "jSev0DDdttI": {
        "primary_topic": "crypto",
        "secondary_topics": ["stock"],
        "tags": ["주식토큰화", "RWA", "온도파이낸스", "시큐리타이즈", "크립토PLUS"],
        "summary": "실물자산 토큰화(RWA) 및 주식 토큰화 시장 개막으로 <span class=\"text-cyan-300 font-semibold\">온도 파이낸스, 시큐리타이즈</span> 등 온체인 금융 인프라 수혜주가 부각되고 있습니다.",
        "key_claims": [
            "전통 주식 및 채권의 온체인 토큰화(RWA)로 <span class=\"text-cyan-300 font-semibold\">24/7 글로벌 거래 인프라</span> 형성.",
            "블랙록 BUIDL 펀드 유입 확대 등으로 <span class=\"text-amber-300 font-bold\">기관 자금의 토큰화 시장 편입</span> 가속화.",
            "온도(Ondo) 및 기관용 커스터디 기업들이 <span class=\"text-violet-300 font-medium\">RWA 수수료 수익 선점</span>."
        ],
        "data_points": [
            "RWA(실물자산 토큰화) 시장 규모: 2030년까지 10조 달러 성장 전망",
            "블랙록 BUIDL 토큰화 펀드 잔고: 5억 달러 초과 달성"
        ],
        "signal": "bullish",
        "signal_reason": "전통 제도권 월가 자본이 토큰화(RWA) 시장으로 본격 유입되는 초기 개화 단계이기 때문입니다.",
        "key_companies": ["Ondo Finance", "Securitize", "BlackRock", "엑스크립톤"],
        "insight": "RWA는 크립토와 전통 금융을 잇는 가장 확실한 유즈케이스로, 토큰화 프로토콜 기업의 성장이 기대됩니다.",
        "action_point": "RWA 대장주(온도 등) 및 제도권 연계 디지털 자산 인프라 기업에 대한 선제적 분할 접근을 권고합니다."
    },
    "lKCUguooVwM": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["미국증시혼조", "반도체하락", "미래에셋", "데일리라이브"],
        "summary": "미국 증시가 반도체주 급락에도 불구하고 필수소비재 및 금융주의 강세로 <span class=\"text-amber-300 font-bold\">섹터 간 균형을 이루며 혼조 마감</span>했습니다.",
        "key_claims": [
            "엔비디아 및 마이크론 급락이 나스닥 지수를 끌어내렸으나 <span class=\"text-rose-400 font-medium\">지수 폭락은 방지</span>되었다.",
            "S&P 500 동일가중 지수의 우위가 증명하듯 <span class=\"text-cyan-300 font-semibold\">수순환매 장세</span> 지속 전개.",
            "빅테크 실적 발표를 앞두고 <span class=\"text-amber-300 font-bold\">투심 관망 및 업종 다변화</span> 강화."
        ],
        "data_points": [
            "나스닥 지수: -0.18% 약보합 마감",
            "필수소비재/헬스케어 섹터: +1.2% 상승하며 반도체 약세 상쇄"
        ],
        "signal": "neutral",
        "signal_reason": "섹터 로테이션으로 시장 전체 붕괴 위험은 낮으나 기술주의 단기 변동성이 이어지기 때문입니다.",
        "key_companies": ["미래에셋증권"],
        "insight": "반도체 일변도의 장세에서 벗어나 시장 자금이 다양한 우량 실적주로 분산되는 건강한 조정 과정입니다.",
        "action_point": "기술주 편중 포트폴리오를 필수소비재 및 우량 밸류주로 일부 다변화할 것을 권고합니다."
    },
    "lsSI3o7jFE8": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["월가선행지표", "삼성전자", "SK하이닉스", "애플금의환향", "한경글로벌마켓"],
        "summary": "월가가 한국 반도체 대장주를 빅테크 실적의 선행지표로 주시하는 가운데, <span class=\"text-cyan-300 font-semibold\">애플이 본업 모멘텀으로 종가 기준 시총 1위</span>에 금의환향했습니다.",
        "key_claims": [
            "한국 반도체 주가 흐름이 미국 빅테크 CapEx 및 실적 선행 지표로 <span class=\"text-amber-300 font-bold\">월가의 핵심 지표화</span>되었다.",
            "애플은 과도한 AI CapEx 대신 본업 마진을 지킨 '록펠러 전략'으로 <span class=\"text-cyan-300 font-semibold\">시총 1위 복귀</span> 성공.",
            "코카콜라, 보잉 등의 실적 호조가 <span class=\"text-violet-300 font-medium\">전통 우량주의 밸류 재평가</span>를 견인."
        ],
        "data_points": [
            "애플 시가총액: 4조 9,480억 달러로 엔비디아 상회 1위 탈환",
            "삼성전자/SK하이닉스 외국인 수급: 월가 기술주 투심과 밀접 연동"
        ],
        "signal": "bullish",
        "signal_reason": "애플 등 글로벌 대형 펀더멘털주들의 가치 상승이 미국 및 한국 증시 하방을 지지하기 때문입니다.",
        "key_companies": ["애플", "삼성전자", "SK하이닉스", "코카콜라", "보잉"],
        "insight": "글로벌 증시는 AI 기술주 일변도에서 벗어나 확실한 펀더멘털과 현금흐름을 증명하는 선도 기업으로 재편되고 있습니다.",
        "action_point": "애플 중심의 펀더멘털 우량주와 선행지표 역할을 하는 국내 반도체 대표주의 동시 보유를 추천합니다."
    },
    "NLmprEofQgc": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["AI사이클", "지식뉴스", "교양이를부탁해", "AI전반부종료", "냉정한신호"],
        "summary": "AI 랠리의 1단계 인프라 구축 사이클 전반부가 일단락되고, <span class=\"text-amber-300 font-bold\">실질 수익성과 서비스 ROI를 입증해야 하는 냉정한 2단계</span> 진입을 경고합니다.",
        "key_claims": [
            "GPU 및 서버 칩 싹쓸이 중심의 AI 1단계 랠리가 <span class=\"text-rose-400 font-medium\">소강 상태 및 수익성 검증</span> 국면에 진입했다.",
            "하이퍼스케일러들의 CapEx 지출 속도가 <span class=\"text-cyan-300 font-semibold\">실질 서비스 과금 매출</span>로 연결되어야 추가 랠리가 가능하다.",
            "단순 칩 제조사보다 <span class=\"text-amber-300 font-bold\">AI 소프트웨어 플랫폼 선도 기업</span>으로 시장 주도권이 이동한다."
        ],
        "data_points": [
            "AI 인프라 사이클 기간: 2023~2025년 1단계 팽창 완료 후 2단계 진입",
            "AI 소프트웨어 마진율 예상: 서비스 안정화 시 50% 이상 고마진 기대"
        ],
        "signal": "neutral",
        "signal_reason": "AI 산업의 지형 변화로 인한 단기 주가 밸류에이션 리셋과 옥석 가리기가 동시에 일어날 것이기 때문입니다.",
        "key_companies": ["엔비디아", "마이크로소프트", "OpenAI", "Meta"],
        "insight": "AI 사이클의 2단계에서는 단순 설비 투자 기업보다 실질 사용자 과금 기반을 굳힌 플랫폼 사가 승자가 됩니다.",
        "action_point": "하드웨어 단독 쏠림을 줄이고 AI 서비스 및 킬러 앱을 보유한 소프트웨어 대표주로 포트폴리오를 분산하십시오."
    },
    "ppxqGKs9KgM": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["미중갈등", "시장상황", "이효석아카데미", "Z1뉴스", "패권경쟁"],
        "summary": "미국과 중국 간의 반도체 및 AI 기술 패권 전쟁이 <span class=\"text-violet-300 font-medium\">글로벌 공급망 재편과 자산 시장 변동성</span>을 지속해서 유도하고 있습니다.",
        "key_claims": [
            "미국의 대중 반도체 제재와 중국의 DUV/레거시 국산화 시도가 <span class=\"text-violet-300 font-medium\">지정학적 리스크</span>를 고착화한다.",
            "미중 기술 분리로 인한 글로벌 공급망 이원화가 <span class=\"text-rose-400 font-medium\">기업들의 설비 투자 비용을 가중</span>시킨다.",
            "한국 기업들은 미중 사의에서 <span class=\"text-cyan-300 font-semibold\">전략적 반사이익과 수급 변동성</span>을 동시에 경험하고 있다."
        ],
        "data_points": [
            "미중 기술 제재 품목: 첨단 EUV 노광장비 및 HBM 메모리 포함",
            "글로벌 공급망 재편 비용: 주요 기업 생산 거점 분산으로 CapEx 15% 증가"
        ],
        "signal": "neutral",
        "signal_reason": "지정학적 불확실성이 상존하나, 우방국 공급망 중심의 한국 반도체/배터리 반사이익 기회도 명확하기 때문입니다.",
        "key_companies": ["이효석아카데미"],
        "insight": "미중 패권 전쟁 속에서는 우방국 밸류체인에 포함된 정밀 제조업체들의 가치가 더욱 부각됩니다.",
        "action_point": "지정학적 리스크에 둔감하고 미국 우방국 공급망에 직결된 소부장 우량주 중심의 투자 전략이 유효합니다."
    },
    "RFiHglleqv8": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["코스피바닥", "차트분석", "교양이를부탁해", "바닥과천장", "알상무"],
        "summary": "코스피 지수가 10% 급락하며 기술적 지지선에 도달한 가운데, <span class=\"text-cyan-300 font-semibold\">역사적 PBR 하단 지지선(바닥) 확인</span>에 따른 매수 관점이 부각되고 있습니다.",
        "key_claims": [
            "코스피 급락은 수급적 과매도에 의한 것으로 <span class=\"text-cyan-300 font-semibold\">역사적 PBR 바닥권(0.85배)</span>에 도달했다.",
            "차트 및 수급 분석 상 과도한 투매 구간은 <span class=\"text-amber-300 font-bold\">중장기 기술적 반등의 기틀</span>을 형성한다.",
            "외국인 수급의 매도세 정체 시점부터 <span class=\"text-cyan-300 font-semibold\">지수 리바운드</span>가 강력하게 진행될 수 있다."
        ],
        "data_points": [
            "코스피 PBR 지지선: 0.83~0.85배 수준 (역사적 강력한 바닥 형성 구간)",
            "외국인 순매도 규모: 지수 10% 폭락 과정에서 극단적 과매도 기록"
        ],
        "signal": "bullish",
        "signal_reason": "기술적 밸류에이션 바닥권 도달로 추가 하락 위험보다 반등 리턴이 월등히 큰 구간이기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "지수 폭락의 끝자락에서는 공포에 투매하기보다 역사적 PBR 바닥 지표를 신뢰하는 저가 매수가 승리합니다.",
        "action_point": "코스피 레버리지 및 시가총액 상위 대형주의 분할 매수를 추천합니다."
    },
    "um4PzXdXXMQ": {
        "primary_topic": "economy",
        "secondary_topics": ["etc"],
        "tags": ["사우디", "후티반군", "중동군사", "언더스탠딩", "방산지정학"],
        "summary": "사우디아라비아가 후티 반군의 드론/미사일 공격에 대응하며 고가의 미사일을 소모함에 따라 <span class=\"text-rose-400 font-medium\">비대칭 전력 및 비대칭 군사비 부담</span> 문제가 부각되고 있습니다.",
        "key_claims": [
            "고가 방공 미사일로 저가 드론을 방어하는 구조는 <span class=\"text-rose-400 font-medium\">지속 불가능한 비대칭 비용 부담</span>을 유발한다.",
            "중동 방산 시장에서 <span class=\"text-cyan-300 font-semibold\">저비용 고효율 안티드론 및 레이저 방공 체계</span>의 중요성이 급증한다.",
            "지정학적 불안 지속으로 <span class=\"text-amber-300 font-bold\">글로벌 방산 기업들의 수주 모멘텀</span>이 장기화되고 있다."
        ],
        "data_points": [
            "방공 미사일 vs 후티 드론 단가 격차: 요격 미사일 1발(수십억 원) vs 드론 1대(수천만 원)",
            "중동 방산비 지출 성장률: 비대칭 위협 대응으로 연 10% 이상 증가"
        ],
        "signal": "bullish",
        "signal_reason": "비대칭 안티드론 및 정밀 방공 체계를 갖춘 국내외 방산 기업들의 해외 수출 기회가 확대되기 때문입니다.",
        "key_companies": ["한화에어로스페이스", "LIG넥스원", "현대로템"],
        "insight": "현대전의 양상이 비대칭 드론 및 저비용 미사일전으로 재편되면서 안티드론 및 가성비 방산 솔루션의 가치가 치솟고 있습니다.",
        "action_point": "안티드론 시스템 및 고효율 방공 미사일 기술을 보유한 K-방산 기업에 대한 중장기 유효 투자를 권고합니다."
    },
    "vFfx2CVZzE8": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["오전방송", "엔비디아급락", "WTI유가폭락", "삼프로TV", "증시조정"],
        "summary": "엔비디아 5% 급락으로 나스닥 지수만 단기 조정을 받는 가운데, <span class=\"text-cyan-300 font-semibold\">WTI 유가가 8% 폭락하며 인플레이션 완화 안도감</span>을 제공했습니다.",
        "key_claims": [
            "엔비디아 등 반도체주 급락이 기술주 지수 하락을 견인했으나 <span class=\"text-cyan-300 font-semibold\">타 섹터로의 순환매</span>는 양호했다.",
            "WTI 유가 8% 폭락은 <span class=\"text-amber-300 font-bold\">거시 인플레이션 피크아웃 신호</span>로 작용해 시중 금리 안정에 기여한다.",
            "증시는 기술주 독주에서 벗어나 <span class=\"text-violet-300 font-medium\">다변화된 업종 밸런스</span>를 갖춰가고 있다."
        ],
        "data_points": [
            "WTI 유가 하락률: 장중 8% 폭락하며 78달러선 안착",
            "엔비디아 주가 변동: 단기 5% 급락으로 기술주 지수 압박"
        ],
        "signal": "neutral",
        "signal_reason": "엔비디아 조정에 따른 기술주 투심 악화와 유가 폭락으로 인한 인플레 완화 호재가 호각을 이루기 때문입니다.",
        "key_companies": ["엔비디아", "삼프로TV"],
        "insight": "유가 폭락은 거시 환경 개선 신호이며, 기술주 단기 조정 후 증시 전반의 바닥 지지력을 강화해 줄 것입니다.",
        "action_point": "유가 하락 수혜주 편입과 함께 엔비디아의 기술적 지지선 확인 후 분할 재매수 전략을 추천합니다."
    },
    "WribtmjU2rw": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["코스닥위험", "삼성전자실적", "교양이를부탁해", "알상무", "실적격차"],
        "summary": "삼성전자가 연간 50조 원 이익을 올리는 거대 대형주 장세 속에서, <span class=\"text-rose-400 font-medium\">실적 펀더멘털이 부실한 코스닥 중소형주의 위험성</span>이 극대화되고 있습니다.",
        "key_claims": [
            "코스피 대형주는 튼튼한 영업이익을 기록 중이나 <span class=\"text-rose-400 font-medium\">코스닥 적자 바이오/IT 기업</span>은 유동성 고갈 위험에 직면했다.",
            "금리 고착화와 디레버리징 환경에서는 <span class=\"text-amber-300 font-bold\">실적 기반 흑자 대형주 쏠림</span>이 더욱 심화된다.",
            "테마성 코스닥 중소형주에 대한 <span class=\"text-rose-400 font-medium\">리스크 관리 및 포트폴리오 슬림화</span>가 시급하다."
        ],
        "data_points": [
            "삼성전자 영업이익 전망: 연간 50조 원 육박",
            "코스닥 상장사 적자 비율: 40% 이상으로 유동성 경색 가중"
        ],
        "signal": "bearish",
        "signal_reason": "실적이 없는 코스닥 중소형주의 수급 이탈과 차별화로 인한 추가 하락 리스크가 높기 때문입니다.",
        "key_companies": ["삼성전자"],
        "insight": "고금리 및 디레버리징 국면에서는 이익을 내지 못하는 중소형주보다 확실한 이익을 거두는 대형주가 절대적으로 안전합니다.",
        "action_point": "코스닥 실적 부실주를 정리하고 코스피 200 시가총액 상위 흑자 대형주 중심으로 포트폴리오를 교체하십시오."
    },
    "wrTNLsmtXOc": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["포트폴리오재정비", "반도체필수", "삼프로TV", "박병창", "여의도인사이트"],
        "summary": "반도체주 단기 급락에도 불구하고 AI 산업에 <span class=\"text-cyan-300 font-semibold\">반도체는 대체 불가능한 필수 재화</span>이므로 past peak를 잊고 포트폴리오를 재정비해야 합니다.",
        "key_claims": [
            "과거 최고가에 연연하지 말고 <span class=\"text-cyan-300 font-semibold\">현재 실적 가치 기준</span>으로 반도체 비중을 재설정해야 한다.",
            "AI 서버, HBM, 온디바이스 등 반도체 수요의 본질적 성장 구조는 <span class=\"text-amber-300 font-bold\">변함없이 견조</span>하다.",
            "단기 공포 장세는 <span class=\"text-cyan-300 font-semibold\">포트폴리오 밸런싱 및 교체 매수</span>의 최적 기회이다."
        ],
        "data_points": [
            "HBM 시장 연평균 성장률: 2028년까지 45% 고성장 유지 전망",
            "반도체 밸류체인 주가 할인율: 최근 조정으로 전고점 대비 20~30% 할인"
        ],
        "signal": "bullish",
        "signal_reason": "반도체의 산업적 필수성과 이익 성장성이 확실한 상황에서 단기 조정은 재매수의 적기이기 때문입니다.",
        "key_companies": ["MP파트너스", "SK하이닉스", "삼성전자"],
        "insight": "주가 전고점에 대한 미련을 버리고, 기업의 본질적 성장성에 기반하여 포트폴리오의 품질을 높여야 합니다.",
        "action_point": "조정받은 메모리 반도체 및 핵심 소부장 종목의 비중을 단계적으로 확대하는 포트폴리오 재정비를 추천합니다."
    },
    "Wrto3usUozY": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["코스피폭락", "삼전닉스무너짐", "삼프로TV", "클로징벨", "마감시황"],
        "summary": "삼성전자와 SK하이닉스의 급락으로 코스피가 10% 폭락하며 투매가 연출되었으나, <span class=\"text-amber-300 font-bold\">과도한 수급 공포의 피크권</span>을 통과 중입니다.",
        "key_claims": [
            "반도체 투매가 지수 폭락을 유도하며 <span class=\"text-rose-400 font-medium\">전 종목 무차별 하락 패닉</span> 발생.",
            "신용 반대매매 및 외국인 선물 매도로 인한 <span class=\"text-cyan-300 font-semibold\">기술적 이격 과대 구간</span> 진입.",
            "패닉 투매가 일단락되는 시점에서 <span class=\"text-amber-300 font-bold\">급반등의 리바운드 장세</span>가 전개될 가능성 우세."
        ],
        "data_points": [
            "코스피 단기 낙폭: 고점 대비 10% 폭락 기록",
            "삼성전자/SK하이닉스 하락 기여도: 지수 하락 폭의 60% 이상 차지"
        ],
        "signal": "bullish",
        "signal_reason": "무차별 투매가 극에 달한 시점은 전형적인 지수 바닥 신호로 강력한 기술적 반등이 임박했기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "패닉 투매의 마지막 단계에서는 이성적인 기업 가치가 무시되나, 수급 클리어링 후 가장 빠른 복원력을 보여줍니다.",
        "action_point": "마감 투매에 동참하지 말고 투매가 그친 후 코스피 200 지수형 ETF 및 반도체 대장주의 저점 매수를 준비하십시오."
    },
    "Xe78bgnviLQ": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["미중AI후폭풍", "TSMC지진", "구글웨이모국내진출", "삼프로TV", "뉴스3"],
        "summary": "미중 AI·반도체 갈등과 일본 강진에 따른 TSMC/토요타 생산 차질 노이즈 속에서, <span class=\"text-cyan-300 font-semibold\">구글 웨이모의 한국 자율주행 시장 진출</span>이 새로운 변수로 부각되었습니다.",
        "key_claims": [
            "미중 기술 갈등과 일본 지진이 겹치며 <span class=\"text-rose-400 font-medium\">반도체 및 자동차 공급망 불안</span> 유발.",
            "구글 웨이모의 한국 시장 진출 타진으로 <span class=\"text-cyan-300 font-semibold\">국내 자율주행 및 모빌리티 생태계</span> 재편 촉발.",
            "단기 공급망 차질 악재 속에서도 <span class=\"text-amber-300 font-bold\">차세대 자율주행 모멘텀</span> 부상."
        ],
        "data_points": [
            "TSMC/토요타 일본 공장: 강진 영향으로 일시 가동 중단 점검",
            "구글 웨이모 자율주행 한국 진출: 국내 모빌리티 파트너십 타진"
        ],
        "signal": "neutral",
        "signal_reason": "자연재해 및 미중 제재 단기 악재와 자율주행 시장 팽창 호재가 교차하고 있기 때문입니다.",
        "key_companies": ["Google", "Waymo", "TSMC", "토요타", "현대차"],
        "insight": "단기 자연재해 및 지정학 노이즈는 일시적이나, 자율주행 등 피지컬 AI 생태계의 한국 진출은 장기적 산업 변화를 이끕니다.",
        "action_point": "구글 웨이모 국내 진출 관련 자율주행 센서, 부품, 지도 데이터 수혜주에 대한 선제적 관심을 권고합니다."
    },
    "XYlXpDyB_sM": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["검은화요일", "외세침략투매", "삼프로TV", "오후방송", "국내증시"],
        "summary": "외국인의 무차별 매도와 해외 노이즈로 '검은 화요일'을 겪은 국내 증시는 <span class=\"text-cyan-300 font-semibold\">기업 펀더멘털을 벗어난 수급 붕괴</span> 상태로, 과도한 투매 지양을 당부합니다.",
        "key_claims": [
            "해외 악재 수입과 외국인 선물 매도로 인한 <span class=\"text-rose-400 font-medium\">국내 증시의 비이성적 투매</span>.",
            "삼성전자 등 주요 기업 이익 대비 <span class=\"text-cyan-300 font-semibold\">주가 하락 폭이 지나치게 과도</span>한 기형적 장세.",
            "수급 쏠림 현상이 진정되면 <span class=\"text-amber-300 font-bold\">빠른 이격 축소 반등</span>이 전개될 수밖에 없음."
        ],
        "data_points": [
            "외국인 순매도 규모: 코스피 시장에서 단기 대규모 수급 유출",
            "하락 종목 비율: 코스피/코스닥 90% 이상 종목 하락 기록"
        ],
        "signal": "bullish",
        "signal_reason": "펀더멘털과 무관한 외부 수급 붕괴에 따른 투매는 강력한 기술적 가격 반등을 수반하기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "외국인 수급 붕괴로 발생한 과도한 낙폭은 냉정함을 되찾은 시장에서 가장 매력적인 반등 보상으로 돌아옵니다.",
        "action_point": "투매에 편승한 손절을 피하고, 펀더멘털이 우수한 코스피 대표주를 침착하게 보유할 것을 권고합니다."
    },
    "yAf1p4oqN8g": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["창신메모리", "외국인큰그림", "삼전닉스던짐", "삼프로TV", "주린이구조대"],
        "summary": "외국인이 창신메모리(CXMT) 이슈를 핑계로 국내 반도체 대장주를 흔든 것은 <span class=\"text-cyan-300 font-semibold\">저가 재매수를 노린 외국인의 수급 플레이</span>일 가능성이 높습니다.",
        "key_claims": [
            "CXMT 우려는 핑계일 뿐 <span class=\"text-rose-400 font-medium\">외국인의 단기 시세 조작 및 차익 실현</span> 수급 플레이.",
            "HBM 기술 격차로 인해 <span class=\"text-cyan-300 font-semibold\">CXMT가 삼성/하이닉스를 대체하는 것은 불가능</span>하다.",
            "외국인 매도세 정과 함께 <span class=\"text-amber-300 font-bold\">강력한 숏커버링 및 재매수 장세</span>가 연출될 전망이다."
        ],
        "data_points": [
            "CXMT 기술 수준: DUV 기반 레거시 DRAM 집중 (HBM 제조 불가능)",
            "외국인 반도체 포지션: 선물 매도 및 현물 차익실현 동시 진행"
        ],
        "signal": "bullish",
        "signal_reason": "외국인의 의도적 노이즈 흔들기 이후 저가 재매수가 유입되며 반도체 대장주가 가파르게 회복될 것이기 때문입니다.",
        "key_companies": ["CXMT", "SK하이닉스", "삼성전자"],
        "insight": "외국인 수급 판읽기가 중요하며, 기술 격차가 입증된 국내 반도체 기업의 펀더멘털을 신뢰해야 합니다.",
        "action_point": "외국인 매도세가 잦아드는 시점에서 SK하이닉스 및 삼성전자의 매수를 추천합니다."
    },
    "YN9VE77PA8Q": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["미국반도체지수", "블룸에너지", "시게이트", "테라다인", "호실적", "삼프로TV"],
        "summary": "미국 필라델피아 반도체 지수가 약세장에 진입했으나, <span class=\"text-cyan-300 font-semibold\">시게이트, 블룸에너지, 테라다인 등 실적 선도 기업의 시간 외 폭등</span>이 차별화 장세를 증명하고 있습니다.",
        "key_claims": [
            "반도체 지수 약세 진입에도 불구하고 <span class=\"text-cyan-300 font-semibold\">확실한 실적(시게이트/블룸에너지)을 낸 기업</span>은 시간에 폭등했다.",
            "단순 테마주에서 <span class=\"text-amber-300 font-bold\">실질 어닝 서프라이즈 기업으로 자금 이동</span>이 명확히 관찰된다.",
            "빅테크 실적 시즌 진행으로 <span class=\"text-cyan-300 font-semibold\">실적주 위주의 증시 분위기 반전</span>이 기대된다."
        ],
        "data_points": [
            "시게이트 시간 외 주가 상승률: +7.8% 급등 (가이던스 대폭 상회)",
            "블룸에너지 시간 외 주가 상승률: +5% 이상 폭등 (매출 116% 증가)"
        ],
        "signal": "bullish",
        "signal_reason": "어닝 서프라이즈를 달성한 실적주들에 대한 강력한 시장 보상이 증시 안도감을 형성하기 때문입니다.",
        "key_companies": ["시게이트", "블룸에너지", "테라다인", "엔비디아"],
        "insight": "지수 약세장 속에서도 시장의 눈높이를 뛰어넘는 가시적 실적을 증명한 기업은 독보적인 주가 상승을 누립니다.",
        "action_point": "실적 발표 후 가이던스를 상향한 시게이트 및 전력/자동화 우량 실적주에 집중 투자하십시오."
    },
    "z-lBSaZGKRA": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["반도체의심", "코스피무너짐", "7월증시", "염승환", "삼프로TV"],
        "summary": "반도체 이익 지속성에 대한 시장의 의심으로 코스피가 무너졌으나, <span class=\"text-cyan-300 font-semibold\">하반기 실제 영업이익 확인 시 의구심 해소</span>와 함께 가파른 복원력을 보일 것입니다.",
        "key_claims": [
            "반도체 피크아웃 우려는 <span class=\"text-rose-400 font-medium\">근거 없는 감정적 의구심</span>이 확산된 결과이다.",
            "HBM3E 양산 확대 및 범용 DRAM 공급 부족으로 <span class=\"text-amber-300 font-bold\">하반기 실적은 추가 상향</span>된다.",
            "7월 증시의 극단적 악재 선반영은 <span class=\"text-cyan-300 font-semibold\">8월 실적 장세의 강력한 반등 발판</span>이 된다."
        ],
        "data_points": [
            "SK하이닉스 하반기 영업이익 전망: 분기별 사상 최고치 경신 예상",
            "코스피 7월 수익률: 글로벌 증시 대비 극단적 하회"
        ],
        "signal": "bullish",
        "signal_reason": "시장의 의구심이 무색할 정도로 하반기 실적이 강력하게 증명될 것이기 때문입니다.",
        "key_companies": ["SK하이닉스", "삼성전자", "염승환"],
        "insight": "시장이 이익의 지속성을 의심할 때가 가장 저렴하게 지분을 모을 수 있는 투자의 기회입니다.",
        "action_point": "염승환 이사의 제언처럼 반도체 대장주의 조정을 활용한 중장기 분할 매수를 강력 추천합니다."
    },
    "zQy5tNLAMEs": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["미국증시혼조", "순환매장세", "반도체급락", "미래에셋", "데일리라이브"],
        "summary": "미국 증시가 반도체주 급락에도 불구하고 <span class=\"text-amber-300 font-bold\">강력한 섹터 순환매(Rotation)</span>에 힘입어 지수 붕괴 없이 혼조세로 마감하며 장세 펀더멘털을 과시했습니다.",
        "key_claims": [
            "반도체 급락 악재에도 <span class=\"text-cyan-300 font-semibold\">산업재·헬스케어·필수소비재로의 돈의 이동</span>이 지수를 버텼다.",
            "시장의 자금이 주식 시장을 이탈하는 것이 아니라 <span class=\"text-amber-300 font-bold\">실적 우수 업종으로 순환매</span>되고 있다.",
            "FOMC와 빅테크 실적을 거치며 <span class=\"text-cyan-300 font-semibold\">증시가 균형 잡힌 다변화 상승 구조</span>를 갖출 것이다."
        ],
        "data_points": [
            "S&P 500 동일가중 지수: 시가총액 가중 지수 대비 높은 수익률 기록",
            "다우존스 지수: +1% 이상 상승하며 52,700선 최고치 경신"
        ],
        "signal": "bullish",
        "signal_reason": "순환매 장세는 증시 전체의 기초체력이 탄탄하다는 방증으로 기술주 조정 후 전반적 상승 전환이 예상되기 때문입니다.",
        "key_companies": ["미래에셋증권", "코카콜라", "캐터필러"],
        "insight": "반도체 조정은 악재가 아닌 증시 내 자금이 다양한 우량 업종으로 퍼져나가는 건강한 로테이션입니다.",
        "action_point": "순환매 수혜가 뚜렷한 산업재 및 필수소비재 대표주 편입과 반도체 눌림목 매수 병행을 권고합니다."
    }
}

# Process each video in analyses dictionary
for vid, data in analyses.items():
    topic_id = data["primary_topic"]
    full_json = {
        "video": json.loads((pending_dir / f"{vid}.json").read_text(encoding="utf-8"))["video"],
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

print("\n[SUCCESS] All 34 pending videos have been analyzed and saved successfully!")
