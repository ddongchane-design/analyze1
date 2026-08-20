import json
from pathlib import Path

analyses = [
    {
        "video": {
            "id": "e76johEpuZw",
            "title": "변동성 시장에서 살아남는 방법",
            "published": "2026-08-19T01:08:02+00:00",
            "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=e76johEpuZw",
            "thumbnail": "https://img.youtube.com/vi/e76johEpuZw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "급격한 시장 변동성과 대외 경제 리스크에 대비하기 위해서는 단일 고위험 자산에 편중된 투자를 지양하고 <span class=\"text-emerald-400 font-medium\">자산 배분(Asset Allocation)</span> 원칙을 철저히 준수해야 합니다.\n중개형 ISA 계좌를 활용하면 주식뿐만 아니라 채권, ETF, 펀드 등 다양한 자산군을 하나의 계좌에 유연하게 담아 포트폴리오를 분산할 수 있습니다.\n비과세 및 분리과세 절세 혜택을 극대화하면서 하락장에서도 계좌 변동성을 낮추는 안정적 자산 배분 전략을 권장합니다.",
            "key_claims": [
                "시장 변동성 장세에서는 단일 자산 올인보다 여러 자산군을 조합한 포트폴리오 구성이 필수적임.",
                "중개형 ISA는 주식, 채권, ETF를 자유롭게 리밸런싱할 수 있어 변동성 관리에 최적화된 절세 계좌임."
            ],
            "data_points": [
                "중개형 ISA 특징: 주식, ETF, 채권 등 다양한 상품 통합 운용 및 비과세 혜택 제공"
            ],
            "signal": "na",
            "signal_reason": "자산 배분 및 절세 계좌(ISA) 운용 가이드 영상으로 개별 종목 매매 시그널에 해당하지 않음.",
            "key_companies": ["미래에셋증권"],
            "insight": "시장의 단기 방향성을 맞추려 하기보다 어떤 시장 충격에도 견딜 수 있는 '자산 배분 벙커'를 마련하는 것이 장기 복리 수익률의 핵심입니다.",
            "action_point": "중개형 ISA 계좌를 통해 변동성이 큰 기술주와 안정적인 배당주/단기채권 ETF를 적절한 비율로 분산 편입할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["etc"],
            "tags": ["중개형ISA", "자산배분", "변동성관리", "절세계좌", "미래에셋"]
        }
    },
    {
        "video": {
            "id": "G0pXO-S0Es4",
            "title": "\"중국AI 쓰겠습니다\" 중국에 애걸복걸한 애플... 절망적인 위기상황",
            "published": "2026-08-19T09:00:02+00:00",
            "channel_name": "Softdragon SOD",
            "url": "https://www.youtube.com/watch?v=G0pXO-S0Es4",
            "thumbnail": "https://img.youtube.com/vi/G0pXO-S0Es4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "애플이 중국 시장 점유율 방어를 위해 애플 인텔리전스에 자체 모델 대신 <span class=\"text-cyan-300 font-semibold\">알리바바의 Qwen(통이첸원)</span>을 탑재하고 중국 당국의 엄격한 데이터 검열 레이어를 수용했습니다.\n고비용 D램 의존을 낮추기 위해 200억 파라미터 경량 모델을 낸드(NAND)에 저장하고 일부만 D램에 올리는 온디바이스 최적화를 시도했으나, 여전히 통합 메모리 12GB 요구 사양으로 인해 구형 모델 지원 한계에 직면했습니다.\n미국 정부의 대중국 반도체/AI 규제가 강화되는 가운데 애플의 친중국 기술 제휴는 미 정치권의 강력한 감시와 규제 리스크에 노출되어 있습니다.",
            "key_claims": [
                "애플은 글로벌 시장에서 구글 제미나이를 쓰는 것과 달리 중국에서는 알리바바 Qwen 기반으로 AI 서비스를 구축함.",
                "D램 가격 부담을 줄이기 위해 낸드 플래시 기반 온디바이스 활성화 기술을 개발했으나 12GB 메모리 하한선으로 삼전/하이닉스 메모리 의존성은 여전히 지속됨.",
                "트럼프 행정부 및 미 의회의 알리바바/바이두 적성기업 지정 검토 등 애플의 대중 AI 협력에 대한 지정학적 규제 리스크가 고조됨."
            ],
            "data_points": [
                "D램 vs 낸드 단위 가격 차이: D램이 낸드 플래시 대비 약 80배 고가",
                "애플 인텔리전스 최소 요구 메모리 사양: 12GB 이상 통합 메모리 탑재 모델 한정 (아이폰 17 기본형 8GB 미지원)",
                "미국 정부 방침: 2026년 8월 15일 중국산 메모리 사용 불가 명령 및 알리바바 제휴 감시"
            ],
            "signal": "bearish",
            "signal_reason": "애플의 독자 AI 경쟁력 부재와 중국 내 서비스 종속성 심화, 그리고 미-중 갈등에 따른 정치적 규제 리스크가 밸류에이션 하방 요인으로 작용하기 때문임.",
            "key_companies": [
                "애플(AAPL)",
                "알리바바(BABA)",
                "삼성전자(005930)",
                "SK하이닉스(000660)",
                "마이크론(MU)"
            ],
            "insight": "소비자 AI 기기의 승패는 독자 모델의 성능뿐만 아니라 <span class=\"text-cyan-300 font-semibold\">메모리 대역폭/원가 구조</span>와 글로벌 지정학적 규제 통과 능력에 좌우되고 있으며, 메모리 반도체 기업들의 공급 우위가 굳건합니다.",
            "action_point": "애플의 AI 업그레이드 사이클 지연 리스크를 감안해 세트 업체보다 고용량 LPDDR5X 및 HBM을 공급하는 메모리 반도체 공급사 비중을 우선 유지해야 합니다."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock", "economy"],
            "tags": ["애플인텔리전스", "알리바바Qwen", "온디바이스AI", "D램의존도", "삼성전자", "SK하이닉스"]
        }
    },
    {
        "video": {
            "id": "gEWbNlpKDHY",
            "title": "미국 헤지펀드들이 '전력 병목' 1위 기업으로 꼽는 이유..",
            "published": "2026-08-19T07:31:27+00:00",
            "channel_name": "월텍남",
            "url": "https://www.youtube.com/watch?v=gEWbNlpKDHY",
            "thumbnail": "https://img.youtube.com/vi/gEWbNlpKDHY/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미국 데이터센터의 일반 전력망 연결 대기 기간이 55개월(약 4.5년)에 달하는 극심한 전력 병목 속에서, 고체산화물 연료전지(SOFC)로 <span class=\"text-emerald-400 font-medium\">단 55일 만에 온사이트 전력을 공급</span>하는 블룸 에너지(Bloom Energy)가 핵심 수혜주로 부상했습니다.\n블룸 에너지는 2026년 2분기 매출이 전년 대비 160% 급증(약 10억 달러)하고 영업이익률이 3배 상승하는 등 강력한 운영 레버리지를 증명했습니다.\n오라클 및 브룩필드와의 3GW급 초대형 계약을 필두로 미국 주요 하이퍼스케일러와 AI 연구소 등 12곳 이상이 솔루션을 채택하며 최대 50GW 파이프라인 확장이 기대됩니다.",
            "key_claims": [
                "AI 데이터센터 가동의 최대 병목은 변압기와 전력망 인입 지연이며, 현장 즉시 발전(온사이트 SOFC)이 유일한 단기 대안임.",
                "기존 가스터빈 3사(GE, 지멘스, 미쓰비시)는 2029년까지 주문이 마감되어 블룸 에너지의 모듈형 연료전지로 수요가 집중됨.",
                "대기오염 물질 배출이 적어 데이터센터 건설 인허가 모라토리엄 규제를 우회할 수 있는 친환경 장점 보유."
            ],
            "data_points": [
                "데이터센터 전력망 연결 소요 기간: 일반 그리드 55개월 vs 블룸 에너지 연료전지 55일",
                "2026년 2분기 실적: 매출 약 10억 달러 돌파 (전년 대비 +160%, 전분기 대비 +41.9%), 영업이익률 3배 급증",
                "오라클-브룩필드 협력: 3GW급 초대형 전력 공급 계약 체결, 잠재 확장 규모 최대 50GW"
            ],
            "signal": "bullish",
            "signal_reason": "하이퍼스케일러 전력 병목 해결의 독보적 선도 기업으로서 매출 급증과 영업 레버리지 개선이 동시에 실현되는 초고성장 구간이기 때문임.",
            "key_companies": [
                "블룸에너지(BE)",
                "오라클(ORCL)",
                "브룩필드(BN)",
                "GE버노바(GEV)",
                "두산퓨얼셀(336260)"
            ],
            "insight": "AI 인프라의 가치는 '얼마나 빨리 전력을 공급받아 GPU를 가동할 수 있는가'라는 시간 프리미엄에 직결되며, <span class=\"text-cyan-300 font-semibold\">온사이트 독립 전력 솔루션</span> 기업이 전력 인프라의 최대 승자가 되고 있습니다.",
            "action_point": "단기 급등에 따른 변동성 조정 시 블룸 에너지를 비롯한 현장 발전(SOFC) 및 데이터센터 특화 전력 인프라 밸류체인을 적극 비중 확대할 것."
        },
        "classification": {
            "primary_topic": "energy",
            "secondary_topics": ["tech", "stock"],
            "tags": ["블룸에너지", "SOFC연료전지", "데이터센터전력", "오라클", "전력병목", "온사이트발전"]
        }
    },
    {
        "video": {
            "id": "hkFObxd1RJw",
            "title": "현금 부자 빅테크의 몰락? 이제 빚 없이 못 사는 이유 #교양이를부탁해 #미국채금리 #삼성전자 #SK하이닉스 #AI사이클 #데이터센터 #목대균",
            "published": "2026-08-19T12:00:11+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=hkFObxd1RJw",
            "thumbnail": "https://img.youtube.com/vi/hkFObxd1RJw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "알파벳 등 글로벌 빅테크들이 견조한 매출 성장에도 불구하고 천문학적인 AI 설비투자(CapEx) 집행으로 인해 <span class=\"text-rose-400 font-medium\">잉여현금흐름(FCF)이 마이너스</span>로 돌아서며 대규모 부채 조달에 의존하기 시작했습니다.\n미국 GDP 대비 데이터센터 투자 비중 자체는 약 2% 이내로 역사적 인프라 붐 대비 과도하지 않으나, 투자 증가 속도가 지나치게 가파른 점이 자금 조달 리스크를 촉발하고 있습니다.\n고금리 장기화 환경에서 채권 발행 및 이자 비용 증가는 향후 빅테크의 수익성 검증과 밸류에이션 유지에 중대한 시험대가 될 것입니다.",
            "key_claims": [
                "자체 현금 창출액을 뛰어넘는 과도한 AI CapEx로 인해 무차입 경영을 자랑하던 빅테크들의 외부 차입 의존도가 급증함.",
                "AI 투자의 절대 규모보다 투자 속도가 너무 빨라 수익화(ROI) 증명 전까지 금융 비용 부담이 가중됨."
            ],
            "data_points": [
                "빅테크 CapEx 규모: 미국 GDP 대비 약 2% 수준이나 단기 증가율 폭증",
                "알파벳(구글): 분기 잉여현금흐름(FCF) 적자 전환 및 채권 발행 확대"
            ],
            "signal": "neutral",
            "signal_reason": "AI 인프라 성장의 필연적 투자 과정이나 단기적으로 FCF 적자 및 자금 조달 비용 상승에 따른 밸류에이션 압박이 공존하기 때문임.",
            "key_companies": [
                "알파벳(GOOGL)",
                "메타(META)",
                "마이크로소프트(MSFT)",
                "아마존(AMZN)"
            ],
            "insight": "현금 부자였던 빅테크들조차 차입금에 의존하는 국면에 진입함에 따라, 향후 시장 평가는 단순 CapEx 가이던스가 아닌 <span class=\"text-emerald-400 font-medium\">실질 AI 수익화(Monetization) 속도</span>에 의해 냉정히 갈릴 것입니다.",
            "action_point": "빅테크 실적 발표 시 잉여현금흐름(FCF) 턴어라운드 여부와 클라우드 AI 매출 성장률을 면밀히 대조하여 선별 투자해야 합니다."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["economy", "stock"],
            "tags": ["잉여현금흐름적자", "빅테크CapEx", "AI수익성", "목대균", "알파벳"]
        }
    },
    {
        "video": {
            "id": "HxwIonJ2nyw",
            "title": "[박신영의 개장전요것만-8월19일] 모더나, 피부암 재발 정복?..주가 177% 폭등 | \"금리 낮춰라\" 美의 바이백 작전",
            "published": "2026-08-19T13:59:48+00:00",
            "channel_name": "한경 글로벌마켓",
            "url": "https://www.youtube.com/watch?v=HxwIonJ2nyw",
            "thumbnail": "https://img.youtube.com/vi/HxwIonJ2nyw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "모더나와 머크가 공동 개발한 개인 맞춤형 암 백신(mRNA-4157 + 키트루다)이 악성 흑색종 후기 임상 3상에서 재발 및 전이 위험을 대폭 낮추며 <span class=\"text-rose-400 font-medium\">주가가 장전 최대 177% 폭등</span>했습니다.\n미국 재무부는 장기 국채 금리 급등을 진정시키기 위해 만기 10~30년물 바이백(국채 환매) 한도를 기존 20억 달러에서 40억 달러 이상으로 2배 전격 확대하며 국채 금리 급락을 유도했습니다.\n마벨(MRVL)은 구글과 맞춤형 TPU 가속기 상업 계약 및 120억 달러 규모 신주인수권 발행 소식에 급등했으며, BofA는 AI 채권 공급 과잉에 대응한 금 매수와 AI 채권 숏 전략을 제시했습니다.",
            "key_claims": [
                "모더나의 맞춤형 mRNA 암 백신 임상 성공은 2027년 상용화 가능성을 열며 암 치료 패러다임을 바꿈.",
                "미 재무부의 장기채 바이백 2배 확대는 채권 시장 유동성 위기를 선제 방어하려는 강력한 정책 개입임.",
                "AI 데이터센터 급증으로 구리 수요 폭증 및 공급 부족(칠레/페루 정체, 콩고 수출 금지)으로 톤당 15,000달러 돌파 전망."
            ],
            "data_points": [
                "모더나(MRNA) 주가: 장전 90%~177% 폭등, 머크(MRK) +7% 상승",
                "미 재무부 장기국채 바이백 규모: 기존 20억 달러에서 40억 달러 이상으로 2배 확대 (10~30년물 집중)",
                "마벨 테크놀로지(MRVL): 구글에 주당 206.58달러로 최대 5,900만 주(120억 달러 규모) 매수권 발행",
                "국제 금값: 트로이온스당 4,517달러 사상 최고치 돌파 (+2.2%)",
                "UBS 구리 가격 전망치: 톤당 14,000달러에서 15,000~15,500달러로 상향"
            ],
            "signal": "bullish",
            "signal_reason": "미 재무부의 전격적 국채 바이백으로 매크로 금리 상방 압력이 완화되고, 모더나 바이오 혁신 및 빅테크 AI ASIC(마벨) 협력 호재가 동시다발로 분출되었기 때문임.",
            "key_companies": [
                "모더나(MRNA)",
                "머크(MRK)",
                "마벨테크놀로지(MRVL)",
                "브로드컴(AVGO)",
                "구글(GOOGL)",
                "엔비디아(NVDA)"
            ],
            "insight": "매크로 정책(재무부 바이백)의 유동성 방어막 위에서 mRNA 기반 혁신 바이오테크와 맞춤형 AI ASIC 반도체로 시장의 주도 테마가 강력하게 확산되고 있습니다.",
            "action_point": "모더나 암백신 임상 성공으로 mRNA 바이오 섹터 및 구글 커스텀 AI 반도체 파트너(마벨)에 대한 단기 모멘텀 매매와 전력/구리 원자재 분산 편입을 병행할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy", "tech"],
            "tags": ["모더나암백신", "국채바이백2배", "마벨구글계약", "금값신고가", "구리가격전망", "박신영"]
        }
    },
    {
        "video": {
            "id": "juzmEaBrrM4",
            "title": "삼전닉스 급락, AI 거품일까... 그 진짜 이유는? #교양이를부탁해 #미국채금리 #삼성전자 #SK하이닉스 #AI사이클 #데이터센터 #목대균",
            "published": "2026-08-19T11:00:27+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=juzmEaBrrM4",
            "thumbnail": "https://img.youtube.com/vi/juzmEaBrrM4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "삼성전자와 SK하이닉스의 가파른 단기 주가 급락은 AI 사이클의 붕괴나 산업 거품이라기보다 <span class=\"text-rose-400 font-medium\">특정 섹터 쏠림과 레버리지 상품의 연쇄 청산</span>이 주된 원인입니다.\n주가가 10~15% 조정을 받자 신용 융자 및 레버리지 파생 상품의 손절매 매물이 쏟아지며 다른 투자자들의 공포 투매를 유발하는 악순환이 발생했습니다.\n수급발 단기 충격이 진정되면 메모리 반도체 펀더멘털에 기반한 기술적 반등 국면이 전개될 것입니다.",
            "key_claims": [
                "반도체 급락은 펀더멘털 악화보다 단기 과도했던 수급 쏠림과 레버리지 포지션 강제 정리에서 비롯됨.",
                "1차 하락 시 레버리지 상품의 기계적 손절매가 2차 투매를 유발하는 전형적인 수급 디레버리징 현상임."
            ],
            "data_points": [
                "국내 반도체 대장주 조정 폭: 단기 고점 대비 10~15% 이상 급락 후 반등 모색"
            ],
            "signal": "neutral",
            "signal_reason": "레버리지 수급 청산 과정의 변동성이 지속될 수 있으나 AI 메모리 펀더멘털이 훼손된 것이 아니므로 바닥 다지기 구간으로 판단되기 때문임.",
            "key_companies": [
                "삼성전자(005930)",
                "SK하이닉스(000660)"
            ],
            "insight": "수급 쏠림이 심했던 주도주의 단기 급락은 레버리지 청산의 자연스러운 시장 정화 과정이며, 공포의 피크에서 손절하기보다 분할 매수 타이밍을 노려야 합니다.",
            "action_point": "레버리지 청산 매물이 진정되는 시점을 확인하며 실적 기반의 삼성전자 및 SK하이닉스 핵심 비중을 유지할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech"],
            "tags": ["삼성전자급락", "SK하이닉스", "수급쏠림", "레버리지청산", "목대균"]
        }
    },
    {
        "video": {
            "id": "Jyumom1L6z4",
            "title": "300만 원 월급 투자 비중은? | 공강 | #Shorts",
            "published": "2026-08-19T08:30:11+00:00",
            "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=Jyumom1L6z4",
            "thumbnail": "https://img.youtube.com/vi/Jyumom1L6z4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "사회초년생의 월 300만 원 급여 기준 소비와 투자 비중에 대한 다양한 인터뷰와 현실적인 자산 형성 전략을 다룹니다.\n생활비를 제외하고 소득의 50~70%(월 150만~200만 원)를 선(先)투자 및 저축으로 배정하여 복리 효과를 극대화하는 시드머니 적립의 중요성을 강조합니다.\n청년기 초기 시드머니 구축이 장기 자산 증식의 성패를 가르는 가장 결정적인 출발점입니다.",
            "key_claims": [
                "월급 300만 원 기준 최소 50% 이상, 거주 비용 절감 시 최대 70%까지 투자/저축 비중을 확보하는 것이 권장됨.",
                "사회초년생 시기에는 지출 통제와 공격적인 시드머니 적립이 최우선 재테크 과제임."
            ],
            "data_points": [
                "월급 300만 원 배분 기준: 투자 200만 원 vs 생활비 100만 원 (2:1 비율)"
            ],
            "signal": "na",
            "signal_reason": "개인 재테크 기초 인터뷰 및 저축 비중 가이드 영상으로 주식 투자 시그널에 해당하지 않음.",
            "key_companies": ["미래에셋증권"],
            "insight": "투자 수익률 못지않게 중요한 것은 초기 저축률이며, 꾸준한 시드머니 불입이 중장기 복리 투자의 튼튼한 토대가 됩니다.",
            "action_point": "고정 지출을 최소화하고 급여의 50% 이상을 자동이체로 ISA 및 연금저축 계좌에 적립식 투자할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["etc"],
            "tags": ["월급투자비중", "사회초년생재테크", "시드머니", "적립식투자", "미래에셋"]
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
print("Batch 2 completed!")
