import json
from pathlib import Path

# Setup paths
base_dir = Path("c:/Users/ddong/OneDrive/Desktop/회사업무/analyze1/youtube-insight")
analyzed_dir = base_dir / "data/analyzed"

batch_data = {
    "-7FvjF7Qqro": {
        "primary_topic": "tech",
        "secondary_topics": ["stock", "economy"],
        "tags": ["AI버블론", "빅테크CapEx", "AI수익성", "수익모델부재"],
        "video": {
            "id": "-7FvjF7Qqro",
            "title": "AI companies are in big trouble",
            "published": "2026-07-08T06:00:00+00:00",
            "channel_name": "Softdragon SOD",
            "url": "https://www.youtube.com/watch?v=-7FvjF7Qqro",
            "thumbnail": "https://img.youtube.com/vi/-7FvjF7Qqro/hqdefault.jpg"
        },
        "analysis": {
            "summary": "글로벌 테크 시장에서 실질적인 비즈니스 모델이나 뚜렷한 매출 성과 없이 천문학적인 인프라 비용(CapEx)을 지출하고 있는 생성형 AI 버블에 대한 경고를 다룹니다. 오픈AI를 비롯한 다수의 AI 스타트업들이 매년 수십억 달러의 적자를 기록하고 있으며, 투자 금액 대비 매출 회수(ROI) 시점이 예상보다 지연되면서 벤처 캐피탈(VC) 및 빅테크들의 투자 속도 조절 가능성이 대두되고 있습니다.",
            "key_claims": [
                "AI 서비스의 연산 비용(API, 인프라)이 사용자당 매출을 압도하여 서비스가 커질수록 적자가 심화되는 구조적 모순이 존재함.",
                "대기업(빅테크) 외의 독립 AI 스타트업들은 추가 펀딩 실패 시 현금 고갈(Runway 끝) 위험에 노출되어 있음.",
                "시장은 더 이상 기술력의 혁신성만 보지 않고 실제 현금 흐름을 창출하는 비즈니스 솔루션 검증을 요구함."
            ],
            "data_points": [
                "오픈AI 연간 인프라 비용 추정치: 약 40억~50억 달러 적자 누적",
                "일부 AI API 서비스의 수익성: 매출 1달러 발생 시 운영비용 1.2달러 이상 소요"
            ],
            "signal": "bearish",
            "signal_reason": "AI 소프트웨어 진영의 수익성 한계가 드러나면서 상반기 지수를 견인한 AI 관련 고PER 기술주들의 밸류에이션 리레이팅 리스크가 가중되고 있습니다.",
            "key_companies": ["OpenAI", "Microsoft", "Google"],
            "insight": "엔비디아 칩 기반의 서버 인프라 구축 단계(1단계)에서 실제 소프트웨어 서비스 매출 창출 단계(2단계)로의 이행이 지체되고 있습니다. 이는 궁극적으로 전방 AI 하드웨어 칩 구매 속도 둔화로 이어질 수 있어 포트폴리오의 보수적 대응이 필요합니다.",
            "action_point": "빅테크 및 반도체 섹터의 비중을 일부 조율하고, AI 솔루션을 통해 실질적인 비용 절감을 검증받은 기업으로 타겟을 좁힐 필요가 있습니다."
        }
    },
    "4H2wm7AaKlU": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["아이폰18프로", "퀄컴모뎀칩", "애플모뎀자립화", "TSMC파운드리"],
        "video": {
            "id": "4H2wm7AaKlU",
            "title": "아이폰18프로 미국판만 퀄컴 칩 쓴다?",
            "published": "2026-07-08T07:15:00+00:00",
            "channel_name": "안될공학 - IT 테크 신기술",
            "url": "https://www.youtube.com/watch?v=4H2wm7AaKlU",
            "thumbnail": "https://img.youtube.com/vi/4H2wm7AaKlU/hqdefault.jpg"
        },
        "analysis": {
            "summary": "애플의 5G 모뎀칩 독자 개발 및 양산 로드맵의 차질로 인해, 아이폰 18 프로 모델 중 북미 유통용 제품에 한하여 여전히 퀄컴(Qualcomm)의 모뎀칩이 독점 탑재될 가능성과 글로벌 공급망 변화를 규명합니다. 애플은 오랜 기간 모뎀칩 자립화를 추진했으나 안테나 신호 왜곡 제어 및 특허 우회 난제로 양산 수율 확보에 어려움을 겪고 있으며, 결국 핵심 프리미엄 라인업에서는 안전한 수급을 위해 퀄컴 의존을 이어갈 전망입니다.",
            "key_claims": [
                "애플이 수년째 추진 중인 독자 5G 모뎀 개발 프로젝트가 안테나 물리 간섭 및 글로벌 주파수 커버리지 문제로 연기됨.",
                "퀄컴은 이에 따라 고마진 프리미엄 아이폰 라인업의 모뎀 공급권 독점을 연장하며 안정적인 캐시카우를 보장받음.",
                "TSMC 3나노/2나노 공정을 활용한 애플의 칩 다변화 전략은 파운드리 독점 지배력을 강화하는 역효과를 냄."
            ],
            "data_points": [
                "애플의 퀄컴 모뎀 수급 비중: 프리미엄 프로 라인업의 북미 유통 물량 100% 퀄컴 칩 탑재 전망",
                "애플 독자 모뎀 양산 목표 시점: 당초 2025년에서 2027년 이후로 재연기"
            ],
            "signal": "bullish",
            "signal_reason": "독점적 모뎀 칩셋 지배력을 보유한 퀄컴의 프리미엄 판로 유지 및 로열티 매출 방어가 강력하게 검증되었기 때문입니다.",
            "key_companies": ["Qualcomm", "Apple", "TSMC"],
            "insight": "모바일 AP 외에 통신 모뎀칩 분야는 무선 RF 안테나 특허 장벽과 주파수 신호 제어 기술 해자가 매우 높습니다. 애플조차 단기간에 자립화에 실패했다는 사실은 퀄컴의 장기적인 라이선스/로열티 사업 안정성을 강력히 보장하는 지표입니다.",
            "action_point": "단기 퀄컴 우려 해소에 따라 퀄컴 지분의 비중 확대를 저울질하며, 수혜를 입는 TSMC 파운드리 밸류체인 수주 모멘텀을 주시합니다."
        }
    },
    "9HJsIgWIZGc": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["매크로패러다임", "성장주수급", "금리둔화", "기업실적중심"],
        "video": {
            "id": "9HJsIgWIZGc",
            "title": "The stock market paradigm has completely changed... 'This' is now more important than interest ra...",
            "published": "2026-07-08T08:00:00+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=9HJsIgWIZGc",
            "thumbnail": "https://img.youtube.com/vi/9HJsIgWIZGc/hqdefault.jpg"
        },
        "analysis": {
            "summary": "글로벌 매크로의 관심사가 연준의 금리 인하 타이밍(Inflation)에서 기업들의 '이익 성장률(EPS Growth)' 및 실물 경기 둔화 방어로 완전히 이동했음을 경고합니다. 물가가 제어 범위에 들어오며 기준 금리의 추가 인상 리스크가 차단된 이상, 이제는 금리 수준 자체보다 기업들이 AI 및 차세대 산업 투자를 통해 실질 성장을 내고 있는지가 멀티플 지지의 유일한 근거입니다.",
            "key_claims": [
                "연준의 금리 인하 여부는 호재가 아닌 경기 침체 헤징용 예방 조치로 읽혀 시장에 미치는 영향력이 예전만 못함.",
                "실제 주가를 견인하는 유일한 모멘텀은 장기 EPS 성장성(실적 장세)으로 패러다임이 전격 전환됨.",
                "고금리 기조 장기화 속에서도 막강한 영업 현금 흐름을 뽑아내는 빅테크의 독점적 지위가 자금 쏠림을 더욱 유도함."
            ],
            "data_points": [
                "S&P 500 내 상위 7대 빅테크 이익 기여도: 전체 EPS 성장률의 약 60% 차지",
                "미국 10년물 국채 금리 안정 밴드: 4.0% ~ 4.2% 사이에서 변동성 수렴"
            ],
            "signal": "neutral",
            "signal_reason": "매크로 불확실성은 감소했으나, 철저한 실적 위주 장세로의 전환에 따라 실적이 받쳐주지 못하는 낙폭과대 중소형주들의 소외 현상이 지속될 수 있습니다.",
            "key_companies": ["Apple", "Nvidia", "Microsoft"],
            "insight": "성장 정체 구간에 진입한 좀비 기업들의 주가 하락과 실적 대장주의 지수 독식이 극명해지는 '지수 왜곡 및 양극화' 현상입니다. 금리 인하에 기대어 부채 비율이 높은 가치주나 리츠를 뇌동 매수하기보다, 현금창출력이 강력한 독점 1등 주식에 지분을 유지하는 정석 투자가 요구됩니다.",
            "action_point": "유동성 위주 투자를 중단하고, 분기 실적 가이드가 우상향하는 반도체 및 핵심 소비재 1등 주식으로 포트폴리오를 압축합니다."
        }
    },
    "biZ2uf5H7xM": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "shipbuilding", "economy"],
        "tags": ["오펜하이머S&P8100", "딥시크자체칩", "호르무즈해협긴장", "해상물류리스크", "홍키자"],
        "video": {
            "id": "biZ2uf5H7xM",
            "title": "오펜하이머 \"연말 S&P500 8100\"ㅣ中딥시크 \"자체 칩 개발중\" 보도ㅣ이란, 호르무즈 해협에서 선박 공격 재개ㅣ홍키자의 매일뉴욕",
            "published": "2026-07-08T08:30:00+00:00",
            "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=biZ2uf5H7xM",
            "thumbnail": "https://img.youtube.com/vi/biZ2uf5H7xM/hqdefault.jpg"
        },
        "analysis": {
            "summary": "연말 S&P500의 8,100포인트 초강세 낙관론, 중국 딥시크(DeepSeek)의 독자 AI 칩 설계 진입 보도, 그리고 이란에 의한 호르무즈 해협의 민간 상선 피격 재개가 글로벌 해운 및 원자재 시장에 미칠 지정학적 파장을 분석합니다. 지정학적 리스크 심화는 공급망을 자극하여 원자재가 상승 및 선박 운임 상승을 주도할 것입니다.",
            "key_claims": [
                "오펜하이머는 자본 유동성의 기술주 쏠림과 기업 생산성 향상을 근거로 S&P 500 연말 가이던스를 역사적 고점인 8,100으로 상향함.",
                "중국 딥시크가 미국의 대중 반도체 장벽을 우회하기 위해 자체 아키텍처 기반 AI 가속 칩셋 설계를 개시하여 자립 노선을 개척 중임.",
                "이란 혁명수비대가 호르무즈 해협을 지나는 민간 유조선 및 상선에 무인 드론 피격을 재개함에 따라 아시아-유럽 해역 해운 운임이 급증세를 맞이함."
            ],
            "data_points": [
                "오펜하이머 가이드: 연말 S&P 500 타겟 8,100 포인트 제시 (업계 최고치)",
                "호르무즈 통행 제한에 따른 상해컨테이너운임지수(SCFI) 급등률: 단기 8.4% 반등"
            ],
            "signal": "neutral",
            "signal_reason": "글로벌 유동성의 낙관론과 기술 자립 시도는 증시에 호재이나, 호르무즈 해협의 실질 물리 충돌 위기가 전 세계 공급망 비용 인상을 촉발해 물가 둔화 속도를 저해하고 해운 운임 상승을 동시에 자극하기 때문입니다.",
            "key_companies": ["DeepSeek", "Oppenheimer", "HMM", "한화오션"],
            "insight": "중동 긴장 재발은 해운/조선업계에 다시 한번 **선박 우회로에 따른 톤마일 상승 및 친환경 고효율 선박 가치 상승**이라는 구조적 모멘텀을 주입합니다. 또한 미 대선 정국과 엮인 이란의 통제 강도는 해상 안보 동맹의 한계를 드높여 특수선 방산 수주전에서의 자주 국방 수요를 견인하게 됩니다.",
            "action_point": "유조선 및 컨테이너 운임 상승의 수혜를 입는 국적선사(HMM 등) 및 특수선 건조 조선사(한화오션 등)의 주가 하방 지지력을 보며 해운/조선 섹터 비중을 유지 및 관리합니다."
        }
    },
    "d_86wrA2qMI": {
        "primary_topic": "space",
        "secondary_topics": ["tech", "economy"],
        "tags": ["차세대중형위성4호", "정밀지상관측", "우주발사체", "위성국산화"],
        "video": {
            "id": "d_86wrA2qMI",
            "title": "South Korea's Next-Generation Medium Satellite 4 Successfully Launched into Space",
            "published": "2026-07-08T09:00:00+00:00",
            "channel_name": "안될과학 Unrealscience",
            "url": "https://www.youtube.com/watch?v=d_86wrA2qMI",
            "thumbnail": "https://img.youtube.com/vi/d_86wrA2qMI/hqdefault.jpg"
        },
        "analysis": {
            "summary": "한국의 독자 기술로 개발된 정밀 지상 관측용 '차세대 중형 위성 4호'의 성공적인 우주 궤도 진입 과정과 이로 인한 국내 우주 인프라 자립화 성과를 상세히 다룹니다. 농업 지형 모니터링, 해양 수질 감시, 산불 방제 등 국토 전반의 실시간 고해상도 영상을 독자 획득함으로써 수입 위성 이미지 의존도를 획기적으로 낮추었습니다.",
            "key_claims": [
                "차세대 중형 위성 4호는 국내 독자적인 탑재체 설계와 본체 조립 기술을 100% 적용하여 국산화율을 극대화함.",
                "지상 500m 해상도의 고화질 광학 분석 성능을 보유하여 재해 예측 및 해양 안보 통제력을 대폭 향상시킴.",
                "한국항공우주연구원과 민간 대기업(KAI 등)의 우주 파트너십 구축이 실전 위성 궤도 배치로 입증됨."
            ],
            "data_points": [
                "위성 탑재 지상 해상도: 50cm급 초정밀 광학 센서 탑재",
                "우주 궤도 고도: 약 497.8km 원궤도 안착 완료"
            ],
            "signal": "bullish",
            "signal_reason": "정부 주도의 대규모 국산 위성 발사 성공은 지상 수신국 및 정밀 소부장, 탑재체 조립을 맡은 국내 항공우주 기자재 기업들의 수주 안정성을 보장하기 때문입니다.",
            "key_companies": ["KAI", "한화시스템", "한국항공우주연구원"],
            "insight": "한국의 독자 위성 발사 연속 성공은 단순 과학 기술 연구를 넘어 상업용 민간 위성 건조 대행 비즈니스로 확장할 수 있는 신뢰성의 궤도(Track Record)를 완성했음을 뜻합니다. K-방산의 안보 자주화 기치와 결합하여 정밀 우주 탑재체 밸류체인의 낙수 효과가 기대됩니다.",
            "action_point": "항공우주 정밀 탑재체 부품사 및 위성 본체 건조 시스템 주도 기업들을 대상으로 중장기적 분할 적립 투자를 검토합니다."
        }
    },
    "EMxWyl7dpME": {
        "primary_topic": "etc",
        "secondary_topics": ["tech"],
        "tags": ["장마철공학", "제습기술", "주파수간섭", "수막현상"],
        "video": {
            "id": "EMxWyl7dpME",
            "title": "장마 속에 숨은 기술 이야기 | 우산·자동차·통신·도시를 움직이는 공학 비가 오면 인터넷이 느려진다? | 당신이 몰랐던 장마철 공학 이야기",
            "published": "2026-07-08T09:30:00+00:00",
            "channel_name": "안될공학 - IT 테크 신기술",
            "url": "https://www.youtube.com/watch?v=EMxWyl7dpME",
            "thumbnail": "https://img.youtube.com/vi/EMxWyl7dpME/hqdefault.jpg"
        },
        "analysis": {
            "summary": "장마철 고온 다습한 기후 환경에서 발생하는 다양한 일상 속 과학 법칙과 정보 통신 기기의 수신 지연(비가 올 때 공기 중 물방울에 의한 2.4GHz/5GHz 전파 산란 현상), 자동차 수막현상(Hydroplaning)의 타이어 공학적 해결책 등을 알기 쉽게 해설합니다.",
            "key_claims": [
                "대기 중 빗방울 밀도 급증 시 스마트폰 및 Wi-Fi 전파의 굴절과 산란이 극대화되어 일시적인 데이터 패킷 손실이 유발될 수 있음.",
                "제습기의 컴프레셔 구동 원리 및 나노 발수 우산 코팅 기술 등 장마철 생필품의 숨겨진 화학/물리 해자가 존재함.",
                "도심 아스팔트 배수 시스템의 배수 용량 설계 한계와 침수 감지 IoT 센서 도입 필요성이 확대됨."
            ],
            "data_points": [
                "빗방울 투과 시 5GHz 대역 통신 신호 감쇄율: 맑은 날 대비 최대 12% 증가",
                "수막현상 방지 타이어 트레드 배수 설계 한계 속도: 시속 80km 이상 급회전 시 작동 한계 도달"
            ],
            "signal": "na",
            "signal_reason": "장마철 기후 특성을 분석한 일상적 과학 다큐멘터리이며, 직접적인 주식 시장 투자 모멘텀 유발 가능성은 낮기 때문입니다.",
            "key_companies": ["한국타이어", "LG전자"],
            "insight": "기후 변동성이 극대화되는 여름철에는 전기차의 배터리 열관리 시스템 안전성과 빗길 제동 타이어 소부장의 신뢰성이 주요 기업의 브랜드 품질 평가 분수령으로 작동할 수 있습니다.",
            "action_point": "실 투자 비중 관여보다는 장마철 수혜를 누리는 가전 서비스 센터 및 자동차 정밀 점검 부품 수요 상승 등의 단기 유통 밸류 체인을 지켜보는 것으로 갈음합니다."
        }
    },
    "LHLg1_mz0Pc": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["뉴욕오피스", "상업용부동산", "빌딩양극화", "원격근무퇴조"],
        "video": {
            "id": "LHLg1_mz0Pc",
            "title": "[어바웃 뉴욕] 뉴욕 오피스는 죽었다는데, 이 빌딩에만 줄을 섭니다 | 써밋 vs 엠파이어스테이트 | 이나연 특파원",
            "published": "2026-07-08T10:00:00+00:00",
            "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=LHLg1_mz0Pc",
            "thumbnail": "https://img.youtube.com/vi/LHLg1_mz0Pc/hqdefault.jpg"
        },
        "analysis": {
            "summary": "원격 근무 유행으로 상업용 부동산 위기가 거론되는 뉴욕 맨해튼에서 최신 랜드마크 빌딩(써밋 원 밴더빌트 등)으로만 글로벌 기업 임차와 관광객 유동 인구가 몰려드는 '상업용 오피스 시장의 극단적 초양극화(Flight to Quality)'를 짚어봅니다. 노후화된 구형 오피스의 공실률은 20%를 돌파하는 반면, 친환경 인증과 최신 어메니티를 갖춘 최상급 오피스는 임대료 사상 최고가를 경신하고 있습니다.",
            "key_claims": [
                "뉴욕 오피스 위기는 평균 수치일 뿐, 1%의 프리미엄 프라임 빌딩은 대기 임차 수요가 넘쳐나 임대료가 급등세임.",
                "대기업들은 복귀(RTO) 유도를 위해 쾌적하고 조망이 뛰어난 친환경 인증 신축 오피스를 선호함.",
                "관광 전망대 비즈니스(써밋 등)가 빌딩 자체의 연간 캐시카우 수입의 30% 이상을 메워주는 복합 모델로 정착함."
            ],
            "data_points": [
                "맨해튼 프라임 빌딩 임대 점유율: 공실률 5% 미만 유지",
                "1970년대 건축된 뉴욕 노후 오피스 공실률: 평균 22.4% 도달"
            ],
            "signal": "neutral",
            "signal_reason": "전체 상업용 부동산 대출 연체율이 상존해 금융권 리스크는 잔존하지만, 프라임 오피스를 소유한 우량 리츠 및 부동산 투자 펀드의 실적 차별화가 진행되고 있기 때문입니다.",
            "key_companies": ["SL Green", "Vornado Realty Trust"],
            "insight": "상업용 자산의 가치는 '위치'를 넘어 '스펙(에너지 효율, 사원 편의성)'에 의해 격차가 결정되는 시대입니다. 리츠 투자를 진행할 때 단순 고배당률에 속지 말고, 자산 포트폴리오의 노후 빌딩 비중을 면밀히 선별해 청산해야 생존할 수 있습니다.",
            "action_point": "보유 리츠 중 구형 맨해튼 중심가 오피스 위주의 자산은 비중을 덜어내고, 프라임급 복합 자산으로 리포지셔닝하는 자산 방어를 취합니다."
        }
    },
    "LJkOaGkVqkE": {
        "primary_topic": "tech",
        "secondary_topics": ["stock", "economy"],
        "tags": ["AI투자피로감", "CapEx우상향", "엔비디아독점역효과", "빅테크마진"],
        "video": {
            "id": "LJkOaGkVqkE",
            "title": "[Kim Jong-hak's New York, Now - July 8] Spreading Concerns Over Sustained AI Investment | Success...",
            "published": "2026-07-08T10:30:00+00:00",
            "channel_name": "한경 글로벌마켓",
            "url": "https://www.youtube.com/watch?v=LJkOaGkVqkE",
            "thumbnail": "https://img.youtube.com/vi/LJkOaGkVqkE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "빅테크 기업들이 AI 칩셋 구매 및 데이터센터 전력망 확보를 위해 자본 지출을 전례 없이 늘리고 있으나, 이에 상응하는 소프트웨어 매출 증가율이 꺾이면서 미국 기관 투자자들 사이에서 'AI 투자 피로감(AI Fatigue)'과 설비 투자 속도 조절론이 확산되는 뉴욕 현지 기류를 전합니다.",
            "key_claims": [
                "마이크로소프트, 알파벳 등 주요 빅테크의 2분기 실적 가이드 발표 이후 주가가 단기 조정을 겪는 이유는 CapEx 급증 대비 영업이익률의 플랫화 때문임.",
                "엔비디아의 AI 가속기 지배력이 여전하여 빅테크가 마진 독점을 엔비디아에 빼앗기는 구도가 고착됨.",
                "향후 3년간 빅테크가 AI 인프라에 1조 달러 이상 투자해야 한다는 가정이 실제 수요 부족으로 좌초될 위험성이 논의됨."
            ],
            "data_points": [
                "MS 연간 CapEx 증가율 전망: 전년 대비 35% 증가한 550억 달러 추정",
                "골드만삭스의 AI 효용성 평가 보고서: 투자금 회수 실패 확률을 25% 상향 조정"
            ],
            "signal": "bearish",
            "signal_reason": "AI 투자 당위성에 대한 금융시장의 의심이 밸류에이션 하단 압박으로 작용하여, 전방 반도체 대형주 및 클라우드 진영 주가의 박스권 행보가 유도될 수 있습니다.",
            "key_companies": ["Nvidia", "Microsoft", "Alphabet"],
            "insight": "현재 시장은 단순 인프라 구축 확장이 아닌 '빅테크 기업의 실제 유료 AI 구독 모델의 전환율과 대기업 온프레미스 AI 라이선스 매출 성적표'라는 실리를 강하게 요구하고 있습니다. 인프라 피크아웃 리스크가 조기 등장할 가능성을 염두에 두어야 합니다.",
            "action_point": "빅테크 및 고성장 AI 주식의 추가 추격 매수를 제어하고, 대신 AI 투자 증가의 유틸리티 실효를 거둘 송배전/전력 수혜주로 일부 헷징을 취합니다."
        }
    },
    "LqqesACErC8": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["미래에셋자산배분", "현금유동성확보", "고배당커버드콜", "7월자산가이드"],
        "video": {
            "id": "LqqesACErC8",
            "title": "Stay Invested. Stay Liquid.#July2026ClientAssetAllocationGuide",
            "published": "2026-07-08T11:00:00+00:00",
            "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=LqqesACErC8",
            "thumbnail": "https://img.youtube.com/vi/LqqesACErC8/hqdefault.jpg"
        },
        "analysis": {
            "summary": "7월 미 대선 가시화 및 금리 경로 불확실성 국면에서 미래에셋 글로벌 자산배분 본부가 제안하는 자산 배분 핵심 원칙(Stay Invested. Stay Liquid)을 요약합니다. 주식 자산의 비중을 완전히 줄이기보다, 투자 상태를 유지(Stay Invested)하되 높은 금리를 주는 CD/파킹형 자산 및 고배당 커버드콜 상품을 결합하여 고도의 유동성(Stay Liquid)을 확보해 기회비용을 방어하는 다중 자산 구조 전략입니다.",
            "key_claims": [
                "변동성 장세에서 성급하게 현금으로 도피할 경우 주가 반등기의 복리 효과를 완전히 놓치는 포모(FOMO) 리스크를 겪게 됨.",
                "따라서 미국 단기 채권, CD 금리 연동 ETF, 그리고 미국 빅테크 기반의 10~15%대 고배당 커버드콜을 결합하는 포트폴리오를 주축으로 삼아야 함.",
                "대선 정책 수혜주(인프라, 에너지, 조선)의 로테이션 장세를 대비해 20% 수준의 상시 가용 투자 유동성을 쥐어야 함."
            ],
            "data_points": [
                "미래에셋 추천 안전/파킹 자산 권장 비중: 전체 포트폴리오의 30% 이상 유지",
                "미국 국채 2년물 금리 배분 매력도 밴드: 4.3% 초과 구간에서 매집 매력 상존"
            ],
            "signal": "neutral",
            "signal_reason": "전반적인 증시 낙관론은 우호적이나 변동성 지수(VIX)가 바닥을 딛고 상승 국면을 보여 단기적인 방어 포지션을 취할 타이밍이기 때문입니다.",
            "key_companies": ["미래에셋자산운용", "BlackRock"],
            "insight": "상승장 끝자락에서 레버리지 투자를 고집하기보다 배당 인컴 수익률을 확보하고 현금 비중을 유지하는 지루하지만 확실한 투자가 이기는 구간입니다. 자금 회전률을 높여 기회 수급을 노려야 합니다.",
            "action_point": "미국 테크 단일 투자를 일부 매도하여 주간 수급 유입이 안정적인 단기 CD 금리 ETF 및 고배당 월배당 상품 비중으로 이동 배치합니다."
        }
    },
    "O85NSkfOGNc": {
        "primary_topic": "robot",
        "secondary_topics": ["space", "stock"],
        "tags": ["현대차우주산업", "전기식아틀라스", "피지컬AI", "HMGICS"],
        "video": {
            "id": "O85NSkfOGNc",
            "title": "Is Hyundai Motor pursuing space exploration and lunar industry projects with Atlas?",
            "published": "2026-07-08T11:30:00+00:00",
            "channel_name": "엔지니어TV",
            "url": "https://www.youtube.com/watch?v=O85NSkfOGNc",
            "thumbnail": "https://img.youtube.com/vi/O85NSkfOGNc/hqdefault.jpg"
        },
        "analysis": {
            "summary": "현대자동차그룹이 보스턴 다이내믹스의 전기식 아틀라스(Atlas) 플랫폼을 단순 완성차 조립 라인을 넘어, 극한 환경인 우주 항공 개척 및 달 표면 탐사(Lunar Exploration)의 실전 물리 제어 탐사 로봇으로 투입하는 대형 장기 프로젝트의 실효성과 시너지를 분석합니다. 현대차의 자율주행 모빌리티 제어 알고리즘과 아틀라스의 3D 자유도가 우주 산업과 융합하는 획기적 로드맵입니다.",
            "key_claims": [
                "달 표면의 극단적 저중력, 고방사선 환경에서 다축 구동 능력을 가진 인간형 로봇 아틀라스가 기존 바퀴형 로버보다 정밀 임무 수행에 우월함.",
                "현대차의 싱가포르 스마트 팩토리(HMGICS)에서 축적된 AI 공정 데이터와 로봇 제어 소프트웨어가 우주 탐사용 물리 제어 기술의 토대가 됨.",
                "미국 항공우주국(NASA)의 민간 아르테미스 프로젝트 참여 파트너사들과의 연대 가능성이 강력히 대두됨."
            ],
            "data_points": [
                "전기식 아틀라스 가동 시간 및 관절 가동 범위: 기존 유압식 대비 부품 90% 이상 단순화 및 360도 전방위 회전 관절 장착",
                "현대차그룹의 달 탐사 협동 로봇 공동 연구 참여 협약처: 한국지질자원연구원 등 6개 안보/우주 국가 연구원 참여"
            ],
            "signal": "bullish",
            "signal_reason": "현대차의 단순 자동차 제조 해자에서 벗어난 고부가가치 우주/로보틱스 테크 플랫폼 기업으로의 장기 리레이팅이 본격화되는 신호탄이기 때문입니다.",
            "key_companies": ["현대자동차", "Boston Dynamics"],
            "insight": "아틀라스 로봇이 단순 물류 상자 이동을 넘어 달 탐사 등 안보/우주 영역의 자주적 기기로 활약한다는 것은 피지컬 AI의 쓰임새가 극대화되는 전폭적인 혁신입니다. 보스턴 다이내믹스의 글로벌 특허권과 제조 공학의 시너지가 현대차의 장기 밸류에이션을 받쳐줄 것입니다.",
            "action_point": "단기 실적 조정기에 현대차 지분을 중장기 가치 방어 자산으로 꾸준히 적립하고, 다축 감속기 및 3D 정밀 센서 소부장 주식의 수혜를 선점합니다."
        }
    },
    "puCJxoyXDvE": {
        "primary_topic": "etc",
        "secondary_topics": ["economy"],
        "tags": ["축구협회행정", "홍명보감독", "체육회이슈", "기타시사"],
        "video": {
            "id": "puCJxoyXDvE",
            "title": "Stagnant Soccer Association: At this rate, they'll just pick Hong Myung-bo again",
            "published": "2026-07-08T12:00:00+00:00",
            "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=puCJxoyXDvE",
            "thumbnail": "https://img.youtube.com/vi/puCJxoyXDvE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "한국 축구협회(KFA)의 국가대표 감독 선임 과정에서 드러난 무능한 행정 시스템과 불투명한 인재 영입 의사결정의 문제점을 사회 공학 및 지배구조 측면에서 날카롭게 비판합니다. 합리적 절차와 데이터 분석 기반의 선발이 아닌, 학연/인맥 위주의 소모적인 결정이 반복되는 원인을 파헤칩니다.",
            "key_claims": [
                "해외 명장급 감독 검증 데이터를 방치한 채 행정 비용 지불을 꺼려 국내 중심의 폐쇄적 인선 구도로 귀결됨.",
                "대한체육회 및 국가 안보 지원 체육 보조금이 협회의 불투명한 회계 및 독점적 행정에 장벽으로 기능함.",
                "대중의 비판 여론에도 불구하고 협회 수뇌부의 지배구조 개편이 전혀 작동하지 않는 조직적 고착화가 지속됨."
            ],
            "data_points": [
                "협회 연간 예산 중 보조금 비중: 약 300억 원대 수준 규모 조달",
                "차기 국가대표 감독 선임 대기 소요 기간: 5개월 이상 장기 행정 공백"
            ],
            "signal": "na",
            "signal_reason": "스포츠 협회 지배구조 분석 및 시사 비판 뉴스이므로, 경제/금융 투자 시장에 미치는 유의미한 영향은 없습니다.",
            "key_companies": ["대한축구협회"],
            "insight": "이 비판은 공공 보조금을 투입받는 준공공 협회들의 전형적인 지배구조 리스크(Agency Problem)를 전형적으로 보여줍니다. 투명한 감시 장치가 없는 독점 단체는 결국 비효율의 극치로 수렴한다는 공공 선택 이론의 실제 사례입니다.",
            "action_point": "투자 대상과는 무관하므로 시사 상식 획득 차원에서 청취를 마치고 추가 대응은 생략합니다."
        }
    },
    "Si_iFd517WU": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["삼성전자실적가이드", "영업이익8.5조", "메모리반등", "외국인매도의견"],
        "video": {
            "id": "Si_iFd517WU",
            "title": "Wall Street Turns to \"Sell\"... But, Samsung Electronics Projected to Reach a Staggering \"850 Tril...",
            "published": "2026-07-08T12:30:00+00:00",
            "channel_name": "월텍남",
            "url": "https://www.youtube.com/watch?v=Si_iFd517WU",
            "thumbnail": "https://img.youtube.com/vi/Si_iFd517WU/hqdefault.jpg"
        },
        "analysis": {
            "summary": "일부 외국인 투자은행(IB)들의 삼성전자 3분기 매도 의견 리포트 출회로 촉발된 우려와 달리, 메리츠 등 국내 전문 하우스의 정밀 예측 결과 삼성전자의 영업이익이 일회성 임직원 특별 상여 상각 비용 환입 회계 반영 등으로 인해 **8.5조~9조 원대 초서프라이즈**를 낼 것이라는 팩트를 대비합니다. 월가의 부정 리포트는 단기 파생상품 매도 숏 포지션 방어를 위한 일시적 여론 조성일 가능성을 경고합니다.",
            "key_claims": [
                "외국인 IB들의 삼성전자 D-RAM 가격 피크아웃 리포트는 HBM3E 및 HBM4의 퀄 테스트 진입 일정을 인위적으로 폄하한 경향이 짙음.",
                "삼성은 일회성 특별 격려금 회계 환입액이 약 1.5조 원 이상 3분기 실적에 대대적으로 복원되어 일시적 이익 폭발을 보여줄 예정임.",
                "글로벌 빅테크의 AI 서버용 메모리 수급은 공급 부족이 장기 고정가 계약(3Q +18% 이상 인상)으로 가시화되는 중임."
            ],
            "data_points": [
                "메리츠증권 분석 3분기 삼성전자 최종 영업이익 가이드라인: 8.5조 ~ 9조 원대 서프라이즈 범위",
                "장기 고정가 계약 인상 요구율: D-RAM 및 NAND 플래시 전월 대비 15%~18% 인상"
            ],
            "signal": "bullish",
            "signal_reason": "외국인 리포트발 단기 노이즈에 따른 급락세는 팩트인 회계 환입 및 D-RAM 장기 공급자 우위 단가 확인 후 강한 턴어라운드를 보장하기 때문입니다.",
            "key_companies": ["삼성전자", "SK하이닉스", "Morgan Stanley"],
            "insight": "외국계 IB들의 숏 플레이와 실질 고정 단가 인상 수치 간의 간극은 역사적으로 반도체 사이클 후반부마다 반복되던 전형적인 개미 털기 구간입니다. 장기 고정 가격 상승 연속성이 훼손되지 않았다는 것이 본질적 팩트입니다.",
            "action_point": "모건스탠리 등 숏 리포트로 유발된 삼성전자 단기 하락 기조를 절호의 추가 수량 적립(매집) 기회로 포착하여 비중을 확대합니다."
        }
    },
    "VqQgxp4JgZY": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["코스피폭락", "연기금리밸런싱", "레버리지반대매매", "수급분석"],
        "video": {
            "id": "VqQgxp4JgZY",
            "title": "[Breaking News] The chaotic KOSPI plunge: How to make sense of it all",
            "published": "2026-07-08T13:00:00+00:00",
            "channel_name": "이효석아카데미",
            "url": "https://www.youtube.com/watch?v=VqQgxp4JgZY",
            "thumbnail": "https://img.youtube.com/vi/VqQgxp4JgZY/hqdefault.jpg"
        },
        "analysis": {
            "summary": "최근 코스피 지수가 장중 7% 이상 폭락하며 프로그램 매도 사이드카가 발동했던 'KOSPI 블랙 웬즈데이'의 원인을 파악합니다. 매크로 펀더멘털의 파멸이 아닌, 국내 연기금의 자산군 비중 조절(리밸런싱 한도 초과에 따른 주식 매도)과 개인 신용 물량의 도미노식 반대매매(Liquidations)가 얽힌 한국형 수급 왜곡 사태입니다.",
            "key_claims": [
                "코스피 폭락은 펀더멘털 리스크가 아니며, 7월 상반기 연기금의 국내 주식 법정 보유 한도 준수 의무에 따른 강제 대량 매도 폭탄이 근본 원인임.",
                "증권사 신용 융자 잔고가 20조 원을 돌파한 상태에서 지수 2% 하락 시 기계적으로 발생하는 반대매매가 투매를 가속함.",
                "외국인의 현선물 매도는 이러한 국내 수급 왜곡을 틈탄 단기 차익 실현 및 아비트라지(재정거래) 포지션 세팅의 도구로 쓰임."
            ],
            "data_points": [
                "일일 강제 청산 반대매매 대기 대금: 약 1조 2,000억 원대 규모 관찰",
                "국민연금의 국내 주식 비중 초과 한도: 법정 14.5% 기준선을 넘어 약 1%p(약 10조 원) 강제 매도 압력 존재"
            ],
            "signal": "neutral",
            "signal_reason": "기계적이고 제도적인 수급 꼬임에 의한 하락은 펀더멘털의 문제가 아니므로 주가 복구력이 강하게 작용하나, 반대매매 소화에 최소 3~5영업일의 매물 소화가 필요하기 때문입니다.",
            "key_companies": ["국민연금", "키움증권"],
            "insight": "안타깝게도 한국 증시는 국민연금의 강제 리밸런싱 족쇄와 고레버리지 신용 반대매매라는 구조적 패시브 수급 함정을 안고 있습니다. 지수가 공포에 젖을 때 펀더멘털이 확실한 반도체 실적주를 줍는 용기가 절대적으로 가치를 냅니다.",
            "action_point": "신용 반대매매 물량이 전량 출회되고 지수 변동성이 안정되는 시점(보통 수요일 폭락 후 금요일 마감 전)을 조준해 우량 소부장 주식을 저가 매집합니다."
        }
    },
    "z6HQrJZUqOk": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["고배당주추천", "커버드콜ETF", "월인컴300만원", "자산포트폴리오"],
        "video": {
            "id": "z6HQrJZUqOk",
            "title": "How to Earn $3,000 in Monthly Dividends with $100,000 (High-Dividend Stocks, Financial Stocks, Co...",
            "published": "2026-07-08T13:30:00+00:00",
            "channel_name": "수페TV",
            "url": "https://www.youtube.com/watch?v=z6HQrJZUqOk",
            "thumbnail": "https://img.youtube.com/vi/z6HQrJZUqOk/hqdefault.jpg"
        },
        "analysis": {
            "summary": "10만 달러(약 1.3억 원)의 가용 자산으로 매월 3,000달러(약 400만 원, 연 배당률 36% 수준)의 안정적인 현금 흐름을 설계하는 포트폴리오 기법을 분석합니다. 초고배당 커버드콜 상품의 함정(원금 갉아먹기, 제자리걸음 등)을 방지하기 위해 금융 우선주, 빅테크 성장 배당주, 고정 금리 우선 채권을 3:3:4 비율로 배분하는 리스크 분산형 웰스 케어 전략입니다.",
            "key_claims": [
                "연 30%를 초과하는 고배당 커버드콜 단일 종목 몰빵은 기초자산 하락 시 원금 갉아먹기(NAV Erosion) 장기 피해를 초래함.",
                "따라서 성장률을 방어하는 빅테크 커버드콜(예: `TSLY` 우회), 금리 안정기 수혜를 입는 금융 우선주, 단기 CD 고정 금리를 믹스해야 함.",
                "복리 효과 극대화를 위해 매월 받은 3,000달러 배당 인컴의 50%는 반드시 배당 성장형 지수 ETF(SCHD 등)로 재투자해야 수명이 유지됨."
            ],
            "data_points": [
                "초고배당 커버드콜의 NAV 갉아먹기 확률: 3년 보유 시 원금의 약 25% 하락 리스크 존재",
                "분산 배분 포트폴리오의 실질 기대 배당수익률: 연 12% ~ 15% 안정적 수렴대 지향"
            ],
            "signal": "neutral",
            "signal_reason": "안정적인 현금 흐름 확보법이나, 단기적인 지수 상승 랠리 국면에서는 성장주 직접 투자 대비 초과 수익률이 제한될 수 있기 때문입니다.",
            "key_companies": ["JPMorgan Chase", "Schwab"],
            "insight": "커버드콜은 변동성이 횡보하는 구간에서 가장 강력한 인컴 효율을 냅니다. 미 대선 가시화 및 금리 인하 대기 국면처럼 지수가 박스권 횡보를 보여줄 때 포트폴리오의 방어적 현금 흐름 쿠션 역할을 톡톡히 해낼 것입니다.",
            "action_point": "전체 주식 포트폴리오의 20% 이내에서 고배당 인컴 연동형 수급이 강한 커버드콜 및 고배당 채권 분산 비중을 점진 확보합니다."
        }
    },
    "ZCQF7om5Y_s": {
        "primary_topic": "etc",
        "secondary_topics": ["tech"],
        "tags": ["5G통신공학", "밀리미터파", "주파수도달거리", "통신인프라"],
        "video": {
            "id": "ZCQF7om5Y_s",
            "title": "5G가 빠른 이유",
            "published": "2026-07-08T14:00:00+00:00",
            "channel_name": "안될공학 - IT 테크 신기술",
            "url": "https://www.youtube.com/watch?v=ZCQF7om5Y_s",
            "thumbnail": "https://img.youtube.com/vi/ZCQF7om5Y_s/hqdefault.jpg"
        },
        "analysis": {
            "summary": "5G 무선 통신 기술이 4G LTE 대비 20배 이상 빠른 대역폭을 획득할 수 있는 고주파 대역(28GHz 등 밀리미터파)의 작동 원리와, 주파수가 높을수록 도달 거리가 짧아지고 장애물 회절이 불가능해지는 전자기학적 한계를 대중의 시선에서 쉽게 풀어 설명합니다.",
            "key_claims": [
                "고주파는 데이터 전송 용량이 큰 반면 회절이 약해 도심 내 수많은 중계기(Small Cell) 초밀집 설치가 필수적임.",
                "대용량 다중 입출력(Massive MIMO) 및 안테나 신호를 특정 기기로 모아주는 빔포밍(Beamforming) 기술이 5G의 지연 시간을 극단적으로 축소함.",
                "국내 통신사들의 28GHz 망 회수 사태에서 보듯 상업적 인프라 투자 대비 실 ROI 획득은 전 세계적 난제임."
            ],
            "data_points": [
                "4G vs 5G 이론적 최고 속도 차이: 4G 1Gbps vs 5G 20Gbps (약 20배)",
                "28GHz 주파수의 가시거리(LoS) 도달 한계 거리: 약 100m~200m 이내 (장애물 회절 없음)"
            ],
            "signal": "na",
            "signal_reason": "통신 주파수 및 물리 공학 원리를 다룬 기초 교양 교육 영상이며, 통신사 및 소부장 기업 실적에 유의미한 영향은 유발하지 않기 때문입니다.",
            "key_companies": ["SK텔레콤", "삼성전자"],
            "insight": "5G의 한계 규명은 향후 자율주행차량 및 스마트 팩토리, 원격 로보틱스 구동을 위해 왜 위성 통신(스타링크 등)과 6G 로드맵에서의 초밀집 서브 식스(Sub-6) 보완 안테나 장비 수주가 계속 팽창할 수밖에 없는지 역설적으로 증명합니다.",
            "action_point": "통신 관련 투자는 단기 지수 배당주 성격으로 접근하고, 우주 위성 통신이나 초소형 중계기 부품사 밸류체인의 장기 성장 기조를 주시하는 것으로 갈음합니다."
        }
    }
}

# Ensure analyzed subdirectories exist and write JSON files
for vid, data in batch_data.items():
    topic = data["primary_topic"]
    dest_path = analyzed_dir / topic / f"{vid}.json"
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Structure data to match schema exactly
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

print("\nSuccessfully generated 15 analyzed JSON files.")
