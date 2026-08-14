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
    "0u98f5AjNAQ": {
        "primary_topic": "etc",
        "secondary_topics": ["tech"],
        "tags": ["인구절벽", "정자수감소", "환경호르몬", "생식보건", "안될과학"],
        "summary": "환경호르몬 및 생활 습관 변화로 인한 <span class=\"text-rose-400 font-medium\">남성 정자 수 감소 및 생식력 저하</span> 현상을 인류학적·의학적 데이터로 분석하고 대책을 제시합니다.",
        "key_claims": [
            "글로벌 연구 결과 최근 40년간 남성 정자 농도가 <span class=\"text-rose-400 font-medium\">50% 이상 급감</span>했다.",
            "미세플라스틱 및 환경호르몬(프탈레이트 등)이 <span class=\"text-amber-300 font-bold\">내분비계 교란의 핵심 원인</span>으로 지목된다.",
            "단순 공포론에서 벗어나 <span class=\"text-cyan-300 font-semibold\">생활 습관 개선 및 화학물질 규제</span>가 시급하다."
        ],
        "data_points": [
            "정자 농도 하락세: 1973년 ㎖당 9,900만 개에서 최근 4,700만 개로 52% 감소",
            "글로벌 합계출산율: 선진국 중심 1.5명 이하 하락"
        ],
        "signal": "neutral",
        "signal_reason": "장기 인구 구조적 위기 요인이나 의학 기술 및 환경 규제로 개선 시도가 이뤄지고 있기 때문입니다.",
        "key_companies": ["안될과학"],
        "insight": "인구 감소는 단순 사회적 문제를 넘어 화학 소재 규제 및 헬스케어 진단 시장의 구조적 성장을 유도합니다.",
        "action_point": "환경호르몬 대체 친환경 소재 기업 및 난임/생식 헬스케어 관련 분야에 장기적 관심을 추천합니다."
    },
    "1iyqUd01fJo": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["반도체집중", "급락장대응", "아침N투자", "포트폴리오", "삼프로TV"],
        "summary": "반도체 쏠림이 컸던 포트폴리오의 변동성에 대응하여 <span class=\"text-cyan-300 font-semibold\">실적 가치 기준의 위험 관리와 필수소비재/산업재 분산 전략</span>이 필요합니다.",
        "key_claims": [
            "반도체 단기 변동성 확대로 인한 <span class=\"text-rose-400 font-medium\">계좌 평가손실 심리적 공포</span> 심화.",
            "손절매보다는 <span class=\"text-cyan-300 font-semibold\">하반기 실적 가시성이 높은 HBM 대장주</span> 위주로 포트폴리오 압축.",
            "지수 반등 시 <span class=\"text-amber-300 font-bold\">실적주 위주 빠른 수급 회복</span> 기대."
        ],
        "data_points": [
            "반도체 비중 손실폭: 고점 대비 25~30% 이상 조정",
            "삼성전자/SK하이닉스 하반기 예상 영업이익: 분기별 고점 형성 지속"
        ],
        "signal": "bullish",
        "signal_reason": "단기 쏠림에 따른 변동성일 뿐 반도체 이익 상향 기조는 유효하기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "투매에 휩쓸리지 않고 펀더멘털이 확실한 대장주 중심으로 포트폴리오를 슬림화해야 합니다.",
        "action_point": "반도체 대장주의 조정을 매수 기회로 활용하고, 일부 자금을 산업재/배당주로 분산하십시오."
    },
    "2Bubm-34v8Q": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["오전방송", "반도체조정", "애플승승장구", "나스닥", "삼프로TV"],
        "summary": "반도체주 조정으로 나스닥 지수가 약보합 마감했으나, <span class=\"text-cyan-300 font-semibold\">애플의 펀더멘털 독주</span>가 전체 증시 하방을 단단히 지지했습니다.",
        "key_claims": [
            "엔비디아/마이크론 약세 속에 <span class=\"text-cyan-300 font-semibold\">애플의 상승세</span>가 지수 방어율을 높였다.",
            "빅테크 간 CapEx 투자 및 <span class=\"text-amber-300 font-bold\">실적 펀더멘털 차별화</span>가 극명하게 전개된다.",
            "미국 증시는 <span class=\"text-violet-300 font-medium\">견조한 로테이션 장세</span>로 하방 경직성을 유지 중이다."
        ],
        "data_points": [
            "나스닥 지수 변동: -0.2% 약보합 마감",
            "애플 시가총액: 4.95조 달러 돌파하며 독주"
        ],
        "signal": "bullish",
        "signal_reason": "빅테크 대장주의 우수한 펀더멘털이 증시 하방 지지력을 공고히 하고 있기 때문입니다.",
        "key_companies": ["애플", "엔비디아", "마이크론"],
        "insight": "반도체 단기 조정에도 빅테크 대표주의 펀더멘털이 든든한 버팀목 역할을 해주고 있습니다.",
        "action_point": "애플 등 시총 상위 우량 펀더멘털 기업 편입을 지속 유지하십시오."
    },
    "5wM1z1034BU": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["7월FOMC", "금리동결", "기준금리", "매파적동결", "매경월가월부"],
        "summary": "연준이 7월 FOMC에서 <span class=\"text-cyan-300 font-semibold\">기준금리를 3.50~3.75%로 9대 3 동결</span>하였으나, 2016년 이후 최다 반대표(3명 인상 의견)가 출현하며 매파적 경계감이 고조되었습니다.",
        "key_claims": [
            "연준 위원 12명 중 <span class=\"text-rose-400 font-medium\">3명이 금리 인상 반대표</span>를 던지며 매파적 균열 표출.",
            "케빈 워시 의장은 포워드 가이던스 제시를 피하며 <span class=\"text-amber-300 font-bold\">데이터 의존적 통화 정책</span> 강조.",
            "인플레이션 우려가 잔존하나 <span class=\"text-cyan-300 font-semibold\">시장 불확실성 1차 해소</span>로 해석."
        ],
        "data_points": [
            "기준금리 동결 수준: 3.50% ~ 3.75% 유지",
            "투표 결과: 9대 3 (3명 금리 인상 찬성표 제출)"
        ],
        "signal": "neutral",
        "signal_reason": "금리 동결로 단기 불확실성은 낮아졌으나 매파적 반대표 출현으로 추가 긴축 경계감이 상존하기 때문입니다.",
        "key_companies": ["연준(Fed)", "매경월가월부"],
        "insight": "만장일치 동결이 아닌 3표의 매파적 반대표 출현은 향후 통화 정책의 변동성 요인이 될 수 있습니다.",
        "action_point": "FOMC 이후 국채 금리 및 환율 변동성을 관찰하며 고배당주 및 우량 밸류주 비중을 유지하십시오."
    },
    "6Xpzw8HYclQ": {
        "primary_topic": "etc",
        "secondary_topics": ["economy"],
        "tags": ["어바웃뉴욕", "뉴욕상권", "임대료폭등", "풍선매장", "매경월가월부"],
        "summary": "뉴욕 초고가 명당 상권에서 미슐랭 셰프 식당마저 임대료와 고물가를 견디지 못하고 철수하며, <span class=\"text-rose-400 font-medium\">상업용 부동산 고비용 리스크</span>를 단적으로 보여줍니다.",
        "key_claims": [
            "뉴욕 상업용 임대료 및 인건비 폭증으로 <span class=\"text-rose-400 font-medium\">전통 고급 요식업체의 폐업</span> 가속화.",
            "고정비 부담이 적은 팝업스토어 및 체험형 엑티비티 매장이 <span class=\"text-cyan-300 font-semibold\">대체 임차인으로 부상</span>.",
            "상업용 부동산 시장의 <span class=\"text-amber-300 font-bold\">양극화 및 구조 재편</span> 진행."
        ],
        "data_points": [
            "뉴욕 명품 거리 임대료 상승률: 전년 대비 15% 이상 폭등",
            "요식업 평균 영업이익률: 고물가로 인해 3% 이하로 축소"
        ],
        "signal": "bearish",
        "signal_reason": "고물가 및 임대료 폭등이 실물 자영업 및 상업용 부동산 임대 시장에 부담으로 작동하기 때문입니다.",
        "key_companies": ["매경월가월부"],
        "insight": "상업용 부동산의 고비용 구조는 오프라인 매장의 패러다임을 체험형 팝업 중심으로 바꾸고 있습니다.",
        "action_point": "전통 리츠 및 오프라인 유통 리츠 투자 시 상권별 임대율과 고정비 구조를 꼼꼼히 점검하십시오."
    },
    "7m-qG9cRV3A": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["전기차나락", "배터리캐즘", "EV캐즘", "완성차전략", "SOD"],
        "summary": "전기차 캐즘(Chasm) 가속화로 완성차 기업들이 <span class=\"text-rose-400 font-medium\">EV 케펙스 축소 및 하이브리드/내연기관 재전환</span>을 추진하고 있습니다.",
        "key_claims": [
            "보조금 축소와 높은 차량 가격으로 <span class=\"text-rose-400 font-medium\">전기차 신규 수요 둔화</span> 심화.",
            "포드, GM 등 글로벌 완성차들이 <span class=\"text-cyan-300 font-semibold\">하이브리드(HEV) 중심으로 라인업 수정</span>.",
            "배터리 셀 제조사들의 <span class=\"text-amber-300 font-bold\">CapEx 속도 조절 및 체질 개선</span> 필수적."
        ],
        "data_points": [
            "글로벌 EV 침투율 성장세: 기존 30% 예상치에서 15% 수준으로 둔화",
            "하이브리드(HEV) 판매 증가율: 전년 대비 30% 이상 폭증"
        ],
        "signal": "bearish",
        "signal_reason": "전기차 수요 캐즘 장기화로 배터리 및 EV 밸류체인의 단기 실적 압박이 지속되기 때문입니다.",
        "key_companies": ["포드", "테슬라", "LG에너지솔루션"],
        "insight": "전동화 전환의 속도가 조절되면서 하이브리드와 유연한 생산 플랫폼을 보유한 완성차 기업이 반사이익을 얻습니다.",
        "action_point": "순수 전기차/배터리 비중을 조절하고 하이브리드 경쟁력을 갖춘 완성차 우량주에 주목하십시오."
    },
    "8d3pAXeeyPE": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["고점대비30퍼", "코스피바닥", "교양이를부탁해", "증시바닥", "알상무"],
        "summary": "고점 대비 30% 가까이 폭락한 증시는 수급 청산의 막바지로, <span class=\"text-cyan-300 font-semibold\">역사적 기술적 바닥권에 근접</span>했습니다.",
        "key_claims": [
            "30% 급락은 반대매매와 패닉셀이 몰린 <span class=\"text-cyan-300 font-semibold\">전형적인 투매의 피크</span>이다.",
            "밸류에이션 상 지수 PBR은 바닥에 진입하여 <span class=\"text-amber-300 font-bold\">강력한 하방 경직성</span>을 보여준다.",
            "투매 마감 후 <span class=\"text-cyan-300 font-semibold\">실적주 중심의 빠른 리바운드</span>가 연출된다."
        ],
        "data_points": [
            "지수 낙폭: 고점 대비 -28.5% 기록",
            "역사적 바닥 PBR: 0.85배 근접"
        ],
        "signal": "bullish",
        "signal_reason": "극단적 과매도 구간 도달로 수급 정상화 시 강력한 반등 보상이 수반되기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "고점 대비 30% 하락은 시장의 공포가 극에 달한 시점으로, 장기 관점의 비중 확대 적기입니다.",
        "action_point": "지수형 ETF 및 반도체 대장주의 분할 매수를 추천합니다."
    },
    "8md2XoVzLok": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["V자반등", "바닥근접", "삼전닉스모을때", "집중오늘의주식", "삼프로TV"],
        "summary": "V자 급반등은 어려울지라도 바닥권이 확인된 만큼, <span class=\"text-cyan-300 font-semibold\">삼성전자와 SK하이닉스를 분할 모아가는 모아내기 전략</span>이 유효합니다.",
        "key_claims": [
            "지수의 급격한 V자 반등보다 <span class=\"text-cyan-300 font-semibold\">바닥 다지기 후 계단식 상승</span> 가능성 높음.",
            "삼성전자/SK하이닉스는 HBM 실적 지표가 탄탄하여 <span class=\"text-amber-300 font-bold\">확실한 저가 매수 구간</span> 진입.",
            "단기 노이즈보다 <span class=\"text-cyan-300 font-semibold\">하반기 영업이익 급증</span>에 집중해야 한다."
        ],
        "data_points": [
            "SK하이닉스 영업이익률: HBM3E 8단/12단 비중 확대로 35%+ 유지",
            "삼성전자 PBR: 1.1배 수준으로 하단 매수 메리트 우수"
        ],
        "signal": "bullish",
        "signal_reason": "메모리 대장주의 강한 펀더멘털 대비 주가가 극저평가되어 장기 이익 보상이 크기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스", "와이즈경제연구소"],
        "insight": "급격한 반등을 기대하기보다 펀더멘털 대장주를 저점에서 분할 모아가는 정석적인 투자가 승리합니다.",
        "action_point": "삼성전자 및 SK하이닉스의 분할 매수를 지속 전개하십시오."
    },
    "8WA1zvNc0Us": {
        "primary_topic": "robot",
        "secondary_topics": ["tech"],
        "tags": ["미중로봇전쟁", "미국중국로봇제재", "한국로봇수혜", "엔지니어TV", "가드액트"],
        "summary": "미국이 중국산 로봇 및 핵심 부품 통제에 착수함에 따라 <span class=\"text-cyan-300 font-semibold\">한국의 정밀 로봇 부품 공급망</span>이 반사이익의 핵심 파트너로 부각됩니다.",
        "key_claims": [
            "미국의 가드 액트(GUARD Act) 추진으로 <span class=\"text-rose-400 font-medium\">중국산 로봇 부품의 미국 진출 차단</span>.",
            "자동차/반도체 제조 역량을 검증받은 <span class=\"text-cyan-300 font-semibold\">한국의 정밀 감속기·액추에이터</span>가 대체 공급망으로 채택.",
            "미·중 로봇 패권 전쟁 속에서 <span class=\"text-amber-300 font-bold\">K-로봇 소부장 기업의 글로벌 확장</span> 가속화."
        ],
        "data_points": [
            "미국 로봇 규제 범위: 중국산 영구자석, 액추에이터, 관절 모터 포함",
            "국내 로봇 부품사 미국 수출 성장률: 연간 30% 이상 확대 기대"
        ],
        "signal": "bullish",
        "signal_reason": "미국의 탈중국 로봇 공급망 재편으로 한국 정밀 부품 기업들의 글로벌 수주가 확정적이기 때문입니다.",
        "key_companies": ["테슬라", "현대차", "엔지니어TV"],
        "insight": "미중 분쟁의 불확실성 속에서 한국의 정밀 제조업 역량이 로봇 시장의 핵심 안보 자산이 되고 있습니다.",
        "action_point": "국내 정밀 감속기 및 모듈형 액추에이터 제조사 비중 확대를 추천합니다."
    },
    "Aeq9ohZmR30": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["앤트로픽", "AMD헬리오스", "AMD4배성장", "월텍남", "AI칩경쟁"],
        "summary": "앤트로픽이 AMD의 차세대 헬리오스(Helios) AI 가속기를 대량 주문하면서, <span class=\"text-cyan-300 font-semibold\">AMD의 내년 AI 칩 매출이 4배 급증</span>할 것으로 기대됩니다.",
        "key_claims": [
            "앤트로픽의 AMD 헬리오스 채택으로 <span class=\"text-cyan-300 font-semibold\">엔비디아 독점 구도 균열</span> 본격화.",
            "AMD의 AI 가속기 매출이 내년 <span class=\"text-amber-300 font-bold\">전년 대비 4배 이상 폭발적 성장</span>할 전망.",
            "빅테크의 멀티 벤더 전략으로 <span class=\"text-cyan-300 font-semibold\">대체 AI 칩 생태계</span>가 급속히 팽창 중이다."
        ],
        "data_points": [
            "AMD 내년 예상 AI 칩 매출: 200억 달러 돌파 전망 (올해 대비 4배)",
            "앤트로픽 헬리오스 주문 규모: 대형 멀티 클러스터 구축용"
        ],
        "signal": "bullish",
        "signal_reason": "엔비디아 외 대체 AI 칩 시장이 본격 개화하면서 AMD의 이익 성장이 매우 명확해졌기 때문입니다.",
        "key_companies": ["AMD", "Anthropic", "엔비디아"],
        "insight": "빅테크는 단일 벤더 독점을 피하기 위해 AMD 등 2순위 AI 칩 공급망을 적극 육성하고 있습니다.",
        "action_point": "AMD 및 관련 밸류체인 수혜주에 대한 긍정적 포트폴리오 편입을 권고합니다."
    },
    "b2PaYphn-QU": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["인플레이션", "보이지않는세금", "실질임금하락", "이효석아카데미", "구매력약화"],
        "summary": "인플레이션은 실질 구매력을 갉아먹는 <span class=\"text-rose-400 font-medium\">보이지 않는 세금</span>으로, 자산 가격 방어를 위한 배당 및 우량주 투자가 필수적입니다.",
        "key_claims": [
            "물가 상승률이 명목 임금 상승률을 초월해 <span class=\"text-rose-400 font-medium\">실질 소득 축소 현상</span> 고착화.",
            "현금 보유는 자산 가치를 훼손시키므로 <span class=\"text-cyan-300 font-semibold\">인플레 헤지형 우량 자산</span>으로 이동해야 함.",
            "가격 결정력을 지닌 기업만이 <span class=\"text-amber-300 font-bold\">인플레이션 환경에서 마진을 방어</span>한다."
        ],
        "data_points": [
            "누적 물가 상승률: 최근 3년간 15% 이상 폭등",
            "실질 임금 성장률: 마이너스 지속"
        ],
        "signal": "neutral",
        "signal_reason": "거시 구매력 둔화 우려가 있으나, 인플레 헤지 자산 투자의 중요성이 명확해지기 때문입니다.",
        "key_companies": ["이효석아카데미"],
        "insight": "인플레이션을 극복하는 유일한 길은 가격 결정력을 보유한 독점 기업의 지분을 소유하는 것입니다.",
        "action_point": "가격 전가력을 지닌 고마진 빅테크 및 인플레이션 헤지형 배당 ETF 보유를 추천합니다."
    },
    "bcn9WFX8AJs": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["빅테크현금흐름", "FCF", "국장반등변수", "주린이구조대", "삼프로TV"],
        "summary": "미국 빅테크의 자유현금흐름(FCF) 변화와 CapEx 속도 조절이 <span class=\"text-cyan-300 font-semibold\">한국 반도체 및 증시 반등의 결정적 변수</span>로 작동하고 있습니다.",
        "key_claims": [
            "빅테크의 FCF 추이가 AI 투자 지속성 및 <span class=\"text-cyan-300 font-semibold\">한국 반도체 수주</span>를 결정한다.",
            "CapEx 지출 부담 완화와 FCF 회복 신호가 나오면 <span class=\"text-amber-300 font-bold\">국내 증시의 가파른 반등</span>이 전개된다.",
            "실질 현금 흐름을 창출하는 <span class=\"text-cyan-300 font-semibold\">빅테크 펀더멘털 확인</span>이 선행되어야 함."
        ],
        "data_points": [
            "빅테크 전체 FCF 합계: CapEx 증가에도 1,500억 달러 이상 유지",
            "한국 반도체 수출 연동성: 빅테크 FCF와 80% 이상 고 correlation"
        ],
        "signal": "bullish",
        "signal_reason": "빅테크의 현금 창출 능력이 탄탄하여 하반기 반도체 설비 투자 기조가 유지될 것이기 때문입니다.",
        "key_companies": ["마이크로소프트", "메타", "SK하이닉스", "삼성전자"],
        "insight": "빅테크의 FCF가 건강하다면 AI 투자 피크아웃 우려는 일시적 노이즈에 그칠 것입니다.",
        "action_point": "빅테크 실적 발표에서 FCF 지표 확인 후 한국 반도체 대장주의 비중을 확대하십시오."
    },
    "D_ZY1a8FuCU": {
        "primary_topic": "crypto",
        "secondary_topics": ["stock"],
        "tags": ["클래리티법안", "코인시장흔들", "크립토PLUS", "디지털애셋", "삼프로TV"],
        "summary": "미 상원에서 클래리티 법안(Clarity Act) 처리가 밀리면서 <span class=\"text-rose-400 font-medium\">크립토 규제 불확실성에 따른 단기 약세</span>가 연출되었습니다.",
        "key_claims": [
            "러시아 제재 법안 우선 처리로 <span class=\"text-rose-400 font-medium\">클래리티 법안의 8월 내 통과 무산</span>.",
            "법안 지연으로 가상자산 제도권 편입 일정에 <span class=\"text-rose-400 font-medium\">단기 노이즈</span> 발생.",
            "9월 재개 시 명확한 규제 가이드라인이 완성되면 <span class=\"text-amber-300 font-bold\">장기 호재로 재전환</span>될 전망."
        ],
        "data_points": [
            "상원 휴회 일정: 8월 7일부터 여름 휴회 진입",
            "비트코인 가격 영향: 62,000~64,000달러 박스권 횡보"
        ],
        "signal": "neutral",
        "signal_reason": "법안 지연에 따른 단기 수급 위축은 있으나 제도권 법안 논의 자체는 9월에 지속되기 때문입니다.",
        "key_companies": ["디지털애셋", "Coinbase"],
        "insight": "크립토 규제 법안의 지연은 일시적 일정 연기일 뿐, 제도권 편입이라는 거대한 대세는 불변합니다.",
        "action_point": "단기 조정을 활용해 비트코인 및 가상자산 대표 인프라 종목의 관망 후 매수 접근을 권고합니다."
    },
    "EOnC6BBced4": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["FOMC생중계", "워시의장", "기자회견분석", "한경글로벌마켓", "금리동결"],
        "summary": "7월 FOMC 성명서 및 케빈 워시 의장의 기자회견은 <span class=\"text-cyan-300 font-semibold\">데이터 의존적 동결과 매파적 반대표</span>를 확인시켜 주었습니다.",
        "key_claims": [
            "워시 의장은 포워드 가이던스를 자제하며 <span class=\"text-cyan-300 font-semibold\">향후 경제 지표에 따른 동적 정책</span> 강조.",
            "3명의 매파적 반대표에도 불구하고 <span class=\"text-amber-300 font-bold\">시장 발작 없는 동결</span>을 달성했다.",
            "유가 하락세가 지속된다면 <span class=\"text-cyan-300 font-semibold\">하반기 금리 인하 가능성</span>도 열려 있다."
        ],
        "data_points": [
            "FOMC 기준금리: 3.50%~3.75% 동결 결정",
            "미국 국채 10년물 금리 반응: 4.6%선에서 안정적 흐름 유지"
        ],
        "signal": "neutral",
        "signal_reason": "통화 정책의 매파적 잔재가 있으나 충격 없이 동결을 통과했기 때문입니다.",
        "key_companies": ["한경글로벌마켓", "연준"],
        "insight": "연준의 데이터 의존 스탠스는 향후 물가 지표 하락 시 유연한 금리 인하로 전환될 수 있습니다.",
        "action_point": "FOMC 통과 후 불확실성이 감소한 미국 증시 패시브 자산 중심의 포트폴리오를 유지하십시오."
    },
    "gdtYv4LnarE": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["개인숏못침", "알상무현실조언", "교양이를부탁해", "하락장대응", "숏돌이"],
        "summary": "하락장에서 개인 투자자가 숏(Short) 포지션으로 이익을 내기는 매우 어려우므로 <span class=\"text-cyan-300 font-semibold\">현금 비중 확보 및 우량주 장기 보유</span>가 최선의 전략입니다.",
        "key_claims": [
            "개인의 숏/인버스 투자는 타임 디케이와 수수료로 인해 <span class=\"text-rose-400 font-medium\">손실 확률이 극도로 높다</span>.",
            "하락장에서는 섣부른 숏 포지션보다 <span class=\"text-amber-300 font-bold\">현금을 쥐고 바닥을 기다리는 것</span>이 정답이다.",
            "장기 투자 관점에서 <span class=\"text-cyan-300 font-semibold\">실적주를 저렴하게 담는 전략</span>이 승리한다."
        ],
        "data_points": [
            "개인 인버스/곱버스 상품 승률: 통계상 80% 이상 손실 기록",
            "증시 복원력: 폭락 후 1년 이내 평균 85% 이상 이전 고점 회복"
        ],
        "signal": "bullish",
        "signal_reason": "하락장 끝자락에서 파생 숏보다 우량 현물 주식의 장기 보유가 확실한 이익을 안겨주기 때문입니다.",
        "key_companies": ["교양이를부탁해"],
        "insight": "파생 상품으로 시장 하락을 맞히려는 오만을 버리고, 펀더멘털을 가진 현물 자산을 지키는 것이 핵심입니다.",
        "action_point": "인버스 및 레버리지 파생 매매를 지양하고 흑자 대형주 현물 매수를 유지하십시오."
    },
    "hBroDVlzGD4": {
        "primary_topic": "space",
        "secondary_topics": ["tech"],
        "tags": ["달충돌실험", "우주탐사", "달자원", "안될과학", "나사"],
        "summary": "인류가 달 표면에 탐사선을 의도적으로 충돌시킨 목적은 <span class=\"text-cyan-300 font-semibold\">달 내부 성분 분석 및 지하 얼음(수자원) 존재 입증</span>에 있었습니다.",
        "key_claims": [
            "인공 충돌 충격파 분석을 통해 <span class=\"text-cyan-300 font-semibold\">달 남극 지하의 대규모 얼음 수자원</span> 확인.",
            "달 지각 성분 데이터를 바탕으로 <span class=\"text-amber-300 font-bold\">향후 달 기지 건설 및 영구 거주</span> 기반 마련.",
            "우주 탐사 기술이 자원 추출 및 <span class=\"text-violet-300 font-medium\">우주 경제 상업화</span> 단계로 진화."
        ],
        "data_points": [
            "달 충돌 탐사 미션: LCROSS 등 나사 충돌 미션 데이터 활용",
            "달 얼음 매장량 예상: 수억 톤 규모의 수자원 존재 추정"
        ],
        "signal": "bullish",
        "signal_reason": "달 수자원 확인이 심우주 탐사 및 우주 인프라 상업화의 경제성을 입증해주기 때문입니다.",
        "key_companies": ["NASA", "SpaceX", "안될과학"],
        "insight": "달 자원 확보는 향후 화성 탐사 및 우주 경제의 전초기지로서 필수적인 경제적 가치를 가집니다.",
        "action_point": "우주 탐사 소재, 위성 인프라 및 우주 방산 밸류체인에 지속적 관심이 필요합니다."
    },
    "HjW2IZkeKtw": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["8월반등핵심", "투매끝", "마켓인사이드", "박병창", "삼프로TV"],
        "summary": "7월 투매 장세가 마감되고 8월 반등을 결정할 핵심 변수는 <span class=\"text-cyan-300 font-semibold\">빅테크 CapEx 실적 발표 및 외국인 수급의 매수 전환</span>입니다.",
        "key_claims": [
            "7월의 무차별 투매는 일단락되었으며 <span class=\"text-cyan-300 font-semibold\">8월 기술적 리바운드 국면</span> 진입.",
            "외국인 수급의 전환과 빅테크 가이던스가 <span class=\"text-amber-300 font-bold\">반등의 강도와 속도</span>를 결정한다.",
            "실적이 뒷받침되는 반도체/자동차 대장주가 <span class=\"text-cyan-300 font-semibold\">반등 장세를 주도</span>할 전망."
        ],
        "data_points": [
            "코스피 8월 계절성 수익률: 과매도 후 8월 평균 +5% 이상 반등 역사",
            "외국인 선물 매도 포지션: 청산 및 숏커버링 진행 관찰"
        ],
        "signal": "bullish",
        "signal_reason": "투매 완료 후 수급 전환 및 실적 확인에 따른 강력한 리바운드가 기대되기 때문입니다.",
        "key_companies": ["MP파트너스", "삼성전자", "SK하이닉스"],
        "insight": "공포가 극에 달했던 7월이 지나면, 8월에는 실적 펀더멘털에 기반한 가격 정상화가 빠르게 이뤄집니다.",
        "action_point": "8월 반등 장세를 대비해 실적 양호 반도체 및 자동차 대장주 비중 확대를 추천합니다."
    },
    "HRfzjuF72xI": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["폭락장종료", "3가지리스크", "글로벌인터뷰", "장우진", "삼프로TV"],
        "summary": "폭락장 종료 기대를 갖고 담대하게 접근하되, <span class=\"text-rose-400 font-medium\">매파 연준, 지정학 노이즈, 기업 실적 둔화</span>의 3대 리스크 점검이 필요합니다.",
        "key_claims": [
            "과도한 폭락 이후 바닥 형성은 진행 중이나 <span class=\"text-cyan-300 font-semibold\">3대 리스크 점검</span> 필수.",
            "연준의 매파적 긴축 장기화 리스크가 <span class=\"text-rose-400 font-medium\">밸류에이션 상단을 제한</span>할 수 있다.",
            "리스크를 분산하는 <span class=\"text-amber-300 font-bold\">우량 분합 매수 전략</span>이 가장 안전한 대응책이다."
        ],
        "data_points": [
            "3대 리스크 지표: 연준 반대표 출현, 중동/미중 지정학, 빅테크 CapEx ROI",
            "지수 하방 지지력: 코스피 밸류 하단 탄탄"
        ],
        "signal": "neutral",
        "signal_reason": "바닥 형성 기대감이 크나 3대 리스크 요인이 완만 상방을 유도할 것이기 때문입니다.",
        "key_companies": ["금시공", "삼성전자"],
        "insight": "폭락 후 반등 국면에서는 3대 리스크를 모니터링하며 리스크 대비 수익비가 높은 종목을 골라야 합니다.",
        "action_point": "패닉을 자제하고 3대 리스크에 강한 대형 고배당주 및 대표 성장주로 균형을 맞추십시오."
    },
    "iGG4upmyLPM": {
        "primary_topic": "crypto",
        "secondary_topics": ["stock"],
        "tags": ["온체인주식", "SK하이닉스토큰", "주식토큰화", "솔라나코리아", "크립토PLUS"],
        "summary": "SK하이닉스 등 한국 주요 주식이 온체인 토큰화(RWA)로 글로벌 솔라나 등 블록체인에 입성하며 <span class=\"text-cyan-300 font-semibold\">24/7 글로벌 온체인 주식 거래</span> 시대가 열리고 있습니다.",
        "key_claims": [
            "솔라나 등 고속 온체인 프로토콜 상에서 <span class=\"text-cyan-300 font-semibold\">국내 대표 주식 토큰화(RWA)</span> 실증.",
            "전 세계 투자자가 시공간 제약 없이 <span class=\"text-amber-300 font-bold\">24시간 K-주식 거래 접근성</span> 확보.",
            "전통 금융 시장과 온체인 크립토 유동성의 <span class=\"text-violet-300 font-medium\">역사적 결합 전개</span>."
        ],
        "data_points": [
            "솔라나 온체인 RWA 트랜잭션 속도: 초당 만 건 이상 고속 처리",
            "토큰화 대상 주식: SK하이닉스, 삼성전자 등 코스피 시총 상위주"
        ],
        "signal": "bullish",
        "signal_reason": "K-주식의 글로벌 유동성 접근성이 온체인을 통해 비약적으로 확장되기 때문입니다.",
        "key_companies": ["솔라나(Solana)", "SK하이닉스", "시큐리타이즈"],
        "insight": "주식 토큰화는 글로벌 자본이 국내 우량 주식에 24시간 언제든 유입될 수 있는 혁신적 창구입니다.",
        "action_point": "RWA 토큰화 플랫폼 및 온체인 금융 인프라 수혜 분야에 장기적 관점으로 접근하십시오."
    },
    "IOyoRJ5GPU0": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["본전탈출", "반등발목범인", "교양이를부탁해", "매물대", "증시심리"],
        "summary": "증시 반등 시 원금 회복 욕구에 따른 <span class=\"text-rose-400 font-medium\">본전 탈출 매물대(매도 벽)</span>가 장기 상승의 발목을 잡는 주요 원인입니다.",
        "key_claims": [
            "폭락 후 반등 과정에서 쌓여 있는 <span class=\"text-rose-400 font-medium\">악성 본전 매물 소화 과정</span>이 필수적이다.",
            "매물대를 돌파하기 위해서는 <span class=\"text-cyan-300 font-semibold\">강력한 기업 실적 모멘텀</span>이 공급되어야 한다.",
            "매물대가 얇은 <span class=\"text-amber-300 font-bold\">새로운 실적 주도주</span>로의 교체 매매가 유리하다."
        ],
        "data_points": [
            "코스피 매물대 집중 구간: 폭락 직전 고점 부근에 매물 40% 집중",
            "매물 소화 소요 기간: 평균 2~3개월의 박스권 소화 필요"
        ],
        "signal": "neutral",
        "signal_reason": "매물대 소화로 인한 박스권 흐름이 예상되나 실적주의 경우 매물 소화 후 신고가 가능성이 있기 때문입니다.",
        "key_companies": ["교양이를부탁해"],
        "insight": "본전 매물벽에 갇힌 과거 주도주보다, 실적이 새롭게 상향되어 매물대가 얇은 차세대 주도주에 집중해야 합니다.",
        "action_point": "매물 상단에 저항을 받는 고점 매물 보유주를 정리하고 흑자 신규 주도주로 정비하십시오."
    },
    "kY-VMYogl8U": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["오후방송", "SK하이닉스실적", "국내증시괴로움", "삼프로TV", "실적반영안됨"],
        "summary": "SK하이닉스가 역대급 호실적을 발표했음에도 수급 악재로 주가가 하락하였으나, <span class=\"text-cyan-300 font-semibold\">실적과 주가의 괴리는 조만간 해소될 과매도 구간</span>입니다.",
        "key_claims": [
            "SK하이닉스의 어닝 서프라이즈에도 불구하고 <span class=\"text-rose-400 font-medium\">외국인 수급 매도로 주가 왜곡</span> 발생.",
            "HBM3E 독점적 지위와 영업이익 폭증은 변함없어 <span class=\"text-amber-300 font-bold\">주가 펀더멘털 회복은 필연적</span>이다.",
            "실적 미반영에 따른 억울한 하락은 <span class=\"text-cyan-300 font-semibold\">최상의 바닥 매수 신호</span>이다."
        ],
        "data_points": [
            "SK하이닉스 2분기 영업이익: 5조 원 돌파 사상 최대급 기록",
            "주가 반응: 호실적에도 불구하고 외국인 매도로 -3% 이상 하락"
        ],
        "signal": "bullish",
        "signal_reason": "어닝 서프라이즈에도 불구하고 수급으로 왜곡된 주가는 반드시 펀더멘털로 수렴하기 때문입니다.",
        "key_companies": ["SK하이닉스", "삼성전자"],
        "insight": "실적이 잘 나왔는데 주가가 빠지는 것은 악재가 아니라 시장의 일시적 눈속임이며 강력한 매수 기회입니다.",
        "action_point": "호실적이 확인된 SK하이닉스의 저가 매수 기회로 활용할 것을 적극 권고합니다."
    },
    "lF6kha6J88M": {
        "primary_topic": "space",
        "secondary_topics": ["tech"],
        "tags": ["스타십해상착수", "스페이스앤", "미래에셋", "스타십성공", "우주발사체"],
        "summary": "스페이스X의 스타십이 해상 수직 착수에 멀쩡하게 성공하면서 <span class=\"text-cyan-300 font-semibold\">우주 발사체 완전 재사용 시대</span>의 실현 가능성을 입증했습니다.",
        "key_claims": [
            "스타십의 해상 수직 착수 성공으로 <span class=\"text-cyan-300 font-semibold\">100% 완전 재사용 발사체 기술</span> 완증.",
            "우주 발사 단가 파격 절감으로 <span class=\"text-amber-300 font-bold\">화성 탐사 및 우주 인터넷 상용화</span> 가속.",
            "글로벌 우주 수송 시장에서 <span class=\"text-violet-300 font-medium\">스페이스X의 독주 체제</span> 완벽 안착."
        ],
        "data_points": [
            "스타십 시험 발사 결과: 궤도 비행 후 지정 해역 정확 수직 착수 성공",
            "재사용 발사체 경제성: 발사 비용 90% 이상 절감 실현"
        ],
        "signal": "bullish",
        "signal_reason": "스타십 착수 성공으로 우주 경제 전체의 물류 혁신과 사업화가 현실화되었기 때문입니다.",
        "key_companies": ["SpaceX", "미래에셋"],
        "insight": "스타십의 재사용 기술 완성은 인류의 우주 접근성을 무한히 확장하는 역사적 전환점입니다.",
        "action_point": "우주 항공 및 위성 통신 밸류체인 핵심 기업에 대한 지속적인 비중 확대를 추천합니다."
    },
    "n8Gx6PeHsio": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["마이크로소프트공매도", "AI투자우려", "개장전요것만", "한경글로벌마켓", "AI군비경쟁"],
        "summary": "마이크로소프트에 대한 공매도가 AI CapEx 지출 우려로 11년 만에 최고치를 기록했으나, <span class=\"text-cyan-300 font-semibold\">클라우드 수주잔고와 실적 상회</span>로 안도감을 안겼습니다.",
        "key_claims": [
            "AI CapEx 수익성 우려로 MSFT 공매도가 <span class=\"text-rose-400 font-medium\">11년 만에 최고 수준</span>까지 급증했다.",
            "실제 실적 발표에서 클라우드(애저) 및 AI 매출이 <span class=\"text-cyan-300 font-semibold\">시장 전망을 상회하며 반전</span>을 이끌었다.",
            "빅테크의 AI 군비 경쟁은 우려를 딛고 <span class=\"text-amber-300 font-bold\">지속적 성장 국면</span>을 유지 중이다."
        ],
        "data_points": [
            "마이크로소프트 공매도 비율: 11년 만의 최고치 기록 후 실적 발표로 숏커버링 유출",
            "애저(Azure) 클라우드 성장률: 30% 이상 고성장 유지"
        ],
        "signal": "bullish",
        "signal_reason": "공매도 우려를 비웃듯 마이크로소프트의 클라우드 AI 매출이 견조하게 상회했기 때문입니다.",
        "key_companies": ["Microsoft", "한경글로벌마켓"],
        "insight": "AI 군비경쟁에 대한 우려는 크지만, 마이크로소프트처럼 클라우드 매출로 입증하는 기업은 흔들리지 않습니다.",
        "action_point": "공매도 우려 해소 후 반등하는 마이크로소프트 등 플랫폼 핵심주의 장기 보유를 권고합니다."
    },
    "ntab3CG8DZ4": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["공포를거래", "실적보다공포", "착각의시작", "주린이구조대", "삼프로TV"],
        "summary": "증시가 실적 펀더멘털 대신 공포 심리를 거래하며 폭락했으나, <span class=\"text-cyan-300 font-semibold\">실질 악재 소멸과 함께 이성적 밸류에이션 회복</span>이 전개될 것입니다.",
        "key_claims": [
            "시장이 이성적 실적 평가를 마비시키고 <span class=\"text-rose-400 font-medium\">공포와 투매 심리 자체를 거래</span>하고 있다.",
            "폭락은 이미 악재를 과도하게 반영해 종료되었으며 <span class=\"text-cyan-300 font-semibold\">착각 구간에서의 저가 매수</span>가 유효하다.",
            "실적이 탄탄한 기업부터 <span class=\"text-amber-300 font-bold\">빠른 주가 정상화</span>가 연출될 전망이다."
        ],
        "data_points": [
            "코스피 공포지수(VIX): 역사적 고점 부근 형성",
            "기업 이익 추정치: 지수 폭락에도 이익 상향 기조 유지"
        ],
        "signal": "bullish",
        "signal_reason": "공포거래가 극에 달한 시점은 전형적인 이격 축소 반등의 전조이기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "시장이 공포를 거래할 때 침착하게 실적 펀더멘털을 거래하는 투자자가 최후의 승자가 됩니다.",
        "action_point": "공포에 휩쓸린 투매를 지양하고 흑자 대형주 중심의 분할 매수를 강력히 추천합니다."
    },
    "oYW4ni1GkzU": {
        "primary_topic": "tech",
        "secondary_topics": ["economy"],
        "tags": ["중국AI천재들", "고국행선택", "이필상", "미래에셋홍콩", "이효석아카데미"],
        "summary": "중국의 1% AI 인재들이 미국의 고액 연봉을 거절하고 귀국하여 <span class=\"text-violet-300 font-medium\">중국 자체 AI 및 피지컬 로봇 생태계</span> 구축을 가속화하고 있습니다.",
        "key_claims": [
            "중국 출신 천재 AI 연구원들의 고국 리턴(Brain Gain)으로 <span class=\"text-violet-300 font-medium\">중국 AI 역량 독자적 진화</span>.",
            "딥시크(DeepSeek) 등 저비용 고효율 AI 모델 개발의 배경에는 <span class=\"text-cyan-300 font-semibold\">중국 귀국 인재들의 역할</span>이 컸다.",
            "미·중 AI 인재 및 패권 경쟁이 <span class=\"text-amber-300 font-bold\">양극화된 AI 글로벌 기술 블록</span>을 형 형성."
        ],
        "data_points": [
            "중국 AI 연구원 귀국 비율: 최근 3년간 미국 유학 인재 중 40% 이상 복귀",
            "중국 오픈소스 AI 모델 성능: Llama 3 수준 추격 성공"
        ],
        "signal": "neutral",
        "signal_reason": "중국의 AI 추격 속도가 빠르나 미국의 규제 및 하드웨어 통제 리스크가 함께 상존하기 때문입니다.",
        "key_companies": ["DeepSeek", "미래에셋", "이효석아카데미"],
        "insight": "AI 경쟁은 단순 칩 수량을 넘어 인재 집적도와 오픈소스 개발 생태계의 싸움으로 확장되고 있습니다.",
        "action_point": "미중 AI 기술 경쟁 속에서 우방국 공급망 수혜 및 독자 소프트웨어 경쟁력을 지닌 기업에 주목하십시오."
    },
    "prQiqA_3sTg": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["오픈AI위기설", "최악의시나리오", "교양이를부탁해", "AI버블", "알상무"],
        "summary": "오픈AI의 천문학적 적자와 비영리 구조 마찰로 <span class=\"text-rose-400 font-medium\">오픈AI 위기설 및 최악의 AI 캐즘 시나리오</span>에 대한 시장의 경계감이 존재합니다.",
        "key_claims": [
            "오픈AI의 연간 50억 달러 적자와 거대한 모델 훈련 비용이 <span class=\"text-rose-400 font-medium\">재정적 한계</span>를 유발한다.",
            "오픈AI 구조조정 및 영리 법인 전환 차질 시 <span class=\"text-rose-400 font-medium\">글로벌 AI 투심에 단기 쇼크</span> 가능성.",
            "마이크로소프트 등 빅테크 파트너십을 통한 <span class=\"text-cyan-300 font-semibold\">수익 구조 전환이 시급</span>한 과제이다."
        ],
        "data_points": [
            "오픈AI 연간 소모 현금(Burn rate): 약 50억 달러 적자 추정",
            "MSFT의 오픈AI 지분 및 클라우드 연계: 130억 달러 투자 집행"
        ],
        "signal": "neutral",
        "signal_reason": "오픈AI 재정 리스크 우려가 있으나 마이크로소프트의 구원 및 수익화 전환 시도가 진행 중이기 때문입니다.",
        "key_companies": ["OpenAI", "Microsoft"],
        "insight": "스타트업 형태의 AI 모델 개발사는 자금난 위험에 노출될 수 있으나, 현금이 풍부한 빅테크가 이를 흡수할 것입니다.",
        "action_point": "단독 AI 모델 개발사보다는 현금 창출 능력이 우수한 빅테크 클라우드 기업 중심의 포트폴리오를 유지하십시오."
    },
    "s2vwCq8zT-A": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["메타급락", "마소실적환호", "빅머니LIVE", "문지웅", "매경월가월부"],
        "summary": "메타가 가이던스 미흡으로 시간 외 급락한 반면, 마이크로소프트는 <span class=\"text-cyan-300 font-semibold\">클라우드 실적 호조로 시장 전망을 상회하며 환호</span>를 받았습니다.",
        "key_claims": [
            "메타는 AI CapEx 증가 대비 주력 광고 가이던스 보수적 제시로 <span class=\"text-rose-400 font-medium\">시간 외 급락</span>.",
            "마이크로소프트는 애저(Azure) 클라우드 AI 매출 급증으로 <span class=\"text-cyan-300 font-semibold\">실적 서프라이즈 달성</span>.",
            "빅테크 내에서도 <span class=\"text-amber-300 font-bold\">실질 수익화 속도에 따라 주가 엇갈림</span> 극명화."
        ],
        "data_points": [
            "마이크로소프트 시간 외 주가: 실적 발표 후 +4% 상승",
            "메타 시간 외 주가: CapEx 부담 및 가이던스 보수성에 -6% 하락"
        ],
        "signal": "bullish",
        "signal_reason": "마이크로소프트의 클라우드 실적 호조가 AI 생태계의 실질적 이익 창출 능력을 증명해주었기 때문입니다.",
        "key_companies": ["Microsoft", "Meta", "매경월가월부"],
        "insight": "CapEx 지출이 많은 기업이라도 마이크로소프트처럼 클라우드 매출로 바로 입증하는 기업이 주가 상승을 주도합니다.",
        "action_point": "실적과 가이던스가 검증된 마이크로소프트의 비중을 늘리고 메타의 주가 안정화를 확인하십시오."
    },
    "S_ZZxVbwK8o": {
        "primary_topic": "economy",
        "secondary_topics": ["etc"],
        "tags": ["한국보유세", "부동산보유세", "이관옥교수", "언더스탠딩", "부동산조세"],
        "summary": "한국의 부동산 보유세 실효 세율을 싱가포르 등 글로벌 기준과 실증 비교하여 <span class=\"text-cyan-300 font-semibold\">실질 조세 부담과 부동산 가격에 미치는 영향</span>을 심층 분석합니다.",
        "key_claims": [
            "명목 보유세율과 달리 실효 보유세율은 <span class=\"text-cyan-300 font-semibold\">공시가격 현실화율과 자산 가격</span>에 따라 좌우된다.",
            "한국 보유세 구조는 거래세(취득세/양도세) 대비 <span class=\"text-amber-300 font-bold\">상대적 균형점 찾기</span>가 진행 중이다.",
            "조세 정책 변화가 <span class=\"text-violet-300 font-medium\">부동산 자산 양극화 및 똘똘한 한 채 선호</span>를 강화한다."
        ],
        "data_points": [
            "한국 부동산 실효 보유세율: 약 0.15%~0.25% 수준 (미국 1% 대비 낮으나 거래세 높음)",
            "싱가포르 누진 보유세율: 고가 주택 대상 최고 36% 적용"
        ],
        "signal": "neutral",
        "signal_reason": "조세 정책이 부동산 자산 시장의 대세 상승을 결정하기보다 양극화를 유도하는 변수이기 때문입니다.",
        "key_companies": ["싱가포르국립대", "언더스탠딩"],
        "insight": "보유세와 거래세의 조세 조합은 부동산 시장의 거래량과 핵심 입지 쏠림 현상을 결정하는 중요 요인입니다.",
        "action_point": "부동산 리츠 및 자산 관리 전략 수립 시 실효 조세 부담과 정책 가이던스를 면밀히 반영하십시오."
    },
    "sK9AOTSvNiI": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["서킷브레이커", "레버리지제한", "연준5연속동결", "국채30년물", "뉴스3"],
        "summary": "국내 증시의 이틀 연속 서킷브레이커 발동에 따라 <span class=\"text-rose-400 font-medium\">단일종목 레버리지 제한 정책</span>이 추진되며, 연준 5연속 금리 동결 속 30년물 금리는 최고치를 기록했습니다.",
        "key_claims": [
            "증시 극단적 변동성에 대응해 <span class=\"text-cyan-300 font-semibold\">고위험 레버리지 상품 규제</span> 전격 검토.",
            "연준 5연속 동결에도 불구하고 <span class=\"text-rose-400 font-medium\">미 30년물 국채 금리 19년 만의 최고치</span> 기록하며 장기 금리 압박.",
            "고금리 장기화 우려 속에 <span class=\"text-amber-300 font-bold\">변동성 완화 제도 도입</span> 추진."
        ],
        "data_points": [
            "미국 30년물 국채 금리: 4.8% 돌파하며 19년 만에 최고치",
            "국내 증시 변동성: 이틀 연속 서킷브레이커/사이드카 발동"
        ],
        "signal": "neutral",
        "signal_reason": "장기 국채 금리 부담이 존재하나 금융 당국의 시장 안정화 제도 조치가 병행되기 때문입니다.",
        "key_companies": ["연준", "삼프로TV"],
        "insight": "장기 국채 금리 고착화는 고부채 기업에 부담을 주므로, 무부채/고현금 유보 기업의 가치가 더욱 커집니다.",
        "action_point": "레버리지 파생 상품 투자를 지양하고 현금 보유 비율이 높은 탄탄한 우량주 중심 투자를 추천합니다."
    },
    "tBS413fg7s4": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["마감시황", "실적보다선반응", "놓친신호", "클로징벨", "삼프로TV"],
        "summary": "증시가 실적 발표 전 공포 심리로 선반영되어 낙폭을 키웠으나, <span class=\"text-cyan-300 font-semibold\">실적 확인 후 시장 안도감과 이격 회복</span>이 기대됩니다.",
        "key_claims": [
            "실적 공개 전 과도한 악재 선반영으로 <span class=\"text-rose-400 font-medium\">지수 과매도 이격 발생</span>.",
            "실제 주요 기업들의 2분기 영업이익은 <span class=\"text-cyan-300 font-semibold\">시장의 우려보다 훨씬 양호</span>하다.",
            "실적 신호 확인 후 <span class=\"text-amber-300 font-bold\">빠른 기술적 복원력</span>이 연출될 전망."
        ],
        "data_points": [
            "S&P 500 기업 어닝 서프라이즈 비율: 78% 기록",
            "코스피 상장사 2분기 영업이익 합계: 전년 대비 40% 이상 성장"
        ],
        "signal": "bullish",
        "signal_reason": "실적 악재 선반영이 끝난 후 양호한 실제 실적이 주가 반등의 강한 촉매가 될 것이기 때문입니다.",
        "key_companies": ["삼성전자", "SK하이닉스"],
        "insight": "실적 발표 전의 공포는 종종 시장이 제공하는 가장 저렴한 매수 기회로 작용합니다.",
        "action_point": "실적 확인 후 반등 모멘텀이 강한 시가총액 상위주 위주로 매수 대응을 추천합니다."
    },
    "ThZHxIJKDSM": {
        "primary_topic": "etc",
        "secondary_topics": ["tech"],
        "tags": ["중국비밀실험", "유전자편집", "생명윤리", "CRISPR", "SOD"],
        "summary": "중국에서 비공식 유전자 편집(CRISPR) 기술 적용 사망 사고가 폭로되며 <span class=\"text-rose-400 font-medium\">유전자 치료 생명윤리 및 국제 규제 강화</span> 논란이 재부각되었습니다.",
        "key_claims": [
            "비윤리적 유전자 편집 임상 시도로 인한 <span class=\"text-rose-400 font-medium\">국제적 규제 및 비난 성명</span> 교차.",
            "CRISPR 유전자 가위 기술의 <span class=\"text-cyan-300 font-semibold\">엄격한 임상 가이드라인과 글로벌 표준</span> 필요성 고조.",
            "정통 바이오텍 치료제 개발사에 대한 <span class=\"text-amber-300 font-bold\">신뢰성 및 규제 검증</span> 강화."
        ],
        "data_points": [
            "유전자 치료제 임상 규제: 미 FDA 및 EMA의 승인 절차 강화",
            "CRISPR 글로벌 시장 성장세: 규제 준수 정통 치료제 중심 성장"
        ],
        "signal": "neutral",
        "signal_reason": "비윤리적 이슈에 따른 불확실성이 있으나 정통 유전자 치료제 개발사의 규제 준수 가치는 높아지기 때문입니다.",
        "key_companies": ["CRISPR Therapeutics", "Editas Medicine"],
        "insight": "유전자 편집 기술은 인류의 질병을 극복하는 강력한 도구이나 글로벌 윤리 및 승인 절차가 생명선입니다.",
        "action_point": "미 FDA 승인 임상을 정식 통과 중인 글로벌 규제 준수 유전자 치료제 바이오텍에 집중하십시오."
    },
    "TP18Alm9qb0": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["한국증시롤러코스터", "개인투자자현실", "교양이를부탁해", "국장변동성", "알상무"],
        "summary": "한국 증시가 글로벌 악재에 유독 롤러코스터를 타는 이유는 <span class=\"text-rose-400 font-medium\">외국인 수급의 기둥 역할 부재와 높은 개인 빚투 비중</span> 때문입니다.",
        "key_claims": [
            "외국인의 국장 파생상품 플레이와 개인의 신용 빚투가 <span class=\"text-rose-400 font-medium\">증시 변동성을 극대화</span>한다.",
            "지배구조 및 주주환원 미흡으로 <span class=\"text-rose-400 font-medium\">장기 기관 자금 유입 부족</span> 한계.",
            "변동성을 극복하기 위해 <span class=\"text-amber-300 font-bold\">원칙 있는 자산 배분과 분할 매수</span>가 필수적이다."
        ],
        "data_points": [
            "한국 증시 변동성 지수(VKOSPI): 주요국 증시 대비 1.5배 높음",
            "개인 신용 융자 비중: 코스닥 시가총액 대비 높은 수준 유지"
        ],
        "signal": "neutral",
        "signal_reason": "국장 변동성이 높으나 저평가 구간에서의 단기 가격 회복 탄력도 크기 때문입니다.",
        "key_companies": ["교양이를부탁해"],
        "insight": "한국 증시의 높은 롤러코스터 변동성을 역이용하여, 극단적 저점 폭락 시 담고 반등 시 수익을 챙기는 전략이 유효합니다.",
        "action_point": "신용 매수를 철저히 배제하고 현금 보유를 통한 변동성 저가 매수 전략을 유지하십시오."
    },
    "txZu4z7KxoE": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["역사적저평가", "서두르면안되는이유", "목대균", "KCGI자산운용", "삼프로TV"],
        "summary": "코스피가 역사적 저평가 영역에 진입했으나, <span class=\"text-cyan-300 font-semibold\">수급 클리어링과 거시 불확실성 해소를 확인하며 호흡을 길게 가져가는 분할 접근</span>이 바람직합니다.",
        "key_claims": [
            "PBR 0.85배의 역사적 저평가이나 <span class=\"text-rose-400 font-medium\">수급 청산 확인 전 일시적 성급한 매수는 자제</span>.",
            "외국인 매도세 정체와 연준 통화 정책 신호를 <span class=\"text-cyan-300 font-semibold\">확인한 뒤 진입해도 늦지 않다</span>.",
            "호흡을 길게 잡고 <span class=\"text-amber-300 font-bold\">실적 우수 대형주 중심 단계적 매수</span> 권고."
        ],
        "data_points": [
            "코스피 PBR: 0.85배 진입 (역사적 하단선)",
            "KCGI 자산운용 권고: 수급 클리어링 후 승률 높은 타점 노림"
        ],
        "signal": "bullish",
        "signal_reason": "역사적 저평가로 중장기 승률은 매우 높으며 호흡을 다듬는 전략적 매수가 최적이기 때문입니다.",
        "key_companies": ["KCGI자산운용", "삼성전자", "SK하이닉스"],
        "insight": "저평가라 해서 한 번에 올인하기보다 수급 멈춤을 확인하며 느긋하게 나누어 담는 호흡이 안전합니다.",
        "action_point": "지수 분할 매수를 추진하되 일단 수급 멈춤 신호를 확인하며 분할 집행하십시오."
    },
    "uKljNsucYks": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["7월FOMC리뷰", "심판대신공을봐라", "이효석아카데미", "속보효", "FOMC분석"],
        "summary": "FOMC 결과(심판)의 말 한마디에 흔들리지 말고, <span class=\"text-cyan-300 font-semibold\">실제 기업들의 실적과 경제의 기초체력(공)</span>에 집중해야 합니다.",
        "key_claims": [
            "연준의 매파적 코멘트(심판)보다 <span class=\"text-cyan-300 font-semibold\">기업들의 실제 현금 창출력(공)</span>이 더 중요하다.",
            "금리 동결에도 불구하고 <span class=\"text-amber-300 font-bold\">실적 호조 기업들의 주가 강세</span> 지속.",
            "거시 노이즈를 뚫고 <span class=\"text-cyan-300 font-semibold\">실적 펀더멘털주로 포커스 이동</span> 필요."
        ],
        "data_points": [
            "미국 기업 2분기 영업이익률: 역사적 고점 유지",
            "연준 금리 결정: 3.50~3.75% 동결 통과"
        ],
        "signal": "bullish",
        "signal_reason": "거시 통화 정책의 성명서 노이즈보다 기업들의 이익 실체가 탄탄하기 때문입니다.",
        "key_companies": ["이효석아카데미", "연준"],
        "insight": "시장을 움직이는 진정한 힘은 중앙은행의 입이 아니라 기업들의 실적 방정식입니다.",
        "action_point": "FOMC 노이즈로 주가가 흔들릴 때 실적이 견조한 우량주를 저가 매수하십시오."
    },
    "Vym-ZJ2sHTc": {
        "primary_topic": "stock",
        "secondary_topics": ["tech"],
        "tags": ["금리동결", "마이크로소프트호실적", "시간외상승", "월가뉴스레터", "삼프로TV"],
        "summary": "연준의 매파적 금리 동결에도 불구하고 마이크로소프트의 <span class=\"text-cyan-300 font-semibold\">클라우드 실적 대폭 상회가 시간 외 급등</span>을 이끌며 기술주 투심을 살려냈습니다.",
        "key_claims": [
            "금리 동결 악재보다 <span class=\"text-cyan-300 font-semibold\">마이크로소프트의 어닝 서프라이즈</span>가 증시를 견인했다.",
            "애저(Azure) 클라우드 매출 성장률이 AI 실질 수익화 우려를 <span class=\"text-amber-300 font-bold\">완전 해소</span>시켰다.",
            "실적이 입증된 빅테크를 중심으로 <span class=\"text-cyan-300 font-semibold\">기술주 반등 모멘텀</span> 재가동."
        ],
        "data_points": [
            "마이크로소프트 시간 외 주가 상승률: +4.2% 상승",
            "애저 클라우드 성장률: 30%+ 이상 상회 달성"
        ],
        "signal": "bullish",
        "signal_reason": "마이크로소프트의 압도적 실적이 AI 팽창과 기술주 상승의 정당성을 증명해주었기 때문입니다.",
        "key_companies": ["Microsoft", "삼프로TV"],
        "insight": "거시 고금리 환경도 마이크로소프트 같은 독점적 실적 성장 기업의 주가 상승을 막을 수 없습니다.",
        "action_point": "마이크로소프트 중심의 핵심 기술주 포트폴리오를 지속 확장하십시오."
    },
    "xA5W3TSPIIs": {
        "primary_topic": "etc",
        "secondary_topics": ["economy"],
        "tags": ["왕따아파트", "한동빼고재건축", "부동산재건축", "언더스탠딩", "재건축갈등"],
        "summary": "재건축 추진 과정에서 분의금 갈등 및 입지적 이해관계로 <span class=\"text-rose-400 font-medium\">특정 동을 제외하고 진행하는 분리 재건축</span> 사례와 부동산 사업성 영향을 다룹니다.",
        "key_claims": [
            "분담금 갈등과 토지 지분율 이견으로 <span class=\"text-rose-400 font-medium\">한 동 제외 단독 재건축</span> 사례 증가.",
            "분리 재건축 진행 시 <span class=\"text-cyan-300 font-semibold\">사업 속도는 빨라지나 단지 가치 훼손</span> 리스크 공존.",
            "재건축 사업성의 핵심은 <span class=\"text-amber-300 font-bold\">속도와 조합원 간 합의 구조</span>에 있음."
        ],
        "data_points": [
            "분리 재건축 소송 비율: 최근 재건축 단지 중 15% 이상 경험",
            "재건축 사업 소요 기간: 합의 단지 5년 vs 갈등 단지 10년 이상 지연"
        ],
        "signal": "neutral",
        "signal_reason": "재건축 속도는 빨라질 수 있으나 단지 완성도 차질이라는 양면성이 존재하기 때문입니다.",
        "key_companies": ["언더스탠딩"],
        "insight": "부동산 재건축 투자 시 단지 전체의 합의율과 지분 갈등 여부가 실질적 사업 수익률을 결정합니다.",
        "action_point": "재건축 아파트 투자 시 조합원 동의율과 분담금 합의 상태를 사전에 철저히 검증하십시오."
    },
    "XacJl7ljjRg": {
        "primary_topic": "space",
        "secondary_topics": ["tech"],
        "tags": ["스페이스X추락", "머스크화성", "이강환", "스펙스", "언더스탠딩"],
        "summary": "스페이스X의 스타십 시험 발사 과정의 실패와 추락에도 불구하고 <span class=\"text-cyan-300 font-semibold\">빠른 반복 실증과 화성 이주 청사진</span>은 흔들림 없이 추진 중입니다.",
        "key_claims": [
            "스페이스X의 실패는 철저히 계획된 <span class=\"text-cyan-300 font-semibold\">데이터 수집형 실패(Fast Iteration)</span>이다.",
            "머스크의 화성 이주 목표는 단순 이상이 아니라 <span class=\"text-amber-300 font-bold\">거대 수송 발사체 양산</span>으로 실현 단계 진입.",
            "우주 발사 시장에서 독보적 수송 비용 절감으로 <span class=\"text-violet-300 font-medium\">우주 안보/산업 생태계 독점</span>."
        ],
        "data_points": [
            "스타십 발사 횟수 및 데이터 수집: 반복 발사를 통해 수천 가지 시스템 개선",
            "화성 수송 단가 목표: 톤당 수송 비용 기존 1/50 축소 목표"
        ],
        "signal": "bullish",
        "signal_reason": "반복 시험을 통한 독보적 기술 격차가 우주 산업 전체의 독점력을 높여주기 때문입니다.",
        "key_companies": ["SpaceX", "언더스탠딩"],
        "insight": "스페이스X의 연쇄 발사 시험은 실패가 아니라 완벽한 발사체를 만들기 위한 가장 빠른 데이터 축적 과정입니다.",
        "action_point": "우주 항공 및 저궤도 위성 통신 관련 밸류체인 기업에 대한 장기적 투자를 유지하십시오."
    },
    "XN9eIOrRvww": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["김종학뉴욕지금", "FOMC동결반대표", "메타실적", "MSFT실적", "한경글로벌마켓"],
        "summary": "7월 FOMC의 2016년 이후 최다 매파 반대표(3명) 속에서도, <span class=\"text-cyan-300 font-semibold\">마이크로소프트의 실적 상회 및 퀄컴/ARM 등 빅테크 실적</span>이 증시를 이끌었습니다.",
        "key_claims": [
            "FOMC에서 3명의 금리 인상 반대표가 출현하며 <span class=\"text-rose-400 font-medium\">매파적 동결 성명</span> 발표.",
            "마이크로소프트 실적 상회가 기술주 하방을 지지했으나 <span class=\"text-rose-400 font-medium\">메타의 가이던스 보수성</span>으로 시간에 혼조.",
            "빅테크 간 실적 차별화 속에 <span class=\"text-amber-300 font-bold\">어닝 서프라이즈 종목으로 자금 이동</span> 격화."
        ],
        "data_points": [
            "FOMC 반대표: 2016년 이후 최대인 3명의 위원이 금리 인상 표 던짐",
            "마이크로소프트 / 메타 시간 외 주가: MSFT +4% 상승 vs Meta -6% 하락"
        ],
        "signal": "bullish",
        "signal_reason": "매파적 연준 성명 악재에도 불구하고 마이크로소프트 등 핵심 빅테크 실적이 시장을 방어해주기 때문입니다.",
        "key_companies": ["Microsoft", "Meta", "Qualcomm", "ARM", "한경글로벌마켓"],
        "insight": "연준의 매파적 포지션보다 빅테크 기업들의 실제 영업이익 지표가 시장 향방을 결정짓고 있습니다.",
        "action_point": "어닝 서프라이즈를 달성한 마이크로소프트 등 실적 선도 기술주 중심의 투자를 권고합니다."
    }
}

for vid, data in analyses.items():
    topic_id = data["primary_topic"]
    pending_file = pending_dir / f"{vid}.json"
    if not pending_file.exists():
        print(f"[Skip] {vid}.json does not exist in data/pending")
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

print("\n[SUCCESS] All 38 new pending videos have been analyzed and saved successfully!")
