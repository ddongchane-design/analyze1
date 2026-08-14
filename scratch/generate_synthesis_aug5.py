import json
from pathlib import Path

synthesis_updates_aug5 = {
    "stock": {
        "consensus": "bullish",
        "cross_insight": "8월 4~5일 글로벌 증시는 유가 급락(-5%)과 <span class=\"text-cyan-300 font-semibold\">팔란티어(+15~30% 폭등)</span>, 캐터필러 호실적에 힘입어 다우 지수 및 S&P500이 <span class=\"text-amber-300 font-bold\">사상 최고치를 경신</span>하며 월가에서 \"기술주 매도세가 공식 종료되었다\"는 선언이 나오는 강세장 2라운드 진입을 알림. 국내 증시는 코스피 지수가 6,000선 하단 지지력을 바탕으로 장기 8,000~9,300pt 도약 시나리오가 거론되는 가운데, 삼전닉스 단일 쏠림에서 <span class=\"text-cyan-300 font-semibold\">코스닥 소부장 장비주, 방산, 주주환원 밸류업 금융주</span>로 자금이 퍼지는 선순환 순환매 장세가 전개되고 있음.",
        "divergence": "코스피 거래대금 감소 및 ISA 계좌 만기 세제 불확실성에 따른 단기 보수론과, 팔란티어/아마존 실적 폭발 및 연준 금리 인하 호재에 따른 대세 반등 낙관론이 교차함.",
        "key_themes": [
            "팔란티어 30% 대폭등 및 S&P500/다우 지수 사상 최고치 경신에 따른 기술주 매도 종료",
            "삼성전자·SK하이닉스 메모리 슈퍼사이클 중심에 둔 채 방산·조선·밸류업 금융주를 섞는 바벨 포트폴리오",
            "코스피 소강 시 수급 빈집 상태인 코스닥 전공정 소부장 장비주로의 강한 순환매"
        ],
        "watch_list": [
            "SK하이닉스(000660) 및 삼성전자(005930) HBM4 판가(ASP) 상승 및 3분기 실적 발표",
            "팔란티어(PLTR), 아마존(AMZN), 엔비디아(NVDA) 주가 2라운드 랠리 지지선",
            "정부 주주환원 밸류업 지수 개편 및 KB금융, 신한지주 등 고배당 금융주"
        ]
    },
    "tech": {
        "consensus": "bullish",
        "cross_insight": "AI 반도체 시장은 <span class=\"text-cyan-300 font-semibold\">HBM4 가격 상승원인(4나노/3나노 베이스 다이 로직 공정 융합)</span> 분석과 빅테크의 천문학적 AI CapEx 지속 지출로 강력한 단가 상승 및 마진 확대 국면에 접어듦. <span class=\"text-cyan-300 font-semibold\">오픈AI 상장 추진</span>이 AI 랠리의 최후 빅이벤트이자 밸류에이션 도약 축복의 변곡점으로 떠올랐으며, 엔비디아 코어 반도체의 압도적 독주 속에 B2B AI 실적(팔란티어 AIP) 수익화 입증이 기술주 반등을 수놓고 있음.",
        "divergence": "AMD 가이던스 아쉬움 및 하위 AI 스타트업 자금난 경고 신호(코어 대 주변 양극화)와, HBM4 ASP 폭등 및 오픈AI 상장 모멘텀에 따른 AI 실적 랠리 지속론이 상충함.",
        "key_themes": [
            "HBM4 베이스 다이 선단 로직 융합에 따른 판가(ASP) 폭등 및 한국 메모리 마진율 최고치",
            "오픈AI IPO 상장 추진 모멘텀과 B2B AI 서비스(팔란티어 AIP) 실질 수익화 가시화",
            "고금리에도 빅테크 CapEx(2,000억 달러 이상) 계속 확장 및 엔비디아 블랙웰 수혜"
        ],
        "watch_list": [
            "삼성전자 및 SK하이닉스의 HBM4 베이스 다이 수율 및 핀당 16Gbps 속도 달성",
            "오픈AI 기업가치 1,000억 달러 이상 상장 일정 및 마이크로소프트(MSFT) 연동",
            "엔비디아(NVDA) Blackwell B200 랙 스케일 출하량 및 가동률"
        ]
    },
    "economy": {
        "consensus": "bullish",
        "cross_insight": "WTI 국제 유가가 배럴당 72달러선(-5.2%)으로 급락하며 인플레이션 우려가 대폭 완화되었고, 미 연준의 9월 금리 인하 착수 기대감이 글로벌 증시에 연착륙 훈풍을 제공함. 일본에서는 <span class=\"text-cyan-300 font-semibold\">라피더스 반도체 공장 유치</span>로 홋카이도 지가가 30년 만에 버블 수준을 경신하고 <span class=\"text-cyan-300 font-semibold\">메가뱅크(MUFG)가 시총 1위</span>에 등극하는 등 반도체 국가 투자와 금융 부활이 눈부신 반면, 국내는 서울 아파트 공사비 폭등 수주 축소와 외환 시장 구조적 변동성 개혁 과제가 상존함.",
        "divergence": "미국 국채 금리 급등과 원/달러 외환시장 변동성 우려와, 유가 하락 및 금리 인하에 따른 인플레이션 완화 훈풍이 맞섬.",
        "key_themes": [
            "WTI 유가 5% 급락에 따른 인플레이션 완화와 연준 금리 인하 명분 강화",
            "일본 라피더스 반도체 투자 지가 폭등 및 메가뱅크 부활 사례",
            "은퇴 노후 자금의 인플레이션 방어를 위한 배당 성장주 현금흐름 자산배분"
        ],
        "watch_list": [
            "WTI 국제 유가 배럴당 70달러선 지지력 및 미국 9월 FOMC 금리 인하 폭",
            "원/달러 환율 추이 및 서울 외환시장 구조 개선 정책",
            "국내 아파트 공사비 및 대형 건설사 PF 우발채무 안정성"
        ]
    },
    "robot": {
        "consensus": "bullish",
        "cross_insight": "구글 딥마인드가 단순 AI 에이전트를 넘어 <span class=\"text-cyan-300 font-semibold\">피지컬 로보틱스(Gemini Robotics, RT-2)</span>에 대규모 집중 투자하며 AGI의 물리적 관문을 열고 있음. 유니트리 21조 원 기업가치 평가와 더불어 현장 실시간 상호작용 멀티모달 데이터 확보가 화두가 되면서, 국내 <span class=\"text-cyan-300 font-semibold\">로보티즈 및 감속기/액추에이터</span> 부품사들의 글로벌 재평가가 가속화되고 있음.",
        "divergence": "로봇 대량 양산 및 가격 하락 지연 신중론과, 구글/엔비디아의 피지컬 AI 올인 및 산업 현장 구인난 해소용 로봇 폭발 낙관론 대립.",
        "key_themes": [
            "구글 딥마인드의 피지컬 로보틱스 올인 및 Gemini Robotics 데이터 확보",
            "유니트리 21조 원 평가 수혜에 따른 국내 로보티즈 등 감속기/액추에이터 부품사 재평가",
            "스마트 건설 및 공장 물류 현장의 모듈형 로봇 도입 확산"
        ],
        "watch_list": [
            "구글 Gemini Robotics 파운데이션 모델 업데이트 및 실물 로봇 연동",
            "로보티즈(108860) 초소형 감속기/액추에이터 실적 증가율",
            "레인보우로보틱스, 두산로보틱스 등 로봇 대장주 수급"
        ]
    },
    "energy": {
        "consensus": "bullish",
        "cross_insight": "빅테크들이 AI 데이터센터 전력난을 극복하기 위해 송전선 인허가(3~5년 소요)를 우회하여 <span class=\"text-amber-300 font-bold\">데이터센터 바로 옆에 발전소를 직결 건설</span>하는 초대형 인프라 전환을 시작함. 이에 따라 <span class=\"text-cyan-300 font-semibold\">초고압 변압기(HD현대일렉트릭, 효성중공업)</span> 및 가스 발전, SMR(소형모듈원자로) 관련 기업들의 수주잔고가 역대 최대치를 경신하며 시장 최고 주도주로 안착함.",
        "divergence": "국제 유가 급락에 따른 에너지 단가 하락 압력과, 빅테크 AI 전력망 부족에 따른 변압기/독립 발전소 장기 붐이 양존.",
        "key_themes": [
            "빅테크의 데이터센터 직결 발전소(원자력/가스) 대규모 직접 건설 전환",
            "미국 AI 전력난에 따른 초고압 변압기 및 SMR 모듈 수주 폭등",
            "전력 계통 과부하 방지를 위한 가상발전소(VPP) 및 독점 인프라 기업 수혜"
        ],
        "watch_list": [
            "HD현대일렉트릭(267260), 효성중공업(298040) 수주잔고 및 영업이익률",
            "미국 SMR 개발사(뉴스케일파워 등) 및 데이터센터 전력 계약 공시",
            "GE버노바 등 글로벌 전력 인프라 대장주 주가 흐름"
        ]
    },
    "crypto": {
        "consensus": "neutral",
        "cross_insight": "가상자산 시장은 미국 <span class=\"text-violet-300 font-medium\">클래리티 법안(Clarity Act)</span>의 연내 통과 확률이 윤리 수정안 마찰로 50%에서 27%로 급락하며 단기 관망세를 보였으나, 미국 국채 금리 급등 장세 속에서 <span class=\"text-cyan-300 font-semibold\">비트코인의 디지털 금(Gold) 가치 저장 자산</span> 입지는 견고하게 유지됨. 기관 자금의 실물자산 토큰화(RWA) 결합 기조는 훼손되지 않음.",
        "divergence": "클래리티 법안 입법 지연에 따른 알트코인 수급 위축 우려와, 비트코인 현물 ETF 기관 자금 유입 및 디지털 금 대체 낙관론 대립.",
        "key_themes": [
            "미국 클래리티 법안 연내 통과 확률 급락과 단기 규제 입법 노이즈",
            "국채 금리 급등 속 비트코인 기관 자금의 하방 지지력 검증",
            "RWA 실물자산 토큰화 및 기업용 트레저리 유입 지속"
        ],
        "watch_list": [
            "비트코인(BTC) 6만 4천 달러 지지선 및 현물 ETF 순유입액",
            "미국 의회 클래리티 법안 수정안 협상 재개 여부",
            "마이크로스트래티지(MSTR) 및 코인베이스(COIN) 주가 추이"
        ]
    }
}

def update_synthesis():
    dest = Path("data/synthesis")
    dest.mkdir(parents=True, exist_ok=True)
    for topic, data in synthesis_updates_aug5.items():
        out_p = dest / f"{topic}.json"
        out_p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[SYNTHESIS AUG 5 UPDATED] {out_p}")

if __name__ == "__main__":
    update_synthesis()
