import json
import os
from pathlib import Path

analyses = [
    {
        "video": {
            "id": "0N4PGfhGkV4",
            "title": "미국은 고금리로 난리났는데, 중국 AI는 2% 금리에 빌린다 (언더스탠딩 김상훈 기자)",
            "published": "2026-08-19T07:55:34+00:00",
            "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=0N4PGfhGkV4",
            "thumbnail": "https://img.youtube.com/vi/0N4PGfhGkV4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미국은 30년물 국채 금리가 5.3%대로 치솟으며 AI 데이터센터 투자 비용 및 하이퍼스케일러들의 부채 부담이 가중되는 반면, 중국은 부동산 부양을 억제하고 국채 및 대출 금리를 2%대로 낮게 설계하여 AI 기업에 막대한 실질 금융 보조금 혜택을 제공하고 있습니다.\n동일하게 4,000조 원을 투자할 때 연간 이자 비용은 중국 122조 원, 한국 170조 원, 미국 270조 원으로 중국이 압도적인 금융 원가 경쟁력을 확보했습니다.\n중국의 저금리 설계 전략은 디플레이션 환경을 전략적으로 용인하며 글로벌 AI 패권 경쟁에서 자국 테크 기업의 인프라 구축 비용을 파격적으로 낮추는 지렛대로 작동하고 있습니다.",
            "key_claims": [
                "미국 재무부는 AI 붐을 지탱하기 위해 장기 국채 발행 축소와 바이백 등 금리 방어에 총력을 기울이고 있음.",
                "중국은 부동산 부양을 차단하고 예금/대출 금리를 설계 통제하여 AI/반도체 등 국가 전략 산업에 2%대 초저금리 자금을 몰아주고 있음.",
                "AI 인프라 투자 규모가 수천조 원에 달하는 상황에서 저금리 조달 비용은 사실상 강력한 정부 보조금 역할을 수행함."
            ],
            "data_points": [
                "미국 30년물 국채 금리: 5.32% 기록 (19년 만의 최고치)",
                "동일 4,000조 원 투자 시 연간 이자비용 비교: 중국 122조 원 vs 한국 170조 원 vs 미국 270조 원",
                "주요국 10년물 국채 금리: 미국 4.47%, 한국 4.18%, 독일 2.97%, 일본 2.67%, 중국 2%대 초반 지속 하락"
            ],
            "signal": "neutral",
            "signal_reason": "미국의 고금리 부담이 AI CapEx의 단기 조정 요인으로 작용할 수 있으나, 중국의 저금리 공세에 맞선 미국의 정책적 대응(바이백 및 국채 관리)이 본격화되는 정책 전환기이기 때문임.",
            "key_companies": [
                "알파벳(GOOGL)",
                "오픈AI",
                "알리바바(BABA)",
                "텐센트",
                "엔비디아(NVDA)"
            ],
            "insight": "AI 패권 전쟁의 본질이 알고리즘에서 <span class=\"text-emerald-400 font-medium\">자본 조달 비용(금리)</span>과 <span class=\"text-cyan-300 font-semibold\">전력 인프라</span>의 싸움으로 전이되었으며, 미국의 금리 인하 지연 시 빅테크의 FCF(잉여현금흐름) 방어 능력이 주가 차별화의 핵심 잣대가 될 것입니다.",
            "action_point": "차입 의존도가 높은 후발 AI 기업에 대한 투자는 경계하고, 강력한 현금 창출력을 바탕으로 고금리를 자체 방어할 수 있는 빅테크 중심의 압축 포트폴리오를 유지해야 합니다."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["tech", "stock"],
            "tags": ["중국금리설계", "AI보조금", "장기국채금리", "데이터센터비용", "김상훈기자"]
        }
    },
    {
        "video": {
            "id": "4ZDjjLjfAE4",
            "title": "미국 주식 계속 사도 될까요?｜The Economistㅣ2026.8.20(목)",
            "published": "2026-08-19T23:24:49+00:00",
            "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=4ZDjjLjfAE4",
            "thumbnail": "https://img.youtube.com/vi/4ZDjjLjfAE4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "한국은행의 기준금리 인상(2.75%)과 달리 미국 연준은 코어 인플레이션 안정으로 추가 금리 인상 가능성이 매우 낮으며, 외환시장은 채권 금리차보다 반도체 수출 및 주식 수급이 환율을 주도하고 있습니다.\n최근 제기된 AI 피크아웃 논란은 역사적으로 늘 존재했던 일시적 변동성일 뿐이며, 주식 시장의 핵심 선행 지표인 <span class=\"text-emerald-400 font-medium\">미국 기업 이익 마진(Profit Margin)</span>은 여전히 사상 최고 수준을 견고하게 유지 중입니다.\n국내 증시의 극심한 변동성에 흔들리기보다 이익 성장 추세가 명확한 미국 주식 중심의 글로벌 분산 투자가 유효합니다.",
            "key_claims": [
                "주식 시장의 가장 신뢰할 수 있는 선행 지표는 '미국 기업들의 이익 마진'이며 현재 전혀 꺾이지 않고 있음.",
                "AI 피크아웃 우려로 인한 주가 조정은 추세 반전이 아닌 상승장 내의 건전한 변동성 소화 과정임.",
                "환율은 채권 금리차보다 반도체 중심의 경상수지 흑자와 외국인 주식 매매 흐름에 의해 결정됨."
            ],
            "data_points": [
                "한국은행 기준금리: 2.5%에서 2.75%로 25bp 인상 완료",
                "달러-원 환율: 상반기 1,505원 고점 후 외국인 매도 진정으로 1,400원대 초중반 등락 중",
                "미국 기업 이익 마진: 1987년 블랙먼데이, 2001년 IT버블, 2008년 금융위기 때와 달리 견고한 우상향 유지"
            ],
            "signal": "bullish",
            "signal_reason": "핵심 선행 지표인 미국 기업 이익 마진이 견고하고 글로벌 빅테크들의 AI 설비 투자가 확고하여 중장기 상승 추세가 훼손되지 않았기 때문임.",
            "key_companies": [
                "엔비디아(NVDA)",
                "마이크로소프트(MSFT)",
                "애플(AAPL)",
                "삼성전자(005930)",
                "SK하이닉스(000660)"
            ],
            "insight": "주가의 단기 흔들림보다 기업 펀더멘털의 본질인 이익 마진을 추종해야 하며, 경기 침체 신호가 없는 한 AI 사이클의 구조적 성장은 지속될 것입니다.",
            "action_point": "코스피의 단기 반등을 활용해 포트폴리오의 비중을 일부 리밸런싱하고, 펀더멘털이 강력한 미국 우량 기술주 및 빅테크 중심 비중을 확대 유지할 것을 권장합니다."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy", "tech"],
            "tags": ["이익마진", "선행지표", "미국주식", "AI피크아웃", "박희찬"]
        }
    },
    {
        "video": {
            "id": "503NEYQ6xXo",
            "title": "미국 국채 금리, 펀더멘탈로 보면 지금 오를 이유가 없습니다. 그런데도 올라간 원인은 따로 있었습니다",
            "published": "2026-08-19T07:45:18+00:00",
            "channel_name": "이효석아카데미",
            "url": "https://www.youtube.com/watch?v=503NEYQ6xXo",
            "thumbnail": "https://img.youtube.com/vi/503NEYQ6xXo/hqdefault.jpg"
        },
        "analysis": {
            "summary": "최근 미국 국채 금리가 급등하며 주식 시장을 흔들고 있지만, 이는 경제 펀더멘털의 개선이 아닌 채권 시장의 <span class=\"text-rose-400 font-medium\">수급 불균형(공급 과잉 및 유동성 왜곡)</span> 때문입니다.\n주식 시장 투자자들은 채권 금리가 이미 폭등한 뒤 뒤늦게 패닉에 빠지는 '뒷북 반응'을 보이는 경향이 짙습니다.\n미국 정부의 신인도와 크레딧에 문제가 없는 한 수급발 금리 왜곡은 점차 해소될 것이며, 금리 공포로 인한 과도한 주식 매도는 경계해야 합니다.",
            "key_claims": [
                "경제 지표가 둔화되는 국면에서 금리가 튀어오르는 것은 펀더멘털이 아닌 채권 수급 꼬임 현상임.",
                "주식 시장에서 금리 급등을 이유로 호들갑을 떨 때는 이미 채권 시장에서 선반영된 이후의 '뒷북'일 확률이 매우 높음.",
                "채권 가격의 본질은 발행 주체(미국 정부)에 대한 '신뢰와 크레딧'이며 장기적 펀더멘털 수렴이 일어날 것임."
            ],
            "data_points": [
                "채권 금리와 주가 관계: 채권 시장의 패닉이 주식 시장으로 전이되는 시차 존재",
                "국채 펀더멘탈 결정 요소: 만기, 표면금리(쿠폰), 발행국가의 크레딧(신용도)"
            ],
            "signal": "neutral",
            "signal_reason": "단기 수급 요인으로 인한 금리 변동성이 주식 시장의 밸류에이션 부담을 자극하고 있으나, 펀더멘털 훼손이 아니므로 과도한 비관론은 지양해야 하기 때문임.",
            "key_companies": [
                "미국 재무부",
                "연방준비제도(Fed)"
            ],
            "insight": "시장의 노이즈가 '펀더멘탈 요인'인지 '일시적 수급 요인'인지 분별하는 안목이 필수적이며, 수급 요인에 의한 주가 급락은 오히려 우량 자산의 분할 매수 기회가 됩니다.",
            "action_point": "금리 상승 뉴스에 휘둘려 패닉 셀을 하기보다 수급 왜곡이 정상화되는 구간을 기다리며 실적 호전주를 분할 매수하는 전략이 유리합니다."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["미국국채", "채권수급", "금리급등원인", "이효석", "채권펀더멘탈"]
        }
    },
    {
        "video": {
            "id": "9BKjJN7Giog",
            "title": "유니트리 시총 93조원이 보여준 휴머노이드의 미래, 현대차 보스턴다이내믹스 기업가치는 얼마가 될까?",
            "published": "2026-08-19T10:32:36+00:00",
            "channel_name": "엔지니어TV",
            "url": "https://www.youtube.com/watch?v=9BKjJN7Giog",
            "thumbnail": "https://img.youtube.com/vi/9BKjJN7Giog/hqdefault.jpg"
        },
        "analysis": {
            "summary": "중국 대표 휴머노이드 로봇 기업 유니트리(Unitree)가 상장 첫날 주가 1,100위안을 돌파하며 <span class=\"text-cyan-300 font-semibold\">시가총액 92.5조~93조 원</span>을 기록하는 기염을 토했습니다.\n현재 매출 규모 대비 기록적인 밸류에이션은 중국 자본이 휴머노이드 하드웨어 시장 선점과 대량 양산 능력에 부여한 막대한 프리미엄을 방증합니다.\n유니트리의 93조 원 밸류는 향후 현대차그룹 산하 보스턴 다이내믹스(Boston Dynamics)의 IPO 기업 가치와 피지컬 AI 로봇 산업 전반의 평가 기준을 대폭 상향시키는 계기가 될 것입니다.",
            "key_claims": [
                "유니트리의 93조 원 시총은 휴머노이드 산업이 단순 연구개발 단계를 넘어 조 단위 양산 산업으로 시장 평가를 받기 시작했음을 증명함.",
                "중국 로봇 생태계의 급격한 밸류에이션 팽창은 글로벌 피지컬 AI 및 휴머노이드 기업들의 리레이팅을 촉발함.",
                "현대차가 보유한 보스턴 다이내믹스의 실물 로봇 기술력과 제조 인프라의 기업 가치 재평가가 임박함."
            ],
            "data_points": [
                "유니트리 상장 첫날 주가: 1,100위안 도달",
                "유니트리 총 주식수 및 시가총액: 약 4억 주, 환율 208원 적용 시 시총 92조 5,000억 원 달성",
                "비교 대상 기업: 현대자동차 산하 보스턴 다이내믹스, 테슬라 옵티머스"
            ],
            "signal": "bullish",
            "signal_reason": "휴머노이드 대장주의 상장 성공과 폭발적인 시가총액 형성은 로보틱스 및 피지컬 AI 밸류체인 전반에 강력한 투자 모멘텀을 공급하기 때문임.",
            "key_companies": [
                "유니트리(Unitree)",
                "현대자동차(005380)",
                "보스턴다이내믹스",
                "테슬라(TSLA)",
                "두산로보틱스(454910)",
                "레인보우로보틱스(277810)"
            ],
            "insight": "자율주행 다음의 메가 트렌드는 <span class=\"text-cyan-300 font-semibold\">피지컬 AI(휴머노이드)</span>이며, 양산 공급망과 부품 단가 절감 능력을 갖춘 한·중·미 대표 로봇 기업들의 밸류에이션 재평가가 본격화되고 있습니다.",
            "action_point": "보스턴 다이내믹스 상장 모멘텀을 가진 현대차 그룹주 및 국내 핵심 로봇 구동기/액추에이터/감속기 밸류체인에 대한 중장기 관심이 필요합니다."
        },
        "classification": {
            "primary_topic": "robot",
            "secondary_topics": ["tech", "stock"],
            "tags": ["유니트리", "휴머노이드", "보스턴다이내믹스", "현대차", "시총93조"]
        }
    },
    {
        "video": {
            "id": "aQ0z5VcNEvU",
            "title": "전기장으로 인공강우를 발생시킨다?",
            "published": "2026-08-19T02:00:07+00:00",
            "channel_name": "안될과학 Unrealscience",
            "url": "https://www.youtube.com/watch?v=aQ0z5VcNEvU",
            "thumbnail": "https://img.youtube.com/vi/aQ0z5VcNEvU/hqdefault.jpg"
        },
        "analysis": {
            "summary": "얼음 결정에 전기장을 인가하면 결정들이 특정 방향으로 정렬되고 서로 끌어당겨 사슬처럼 이어지는 물리적 특성을 활용한 인공강우 연구가 활발히 진행 중입니다.\n과거 실험실 수준의 강한 전기장 한계를 극복하고 실제 대기 구름에 적용할 수 있는 새로운 방식의 기상 조절 기술이 개발되고 있습니다.\n제주 서귀포 구름물리연구소 등 국내 연구진이 참여하는 기상 조절 및 기후 테크 기술의 실전 적용 가능성이 주목받고 있습니다.",
            "key_claims": [
                "전기장을 이용해 구름 속 물방울과 얼음 입자의 결합을 유도하여 비를 내리게 하는 혁신적 기상 조절 기술 개발 중.",
                "과거 화학물질(요오드화은) 살포 방식 대비 환경 오염이 적고 효율적인 차세대 인공강우 솔루션으로 부상."
            ],
            "data_points": [
                "연구 기관: 제주 서귀포 구름물리연구소 및 국내외 기상물리 연구팀",
                "핵심 원리: 전기장에 의한 빙정 정렬 및 응결 촉진 메커니즘"
            ],
            "signal": "na",
            "signal_reason": "순수 기초과학 및 기후 테크 응용 연구 소개 영상으로 금융 투자 시그널 판단 대상이 아님.",
            "key_companies": [],
            "insight": "기후 변화에 대응하기 위한 기후 테크(Climate Tech)가 기초 물리 현상 제어 기술과 결합하여 실용화 단계로 진화하고 있습니다.",
            "action_point": "가뭄 해소 및 기상 조절 관련 국책 연구 과제와 차세대 기후 엔지니어링 기술 동향을 지식 차원에서 지속 모니터링할 것."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["etc"],
            "tags": ["인공강우", "전기장", "구름물리", "안될과학", "기후테크"]
        }
    },
    {
        "video": {
            "id": "CH1FrANSxgU",
            "title": "세계의 공장 다시 노리는 중국, 인건비 0원 시대 온다 (딥엑스 김녹원 대표)",
            "published": "2026-08-19T12:25:14+00:00",
            "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=CH1FrANSxgU",
            "thumbnail": "https://img.youtube.com/vi/CH1FrANSxgU/hqdefault.jpg"
        },
        "analysis": {
            "summary": "중국은 전 세계에서 가장 방대한 제조 공장 인프라와 실물 제조 데이터를 바탕으로 피지컬 AI와 휴머노이드 로봇을 결합해 <span class=\"text-rose-400 font-medium\">'인건비 0원 무인 공장'</span> 시대를 열어가고 있습니다.\n피지컬 AI의 핵심 경쟁력은 알고리즘뿐만 아니라 엣지에서 초저전력으로 구동되는 온디바이스 AI 반도체(NPU)와 실물 환경에서의 데이터 축적입니다.\n한국 제조업과 팹리스 산업이 중국의 제조 패권 장악에 맞서려면 독자적인 온디바이스 AI 반도체와 로보틱스 솔루션을 통한 제조 자주권 확보가 시급합니다.",
            "key_claims": [
                "중국은 전 세계 공장 데이터를 독점하고 있어 피지컬 AI 영역에서 미국보다 실질적인 제조 현장 데이터 우위를 점하고 있음.",
                "휴머노이드와 스마트 팩토리가 결합된 '인건비 제로' 공장이 완성될 경우 글로벌 제조업 공급망에 대한 중국의 헤게모니가 더욱 강력해짐.",
                "엣지 디바이스와 로봇에 탑재될 초저전력·고효율 온디바이스 NPU가 피지컬 AI 하드웨어 혁신의 열쇠임."
            ],
            "data_points": [
                "딥엑스(DEEPX) 온디바이스 AI 반도체: 로보틱스 및 스마트 팩토리용 고효율 NPU 양산 및 글로벌 공급 추진",
                "글로벌 제조업 공장 데이터 비중: 중국이 전 세계 제조 설비의 압도적 비중 차지"
            ],
            "signal": "bullish",
            "signal_reason": "피지컬 AI 및 온디바이스 AI 반도체의 폭발적 수요 성장이 확인되며, 엣지 AI NPU를 개발하는 반도체 및 하드웨어 밸류체인의 성장 가시성이 매우 높기 때문임.",
            "key_companies": [
                "딥엑스(DEEPX)",
                "테슬라(TSLA)",
                "엔비디아(NVDA)",
                "삼성전자(005930)",
                "SK하이닉스(000660)",
                "유니트리"
            ],
            "insight": "거대언어모델(LLM)에 머물던 AI 혁명이 실제 물리적 공장과 로봇을 움직이는 <span class=\"text-cyan-300 font-semibold\">피지컬 AI(Physical AI)</span>로 확장되고 있으며, 이를 구동하는 저전력 AI 반도체 기업들의 전략적 가치가 급등하고 있습니다.",
            "action_point": "데이터센터 중심 반도체에서 엣지 온디바이스 AI 및 로보틱스용 NPU/액추에이터 관련 기술 기업으로 관심 범위를 확장하고 국내 AI 반도체 생태계의 상장 수혜주를 추적해야 합니다."
        },
        "classification": {
            "primary_topic": "robot",
            "secondary_topics": ["tech", "stock"],
            "tags": ["피지컬AI", "딥엑스", "김녹원", "인건비0원", "스마트팩토리", "온디바이스AI"]
        }
    },
    {
        "video": {
            "id": "dHP6_zOmBFk",
            "title": "\"재무제표는 어려워서 못 봐요\"...개별주식 사기 전에 단어 9개면 끝납니다 | 왕초보 탈출 4탄",
            "published": "2026-08-19T10:00:01+00:00",
            "channel_name": "이효석아카데미",
            "url": "https://www.youtube.com/watch?v=dHP6_zOmBFk",
            "thumbnail": "https://img.youtube.com/vi/dHP6_zOmBFk/hqdefault.jpg"
        },
        "analysis": {
            "summary": "개별 주식 투자 전 복잡한 재무제표 대신 기업의 실체를 파악할 수 있는 <span class=\"text-emerald-400 font-medium\">9가지 핵심 단어</span>(매출액, 영업이익, 당기순이익, 영업이익률, PER, PBR, ROE, 잉여현금흐름, 부채비율)의 원리와 실전 활용법을 소개합니다.\n장부상 이익과 실제 통장에 꽂히는 현금의 차이를 나타내는 '잉여현금흐름(FCF)'의 중요성과 과도한 부채 위험을 방어하는 재무 건전성 판단 기준을 제시합니다.\n주식 투자에서 손실을 방지하려면 기업이 실제로 돈을 벌고 있는지와 밸류에이션이 적정한지 9개 지표로 사전 검증해야 합니다.",
            "key_claims": [
                "재무제표의 모든 숫자를 다 볼 필요 없이 핵심 9개 단어만 이해해도 부실 기업을 완벽히 걸러낼 수 있음.",
                "단순 당기순이익보다 회사가 실제로 투자 후 손에 쥐는 잉여현금흐름(FCF)이 기업 가치의 본질임.",
                "PER과 PBR, ROE를 종합적으로 분석해야 고평가 거품 주식을 피하고 저평가 우량주를 발굴할 수 있음."
            ],
            "data_points": [
                "핵심 9개 단어: 매출액, 영업이익, 당기순이익, 영업이익률, PER, PBR, ROE, 잉여현금흐름(FCF), 부채비율"
            ],
            "signal": "na",
            "signal_reason": "초보 투자자를 위한 재무제표 기초 교육 및 밸류에이션 분석 가이드 영상으로 단기 투자 시그널에 해당하지 않음.",
            "key_companies": [],
            "insight": "화려한 테마와 스토리 뒤에 숨겨진 기업의 '현금 창출 능력'과 '부채 건전성'을 스스로 검증하는 기본기가 변동성 장세에서 계좌를 지키는 가장 강력한 무기입니다.",
            "action_point": "보유 중인 종목들의 최근 분기 FCF(잉여현금흐름) 흑자 여부와 부채비율을 재검토하여 펀더멘털이 부실한 테마주는 비중을 축소할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["etc"],
            "tags": ["재무제표기초", "이효석", "주식초보", "잉여현금흐름", "PER_PBR"]
        }
    }
]

def save_batch(batch_list):
    for item in batch_list:
        vid = item["video"]["id"]
        primary = item["classification"]["primary_topic"]
        target_dir = Path(f"data/analyzed/{primary}")
        target_dir.mkdir(parents=True, exist_ok=True)
        
        target_file = target_dir / f"{vid}.json"
        with open(target_file, "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
        print(f"Saved: {target_file}")
        
        # Remove from pending if exists
        pending_file = Path(f"data/pending/{vid}.json")
        if pending_file.exists():
            pending_file.unlink()
            print(f"Deleted pending: {pending_file}")

save_batch(analyses)
print("Batch 1 completed!")
