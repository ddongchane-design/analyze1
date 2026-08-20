import json
import os
from pathlib import Path

ANALYSIS_DATA = {
    "-Ww4XXgvVlo": {
        "primary_topic": "stock",
        "analysis": {
            "summary": "샌디스크 인베스터데이 이후 주가 30% 상승과 뉴욕 증시의 금리 불확실성 여파를 분석함. <span class=\"text-cyan-300 font-semibold\">메모리 반도체</span> 섹터의 강세와 거시경제적 금리 인상 우려가 혼재된 장세임.",
            "key_claims": ["샌디스크 등 메모리 기업들의 실적 기대감이 주가를 견인 중임", "금리 불확실성은 기술주 전반에 변동성을 부여하고 있음"],
            "data_points": ["샌디스크 주가 30% 상승"],
            "signal": "neutral",
            "signal_reason": "개별 종목 호재와 매크로 불안이 상쇄됨",
            "key_companies": ["샌디스크"],
            "insight": "반도체 섹터 내에서도 실적 가시성이 높은 기업 위주로 차별화된 흐름이 전개됨.",
            "action_point": "금리 방향성에 따른 포트폴리오 리밸런싱 및 반도체 비중 조절 필요"
        },
        "tags": ["샌디스크", "미국증시", "금리인상", "반도체"]
    },
    "0q1ZlstvTZk": {
        "primary_topic": "energy",
        "analysis": {
            "summary": "AI 경쟁에서 핵심 병목으로 부상한 <span class=\"text-amber-300 font-bold\">전력 인프라 및 냉각 기술</span>을 조명함. 데이터센터 확충에 필수적인 안정적 에너지 공급망이 <span class=\"text-cyan-300 font-semibold\">K-반도체</span>의 미래 경쟁력을 결정지을 것임.",
            "key_claims": ["AI 데이터센터는 막대한 전력과 효율적 냉각이 필수임", "에너지 공급 여력이 곧 국가 및 기업의 AI 경쟁력임"],
            "data_points": [],
            "signal": "bullish",
            "signal_reason": "전력 및 냉각 인프라 관련주에 대한 구조적 수요 증가",
            "key_companies": [],
            "insight": "AI 투자는 소프트웨어와 칩셋을 넘어 전력과 냉각 등 물리적 인프라 투자로 확장되고 있음.",
            "action_point": "데이터센터용 수냉식 쿨링 및 전력기기 공급업체 주목"
        },
        "tags": ["AI데이터센터", "전력인프라", "수냉식쿨링", "에너지"]
    },
    "7AfxcaDXWLY": {
        "primary_topic": "economy",
        "analysis": {
            "summary": "빅테크 기업들의 <span class=\"text-amber-300 font-bold\">부도보험(CDS 프리미엄)</span>이 600% 이상 급증한 현상을 통해, 시장 내 누적된 고평가 리스크와 신용 경색 우려를 진단함.",
            "key_claims": ["빅테크 밸류에이션 고점 논란 속 신용 위험 지표가 악화됨"],
            "data_points": ["빅테크 CDS 프리미엄 600% 급증"],
            "signal": "bearish",
            "signal_reason": "빅테크 주도 장세의 취약성과 신용 위험 확대",
            "key_companies": [],
            "insight": "AI 랠리로 가려졌던 빅테크들의 펀더멘털 외적인 부채 및 거시 리스크가 수면 위로 부상 중임.",
            "action_point": "빅테크 비중 축소 및 가치주/현금 확보 고려"
        },
        "tags": ["빅테크", "부도보험", "신용위험", "미국경제"]
    },
    "asuDSvnHz5Q": {
        "primary_topic": "stock",
        "analysis": {
            "summary": "주식 시장의 높은 변동성 속에서도 <span class=\"text-cyan-300 font-semibold\">흔들리지 않는 투자 원칙</span>의 중요성을 강조함. 시장의 단기적 '굴욕'을 견뎌야 장기적 수익을 달성할 수 있음을 역사적 사례로 증명함.",
            "key_claims": ["변동성은 주식 투자의 필연적 비용임", "시장 타이밍보다 장기 보유 원칙이 중요함"],
            "data_points": [],
            "signal": "neutral",
            "signal_reason": "단기 변동성 확대 장세 지속",
            "key_companies": [],
            "insight": "하락장과 조정은 장기 투자자에게 저가 매수의 기회이자 포트폴리오를 점검할 계기임.",
            "action_point": "투기적 쏠림 현상 배제 및 우량주 중심의 분할 매수"
        },
        "tags": ["투자원칙", "장기투자", "주식변동성"]
    },
    "ejabe8LSQtg": {
        "primary_topic": "robot",
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">피지컬 AI(로봇)</span> 시대의 도래로 데이터 처리량이 급증하며 메모리 반도체 수요가 1,000배 이상 증가할 수 있음을 분석함. <span class=\"text-cyan-300 font-semibold\">삼성전자</span>가 로봇 산업을 신성장 동력으로 키우는 본질적 이유임.",
            "key_claims": ["휴머노이드 및 피지컬 AI는 막대한 메모리와 엣지 컴퓨팅을 요구함", "삼성전자의 로봇 투자는 자사 반도체 생태계 확장을 위한 포석임"],
            "data_points": ["로봇 AI 시대 메모리 요구량 1,000배 폭증 전망"],
            "signal": "bullish",
            "signal_reason": "로봇 산업 개화로 인한 차세대 반도체 및 부품 생태계의 폭발적 성장",
            "key_companies": ["삼성전자", "테슬라"],
            "insight": "로봇은 움직이는 거대한 스마트폰이자 데이터센터로, 온디바이스 AI 메모리의 최대 수요처가 될 것임.",
            "action_point": "로봇 구동용 시스템 반도체, 센서, 고용량 메모리 밸류체인 점검"
        },
        "tags": ["피지컬AI", "로봇", "삼성전자", "메모리반도체"]
    },
    "eNuhdtXb8S4": {
        "primary_topic": "economy",
        "analysis": {
            "summary": "앤트로픽의 가파른 매출 성장과 가치 평가, 골드만삭스의 금리 인상 사이클 종료 전망, 기관 투자자들의 13F 공시 내용 및 트럼프의 지정학적 발언 등을 망라하여 <span class=\"text-amber-300 font-bold\">미국 경제 및 글로벌 매크로 환경</span>을 종합 분석함.",
            "key_claims": ["AI 유니콘(앤트로픽)의 폭발적 성장세가 지속됨", "9월 기준금리 인상 가능성 축소", "지정학적 리스크 장기화 우려"],
            "data_points": ["앤트로픽 매출 14배 급증"],
            "signal": "neutral",
            "signal_reason": "금리 동결 호재와 정치/지정학적 리스크가 맞물림",
            "key_companies": ["앤트로픽"],
            "insight": "거시적 불확실성 속에서도 AI 소프트웨어 및 인프라 기업들의 실적은 차별적으로 우상향하고 있음.",
            "action_point": "기관(13F) 포트폴리오를 참고하여 AI 관련 주도주 포지션 유지"
        },
        "tags": ["앤트로픽", "금리인상", "13F", "미국경제", "트럼프"]
    },
    "gs_t5MCZ7Mk": {
        "primary_topic": "economy",
        "analysis": {
            "summary": "스타트업 투자금이 개인의 빚으로 전가되는 구조적 문제와 벤처 캐피탈(VC) 생태계의 그림자를 신철호 대표의 인터뷰를 통해 짚어봄. <span class=\"text-amber-300 font-bold\">스타트업 생태계</span>의 자본 구조와 창업자의 리스크 관리에 대한 통찰을 제공함.",
            "key_claims": ["과도한 투자 유치는 창업자의 지분 희석과 연대보증 등 리스크를 키움"],
            "data_points": [],
            "signal": "na",
            "signal_reason": "VC 및 벤처 생태계 분석",
            "key_companies": ["OGQ"],
            "insight": "유동성 파티가 끝난 후 벤처 생태계는 옥석 가리기와 자본 효율성을 강요받고 있음.",
            "action_point": "비상장 주식 및 벤처 투자 펀드에 대한 보수적 접근 필요"
        },
        "tags": ["스타트업", "벤처투자", "VC", "부채"]
    },
    "id2adAbxlEE": {
        "primary_topic": "economy",
        "analysis": {
            "summary": "트럼프의 한미연합훈련 축소 시사 발언이 미치는 지정학적 파장과, <span class=\"text-cyan-300 font-semibold\">구광모-젠슨 황</span>의 AI 동맹, <span class=\"text-cyan-300 font-semibold\">최태원-빌 게이츠</span>의 SMR(소형모듈원전) 동맹 등 주요 재계 총수들의 글로벌 합종연횡을 조명함.",
            "key_claims": ["미국 대선 결과에 따라 한반도 지정학적 리스크가 요동칠 수 있음", "국내 대기업들이 글로벌 빅테크와 AI 및 차세대 에너지 분야 생존 동맹을 맺고 있음"],
            "data_points": [],
            "signal": "neutral",
            "signal_reason": "지정학적 불안과 기술 혁신 동맹이라는 상반된 재료 혼재",
            "key_companies": ["LG전자", "엔비디아", "SK", "테라파워"],
            "insight": "AI와 에너지 패권 경쟁에서 살아남기 위한 기업 간 크로스보더(Cross-border) 파트너십이 필수가 됨.",
            "action_point": "SMR 및 AI 반도체 공급망에 편입된 국내 기업들의 장기 비전 주목"
        },
        "tags": ["트럼프", "SMR", "LG전자", "엔비디아", "SK"]
    },
    "jYJjcbOQbhA": {
        "primary_topic": "stock",
        "analysis": {
            "summary": "월가 거물들이 <span class=\"text-cyan-300 font-semibold\">알파벳(구글)</span>을 대거 매수하는 배경과, 공포지수(VIX) 최저 수준에도 불구하고 시장 저변에 깔린 불안 심리를 분석함. 빅테크 실적 장세 속 숨고르기 국면임.",
            "key_claims": ["알파벳의 AI 경쟁력과 밸류에이션 매력이 부각됨", "낮은 VIX는 향후 변동성 급증의 전조일 수 있음"],
            "data_points": [],
            "signal": "neutral",
            "signal_reason": "지수 고점 부담과 빅테크 개별 종목 장세 지속",
            "key_companies": ["알파벳", "구글"],
            "insight": "시장 지수의 방향성보다 개별 기업의 펀더멘털과 AI 수익화 가능성이 투자의 핵심 기준이 됨.",
            "action_point": "구글 등 상대적으로 덜 오른 AI 소프트웨어 플랫폼 기업 비중 확대 고려"
        },
        "tags": ["미국증시", "알파벳", "VIX", "월가구루"]
    },
    "KA8dXfkD2J8": {
        "primary_topic": "economy",
        "analysis": {
            "summary": "미 국채 30년물 금리가 19년래 최고치를 경신한 거시 경제 상황과 13F 공시를 통해 드러난 스페이스X의 주주 구성, 그리고 피터 틸의 인프라 중심 <span class=\"text-amber-300 font-bold\">'삽과 곡괭이' 투자 전략</span>을 분석함.",
            "key_claims": ["장기 국채 금리 상승은 주식 시장의 밸류에이션 부담으로 작용함", "스페이스X 등 우주 인프라 산업에 기관 자금이 몰리고 있음"],
            "data_points": ["미 국채 30년물 금리 19년래 최고치"],
            "signal": "bearish",
            "signal_reason": "장기 국채 금리 급등에 따른 할인율 상승 부담",
            "key_companies": ["스페이스X", "팔란티어"],
            "insight": "AI 붐 시대에 AI 자체보다 전력, 인프라, 데이터센터 등 필수 기반 시설(삽과 곡괭이)에 투자하는 것이 가장 확실한 수익 창출 방법임.",
            "action_point": "고금리 환경에서 재무가 건전한 인프라 및 가치주로의 단기 피난처 마련"
        },
        "tags": ["국채금리", "13F", "스페이스X", "피터틸"]
    },
    "kW6v2a9IZN4": {
        "primary_topic": "tech",
        "analysis": {
            "summary": "애플의 차세대 칩셋 생산 전략과 공급망 재편이 <span class=\"text-amber-300 font-bold\">미국 본토 반도체 제조 부흥(칩스법 등)</span>에 미치는 영향을 비판적으로 살펴봄. 애플의 철저한 공급망 단가 인하 압박이 자국 내 반도체 생태계 마진을 위협할 수 있음.",
            "key_claims": ["애플의 대만 TSMC 의존도와 자국 내 팹 활용에 대한 회의적 시각", "미국 내 파운드리 공장의 높은 제조 단가가 걸림돌임"],
            "data_points": [],
            "signal": "neutral",
            "signal_reason": "미국 반도체 자급주의의 현실적 한계와 비용 문제 부각",
            "key_companies": ["애플", "TSMC", "인텔"],
            "insight": "글로벌 테크 거인들의 원가 절감 의지와 국가주의적 공급망 재편 사이의 괴리가 파운드리 산업의 장기 숙제임.",
            "action_point": "파운드리 시장의 지정학적 프리미엄과 실제 수율 경쟁력 사이의 격차 확인 필요"
        },
        "tags": ["애플", "TSMC", "미국반도체", "파운드리"]
    },
    "MADsi36tWmk": {
        "primary_topic": "stock",
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">테슬라</span>의 최근 전기차 성장 둔화 및 주춤한 주가 흐름의 본질적 이유를 일론 머스크의 전략 부재와 전기차 시장 캐즘(Chasm)에서 찾음. 단순 가격 인하만으로는 해결할 수 없는 수요 한계에 직면함.",
            "key_claims": ["글로벌 전기차 수요 성장률 둔화가 테슬라 펀더멘털을 압박함", "신모델(모델2) 부재 및 자율주행 상용화 지연이 투자 심리 악화의 원인임"],
            "data_points": [],
            "signal": "bearish",
            "signal_reason": "전기차 시장의 캐즘 진입과 테슬라 마진 훼손 우려",
            "key_companies": ["테슬라"],
            "insight": "테슬라는 이제 전기차 제조사를 넘어 AI/로보틱스 기업으로의 패러다임 전환(FSD, 옵티머스 등)을 증명해야만 프리미엄을 유지할 수 있음.",
            "action_point": "전기차 수요 회복 지표 확인 전까지 배터리 및 부품 밸류체인에 대한 보수적 시각 견지"
        },
        "tags": ["테슬라", "전기차", "캐즘", "일론머스크"]
    },
    "NHs3DcCD3Fc": {
        "primary_topic": "stock",
        "analysis": {
            "summary": "8주 만에 강한 반등을 보인 코스피 지수의 원동력과 <span class=\"text-cyan-300 font-semibold\">반도체 섹터의 랠리</span> 지속 가능성을 분석함. 외국인 수급 귀환과 HBM 수출 호조가 하반기 국내 증시 상승을 이끌 주역임.",
            "key_claims": ["코스피 반등은 일시적 데드캣 바운스가 아닌 반도체 펀더멘털 회복에 기인함", "SK하이닉스와 삼성전자의 HBM 모멘텀이 하반기까지 유효함"],
            "data_points": ["코스피 8주 만의 반등 시현"],
            "signal": "bullish",
            "signal_reason": "메모리 반도체 턴어라운드와 수출 데이터 호조",
            "key_companies": ["SK하이닉스", "삼성전자"],
            "insight": "한국 증시는 결국 반도체 수출 사이클과 동행하며, 현재는 상승장의 중간 허리 국면에 위치해 있음.",
            "action_point": "국내 증시 내 반도체 소부장(소재·부품·장비) 기업들에 대한 옥석 가리기 및 비중 확대"
        },
        "tags": ["코스피", "반도체랠리", "국내증시", "시황"]
    },
    "RGoHFSELdVA": {
        "primary_topic": "space",
        "analysis": {
            "summary": "중국이 막대한 국가 자본을 투입하여 <span class=\"text-cyan-300 font-semibold\">우주 굴기</span>를 실현하고 미국(NASA)의 패권을 위협하게 된 발전 과정과 핵심 기술력을 분석함.",
            "key_claims": ["중국 우주정거장 톈궁 완공 및 달 탐사 프로젝트의 괄목할 성과", "우주 공간이 미중 패권 경쟁의 새로운 군사·경제적 전장으로 격상됨"],
            "data_points": [],
            "signal": "neutral",
            "signal_reason": "우주 인프라 관련 글로벌 국가 투자 경쟁 심화",
            "key_companies": ["CASC(중국항천과기집단)"],
            "insight": "우주 산업은 민간 상업화(스페이스X) 트렌드와 함께 국가 주도의 안보 인프라 확충 투트랙으로 폭발적 성장이 예상됨.",
            "action_point": "저궤도 위성통신, 발사체 부품 등 국내외 우주항공 방산 섹터 장기 투자 관점 유지"
        },
        "tags": ["중국우주", "우주굴기", "미중패권", "우주산업"]
    },
    "s8ymgSvdwMo": {
        "primary_topic": "stock",
        "analysis": {
            "summary": "미국 증시와 나스닥의 거침없는 상승 랠리를 이끄는 핵심 동력이 무엇인지 진단함. AI 거품 논란에도 불구하고 <span class=\"text-cyan-300 font-semibold\">소프트웨어 및 데이터 인프라 실적</span>이 주가를 정당화하고 있음.",
            "key_claims": ["AI 하드웨어에서 소프트웨어 및 서비스 영역으로 상승세가 확산될 조짐", "금리 불확실성보다 기업 이익 성장률이 주가를 주도함"],
            "data_points": [],
            "signal": "bullish",
            "signal_reason": "빅테크 및 AI 관련 기업들의 이익 전망치 지속 상향",
            "key_companies": ["마이크로소프트", "메타", "엔비디아"],
            "insight": "나스닥의 상승은 유동성 랠리가 아닌 실적 랠리이며, AI 생태계가 실질적 매출을 창출하기 시작했음을 의미함.",
            "action_point": "빅테크 외에 AI를 도입하여 생산성을 혁신하는 B2B 소프트웨어 기업들로 투자 대상 확대"
        },
        "tags": ["미국증시", "나스닥랠리", "AI", "빅테크"]
    },
    "TsIafjH9uHc": {
        "primary_topic": "energy",
        "analysis": {
            "summary": "수천 조 원이 투입되는 글로벌 <span class=\"text-cyan-300 font-semibold\">반도체 메가 팹</span> 구축 경쟁에서 최종 승패는 보조금이 아닌 <span class=\"text-amber-300 font-bold\">막대한 전력과 용수 인프라의 확보</span> 여부에 달려 있음을 분석함.",
            "key_claims": ["첨단 파운드리는 전기 먹는 하마로 꼽힘", "한국 반도체 클러스터의 핵심 리스크는 전력 송배전망 및 용수 공급 지연임"],
            "data_points": ["글로벌 메가팹 투자 규모 4,755조 원 추산"],
            "signal": "bullish",
            "signal_reason": "반도체 팹 확장에 따른 유틸리티(전력기기, 송전망, 수처리) 인프라 기업 수혜 예상",
            "key_companies": ["삼성전자", "SK하이닉스"],
            "insight": "반도체 공급망 전쟁은 결국 에너지 패권 전쟁으로 귀결되며, 국가 전력 인프라가 반도체 경쟁력을 좌우함.",
            "action_point": "전선, 전력 설비, 원자력 및 SMR 관련 밸류체인에 대한 강력한 비중 확대 유지"
        },
        "tags": ["메가팹", "반도체", "전력인프라", "에너지"]
    },
    "vOk4BAW0rak": {
        "primary_topic": "energy",
        "analysis": {
            "summary": "AI 시대의 폭발적 전력 수요를 감당하기 위해 단순히 원전 신설에 의존하는 것을 넘어 재생에너지, SMR, ESS(에너지저장장치) 등 <span class=\"text-cyan-300 font-semibold\">스마트 에너지 믹스</span>가 필수적임을 역설함.",
            "key_claims": ["원전만으로는 리드타임 문제로 당장의 전력 부족을 해결할 수 없음", "다양한 발전원과 송배전망 고도화(그리드) 투자가 동반되어야 함"],
            "data_points": [],
            "signal": "neutral",
            "signal_reason": "특정 발전원에 국한되지 않은 전력 포트폴리오 다변화 필요성 부각",
            "key_companies": [],
            "insight": "AI 데이터센터 발 전력 슈퍼 사이클은 단일 테마(예: 원전)를 넘어 전력망 인프라 전체의 르네상스를 견인함.",
            "action_point": "변압기, 송전선, 스마트그리드, ESS 등 전력망 고도화 관련 종합 인프라 기업 공략"
        },
        "tags": ["전력인프라", "에너지믹스", "AI데이터센터", "원전"]
    },
    "x-qBdbl3th8": {
        "primary_topic": "tech",
        "analysis": {
            "summary": "차세대 메모리인 <span class=\"text-cyan-300 font-semibold\">HBM4</span> 시대에 접어들며 공정 핵심 기술(하이브리드 본딩, 로직 다이 맞춤화 등)이 어떻게 진화하는지 심층 분석함. 메모리와 파운드리의 경계가 허물어지고 있음.",
            "key_claims": ["HBM4부터는 베이스 다이에 로직 공정이 적용되어 TSMC 등 파운드리와의 협력이 필수임", "열 방출 한계를 극복하기 위한 새로운 패키징 기술이 승부처임"],
            "data_points": [],
            "signal": "bullish",
            "signal_reason": "어드밴스드 패키징(Advanced Packaging) 및 후공정 장비 시장의 도약 기대감",
            "key_companies": ["SK하이닉스", "TSMC", "삼성전자", "한미반도체"],
            "insight": "HBM4는 단순한 D램의 진화가 아닌 맞춤형 시스템 반도체 영역으로 진입하는 변곡점이며, 패키징 장비사의 밸류에이션 리레이팅이 지속됨.",
            "action_point": "하이브리드 본딩, TSV, 후공정 검사 장비 관련 국내 핵심 소부장 기업 롱(Long) 포지션"
        },
        "tags": ["HBM4", "패키징", "로직다이", "반도체"]
    },
    "YlE2u8ADWjA": {
        "primary_topic": "robot",
        "analysis": {
            "summary": "테슬라가 새롭게 선보인 <span class=\"text-cyan-300 font-semibold\">완전 자율주행(FSD)</span> 최신 버전이 기존 룰베이스를 넘어선 엔드투엔드(End-to-End) AI 방식을 채택하여 인간과 유사한 상식 밖의 유연한 주행을 선보임.",
            "key_claims": ["엔드투엔드 신경망 기반 FSD V12의 성능 개선이 경이로운 수준임", "로보택시 상용화 시점이 크게 앞당겨질 수 있음"],
            "data_points": [],
            "signal": "bullish",
            "signal_reason": "자율주행 기술 임계점 돌파로 인한 테슬라 소프트웨어 플랫폼 가치 재평가",
            "key_companies": ["테슬라"],
            "insight": "테슬라의 본질은 자동차 제조사가 아니라 세상에서 가장 발전된 현실 세계(Real-world) AI 비전 플랫폼 기업임.",
            "action_point": "테슬라 주가 조정 시 자율주행 모멘텀을 겨냥한 장기 비중 확대 관점 유효"
        },
        "tags": ["테슬라", "자율주행", "FSD", "로보택시"]
    },
    "zqvm3JAr4Ng": {
        "primary_topic": "energy",
        "analysis": {
            "summary": "AI 투자 열풍이라는 10년 만의 기회가 찾아왔으나, 국내 <span class=\"text-amber-300 font-bold\">전력 공급망 부족</span>으로 인해 K-반도체가 제때 공장을 가동하지 못할 심각한 리스크를 지적함.",
            "key_claims": ["신규 반도체 클러스터 송전망 건설 지연이 심각한 수준임", "국가 차원의 전력 인프라 패스트트랙 법안 통과가 시급함"],
            "data_points": [],
            "signal": "bearish",
            "signal_reason": "전력 병목 현상에 따른 국내 반도체 설비 투자 가동 지연 우려",
            "key_companies": ["삼성전자", "SK하이닉스"],
            "insight": "반도체 초격차 경쟁은 결국 인프라 속도전이며, 정치적·규제적 지연이 한국 반도체의 최대 아킬레스건으로 작용 중임.",
            "action_point": "반도체 실적 개선 랠리 속에서도 송전 인프라 지연 이슈 발생 시 리스크 관리 대응 준비"
        },
        "tags": ["K반도체", "전력인프라", "송전망", "에너지"]
    },
    "_0h99Xnsh60": {
        "primary_topic": "space",
        "analysis": {
            "summary": "스페이스X의 팰컨 9 로켓 잔해가 달 뒷면에 충돌한 후 생성된 크레이터를 한국의 첫 달 탐사선 <span class=\"text-cyan-300 font-semibold\">다누리호</span>가 세계에서 가장 먼저 촬영한 과학적 쾌거를 소개함.",
            "key_claims": ["다누리호의 고해상도 카메라(루티) 성능이 글로벌 우주 강국 수준임을 증명함"],
            "data_points": [],
            "signal": "na",
            "signal_reason": "우주 과학 성과 소개",
            "key_companies": ["스페이스X", "한국항공우주연구원"],
            "insight": "대한민국의 우주 인프라 구축 역량과 위성 운영 기술력이 세계적 궤도에 올랐음을 시사함.",
            "action_point": "국내 우주항공청 개청과 맞물린 우주 산업(위성, 발사체) 모멘텀 점검"
        },
        "tags": ["다누리", "스페이스X", "달탐사", "우주산업"]
    },
    "_SY7lVVWyWY": {
        "primary_topic": "tech",
        "analysis": {
            "summary": "미국의 강력한 제재에도 불구하고 레거시 공정과 막대한 정부 보조금을 바탕으로 급성장하는 <span class=\"text-amber-300 font-bold\">중국 반도체(CXMT 등)</span> 산업의 굴기와 재평가 가능성을 심층 분석함.",
            "key_claims": ["중국 창신메모리(CXMT) 등 자국 기업의 점유율 및 수율이 위협적으로 개선됨", "레거시 반도체 생태계에서 중국의 자급자족 전략이 성과를 냄"],
            "data_points": [],
            "signal": "bearish",
            "signal_reason": "레거시 메모리 시장 내 공급 과잉 우려 및 범용 반도체 마진 훼손 압박",
            "key_companies": ["CXMT", "SMIC", "삼성전자", "SK하이닉스"],
            "insight": "AI 반도체 등 최첨단 영역에서는 미국 주도의 동맹이 굳건하나, 가전/자동차용 범용 반도체 시장에서는 중국발 디플레이션 수출 우려가 상존함.",
            "action_point": "국내 반도체 섹터 투자 시 범용 레거시 비중이 큰 기업보다 HBM 등 첨단 공정 비중이 높은 기업으로 압축"
        },
        "tags": ["중국반도체", "CXMT", "미중갈등", "반도체자급"]
    }
}

def analyze_and_move():
    for vid, meta in ANALYSIS_DATA.items():
        pending_path = Path(f"data/pending/{vid}.json")
        if not pending_path.exists():
            continue
            
        with open(pending_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        primary = meta["primary_topic"]
        
        # update data
        data["analysis"] = meta["analysis"]
        data["classification"] = {
            "primary_topic": primary,
            "secondary_topics": [],
            "tags": meta["tags"]
        }
        
        out_dir = Path(f"data/analyzed/{primary}")
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{vid}.json"
        
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        pending_path.unlink()
        print(f"[분석 완료] {vid} -> {primary}")
        
if __name__ == "__main__":
    analyze_and_move()
