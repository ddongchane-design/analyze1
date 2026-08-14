import json
from pathlib import Path

synthesis_updates = {
    "stock": {
        "consensus": "bullish",
        "cross_insight": "8월 초 글로벌 증시는 엔화 환율 변동성(엔 캐리 트레이드 청산 수급)과 빅테크 실적 발표가 맞물리며 코스피가 폭등 후 급락하는 <span class=\"text-rose-400 font-medium\">극심한 진통 변동성 장세</span>를 연출함. 그럼에도 불구하고 <span class=\"text-cyan-300 font-semibold\">팔란티어(+12%)</span>와 <span class=\"text-cyan-300 font-semibold\">아마존(+15%)</span>의 어닝 서프라이즈, 다우 지수의 사상 최고치 경신, 그리고 <span class=\"text-cyan-300 font-semibold\">SK하이닉스·삼성전자</span>의 3분기 HBM3E 이익 가시성이 하단을 강력하게 받치고 있음. 전문가들은 급락 갭하락을 공포의 손절이 아니라 우량주를 저점에 주울 수 있는 <span class=\"text-amber-300 font-bold\">기능별 자산배분 및 저점 분할 매수 기회</span>로 적극 활용할 것을 권고함.",
        "divergence": "사상 최대 폭등 후 일시적 외국인 매도세와 엔화 강세로 인한 추가 조정 가능성을 경고하는 신중론이 있는 반면, 레버리지 반대매매 청산 완료와 강한 실적 펀더멘털에 기반해 8월 전강후강 반등 장세가 전개될 것이라는 낙관론이 팽팽히 맞섬.",
        "key_themes": [
            "빅테크 실적 발표(팔란티어, 아마존 호조 vs 애플 약세)에 따른 AI 수익화 차별화 장세",
            "엔/달러 환율 변동성 및 엔 캐리 트레이드 청산 영향에 따른 코스피 일시적 조정",
            "삼성전자·SK하이닉스 대장주 비중을 고수한 채 방산·조선·고배당주를 섞는 바벨 전략"
        ],
        "watch_list": [
            "SK하이닉스(000660) 및 삼성전자(005930) HBM3E/HBM4 공급 성과 및 외국인 수급 전환",
            "팔란티어(PLTR) 및 아마존(AMZN) 실적 발표 후 주가 추이와 AI CapEx 효율성",
            "엔/달러 환율 145엔 하회 여부 및 미국 연준 금리 인하 기대감"
        ]
    },
    "tech": {
        "consensus": "bullish",
        "cross_insight": "AI 반도체 시장은 단순 D램 적층에서 차세대 <span class=\"text-cyan-300 font-semibold\">HBM4 베이스 다이(4나노/TSMC 공정)</span> 로직 융합으로 전장이 이동하고 있으며, 초고가 NVL 랙 스케일 시스템 구축과 수냉식 쿨링 및 전력 인프라가 핵심 경쟁력으로 부상함. 중국 <span class=\"text-cyan-300 font-semibold\">CXMT</span>의 범용 D램 공포는 미국 장비 제재로 과장된 소음임이 확인된 반면, 빅테크의 천문학적 AI CapEx 지출과 FCF(잉여현금) 관리 능력 및 B2B AI 엔터프라이즈(팔란티어 AIP)의 실질 매출 검증이 <span class=\"text-amber-300 font-bold\">AI 랠리 2라운드</span>의 성패를 가르고 있음.",
        "divergence": "빅테크 숨은 부채(2,390조 원)와 FCF 하락 및 인도 IT 아웃소싱 고용 둔화에 따른 AI 버블 캐즘 경고론과, HBM4 로직 융합 및 실질 B2B 매출 증대에 힘입어 기술주 독주가 이어질 것이라는 환호론이 상충함.",
        "key_themes": [
            "HBM4 베이스 다이 로직 융합(삼성 4나노 vs SK하이닉스-TSMC) 및 랙 스케일 AI 팩토리",
            "CXMT 중국 반도체 공포 과장 입증 및 미국 장비 규제 하의 한국 HBM 독점 선점",
            "AI CapEx와 FCF(잉여현금흐름) 방어 능력을 갖춘 빅테크 중심의 2라운드 실적 차별화"
        ],
        "watch_list": [
            "삼성전자 파운드리 4나노 HBM4 베이스 다이 수율 및 SK하이닉스-TSMC 밸류체인",
            "엔비디아(NVDA) NVL72/144 수냉식 쿨링 시스템 출하량 및 수주잔고",
            "팔란티어(PLTR), 구글(GOOGL) AI 클라우드 실적 및 자사주 매입 체력"
        ]
    },
    "economy": {
        "consensus": "neutral",
        "cross_insight": "글로벌 매크로 환경은 미-일 당국의 <span class=\"text-amber-300 font-bold\">엔화 방어 구출 작전</span> 및 스콧 베선트의 환율 개입 발언으로 엔/달러 환율이 급변동함에 따라 <span class=\"text-rose-400 font-medium\">엔 캐리 트레이드 청산 리스크</span>가 재차 고조됨. 국내적으로는 종부세 장특공제 한도 축소 등 부동산 세제 개편과 내수 소비 양극화(다이소 초저가 vs 샤넬 초고가) 현상이 깊어지는 가운데, 미 연준의 금리 인하 재개 기대감과 매크로 변동성이 교차하며 팽팽한 관망세를 형성함.",
        "divergence": "엔화 강세 전환으로 인한 신흥국 자금 유출 및 내수 경기 양극화 악화 우려와, 미 연준의 9월 금리 인하 착수 및 환율 개입에 따른 변동성 해소 기대감이 대립 중.",
        "key_themes": [
            "미-일 공동 엔화 방어 작전 및 엔 캐리 트레이드 청산에 따른 글로벌 자금 요동",
            "초고가·비거주 주택 종부세 세제 개편 및 국내 소득/소비 양극화 심화",
            "미 국채 금리 상승 속 연준 금리 인하 기대감과 매크로 리스크 관리"
        ],
        "watch_list": [
            "엔/달러 환율 추이 및 일본은행(BOJ) 통화 정책 방향",
            "미국 9월 FOMC 기준금리 인하 폭 및 국채 10년물 금리 반응",
            "국내 내수 유통주 및 초가성비 리테일 기업들의 영업이익률"
        ]
    },
    "robot": {
        "consensus": "bullish",
        "cross_insight": "로봇 산업은 중국 휴머노이드 선두주자 <span class=\"text-cyan-300 font-semibold\">유니트리(Unitree)의 21조 원 기업가치</span> 충격 평가가 공개되며 실험실을 지나 대량 양산 및 피지컬 AI 단계로 진입했음을 입증함. 이에 따라 국내 로봇 액추에이터 및 초소형 감속기 기술을 보유한 <span class=\"text-cyan-300 font-semibold\">로보티즈</span> 등 핵심 부품기업들의 글로벌 밸류체인 재평가가 본격화되고 있음.",
        "divergence": "범용 휴머노이드의 일상 보급 속도에 대한 신중한 시각과, 감속기/모터 국산화 및 산업 현장 특화 로봇 상용화가 폭발적으로 앞당겨질 것이라는 강한 낙관론이 공존함.",
        "key_themes": [
            "유니트리 21조 원 밸류에이션 충격과 피지컬 AI 상용화 가속",
            "로보티즈 등 국내 액추에이터 및 핵심 감속기 부품기업 재평가",
            "산업/건설 현장의 구인난 해소를 위한 로봇 자동화 도입"
        ],
        "watch_list": [
            "로보티즈(108860) 액추에이터 수주 공급 계약 및 실적 지표",
            "유니트리 및 글로벌 휴머노이드 로봇 기업 양산 일정",
            "레인보우로보틱스, 두산로보틱스 등 대장주의 기술 협력 성과"
        ]
    },
    "crypto": {
        "consensus": "bullish",
        "cross_insight": "암호화폐 시장은 미국 의회 통과를 앞둔 <span class=\"text-violet-300 font-medium\">클래리티 법안(Clarity Act)</span> 윤리 수정안 등 입법 명확화 논의와 <span class=\"text-cyan-300 font-semibold\">실물 자산 토큰화(RWA)</span> 시장 팽창이 제도권 자금 유입을 자극함. 전통 금융 기관의 비트코인 및 이더리움 포트폴리오 편입과 신금융 인프라 결합이 지속되어 장기 가치 상승 흐름을 형성 중임.",
        "divergence": "윤리 수정안 추가로 인한 입법 표결 지연 가능성과, 제도화에 따른 월가 기관 자금의 폭발적 편입 기대가 대립함.",
        "key_themes": [
            "미국 클래리티 법안 통과 수순 및 규제 명확화 호재",
            "실물 자산 토큰화(RWA) 시장의 전통 금융 융합 및 기관 자금 유입",
            "비트코인 및 이더리움 대장주 중심의 가치 저장 수단 안착"
        ],
        "watch_list": [
            "미국 의회 클래리티 법안 표결 진행 및 SEC/CFTC 관할권 정리",
            "비트코인(BTC) 6만5천 달러 돌파 여부 및 기관 ETF 유입액",
            "코인베이스(COIN) 및 RWA 플랫폼 연계 기업 실적"
        ]
    },
    "space": {
        "consensus": "bullish",
        "cross_insight": "우주산업은 일론 머스크의 <span class=\"text-cyan-300 font-semibold\">스페이스X</span> 첫 실적 공개와 기업가치 40조 달러 장기 전망, 그리고 <span class=\"text-cyan-300 font-semibold\">스타링크</span> 가입자 폭증에 힘입어 민간 우주 랠리를 가속화함. 우주 제조(In-Space Manufacturing)와 궤도 회수 캡슐 기술이 가시화되며 우주항공 밸류체인의 이익 가시성이 부각됨.",
        "divergence": "보호예수 물량 해소 및 높은 밸류에이션 부담에 대한 단기 조정론과, 민간 우주 인터넷 및 무인 캡슐 우주 물류가 만들 사상 최대 시장에 대한 환호론이 대립함.",
        "key_themes": [
            "스페이스X 첫 실적 공개 및 스타링크 B2B 이익 창출력 검증",
            "민간 우주 제조 및 궤도 캡슐 회수 등 차세대 우주 물류 프로젝트",
            "머스크 우주 생태계 확장에 따른 관련 밸류체인 수혜"
        ],
        "watch_list": [
            "스페이스X 추가 발사 테스트 및 상장 진행 관련 소식",
            "스타링크 글로벌 가입자 성장세 및 B2B 서비스 확장",
            "테슬라(TSLA) 및 우주항공 관련 부품사 저점 수급"
        ]
    }
}

def update_synthesis():
    dest = Path("data/synthesis")
    dest.mkdir(parents=True, exist_ok=True)
    for topic, data in synthesis_updates.items():
        out_p = dest / f"{topic}.json"
        out_p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[SYNTHESIS UPDATED] {out_p}")

if __name__ == "__main__":
    update_synthesis()
