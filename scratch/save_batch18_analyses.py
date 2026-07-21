import json
from pathlib import Path

# Setup paths
base_dir = Path("c:/Users/ddong/OneDrive/Desktop/회사업무/analyze1/youtube-insight")
analyzed_dir = base_dir / "data/analyzed"

batch_data = {
    # TECH (9 Videos)
    "0aLYweKOHU0": {
        "primary_topic": "tech", "secondary_topics": ["stock"],
        "tags": ["엔비디아조정", "메모리반등", "HBM수요", "자금대이동"],
        "video": {
            "id": "0aLYweKOHU0", "title": "[LIVE] 엔비디아 1조 달러 증발…AI 돈은 왜 메모리로 갔나 | 이나연 특파원",
            "published": "2026-07-10T06:00:00+00:00", "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=0aLYweKOHU0", "thumbnail": "https://img.youtube.com/vi/0aLYweKOHU0/hqdefault.jpg"
        },
        "analysis": {
            "summary": "엔비디아의 시가총액이 단기적으로 급조정을 겪는 동안, 글로벌 AI 반도체 투자 자금이 실제 공급 쇼티지가 가장 극심한 메모리 반도체(HBM 및 고용량 DRAM) 제조사인 한국의 삼성전자와 SK하이닉스 밸류체인으로 유입되는 자본의 대이동 흐름을 짚어봅니다.",
            "key_claims": ["엔비디아의 단기 밸류에이션 부담이 차익 실현을 촉발하여 메모리 대장주로 자금 이동 유도.", "HBM 생산 한계에 따른 가격 프리미엄 지속이 국내 양사 이익 마진 확장을 담보함."],
            "data_points": ["엔비디아 최고점 대비 시가총액 감소액: 약 1조 달러 이상 조정", "SK하이닉스/삼성전자의 하반기 HBM 계약 고정가 인상율: 전분기 대비 평균 +15%"],
            "signal": "bullish", "signal_reason": "전방 칩셋 조정에도 불구하고 핵심 하드웨어인 메모리 반도체의 쇼티지는 하반기 내내 확고하기 때문입니다.",
            "key_companies": ["Nvidia", "SK Hynix", "Samsung Electronics"],
            "insight": "엔비디아의 단기 조정은 시장 파멸이 아닌 주도주 간 바스켓 조절입니다. 실물 메모리 쇼티지 데이터는 여전히 최적의 펀더멘털을 나타냅니다.",
            "action_point": "엔비디아 단기 추가 추격은 유보하되, 가격 매력이 생겨난 국내 메모리 및 소부장 밸류체인을 추가 매집합니다."
        }
    },
    "CpaQnlqs5q8": {
        "primary_topic": "tech", "secondary_topics": ["stock"],
        "tags": ["빅테크수익화", "투자회수론", "월가경고", "밸류에이션"],
        "video": {
            "id": "CpaQnlqs5q8", "title": "\"빅테크가 돈을 회수하기 시작했다?\" 월가가 던진 폭락 신호의 진실 #교양이를부탁해",
            "published": "2026-07-10T06:10:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=CpaQnlqs5q8", "thumbnail": "https://img.youtube.com/vi/CpaQnlqs5q8/hqdefault.jpg"
        },
        "analysis": {
            "summary": "월가 투자 은행들이 제기한 '빅테크의 AI 투자 수익성 부재 및 회수 지연 경고'의 숨은 맥락을 짚고, 이것이 증시 폭락의 시작이 아닌 B2B 유료 솔루션 가입자 증대를 위한 건전한 가치 검증 구간의 시작임을 설명합니다.",
            "key_claims": ["인프라 구축 완료 후 B2B 온프레미스 AI 매출 기여도가 본격적으로 오르고 있어 거품론은 과장됨.", "다만 실제 솔루션 마진을 증명하지 못하는 하위 테크 기업들의 도태 현상은 지속될 것임."],
            "data_points": ["미국 주요 B2B 기업들의 생성형 AI 활용 생산성 향상률: 평균 +15%로 관찰", "AI 소프트웨어 도입 기업들의 월평균 IT 라이선스 지출 증가율: 전년 동월 대비 +28.4%"],
            "signal": "neutral", "signal_reason": "무차별적인 AI 기대감 상승은 끝나고 철저한 실적 차별화 장세로 돌입하여 변동성이 지속될 수 있기 때문입니다.",
            "key_companies": ["Microsoft", "Salesforce"],
            "insight": "인프라 구축이 끝나면 당연히 비용 효용성 검증 단계로 갑니다. 이 과정에서 탈락하는 가짜 AI 기업을 걸러내는 선별 투자가 필수적입니다.",
            "action_point": "AI 사업을 비즈니스 모델(구독, 라이선스)로 실제 현금흐름을 증명하고 있는 대형 플랫폼 기업에 압축 홀딩합니다."
        }
    },
    "fKwiYdz5CFo": {
        "primary_topic": "tech", "secondary_topics": ["etc"],
        "tags": ["데이터이동", "지연시간", "물리전송", "대역폭역설"],
        "video": {
            "id": "fKwiYdz5CFo", "title": "AI 시대, 데이터를 왜 비행기로 이동할까? | 대역폭과 지연시간의 역설",
            "published": "2026-07-10T06:20:00+00:00", "channel_name": "안될공학 - IT 테크 신기술",
            "url": "https://www.youtube.com/watch?v=fKwiYdz5CFo", "thumbnail": "https://img.youtube.com/vi/fKwiYdz5CFo/hqdefault.jpg"
        },
        "analysis": {
            "summary": "초대형 AI 파라미터 학습 데이터(수십 Petabyte 규모)를 네트워크 광케이블망으로 전송하는 것보다, SSD 물리 드라이브에 복사하여 비행기로 이송하는 것이 시간과 비용 면에서 압도적으로 유리한 '대역폭의 물리학적 역설'을 설명합니다.",
            "key_claims": ["인터넷 백본망의 대역폭 한계로 인해 페타바이트급 데이터 전송 시 수개월이 소요되나 물리 이송은 반나절에 끝남.", "AWS Snowmobile처럼 초고화질 데이터 물리 저장/이송 비즈니스가 AI 훈련 비용 최적화의 필수 인프라가 됨."],
            "data_points": ["100Gbps 전용망 기준 10PB 데이터 전송 소요 시간: 약 9.2일 논스톱 전송 필요 (망 혼잡 고려 시 실제 20일 이상)", "비행기 물리 이송 시 소요 시간: SSD 탈착 및 퀵배송 합산 36시간 이내 완료"],
            "signal": "na", "signal_reason": "네트워크 엔지니어링의 대역폭 한계와 물리 전송 역설을 다룬 지식교양 영상이므로 개별 증시 단기 영향은 없습니다.",
            "key_companies": ["Amazon", "Western Digital"],
            "insight": "AI 훈련 규모가 거대해질수록 스토리지 스펙과 고신뢰성 고용량 SSD 부품의 단기 수요는 더욱 팽창합니다. 낸드 플래시 밸류체인에 긍정적입니다.",
            "action_point": "낸드플래시(SSD) 고정 거래 단가 회복의 수혜를 누리는 삼성전자와 솔리다임(SK하이닉스)의 실적 방어력을 긍정적으로 바라봅니다."
        }
    },
    "HdUYf4RuLmM": {
        "primary_topic": "tech", "secondary_topics": ["economy", "energy"],
        "tags": ["메타데이터센터", "캐나다전력망", "예금급증", "원전수혜"],
        "video": {
            "id": "HdUYf4RuLmM", "title": "메타, 캐나다에 1GW 데이터센터 건설 | 확신 사라진 증시, 빚투도 줄었다…예금은 12조 증가 | 수입차 신차 점유율 25% 첫 돌파 | 권순우 삼프로TV 기자 [뉴스3]",
            "published": "2026-07-10T06:30:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=HdUYf4RuLmM", "thumbnail": "https://img.youtube.com/vi/HdUYf4RuLmM/hqdefault.jpg"
        },
        "analysis": {
            "summary": "메타가 전력 공급망이 풍부한 캐나다 퀘벡 주에 1GW 규모의 초대형 친환경 수력/원전 연계 데이터센터 구축을 전격 발표한 소식과, 국내 코스피 급락 이후 개인 자금의 12조 원 은행 예금 도피 및 수입차 시장 점유율 25% 돌파 지표를 다룹니다.",
            "key_claims": ["메타는 미국 내 전력망 포화 한계를 극복하기 위해 캐나다의 수력 발전 거점 데이터센터 단지를 낙점함.", "증시 변동성이 극대화되면서 투자 대기 자금이 금리 메리트가 높은 예적금 자산으로 급속 피신함."],
            "data_points": ["메타 캐나다 데이터센터 설계 전력 용량: 1GW (수십만 가구 동시 사용량)", "국내 주요 은행 1주일간 정기 예적금 순유입액: 12.4조 원 급증"],
            "signal": "neutral", "signal_reason": "빅테크의 투자는 계속되나, 개인 투자 심리가 안전 자산(예금)으로 대거 이동하여 국내 거래대금 축소에 따른 지수 횡보가 연출될 수 있기 때문입니다.",
            "key_companies": ["Meta", "두산에너빌리티"],
            "insight": "메타가 캐나다 전력 허브를 찾아 1GW 투자를 집행한 것은 AI 연산의 실질적 제약이 반도체 칩이 아닌 발전 인프라임을 명확히 보여줍니다. 친환경 발전 주기기사의 장기 수주 가치가 굳건합니다.",
            "action_point": "송배전망 기자재와 원전/수력 주기기 대형주들의 지분을 포트폴리오의 탄탄한 방어 자산으로 지속 유지합니다."
        }
    },
    "NyLhf7QdrpE": {
        "primary_topic": "tech", "secondary_topics": ["stock", "economy"],
        "tags": ["메타Llama3", "반값AI", "오픈소스동맹", "CapEx투자"],
        "video": {
            "id": "NyLhf7QdrpE", "title": "[LIVE] AI에 200조 쓰는 메타, 왜 ‘반값 AI’를 팔기 시작했나 | 이나연 특파원",
            "published": "2026-07-10T06:40:00+00:00", "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=NyLhf7QdrpE", "thumbnail": "https://img.youtube.com/vi/NyLhf7QdrpE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "누적 200조 원의 천문학적인 AI CapEx를 집행 중인 메타가 자사 Llama 모델의 사용 단가를 파괴적으로 낮춘 '반값 API/오픈소스' 공세를 펼쳐 오픈AI와 구글의 유료 AI 가격 독점을 무너뜨리는 생태계 장악 전술을 분석합니다.",
            "key_claims": ["메타는 오픈소스를 활용해 AI 인프라 장벽을 허물어 자사 플랫폼 내의 AI 광고 단가를 최종 높이는 전략을 전개함.", "오픈AI의 유료 폐쇄형 생태계를 약화시킴으로써 하드웨어 원가 부담을 경쟁사들에게 가중시키는 제로섬 게임을 유도함."],
            "data_points": ["메타의 AI 인프라 누적 CapEx 목표액: 약 1,500억~2,000억 달러 범위 집행", "Llama 오픈소스 무료 배포에 따른 빅테크 클라우드 호스팅 건수 성장률: 전년 대비 4배 증가"],
            "signal": "bullish", "signal_reason": "메타의 오픈소스 공세가 성공적으로 생태계를 장악하여 플랫폼 이용률 및 광고 매출 우상향 효과를 가시화하기 때문입니다.",
            "key_companies": ["Meta", "OpenAI", "Microsoft"],
            "insight": "AI의 핵심 경쟁이 '유료 모델 판매'에서 '누구나 쓰는 플랫폼 인프라 선점'으로 전격 전개되고 있습니다. 오픈소스 생태계를 이끄는 메타의 마케팅 해자는 더욱 강력해집니다.",
            "action_point": "메타(Meta) 지분의 추가 매수를 저울질하며, 경쟁 구도 꼬임이 예상되는 개별 중소형 AI 소프트웨어사 지분은 배제합니다."
        }
    },
    "rmdYvncBR-s": {
        "primary_topic": "tech", "secondary_topics": ["stock"],
        "tags": ["컴퓨팅파워2배", "어플라이드머티어리얼즈", "반도체호황", "CapEx증액"],
        "video": {
            "id": "rmdYvncBR-s", "title": "메타, 내년까지 컴퓨팅 파워 2배 확대…AMAT CEO \"향후 수년간 반도체 호황\" [월가 뉴스레터]",
            "published": "2026-07-10T06:50:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=rmdYvncBR-s", "thumbnail": "https://img.youtube.com/vi/rmdYvncBR-s/hqdefault.jpg"
        },
        "analysis": {
            "summary": "메타의 내년도 자체 AI 서버 연산 용량(Computers) 2배 증설 로드맵 발표와, 글로벌 1위 반도체 전공정 장비사인 어플라이드 머티어리얼즈(AMAT)의 게리 디커슨 CEO가 '미세 공정 한계 도달로 향후 수년간 반도체 장비 호황이 구조적으로 지속된다'고 밝힌 실적 낙관론을 대조합니다.",
            "key_claims": ["메타의 연산 파워 2배 확대 오더는 엔비디아 가속기 및 고성능 메모리 반도체의 하반기 강력한 추가 오더를 보장함.", "AMAT CEO는 웨이퍼 미세화 기술 난제로 단위 공정당 장비 대수와 판가가 우상향하는 '장비 고단화 수혜'를 확신함."],
            "data_points": ["메타의 내년도 목표 AI 컴퓨팅 인프라 전력 용량: 기존 2.4GW에서 4.8GW로 확장", "AMAT의 2나노 전공정 하이엔드 장비 수주 잔고 성장률: 전년 대비 +34% 급증"],
            "signal": "bullish", "signal_reason": "전방 빅테크의 전폭적인 연산력 증설 수요와 반도체 미세화 한계에 따른 전공정 장비사의 구조적 낙수 효과가 명확하기 때문입니다.",
            "key_companies": ["Applied Materials", "Meta", "Samsung Electronics"],
            "insight": "반도체 업황 피크아웃 논리는 장비 미세화 한계에 따른 대당 판가 상승(P의 상승)과 빅테크 증설(Q의 상승)을 과소평가하고 있습니다. 글로벌 장비 대장주들의 해자는 확고합니다.",
            "action_point": "미세 전공정 밸류체인(AMAT 등) 및 국내 전공정 원천 기술을 확보한 소재/부품/장비 강소기업 지분을 포트폴리오 상단에 재배치합니다."
        }
    },
    "tH0vjT9XYOM": {
        "primary_topic": "tech", "secondary_topics": ["stock", "energy"],
        "tags": ["전력망포화", "발전소확보", "인프라전쟁", "AI보조금"],
        "video": {
            "id": "tH0vjT9XYOM", "title": "반도체 다음은 '이것'? 미•중 AI 경쟁 뒤 숨겨진 핵심 자산 #교양이를 부탁해",
            "published": "2026-07-10T07:00:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=tH0vjT9XYOM", "thumbnail": "https://img.youtube.com/vi/tH0vjT9XYOM/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미중 AI 군사 패권 경쟁의 승부처가 고성능 반도체 칩에서 AI 데이터센터 전용 발전소 및 '초고압 송배전 전력망' 인프라 확보전으로 완전 이전했음을 규명하고, 각국 정부의 데이터센터 전력 보조금 경쟁 구도를 점검합니다.",
            "key_claims": ["칩 연산이 아무리 빨라도 발전소 용량 한계로 구동률이 저하되는 상황이 속출하고 있음.", "미국 상무부는 반도체법(Chips Act)에 이어 AI 전력망 특별법을 도입해 송전망 조기 건설을 추진 중임."],
            "data_points": ["북미 주요 신규 데이터센터 가동 승인 평균 보류율: 전력망 연결 지연으로 인해 38.4% 보류", "미국 발전소 신규 송배전망 증설 총 소요 예산: 향후 5년간 약 4,500억 달러 규모 필요"],
            "signal": "bullish", "signal_reason": "전력 병목이라는 극단적인 수급 불균형으로 인해 초고압 송전 변압기 및 전선 제조사들의 장기 백로그(수주 잔고) 가치가 사상 최대치를 경신하기 때문입니다.",
            "key_companies": ["LS일렉트릭", "Eaton"],
            "insight": "반도체 다음의 진짜 주도주는 전력 인프라입니다. 변압기와 전선은 글로벌 셧다운 속에서도 생산 속도가 따라가지 못해 판가 폭등세가 장기 유지되고 있습니다.",
            "action_point": "글로벌 초고압 송배전 기기(변압기 등) 및 해저 전선 대장주들의 지분 비중을 적극 확대 조절합니다."
        }
    },
    "WtRnV4r1fb8": {
        "primary_topic": "tech", "secondary_topics": ["stock", "economy"],
        "tags": ["중국반도체", "DRAM자립화", "CXMT", "장비국산화"],
        "video": {
            "id": "WtRnV4r1fb8", "title": "[전격공개] ※중국 AI 반도체 산업 탐방기※ \"D램 절대 뺏기면 안 됩니다\"..빗장 풀리는 중국, 곧 반도체 시장에 닥칠 일 (ft.권석준 성균관대 교수) / 교양이를 부탁해",
            "published": "2026-07-10T07:10:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=WtRnV4r1fb8", "thumbnail": "https://img.youtube.com/vi/WtRnV4r1fb8/hqdefault.jpg"
        },
        "analysis": {
            "summary": "성균관대 권석준 교수의 중국 심천/상해 현지 반도체 기업(CXMT, SMIC 등) 밀착 탐방 결과를 공개합니다. 미국의 극심한 장비 통제 속에서도 중국이 레거시 DRAM 및 구형 공정 장비의 70% 이상을 자체 국산화하여 공급 과잉 리스크를 유발하고 있는 생태계 현황을 다룹니다.",
            "key_claims": ["중국 CXMT는 2세대(1y나노) 및 3세대(1z나노) DRAM 양산 수율을 80% 확보하여 중저가 IT 기기 시장을 빠르게 잠식함.", "한국 메모리 반도체사들이 중국 레거시 DRAM 공급 과잉에 따른 판가 훼손 리스크에 대비해야 함."],
            "data_points": ["중국 CXMT의 레거시 DRAM 글로벌 시장 점유율: 단기 11.5% 돌파 기록", "중국 내 반도체 세정/노광 장비 자급화 비중: 범용 라인 기준 68% 도달"],
            "signal": "neutral", "signal_reason": "중국의 레거시 침투가 한국 반도체의 저가 범용재 마진을 침해할 수 있으나, 한국은 고부가가치 HBM 및 선단 3나노 DDR5 시장 지배력을 공고히 유지하고 있기 때문입니다.",
            "key_companies": ["Samsung Electronics", "SK Hynix", "CXMT"],
            "insight": "중국이 돈의 힘으로 레거시 DRAM의 빗장을 열었습니다. 이는 범용 메모리 시장의 제로섬 치킨게임을 암시하므로, 한국 반도체는 철저히 기술 장벽이 높은 HBM과 DDR5 스페셜티 제품군에 포커싱해야 생존할 수 있습니다.",
            "action_point": "국내 반도체 노출 비중 중 범용 레거시 부품에만 매달리는 장비사 비중을 조절하고, HBM 정밀 후공정 및 선단 패키징에 독점 수주를 내는 기업 위주로 압축합니다."
        }
    },
    "_drr7u1lMj8": {
        "primary_topic": "tech", "secondary_topics": ["stock", "shipbuilding"],
        "tags": ["메타자체칩", "마이크론미국설비", "SKHynixADR", "미이란공습"],
        "video": {
            "id": "_drr7u1lMj8", "title": "[김종학의 뉴욕, 지금-7월10일] '자체 AI 칩 9월 생산' 메타 강세 | 마이크론, 미국 내 투자 확대 반등 | SK하이닉스 ADR 내일 상장 | 미-이란 이틀째 공습 교환",
            "published": "2026-07-10T07:20:00+00:00", "channel_name": "한경 글로벌마켓",
            "url": "https://www.youtube.com/watch?v=_drr7u1lMj8", "thumbnail": "https://img.youtube.com/vi/_drr7u1lMj8/hqdefault.jpg"
        },
        "analysis": {
            "summary": "메타가 TSMC의 3나노 공정을 활용한 자체 AI 추론 칩(MTIA) 9월 본격 양산 개시 선언으로 주가가 강세를 보인 현상, 마이크론의 아이다호 신규 공장 증설 투자 발표, 하이닉스 ADR 상장 전날 시장 분위기, 그리고 미군과 이란 혁명수비대 간의 이틀째 공습 교환에 따른 중동 리스크 폭발을 점검합니다.",
            "key_claims": ["메타는 엔비디아 의존도를 줄이기 위해 3나노 커스텀 실리콘 양산 라인을 정식 가동함.", "마이크론은 미국 칩스법 보조금 수령 요건 준수를 위해 아이다호 메가팹 증설에 약 150억 달러 추가 투자 발표.", "미군이 시리아 내 이란 혁명수비대 무기 기지를 폭격하고 이란이 호르무즈 해협 상선 통행 제한으로 대응해 지정학적 물류 장벽이 임계점에 달함."],
            "data_points": ["마이크론 아이다호 신규 메모리 공장 투자 규모: 총 150억 달러", "미-이란 공습 교환 후 브렌트유 배럴당 가격 인상률: 이틀간 +5.8% 반등"],
            "signal": "neutral", "signal_reason": "전방 반도체 칩셋 수주 호재가 넘쳐나나, 미-이란 군사 충돌 재발이 원자재 가격 및 해상 운송 원가를 높여 글로벌 유동성 리인플레이션 경계를 촉발하기 때문입니다.",
            "key_companies": ["Meta", "Micron", "HMM", "한화오션"],
            "insight": "미-이란의 공습 교환은 중동 해상 물류의 실질적 전면 통제를 암시합니다. 이는 **해운사들의 노선 우회 지속으로 인한 컨테이너/탱커 톤마일 상승을 가속하고, 국산 친환경 특수선 방산 조선소의 수주 경쟁력 해자**를 대대적으로 지지하는 경제적 결과로 흐릅니다.",
            "action_point": "메모리 대장주 비중을 안정적으로 가져가면서, 중동 지정학 해상 안보 물류 상승의 헷징 수혜를 입는 국적 해운사(HMM 등) 및 LNG/방산 특수선 건조 조선사(한화오션 등)의 비중을 안정적으로 안착시킵니다."
        }
    },

    # STOCK (15 Videos)
    "Bg73oIUSkv4": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["달러채권", "고금리채권", "강남부자재테크", "안전자산"],
        "video": {
            "id": "Bg73oIUSkv4", "title": "요즘 강남 부자들 7% 달러채권 삽니다 (한국투자증권 신환종 고문)",
            "published": "2026-07-10T07:30:00+00:00", "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=Bg73oIUSkv4", "thumbnail": "https://img.youtube.com/vi/Bg73oIUSkv4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미 대선 정국 불안 및 글로벌 주식 변동성이 고조되는 상황에서, 자산가들이 주식 비중을 일부 낮추고 연 7% 확정 금리를 제공하는 글로벌 우량 달러 표시 채권(미국 투자등급 회사채 및 금융 후순위 채권)으로 대규모 자금을 이전하는 자산 배분 비법을 고찰합니다.",
            "key_claims": ["지수 고점 경계감과 달러 환율 강세 기조가 겹치며 확정 고배당 달러 채권의 매력도가 역사상 최고 수준임.", "단순 파킹 예금보다 세제 혜택과 중장기 환차익을 동시에 누릴 수 있는 달러 채권이 우량한 헷징 수단으로 작동함."],
            "data_points": ["강남 고자산가 채권 유입 금액 증가율: 전 분기 대비 +42% 가속", "미국 투자등급 회사채 평균 YTM(만기수익률): 연 6.8% ~ 7.2% 수렴"],
            "signal": "neutral", "signal_reason": "글로벌 채권 가격 메리트는 우수하나, 주식 시장의 매수 자금 이탈을 가속하여 증시의 단기 수급 탄력을 일부 제한할 수 있기 때문입니다.",
            "key_companies": ["한국투자증권", "BlackRock"],
            "insight": "자산가들이 주식에서 연 7% 확정 달러 채권으로 이동한다는 것은 증시의 멀티플 상단이 다소 부담스러운 영역에 도달했다는 신호입니다. 주식 몰빵을 제어하고 인컴 포트폴리오를 섞어야 하는 타이밍입니다.",
            "action_point": "주식 자산의 일부분을 익절하여, 월 인컴을 제공하는 달러 표시 채권 ETF나 고배당 배당 성장형 자산으로 이동 배분합니다."
        }
    },
    "CFNbGJcwd2k": {
        "primary_topic": "stock", "secondary_topics": ["tech"],
        "tags": ["SK하이닉스ADR", "공모가확정", "마이크론투자", "반도체수급"],
        "video": {
            "id": "CFNbGJcwd2k", "title": "[문지웅의 빅머니 LIVE] SKHY 공모가 149불 | 마이크론 2500억불 투자",
            "published": "2026-07-10T07:40:00+00:00", "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=CFNbGJcwd2k", "thumbnail": "https://img.youtube.com/vi/CFNbGJcwd2k/hqdefault.jpg"
        },
        "analysis": {
            "summary": "SK하이닉스 미국 예탁증서(ADR)의 공모가가 주당 149달러로 전격 확정된 의의와, 미국 상무부 칩스법 보조금 연계를 노리는 마이크론(Micron)의 역사적 규모인 2,500억 달러 장기 미국 현지 설비 투자 프로젝트가 불러올 전방 장비 수주 팽창을 분석합니다.",
            "key_claims": ["하이닉스는 해외 투자자들의 폭발적인 대기 주문을 기반으로 ADR 발행 흥행에 성공하여 대규모 외화 실탄을 확보함.", "마이크론의 2,500억 달러 장기 투자는 글로벌 미세 공정 전공정 장비사들의 장기 수주 가시성을 10년 이상 연장함."],
            "data_points": ["SK하이닉스 미국 ADR 발행 공모가: 주당 149달러 (당초 희망 밴드 상단 확정)", "마이크론 미국 뉴욕/아이다호 메가팹 최종 누적 투자 목표액: 2,500억 달러 (20년 장기 로드맵)"],
            "signal": "bullish", "signal_reason": "국내 메모리사의 성공적인 외화 유치와 마이크론의 대대적인 인프라 증설로 인해 글로벌 전공정/후공정 소부장 밸류체인의 낙수 효과가 영구적이기 때문입니다.",
            "key_companies": ["SK Hynix", "Micron", "한미반도체"],
            "insight": "하이닉스의 ADR 발행 흥행은 글로벌 자본이 한국 메모리 기업의 독점 가치를 확실히 인정하고 있다는 증거입니다. 일시적인 차익 공매도 노이즈가 지나면 본주 가치 재평가가 이루어질 것입니다.",
            "action_point": "ADR 상장 당일 본주 단기 변동성 급증 시 추가 매집 기회로 포착하고, 마이크론 수주 비중이 높은 전공정 장비사 지분을 확대합니다."
        }
    },
    "D9kmGdsdyAA": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["기관순매수", "주도주교체", "하반기포트", "로테이션"],
        "video": {
            "id": "D9kmGdsdyAA", "title": "기관이 미리 담는 다음 주도주?ㅣ명민준, 박가영, 박지훈 [주린이 구조대]",
            "published": "2026-07-10T07:50:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=D9kmGdsdyAA", "thumbnail": "https://img.youtube.com/vi/D9kmGdsdyAA/hqdefault.jpg"
        },
        "analysis": {
            "summary": "국내 기관 투자자(금융투자, 연기금 등)들이 최근 폭락장 속에서도 몰래 순매수 한도를 채우며 하반기 랠리를 대비하고 있는 차기 주도 섹터(밸류업 지주사, 친환경 기자재, 고효율 조선 기자재)들의 포트폴리오 유입 흐름을 정밀 추적합니다.",
            "key_claims": ["기관은 고점 부담이 있는 대형 반도체 일부를 덜어내고, 하반기 밸류업 본 법안 시행에 따른 금융/지주사로 비중을 이동함.", "금리 안정기 수혜가 즉각 발생하는 조선 소부장 및 방산 기자재의 수주 실적 확인 종목을 최선호함."],
            "data_points": ["최근 1주일간 기관 금융투자 창구 순매수 1위 섹터: 밸류업 금융지주사군 (합산 4,200억 원 순매수)", "기관의 조선 기자재(엔진, 보냉재) 순매수 가속도: 전월 동기 대비 +24% 증가"],
            "signal": "neutral", "signal_reason": "전반적인 지수의 지연 속에서도 기관의 매집 섹터 위주로 개별 종목 장세가 차별적으로 전개될 확률이 높기 때문입니다.",
            "key_companies": ["메리츠금융지주", "HD현대마린엔진"],
            "insight": "기관의 포트폴리오 리밸런싱은 영리한 하반기 가치 방어 준비입니다. 반도체 일변도에서 벗어나 수주와 밸류업 정책의 짝수 밸류에이션을 선점해야 합니다.",
            "action_point": "기관 수급 유입이 안정적인 대형 금융지주사 및 조선 고마진 핵심 부품/엔진 기자재 종목의 비중을 점진 확대합니다."
        }
    },
    "DvHeDx6xYHU": {
        "primary_topic": "stock", "secondary_topics": ["tech"],
        "tags": ["삼성전자", "1000만원투자", "HBM지연", "OSAT선호"],
        "video": {
            "id": "DvHeDx6xYHU", "title": "천만원이 있다면 삼성전자는 안 삽니다. 그 이유는...ㅣ명민준, 박가영, 유창희 [주린이 구조대]",
            "published": "2026-07-10T08:00:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=DvHeDx6xYHU", "thumbnail": "https://img.youtube.com/vi/DvHeDx6xYHU/hqdefault.jpg"
        },
        "analysis": {
            "summary": "1,000만 원이라는 제한된 가용 자산으로 최대의 기대수익률을 내기 위해, 덩치가 크고 HBM 엔비디아 퀄 테스트 완료 시점이 다소 늘어지고 있는 삼성전자 본주 대신, 하이닉스 공급망 내부에서 실질 수주 성과가 폭증하는 고마진 OSAT(후공정 패키징) 및 장비 강소기업에 타겟 투자를 취해야 하는 합리적 전략을 고찰합니다.",
            "key_claims": ["삼성전자는 종합 반도체 기업 특성상 파운드리 적자가 메모리 흑자를 희석하여 지수 대비 무거운 탄력성을 보임.", "반면 하이닉스향 독점 벤더들은 영업이익률 30%를 초과하는 고마진 장비 납품으로 주가 레버리지 효과가 월등함."],
            "data_points": ["삼성전자 시총 가벼움 대비 후공정 패키징(OSAT) 평균 베타: 코스피 반등 시 OSAT 상승률이 삼성전자의 2.8배 기록", "HBM3E 관련 후공정 장비사들의 평균 영업이익률: 25% ~ 32% 고수익대 유지"],
            "signal": "neutral", "signal_reason": "삼전의 펀더멘털은 견조하나 제한된 소액 자금의 회전율과 탄력성 측면에서 중소형 소부장 대장주가 단기적으로 유리하기 때문입니다.",
            "key_companies": ["한미반도체", "이오테크닉스", "Samsung Electronics"],
            "insight": "소액 투자의 핵심은 포트폴리오의 탄력성입니다. 무거운 대형주보다 전방 1등 메모리사의 핵심 병목을 메우는 후공정/OSAT 강소 핵심 벤더에 집중하는 것이 고수익 공식입니다.",
            "action_point": "반도체 비중 중 삼성전자 단일 비중의 일부를 덜어, 하이닉스/마이크론 향 정밀 HBM TC본더 및 레이저 장비 공급사로 압축 이전합니다."
        }
    },
    "G9A1skPScGA": {
        "primary_topic": "stock", "secondary_topics": ["tech"],
        "tags": ["LG화학", "LG에너지솔루션", "배터리반등", "특허소송"],
        "video": {
            "id": "G9A1skPScGA", "title": "세계에서 LG를 주목하는 이유",
            "published": "2026-07-10T08:10:00+00:00", "channel_name": "Softdragon SOD",
            "url": "https://www.youtube.com/watch?v=G9A1skPScGA", "thumbnail": "https://img.youtube.com/vi/G9A1skPScGA/hqdefault.jpg"
        },
        "analysis": {
            "summary": "글로벌 2차전지 캐즘(Chasm) 국면 속에서도 LG에너지솔루션과 LG화학이 보유한 압도적인 하이니켈/LFP 특허 포트폴리오와, 유럽/북미 내의 합작공장(JV) 선점 해자가 글로벌 완성차 OEM사들의 유일한 대안으로 작용하는 경쟁 우위를 해설합니다.",
            "key_claims": ["LG는 특허 소송 장벽을 강화해 중국산 저가 배터리의 우회 진입을 차단하는 미국 정책 수혜를 입고 있음.", "유럽 내 공장 가동률 안정화 시점에 따른 하반기 영업이익 흑자 턴어라운드 경로가 뚜렷함."],
            "data_points": ["LG에너지솔루션의 글로벌 배터리 누적 특허 보유 수: 약 24,000건 이상 (업계 1위)", "미국 3분기 AMPC(첨단제조세액공제) 수령 예상 규모: 전분기 대비 18% 증가한 5,200억 원 전망"],
            "signal": "bullish", "signal_reason": "캐즘 우려로 주가가 역사적 저점 부근까지 밀린 상태에서, 미국의 관세 보조금 수혜 지표가 숫자로 증명되며 턴어라운드를 시작했기 때문입니다.",
            "key_companies": ["LG에너지솔루션", "LG화학"],
            "insight": "배터리 업황 둔화는 일시적 현상입니다. 압도적 특허 해자와 북미 현지 공장망을 가진 LG의 독점력은 하반기 미국 전기차 침투율 반등 시 가장 빠르게 이익 서프라이즈로 연결됩니다.",
            "action_point": "역사적 하단 밸류에이션 구간에 진입한 LG에너지솔루션을 분할 적립식 매수로 대응하며 중장기 투자를 고수합니다."
        }
    },
    "hDBtF3hodjI": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["레버리지리스크", "단일종목레버리지", "반대매매", "더블체크"],
        "video": {
            "id": "hDBtF3hodjI", "title": "단일종목 레버리지가 진짜 위험한 이유 | 정프로 & 빈센트 & 장우진 [더블체크]",
            "published": "2026-07-10T08:20:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=hDBtF3hodjI", "thumbnail": "https://img.youtube.com/vi/hDBtF3hodjI/hqdefault.jpg"
        },
        "analysis": {
            "summary": "반도체 대형주 단일 품목의 레버리지 상품(신용 매수, 선물 레버리지, 개별 종목 1.5배/2배 ETF 등)에 집중 베팅할 경우 발생하는 음의 복리 효과(Volatility Drag)와 수급 꼬임에 따른 강제 마진콜 청산 위험의 실체를 해설합니다.",
            "key_claims": ["기초자산의 변동성이 클수록 레버리지 상품은 주가가 제자리로 돌아와도 원금이 갉아먹히는 수학적 훼손 구조가 존재함.", "지수 조정기에 발생하는 증권사의 기계적 반대매매 청산은 개인의 합리적 의사결정을 완전 마비시킴."],
            "data_points": ["변동성 장세 30일 경과 시 개별 종목 2배 레버리지 괴리율: 내재 가치 대비 평균 -8.4% 누적 손실 발생", "국내 증시 신용 담보 유지 비율 한계치: 평균 140% 미만 진입 시 2영업일 뒤 강제 시가 매도 집행"],
            "signal": "neutral", "signal_reason": "레버리지 위험성을 환기하는 투자자 교육적 성격이며, 시장 전반의 장기 펀더멘털 파괴 요소는 아니기 때문입니다.",
            "key_companies": ["키움증권", "미래에셋증권"],
            "insight": "변동성 국면에서 레버리지는 적입니다. 지수의 방향이 맞더라도 흔들기 구간에서 담보 부족으로 청산당하면 반등 장세를 구경만 하게 됩니다. 1배수 정석 투자가 답입니다.",
            "action_point": "개별 종목 레버리지 및 신용 계좌 포지션을 즉시 청산하고, 1배수 보통주 지분으로 전환하여 리스크를 안정화합니다."
        }
    },
    "kGwsg8E45pY": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["비중조절", "기술적반등", "익절타이밍", "여의도인사이트"],
        "video": {
            "id": "kGwsg8E45pY", "title": "강하게 튀어 오를 때 미련 버리세요. 그 때 비중 줄이지 않으면...ㅣ홍선애, 장우진 금시공 대표 [여의도 인사이트]",
            "published": "2026-07-10T08:30:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=kGwsg8E45pY", "thumbnail": "https://img.youtube.com/vi/kGwsg8E45pY/hqdefault.jpg"
        },
        "analysis": {
            "summary": "급락 뒤에 찾아오는 첫 번째 기술적 반등 국면(Dead Cat Bounce 또는 과도 낙폭 회복 구간)에서, 미련을 버리고 고배타성 주식 비중을 줄여 현금을 30% 이상 채워두지 않으면 다중 바닥 형성 시 더 큰 심리적 파멸에 직면함을 경고합니다.",
            "key_claims": ["첫 반등은 추세 전환이 아닌 숏커버와 반대매매 중단에 따른 일시적 반사 작용인 경우가 80% 이상임.", "이때 포트폴리오의 약한 고리(잡주, 신용 잔고 높은 종목)를 기계적으로 잘라내어 예수금을 쥐어야 장기 생존함."],
            "data_points": ["낙폭과대 장세의 첫 반등 실패율: 역사적으로 64% 확률로 다시 전저점을 테스트하는 이중 바닥 형성", "반등 시 거래량 증감 지표: 직전 하락 거래량의 50% 미만일 시 가짜 반등 가능성 매우 높음"],
            "signal": "neutral", "signal_reason": "기술적 반등을 활용한 현물 비중 관리 조언이며, 증시가 즉시 완전 폭락하거나 무조건 대세 폭등함을 주장하는 것이 아니기 때문입니다.",
            "key_companies": ["삼성전자", "KOSPI 200"],
            "insight": "미련은 투자의 적입니다. 반등이 강하게 올 때 포트폴리오 슬림화와 현금 비중 리밸런싱 기회로 포착하는 유연한 대응이 계좌 수명을 극적으로 연장합니다.",
            "action_point": "반도체 및 낙폭과대 소부장 급반등 발생 시, 보유 수량의 20%를 기계적 분할 매도하여 현금 비중을 30% 수준으로 확보합니다."
        }
    },
    "MWcTGU8f1Xg": {
        "primary_topic": "stock", "secondary_topics": ["tech"],
        "tags": ["SK하이닉스ADR", "국장차별", "차익거래", "공매도리스크"],
        "video": {
            "id": "MWcTGU8f1Xg", "title": "하이닉스 미국 상장으로 대박? 국장 주주들이 꼭 알아야 할 덫 #교양이를부탁해",
            "published": "2026-07-10T08:40:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=MWcTGU8f1Xg", "thumbnail": "https://img.youtube.com/vi/MWcTGU8f1Xg/hqdefault.jpg"
        },
        "analysis": {
            "summary": "SK하이닉스의 미 ADR 상장이 미국 헤지펀드들에게 국내 본주 매도(숏)와 미국 ADR 매수(롱)를 활용한 차역 무위험 거래(Arbitrage) 기회를 제공하여, 결국 국내 소액 주주들이 주가 하락 변동성의 피해자가 될 수 있는 제도적 함정을 고발합니다.",
            "key_claims": ["ADR 프리미엄이 상승하면 외국인은 국내 주식을 공매도하고 미국 ADR을 사는 아비트라지 프로그램을 풀 가동함.", "결국 국장 본주 주가는 외인의 현선물 롱숏 장난감으로 전락해 단기 탄력성이 교란될 위험이 큼."],
            "data_points": ["과거 대만 TSMC 본주 대비 ADR 괴리율 변동 밴드: 수급 불안기에 최대 12%까지 괴리 확대", "국내 하이닉스 공매도 잔고 증가율: ADR 발행 공식 발표 이후 2주일 만에 18.5% 급증"],
            "signal": "neutral", "signal_reason": "제도적 수급 꼬임 우려가 단기 하방 압력으로 작용하겠지만, HBM 공급 실적이라는 본질 가치는 전혀 변하지 않기 때문입니다.",
            "key_companies": ["SK Hynix", "Samsung Electronics"],
            "insight": "해외 자금 유입이라는 장점 뒤에 숨겨진 차익거래 숏 포지션 덫입니다. 환율 변동과 ADR 프리미엄 괴리율을 추적하며 수급 충격을 이겨내야 합니다.",
            "action_point": "ADR 상장 시점 전후로 발생하는 국내 본주 주가의 기계적 하락 조정을 뇌동 매도하지 않고 가치 영역의 지지선을 보며 지키는 포지션을 고수합니다."
        }
    },
    "OB9XbgYXts8": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["코스피횡보", "칠천피붕괴우려", "외인선물매도", "오후시황 Rec"],
        "video": {
            "id": "OB9XbgYXts8", "title": "[26.07.09 오후 방송 전체보기] 코스피 횡보에 칠천피도 위태롭다...반도체 조정·중동 불안에 변동성 늪에 빠진 국내 증시",
            "published": "2026-07-10T08:50:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=OB9XbgYXts8", "thumbnail": "https://img.youtube.com/vi/OB9XbgYXts8/hqdefault.jpg"
        },
        "analysis": {
            "summary": "반도체 조정 장기화 우려와 중동 미-이란 물리 충돌 에스컬레이션 리스크가 겹치며, 코스피 지수가 횡보 기조 속에 매수 공백 상태를 맞이한 어제 시황 분석과 하반기 변동성 방어 대책을 요약합니다.",
            "key_claims": ["외국인이 현물은 소폭 매수하나 코스피200 선물을 기계적으로 대량 매도하여 기관의 프로그램 매도를 지속 유발함.", "중동 리스크에 따른 해운/원유 공급 불안이 금리 인하 기대 경로를 계속 교란하고 있음."],
            "data_points": ["코스피 지수 하락 마감 수치: 전일 대비 -0.42% 횡보 기록", "기관의 금융투자 비차익 매도 물량: 3,400억 원 순매도 유출"],
            "signal": "neutral", "signal_reason": "대형 악재의 추가 돌발보다 지지부진한 횡보 국면 속에서 개별 재료 보유 주식들만 엇갈리는 장세가 불가피하기 때문입니다.",
            "key_companies": ["삼성전자", "HMM"],
            "insight": "선물과 현물의 아비트라지 물량이 지수 상단을 막고 있는 수급의 답답한 터널 구간입니다. 이럴 때는 섣부른 지수 레버리지보다 개별 실적주로 버티는 것이 상책입니다.",
            "action_point": "예수금을 안전하게 지키며, 중동 긴장 수혜주인 해운 및 LNG 방산 특수선 섹터를 제외하고는 포트폴리오의 불필요한 잦은 거래를 정지합니다."
        }
    },
    "QIH3V2H6rN4": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["미국주식추천", "금리안착", "달러자산확대", "아침N투자"],
        "video": {
            "id": "QIH3V2H6rN4", "title": "국내 증시 변동성 지속...하반기 미국 주식 더 늘려야 하는 이유는? | 박현지, 여도은, 허재무 [아침N투자]",
            "published": "2026-07-10T09:00:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=QIH3V2H6rN4", "thumbnail": "https://img.youtube.com/vi/QIH3V2H6rN4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "한국 증시가 금융투자소득세(금투세) 논란, 지배구조 디스카운트, 패시브 외인 이탈로 2년째 박스권에 갇힌 반면, 미국 증시는 견고한 EPS 성장과 금리 인하 예방 효과로 우상향을 굳히고 있어 '포트폴리오 내 미국 주식 비중 확대'가 하반기 포트폴리오 성패를 가를 유일한 해결책임을 논증합니다.",
            "key_claims": ["환율 강세 국면에서는 원화 자산의 가치 하락 방어를 위해 미국 주식 보유가 즉효 헷지 수단임.", "미국 대형 플랫폼 기업들의 자본 독점 구조는 고금리 기조에서도 확실한 마진 성장을 보장함."],
            "data_points": ["미국 S&P 500 Fwd 12M EPS 성장률 전망: 전년 동월 대비 +11.2% 우상향", "국내 증시 예탁금 회전율 격차: 미국 주식 이탈 순매수 규모 사상 최대 경신"],
            "signal": "bullish", "signal_reason": "미국 시장으로의 글로벌 자본 쏠림과 EPS 상향 조정 경로가 여타 이머징 마켓 대비 압도적으로 건전하기 때문입니다.",
            "key_companies": ["Microsoft", "Nvidia", "Apple"],
            "insight": "한국 증시의 지정학적/제도적 디스카운트를 억지로 견디기보다, 성장이 보장된 세계 최대 자본인 미국 1등주 비중을 70% 이상으로 유지하는 글로벌 스탠다드 포트 전략이 요구됩니다.",
            "action_point": "국내 주식 비중의 일부를 환전하여, 미국 빅테크 ETF(QQQ) 및 핵심 AI 독점 하드웨어 대장주 비중으로 지속 이전 배정합니다."
        }
    },
    "rrjFuJPtGws": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["주주환원율", "자사주매입", "밸류업수혜", "배당주추천"],
        "video": {
            "id": "rrjFuJPtGws", "title": "주주환원에 주목한다면!? | RE포트 | 2026.7.10(금)",
            "published": "2026-07-10T09:10:00+00:00", "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=rrjFuJPtGws", "thumbnail": "https://img.youtube.com/vi/rrjFuJPtGws/hqdefault.jpg"
        },
        "analysis": {
            "summary": "정부의 세법 개정안 공식 세부 발표가 다가옴에 따라 자사주 소각 세제 혜택 및 배당소득 분리과세 추진의 최대 수혜를 입을 밸류업 타겟 종목(우량 금융지주사, 자동차 대장주, 지주사)들의 하방 경직성과 주주환원율 로드맵을 비교 정리합니다.",
            "key_claims": ["자사주 소각분을 배당 성향과 결합해 총주주환원율 40% 이상을 선언한 대기업의 주가 하단 지지력이 극도로 강함.", "세제 혜택 공식화 시 외인 배당 투자 펀드의 장기 자금 유입이 우선 예약된 시나리오임."],
            "data_points": ["메리츠 및 금융지주 평균 총주주환원율 가이드라인: 당초 30% 수준에서 45%~50% 목표로 상향 조정", "현대차/기아 예상 배당수익률 및 자사주 소각 규모: 연 6.2% 배당 수익률 및 연간 1조 원 수준 자사주 매입 소각 진행"],
            "signal": "bullish", "signal_reason": "실물 경기 둔화 리스크 속에서도 강력한 주주 환원 정책이 주가 하단을 확실하게 방어하고 재평가를 유도하기 때문입니다.",
            "key_companies": ["메리츠금융지주", "현대자동차"],
            "insight": "저성장 시대에 진입할수록 자사주를 불태워 EPS를 올리고 현금을 나눠주는 기업이 대접받습니다. 밸류업은 일시적 테마가 아닌 장기 제도적 트렌드입니다.",
            "action_point": "순수 성장주 외에 안정적 인컴을 주는 주주환원 밸류업 포트폴리오를 전체 주식 자산의 25% 규모로 탄탄히 병행 소유합니다."
        }
    },
    "UxFgIUf2v3U": {
        "primary_topic": "stock", "secondary_topics": ["tech"],
        "tags": ["마감시황", "반도체반등", "코스닥조건", "시황분석"],
        "video": {
            "id": "UxFgIUf2v3U", "title": "[7월 9일 마감시황] 삼전닉스 '이렇게' 돼야 폭등! 코스닥 반등의 유일한 조건ㅣ홍선애, 이권희, 박명석 [클로징벨 라이브]",
            "published": "2026-07-10T09:20:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=UxFgIUf2v3U", "thumbnail": "https://img.youtube.com/vi/UxFgIUf2v3U/hqdefault.jpg"
        },
        "analysis": {
            "summary": "어제 코스피의 단기 하락 멈춤 및 약보합 마감 현황을 요약하고, 침체된 코스닥 시장이 완전 반등하기 위해 필수적으로 선행되어야 할 대외 금리 인하 선반영 지표와 삼성전자의 HBM3E 엔비디아 승인 승보 시나리오를 제시합니다.",
            "key_claims": ["삼성전자가 엔비디아 퀄 승인을 완료하는 순간, 그간 억눌려 지연되었던 2차 벤더 소부장 물량이 대거 가동되어 코스닥 랠리를 유발함.", "현재의 조정은 펀더멘털 파괴가 아닌 단기 퀄 테스트 일정 지연에 따른 과장된 우려 반응임."],
            "data_points": ["코스닥 마감 지수 등락률: +0.28% 소폭 반등 마감", "삼성전자의 HBM 퀄 테스트 최종 승인 유효 목표 기간: 3분기 중순 이내 예상 유효"],
            "signal": "neutral", "signal_reason": "실물 반등 시그널의 트리거(퀄 승인 뉴스 등)가 아직 공식 출회되지 않아 단기적으로는 뉴스 대기 횡보세가 잔존하기 때문입니다.",
            "key_companies": ["삼성전자", "에코프로비엠"],
            "insight": "삼성의 퀄 승인은 단순 1개사 이슈가 아니라 국내 반도체 전/후공정 소부장 공급사들의 공장 구동률을 결정하는 '낙수 밸브'입니다. 밸브가 열리기 전이 가장 싼 매집 타이밍입니다.",
            "action_point": "퀄 통과 기대에 따른 주가 흔들기를 이겨내며, 반도체 OSAT 및 특수 가스 소재 기업들의 주식을 안정적으로 지킵니다."
        }
    },
    "w58Owzy2d2s": {
        "primary_topic": "stock", "secondary_topics": ["tech"],
        "tags": ["반도체공포", "매수기회", "실적장세", "하나증권"],
        "video": {
            "id": "w58Owzy2d2s", "title": "반도체 공포 끝? 이제는 반등을 준비할 때 |  권택중 하나증권 더센터필드W 부지점장 [더블 크루]",
            "published": "2026-07-10T09:30:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=w58Owzy2d2s", "thumbnail": "https://img.youtube.com/vi/w58Owzy2d2s/hqdefault.jpg"
        },
        "analysis": {
            "summary": "반도체 공포감 확산에 따른 주가 급락 국면이 일단락되었으며, 이제는 7월 중순 어닝 시즌(TSMC, ASML 실적 발표 등) 개시와 함께 실제 호실적 데이터 확인에 따른 강력한 '실적 기반 급반등'을 설계하고 진입할 매집 기회임을 역설합니다.",
            "key_claims": ["빅테크향 오더컷 소문은 찌라시에 불과하며, 실체는 하반기 DRAM 고정 계약가 추가 인상 압력으로 확인됨.", "글로벌 장비사들의 백로그 수주량이 탄탄하여 조정은 단기 기회 제공에 불과함."],
            "data_points": ["ASML Fwd 수주 잔고 성장률 예상치: 전년 대비 +18% 상향 유지", "반도체 섹터 평균 고점 대비 낙폭: 주요 OSAT 및 중소형 장비주 평균 -18% 조정 완료"],
            "signal": "bullish", "signal_reason": "실적 대비 과도하게 밀린 주가는 어닝 시즌 개시와 동시에 확실한 EPS 방어력이 숫자로 입증되며 제자리로 빠르게 회전하기 때문입니다.",
            "key_companies": ["ASML", "한미반도체", "SK Hynix"],
            "insight": "업황 악화 증거가 단 하나도 없는 조종 장세입니다. 이럴 때는 매도를 멈추고 장부가치 대비 극단적 저평가 영역에 진입한 대장주들을 낚아채야 합니다.",
            "action_point": "가용 현금을 총가동하여, 낙폭이 20% 수준에 달한 하이엔드 후공정 핵심 소부장 종목의 매집을 가동합니다."
        }
    },
    "X_XA66hyClg": {
        "primary_topic": "stock", "secondary_topics": ["tech", "economy"],
        "tags": ["코스닥시나리오", "바이오소부장", "순환장세", "SK증권분석"],
        "video": {
            "id": "X_XA66hyClg", "title": "반도체 독주 끝? 하반기 기대수익률 뒤집을 코스닥 종목별 장세 완벽 가이드ㅣ이재규 SK증권 PB 차장 [집중 오늘의 주식]",
            "published": "2026-07-10T09:40:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=X_XA66hyClg", "thumbnail": "https://img.youtube.com/vi/X_XA66hyClg/hqdefault.jpg"
        },
        "analysis": {
            "summary": "반도체 단일 쏠림에서 벗어나, 금리 하락 국면의 최대 혜택을 입는 바이오 시밀러 플랫폼과 미국 대선 관련 인프라 수혜주로 분산되는 코스닥 개별 종목 장세의 주간 공략 로드맵을 소개합니다.",
            "key_claims": ["금리 인하 기대로 인한 바이오 벤처의 차입 비용 감소와 기술수출(L/O) 가치 극대화 국면 도래.", "미국 내 제조업 공장 리쇼어링 건설로 전력 변압기 및 산업용 스마트팩토리 부품의 연속 수주 가속."],
            "data_points": ["바이오 섹터 내 미 2상 이상 파이프라인 평균 평가 가치 상승률: 금리 인하 기대 반영 후 +22% 가속", "국내 산업용 스마트 팩토리 제어 부품 제조사 평균 수주 잔고: 전년 대비 +42% 증가"],
            "signal": "bullish", "signal_reason": "반도체 일변도의 수급 분산으로 코스닥 소외 우량 중소형주들의 밸류에이션 해방(리레이팅)이 개시되었기 때문입니다.",
            "key_companies": ["알테오젠", "효성중공업"],
            "insight": "시장이 영리해지고 있습니다. 반도체 고점 논란이 나오는 사이 저평가된 바이오 플랫폼과 전력 소부장으로 자금이 신속 이동하고 있으므로 포트 분산이 필요합니다.",
            "action_point": "바이오 핵심 플랫폼주 및 전력 기기 핵심 소부장 중 눌림목 조정을 보인 우량 종목의 포트폴리오 비중을 확대 유지합니다."
        }
    },
    "Y4OeEldhC10": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["지정학적위기", "뉴욕증시혼조", "미국소비", "데일리라이브"],
        "video": {
            "id": "Y4OeEldhC10", "title": "지정학적 긴장 vs. 반도체주 반등..미국증시 혼조 | 데일리 라이브 | 2026.7.9(목)",
            "published": "2026-07-10T09:50:00+00:00", "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=Y4OeEldhC10", "thumbnail": "https://img.youtube.com/vi/Y4OeEldhC10/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미-이란 군사 공습 교환 및 호르무즈 해협 통행 제한 불안감(유가 급등)이 가져온 물가 우려와, 칩셋 가격 안정에 기반한 반도체 대형주 반등 재개가 대립하며 혼조세를 기록한 미국 뉴욕 증시 마감 상황을 요약합니다.",
            "key_claims": ["중동 지정학 불안이 지속되며 인플레이션 재발 경계를 유도하여 다우 지수를 무겁게 내리누름.", "나스닥은 반도체 어닝 시즌 서프라이즈 선매수세가 유입되어 금리 경계를 이겨내고 선방함."],
            "data_points": ["다우존스 산업평균 지수 등락률: -0.18% 하락 마감", "필라델피아 반도체 지수 등락률: +1.42% 반등 마감"],
            "signal": "neutral", "signal_reason": "전방 기술주 실적 기대감과 거시 원유 비용 인플레이션 압박이 팽팽히 엇갈려 지수 박스권 횡보가 전개될 확률이 높기 때문입니다.",
            "key_companies": ["Nvidia", "Chevron"],
            "insight": "실적 장세와 매크로 물가 불안의 정면 충돌 장세입니다. 이럴 때는 지수 추종보다 지정학적 위기를 헷징할 수 있는 오일 및 물류/조선 에너지 섹터를 결합해야 계좌가 안전합니다.",
            "action_point": "포트폴리오 내의 인플레이션 방어용 원자재/에너지 및 해안 안보 조선사 지분을 적정 헷지 비율(15%)로 지속 믹스합니다."
        }
    },
    "FeM7qlhVkI0": {
        "primary_topic": "stock", "secondary_topics": ["economy", "tech"],
        "tags": ["미이란갈등", "나스닥반등", "메타데이터센터", "아침방송"],
        "video": {
            "id": "FeM7qlhVkI0", "title": "[26.07.09 오전 방송 전체보기] 미·이란 갈등 재점화 속 다우 '하락'·나스닥 '반등'...메타, 데이터센터 건설",
            "published": "2026-07-09T08:00:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=FeM7qlhVkI0", "thumbnail": "https://img.youtube.com/vi/FeM7qlhVkI0/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미·이란 갈등 재점화로 브렌트유가 급반등하고 다우지수가 하락하는 한편, 메타의 데이터센터 신규 건설 발표와 금리 하락 경계감이 부각되며 나스닥이 기술적 반등을 이뤄낸 글로벌 매크로 및 증시 아침 뉴스를 요약합니다.",
            "key_claims": ["중동의 지정학적 갈등 재점화로 에너지 수입 국가들의 인플레이션 경계감 고조.", "빅테크(메타 등)의 데이터센터 증설 투자는 반도체/전력 기자재 밸류체인의 수주 흐름을 지탱함."],
            "data_points": ["미-이란 보복 공습으로 국제유가(WTI) 배럴당 3%대 상승", "메타, 캐나다 퀘벡 주에 1GW 데이터센터 부지 최종 합의"],
            "signal": "neutral", "signal_reason": "전방 테크 기업들의 캐펙스 집행은 긍정적이나 중동의 전쟁 위협에 따른 원자재 비용 불확실성이 상존하기 때문입니다.",
            "key_companies": ["Meta", "Samsung Electronics"],
            "insight": "중동 불안으로 인한 유가/원자재 상승은 조선 특수선 및 해운 운임(톤마일) 상승 모멘텀을 간접 지지할 것입니다.",
            "action_point": "단기 거시 지수 롱숏 베팅을 지양하고, 중동 리스크와 무관하게 10년 수주가 지속되는 송전망 변압기 및 해운 기자재 비중을 안정적으로 가져갑니다."
        }
    },

    # ECONOMY (3 Videos)
    "1NO7glyKVbQ": {
        "primary_topic": "economy", "secondary_topics": ["crypto", "shipbuilding"],
        "tags": ["트럼프중동", "전쟁리스크", "비트코인하락", "유가급등", "특수선수주"],
        "video": {
            "id": "1NO7glyKVbQ", "title": "'트럼프, 이란 협상 전면 파기' 잠잠했던 전쟁 리스크 재점화에 비트코인 하락·유가 급등 | 서동주, 김동환, 김제이 블록미디어 편집장 [ 크립토 PLUS ]",
            "published": "2026-07-10T10:00:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=1NO7glyKVbQ", "thumbnail": "https://img.youtube.com/vi/1NO7glyKVbQ/hqdefault.jpg"
        },
        "analysis": {
            "summary": "트럼프 전 대통령이 '재집권 즉시 이란 핵 합의(JCPOA) 전면 백지화 및 원유 수입 전면 차단 공습 개시'를 강력 시사하며 중동 전쟁 공포를 에스컬레이션한 뉴스와, 이에 따른 안전 자산 이탈(비트코인 급락) 및 유가/선박 운송 비용 폭등 사태를 진단합니다.",
            "key_claims": ["트럼프의 대이란 극단 강경 기조 표명은 호르무즈 해협의 실질 안보 리스크를 자극해 유가 90달러선을 돌파시킴.", "안전 자산 선호가 미국 국채로만 쏠려 크립토 위험 자산의 단기 유동성이 급속 이탈함."],
            "data_points": ["비트코인 일일 낙폭률: 단기 -4.8% 급락하며 6만 4천 달러선 이탈", "WTI 및 브렌트 원유 인도분 급등률: 일평균 +4.2% 폭등"],
            "signal": "bearish", "signal_reason": "지정학 전쟁 리스크 폭발은 공급 인프라 훼손 및 비용 인상을 동반하여, 장기 금리 하락을 지연시키고 크립토 및 성장주 멀티플을 억누르기 때문입니다.",
            "key_companies": ["HMM", "HD현대중공업"],
            "insight": "중동 전쟁 리스크 재점화는 **해운 톤마일 상승에 따른 컨테이너/유조선 운임 폭등과 해군 특수방산선 건조 자주화 오더**로 귀결되는 조선/해운 업계의 구조적 반사이익 지표입니다.",
            "action_point": "크립토 자산 노출 한도를 축소 조율하고, 지정학 중동 물류 통행 제한의 강력한 헷지 수혜를 입는 국적 해운사 및 조선 특수선 대장주의 지분을 지켜나갑니다."
        }
    },
    "8K958q9QFf4": {
        "primary_topic": "economy", "secondary_topics": ["stock"],
        "tags": ["금리인하경고", "오건영", "연준통화정책", "매크로분석"],
        "video": {
            "id": "8K958q9QFf4", "title": "금리 인하가 반가운 소식이 아닌 이유 ,새 연준 체제가 바꾸는 게임의 룰ㅣ오건영 단장",
            "published": "2026-07-10T10:10:00+00:00", "channel_name": "이효석아카데미",
            "url": "https://www.youtube.com/watch?v=8K958q9QFf4", "thumbnail": "https://img.youtube.com/vi/8K958q9QFf4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "신한은행 오건영 단장이 출연하여, 연준의 향후 금리 인하가 경기 호황 지속 신호가 아닌 '고금리 장기화에 따른 은행권 부실 및 실물 침체 균열을 막기 위한 강제적 인하(Bad Cut)'일 확률이 높음을 경고하고 새 정책 게임의 룰을 설파합니다.",
            "key_claims": ["금리 인하가 단기 호재로 읽히나, 이면에는 중소형 상업용 은행 연체율 상승 등 시스템 균열 방어 목적이 짙음.", "시장은 더 이상 '인하 타이밍'에 환호하기보다 실제 경기 침체 진입 여부 데이터를 보며 하강 국면을 우려할 것임."],
            "data_points": ["미국 상업용 부동산 대출 은행 연체율: 사상 최고치인 4.8%로 상승세 지속", "금리 인하 개시 후 역사적 3개월 내 증시 하락 동조화 확률: 약 58% 확률 기록"],
            "signal": "bearish", "signal_reason": "실물 지표 균열에 대응한 연준의 예방적 금리 인하는 자산 밸류에이션의 변동성을 장기적으로 유도하기 때문입니다.",
            "key_companies": ["JPMorgan Chase", "Bank of America"],
            "insight": "인하 자체는 호재가 아닙니다. 경기가 부서져서 내리는 인하는 주식 시장에 가장 강력한 고점 경고등입니다. 고채무 한도를 가진 성장주는 리스크가 큽니다.",
            "action_point": "부채 비율이 높고 단기 차입 의존도가 큰 한계 성장 기업 비중을 축소하고, 부채 제로에 가까운 막강 현금 대장주로 자산을 집중합니다."
        }
    },
    "Tx4ClolaDRw": {
        "primary_topic": "economy", "secondary_topics": ["stock"],
        "tags": ["금가격전망", "번스타인보고서", "인플레이션헷지", "펩시코실적"],
        "video": {
            "id": "Tx4ClolaDRw", "title": "번스타인, 올해말 금 가격 $4533 전망ㅣ펩시코, 북미 판매량 감소에 실적 혼조세ㅣ홍키자의 매일뉴욕",
            "published": "2026-07-10T10:20:00+00:00", "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=Tx4ClolaDRw", "thumbnail": "https://img.youtube.com/vi/Tx4ClolaDRw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "번스타인(Bernstein)의 올해 말 국제 금 시세의 온스당 4,533달러 폭등 낙관론과, 미국 실물 소비 둔화를 가리키는 펩시코(PepsiCo)의 북미 유통 판매량 하락 소식을 통해 매크로 스태그플레이션 리스크를 조명합니다.",
            "key_claims": ["번스타인은 글로벌 중앙은행들의 탈달러(De-dollarization) 자산 다변화 및 실물 화폐 가치 하락으로 금의 초강세를 예상함.", "펩시코의 북미 스낵/음료 판매량 감소는 미국 서민층의 가용 소득 한계 도달 및 불황형 소비 축소를 시사함."],
            "data_points": ["번스타인 제시 연말 금 가격 타겟: 온스당 4,533달러 (역사적 최고 수준 낙관안)", "펩시코 북미 식음료 판매량(Q) 등락률: 전년 동기 대비 -3.8% 감소"],
            "signal": "bearish", "signal_reason": "실물 소비재의 판매량 감소와 실물 원자재(금 등) 강세 전망은 경기 둔화 속 고물가가 지속되는 거시경제적 부담을 뜻하기 때문입니다.",
            "key_companies": ["PepsiCo", "SPDR Gold Shares"],
            "insight": "소비재 판가 인상(P)의 한계가 다해 판매량(Q)이 줄어드는 현상은 미국 실물 소비 엔진에 균열이 생기고 있음을 보여줍니다. 금과 같은 안전 헷지 자산의 비중 증설이 유효합니다.",
            "action_point": "포트폴리오의 10% 내외에서 실물 금 ETF(GLD) 또는 원자재 연동 파킹형 자산을 안착시켜 실물 소비 둔화 리스크를 방어합니다."
        }
    },

    # CRYPTO (1 Video)
    "PGYtOifnlq0": {
        "primary_topic": "crypto", "secondary_topics": ["stock", "economy"],
        "tags": ["클래리티법안", "미국가상자산법", "비트코인상승", "규제분수령"],
        "video": {
            "id": "PGYtOifnlq0", "title": "클래리티 법안 7월 15일이 '마지막 분수령' 불발 시 비트코인 상승 모멘텀 없다 | 서동주, 김동환, 최윤영 한화투자증권 팀장 [ 크립토 PLUS ]",
            "published": "2026-07-10T10:30:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=PGYtOifnlq0", "thumbnail": "https://img.youtube.com/vi/PGYtOifnlq0/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미국 가상자산 규제 명확성 및 스테이블코인 가이드라인을 규정하는 '클래리티 법안(Clarity for Stablecoins Act)'의 7월 15일 의회 최종 승인 시한 통과 성패 시나리오와, 이것이 막혔을 때 발생할 비트코인 유동성 공급 쇼크 가능성을 다룹니다.",
            "key_claims": ["클래리티 법안은 스테이블코인 발행사의 투명성을 제도화해 전통 금융(은행) 자본 유입을 보장하는 우회로임.", "7월 15일 의회 통과 불발 시 규제 공백에 따른 미 증권거래위원회(SEC)의 추가 소송 공세가 부활하여 비트코인 상승 한계가 작용함."],
            "data_points": ["스테이블코인 글로벌 발행 총 대금 규모: 약 1,600억 달러 돌파", "법안 통과 여부에 따른 비트코인 단기 예측 밴드: 통과 시 8만 달러 안착 시도 vs 불발 시 5만 8천 달러선 리테스트 우려"],
            "signal": "neutral", "signal_reason": "법안 통과를 둘러싼 의회 내 양당 의견 대립이 팽팽하여 최종 뉴스 발표 전까지는 보수적인 관망세를 유지해야 하기 때문입니다.",
            "key_companies": ["Coinbase", "MicroStrategy"],
            "insight": "가상자산은 제도권 금융과의 규제 연계(Clarity) 속에서만 밸류에이션 확장이 가능합니다. 7월 15일 전후의 미국 의회 법안 동향 모니터링이 투자 성패의 변곡점입니다.",
            "action_point": "가상자산 및 비트코인 직접 지분의 신규 추가 매수를 일시 멈추고, 15일 법안 표결 최종 결과를 보며 비중을 기계적으로 가감합니다."
        }
    },

    # ENERGY (1 Video)
    "JXtKnYUaVtg": {
        "primary_topic": "energy", "secondary_topics": ["tech", "stock"],
        "tags": ["SK텔레콤AI", "15GW발전소", "AI인프라", "변압기수요"],
        "video": {
            "id": "JXtKnYUaVtg", "title": "SKT가 15GW AI 데이터센터를 건설하려는 이유",
            "published": "2026-07-10T10:40:00+00:00", "channel_name": "안될공학 - IT 테크 신기술",
            "url": "https://www.youtube.com/watch?v=JXtKnYUaVtg", "thumbnail": "https://img.youtube.com/vi/JXtKnYUaVtg/hqdefault.jpg"
        },
        "analysis": {
            "summary": "SK텔레콤이 15GW 분산형 친환경 전력망을 연계한 AI 데이터센터 건설 로드맵을 선언한 진짜 목적을 해부합니다. 이는 단순 서버 관리를 넘어, 고전력 전송 인프라(송전선로 및 전력 변압기 설비)를 자체 장악하여 글로벌 CSP사들 대비 비교 우위의 AI 부동산 임대 해자를 굳히기 위함입니다.",
            "key_claims": ["인공지능 데이터 처리를 위해 필요한 천문학적인 전력 공급은 일반 망으로 조달 불가능하여 분산 발전소 결합이 필수적임.", "SKT는 국내 거점의 초고압 유휴 변전소 부지와 에너지 저장 장치(ESS) 기술을 결합하는 포털 인프라를 구축하려 함."],
            "data_points": ["SKT 데이터센터 최종 전력망 가동 규모: 15GW (소형 원자력 발전 약 15기 분량의 전송 케파 확보안)", "데이터센터용 수냉식 쿨링 인프라 도입 시 기존 공랭식 대비 팬 구동 에너지 절감률: -34%"],
            "signal": "bullish", "signal_reason": "전력 병목이라는 시대적 한계 속에서 송전선 연결권을 쥔 에너지 인프라 및 변압기 소부장의 독점적 가치 우상향이 강력히 지지되기 때문입니다.",
            "key_companies": ["SK텔레콤", "효성중공업", "LS일렉트릭"],
            "insight": "반도체를 사들이던 AI 경쟁이 발전소와 송배전선로 부지를 선점하려는 물리적 부동산 전쟁으로 격화되고 있습니다. 송전 제어 기기를 독점 공급하는 국내 대형 전력 기자재사의 초장기 수혜가 뒷받침됩니다.",
            "action_point": "통신사의 배당 수입을 포트폴리오 기저에 깔며, 초고압 전선 및 가스 절연 개폐기(GIS) 생산 대장주의 중장기 투자를 확대 유지합니다."
        }
    },

    # ROBOT (1 Video)
    "JqbV4SjtmbE": {
        "primary_topic": "robot", "secondary_topics": ["tech", "stock"],
        "tags": ["휴머노이드로봇", "유비테크", "공감로봇", "양산도입"],
        "video": {
            "id": "JqbV4SjtmbE", "title": "작업용 로봇이 아니다. 공감 로봇 1만3천대 주문, 유비테크",
            "published": "2026-07-10T10:50:00+00:00", "channel_name": "엔지니어TV",
            "url": "https://www.youtube.com/watch?v=JqbV4SjtmbE", "thumbnail": "https://img.youtube.com/vi/JqbV4SjtmbE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "중국의 대표적인 휴머노이드 로봇사인 유비테크(Ubtech)가 가구 조립/순찰 등 기계적 단순 노동을 넘어, 요양 병원 및 가정 내에서 돌봄과 정서적 교감을 수행하는 3D 공감형 휴머노이드 로봇 '워커S(Walker S)' 라인업의 13,000대 대량 실전 상업 양산 주문을 획득한 의의와 공급망 낙수를 파헤칩니다.",
            "key_claims": ["단순 연구용 모형을 탈피해 B2B 실전 돌봄 및 물류 서비스 라인에 1만 대 이상 동시 배치되는 세계 첫 상업 성과임.", "로봇 구동 관절에 필요한 정밀 모터, 다축 하모닉 감속기 및 3D 라이더 정밀 센서 소부장 오더가 본격 개시됨."],
            "data_points": ["유비테크 휴머노이드 로봇 수주 확정 수량: 13,000대 누적 오더 확보", "로봇 1대당 탑재되는 정밀 서보모터 및 감속기 개수: 평균 32개 관절 구동 적용"],
            "signal": "bullish", "signal_reason": "휴머노이드 로봇의 대량 생산 오더 확인은 로보틱스 감속기 및 구동 제어 모터 등 핵심 부품사들의 실질 실적 숫자가 급상승하는 팩트 구간이기 때문입니다.",
            "key_companies": ["UBTECH Robotics", "에스피지", "레인보우로보틱스"],
            "insight": "휴머노이드 로봇 13,000대 대량 주문은 서비스 로봇의 캐즘 돌파를 뜻하는 역사적 지표입니다. 다축 감속기와 물리 제어 정밀 센서를 공급하는 핵심 소부장 기업들의 동반 성장이 기대됩니다.",
            "action_point": "로봇 감속기 정밀 기어 제조 원천 특허를 가진 소부장 우량 핵심주 및 대형 제조사향 감속기 공급사들의 지분 비중을 적극 확대 조절합니다."
        }
    },

    # ETC (5 Videos)
    "1wrdc8_rBVw": {
        "primary_topic": "etc", "secondary_topics": ["economy"],
        "tags": ["교육제도", "학교공학", "사회구조", "인적자원"],
        "video": {
            "id": "1wrdc8_rBVw", "title": "학교는 원래 노는 곳이었다",
            "published": "2026-07-10T11:00:00+00:00", "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=1wrdc8_rBVw", "thumbnail": "https://img.youtube.com/vi/1wrdc8_rBVw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "산업혁명 초기 공장식 규율에 길들여진 인적 자원을 길러내기 위해 변형되었던 근대 공교육 제도의 역사적 기원과, 미래 창의성 시대로 가기 위해 본래의 자율 교감 및 사회성 발달 공간(노는 곳)으로 학교의 기능이 전면 개편되어야 하는 교육 공학적 당위성을 다룹니다.",
            "key_claims": ["획일적 주입식 공교육은 과거 단순 노동자 양성소 기능에 머물러 미래 AI 인재 양성에 완전히 부적합함.", "학생 주도형 자율 탐색 및 협업 위주로의 학교 공간 구조 개편이 인구 절벽 속의 필수적 인적 자원 생존 조건임."],
            "data_points": ["한국 공교육 예산 GDP 대비 비중: 약 4.8%로 OECD 상위권 수준", "AI 대체율이 가장 높은 직업군을 교육하는 전통 인문/상업계 직업 훈련 과정 비중: 여전히 전체 교과 비중의 62% 차지"],
            "signal": "na", "signal_reason": "교육 제도 및 역사적 사료 비판 다큐멘터리이므로, 개별 금융 투자 시장에 미치는 유의미한 영향은 없습니다.",
            "key_companies": ["메가스터디"],
            "insight": "교육 제도의 획일성은 결국 국가 혁신 역량을 갉아먹는 제도적 장벽입니다. 데이터 기반 맞춤형 개별 에듀테크 및 창의 솔루션을 제공하는 교육 플랫폼의 질적 차별화가 요구됩니다.",
            "action_point": "투자 대상과는 무관하므로 교양 획득 차원에서 청취를 마치고 추가 포트폴리오 대응은 배제합니다."
        }
    },
    "BncpRRarR1g": {
        "primary_topic": "etc", "secondary_topics": ["tech"],
        "tags": ["개인정보유출", "쿠팡티빙", "소송배상금", "사이버보안"],
        "video": {
            "id": "BncpRRarR1g", "title": "티빙 쿠팡서 개인정보 털렸나요? 소송하면 10만원씩 받습니다 (언더스탠딩 백종훈 기자)",
            "published": "2026-07-10T11:10:00+00:00", "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=BncpRRarR1g", "thumbnail": "https://img.youtube.com/vi/BncpRRarR1g/hqdefault.jpg"
        },
        "analysis": {
            "summary": "최근 대형 OTT 플랫폼과 커머스 기업의 데이터베이스 침투로 유출된 개인정보 집단 소송 진행 현황과, 법원의 위자료 판결 가이드라인(1인당 평균 10만 원 배상)에 따른 기업들의 실질 재무 충격 및 기업 보안 투자 강제 조치를 짚어봅니다.",
            "key_claims": ["가입자 수백만 명의 집단 소송 시, 1인당 10만 원 위자료는 기업에게 수천억 원대 치명적 배상금 리스크로 환원됨.", "결국 대형 인터넷/커머스 플랫폼사들이 사법 리스크 회피를 위해 클라우드 암호화 보안 시스템 투자를 대대적으로 늘릴 수밖에 없음."],
            "data_points": ["쿠팡/티빙 집단 소송 예상 신청 인원: 총 12만 명 이상 접수 중", "법적 확정 시 예상 총배상 판결 대금 규모: 기업당 최소 120억 원에서 최대 340억 원 범위 발생"],
            "signal": "neutral", "signal_reason": "개별 플랫폼 기업들의 단기 충당금 설정 우려는 존재하나, 역설적으로 기업 사이버 보안 솔루션 업계의 수주 증가를 자극하기 때문입니다.",
            "key_companies": ["안랩", "파수", "쿠팡"],
            "insight": "데이터 보안 실패는 단순 평판 저하를 넘어 사법적 현금 파멸 리스크로 작동합니다. 플랫폼사들은 데이터 무단 침입을 차단하는 통합 클라우드 보안 시스템 구축에 투자를 적극 늘려야 생존합니다.",
            "action_point": "집단 소송 타격을 입는 일부 인터넷 플랫폼의 비중을 조율하고, 보안 모듈 솔루션을 독점 제공하는 보안 전용 기술주 비중을 유지합니다."
        }
    },
    "F-UgZE6QZiQ": {
        "primary_topic": "etc", "secondary_topics": ["economy"],
        "tags": ["도시방제공학", "침수방지", "배수시스템", "도시공학"],
        "video": {
            "id": "F-UgZE6QZiQ", "title": "도시가 물에 잠기지 않게 하는 방법",
            "published": "2026-07-10T11:20:00+00:00", "channel_name": "안될공학 - IT 테크 신기술",
            "url": "https://www.youtube.com/watch?v=F-UgZE6QZiQ", "thumbnail": "https://img.youtube.com/vi/F-UgZE6QZiQ/hqdefault.jpg"
        },
        "analysis": {
            "summary": "기습 폭우 및 장마철 도심 대홍수를 제어하는 대심도 빗물 배수 터널(Deep Tunnel) 및 스마트 수문 방제 시스템의 작동 원리와, 인구 밀집 도심지의 침수 피해 차단을 위한 토목/IT 연동 방제 인프라 공학을 설명합니다.",
            "key_claims": ["기존 도로 아스팔트 배수구 용량은 시간당 50mm 폭우 시 차단 한계에 직면하여 지하 대심도 보관 저류조가 필수적임.", "실시간 침수 감지 센서 및 AI 스마트 수문 개폐 제어 시스템이 방제 공학의 핵심으로 결합됨."],
            "data_points": ["대심도 빗물 터널(강남역 설계 기준) 최대 처리 용량: 시간당 100mm 폭우 수용 목표", "빗물 유입 제어용 초당 배출 펌프 모터 전력량: 개당 5,000마력급 초고압 배수 모터 설치"],
            "signal": "na", "signal_reason": "도심 방제 토목 공학 기술 설명이며, 상업적 주식 시장에 미치는 유의미한 영향은 유발하지 않기 때문입니다.",
            "key_companies": ["현대로템", "한화오션"],
            "insight": "도심 기후 재해 방제 예산 증설은 특수 배수 터널 토목 및 고용량 배수 펌프/모터 시스템 수주를 창출합니다. 정밀 펌프 밸류체인에 장기 긍정적입니다.",
            "action_point": "토목 방제 인프라 수혜 대형 건설 및 특수 중공업 주기기 공급사들의 잔존 수주를 모니터링하는 것으로 갈음합니다."
        }
    },
    "FgBlwFtulBc": {
        "primary_topic": "etc", "secondary_topics": ["tech"],
        "tags": ["우천시통신", "주파수감쇄", "Wi-Fi산란", "통신공학"],
        "video": {
            "id": "FgBlwFtulBc", "title": "비가 많이 올 때 데이터가 끊기는 이유?",
            "published": "2026-07-10T11:30:00+00:00", "channel_name": "안될공학 - IT 테크 신기술",
            "url": "https://www.youtube.com/watch?v=FgBlwFtulBc", "thumbnail": "https://img.youtube.com/vi/FgBlwFtulBc/hqdefault.jpg"
        },
        "analysis": {
            "summary": "우천 시 공기 중에 존재하는 조밀한 물방울들이 무선 데이터 통신 전파(특히 5GHz Wi-Fi 및 28GHz 고주파 대역)의 파장을 차단 및 산란(Scattering)시켜 패킷 유실을 동반하는 전자기학적 감쇄 원리를 다룹니다.",
            "key_claims": ["물 분자의 공진 주파수(2.4GHz)가 무선 Wi-Fi 주파수 대역과 겹쳐 빗물에 데이터 신호 에너지가 대거 흡수 감쇄됨.", "도심 내 고주파 중계기 사이의 가시거리(LoS) 확보와 비에 강한 저주파(Sub-6) 보조 주파수 설계의 결합 필요성이 확대됨."],
            "data_points": ["강수량 시간당 20mm 증가 시 고주파(28GHz) 통신 신호 도달 거리 감소율: 맑은 날 대비 최대 22% 감소", "신호 왜곡 보정용 빔포밍 스마트 안테나의 실시간 전력 이득 보상 강도: 비가 올 때 평균 4dB 증가 구동"],
            "signal": "na", "signal_reason": "통신 무선 주파수 신호 간섭 물리학을 해설한 기초 공학 교육 영상이며 개별 통신사 실적 충격은 낮기 때문입니다.",
            "key_companies": ["케이엠더블유", "삼성전자"],
            "insight": "기후 변동에 대항하는 무선 통신 신뢰성 확보는 중계기용 RF 안테나 필터 및 지능형 빔포밍 소부장의 기술 고도화를 유도하는 구조적 기폭제입니다.",
            "action_point": "통신 장비 부품사의 기술 경쟁력을 점검하며, 장기 무선 통신 인프라 국산화 오더 일정을 주시합니다."
        }
    },
    "pGu6-1epvsw": {
        "primary_topic": "etc", "secondary_topics": ["economy"],
        "tags": ["노후준비", "자산관리", "연금연계", "공강"],
        "video": {
            "id": "pGu6-1epvsw", "title": "2030노후준비 vs 4050노후준비 | 공강 | 토크룸",
            "published": "2026-07-10T11:40:00+00:00", "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=pGu6-1epvsw", "thumbnail": "https://img.youtube.com/vi/pGu6-1epvsw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "세대별(청년층 2030 vs 중장년층 4050) 노후 자산 관리의 본질적 목표 차이를 분석하고, 2030은 복리 효과 극대화를 위한 성장주/지수 연동 적립식 투자를, 4050은 원금 손실을 제한하고 즉시 캐시플로우를 뽑아내는 배당/연금 연계 인컴 구조로의 포트폴리오 최적화 로드맵을 제안합니다.",
            "key_claims": ["2030 세대는 긴 투자 시계를 활용해 단기 하락을 견디는 복리 연금 적립(지수 ETF)에 집중해야 함.", "4050 세대는 은퇴 즉시 매월 고정 인컴을 보장하는 연금저축펀드(IRP) 및 고배당 커버드콜 상품 비중 배치가 정석임."],
            "data_points": ["4050 세대의 은퇴 시 필요한 최소 월평균 기대 소득: 부부 기준 약 320만 원 수준", "연금저축펀드 과세 이연을 활용한 복리 누적 세액 절감 기대치: 연간 최대 99만 원 한도 혜택"],
            "signal": "na", "signal_reason": "연령대별 재무 설계 및 연금 포트폴리오 구성 교육 토크쇼 영상이며, 단기 단일 종목 투자 영향은 없기 때문입니다.",
            "key_companies": ["미래에셋자산운용"],
            "insight": "인구 고령화 시대에 개인의 연금저축 및 월배당 IRP 시장 규모는 거대해질 수밖에 없습니다. 고배당 월배당 자산 및 지수 연동 연금 상품을 공급하는 운용사 밸류가 강화됩니다.",
            "action_point": "연령별 재무 규칙에 맞추어 본인의 IRP 세액 공제 납입 한도를 확인 채우고, 배당 재투자 포트를 안정 유지합니다."
        }
    },
    "uIPJ1a0VgPM": {
        "primary_topic": "etc", "secondary_topics": ["economy"],
        "tags": ["강남침수", "침수재현", "도시안전", "방제공학"],
        "video": {
            "id": "uIPJ1a0VgPM", "title": "강남 침수 100% 재현, 몸으로 직접 들어갔습니다",
            "published": "2026-07-10T11:50:00+00:00", "channel_name": "안될과학 Unrealscience",
            "url": "https://www.youtube.com/watch?v=uIPJ1a0VgPM", "thumbnail": "https://img.youtube.com/vi/uIPJ1a0VgPM/hqdefault.jpg"
        },
        "analysis": {
            "summary": "강남역 등 도심 상습 침수 구역의 100% 모형 실험장을 찾아 물이 정강이 높이까지 차올랐을 때 유속과 수압이 인간의 탈출 제어력 및 차량의 시동 꺼짐 유도를 어떻게 유발하는지 몸소 체험하며 스마트 도시 방제 인프라의 필요성을 대중적으로 설파합니다.",
            "key_claims": ["수심이 30cm에 불과하더라도 유속이 시속 10km를 넘는 순간 성인도 문을 열 수 없는 유압 장벽이 작동함.", "침수 감지 시 하수구 빗물 뚜껑의 기계적 막힘을 예방하는 자동 세정 개폐 장치의 대대적인 매설이 시급함."],
            "data_points": ["침수 유발 수심 임계값: 타이어 중심선 기준 30cm 도달 시 엔진 에어클리너 내 빗물 흡입으로 시동 정지 돌입", "유수 탈출 한계 압력 수치: 수위 40cm 도달 시 문 1개당 평균 120kg의 정수압 방해 발생"],
            "signal": "na", "signal_reason": "도심 방제 실험 및 일상 침수 탈출 안전 교육 콘텐츠이므로, 개별 금융 투자 자산에 미치는 유의미한 영향은 없습니다.",
            "key_companies": ["한국건설기술연구원"],
            "insight": "기후 이변 폭우 빈도 증가는 지능형 침수 경보 IoT 모듈 및 고신뢰성 도심 배수 부품 수주를 필연적으로 견인합니다.",
            "action_point": "투자 대상과는 무관하므로 우기 안전 요령을 숙지하고 추가적인 포트폴리오 조율은 배제합니다."
        }
    }
}

# Ensure analyzed subdirectories exist and write JSON files
for vid, data in batch_data.items():
    topic = data["primary_topic"]
    dest_path = analyzed_dir / topic / f"{vid}.json"
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    output_json = {
        "video": data["video"],
        "analysis": data["analysis"],
        "classification": {
            "primary_topic": data["primary_topic"],
            "secondary_topics": data["secondary_topics"],
            "tags": data["tags"]
        }
    }
    
    dest_path.write_text(json.dumps(output_json, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated data/analyzed/{topic}/{vid}.json")

print("\nSuccessfully generated 37 analyzed JSON files.")
