import json
from pathlib import Path

analyses = [
    {
        "video": {
            "id": "Q_VGQa7wK3M",
            "title": "테슬라가 진짜 노리는 건 당신 집이다 #일론머스크 #휴머노이드",
            "published": "2026-08-19T14:15:35+00:00",
            "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=Q_VGQa7wK3M",
            "thumbnail": "https://img.youtube.com/vi/Q_VGQa7wK3M/hqdefault.jpg"
        },
        "analysis": {
            "summary": "테슬라 옵티머스가 로봇 손에 22자유도를 초과하는 고난도 힘줄(Tendon) 구동 방식을 고집하는 이유는 단순 공장 조립용 로봇을 넘어 <span class=\"text-cyan-300 font-semibold\">무한대의 잠재력을 지닌 '가정용(B2C) 휴머노이드'</span> 시장을 타깃으로 하기 때문입니다.\n가정 내 비정형 환경과 복잡한 인간 도구를 다루기 위해서는 인간의 손과 동일한 정밀 조작 능력이 필수적입니다.\n제조 현장을 거쳐 궁극적으로 수억 가구에 보급될 B2C 휴머노이드 시장 선점이 테슬라 피지컬 AI 비전의 핵심입니다.",
            "key_claims": [
                "테슬라 옵티머스 손 설계(22자유도)의 진정한 목적은 제조 공장이 아닌 가정용 도우미 로봇 시장임.",
                "가정용 휴머노이드 시장은 산업용 로봇 시장보다 수십 배 거대한 궁극의 피지컬 AI 시장임."
            ],
            "data_points": [
                "옵티머스 손 메커니즘: 22자유도 이상 구현 및 힘줄(Tendon) 기반 정밀 구동 채택"
            ],
            "signal": "bullish",
            "signal_reason": "테슬라 휴머노이드의 상용화 로드맵이 산업용에서 조 단위 가정용 서비스 로봇 생태계로 확장되는 장기 비전을 구체화했기 때문임.",
            "key_companies": [
                "테슬라(TSLA)",
                "유니트리",
                "보스턴다이내믹스"
            ],
            "insight": "자율주행차가 도로 위의 피지컬 AI라면, <span class=\"text-cyan-300 font-semibold\">휴머노이드 핸드</span>는 가사 노동과 일상 서비스를 대체할 궁극의 소비자용 AI 하드웨어 플랫폼입니다.",
            "action_point": "옵티머스 밸류체인에 포함되는 초소형 모터, 감속기, 촉각 센서 및 테슬라 본주에 대한 중장기 적립식 투자를 유지할 것."
        },
        "classification": {
            "primary_topic": "robot",
            "secondary_topics": ["tech", "stock"],
            "tags": ["테슬라옵티머스", "22자유도", "가정용휴머노이드", "일론머스크", "피지컬AI"]
        }
    },
    {
        "video": {
            "id": "Tln76jprMiE",
            "title": "'안전하다'던 지갑 이제 믿을 수 없다…시드 문구까지 노리는 해킹 | 서동주, 김동환, 함지현 블록미디어 기자 [크립토 PLUS]",
            "published": "2026-08-19T02:49:02+00:00",
            "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=Tln76jprMiE",
            "thumbnail": "https://img.youtube.com/vi/Tln76jprMiE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미 상원의 가상자산 규제 명문화 법안인 '클라리티(Clarity) 법' 토론 종결(클로처) 표결이 9월 15일로 확정되고 SEC가 소규모 프로젝트 등록 면제 규정(Reg Crypto)을 제안하며 규제 불확실성 해소 기대감이 커졌습니다.\n국내에서는 방통위의 폴리마켓 접속 차단 조치와 2027년 가상자산 과세 시행을 앞두고 취득가 산정 난항 및 과세 유예 청원 논란이 거세지고 있습니다.\n시드 문구를 탈취하는 고도화된 지갑 해킹 위협이 급증함에 따라 콜드월렛 보관 및 보안 수칙 준수가 요구됩니다.",
            "key_claims": [
                "미 상원 클라리티 법안의 9월 15일 클로처 표결 확정 및 SEC의 등록 면제 완화로 가상자산 제도권 편입 가속화.",
                "국내 가상자산 과세(22% 분리과세) 시행 시 디파이/해외 거래 취득가 입증 부재에 따른 억울한 세금 폭탄 우려.",
                "예측 시장(폴리마켓) 차단 등 국내 규제 당국의 보수적 기조가 크립토 유동성 위축 요인으로 작용 중임."
            ],
            "data_points": [
                "미 상원 클라리티 법안 표결: 2026년 9월 15일 클로처(토론 종결) 표결 진행 (60표 필요)",
                "SEC 레그 크립토 제정안: 4년간 500만 달러, 연간 7,500만 달러 규모 ICO 증권 등록 면제 허용",
                "국내 가상자산 과세: 250만 원 초과 소득에 대해 22% 분리과세 추진 (유예 청원 심사 중)"
            ],
            "signal": "neutral",
            "signal_reason": "미국 규제 명문화 진전 호재와 국내 과세/접속 차단에 따른 단기 거래량 급감 악재가 교차하고 있기 때문임.",
            "key_companies": [
                "비트코인(BTC)",
                "이더리움(ETH)",
                "코인베이스(COIN)",
                "폴리마켓"
            ],
            "insight": "가상자산 시장이 무법지대에서 <span class=\"text-emerald-400 font-medium\">제도권 금융 규율(SEC 면제 규정 및 클라리티 법)</span>로 편입되는 과도기에 있으며, 세무 리스크와 지갑 보안 관리가 투자자의 핵심 역량이 되었습니다.",
            "action_point": "미국 클라리티 법안 통과 여부를 모니터링하며 비트코인 및 대형 코인 중심의 분할 매수를 유지하고 개인 지갑의 시드 문구 보안을 강화할 것."
        },
        "classification": {
            "primary_topic": "crypto",
            "secondary_topics": ["stock", "etc"],
            "tags": ["클라리티법안", "SEC레그크립토", "가상자산과세", "폴리마켓차단", "지갑해킹주의", "함지현기자"]
        }
    },
    {
        "video": {
            "id": "tyq4GT_2rGg",
            "title": "[26.08.19 오전 방송 전체보기] '장기채 금리 부담돼' 뉴욕증시 동반 하락...미국 반도체 지수 -4.9%",
            "published": "2026-08-19T03:10:47+00:00",
            "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=tyq4GT_2rGg",
            "thumbnail": "https://img.youtube.com/vi/tyq4GT_2rGg/hqdefault.jpg"
        },
        "analysis": {
            "summary": "글로벌 채권 시장의 장기 차입 비용이 수십 년 만에 최고치(미 30년물 5.3% 돌파)로 치솟으며 필라델피아 반도체 지수가 <span class=\"text-rose-400 font-medium\">-4.9% 급락</span>하고 마이크론(-7%), 샌디스크(-9%) 등 메모리 섹터가 큰 폭의 조정을 받았습니다.\n반면 막대한 현금 창출력을 보유한 애플과 경기 방어 성격의 헬스케어, 에너지 섹터는 상대적 강세를 보이며 지수 하방을 지지했습니다.\n사상 최고치 랠리 이후 단기 차익 실현과 금리 충격이 겹친 구간이므로 감정적 투매를 지양하고 철저한 글로벌 분산 포트폴리오를 유지해야 합니다.",
            "key_claims": [
                "글로벌 장기 국채 수익률 급등은 고금리 차입에 의존하는 AI CapEx와 테크주 밸류에이션에 직접적인 하방 압력으로 작용함.",
                "나스닥은 반도체 급락에도 불구하고 헬스케어/빅테크 분산 효과로 -1%대 선방하며 포트폴리오 배분의 위력을 증명함.",
                "금리 변동성 국면에서는 현금 창출 능력이 뛰어난 우량주와 비기술주 섹터의 방어력이 두드러짐."
            ],
            "data_points": [
                "필라델피아 반도체 지수(SOX): -4.9% 급락 (마이크론 -7%, 샌디스크 -9%, AMD -4%, 엔비디아 -2%)",
                "미국 30년 만기 국채 수익률: 5.32% (2007년 이후 19년 만에 최고치 기록 후 등락)",
                "워런 버핏의 버크셔 해서웨이 2분기 포트폴리오: 알파벳(구글) 지분 83% 대폭 확대(360억 달러 보유)"
            ],
            "signal": "neutral",
            "signal_reason": "장기 금리 급등에 따른 반도체 차익 실현 매물이 출회되었으나, 기업 실적과 이익 마진이 훼손되지 않은 단기 변동성 구간이기 때문임.",
            "key_companies": [
                "마이크론(MU)",
                "샌디스크(SNDK)",
                "엔비디아(NVDA)",
                "애플(AAPL)",
                "알파벳(GOOGL)",
                "버크셔해서웨이(BRK)"
            ],
            "insight": "반도체 단일 섹터 몰빵은 금리 쇼크 시 계좌 치명상을 부를 수 있으며, <span class=\"text-emerald-400 font-medium\">현금 창출 빅테크+헬스케어+배당주</span>를 조합한 글로벌 분산 구조가 하락장 방어의 핵심입니다.",
            "action_point": "반도체 급락 시 공포에 동요하지 말고, 버핏의 알파벳 매수 사례처럼 펀더멘털이 확실한 현금 부자 빅테크와 메모리 대표주를 저가 분할 매수할 것."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock", "tech"],
            "tags": ["장기국채금리급등", "필라델피아반도체급락", "마이크론조정", "버크셔알파벳매수", "글로벌자산배분", "삼프로TV"]
        }
    },
    {
        "video": {
            "id": "wEigQQsC_ok",
            "title": "2천만원 VS 1억원, 시간이 만든 격차",
            "published": "2026-08-19T01:00:29+00:00",
            "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=wEigQQsC_ok",
            "thumbnail": "https://img.youtube.com/vi/wEigQQsC_ok/hqdefault.jpg"
        },
        "analysis": {
            "summary": "중개형 ISA 계좌는 가입 첫해부터 매년 2,000만 원씩 납입 한도가 자동 누적되어 5년 차에는 <span class=\"text-emerald-400 font-medium\">최대 1억 원까지 비과세 납입 한도</span>가 쌓입니다.\n가입을 늦게 시작하면 과거 연도의 누적 한도를 활용할 수 없으므로, 지금 당장 불입하지 않더라도 계좌를 개설해 두는 것만으로 큰 세제 혜택을 선점할 수 있습니다.\n시간이 만들어내는 납입 한도와 비과세 복리 효과의 구조적 격차를 활용하는 똑똑한 자산 관리 팁을 제시합니다.",
            "key_claims": [
                "ISA는 가입 즉시 납입 한도가 매년 2,000만 원씩 이월 누적되므로 조기 개설이 절대적으로 유리함.",
                "실제 투자 금액이 적더라도 계좌를 미리 만들어 두어야 최대 1억 원 한도를 빠르게 확보 가능함."
            ],
            "data_points": [
                "ISA 연간 납입 한도: 매년 2,000만 원 누적 (최대 5년간 1억 원)"
            ],
            "signal": "na",
            "signal_reason": "절세 계좌 개설 및 한도 누적 원리 소개 영상으로 투자 시그널에 해당하지 않음.",
            "key_companies": ["미래에셋증권"],
            "insight": "재테크에서 시간은 단순한 기다림이 아니라 <span class=\"text-emerald-400 font-medium\">제도적 절세 한도를 확보하는 가장 값진 자산</span>입니다.",
            "action_point": "아직 ISA 계좌가 없는 경우 즉시 개설하여 연 2,000만 원의 납입 한도 누적 타이머를 시작할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["etc"],
            "tags": ["중개형ISA", "납입한도누적", "최대1억원", "비과세복리", "미래에셋"]
        }
    },
    {
        "video": {
            "id": "WzEcPznO5f4",
            "title": "노후 준비 몇 살부터? | 공강 | #Shorts",
            "published": "2026-08-19T08:30:37+00:00",
            "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=WzEcPznO5f4",
            "thumbnail": "https://img.youtube.com/vi/WzEcPznO5f4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "100세 시대와 고물가 환경 속에서 청년층의 노후 준비 시작 적정 연령에 대한 솔직한 인터뷰와 자산 형성 조언을 전달합니다.\n노후 준비는 은퇴 직전인 40~50대가 아니라 소액(월 5만~10만 원)이라도 <span class=\"text-emerald-400 font-medium\">취업 직후인 20대부터 시작</span>해야 복리 시간의 마법을 온전히 누릴 수 있습니다.\n일찍 시작할수록 부가 지출 부담 없이 여유로운 노후 자산 형성이 가능합니다.",
            "key_claims": [
                "노후 준비는 취업 직후인 20대 중후반부터 소액 적립식으로 시작하는 것이 가장 현실적이고 강력함.",
                "고물가 시대일수록 시간의 복리 효과를 극대화하는 조기 연금 투자가 필수적임."
            ],
            "data_points": [
                "추천 시작 시기: 취업 직후 20대 중후반, 월 5만~10만 원 소액 불입부터 시작"
            ],
            "signal": "na",
            "signal_reason": "노후 연금 준비 및 청년 재테크 마인드셋 인터뷰 영상으로 시그널 대상이 아님.",
            "key_companies": ["미래에셋증권"],
            "insight": "노후 자산의 크기는 불입 금액의 크기보다 <span class=\"text-emerald-400 font-medium\">불입 기간의 길이</span>에 비례합니다.",
            "action_point": "연금저축 및 IRP 계좌에 매월 자동이체를 설정하여 장기 복리 투자 파이프라인을 구축할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["etc"],
            "tags": ["노후준비", "20대재테크", "복리효과", "연금저축", "미래에셋"]
        }
    },
    {
        "video": {
            "id": "xR5BqDcw5D0",
            "title": "[문지웅의 빅머니 LIVE] 미국정부 장기국채 바이백 2배로 사실상 '오퍼레이션 트위스트' | 하이닉스, 샌디스크 주주환원 비교",
            "published": "2026-08-19T22:03:39+00:00",
            "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=xR5BqDcw5D0",
            "thumbnail": "https://img.youtube.com/vi/xR5BqDcw5D0/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미국 재무부가 9월 9일부터 10~30년물 장기 국채 바이백 한도를 회당 20억 달러에서 40억 달러로 2배 전격 확대하며, 연준의 양적완화(QE) 대신 정부 재정(TGA 계정 9,328억 달러)을 활용한 <span class=\"text-rose-400 font-medium\">'소규모 오퍼레이션 트위스트(OT)'</span>를 단행했습니다.\nSK하이닉스는 잉여현금흐름(FCF) 50% 이상을 주주환원에 투입하기로 하고 40조 원 규모 자사주 매입 소각(발행주식 3.3% 소각, EPS 3.4% 상승 효과)을 발표하며 강력한 주가 방어막을 구축했습니다.\n모더나는 머크와 공동 개발한 mRNA 흑색종 백신 임상 3상 성공으로 4년 만에 흑자 성장 궤도에 재진입하며 주가가 폭등했습니다.",
            "key_claims": [
                "미 재무부의 바이백 2배 확대는 단기채 발행으로 조달한 TGA 재정을 통해 장기 국채를 매입 소각하는 실질적 일드커브 평탄화(OT) 조치임.",
                "SK하이닉스의 40조 원 자사주 매입소각은 샌디스크(초과현금 100%) 대비 실질 현금 환원 규모가 훨씬 거대하며 강력한 주주가치 제고 효과를 냄.",
                "모더나의 암 백신 3상 성공은 mRNA 기술이 감염병을 넘어 항암 종양학 플랫폼으로 진화했음을 입증함."
            ],
            "data_points": [
                "미 재무부 국채 바이백 한도: 기존 회당 20억 달러 -> 40억 달러로 2배 확대 (9월 9일~11월 4일)",
                "미국 재무부 일반계정(TGA) 잔고: 9,328억 달러로 바이백 여력 충분",
                "SK하이닉스 주주환원: 누적 FCF의 50% 이상 환원, 40조 원 투입 3.3% 자사주 매입 소각 (EPS +3.4% 개선)",
                "모더나(MRNA) 실적 추이: 2022년 193억 달러 -> 2025년 19억 달러 급감 후 2026년 암 백신으로 턴어라운드 개시"
            ],
            "signal": "bullish",
            "signal_reason": "미 재무부의 국채 금리 안정화 개입과 SK하이닉스의 초대형 주주환원, 모더나 바이오 신약 혁신이 맞물려 증시 하방 지지력이 대폭 강화되었기 때문임.",
            "key_companies": [
                "SK하이닉스(000660)",
                "모더나(MRNA)",
                "샌디스크(SNDK)",
                "엔비디아(NVDA)",
                "테슬라(TSLA)"
            ],
            "insight": "장기 금리 급등 리스크를 미국 정부가 <span class=\"text-rose-400 font-medium\">재정 기반 바이백</span>으로 차단하는 가운데, 메모리 반도체 1위 기업의 <span class=\"text-emerald-400 font-medium\">초대형 자사주 소각</span>은 주가의 하방 안전마진을 완벽히 보장합니다.",
            "action_point": "SK하이닉스의 주주환원 수혜와 매크로 금리 진정에 따른 메모리 반도체 및 모더나 발 바이오 혁신주에 대한 비중을 확대할 것."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock", "tech"],
            "tags": ["국채바이백2배", "오퍼레이션트위스트", "TGA계정", "SK하이닉스주주환원", "자사주40조매입소각", "모더나암백신", "문지웅"]
        }
    },
    {
        "video": {
            "id": "yxSBpqS1pSI",
            "title": "미국 재무부, 장기 국채 매입 2배로 확대...모더나-머크, 암 백신 임상 결과에 폭등 [월가 뉴스레터]",
            "published": "2026-08-19T22:18:32+00:00",
            "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=yxSBpqS1pSI",
            "thumbnail": "https://img.youtube.com/vi/yxSBpqS1pSI/hqdefault.jpg"
        },
        "analysis": {
            "summary": "베선트 미 재무장관의 국채 바이백 2배 전격 확대로 미국 10년물 국채 금리가 4.64%로 급락하며 채권발 공포가 진정되었습니다.\n모더나-머크의 흑색종 암 백신 3상 성공으로 모더나 주가가 180%대 폭등을 기록했고, 유니트리 상장 대흥행에 힘입어 테슬라 옵티머스 휴머노이드 가치가 재평가되며 4.2% 상승했습니다.\n구글의 마벨(MRVL) 커스텀 TPU 협력 체결로 마벨이 10% 급등한 반면 브로드컴이 하락하는 등 AI 하드웨어 내 차별화 장세가 뚜렷해졌습니다.",
            "key_claims": [
                "미 재무부의 장기 국채 매입 확대는 금리 불안을 잠재우며 증시 전반에 즉각적인 안도 랠리를 촉발함.",
                "바이오(모더나), 로봇(테슬라/유니트리), ASIC 반도체(마벨) 등 실질적 기술 혁신 테마로 자금 순환매가 전개됨.",
                "금리 하락으로 그동안 억눌려 있던 크립토(비트코인), 금, 바이오, 건설 섹터가 동반 반등세를 시현함."
            ],
            "data_points": [
                "미국 10년물 국채 금리: 4.64%로 급락 (장대 음봉 출현)",
                "모더나(MRNA) 주가: 장중 180% 이상 폭등 기록",
                "테슬라(TSLA): 유니트리 로봇 IPO 흥행 연동으로 +4.23% 상승",
                "마벨 테크놀로지(MRVL): 구글 TPU 협력 발표로 +10% 급등 vs 브로드컴(AVGO) -4.6% 하락"
            ],
            "signal": "bullish",
            "signal_reason": "매크로 금리 상방 압력 해소와 모더나 암백신/테슬라 로봇/마벨 ASIC 등 다변화된 기술 호재가 시장의 투자 심리를 급속히 회복시키고 있기 때문임.",
            "key_companies": [
                "모더나(MRNA)",
                "테슬라(TSLA)",
                "마벨테크놀로지(MRVL)",
                "구글(GOOGL)",
                "브로드컴(AVGO)",
                "엔비디아(NVDA)"
            ],
            "insight": "빅테크 단일 독주에서 벗어나 <span class=\"text-rose-400 font-medium\">바이오 신약</span>, <span class=\"text-cyan-300 font-semibold\">피지컬 AI(휴머노이드)</span>, <span class=\"text-emerald-400 font-medium\">맞춤형 ASIC 반도체</span>로 시장의 상승 동력이 다각화되고 있습니다.",
            "action_point": "금리 안정화의 직접 수혜를 받는 테슬라(로봇), 모더나(바이오), 마벨(ASIC) 등 다변화된 혁신 성장주를 균형 있게 포트폴리오에 편입할 것."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock", "tech", "robot"],
            "tags": ["국채매입2배확대", "모더나폭등", "테슬라로봇재평가", "마벨구글TPU", "베선트재무부", "박명석큐레이터"]
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
print("Batch 4 completed!")
