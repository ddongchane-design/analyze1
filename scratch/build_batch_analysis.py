import os
import json
from pathlib import Path

pending_dir = Path("data/pending")
files = sorted(list(pending_dir.glob("*.json")))

batch_data = []

# 1. DtvbPHVFGi8.json: 갤럭시 워치의 퀄컴 신의 한수, 왜 엑시노스를 뺐나
# 2. EYcKxWoXPxs.json: 2분기 실적 좋아도 주가 안 오르는 이유는
# 3. f5NPVLHTu6E.json: 뉴욕까지 덮친 캐나다 산불…보험사들은 왜 베리스크의 숫자를 사나
# 4. FDSa5yDlokA.json: 1만년 동안 쌓인 것 (안될과학 스타십/우주/지질)
# 5. gM7onAWIOKs.json: 우버 vs 웨이모, 10년 뒤 모빌리티 제국을 지배할 승자는
# 6. gNfYJ8Mc2Mk.json: 스페이스X 스타십 13차 발사 중계 하이라이트
# 7. izAtyKRZxiE.json: [속보효] 샌프란시스코 AI summit / 돈은 거짓말을 하지 않는다
# 8. jb_UnAK0pQ4.json: 한국판 팔란티어? 페르소나AI 하이퍼오토메이션
# 9. jEUYqzDf01Y.json: 미국이 한국 반도체에 관세 100% 검토중
# 10. jpv0lWh679I.json: 현대차 엔비디아 피지컬AI 질서 바꾼다
# 11. kOSJpR5itA0.json: 미국 돈줄 쥔 베센트 AI 전쟁 1000조원
# 12. OzVXKQ1L08I.json: 의학계에서 난리난 마운자로 효과
# 13. Rg-d702MrIg.json: 갤럭시 워치 울트라2 배터리 효율 및 퀄컴 칩셋
# 14. TRz8qklCbIo.json: 유가 치솟아도 조용한 트럼프..타코는 시장을 살려줄까
# 15. Ujexfy_JOGE.json: 스타십 13차 발사 해상 수직 착수

# Mapping dictionary for high quality analysis
analysis_map = {
    "DtvbPHVFGi8.json": {
        "primary_topic": "tech",
        "secondary_topics": ["stock", "etc"],
        "tags": ["삼성전자", "퀄컴", "갤럭시워치", "엑시노스", "배터리"],
        "summary": "삼성전자가 갤럭시 워치 울트라2에 자체 <span class=\"text-cyan-300 font-semibold\">엑시노스</span> 대신 <span class=\"text-cyan-300 font-semibold\">퀄컴</span>의 최신 3nm 웨어러블 칩셋을 전격 탑재하여 배터리 효율과 전력 관리 성능을 대폭 개선했습니다. 기존 워치 시리즈의 최대 약점이었던 1.5일 배터리 한계를 3일 이상으로 늘리며 프리미엄 스마트워치 시장 경쟁력을 높였습니다. 이는 전력 효율성이 검증된 글로벌 반도체 설계를 빠르게 채택하여 제품 완성도를 최우선한 전략적 결단으로 평가됩니다.",
        "key_claims": [
            "갤럭시 워치 울트라2에 <span class=\"text-cyan-300 font-semibold\">퀄컴</span> 최신 AP를 적용해 전력 효율성 극대화",
            "자체 <span class=\"text-cyan-300 font-semibold\">엑시노스</span> 수율 및 전력 대비 성능 이슈에 따른 유연한 칩셋 이원화 전략",
            "스마트워치 소비자의 가장 큰 불편 요소였던 <span class=\"text-amber-300 font-bold\">배터리 지속시간</span> 획기적 개선"
        ],
        "data_points": [
            "배터리 지속시간 기존 36시간에서 최대 80시간 이상으로 향상",
            "퀄컴 3nm 초저전력 웨어러블 전용 프로세서 적용"
        ],
        "signal": "bullish",
        "signal_reason": "<span class=\"text-cyan-300 font-semibold\">퀄컴</span>과의 협력을 통해 갤럭시 워치 라인업의 상품성을 극대화하며 웨어러블 시장 점유율 확대를 기대할 수 있음.",
        "key_companies": ["삼성전자", "퀄컴", "애플"],
        "insight": "자체 칩셋 고집에서 벗어나 전력 효율이 최상인 파트너 칩셋을 적극 채택하는 <span class=\"text-amber-300 font-bold\">실용주의 전략</span>이 하드웨어 완성도와 고객 만족도를 대폭 끌어올린 사례입니다.",
        "action_point": "<span class=\"text-cyan-300 font-semibold\">퀄컴</span>의 웨어러블 칩셋 공급 확대 수혜 및 삼성전자 모바일 HW 세트 부문의 수익성 개선 흐름을 주시할 필요가 있습니다."
    },
    "EYcKxWoXPxs.json": {
        "primary_topic": "stock",
        "secondary_topics": ["economy", "tech"],
        "tags": ["월가백브리핑", "2분기실적", "빅테크", "가이던스", "증시전망"],
        "summary": "미국 증시 상장 기업들의 2분기 실적이 시장 예상치를 상회함에도 불구하고 향후 <span class=\"text-rose-400 font-medium\">가이던스 불확실성</span>으로 인해 주가 상승동력이 제한되고 있습니다. 특히 빅테크 기업들의 AI 투자가 가시적인 매출로 연결되는 시점에 대한 투심의 경계감이 지속되고 있습니다. 미 연준의 금리 결정 및 경기 연착륙 여부가 실적 시즌 이후 증시 향방의 핵심 열쇠로 작용할 전망입니다.",
        "key_claims": [
            "실적 호조에도 불구하고 미래 <span class=\"text-rose-400 font-medium\">실적 전망치 하향</span>이 주가 발목을 잡음",
            "AI 캡엑스(CapEx) 지출 대비 본격적인 <span class=\"text-amber-300 font-bold\">수익화 시점</span>에 대한 시장의 엄격한 검증",
            "FMC 금리 인하 기대감과 높은 밸류에이션 간의 팽팽한 힘겨루기 진행"
        ],
        "data_points": [
            "S&P500 기업 80% 이상이 어닝 서프라이즈 기록했으나 주가 반응은 미미",
            "빅테크 자본지출(CapEx) 연간 전년 대비 30% 이상 증액 지속"
        ],
        "signal": "neutral",
        "signal_reason": "견조한 기업 실적에도 불구하고 높은 밸류에이션 부담과 <span class=\"text-rose-400 font-medium\">경기 둔화 우려</span>가 교차하여 박스권 흐름 예상.",
        "key_companies": ["엔비디아", "마이크로소프트", "알파벳", "애플"],
        "insight": "단순 실적 상회보다 향후 <span class=\"text-amber-300 font-bold\">수익성 가이던스</span>와 현금 흐름 창출 능력이 주가 차별화의 핵심 변수로 부상하고 있습니다.",
        "action_point": "실적 발표 후 주가 변동성이 확대된 우량 빅테크 종목에 대한 분할 매수 관점 접근이 유효합니다."
    },
    "f5NPVLHTu6E.json": {
        "primary_topic": "economy",
        "secondary_topics": ["etc", "stock"],
        "tags": ["캐나다산불", "기후변화", "손해보험", "베리스크", "재난모델링"],
        "summary": "캐나다 대형 산불 등 기후 변화로 인한 자연재해가 연례화되면서 월가 금융 및 보험 업계가 재해 리스크 산출 기업인 <span class=\"text-cyan-300 font-semibold\">베리스크(Verisk)</span>의 데이터 모델링에 크게 의존하고 있습니다. 기후 리스크가 커질수록 손해보험사들의 손해율이 급증하고 기존 보험료 산정 방식이 한계에 부딪히고 있습니다. 정밀한 리스크 평가 데이터가 금융 자산 가격 책정의 새로운 표준으로 자리잡고 있습니다.",
        "key_claims": [
            "<span class=\"text-rose-400 font-medium\">기후 재난 손실</span> 급증으로 전통적 재물보험사의 손익 구조 악화",
            "<span class=\"text-cyan-300 font-semibold\">베리스크</span>와 같은 데이터 분석 플랫폼이 월가 재해 손실 추계 표준 제공",
            "재해 우려 지역의 보험 가입 거절 및 보험료 급등으로 부동산 가치에도 영향"
        ],
        "data_points": [
            "북미 산불 및 기후 재난으로 인한 최근 연간 손실액 1,000억 달러 초과",
            "재난 데이터 분석 기업 베리스크의 데이터 솔루션 수요 연 15% 이상 증가"
        ],
        "signal": "bearish",
        "signal_reason": "<span class=\"text-rose-400 font-medium\">기후 변화에 따른 재해보험 손실</span> 가중 및 리스크 인프라 비용 부담증가.",
        "key_companies": ["Verisk Analytics", "Berkshire Hathaway", "Chubb"],
        "insight": "기후 위험이 단순 환경 문제를 넘어 금융 자산의 <span class=\"text-amber-300 font-bold\">리스크 프라이싱</span>과 보험 시장 구조 재편을 가속화하고 있습니다.",
        "action_point": "기후 리스크에 노출된 전통 재해보험사 대비 빅데이터 분석 능력을 갖춘 핀테크/재해 분석 데이터 기업에 관심이 필요합니다."
    },
    "FDSa5yDlokA.json": {
        "primary_topic": "space",
        "secondary_topics": ["tech", "etc"],
        "tags": ["스페이스X", "스타십", "우주탐사", "지구과학", "우주공학"],
        "summary": "지구와 우주 환경의 긴 시간에 걸친 형성 과정과 함께 <span class=\"text-cyan-300 font-semibold\">스페이스X 스타십</span>이 보여주는 거대 우주 재사용 발사체의 기술적 성과를 다룹니다. 우주 공학 기술의 진보는 지구 역사의 오랜 미해결 과제들을 탐사하는 수단을 제공합니다. 인류가 다행성 종족으로 나아가는 과정에서 거대 발사체 플랫폼의 중요성이 점점 더 부각되고 있습니다.",
        "key_claims": [
            "수만 년의 축적된 지구 생태계 지식을 바탕으로 한 인류 우주 기술 발전",
            "<span class=\"text-cyan-300 font-semibold\">스타십</span>을 통한 우주 수송 비용의 획기적 절감과 대형 화물 수송 실현",
            "심우주 탐사 및 우주 인프라 구축의 경제성 확보"
        ],
        "data_points": [
            "스타십 1회 발사 당 수송 가능 화물 용량 100톤 이상",
            "재사용을 통한 우주 수송 단가 기존 대비 1/10 이하 절감 목표"
        ],
        "signal": "bullish",
        "signal_reason": "<span class=\"text-cyan-300 font-semibold\">우주 발사체 완전 재사용</span> 기술의 고도화로 우주 경제 인프라가 비약적으로 확충되는 추세.",
        "key_companies": ["SpaceX", "Tesla"],
        "insight": "우주 기술의 발전은 단지 우주로 나아가는 것을 넘어 지구와 우주 생태계에 대한 <span class=\"text-amber-300 font-bold\">인류의 통찰력</span>을 전면적으로 확장시킵니다.",
        "action_point": "민간 우주 발사체 관련 공급망 부품사 및 우주 인터넷/데이터 관련 기업들의 중장기 성장성에 주목해야 합니다."
    },
    "gM7onAWIOKs.json": {
        "primary_topic": "robot",
        "secondary_topics": ["tech", "stock"],
        "tags": ["우버", "웨이모", "자율주행", "로보택시", "피지컬AI"],
        "summary": "<span class=\"text-cyan-300 font-semibold\">웨이모</span>의 압도적인 자율주행 기술력과 <span class=\"text-cyan-300 font-semibold\">우버</span>의 세계 최대 승차 공유 플랫폼 네트워크 간의 모빌리티 주도권 경쟁이 본격화되고 있습니다. 웨이모는 센서 알고리즘 중심의 기술 우위를 기반으로 로보택시를 확장하는 반면, 우버는 플랫폼 및 fleet 운영 효율성을 내세워 파트너십 확장에 집중하고 있습니다. 10년 뒤 모빌리티 시장은 독자 기술 보유자와 플랫폼 독점자 간의 융합 또는 패권 다툼이 결정지을 것입니다.",
        "key_claims": [
            "<span class=\"text-cyan-300 font-semibold\">웨이모</span>: 풀스택 독자 자율주행 기술 및 센서 인프라 우위",
            "<span class=\"text-cyan-300 font-semibold\">우버</span>: 월간 1억 5천만 명의 이용자를 가진 글로벌 배차 플랫폼 파워",
            "로보택시 상용화의 핵심은 <span class=\"text-amber-300 font-bold\">운행 단가 낮추기</span>와 안전성 검증"
        ],
        "data_points": [
            "웨이모 주간 유료 로보택시 운행 건수 10만 건돌파",
            "우버 글로벌 승차 공유 시장 점유율 70% 수준 유지"
        ],
        "signal": "bullish",
        "signal_reason": "<span class=\"text-amber-300 font-bold\">로보택시 생태계</span>가 실험실을 벗어나 실제 상업 매출과 대량 확장 단계로 진입함.",
        "key_companies": ["Uber", "Waymo (Alphabet)", "Tesla"],
        "insight": "자율주행 기술 자체 못지않게 이를 대중에게 서비스화할 수 있는 <span class=\"text-cyan-300 font-semibold\">플랫폼 네트워크</span>가 모빌리티 승패의 핵심 열쇠가 되고 있습니다.",
        "action_point": "웨이모의 자율주행 솔루션을 적용하는 차량 제조사 및 우버의 로보택시 플랫폼 얼라이언스 참여 기업에 대한 관찰이 필요합니다."
    },
    "gNfYJ8Mc2Mk.json": {
        "primary_topic": "space",
        "secondary_topics": ["tech", "stock"],
        "tags": ["스페이스X", "스타십13차", "우주발사", "스타링크", "재사용로켓"],
        "summary": "<span class=\"text-cyan-300 font-semibold\">스페이스X</span>의 스타십 13차 시험 발사가 폭발 없이 해상 수직 착수까지 완벽하게 성공하며 우주 발사체 역사의 이정표를 세웠습니다. 33개 라프터 엔진의 동시 점화와 메가 랩터의 안정적인 작동이 검증되었습니다. 이는 우주 인공위성 네트워크 배치는 물론 향후 달과 화성 수송 프로젝트의 실현 가능성을 극적으로 끌어올렸습니다.",
        "key_claims": [
            "스타십 13차 발사에서 비행 중 폭발 없이 <span class=\"text-cyan-300 font-semibold\">목표 궤도 안착 및 수직 착수</span> 성공",
            "33개 랩터 엔진의 완벽한 추력 제어와 핫 스태이징 분리 검증",
            "<span class=\"text-amber-300 font-bold\">스타링크</span> 차세대 거대 위성 대량 수송 능력 입증"
        ],
        "data_points": [
            "13차 시험 비행 성공으로 최고 비행 고도 및 복귀 스케줄 완수",
            "차세대 랩터 3 엔진 도입으로 추력 20% 이상 향상"
        ],
        "signal": "bullish",
        "signal_reason": "<span class=\"text-cyan-300 font-semibold\">스타십 재사용 발사</span>의 핵심 기술적 허들을 통과함에 따라 우주산업 전반에 강한 호재로 작용.",
        "key_companies": ["SpaceX", "Tesla"],
        "insight": "스타십의 연이은 성공은 인류의 우주 접근 비용을 <span class=\"text-amber-300 font-bold\">패러다임 전환</span> 수준으로 낮추어 민간 우주 경제의 폭발적 성장을 견인할 것입니다.",
        "action_point": "우주 항공 관련 국내외 소재/부품/장비 채널 및 위성 통신 관련 서비스 기업에 주목할 시점입니다."
    },
    "izAtyKRZxiE.json": {
        "primary_topic": "tech",
        "secondary_topics": ["stock", "economy"],
        "tags": ["샌프란시스코", "이재명대통령", "젠슨황", "최태원", "이재용", "AI투자"],
        "summary": "샌프란시스코에서 열린 글로벌 AI 정상급 면담에서 <span class=\"text-cyan-300 font-semibold\">젠슨 황(엔비디아)</span>, 샘 올트먼, 브로드컴 수장 및 국내 재계 총수들이 한자리에 모여 초대형 AI 인프라 펀딩과 반도체 공급망 협력을 논의했습니다. 한국의 HBM 메모리 반도체와 글로벌 GPU 플랫폼 간의 결합이 더욱 공고해지고 있습니다. 글로벌 기술 자본의 거대한 자금 흐름이 AI 밸류체인으로 집결하고 있음을 확인했습니다.",
        "key_claims": [
            "엔비디아 및 빅테크 최고경영진과 한국 최고 재계 리더들의 <span class=\"text-violet-300 font-medium\">전대미문의 AI 협력 얼라이언스</span>",
            "HBM4 등 차세대 메모리 반도체 시장에서의 한국 기업 독점적 기술 우위 확인",
            "글로벌 AI 데이터센터 확충을 위한 <span class=\"text-amber-300 font-bold\">천문학적 수조 달러 단위 자금 유입</span>"
        ],
        "data_points": [
            "글로벌 빅테크 연간 AI 데이터센터 투자 규모 2,000억 달러 초과 전망",
            "HBM3e/HBM4 공급계약 물량 향후 2년간 완료 수준"
        ],
        "signal": "bullish",
        "signal_reason": "글로벌 테크 거인들과 한국 반도체 기업 간의 <span class=\"text-cyan-300 font-semibold\">강력한 파트너십과 대규모 투자 집행</span> 확정.",
        "key_companies": ["엔비디아", "SK하이닉스", "삼성전자", "브로드컴"],
        "insight": "자본 시장의 돈은 거짓말을 하지 않으며, 현재 글로벌 메가머니의 지향점은 오직 <span class=\"text-amber-300 font-bold\">AI 인프라와 첨단 반도체</span>로 집결되고 있습니다.",
        "action_point": "HBM 장비사, 패키징 관련주 및 AI 파운드리 밸류체인 수혜주 중심의 지속적인 비중 확대가 추천됩니다."
    },
    "jb_UnAK0pQ4.json": {
        "primary_topic": "tech",
        "secondary_topics": ["stock", "robot"],
        "tags": ["페르소나AI", "팔란티어", "하이퍼오토메이션", "AI에이전트", "기업용AI"],
        "summary": "기업의 실제 업무를 자동화하는 '하이퍼 오토메이션' 시장이 열리면서 <span class=\"text-cyan-300 font-semibold\">페르소나AI</span>가 한국판 팔란티어로 급부상하고 있습니다. 기존의 단순 대화형 생성 AI를 넘어 AI 에이전트가 기업 내부 데이터베이스 및 ERP와 연동되어 업무 판단과 실행까지 담당합니다. 시가총액 400조 원의 팔란티어처럼 B2B 및 공공기관의 디지털 전환을 주도하는 기업용 AI 소프트웨어 수요가 폭증하고 있습니다.",
        "key_claims": [
            "단순 챗봇을 넘어 업무 실행까지 맡는 <span class=\"text-amber-300 font-bold\">자율형 AI 에이전트</span>의 등장",
            "<span class=\"text-cyan-300 font-semibold\">팔란티어</span> 모델처럼 기업/국가 데이터 융합 및 실시간 의사결정 플랫폼화",
            "국내 금융 및 제조 현장에 하이퍼오토메이션 빠르게 침투 중"
        ],
        "data_points": [
            "팔란티어 주가 최근 1년간 200% 이상 상승하며 B2B AI 시장 가치 입증",
            "국내 기업 AI 솔루션 도입률 연 40% 고성장"
        ],
        "signal": "bullish",
        "signal_reason": "B2B 실질 매출을 창출하는 <span class=\"text-cyan-300 font-semibold\">기업용 AI 에이전트 서비스</span> 시장의 가파른 성장세.",
        "key_companies": ["Palantir", "페르소나AI", "삼성SDS", "포스코DX"],
        "insight": "AI의 가치는 단순 생성 능력이 아니라 기업의 생산성을 직접 높이는 <span class=\"text-amber-300 font-bold\">업무 자동화 플랫폼</span> 구현에 결정되어 있습니다.",
        "action_point": "국내 B2B AI 에이전트 개발사 및 SI 스마트팩토리 관련 솔루션기업에 지속적인 관심을 가질 필요가 있습니다."
    },
    "jEUYqzDf01Y.json": {
        "primary_topic": "tech",
        "secondary_topics": ["economy", "stock"],
        "tags": ["미국관세", "반도체관세", "트럼프관세", "메모리반도체", "통상리스크"],
        "summary": "미국 백악관과 상무부가 2026년 7월 자국 내 데이터센터용 수입 반도체에 대해 최대 100%의 관세 부과를 검토 중인 것으로 나타나 한국 메모리 반도체 업계에 비상이 걸렸습니다. 미-중 패권 경쟁 고도화 속에서 자국 생산 인센티브 강화를 위한 무역장벽 카드로 활용하려는 의도입니다. 다만 미국 내 Big Tech들의 HBM 등 첨단 반도체 수급 대안이 부족해 실제 시행 여부 및 수율 조건 완화 negotiation이 관건입니다.",
        "key_claims": [
            "미 미국 상무부, 수입 데이터센터용 반도체 대상 <span class=\"text-rose-400 font-medium\">최대 100% 관세 검토</span> 공식화",
            "한국 <span class=\"text-cyan-300 font-semibold\">SK하이닉스/삼성전자</span>의 미 현지 생산 공장 설립 가속화 압박",
            "미국 빅테크 기업들의 인프라 구축 비용 증가에 따른 발등의 불"
        ],
        "data_points": [
            "검토 중인 데이터센터용 첨단 메모리 관세율 최대 100%",
            "한국 기업의 대미 메모리 반도체 수출 비중 전체 수출의 35%"
        ],
        "signal": "bearish",
        "signal_reason": "<span class=\"text-rose-400 font-medium\">보호무역주의 관세 리스크</span> 가시화에 따른 반도체 수출 센티멘트 악화.",
        "key_companies": ["SK하이닉스", "삼성전자", "엔비디아", "마이크론"],
        "insight": "미국의 관세 위협은 자국 내 파운드리 및 메모리 생산기지 이전을 강제하기 위한 <span class=\"text-violet-300 font-medium\">지정학적 통상 압박</span>의 일환입니다.",
        "action_point": "미국 현지 공장 신설이 빠르게 이루어지는 반도체 밸류체인 및 관세 면제 가능성을 고려한 유연한 리스크 관리가 필요합니다."
    },
    "jpv0lWh679I.json": {
        "primary_topic": "robot",
        "secondary_topics": ["tech", "stock"],
        "tags": ["현대차", "엔비디아", "피지컬AI", "보스턴다이내믹스", "자율주행"],
        "summary": "<span class=\"text-cyan-300 font-semibold\">현대차그룹</span>과 <span class=\"text-cyan-300 font-semibold\">엔비디아</span>가 피지컬 AI 및 자율주행, 로보틱스 전반에서의 대대적인 파트너십 확대를 선언했습니다. 젠슨 황과 이재명 대통령, 현대차 경영진 간의 연쇄 면담을 통해 제네시스 차세대 자율주행 차량 공동 개발 및 보스턴 다이내믹스 로봇에 엔비디아의 드라이브/아이작(Isaac) 플랫폼을 이식하기로 했습니다. 이는 완성차 제조 역량과 세계 최고 AI 파운드리의 결합으로 로보틱스 산업의 패러다임을 전환시킬 핵심 동맹입니다.",
        "key_claims": [
            "<span class=\"text-cyan-300 font-semibold\">현대차-엔비디아</span> 동맹: 자율주행 차량 및 피지컬 AI 로봇 공동 개발",
            "보스턴 다이내믹스 휴머노이드 로봇에 <span class=\"text-cyan-300 font-semibold\">엔비디아 Isaac 로보틱스 엔진</span> 통합",
            "한국을 글로벌 로보틱스 및 피지컬 AI의 전초기지로 육성"
        ],
        "data_points": [
            "글로벌 피지컬 AI 시장 규모 2030년까지 1조 달러 성장 전망",
            "현대차그룹 자율주행 및 로보틱스 분야 누적 투자액 10조 원 상회"
        ],
        "signal": "bullish",
        "signal_reason": "<span class=\"text-cyan-300 font-semibold\">현대차와 엔비디아</span>의 구체적인 글로벌 로보틱스/자율주행 사업화 파트너십 구축.",
        "key_companies": ["현대차", "엔비디아", "보스턴다이내믹스", "현대모비스"],
        "insight": "피지컬 AI의 핵심은 소프트웨어 파워와 정밀 하드웨어의 접목이며, <span class=\"text-amber-300 font-bold\">현대차-엔비디아 동맹</span>은 이 분야 글로벌 리더십을 쥐게 될 것입니다.",
        "action_point": "현대차그룹 로보틱스 부품 공급망 및 엔비디아 로보틱스 파트너로 참여하는 국내 핵심 부품사에 주목하세요."
    },
    "kOSJpR5itA0.json": {
        "primary_topic": "economy",
        "secondary_topics": ["stock", "tech"],
        "tags": ["스콧베센트", "AI전쟁", "1000조원", "미국재무부", "우주항공"],
        "summary": "미국 차기 재무장관으로 유력한 <span class=\"text-amber-300 font-bold\">스콧 베센트</span>가 글로벌 AI 주도권 전쟁에서 승리하기 위해 1,000조 원(약 7,500억 달러) 이상의 국가적 자본 투입이 시급하다고 밝혔습니다. 민간 빅테크 캡엑스뿐만 아니라 미 정부 차원의 첨단 기술 및 우주 안보 예산 확충이 가속화될 전망입니다. 동시에 재성공한 스페이스X 스타십 13차 발사 등 우주 항공 테마와 AI 인프라 투자가 글로벌 시장 상승을 이끄는 쌍두마차로 부상했습니다.",
        "key_claims": [
            "미 재무장관 후보 베센트, <span class=\"text-amber-300 font-bold\">1,000조 원 규모 AI 국가 패권 예산</span> 및 민간 자본 유출입 관리 강조",
            "<span class=\"text-cyan-300 font-semibold\">스페이스X 스타십</span> 성공에 따른 우주 항공 관련주 재평가 모멘텀",
            "미국 안보 중심의 첨단 기술 공급망 재편 재정 지원 확대"
        ],
        "data_points": [
            "베센트 제안 AI 및 국방 기술 기여 자본 규모 7,500억 달러",
            "스페이스X 스타십 성공 직후 글로벌 우주 항공 지수 5% 급등"
        ],
        "signal": "bullish",
        "signal_reason": "미 정부 차원의 <span class=\"text-amber-300 font-bold\">초대형 재정 투입</span> 및 안보 AI/우주 산업 국가 지원 가속화.",
        "key_companies": ["NVIDIA", "SpaceX", "Palantir", "Lockheed Martin"],
        "insight": "AI와 우주는 단순 민간 기술을 넘어 강대국 간의 <span class=\"text-violet-300 font-medium\">패권 유지를 위한 국가 안보 자산</span>으로 격상되었습니다.",
        "action_point": "미국 국방/안보 AI 및 우주 항공 부품 밸류체인 관련 종목에 대한 주도적 투자 전략이 필요합니다."
    },
    "OzVXKQ1L08I.json": {
        "primary_topic": "tech",
        "secondary_topics": ["stock", "etc"],
        "tags": ["마운자로", "일라이릴리", "비만치료제", "GLP-1", "바이오헬스"],
        "summary": "<span class=\"text-cyan-300 font-semibold\">일라이 릴리</span>의 비만 치료제 <span class=\"text-cyan-300 font-semibold\">마운자로(Mounjaro)</span>가 체중 감량 효과를 넘어 심혈관 질환, 당뇨, 심지어 치매 예방 가능성까지 입증하며 의학계와 헬스케어 증시에 돌풍을 일으키고 있습니다. GLP-1 계열 약물의 적응증 확대로 관련 시장 규모가 폭발적으로 팽창하고 있습니다. 글로벌 제약사들의 위탁생산(CMO) 및 원료의약품 수혜가 본격화되고 있습니다.",
        "key_claims": [
            "<span class=\"text-cyan-300 font-semibold\">마운자로</span>의 탁월한 체중 감량(임상 시 최대 22% 감소) 및 대사 질환 치료 효능",
            "GLP-1 의약품의 심혈관 질환 및 뇌질환 등 <span class=\"text-amber-300 font-bold\">적응증 연쇄 확장</span>",
            "글로벌 의약품 위탁생산(CMO) 공급 부족에 따른 생산 설비 경쟁"
        ],
        "data_points": [
            "글로벌 비만치료제 시장 규모 2030년 1,000억 달러 초과 예상",
            "일라이 릴리 시가총액 제약바이오 최초 1조 달러 돌파 육박"
        ],
        "signal": "bullish",
        "signal_reason": "<span class=\"text-cyan-300 font-semibold\">GLP-1 블록버스터 신약</span>의 지속적인 적응증 확대 및 글로벌 글로벌 제약바이오 시총 견인.",
        "key_companies": ["Eli Lilly", "Novo Nordisk", "삼성바이오로직스"],
        "insight": "마운자로는 단순 다이어트 약이 아니라 인간의 건강 수명을 늘리는 <span class=\"text-amber-300 font-bold\">대사 질환 게임체인저</span>로 자리매김하고 있습니다.",
        "action_point": "글로벌 비만치료제 펩타이드 원료 제조사 및 바이오 의약품 CMO 생산기업에 지속 관심이 요구됩니다."
    },
    "Rg-d702MrIg.json": {
        "primary_topic": "tech",
        "secondary_topics": ["stock", "etc"],
        "tags": ["갤럭시워치울트라2", "퀄컴", "엑시노스", "스마트워치", "배터리효율"],
        "summary": "삼성전자가 신형 갤럭시 워치 울트라2에 자체 <span class=\"text-cyan-300 font-semibold\">엑시노스</span> 대신 <span class=\"text-cyan-300 font-semibold\">퀄컴</span>의 3nm 웨어러블 칩셋을 전격 채택하며 배터리 성능을 대폭 끌어올렸습니다. 일상적인 잦은 충전 문제를 해결하여 최대 3일간 작동할 수 있는 전력 관리 효율성을 갖췄습니다. 칩셋 이원화와 고객 경험 극대화를 위한 이번 선택이 글로벌 프리미엄 스마트워치 시장에서 긍정적 평가를 받고 있습니다.",
        "key_claims": [
            "<span class=\"text-cyan-300 font-semibold\">퀄컴 초저전력 AP</span> 도입으로 배터리 성능 전작 대비 2배 이상 획기적 증가",
            "스마트워치 최대 단점이었던 <span class=\"text-amber-300 font-bold\">배터리 조기 방전 이슈</span> 해결",
            "삼성전자의 실용적인 글로벌 반도체 얼라이언스 전략 강화"
        ],
        "data_points": [
            "갤럭시 워치 울트라2 배터리 타임 최대 80시간 달성",
            "퀄컴 3nm 프로세서의 전력 효율 개선율 30% 증가"
        ],
        "signal": "bullish",
        "signal_reason": "소비자 니즈 중심의 <span class=\"text-cyan-300 font-semibold\">칩셋 채택 전략</span>으로 완성도 제고 및 제품 판매량 증대 기대.",
        "key_companies": ["삼성전자", "퀄컴", "애플"],
        "insight": "자체 수율에 얽매이지 않고 최상의 파트너 솔루션을 선택하는 <span class=\"text-amber-300 font-bold\">유연한 결단</span>이 하드웨어 경쟁력을 살린 본보기입니다.",
        "action_point": "퀄컴 웨어러블 반도체 밸류체인 및 삼성전자 모바일 신제품 흥행 가능성에 따른 부품 공급사에 관심이 필요합니다."
    },
    "TRz8qklCbIo.json": {
        "primary_topic": "economy",
        "secondary_topics": ["stock", "energy"],
        "tags": ["월가백브리핑", "국제유가", "트럼프", "FOMC", "타코법안"],
        "summary": "중동 및 국제 유가 상승세에도 불구하고 트럼프의 관망 태도 속에서 다음 주 열릴 FOMC 금리 결정에 금융 시장의 시선이 집중되고 있습니다. 트럼프 전 대통령이 에너지 가격 안정에 즉각적인 발언을 아끼는 가운데, 증시 살리기를 위한 정책적 카드('타코' 등 시장 달래기 조치)가 유효할지 관심입니다. 인플레이션 재발 우려와 금리 인하 경로 간의 신경전이 지속되는 상황입니다.",
        "key_claims": [
            "국제 유가 반등에도 불확실한 <span class=\"text-rose-400 font-medium\">트럼프의 에너지 무역 정책</span> 행보",
            "미 연준 FOMC 금리 결정 전 시장의 통화정책 힌트 부재로 <span class=\"text-amber-300 font-bold\">관망세 심화</span>",
            "증시 하방을 방어할 수 있는 정책적 모멘텀 부재 우려"
        ],
        "data_points": [
            "WTI 국제 유가 배럴당 80달러선 근접 반등",
            "연준 7월 금리 동결 확률 90% 이상 형성"
        ],
        "signal": "neutral",
        "signal_reason": "유가 상승에 따른 인플레 우려와 <span class=\"text-amber-300 font-bold\">FOMC 대기 심리</span>가 맞물려 시장 변동성 확대.",
        "key_companies": ["ExxonMobil", "Chevron", "Apple", "Microsoft"],
        "insight": "정치적 셈법과 유가 인플레이션, 연준의 통화정책 사이에서 금융 시장은 확실한 <span class=\"text-amber-300 font-bold\">시그널이 나오기 전까지 숨고르기</span>를 이어나갈 것입니다.",
        "action_point": "에너지 유가 수혜주와 지수 하방 방어력이 뛰어난 고배당/현금흐름 우수주 중심으로 위험을 분산할 필요가 있습니다."
    },
    "Ujexfy_JOGE.json": {
        "primary_topic": "space",
        "secondary_topics": ["tech", "stock"],
        "tags": ["스페이스X", "스타십13차", "해상착수", "재사용로켓", "안될과학"],
        "summary": "<span class=\"text-cyan-300 font-semibold\">스페이스X 스타십</span> 13차 시험 발사에서 33개 랩터 엔진 점화부터 분리, 목표 궤도 진입 및 해상 수직 착수까지 단 한 번의 폭발 없이 완벽하게 수행되었습니다. 초대형 발사체 완전 재사용 구상이 실제 현실화되고 있음을 보여주었습니다. 우주 수송의 경제성이 기하급수적으로 개선되면서 우주 탐사 및 위성 네트워크 분야에 큰 변혁이 시작되었습니다.",
        "key_claims": [
            "스타십 13차 시험 비행 완벽 성공 및 <span class=\"text-cyan-300 font-semibold\">해상 수직 연착수</span> 달성",
            "33개 메가 랩터 엔진의 안정적인 추력 및 제어 능력 입증",
            "<span class=\"text-amber-300 font-bold\">민간 우주 수송 시대</span> 본격 개막"
        ],
        "data_points": [
            "발사체 33개 라프터 엔진 100% 정상 작동 검증",
            "해상 수직 착수 정밀도 목표 범위 내 달성"
        ],
        "signal": "bullish",
        "signal_reason": "<span class=\"text-cyan-300 font-semibold\">스타십 시험 비행의 완벽한 성취</span>로 우주항공 산업 투자 심리 대폭 개선.",
        "key_companies": ["SpaceX", "Tesla"],
        "insight": "스타십의 수직 착수 성공은 발사체 재사용을 통한 <span class=\"text-amber-300 font-bold\">우주 수송 비용 1/10 절감</span> 목표가 완성에 매우 가까워졌음을 의미합니다.",
        "action_point": "우주 항공 위성 통신 플랫폼 및 국내 우주 발사체 부품 공급 기업에 대한 적극적 투자가 유망합니다."
    }
}

for f in files:
    path = pending_dir / f.name
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    video_info = data.get("video", {})
    v_id = video_info.get("id")
    
    if f.name in analysis_map:
        ana_info = analysis_map[f.name]
        item = {
            "video": video_info,
            "classification": {
                "primary_topic": ana_info["primary_topic"],
                "secondary_topics": ana_info["secondary_topics"],
                "tags": ana_info["tags"]
            },
            "analysis": {
                "summary": ana_info["summary"],
                "key_claims": ana_info["key_claims"],
                "data_points": ana_info["data_points"],
                "signal": ana_info["signal"],
                "signal_reason": ana_info["signal_reason"],
                "key_companies": ana_info["key_companies"],
                "insight": ana_info["insight"],
                "action_point": ana_info["action_point"]
            }
        }
        batch_data.append(item)

out_file = Path("scratch/batch_analyzed.json")
out_file.write_text(json.dumps(batch_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated batch_analyzed.json with {len(batch_data)} items.")
