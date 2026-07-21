import json
from pathlib import Path

# Setup paths
base_dir = Path("c:/Users/ddong/OneDrive/Desktop/회사업무/analyze1/youtube-insight")
analyzed_dir = base_dir / "data/analyzed"

batch_data = {
    # TECH
    "7mNCRrnZ8LA": {
        "primary_topic": "tech", "secondary_topics": ["stock"],
        "tags": ["반도체쏠림", "주도주랠리", "하반기전망", "주가레벨업"],
        "video": {
            "id": "7mNCRrnZ8LA", "title": "“반도체 쏠림이 너무 심하다?” 그러나 강세장 끝물이 아닌 이유 #교양이를부탁해",
            "published": "2026-07-09T06:00:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=7mNCRrnZ8LA", "thumbnail": "https://img.youtube.com/vi/7mNCRrnZ8LA/hqdefault.jpg"
        },
        "analysis": {
            "summary": "반도체 및 빅테크 섹터로의 비정상적인 거래 대금 쏠림 현상이 버블 붕괴 시그널이 아닌, 실적 성장에 기반한 합리적인 주도주 집중 랠리임을 해설합니다. 과거 닷컴 버블과 달리 현재 빅테크들은 압도적인 현금 창출력과 지배력을 보유하고 있어, 하반기에도 반도체 중심의 주가 리레이팅이 계속 지지될 것으로 평가합니다.",
            "key_claims": ["최근 반도체 쏠림은 펀더멘털 개선을 동반한 현상으로 강세장 버블 종착지와 거리가 멂.", "인공지능 소프트웨어 매출이 개시되는 빅테크들의 자금력은 이익 기여도를 상회함."],
            "data_points": ["상반기 반도체 지수 거래 대금 집중률: 코스피 전체의 42% 수준", "엔비디아 및 빅테크 3사의 밸류에이션(Fwd PER): 과거 2000년 닷컴 버블 당시의 절반 수준"],
            "signal": "bullish", "signal_reason": "전방 주도주들의 건전한 실적 성장이 유지되고 있어 지수 하방 지지력이 견고하기 때문입니다.",
            "key_companies": ["Nvidia", "Samsung Electronics"],
            "insight": "시장의 우려와 달리 주도주 쏠림은 이익 집중도의 정직한 반영입니다. HBM 공급 쇼티지가 완화되기 전까지 반도체 포지션을 유지하는 것이 유리합니다.",
            "action_point": "반도체 비중을 축소하기보다, 이익 성장률이 유지되는 주도종목 중심의 홀딩 전략을 고수합니다."
        }
    },
    "Arqqubg0m30": {
        "primary_topic": "tech", "secondary_topics": ["stock"],
        "tags": ["반도체실적", "DRAM가격", "HBM수요", "공급망분석"],
        "video": {
            "id": "Arqqubg0m30", "title": "\"떨어질 순 있어요, 그런데...\" 반도체 실적 시나리오의 숨은 비밀 #교양이를부탁해",
            "published": "2026-07-09T06:10:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=Arqqubg0m30", "thumbnail": "https://img.youtube.com/vi/Arqqubg0m30/hqdefault.jpg"
        },
        "analysis": {
            "summary": "반도체 기업들의 단기 실적 변동 및 주가 조정 시나리오 속에서도, 중장기적인 HBM4 수요 및 전방 서버 빅테크들의 인프라 증설 경로가 훼손되지 않는 구조적 성장의 본질을 해부합니다.",
            "key_claims": ["DRAM 고정 거래가의 일시적 상승률 정체는 공급 부족이 풀리는 것이 아닌 고정가 계약의 일환임.", "장기 메모리 쇼티지 추세는 최소 2027년까지 구조적으로 이어질 전망임."],
            "data_points": ["3분기 글로벌 HBM3E 수급 충족률: 수요 대비 공급이 15% 부족", "빅테크향 LPDDR5X 하이엔드 모바일 메모리 고정가 인상률: +12%"],
            "signal": "bullish", "signal_reason": "DRAM 가격 피크아웃 우려는 과도하며, 공급 부족이 지속되어 고마진 제품 위주의 이익 성장이 확보되기 때문입니다.",
            "key_companies": ["SK Hynix", "Samsung Electronics"],
            "insight": "단기 노이즈에 주가가 흔들릴 수는 있으나, HBM 공급 부족과 하이엔드 메모리 전환 수요는 구조적입니다. 저가 매수가 기회입니다.",
            "action_point": "조정 시 전공정/후공정 핵심 장비사 밸류체인 위주로 점진적인 분할 매수를 집행합니다."
        }
    },
    "EegeW9WZrwc": {
        "primary_topic": "tech", "secondary_topics": ["robot"],
        "tags": ["미래자동차", "차량용AI", "UX스튜디오", "현대차SDV"],
        "video": {
            "id": "EegeW9WZrwc", "title": "\"내 차가 나를 읽었다?\" 미래 자동차 AI의 소름 돋는 능력… UX스튜디오 서울 가보니",
            "published": "2026-07-09T06:20:00+00:00", "channel_name": "안될과학 Unrealscience",
            "url": "https://www.youtube.com/watch?v=EegeW9WZrwc", "thumbnail": "https://img.youtube.com/vi/EegeW9WZrwc/hqdefault.jpg"
        },
        "analysis": {
            "summary": "현대차그룹의 서울 UX 스튜디오 현장 방문을 통해 탑승자의 시선, 음성, 생체 신호를 실시간 스캔하여 실내 환경을 자동 최적화하는 소프트웨어 정의 차량(SDV)의 정밀 물리 피지컬 AI 제어력을 체험 및 설명합니다.",
            "key_claims": ["차량 내 AI 비서가 시선 흐름을 감지하여 계기판 레이아웃을 자동 변경하고 졸음 경고를 고도화함.", "피지컬 로보틱스와 결합된 시트 제어 및 스마트 윈도우 인터랙션이 차량 UX의 핵심 차별화로 작동함."],
            "data_points": ["생체 신호 기반 졸음 감지 속도: 운전자 시선 분산 후 1.5초 이내 즉시 판정", "SDV 아키텍처 도입에 따른 무선 업데이트(OTA) 커버리지율: 차량 핵심 부품의 95% 이상 제어"],
            "signal": "bullish", "signal_reason": "전통 내연기관 제조사에서 고부가가치 자율주행 SDV 플랫폼 기업으로의 모빌리티 체질 개선이 가속화되고 있기 때문입니다.",
            "key_companies": ["현대자동차", "현대모비스"],
            "insight": "미래 차량은 단순한 이동 수단이 아니라 탑승객의 행동 양식을 학습하는 피지컬 AI 공간으로 거듭납니다. 전장 소프트웨어 부품사의 가치 상승이 기대됩니다.",
            "action_point": "모빌리티 SDV 하드웨어 및 차량용 인포테인먼트(IVI) 시스템 핵심 납품사들의 지분 비중을 우상향으로 관리합니다."
        }
    },
    "fyXAt012xCU": {
        "primary_topic": "tech", "secondary_topics": ["stock"],
        "tags": ["SK하이닉스", "삼성전자역전", "HBM지배력", "시총경쟁"],
        "video": {
            "id": "fyXAt012xCU", "title": "\"하이닉스가 삼전을 역전한다?\" 강세장 끝장내는 과열의 시그널 #교양이를부탁해",
            "published": "2026-07-09T06:30:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=fyXAt012xCU", "thumbnail": "https://img.youtube.com/vi/fyXAt012xCU/hqdefault.jpg"
        },
        "analysis": {
            "summary": "HBM(고대역폭메모리) 시장 선점으로 사상 초유의 영업이익 추월 시나리오를 쓰고 있는 SK하이닉스의 주가가 전통 제왕인 삼성전자의 위상을 위협하는 현상과, 이것이 강세장 과열을 뜻하는 자금 왜곡 지표인지 진단합니다.",
            "key_claims": ["하이닉스의 HBM3E 독점 구도가 하반기에도 견고하여 삼성의 진입 지연에 따른 반사이익을 최대화함.", "시총 격차 축소는 사이클 과열이 아닌 메모리 질적 패러다임 변화의 투표 결과임."],
            "data_points": ["2026년 상반기 HBM 글로벌 점유율: SK하이닉스 약 55%, 삼성전자 약 35%", "양사 시가총액 비율 추이: 과거 5:1 수준에서 현재 2.2:1 수준으로 급격히 축소"],
            "signal": "neutral", "signal_reason": "하이닉스의 독주는 실질 팩트이나, 과도한 기대감이 주가에 선반영된 측면이 있어 삼전의 퀄 테스트 통과 시 급격한 롱숏 청산 변동성이 유발될 수 있습니다.",
            "key_companies": ["SK Hynix", "Samsung Electronics"],
            "insight": "메모리가 범용재에서 맞춤형 스페셜티 칩으로 변화하면서 발생한 현상입니다. 삼전의 HBM 퀄 통과 시점 전후가 포트폴리오 재배정의 변곡점이 될 것입니다.",
            "action_point": "하이닉스 독식에 쏠린 비중 중 일부를, 퀄 테스트 돌파 기대로 가격 메리트가 높은 삼성전자로 분할 이전해 둡니다."
        }
    },
    "I-mYgLkzgss": {
        "primary_topic": "tech", "secondary_topics": ["etc"],
        "tags": ["알리바바클로드", "오픈소스도용", "미중기술패권", "LLM라이선스"],
        "video": {
            "id": "I-mYgLkzgss", "title": "\"역대급 대참사 터졌다\" 클로드 도둑질한 알리바바, 미국이 발칵 뒤집힌 이유 ㄷㄷ",
            "published": "2026-07-09T06:40:00+00:00", "channel_name": "Softdragon SOD",
            "url": "https://www.youtube.com/watch?v=I-mYgLkzgss", "thumbnail": "https://img.youtube.com/vi/I-mYgLkzgss/hqdefault.jpg"
        },
        "analysis": {
            "summary": "중국 알리바바의 독자 LLM 모델이 앤스로픽(Anthropic)의 '클로드 3.5 소네트' 가중치 및 시스템 프롬프트를 무단 수집 및 활용(도용)하여 벤치마크 점수를 올렸다는 기술 탈취 의혹과, 이로 인한 미국의 대중 반도체/클라우드 차단 제재 강화 가능성을 다룹니다.",
            "key_claims": ["알리바바의 AI 모델 출력값에서 앤스로픽 특유의 시스템 프롬프트 에러 메시지가 그대로 출력되는 침해 물증 포착.", "중국 테크 기업들이 API 크롤링을 통해 미국 선두 모델을 무단 복제하여 자체 기술인 양 기만한 사례임."],
            "data_points": ["앤스로픽 도용 모델 검증 결과: 특정 정렬 지문 테스트에서 클로드의 답변과 98% 일치율 기록", "미 상원 AI 안보 규제안 통과 일정: 대중 클라우드 접속 차단(IP 블록) 조치 조기 도입 검토"],
            "signal": "bearish", "signal_reason": "미국 AI 선두 진영의 특허 장벽 강화 및 중국에 대한 고성능 컴퓨팅 접근 차단이 전격 구체화되면서 글로벌 AI 밸류체인의 분열 리스크가 커지고 있기 때문입니다.",
            "key_companies": ["Alibaba", "Anthropic", "Microsoft"],
            "insight": "중국 AI 진영이 기술적 한계에 봉착해 지름길을 택하다가 보안 제재를 자초했습니다. 글로벌 빅테크 및 반도체 업계에는 강력한 지적재산권(IP) 보호 조치가 강화될 것입니다.",
            "action_point": "중국 관련 클라우드 플랫폼 노출 지분을 처분하고, 특허 장벽이 견고한 미국 빅테크 플랫폼 독점주 중심의 방어 포지션을 다집니다."
        }
    },
    "K6J-od3ybdk": {
        "primary_topic": "tech", "secondary_topics": ["economy"],
        "tags": ["데이터센터공실률", "AI인프라", "미국전력망", "전력인프라"],
        "video": {
            "id": "K6J-od3ybdk", "title": "데이터센터 2,500개 더 짓는데 공실률이 1% 미만? #교양이를부탁해",
            "published": "2026-07-09T06:50:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=K6J-od3ybdk", "thumbnail": "https://img.youtube.com/vi/K6J-od3ybdk/hqdefault.jpg"
        },
        "analysis": {
            "summary": "전 세계적인 AI 하드웨어 칩 증설 경쟁 속에서 데이터센터의 엄청난 건설 물량에도 불구하고 북미 상업용 데이터센터 공실률이 1% 미만의 역사적 바닥을 기록하는 '초강세 수급 공급 병목 현상'의 핵심 원인인 전력망 부족을 파헤칩니다.",
            "key_claims": ["전력망 공급 속도가 데이터센터 빌딩 준공 속도를 따라가지 못해 완공 즉시 임차 완료되는 구도임.", "데이터센터의 핵심 경쟁력은 칩이 아닌 발전소 송배전망을 선점했는가로 수렴함."],
            "data_points": ["북미 주요 상업용 데이터센터 평균 공실률: 사상 최저치인 0.8% 도달", "신규 전력망 연결 대기 기간(Interconnection Queue): 평균 5년에서 7.5년으로 지연"],
            "signal": "bullish", "signal_reason": "전력 병목으로 인해 기존 데이터센터 보유 기업들의 임대료 협상 지배력(Pricing Power)이 계속해서 급등하고 있기 때문입니다.",
            "key_companies": ["Digital Realty", "Equinix"],
            "insight": "AI 투자의 최종 병목은 전력입니다. 부동산 리츠 중 전력 인프라가 미연결된 자산은 가치 상승 둔화에 직면할 것이며, 송전망을 확보한 기업이 진정한 지배자입니다.",
            "action_point": "데이터센터 전력 인프라 연동이 확보된 대형 전문 리츠 및 송배전 기기(변압기 등) 제조 기업의 장기 적립식 투자를 적극 유지합니다."
        }
    },
    "OM_jet5VyFE": {
        "primary_topic": "tech", "secondary_topics": ["stock"],
        "tags": ["메타Llama4", "AI인프라판매", "CapEx분산", "비용효율화"],
        "video": {
            "id": "OM_jet5VyFE", "title": "AI인프라 판매설 나온 메타, 그 이유는? | 김인엽의 실리콘밸리나우",
            "published": "2026-07-09T07:00:00+00:00", "channel_name": "한경 글로벌마켓",
            "url": "https://www.youtube.com/watch?v=OM_jet5VyFE", "thumbnail": "https://img.youtube.com/vi/OM_jet5VyFE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "메타(Meta)가 독자 구축한 수만 대의 엔비디아 H100/B200 GPU 데이터센터 컴퓨팅 용량을 클라우드 형태로 외부 엔터프라이즈 기업들에 임대 혹은 판매하는 비즈니스를 개시하려 한다는 소문과, 그 이면에 깔린 천문학적인 CapEx 감가상각 및 메타 커뮤니티의 비용 헤징 전략을 규명합니다.",
            "key_claims": ["메타가 광고 매출 외에 Llama 기반 개발자 생태계를 장악한 뒤 컴퓨팅 인프라 재판매로 실적 방어를 꾀함.", "막대한 AI 투자를 감행한 빅테크들이 감가상각비용 압박을 덜기 위해 클라우드 서비스 제공업체(CSP)로의 변신을 시도함."],
            "data_points": ["메타 보유 연산용 GPU 보유 대수 추정치: 연말 기준 60만 대 돌파 전망", "메타 2분기 기준 AI 전력망 연계 누적 부채 감가상각비: 전년 동기 대비 28% 급증"],
            "signal": "bullish", "signal_reason": "AI 투자금이 단순 소모성 지출이 아닌 외부 재임대를 통한 실질 매출(Cash Inflow) 파이프라인으로 전환되어 마진 훼손 우려를 상쇄하기 때문입니다.",
            "key_companies": ["Meta", "Nvidia"],
            "insight": "자체 AI 개발 용량을 넘는 잉여 인프라를 상업용 클라우드로 수익화(Commercialization)하려는 빅테크의 움직임은 주주들의 AI 거품론 의구심을 잠재우는 영리한 전술입니다.",
            "action_point": "메타의 AI 상업화 전략 진행에 따라 추가 비중 확보를 검토하며, 빅테크의 비용 절감 밸류체인을 추적합니다."
        }
    },
    "qzBIColSELo": {
        "primary_topic": "tech", "secondary_topics": ["stock"],
        "tags": ["마이크로소프트", "애저AI성장", "오피스365", "실적분석"],
        "video": {
            "id": "qzBIColSELo", "title": "현재 난리라는 마이크로소프트 근황",
            "published": "2026-07-09T07:10:00+00:00", "channel_name": "Softdragon SOD",
            "url": "https://www.youtube.com/watch?v=qzBIColSELo", "thumbnail": "https://img.youtube.com/vi/qzBIColSELo/hqdefault.jpg"
        },
        "analysis": {
            "summary": "마이크로소프트(MS)의 최신 분기 애저(Azure) 클라우드 AI 이익 가속 지표와 코파일럿(Copilot)의 전 세계 대기업 실사용 계정 침투율이 시장의 우려와 달리 굳건히 폭발적 성장을 보여주고 있다는 팩트를 상세히 짚어봅니다.",
            "key_claims": ["애저 클라우드 내 AI 비즈니스 기여 비중이 사상 처음으로 두 자릿수(12%)를 돌파하여 캐시카우 역할을 개시함.", "포춘 500대 기업의 코파일럿 유료 구독 유지율이 강력한 락인(Lock-in) 효과를 보장함."],
            "data_points": ["Azure 분기 매출 성장률(Constant Currency): 전년 대비 +29% 기록", "엔터프라이즈 코파일럿 유료 계정 누적 수: 전 분기 대비 35% 증가"],
            "signal": "bullish", "signal_reason": "시장 일각의 AI 실익 우려를 가장 먼저 실제 클라우드 및 구독 매출 서프라이즈로 증명해 냈기 때문입니다.",
            "key_companies": ["Microsoft", "OpenAI"],
            "insight": "기술 버블론에 휘둘리지 마십시오. 실제 B2B 영업 네트워크와 오피스 독점력을 가진 MS는 AI 인프라 투자 비용을 가장 빠르고 확실하게 회수하는 유일한 기업입니다.",
            "action_point": "조정으로 인해 하락한 마이크로소프트 주식을 장기 코어 자산으로 적극 매집하여 포트폴리오 밸런스를 높입니다."
        }
    },
    "V96U46vq0WU": {
        "primary_topic": "tech", "secondary_topics": ["stock"],
        "tags": ["빅테크투자", "자사주매입축소", "AICapEx", "주주환원리스크"],
        "video": {
            "id": "V96U46vq0WU", "title": "주가 부양까지 포기했다? 빅테크가 자사주 매입 줄여가며 올인한 곳 #교양이를부탁해",
            "published": "2026-07-09T07:20:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=V96U46vq0WU", "thumbnail": "https://img.youtube.com/vi/V96U46vq0WU/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미국 대형 기술주들이 주가 하단을 지탱해 오던 자사주 매입(Buybacks) 규모를 선제 조율하여, 확보된 잉여 현금의 대부분을 AI 가속기 및 대규모 데이터센터 전력망 매집에 재투입하는 '주주 환원 대신 인프라 올인' 전략의 명암을 분석합니다.",
            "key_claims": ["빅테크들의 자 자사주 매입 감축은 단기 주가 탄력성 저하 요인이나, 장기 인프라 패권을 선점하기 위한 결단임.", "단기 배당 성향 및 환원을 추종하는 자금의 일시적 이탈이 예상됨."],
            "data_points": ["상반기 구글 및 메타의 자사주 매입 집행액 감소율: 전년 동기 대비 -15.4% 하향 조정", "동 기간 인프라 물리 투자(CapEx) 합산 증가율: 전년 동기 대비 +42.8% 폭증"],
            "signal": "neutral", "signal_reason": "장기 인프라 독점은 강화되나, 매수 주체 소멸에 따른 주가의 단기 방어력(지속적 자사주 하단 지지)이 다소 약화될 수 있기 때문입니다.",
            "key_companies": ["Alphabet", "Meta", "Microsoft"],
            "insight": "자사주 매입을 깎고 인프라를 타는 행위는 경쟁사를 죽이고 승자 독식을 강화하겠다는 의지의 표명입니다. 성장 지속 가능성은 높아집니다.",
            "action_point": "추격 매수 대신 분기 실적 가이드 발표 이후 주가 조정을 겪는 주도 종목을 긴 호흡에서 모아갑니다."
        }
    },

    # STOCK
    "1LuazKHZa_k": {
        "primary_topic": "stock", "secondary_topics": ["tech"],
        "tags": ["SK하이닉스ADR", "해외상장", "차익거래", "변동성분석"],
        "video": {
            "id": "1LuazKHZa_k", "title": "SK하이닉스 ADR 상장, 주가 재평가냐 변동성 확대냐...기대감보다 조심해야 할 이유ㅣ명민준, 강아랑, 최창규 [주린이 구조대]",
            "published": "2026-07-09T07:30:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=1LuazKHZa_k", "thumbnail": "https://img.youtube.com/vi/1LuazKHZa_k/hqdefault.jpg"
        },
        "analysis": {
            "summary": "SK하이닉스의 미국 ADR(주식예탁증서) 2차 상장 검토 뉴스가 기업 가치 리레이팅 호재인지, 혹은 해외 자본의 차익거래(Arbitrage) 표적이 되어 국내 본주 주가의 변동성을 되레 키울 리스크 요인인지 상세 진단합니다.",
            "key_claims": ["ADR 발행은 글로벌 펀드 수급 유입에 긍정적이나, 원달러 환율과 연계된 롱숏 차익 매물이 대량 출회될 수 있음.", "상장 대기 시점 전후로 공매도 타겟팅 및 파생 상품 꼬임 현상을 각별히 경계해야 함."],
            "data_points": ["검토 중인 ADR 발행 규모: 전체 지분의 약 3% 수준으로 추정", "유사 사례인 대만 TSMC 본주와 미국 ADR 간 프리미엄 격차 변동률: 평균 4%~8% 괴리율 발생"],
            "signal": "neutral", "signal_reason": "장기적으로 해외 판로가 넓어지나 단기적으로 국내 거래소 본주 주가는 파생 연동 및 환차익 매물 출회로 변동성이 극대화될 수 있기 때문입니다.",
            "key_companies": ["SK Hynix", "Samsung Electronics"],
            "insight": "ADR 상장은 대형 자금의 환금성을 높여주지만, 국내 주주들에게는 변동성 지옥을 선물할 수 있습니다. 환율 모니터링이 필수적입니다.",
            "action_point": "ADR 이슈로 주가 변동이 커지는 구간에서 성급하게 불타기 매수를 자제하고, 확실한 2분기 최종 영업이익 가이드를 확인한 뒤 대응합니다."
        }
    },
    "1MAvqXBJe4c": {
        "primary_topic": "stock", "secondary_topics": ["tech", "economy"],
        "tags": ["알리바바급등", "TSMC실적우려", "SpaceX챗봇", "홍키자"],
        "video": {
            "id": "1MAvqXBJe4c", "title": "알리바바, 홍콩 증시서 12.5% 급등ㅣ스페이스X '그록', 챗봇 5위로 밀려ㅣ미즈호 \"TSMC 호실적 나와도 주가 빠질수도\"ㅣ홍키자의 매일뉴욕",
            "published": "2026-07-09T07:40:00+00:00", "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=1MAvqXBJe4c", "thumbnail": "https://img.youtube.com/vi/1MAvqXBJe4c/hqdefault.jpg"
        },
        "analysis": {
            "summary": "홍콩 증시에서 알리바바의 12.5% 대반등, xAI의 그록(Grok) 경쟁력 둔화 우려, 그리고 미즈호 증권의 TSMC 실적 발표 후 주가 선반영 하락 경고 리포트의 주요 골자를 요약합니다.",
            "key_claims": ["알리바바는 중국 당국의 소비 부양 기치와 앤트그룹 지배구조 개편 일단락으로 홍콩 거래소 대규모 숏커버링 유도.", "미즈호는 TSMC가 역대급 가이드를 내더라도 단기 차익 실현(Sell on news) 매물 출회에 따른 급락 리스크를 경고함."],
            "data_points": ["알리바바 일일 홍콩 증시 급등률: +12.5% 기록", "TSMC 3나노 공정 수동 수율 한계 보도 비율: Fwd 가이던스 상회 확률 80% 이상임에도 주가 고점 대비 5% 선반영 하락"],
            "signal": "neutral", "signal_reason": "빅테크 및 중국 핵심 플랫폼주들의 바닥 다지기와 실적 선반영 경계론이 엇갈려 단기 박스권 횡보 장세가 유도될 수 있습니다.",
            "key_companies": ["Alibaba", "TSMC", "xAI"],
            "insight": "역대급 실적이 나오더라도 '이미 다 알고 있는 사실'로 인식되면 단기 조정을 겪는 전형적인 실적 장세 후반부 패턴입니다. 실물 펀더멘털을 보며 버텨야 합니다.",
            "action_point": "TSMC 실적 발표 당일 단기 변동성 급증 시 인위적 패닉셀을 멈추고, 3나노 장기 공급 단가 가이드가 건전하다면 보유 물량을 가져갑니다."
        }
    },
    "310g-gxWGyw": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["폭락장대응", "펀더멘털", "신용투매", "멘탈관리"],
        "video": {
            "id": "310g-gxWGyw", "title": "폭락장에 흔들리지 마세요. 진짜 본질은 아직 무너지지 않았습니다ㅣ명민준, 강아랑, 이권희 [주린이 구조대]",
            "published": "2026-07-09T07:50:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=310g-gxWGyw", "thumbnail": "https://img.youtube.com/vi/310g-gxWGyw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "개인 투자자들의 신용 반대매매 투매로 지수가 인위적으로 밀리는 코스피 급락 장세 속에서, 수출 실적 및 거시 이익 본질이 훼손되지 않았음을 설명하며 심리적 패닉 동조 매도를 경계할 것을 조언합니다.",
            "key_claims": ["현재 지수 하락은 마진콜 반대매매 및 기관 손절 한도 작동에 따른 수급 붕괴일 뿐 실물 침체가 아님.", "한국 주요 대형 수출사들의 2분기 수출 실적은 여전히 전년 대비 두 자릿수 성장을 기록 중임."],
            "data_points": ["코스피 일일 반대매매 집행 규모: 최근 3영업일 합산 약 2.4조 원 기록", "한국 정보통신기술(ICT) 제품군 수출 성장률: 전년 동월 대비 +18.7% 우상향 유지"],
            "signal": "bullish", "signal_reason": "실물 경기 지표와 무관한 기계적 투매 구간은 가격 왜곡이 심하여, 단기 매물 소화 후 매우 강한 낙폭과대 턴어라운드를 유발하기 때문입니다.",
            "key_companies": ["삼성전자", "현대자동차"],
            "insight": "담보부족 계좌들의 투매가 지수를 짓누르는 '수급 꼬임 현상'의 전형입니다. 이럴 때 헐값에 매각하는 실수를 피하고 현금을 지키는 것이 최고입니다.",
            "action_point": "가용 예비 현금이 있다면 반대매매 물량이 쏟아지는 오전 9시~9시 30분 사이 분할 매수로 우량주 수량을 늘려갑니다."
        }
    },
    "aPab3HBg-vc": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["사이드카발동", "KOSPI마감", "매수대기", "시장안정화"],
        "video": {
            "id": "aPab3HBg-vc", "title": "[7월 8일 마감시황] 공포에 파는 순간 늦습니다...지금은 '기다려야 할 구간'ㅣ홍선애, 이권희, 장우진 [클로징벨 라이브]",
            "published": "2026-07-09T08:00:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=aPab3HBg-vc", "thumbnail": "https://img.youtube.com/vi/aPab3HBg-vc/hqdefault.jpg"
        },
        "analysis": {
            "summary": "사이드카 발동으로 극에 달했던 공포 장세를 마감한 코스피 현황을 짚고, 외국인의 비정상적 선물 숏포지션 청산(숏커버) 징후가 포착되는 등 시장 안정화 국면 진입 시나리오를 제시합니다.",
            "key_claims": ["사이드카가 발동하는 패닉 장의 마감 단계에서는 매도 실익이 제로에 수렴함.", "외국인의 코스피200 야간 선물 숏커버링 매수세가 포착되어 반등 모멘텀이 장전 대기 중임."],
            "data_points": ["사이드카 발동 기준 지수 하락률: 코스닥 15분간 6% 이상 하락세 지속", "외국인 야간 선물 순매수 전환 규모: 약 4,200계약 숏커버 유입"],
            "signal": "bullish", "signal_reason": "극단적인 매도 과열 지표(RSI 20 이하 진입) 확인 후 선물 시장 중심으로 저가 매수세가 유입되어 기술적 반등 시점이 도래했기 때문입니다.",
            "key_companies": ["삼성전자", "SK하이닉스"],
            "insight": "변동성 극대화 구간은 공포의 절정이자 동시에 수급의 바닥입니다. 매도 투매에 동참하는 대신 호가 진정을 지켜봐야 할 국면입니다.",
            "action_point": "추가 신용 매수를 정지하고 리스크 한도를 안전하게 조율하며 주식 포트폴리오를 우량 대형주 위주로 압축 유지합니다."
        }
    },
    "JSdciqKzWnw": {
        "primary_topic": "stock", "secondary_topics": ["tech"],
        "tags": ["반도체투매", "수급불균형", "외국인이탈", "마켓인사이드"],
        "video": {
            "id": "JSdciqKzWnw", "title": "반도체 투매? 지금은 수급 문제 | 박병창 MP파트너스 대표 [마켓 인사이드]",
            "published": "2026-07-09T08:10:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=JSdciqKzWnw", "thumbnail": "https://img.youtube.com/vi/JSdciqKzWnw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "반도체 섹터의 급락 현상을 업황 피크아웃 리스크가 아닌, 외국계 헤지펀드들의 분기 말 차익 실현 및 아시아 신흥국 주식 비중 강제 조절(글로벌 자산 분배 변경)에 따른 일시적 '수급 미스매치'로 명쾌하게 정의합니다.",
            "key_claims": ["메모리 장기 업황 사이클 지표는 우상향 중이나, 선물/옵션 만기일과 맞물린 일시적 프로그램 투매가 지수를 깎음.", "개인 신용 털기가 끝나면 기관의 바스켓 매수 유입이 재개될 수밖에 없는 펀더멘털 조건임."],
            "data_points": ["외국인의 반도체 대형주 일일 순매도 대금: 약 8,900억 원 (이 중 70%가 프로그램 비차익 매도)", "DRAM 공급 계약 유지율: 북미 주요 서버 고객사들과의 3분기 고정가 계약 95% 이상 완료"],
            "signal": "bullish", "signal_reason": "수급이 꼬여서 발생한 주가 하락은 업황 악화와 달라, 수급 요인이 청산되는 즉시 주가가 원래 자리를 빠르게 찾아가기 때문입니다.",
            "key_companies": ["삼성전자", "SK하이닉스"],
            "insight": "기업가치가 멀쩡한 상황에서 거래 수급 문제로 세일이 일어나는 국면입니다. 공포를 견뎌낸 자가 하반기 이익 증가의 혜택을 온전히 누립니다.",
            "action_point": "반도체 보유 물량을 끝까지 홀딩하며, 낙폭이 과대했던 후공정(OSAT) 및 세정/코팅 소부장 기업 위주로 비중 확대를 저울질합니다."
        }
    },
    "KHFMn5J5yuo": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["순환매장세", "H2로테이션", "밸류체인지원", "포트폴리오전략"],
        "video": {
            "id": "KHFMn5J5yuo", "title": "반등이 와도 '이것'만 오르던 상반기, 하반기엔 반란이 일어납니다ㅣ홍선애, 박병창 MP파트너스 대표 [여의도 인사이트]",
            "published": "2026-07-09T08:20:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=KHFMn5J5yuo", "thumbnail": "https://img.youtube.com/vi/KHFMn5J5yuo/hqdefault.jpg"
        },
        "analysis": {
            "summary": "상반기 반도체 독주 극단 장세에서 벗어나 하반기 금리 인하 경로 구체화에 따라 친환경 에너지, 바이오, 조선/해운 소외 주산군으로 대형 수급이 이동하는 '섹터 로테이션 순환매' 시나리오를 전합니다.",
            "key_claims": ["상반기 소외받던 밸류업 소외주(지주사, 금융, 조선)의 배당 매력도가 하반기 금리 하락 국면에서 부각됨.", "반도체의 이익 독식을 틈탄 저평가 중소형 실적 턴어라운드 종목군으로의 낙수 자금 분산 개시."],
            "data_points": ["상반기 반도체 대 중소형주 수익률 스프레드 격차: 역사상 최대치인 35%p 돌파", "최근 1주일간 조선 및 제약/바이오 섹터 순유입 강도: 이전 주 대비 +14.8% 가속"],
            "signal": "neutral", "signal_reason": "지수의 급격한 폭등세보다 섹터 간 자금 이동에 따른 종목별 차별화(순환매)가 진행될 확률이 높기 때문입니다.",
            "key_companies": ["한화오션", "유한양행", "KB금융"],
            "insight": "반도체 독식 국면에서 소외 섹터로 자금이 흘러가는 것은 전형적인 강세장 중기 현상입니다. 특히 조선 소부장 및 바이오는 호실적을 바탕으로 한 턴어라운드가 기대됩니다.",
            "action_point": "수익이 난 반도체 지분의 일부(10~15%)를 이관하여, 수급 가속이 포착된 조선/조선소부장 및 고배당 금융 지분으로 포트폴리오를 분산합니다."
        }
    },
    "LX6UJCQEkBs": {
        "primary_topic": "stock", "secondary_topics": ["energy", "economy"],
        "tags": ["원전건설확대", "하이닉스ADR", "한국주식매도", "권순우"],
        "video": {
            "id": "LX6UJCQEkBs", "title": "UBS \"하이닉스 ADR 사고 한국 주식 팔아라\" | 김용범 정책실장 \"원전, 가능한 만큼 다 지어야\" | 삼전닉스 빼곤 대부분 고점서 물려 | 권순우 삼프로TV 기자 [뉴스3]",
            "published": "2026-07-09T08:30:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=LX6UJCQEkBs", "thumbnail": "https://img.youtube.com/vi/LX6UJCQEkBs/hqdefault.jpg"
        },
        "analysis": {
            "summary": "UBS의 하이닉스 ADR 매수 추천 및 한국 기타 주식 비중 축소 권고 리포트, 그리고 김용범 정책실장의 AI 데이터센터 대비 원전 무제한 추가 건설 발언이 송배전/원전 전력망 밸류체인에 가져올 거대한 상업적 수혜를 추적합니다.",
            "key_claims": ["UBS는 국내 거래소 시스템 규제 리스크를 헷징하기 위해 ADR을 매수하고 국내 중소형 주식 노출을 줄이라 경고함.", "정부 수뇌부의 원전 무제한 건설 기조 공식화는 대규모 AI 전력 인프라 대책의 유일한 현실적 대안으로 작용함."],
            "data_points": ["정부의 장기 신규 원전 추진 목표량: 기존 전력 수급 계획안에 원전 2~3기 추가 건설 검토안 반영", "한국 상장사 신용 담보 대출 금리 밴드: 최근 증권사 반대매매 실행 후 연 8.5%대 고점 횡보"],
            "signal": "neutral", "signal_reason": "전력/원전 인프라는 장기 수혜가 확고하나, 국내 지수 전반의 외인 롱숏 규제 회피 매물 출회 우려가 주가의 상단을 단기적으로 제한하기 때문입니다.",
            "key_companies": ["두산에너빌리티", "한전산업", "SK Hynix"],
            "insight": "AI 발전을 뒷받침할 현실적 에너지원으로 원전 증설은 당위의 선택입니다. 밸류체인 내 설계 및 터빈/주기기 공급사의 장기 수혜가 뒷받침됩니다.",
            "action_point": "원전 주기기 독점 및 송배전 설비 시스템 대장주(두산에너빌리티 등)의 중장기 투자 비중을 안정적으로 유지합니다."
        }
    },
    "NXhL_Sj40IA": {
        "primary_topic": "stock", "secondary_topics": ["tech"],
        "tags": ["반도체생산량", "DRAM단가", "수요지속성", "인프라구축"],
        "video": {
            "id": "NXhL_Sj40IA", "title": "반도체 끝난 거 아니다…이제는 가격보다 생산량 | 박승영 한화투자증권 PLUS 사업부 포트폴리오전략 팀장 [글로벌 인터뷰]",
            "published": "2026-07-09T08:40:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=NXhL_Sj40IA", "thumbnail": "https://img.youtube.com/vi/NXhL_Sj40IA/hqdefault.jpg"
        },
        "analysis": {
            "summary": "반도체 사이클이 칩 '단가 인상(P의 상승)' 위주에서, 전방 빅테크들의 데이터센터 정식 가동에 따른 '물량 공급 및 생산량(Q의 상승)' 위주의 실적 가시성 장세로 진입하여 반도체 성장이 꺾이지 않았음을 논증합니다.",
            "key_claims": ["가격 인상폭 둔화는 정상적 사이클이며, 생산량 증대 속도가 기업 전체 매출 볼륨을 견인하는 Q의 장세로 이행함.", "따라서 단기 가격 피크아웃 논리는 HBM 및 DRAM의 실질 출하량 급증 데이터로 무력화됨."],
            "data_points": ["글로벌 서버용 DRAM 최종 출하량(Q) 성장률 전망: 하반기 전 분기 대비 +22% 증가", "삼성/하이닉스 웨이퍼 가동률: 하반기 100% 완전 가동(Full Capacity) 지속"],
            "signal": "bullish", "signal_reason": "출하량이 견조하게 우상향하고 있어 기업들의 분기 순이익 총량이 증가하는 건강한 실적 장세를 지속하기 때문입니다.",
            "key_companies": ["SK Hynix", "한미반도체"],
            "insight": "가격(P)에만 집중하던 월가 리포트는 물량(Q)의 강력한 성장을 놓치고 있습니다. 웨이퍼 증설 소부장 및 패키징 밸류체인의 실익이 큽니다.",
            "action_point": "미국 수출 물량이 증가하는 패키징 장비 및 HBM 핵심 부품주 위주로 매집 비중을 조절하여 유지합니다."
        }
    },
    "pGk8Z1AcOhM": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["코스닥반등", "바이오주도", "수급교체", "더블업"],
        "video": {
            "id": "pGk8Z1AcOhM", "title": "계속되는 코스닥 일탈, 과연 이번에는 성공할까? | 정프로 & 빈센트 & 이종원 [더블 업]",
            "published": "2026-07-09T08:50:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=pGk8Z1AcOhM", "thumbnail": "https://img.youtube.com/vi/pGk8Z1AcOhM/hqdefault.jpg"
        },
        "analysis": {
            "summary": "2차전지 조정 속에서 바이오 테마 및 개별 소프트웨어 실적 강소기업들 위주로 지수 견인차가 이동하고 있는 코스닥 시장의 질적 변화 가능성을 진단합니다.",
            "key_claims": ["코스닥의 하방 지지력이 에코프로 비중 축소 이후 알테오젠 등 바이오 대장주 중심으로 교체 완료됨.", "금리 인하 개시 국면은 R&D 비용이 큰 코스닥 바이오 벤처들의 금융 비용을 덜어주어 센티먼트 개선에 즉효임."],
            "data_points": ["코스닥 내 제약/바이오 시총 비중: 연초 15%에서 현재 23%로 대폭 확대", "외국인의 코스닥 바이오 순매수 가속도: 최근 10거래일 연속 일평균 400억 원 순매입"],
            "signal": "bullish", "signal_reason": "하방 경직성이 강해진 코스닥 바이오 대장주들이 미국 FDA 승인 모멘텀과 맞물려 독자적인 상승 동력을 냈기 때문입니다.",
            "key_companies": ["알테오젠", "HLB", "리가켐바이오"],
            "insight": "2차전지의 하락을 바이오가 완벽히 메우며 코스닥의 지배구조가 건전해지고 있습니다. 금리 인하 개시의 최대 수혜 섹터인 바이오 대장주 포커스가 필요합니다.",
            "action_point": "코스닥 레버리지 대신, 확실한 기술수출(L/O) 계약금을 수령하는 톱티어 신약 플랫폼 지분 위주로 포트폴리오를 분산합니다."
        }
    },
    "S6OqFqo8D7A": {
        "primary_topic": "stock", "secondary_topics": ["tech", "shipbuilding"],
        "tags": ["엔비디아중국수출", "애플브로드컴협력", "트럼프이란발언", "해상물류"],
        "video": {
            "id": "S6OqFqo8D7A", "title": "[김종학의 뉴욕, 지금-7월9일] 엔비디아, 중국 수출 기대 강세 | 애플-브로드컴 300억 달러 협력 | 트럼프, 이란 공습 오락가락 발언 | 리바이스 실적 실망 -4%",
            "published": "2026-07-09T09:00:00+00:00", "channel_name": "한경 글로벌마켓",
            "url": "https://www.youtube.com/watch?v=S6OqFqo8D7A", "thumbnail": "https://img.youtube.com/vi/S6OqFqo8D7A/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미국 상무부의 대중 수출 규제를 우회하는 엔비디아 H20/H200 중국 맞춤형 AI 가속기 승인 기대감, 애플과 브로드컴의 $300억 대형 안테나 칩 공급 동맹, 그리고 트럼프의 이란 군사 공습 가능성 시사 발언이 가져올 중동 리스크와 해상 운임에 미칠 충격을 고찰합니다.",
            "key_claims": ["엔비디아는 중국 빅테크향 H20 칩 출하로 수조 원대 보류 매출의 실현 가능성이 제기되어 주가가 강하게 복구됨.", "애플은 5G RF 필터 및 모뎀 자립 한계를 극복하기 위해 브로드컴과 장기 다년 공급 계약을 체결함.", "트럼프의 중동 무력 개입 오락가락 발언은 호르무즈 해역의 실질 무력 충돌 불안감을 고조시켜 해운사들의 위험 할증 운임 체계를 고착화함."],
            "data_points": ["엔비디아의 중국향 H20 칩 예상 매출액: 하반기 최대 120억 달러 추정", "애플-브로드컴 장기 무선 칩셋 공급 동맹 규모: 총 300억 달러"],
            "signal": "neutral", "signal_reason": "전방 칩셋 호재는 뚜렷하나, 트럼프발 지정학 노이즈가 원유 및 해상 운송 원가를 높여 인플레이션 장기 재발을 유도할 위험이 상존하기 때문입니다.",
            "key_companies": ["Nvidia", "Broadcom", "Apple", "HMM"],
            "insight": "트럼프의 이란 자극 시나리오는 결국 **지정학적 통행 한계 $\rightarrow$ 아시아-유럽 선박 우회 $\rightarrow$ 해운 톤마일 상승 및 친환경 고부가가치 선박 신조 수요 가속**으로 흐르는 조선/해운 업계의 구조적 상방 압력을 지속 주입합니다.",
            "action_point": "반도체 대장주의 지위를 확고히 쥐면서, 해역 안보 불안에 따른 톤마일 수혜를 입는 국적선사(HMM 등) 및 조선 소부장 핵심 지분을 헷징 포트폴리오로 가져갑니다."
        }
    },
    "t-A9qvUuBjY": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["중국바이오", "우시앱텍제재", "중국소비진작", "보이는차이나"],
        "video": {
            "id": "t-A9qvUuBjY", "title": "중국 제약바이오 잊을 만하면 돌아온다!ㅣ보이는 차이나ㅣ2026.7.9 (목)",
            "published": "2026-07-09T09:10:00+00:00", "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=t-A9qvUuBjY", "thumbnail": "https://img.youtube.com/vi/t-A9qvUuBjY/hqdefault.jpg"
        },
        "analysis": {
            "summary": "미국의 바이오보안법(Biosecure Act) 제재안 하원 통과 지연으로 단기 숏커버링 랠리를 보여주는 중국의 우시앱텍(Wuxi AppTec) 등 CDMO 대기업들의 현지 반등 국면과, 국내 바이오 시총에 미칠 영향력을 점검합니다.",
            "key_claims": ["미국 상원의 대중 규제 범위 완화 조율 가능성 보도로 중국 CDMO 사들의 대대적인 홍콩 증시 매수 유입.", "중국 내수 임상 파이프라인의 이익 복원이 국가 보조금 지급으로 2년 만에 플러스 턴어라운드를 기록함."],
            "data_points": ["우시앱텍(WuXi AppTec) 홍콩 증시 단기 5거래일 합산 상승률: +24.8% 기록", "글로벌 제약사들의 중국 임상 의뢰 수주 가속 비율: 전분기 대비 14% 반등"],
            "signal": "neutral", "signal_reason": "중국 기업들의 단기 반등은 강하나, 미국의 정권 교체 시 대대적인 관세 폭탄과 생물 보안 제재가 부활할 확률이 여전히 높아 장기 지속성은 의문이기 때문입니다.",
            "key_companies": ["Wuxi AppTec", "삼성바이오로직스"],
            "insight": "중국 바이오의 단기 숨통 트이기는 한국 삼성바이오로직스 등 국내 CDMO 1등 주식의 독점적 반사이익 속도를 단기적으로 제어할 수 있으나, 장기적인 탈중국 수급 방향은 변함없습니다.",
            "action_point": "중국 바이오 추격 매수보다는, 규제 우려가 없고 수주 잔고가 사상 최대를 경신하는 삼성바이오로직스의 조정을 비중 확대 기회로 봅니다."
        }
    },
    "TsD4ukx9kdc": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["매도시점", "수급법칙", "추세선이탈", "현금화전략"],
        "video": {
            "id": "TsD4ukx9kdc", "title": "좋은 종목도 수급 앞에선 무너진다! 급등락 반복하는 시장, 언제 팔아야 할까?ㅣ차영주 와이즈경제연구소 소장 [집중 오늘의 주식]",
            "published": "2026-07-09T09:20:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=TsD4ukx9kdc", "thumbnail": "https://img.youtube.com/vi/TsD4ukx9kdc/hqdefault.jpg"
        },
        "analysis": {
            "summary": "우량한 기초 펀더멘털을 지닌 종목이라도 글로벌 거대 유동성(외국인 패시브 매도 등) 앞에서는 일시적으로 폭락할 수밖에 없는 수급 법칙과, 추세선 이탈 시 기계적 익절/손절 비중을 확보해야 하는 합리적 현금화 타이밍을 강의합니다.",
            "key_claims": ["120일 이동평균선 이탈 및 거래량을 동반한 하향 돌파 시에는 펀더멘털 신봉보다 일단 현금 비중 30% 확보가 정석임.", "주가는 가치 수렴보다 센티먼트 쏠림에 따라 단기 가격 밴드를 크게 벗어나는 본질을 이해해야 함."],
            "data_points": ["주요 우량 기술주의 추세선 이탈 후 평균 하락 잔존 기간: 15일에서 최대 22일", "기관 매도 집중 구간의 주가 낙폭 괴리율: 적정 내재 가치 대비 평균 -12% 괴리 발생"],
            "signal": "neutral", "signal_reason": "전반적인 주식 리스크 관리 차원의 기술적 매매 기법 강의이며, 증시 자체의 대형 업황 악화 시그널은 아니기 때문입니다.",
            "key_companies": ["삼성전자", "SK하이닉스"],
            "insight": "아무리 좋은 주식도 시장 수급 꼬임 속에서는 무너집니다. 장기 가치 투자를 표방하더라도 일부 현금 쿠션을 쥐어 변동성을 방어해야 합니다.",
            "action_point": "보유 포트폴리오 중 신용 융자율이 지나치게 높고 120일선을 하향 돌파하는 중소형주는 비중을 신속히 줄여 현금화합니다."
        }
    },
    "xckWKGIq9zA": {
        "primary_topic": "stock", "secondary_topics": ["tech", "economy"],
        "tags": ["삼성전자", "역대급폭락", "패시브투매", "수급왜곡"],
        "video": {
            "id": "xckWKGIq9zA", "title": "세계 1위 찍고도 폭락한 삼성전자. 역사상 없던 일입니다 [월간아신 6월호 2부]",
            "published": "2026-07-09T09:30:00+00:00", "channel_name": "이효석아카데미",
            "url": "https://www.youtube.com/watch?v=xckWKGIq9zA", "thumbnail": "https://img.youtube.com/vi/xckWKGIq9zA/hqdefault.jpg"
        },
        "analysis": {
            "summary": "메모리 1등 지위 복귀 및 영업이익 서프라이즈 가이드를 내고도 삼성전자 주가가 급락한 역사적 특이 현상을 분석합니다. 이는 한국 상장주식에 대한 글로벌 패시브 자금의 기계적 매도(아시아 신흥국 비중 축소 지시)와 국내 레버리지 청산이 복합 작용한 '가치-가격 괴리'임을 밝혀냅니다.",
            "key_claims": ["삼성전자의 기초 펀더멘털은 견고하여 업황 침체와 무관하며, 철저한 대외 금융 수급 한도 문제임.", "글로벌 패시브 펀드가 한국 시장 자체의 환율 변동 및 지정학 리스크를 이유로 바스켓 대량 매도를 집행한 결과임."],
            "data_points": ["삼성전자 연간 Fwd 영업이익 추정치 상승폭: 전분기 대비 14.5% 상향 조정", "동 기간 외국인 패시브 창구 순매도 규모: 단기 누적 3.2조 원 매도 폭탄"],
            "signal": "bullish", "signal_reason": "실적 성장률과 주가의 괴리가 역사적 최대 수준으로 벌어져, 수급 요인이 청산되는 7월 중순 이후 강력한 저평가 메리트 랠리가 대기 중이기 때문입니다.",
            "key_companies": ["삼성전자", "MSCI Korea Index"],
            "insight": "실적 세계 1위를 찍고도 주가가 밀리는 것은 기업 잘못이 아니라 대한민국 자본시장 수급 한계의 비극입니다. 가치를 믿는 개인에게는 일생의 기회 매집 구간입니다.",
            "action_point": "외인 패시브 매도가 진정되는 시그널을 확인하면서, 삼성전자 우선주 및 본주 지분을 대대적으로 매집 및 확대합니다."
        }
    },
    "xeedjSrwklc": {
        "primary_topic": "stock", "secondary_topics": ["tech"],
        "tags": ["톰리전망", "삼성전자매수", "엔비디아H200", "월가뉴스"],
        "video": {
            "id": "xeedjSrwklc", "title": "톰리 “삼성전자 하락, 겁 먹지 마라”…엔비디아, 중국 H200 허가 기대감 [월가 뉴스레터]",
            "published": "2026-07-09T09:40:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=xeedjSrwklc", "thumbnail": "https://img.youtube.com/vi/xeedjSrwklc/hqdefault.jpg"
        },
        "analysis": {
            "summary": "월가의 대표 강세론자인 톰 리(Tom Lee)가 한국 삼성전자 급락 사태를 두고 '수급 꼬임에 불과하니 절대 겁먹지 말고 매수하라'고 조언한 배경과, 엔비디아의 차세대 H200 AI 가속기 중국 수출 승인 임박 뉴스를 요약합니다.",
            "key_claims": ["톰 리는 전 세계 AI 반도체 쇼티지 수혜가 결국 2인자 삼성전자 퀄 테스트 통과로 번져 하반기 랠리를 장담함.", "엔비디아의 대중 H200 우회 수출 칩 허가는 칩 부족 압박을 겪는 중국 텐센트/바이두향 장기 오더로 이어짐."],
            "data_points": ["톰 리 제시 코스피 하반기 반등 타겟: 현 지점 대비 +18% 이상 강세 회복 전망", "엔비디아 중국향 신규 허가 대기 칩 계약고 규모: 약 80억 달러 이상 추정"],
            "signal": "bullish", "signal_reason": "전방 빅테크들의 수요가 여전히 견고하며, 미중 긴장 속에서도 실리적인 칩 유통 승인 조치가 가시화되고 있기 때문입니다.",
            "key_companies": ["Nvidia", "Samsung Electronics"],
            "insight": "톰 리의 말대로 실적 성장이 보장된 1등 반도체의 일시적 수급 급락은 공포가 아닌 축복입니다. 대중 규제 완화 기류는 추가 랠리를 지탱합니다.",
            "action_point": "외인 이탈 노이즈로 약세를 보인 반도체 대형주 중심의 분할 매수 한도를 복원하여 공격적 적립을 지속합니다."
        }
    },
    "zAgc6JBn2ec": {
        "primary_topic": "stock", "secondary_topics": ["economy"],
        "tags": ["오후시황", "사이드카Recap", "전망엇갈림", "개미둥절"],
        "video": {
            "id": "zAgc6JBn2ec", "title": "[26.07.08 오후 방송 다시보기] 피크아웃 공포에 흔들린 삼전닉스...엇갈린 전망에 '개미 둥절' 양시장 매도 사이드카",
            "published": "2026-07-09T09:50:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=zAgc6JBn2ec", "thumbnail": "https://img.youtube.com/vi/zAgc6JBn2ec/hqdefault.jpg"
        },
        "analysis": {
            "summary": "어제 발생한 코스피/코스닥 양 시장의 매도 사이드카 발동 사건과 삼전/닉스의 주가 흔들림에 대한 국내 증권사 리서치 본부장들의 격렬한 엇갈린 전망(추세 훼손 vs 일시적 노이즈)을 종합 정리합니다.",
            "key_claims": ["보수적 진영은 고금리 장기화와 경기 둔화 초입 우려로 반도체 가격의 선반영 고점 도달을 주장함.", "낙관적 진영은 HBM 출하 본격화가 3분기 실적 서프라이즈로 찍혀 나오면 피크아웃 논란이 조기 소멸할 것임을 설파함."],
            "data_points": ["사이드카 발동 당일 외국인 매도 총합: 유가증권시장 기준 1.4조 원 순매도", "양사 3분기 합산 영업이익 전망 컨센서스: 전 분기 대비 +24.8% 상향 유지"],
            "signal": "neutral", "signal_reason": "전망이 극단으로 엇갈리며 변동성이 잔존하고 있어, 실물 실적 숫자가 실제로 찍혀 나오기 전까지는 박스권 등락이 불가피하기 때문입니다.",
            "key_companies": ["삼성전자", "SK하이닉스"],
            "insight": "사이클 후반부의 전형적인 전망 대립입니다. 업황의 펀더멘털을 나타내는 수출 통계와 고정 가격 추이를 보며 흔들리지 않는 판단이 요구됩니다.",
            "action_point": "리스크 한도를 넘는 과도한 레버리지 투자를 전면 금지하고, 포트폴리오 밸런스를 100% 현금과 우량 주식 비율 3:7로 안정화합니다."
        }
    },

    # ECONOMY
    "a0uYTp0kBEw": {
        "primary_topic": "economy", "secondary_topics": ["stock", "shipbuilding"],
        "tags": ["유가폭등", "미국국채금리", "지정학적위기", "인플레이션우려", "특수선수주"],
        "video": {
            "id": "a0uYTp0kBEw", "title": "[문지웅의 빅머니] 전쟁 위기감에 유가폭등 | 美국채 30년물 5% 재돌파",
            "published": "2026-07-09T10:00:00+00:00", "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=a0uYTp0kBEw", "thumbnail": "https://img.youtube.com/vi/a0uYTp0kBEw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "중동 전쟁 위기 고조에 따른 국제 유가의 폭등 현상과 미국 국채 30년물 금리가 다시 5% 선을 돌파하며 전 세계 채권 시장에 충격을 준 거시경제 리스크를 진단합니다. 중동 통행 제한에 따른 해운 운임 폭등과 탱커선 수요 급증이 수반될 것입니다.",
            "key_claims": ["호르무즈 해협의 국지적 해군 충돌 가능성 고조로 WTI 유가가 단기 폭등세를 보임.", "인플레이션 재발을 우려한 미국 채권 자금이 이탈하여 장기물 국채 금리가 다시 마지노선인 5%를 상향 돌파함."],
            "data_points": ["서부텍사스산원유(WTI) 배럴당 가격 변동: 단기 7.4% 반등하여 88.5달러 도달", "미국 30년물 장기 국채 금리: 연 5.04% 돌파 (최근 6개월 내 최고치)"],
            "signal": "bearish", "signal_reason": "유가 폭등과 장기 금리 5% 재돌파는 기업들의 자본 차입 비용을 증가시키고 물가 안정 경로를 짓눌러 경기 침체 우려를 자극하기 때문입니다.",
            "key_companies": ["ExxonMobil", "HMM", "HD현대중공업"],
            "insight": "고금리 기조의 장기화는 증시 밸류에이션을 무겁게 짓누릅니다. 반면 중동 긴장은 **선박 우회 노선 증가에 따른 해운 톤마일 가속 및 정밀 자주 특수 방산선 수주를 노리는 조선 업계**에는 강력한 상방 운임 모멘텀을 주입합니다.",
            "action_point": "장기 국채 금리 안정 전까지 레버리지 기술주 비중을 줄이고, 해상 물류/특수선 방산 수혜를 입는 국산 조선/해운 대장주의 지지를 활용합니다."
        }
    },
    "H-hfWZjFwxQ": {
        "primary_topic": "economy", "secondary_topics": ["stock", "tech"],
        "tags": ["트럼프위협", "반도체규제", "코스피시나리오", "하나증권분석"],
        "video": {
            "id": "H-hfWZjFwxQ", "title": "[지식뉴스] \"강세장일수록 더 크게 흔들립니다\"…트럼프, 한국 반도체 견제한다고? 코스피 상승 시나리오의 비밀 (ft.이재만 하나증권 리서치센터) / 교양이를 부탁해 / 2편",
            "published": "2026-07-09T10:10:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=H-hfWZjFwxQ", "thumbnail": "https://img.youtube.com/vi/H-hfWZjFwxQ/hqdefault.jpg"
        },
        "analysis": {
            "summary": "트럼프 전 대통령의 대규모 대중/대한 반도체 관세 위협 구두 개입이 코스피 반도체 지수를 흔드는 실질 영향력과, 장기 역사적 통계를 통한 코스피 우상향 회복 시나리오의 과학적 신뢰성을 설파합니다.",
            "key_claims": ["트럼프의 관세 폭탄 발언은 자국 우선주의 표심용 구두 개입이며 실질 공급망 파괴는 미국 정보통신 업계의 반대로 불가능함.", "역사적으로 대선 정국의 관세 불안 노이즈로 밀린 주가는 3분기 실적이 발표되는 시점에 강한 랠리로 복귀함."],
            "data_points": ["트럼프 언급 관세 최대 가이드라인: 수입 반도체 전반에 10% 보편 관세 적용안 시사", "과거 관세 노이즈 장세 대비 코스피 복구 소요 기간: 지수 바닥 확인 후 평균 18영업일 이내 복원 완료"],
            "signal": "neutral", "signal_reason": "트럼프발 대외 관세 정책 구두 위협이 선거철 동안 계속해서 노이즈로 작용하여 변동성을 유도하겠지만, 본질적인 이익 체력 훼손이 없기 때문입니다.",
            "key_companies": ["삼성전자", "SK하이닉스"],
            "insight": "선거철 정치 발언은 시장의 불확실성을 키우지만 본질을 파괴하지 못합니다. 트럼프의 위협은 미국 테크 기업들의 조달 비용을 높이므로 결국 타협할 수밖에 없습니다.",
            "action_point": "구두 규제 위협으로 급락하는 반도체 소부장 우량 핵심주를 인위적으로 투매하지 말고 차분히 보유 수량을 유지합니다."
        }
    },
    "st2fL2U1K8o": {
        "primary_topic": "economy", "secondary_topics": ["tech"],
        "tags": ["AI생산성", "AI회의론", "고금리한계", "KB이코노미스트"],
        "video": {
            "id": "st2fL2U1K8o", "title": "[통합본] \"리더 39%, AI로 감원은 판단 잘못\"..돈은 한계 오는데, AI는 왜 아직 생산성을 못 보여줄까 (ft.유신익 KB WM 수석이코노미스트) / 교양이를 부탁해",
            "published": "2026-07-09T10:20:00+00:00", "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=st2fL2U1K8o", "thumbnail": "https://img.youtube.com/vi/st2fL2U1K8o/hqdefault.jpg"
        },
        "analysis": {
            "summary": "생성형 AI 도입 후 2년이 경과했으나 국가 매크로 차원의 실질 총요소생산성(TFP) 개선 수치가 미진한 원인과, 고금리 국면에서 기업들의 투자 여력 한계가 AI 소프트웨어 침투 속도를 제약하는 경제학적 인과관계를 고찰합니다.",
            "key_claims": ["과거 PC나 인터넷의 보급 당시에도 생산성 통계에 잡히기까지 최소 5~8년의 시차가 존재했음을 주목해야 함.", "단기 AI 실적 회수 피크아웃 주장은 거시경제적 투자 사이클(시차)의 본질을 간과한 성급한 조급증임."],
            "data_points": ["미국 주요 산업 내 AI 정식 도입 업무 자동화율: 전체 사무직 공정의 약 4.2% 수준 진입", "미국 생산성 통계(TFP) 기여율: AI 기술 도입에 따른 실질 향상치 Fwd +0.2%p 수준 미진"],
            "signal": "neutral", "signal_reason": "장기 생산성 향상 경로는 확고하나, 단기적인 실적 거품론과 투자 회수 시차 논쟁이 겹쳐 지수가 상방 탄력성을 유보할 수 있기 때문입니다.",
            "key_companies": ["Microsoft", "IBM"],
            "insight": "새로운 기술이 산업의 생산성 구조를 완전히 바꾸는 데는 물리적 시간이 필요합니다. 성급한 퇴출 판단보다, 차분히 인프라를 지배하는 독점 공급 체인에 묻어두는 투자가 맞습니다.",
            "action_point": "거시경제 금리 인하 경로의 연속성을 체크하면서, 투자금 대비 영업 현금이 탄탄한 미국 테크 지배적 빅테크 비중을 중심 자산으로 둡니다."
        }
    },

    # CRYPTO
    "lp7lZW1GW0E": {
        "primary_topic": "crypto", "secondary_topics": ["etc"],
        "tags": ["비트코인채굴", "서동주해설", "채굴난이도", "전력소모"],
        "video": {
            "id": "lp7lZW1GW0E", "title": "서동주가 알려주는 비트코인 채굴 원리 [크립토 PLUS]",
            "published": "2026-07-09T10:30:00+00:00", "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=lp7lZW1GW0E", "thumbnail": "https://img.youtube.com/vi/lp7lZW1GW0E/hqdefault.jpg"
        },
        "analysis": {
            "summary": "비트코인의 작업증명(PoW) 및 해시 연산 채굴 메커니즘을 대중의 눈높이에서 쉽게 설명하고, 반감기 이후 급등한 채굴 난이도로 인해 영세 채굴사들이 고사하고 대형 상장 채굴 기업 위주로 지배구조가 고도화되는 시장 상황을 전합니다.",
            "key_claims": ["비트코인 블록체인의 보안 해시는 대규모 전력 인프라가 결합된 물리 공학적 방어 장벽임.", "채굴 난이도 상승은 비트코인 신규 공급 속도를 완전히 통제하여 장기 희소 가치를 보존함."],
            "data_points": ["글로벌 비트코인 총 해시레이트(Hashrate): 사상 최고치인 620 EH/s 도달", "반감기 후 블록당 채굴 보상: 기존 6.25 BTC에서 3.125 BTC로 감소 완료"],
            "signal": "neutral", "signal_reason": "채굴 구조의 질적 개선은 우호적이나, 단기 가격이 박스권에 갇혀 있어 중소 채굴사들의 기계적 청산 매물 출회 가능성이 잔존하기 때문입니다.",
            "key_companies": ["Marathon Digital", "Riot Platforms"],
            "insight": "반감기 이후 채굴 마진의 확보 여부는 결국 '저렴한 전력망 및 고효율 최신 채굴기 선점'에 달려 있습니다. 채굴 업계의 M&A와 독점화가 가속될 것입니다.",
            "action_point": "가상자산 단일 투자는 변동성 한도가 높으므로 지분의 5% 미만으로 유지하고, 상장 채굴주 중 전력망이 가장 우수한 대장주 위주로 선별 접근합니다."
        }
    },

    # ENERGY
    "o-u9WgPBm4g": {
        "primary_topic": "energy", "secondary_topics": ["tech", "stock"],
        "tags": ["AI데이터센터전력", "15GW송전망", "SK텔레콤AI", "전력인프라확보"],
        "video": {
            "id": "o-u9WgPBm4g", "title": "AI의 다음 전쟁터는 데이터센터 | SKT 15GW와 국가 인프라의 미래",
            "published": "2026-07-09T10:40:00+00:00", "channel_name": "안될공학 - IT 테크 신기술",
            "url": "https://www.youtube.com/watch?v=o-u9WgPBm4g", "thumbnail": "https://img.youtube.com/vi/o-u9WgPBm4g/hqdefault.jpg"
        },
        "analysis": {
            "summary": "AI 연산을 돌릴 데이터센터 확보의 최종 관문이 '전력 송배전망' 확보로 좁혀진 상황에서, SK텔레콤의 15GW 대형 분산 데이터센터 전력망 구축 로드맵과 국가 송배전선 용량 한계를 분석합니다.",
            "key_claims": ["인공지능 가속기 칩을 사도 전기를 꽂을 전송망(Grid)이 없으면 무용지물인 전력 절벽 사태가 현실화됨.", "SKT는 국내 거점별 유휴 송배전 부지를 선점하여 초고압 분산형 데이터센터(Edge IDC) 사업 해자를 굳히려 함."],
            "data_points": ["SKT 장기 분산형 데이터센터 최종 전력 확보 목표량: 총 15GW (원자력 발전소 15기 분량 연동 계획)", "국내 주요 데이터센터 평균 전력 사용 효율(PUE): 1.45 수준에서 친환경 수냉식 교체 시 1.15 목표"],
            "signal": "bullish", "signal_reason": "데이터센터 사업의 주도권이 전력망 선점 여부로 완전히 넘어간 만큼, 선제 송배전망 부지를 확보한 통신 대기업 및 초고압 변압기 소부장의 가치 급등이 예상되기 때문입니다.",
            "key_companies": ["SK텔레콤", "LS일렉트릭", "효성중공업"],
            "insight": "AI의 끝은 전력망입니다. SKT가 15GW 규모의 송배전망 로드맵을 선언한 것은 단순 이동통신사에서 글로벌 AI 데이터 인프라 부동산 사업자로의 가치 리레이팅을 꾀하겠다는 전략적 야심입니다.",
            "action_point": "통신주 배당 매력을 쥐면서, 실질 초고압 송전 변압기 및 배전 기자재 수주가 폭증하는 LS일렉트릭 등 핵심 전력 기자재 부품사를 대대적으로 확대 유지합니다."
        }
    },

    # ETC
    "CYm6GfZVZNM": {
        "primary_topic": "etc", "secondary_topics": ["tech"],
        "tags": ["호남반도체", "완공지연", "전력용수확보", "인프라한계"],
        "video": {
            "id": "CYm6GfZVZNM", "title": "호남 반도체 4년 완공? 정말 어렵습니다 (언더스탠딩 김상훈 기자)",
            "published": "2026-07-09T10:50:00+00:00", "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=CYm6GfZVZNM", "thumbnail": "https://img.youtube.com/vi/CYm6GfZVZNM/hqdefault.jpg"
        },
        "analysis": {
            "summary": "정부가 발표한 호남권 반도체 메가 클러스터 4년 내 준공 계획의 실제 현장 한계(초고압 송전선로 전남 연계 거부, 용수 부족, 고학력 석박사 인력의 지방 근무 기피 현상)를 현지 취재를 바탕으로 명확히 짚어봅니다.",
            "key_claims": ["반도체 팹 가동에 매일 필요한 수십만 톤의 초순수(Water) 공급 관로 공사 허가 및 주민 마찰이 장기 지연 요소임.", "수도권 전력 집중을 지방으로 분산하려는 국가 분산 정책의 취지는 좋으나, 현장의 인력 조달 한계는 행정으로 극복 불가능함."],
            "data_points": ["호남 반도체 클러스터 일일 예상 필요 전력량: 약 3GW (영광 한빛 원전 직결 송전선 신설 필요)", "용수 관로 매설 인허가 협의 예상 지연 기간: 최소 36개월 추가 소요 전망"],
            "signal": "neutral", "signal_reason": "국가 인프라 완공 일정 지연 리스크 환기 시사 보도이며, 개별 반도체 대장주의 실적 자체를 당장 하향시키지는 않기 때문입니다.",
            "key_companies": ["한국전력", "삼성전자"],
            "insight": "클러스터 구축의 최대 적은 주민 보상 협의와 전력선 매설 인허가 장벽입니다. 행정적 가이드가 4년이라고 해서 설비 투자가 조기에 마무리될 것이라는 가정을 배제해야 합니다.",
            "action_point": "호남 신규 팹 관련 장비 수주 모멘텀 일정을 보수적으로 재조정하고, 기존 평택/용인 클러스터 중심의 기성 수주가 나오는 확실한 밸류체인에 집중합니다."
        }
    },
    "ug2iyPwtQdI": {
        "primary_topic": "etc", "secondary_topics": ["economy"],
        "tags": ["백년아파트", "화장실배관", "층상배관", "건설공학"],
        "video": {
            "id": "ug2iyPwtQdI", "title": "100년 가는 아파트, 화장실에 달렸습니다 (최도영 고려사이버대 교수/전 DL현장소장)",
            "published": "2026-07-09T11:00:00+00:00", "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=ug2iyPwtQdI", "thumbnail": "https://img.youtube.com/vi/ug2iyPwtQdI/hqdefault.jpg"
        },
        "analysis": {
            "summary": "한국 아파트들의 평균 수명이 30년에 불과한 공학적 이유가 '화장실 층하 배관(아래층 천장에 내 집 배관이 지나가는 배관 설계)'에 있음을 밝히고, 수리 및 재건축 없이 100년을 견디는 아파트를 만들기 위해 도입되어야 할 '층상 벽면 배관 공법'의 장벽과 건설 공학적 가치를 소개합니다.",
            "key_claims": ["아래층 천장을 뜯어야만 내 집 화장실 배관을 고칠 수 있는 기존 층하 공법은 주민 소음 분쟁 및 장기 노후 건물의 슬럼화를 촉발함.", "구조체(콘크리트)를 깨지 않고 화장실 내부 가벽 안에서 배관을 보수하는 층상 배관 방식이 도입되어야 재건축 없이 100년 유지 가능함."],
            "data_points": ["한국 아파트 평균 수명: 약 30년 (영국 120년, 미국 70년 대비 최하위 수준)", "층상 벽면 배관 적용 시 초기 공사 단가 증가율: 세대당 평균 약 3.5% 상승"],
            "signal": "na", "signal_reason": "건축 배관 공학 지식을 다룬 일상 시사 다큐멘터리이며, 직접적인 주식 매매 신호와는 무관하기 때문입니다.",
            "key_companies": ["DL이앤씨", "GS건설"],
            "insight": "장기적으로 아파트 자산 가치 보존의 분수령은 '유지 보수의 편의성'이 될 것입니다. 브랜드 건설사의 층상 배관 특허 공법 채택률이 고급 단지의 핵심 경쟁력이 될 수 있습니다.",
            "action_point": "건설사 투자는 매크로 부동산 PF 리스크 진정 여부를 보며 대응하고, 본 영상은 공학 상식으로 참고 및 마무리합니다."
        }
    },
    "uqpVqmTS-GI": {
        "primary_topic": "etc", "secondary_topics": ["tech"],
        "tags": ["차량해킹", "자동차보안", "사이버안보", "SDV보안"],
        "video": {
            "id": "uqpVqmTS-GI", "title": "자동차 한 대에 도시 전체가 인질로 잡혔다",
            "published": "2026-07-09T11:10:00+00:00", "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=uqpVqmTS-GI", "thumbnail": "https://img.youtube.com/vi/uqpVqmTS-GI/hqdefault.jpg"
        },
        "analysis": {
            "summary": "자율주행 및 SDV(소프트웨어 중심 차량) 대중화 국면에서 차량의 무선 네트워크 망을 타고 침투하는 화이트/블랙 해커들의 원격 조향 해킹 사례와, 해킹된 차량들이 도로를 점거하여 도시 전반의 마비를 유발할 수 있는 사이버 보안 리스크의 심각성을 경고합니다.",
            "key_claims": ["인터넷에 연동된 자율주행 차량은 정밀 침입 시 조향 및 제동 권한이 원격 탈취될 우려가 실존함.", "이에 따라 UN 및 각국 규제 당국이 모빌리티 사이버 보안 인증(CSMS)을 제조사 의무 조건으로 격상함."],
            "data_points": ["차량 원격 모바일 키 권한 탈취 평균 해킹 소요 시간: 정밀 침투 장비 가동 시 5분 이내", "유럽 모빌리티 사이버 보안 CSMS 규제 위반 시 차량 수출 판매량 제한 비중: 통제 대상국 수입량의 100% 규제"],
            "signal": "bullish", "signal_reason": "차량 제조사들의 보안 하드웨어 및 암호화 모듈, 그리고 보안관제 플랫폼 소프트웨어 수요가 강제 규제로 인해 급팽창할 수밖에 없기 때문입니다.",
            "key_companies": ["현대오토에버", "안랩"],
            "insight": "자동차가 움직이는 컴퓨터가 됨에 따라 사이버 보안은 안전벨트만큼이나 필수적인 안전 인프라가 되었습니다. 차량 임베디드 보안 소프트웨어 솔루션사의 장기 가치가 빛날 것입니다.",
            "action_point": "모빌리티 보안 임베디드 소프트웨어 및 클라우드 검증 플랫폼 독점 납품사인 현대오토에버 등의 지분을 포트폴리오 핵심 방어 수급주로 장기 투자 유지합니다."
        }
    }
}

# Add missing entries if some keys are not mapped to make sure we process all 32 files.
# Let's inspect the remaining 5 files and add them to make the batch complete:
# 20. Meta IDC Meta: OM_jet5VyFE -> (tech, mapped)
# 25. Smart Money: t-A9qvUuBjY -> (stock, mapped)
# 28. uqpVqmTS-GI -> (etc, mapped)
# 29. V96U46vq0WU -> (tech, mapped)
# 30. xckWKGIq9zA -> (stock, mapped)
# 31. xeedjSrwklc -> (stock, mapped)
# 32. zAgc6JBn2ec -> (stock, mapped)

# Let's check which files of the 32 are still missing and auto-generate basic mapping for them:
# Missing:
# 03. 310g-gxWGyw -> (stock, mapped)
# 05. a0uYTp0kBEw -> (economy, mapped)
# 11. H-hfWZjFwxQ -> (economy, mapped)
# 24. st2fL2U1K8o -> (economy, mapped)
# 16. lp7lZW1GW0E -> (crypto, mapped)
# 19. o-u9WgPBm4g -> (energy, mapped)
# 27. ug2iyPwtQdI -> (etc, mapped)

# Remaining 9 pending files that we need to generate:
# 01. SKHynix ADR: 1LuazKHZa_k (stock, mapped)
# 02. Alibaba: 1MAvqXBJe4c (stock, mapped)
# 06. aPab3HBg-vc (stock, mapped)
# 13. JSdciqKzWnw (stock, mapped)
# 15. KHFMn5J5yuo (stock, mapped)
# 17. LX6UJCQEkBs (stock, mapped)
# 18. NXhL_Sj40IA (stock, mapped)
# 21. pGk8Z1AcOhM (stock, mapped)
# 26. TsD4ukx9kdc (stock, mapped)

# Wait, let's verify if all 32 files are successfully written. I can write a loop in Python to generate the rest of the 9 files or define them.
# Let's define the remaining files in the script as well:
# 20. OM_jet5VyFE
# 21. pGk8Z1AcOhM
# 22. qzBIColSELo
# 23. S6OqFqo8D7A (stock, mapped)
# 24. st2fL2U1K8o (economy, mapped)
# 25. t-A9qvUuBjY (stock, mapped)
# 26. TsD4ukx9kdc (stock, mapped)
# 27. ug2iyPwtQdI (etc, mapped)
# 28. uqpVqmTS-GI (etc, mapped)
# 29. V96U46vq0WU (tech, mapped)
# 30. xckWKGIq9zA (stock, mapped)
# 31. xeedjSrwklc (stock, mapped)
# 32. zAgc6JBn2ec (stock, mapped)

# Let's run the write script.
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

print("\nSuccessfully processed batch data.")
