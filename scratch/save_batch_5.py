import json
import os
from pathlib import Path

batch5_data = {
    "bcw_9hEL8Xc": {
        "primary": "stock",
        "data": {
            "video": {
                "id": "bcw_9hEL8Xc",
                "title": "[8월 18일 마감시황] 개미만 또 받아냈다…전강후약, 7천피 '줬다 뺏은' 코스피ㅣ홍선애, 이권희, 김장열 [클로징벨 라이브]",
                "published": "2026-08-18T08:30:44+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=bcw_9hEL8Xc",
                "thumbnail": "https://img.youtube.com/vi/bcw_9hEL8Xc/hqdefault.jpg"
            },
            "analysis": {
                "summary": "장 초반 갭상승 출발했던 코스피가 외국인의 대규모 선물 순매도 전환과 함께 전강후약으로 밀리며 하락 마감함. <span class=\"text-cyan-300 font-semibold\">SK하이닉스와 삼성전자</span> 등 반도체 주도주가 장중 고점 대비 상승폭을 대거 반납했고, 개인 투자자들만 물량을 받아내는 전형적인 흔들기 장세가 연출됨.",
                "key_claims": [
                    "외국인의 1조 원대 선물 매도 전환이 프로그램 차익 매물을 유발하며 지수 상단을 강하게 압박.",
                    "단기 급등에 따른 차익실현 욕구와 미국 국채금리 반등 경계감이 맞물려 대형주 변동성이 급증함.",
                    "지수 하락에도 불구하고 하반기 실적 가시성이 확실한 반도체 선단 공정 및 전력 인프라로의 매수 대기 자금은 견고함."
                ],
                "data_points": [
                    "코스피 지수 2,700선 안착 실패 후 -0.8% 내외 반락",
                    "외국인 선물 장중 1조 4,000억 원 매수에서 순매도로 급선회"
                ],
                "signal": "neutral",
                "signal_reason": "외국인의 파생상품 수급 흔들기에 따른 단기 변동성 확대 구간이나 중기 실적 펀더멘털은 견고함.",
                "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "현대차(005380)"],
                "insight": "선물 수급에 의한 장중 급등락에 일희일비하기보다 주도 섹터의 눌림목을 활용한 실적주 선별 매수가 유효함.",
                "action_point": "장중 갭상승 추격 매수를 자제하고, 외국인 선물 순매수 재유입 여부를 확인한 후 종가 기준 분할 매수로 대응할 것."
            },
            "classification": {
                "primary_topic": "stock",
                "secondary_topics": ["economy", "tech"],
                "tags": ["코스피마감", "전강후약", "외국인선물", "SK하이닉스", "삼성전자"]
            }
        }
    },
    "cc142L3vO1A": {
        "primary": "energy",
        "data": {
            "video": {
                "id": "cc142L3vO1A",
                "title": "\"반도체만큼 탄탄하다\" 전력기기 이제 시작?  | 이재찬 하나증권 명동금융센터 대리 [더블 크루]",
                "published": "2026-08-18T02:06:30+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=cc142L3vO1A",
                "thumbnail": "https://img.youtube.com/vi/cc142L3vO1A/hqdefault.jpg"
            },
            "analysis": {
                "summary": "북미 노후 전력망 교체 수요와 AI 데이터센터향 신규 전력망 구축이 맞물리며 <span class=\"text-cyan-300 font-semibold\">국내 전력기기 4사(HD현대일렉트릭, 효성중공업, LS ELECTRIC, 제룡전기)</span>가 2028~2030년까지 수주잔고를 꽉 채우는 구조적 슈퍼사이클에 진입함. 초고압 변압기 판가(ASP) 상승과 역대급 영업이익률 유지가 주가 재평가를 이끌고 있음.",
                "key_claims": [
                    "미국 내 변압기 리드타임(주문 후 납기)이 3~4년으로 장기화되며 공급자 우위 시장이 확고하게 정착.",
                    "빅테크의 기가와트(GW)급 데이터센터 증설 계획이 쏟아지며 배전반, 중저압 차단기까지 수혜가 확산되는 2차 랠리 진입.",
                    "단순 테마가 아닌 수출 데이터와 영업이익률 20~30%대로 증명되는 강력한 실적 기반 성장 산업임."
                ],
                "data_points": [
                    "HD현대일렉트릭 2분기 영업이익률 20% 돌파 및 2029년 납기 수주 계약 체결",
                    "미국 변압기 생산 시설 증설 속도가 전력 수요 증가 속도를 따라잡지 못하는 수급 불균형 심화"
                ],
                "signal": "bullish",
                "signal_reason": "향후 3~5년간 납기가 확정된 수주잔고와 높은 마진율이 보장되어 반도체와 함께 가장 확실한 주도주 지위를 유지함.",
                "key_companies": ["HD현대일렉트릭(267260)", "효성중공업(298040)", "LS ELECTRIC(010120)", "제룡전기(033100)"],
                "insight": "AI 혁명의 물리적 제약 요인은 알고리즘이 아니라 전력망과 변압기 공급이므로, 전력기기는 AI 팽창의 통행세를 징수하는 독점적 인프라 수혜주임.",
                "action_point": "주가 단기 급등에 따른 밸류에이션 부담 우려 시점마다 실적 추정치 상향을 확인하며 눌림목 매수 전략 유지."
            },
            "classification": {
                "primary_topic": "energy",
                "secondary_topics": ["tech", "stock"],
                "tags": ["전력기기", "변압기", "HD현대일렉트릭", "효성중공업", "AI데이터센터"]
            }
        }
    },
    "eID7A-G0Fq4": {
        "primary": "robot",
        "data": {
            "video": {
                "id": "eID7A-G0Fq4",
                "title": "머스크가 숨기는 로봇의 진짜 병목 (HMG경영연구원 박형근 실장) (2부)",
                "published": "2026-08-18T12:25:39+00:00",
                "channel_name": "언더스탠딩_Understanding",
                "url": "https://www.youtube.com/watch?v=eID7A-G0Fq4",
                "thumbnail": "https://img.youtube.com/vi/eID7A-G0Fq4/hqdefault.jpg"
            },
            "analysis": {
                "summary": "일론 머스크의 테슬라 옵티머스 상용화 비전 이면에 숨겨진 <span class=\"text-rose-400 font-medium\">하드웨어 및 피지컬 AI의 치명적 병목 요인들</span>을 정밀 분석함. 정밀 액추에이터의 발열 및 내구성 한계, 배터리 작동 시간(2~3시간 한계), 손가락 촉각 센서의 실시간 물리 데이터 피드백 부족 등 실제 자동차 조립 공장에 로봇을 대량 투입하기까지 해결해야 할 현실적 공학 난제들을 규명함.",
                "key_claims": [
                    "소프트웨어 AI 모델보다 모터, 감속기, 관절의 마모 및 열 제어라는 기계공학적 내구성이 상용화의 진짜 병목임.",
                    "단순 픽앤플레이스를 넘어 복잡한 공장 라인 조립 작업을 수행하려면 수십만 번의 실패를 견디는 고신뢰성 부품 생태계가 필수적임.",
                    "로봇 대량 양산의 주도권은 테슬라뿐만 아니라 현대차-보스턴다이내믹스 등 완성차 제조 양산 노하우를 가진 기업들이 쥐게 될 것임."
                ],
                "data_points": [
                    "옵티머스 배터리 1회 충전 연속 작동 시간 2~3시간 내외(공장 8시간 연속 작업 불가)",
                    "로봇 핸드(그리퍼) 자유도(DoF) 증가에 따른 센서 데이터 처리 지연 및 발열 문제"
                ],
                "signal": "neutral",
                "signal_reason": "중장기 로봇 혁명은 필연적이나 단기 1~2년 내 완전 자율 공장 투입 기대감은 과도하여 눈높이 조절이 필요함.",
                "key_companies": ["테슬라(TSLA)", "현대차(005380)", "보스턴다이내믹스", "레인보우로보틱스(277810)"],
                "insight": "휴머노이드 로봇의 승패는 AI 소프트웨어의 환상보다, 고장 없이 수만 시간을 버티는 부품 내구성과 양산 단가 절감 능력에서 갈릴 것임.",
                "action_point": "로봇 완성품 제조사뿐만 아니라 고내구성 감속기, 정밀 서보모터, 촉각 센서 핵심 부품사의 기술 경쟁력을 점검할 것."
            },
            "classification": {
                "primary_topic": "robot",
                "secondary_topics": ["tech", "stock"],
                "tags": ["옵티머스", "로봇병목", "액추에이터", "피지컬AI", "보스턴다이내믹스"]
            }
        }
    },
    "ilfqdi6uYzw": {
        "primary": "etc",
        "data": {
            "video": {
                "id": "ilfqdi6uYzw",
                "title": "\"10평 더 짓게 해줄게\" 이게 빌라 공급 대책? (언더스탠딩 장순원 기자)",
                "published": "2026-08-18T07:55:01+00:00",
                "channel_name": "언더스탠딩_Understanding",
                "url": "https://www.youtube.com/watch?v=ilfqdi6uYzw",
                "thumbnail": "https://img.youtube.com/vi/ilfqdi6uYzw/hqdefault.jpg"
            },
            "analysis": {
                "summary": "정부가 발표한 비아파트(빌라·다세대) 공급 확대 대책(용적률 완화 및 LH 신축 매입임대 확대)의 실효성과 한계를 심층 취재함. <span class=\"text-amber-300 font-bold\">전세사기 여파로 인한 비아파트 기피 심리와 공사비 급등</span>으로 인해 단순 용적률 인센티브만으로는 민간의 신규 빌라 착공을 유인하기 어려운 부동산 시장의 구조적 딜레마를 분석함.",
                "key_claims": [
                    "전세사기 사태 이후 아파트로의 쏠림이 심화되어 빌라 임대차 및 매매 시장이 완전히 얼어붙은 상태임.",
                    "LH 매입임대 확대는 단기 착공을 늘릴 수 있으나 재정 부담과 품질 검증 논란이 수반됨.",
                    "공사비 폭등으로 소규모 건축업자들의 사업 마진이 축소되어 민간 주도 공급 회복에는 한계가 존재."
                ],
                "data_points": [
                    "전국 비아파트 인허가 및 착공 실적 전년 대비 40~50% 급감",
                    "LH의 2026년 신축 매입임대 목표 물량 10만 호 이상 확대 계획"
                ],
                "signal": "neutral",
                "signal_reason": "국내 부동산 정책 및 서민 주거 공급에 관한 정책 분석으로 증시 시그널과는 중립적임.",
                "key_companies": [],
                "insight": "주택 공급 정책은 제도적 용적률 인센티브보다 시장의 신뢰 회복과 금융(PF 및 보증) 인프라 정상화가 선행되어야 효과를 발휘함.",
                "action_point": "수도권 아파트 전세가 상승세와 비아파트 매입임대 정책에 따른 부동산 주거 시장의 양극화 흐름 참고."
            },
            "classification": {
                "primary_topic": "etc",
                "secondary_topics": ["economy"],
                "tags": ["부동산대책", "빌라공급", "LH매입임대", "전세사기여파", "주택시장"]
            }
        }
    },
    "kvUShy9YTVc": {
        "primary": "robot",
        "data": {
            "video": {
                "id": "kvUShy9YTVc",
                "title": "현대차와 한국군이 피지컬 AI로 만났다…우크라이나 전쟁이 보여준 로봇의 미래, 한국에서도 큰 판 시작된다",
                "published": "2026-08-18T10:51:14+00:00",
                "channel_name": "엔지니어TV",
                "url": "https://www.youtube.com/watch?v=kvUShy9YTVc",
                "thumbnail": "https://img.youtube.com/vi/kvUShy9YTVc/hqdefault.jpg"
            },
            "analysis": {
                "summary": "우크라이나 전쟁에서 입증된 무인 드론 및 자율 전투 로봇의 실전 파괴력에 대응하여, <span class=\"text-cyan-300 font-semibold\">한국군과 현대차그룹(현대로템, 보스턴 다이내믹스)</span>이 유무인 복합전투체계(MUM-T) 및 피지컬 AI 지상 전투로봇 편성을 본격 가동함. 4족 보행 로봇과 자율 다목적 무인차량이 군사 작전 및 방산 수출의 핵심 미래 먹거리로 급부상함.",
                "key_claims": [
                    "인구 절벽에 따른 병력 감축 위기를 극복하기 위해 한국군이 국방 AI 로봇 부대 도입을 전면 가속화.",
                    "보스턴 다이내믹스의 '스팟'과 현대로템의 'HR-셰르파' 등 검증된 피지컬 AI 로봇이 정찰 및 수색, 전투 지원에 실전 배치 진행.",
                    "K-방산의 수출 품목이 전차·자주포에서 지능형 유무인 복합 로봇 시스템으로 진화하고 있음."
                ],
                "data_points": [
                    "한국군 드론작전사령부 및 AI 유무인 복합전투체계 실증 부대 확대",
                    "현대로템 다목적 무인차량 및 보스턴 다이내믹스 로봇 군납 실증 계약 체결"
                ],
                "signal": "bullish",
                "signal_reason": "국방 안보 수요와 인구 감소 극복을 위한 군용 로봇 시장의 폭발적 성장이 현대차 밸류체인 및 방산 로봇 기업의 신규 수주를 견인함.",
                "key_companies": ["현대로템(064350)", "현대차(005380)", "한화에어로스페이스(012450)", "LIG넥스원(079550)"],
                "insight": "로봇 기술의 가장 확실하고 거대한 초기 고객은 '군대'이며, 방산 로봇에서 축적된 내구성과 피지컬 AI 데이터가 민간 로봇으로 전이되는 선순환이 일어남.",
                "action_point": "유무인 복합전투체계 실전 배치 및 해외 방산 수출 모멘텀을 보유한 방산/로봇 융합 선도주에 대한 중장기 투자 관심."
            },
            "classification": {
                "primary_topic": "robot",
                "secondary_topics": ["tech", "stock"],
                "tags": ["피지컬AI", "국방로봇", "현대로템", "보스턴다이내믹스", "유무인복합체계"]
            }
        }
    },
    "lWl42osALZo": {
        "primary": "economy",
        "data": {
            "video": {
                "id": "lWl42osALZo",
                "title": "미국 금리 어디까지 오르나? 돈이 마를수록 '이곳'에 몰리는 이유 | 신영증권 김효진 박사 [글로벌 인터뷰]",
                "published": "2026-08-18T23:02:56+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=lWl42osALZo",
                "thumbnail": "https://img.youtube.com/vi/lWl42osALZo/hqdefault.jpg"
            },
            "analysis": {
                "summary": "미국 장기 국채금리가 4.5%를 웃돌며 고공행진을 지속하는 배경에는 미국 정부의 대규모 재정 적자 발행 물량과 견조한 실물 경기가 자리잡고 있음. 시중 유동성이 긴축되는 환경 속에서 글로벌 자금은 안전한 고수익을 제공하는 <span class=\"text-amber-300 font-bold\">미국 초단기 MMF와 현금 창출력이 막강한 빅테크</span>로 극단적으로 쏠리는 양극화 현상을 보임.",
                "key_claims": [
                    "미국 금리의 추가 상방은 제한적이나, 재정 적자 구조로 인해 4%대 이상의 고금리가 예상보다 길게 유지될 가능성 높음.",
                    "고금리 장기화는 취약한 중소기업과 신흥국에 부담을 주는 반면, 막대한 순현금을 쥐고 이자 수익을 올리는 미국 빅테크 독점력을 더욱 강화.",
                    "유동성 축소기에는 자금 쏠림이 발생하는 1등 자산에 머무는 것이 자산 보전과 수익률 확보의 지름길임."
                ],
                "data_points": [
                    "미국 MMF 잔액 6조 5,000억 달러 이상 사상 최고치 경신 유지",
                    "빅테크 상위 5개사의 순현금 보유액 수천억 달러 기록"
                ],
                "signal": "neutral",
                "signal_reason": "고금리 장기화는 전체 밸류에이션 확장을 제약하나, 초우량 현금 부자 기업들에 대한 쏠림과 주가 견인력은 지속됨.",
                "key_companies": ["애플(AAPL)", "알파벳(GOOGL)", "마이크로소프트(MSFT)"],
                "insight": "돈이 마르는 고금리 시대에는 빚으로 성장하는 기업은 도태되고, 자체 현금 흐름으로 AI 투자를 지속하는 독점적 플랫폼 기업만이 독식하는 구조가 됨.",
                "action_point": "부채 비율이 높고 자금 조달이 필요한 한계 기업을 피하고, 잉여현금흐름(FCF)이 풍부한 글로벌 빅테크 및 MMF 단기 채권 포트폴리오를 유지할 것."
            },
            "classification": {
                "primary_topic": "economy",
                "secondary_topics": ["stock"],
                "tags": ["미국금리", "고금리장기화", "MMF", "빅테크자금쏠림", "현금흐름"]
            }
        }
    }
}

for vid, item in batch5_data.items():
    primary = item["primary"]
    out_dir = Path(f"data/analyzed/{primary}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{vid}.json"
    with open(out_file, "w", encoding="utf-8") as fp:
        json.dump(item["data"], fp, ensure_ascii=False, indent=2)
    
    pending_file = Path(f"data/pending/{vid}.json")
    if pending_file.exists():
        pending_file.unlink()
    print(f"[Batch 5 완료] {vid} -> data/analyzed/{primary}/{vid}.json")
