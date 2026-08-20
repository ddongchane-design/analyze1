import json
import os
from pathlib import Path

batch3_data = {
    "FkMBJWYopzY": {
        "primary": "stock",
        "data": {
            "video": {
                "id": "FkMBJWYopzY",
                "title": "\"온 우주가 내 매매를 감시한다\" 트레이딩 꿀팁은?  | 김민수 레몬리서치 대표 [더블 업]",
                "published": "2026-08-18T05:42:21+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=FkMBJWYopzY",
                "thumbnail": "https://img.youtube.com/vi/FkMBJWYopzY/hqdefault.jpg"
            },
            "analysis": {
                "summary": "내가 사면 떨어지고 내가 팔면 급등하는 투자자들의 전형적인 심리적 착각(FOMO와 공포)의 원인을 짚고, 호가창을 실시간 감시하는 뇌동매매를 끊어내는 <span class=\"text-cyan-300 font-semibold\">원칙 기반 트레이딩 규칙</span>을 조언함. 분할 매수와 사전 손절/익절선 설정 등 감정을 배제한 시스템 매매의 중요성을 강조함.",
                "key_claims": [
                    "단기 등락에 집착해 잦은 매매를 반복할수록 수수료와 슬리피지로 인해 계좌 손실 확률이 기하급수적으로 증가함.",
                    "진입 전 매수 이유와 목표가, 손절 기준을 명확히 문서화하고 시세창을 끄는 훈련이 필수적임."
                ],
                "data_points": [
                    "개인 투자자 평균 보유 기간 단축 및 잦은 손절매로 인한 누적 손실 통계",
                    "원칙 준수 트레이더의 장기 승률 비교"
                ],
                "signal": "neutral",
                "signal_reason": "투자 멘탈 및 매매 기법 교육으로 개별 종목에 대한 시그널과는 중립적임.",
                "key_companies": [],
                "insight": "시장은 개인을 감시하는 것이 아니라 대중의 탐욕과 공포라는 보편적 심리를 역이용할 뿐이므로, 원칙 없는 뇌동매매를 멈추는 것이 수익의 출발점임.",
                "action_point": "매매 일지 작성을 통해 충동적 진입을 억제하고, 계좌 내 현금 비중 20~30%를 상시 유지하는 리스크 관리 실행."
            },
            "classification": {
                "primary_topic": "stock",
                "secondary_topics": [],
                "tags": ["트레이딩", "투자심리", "뇌동매매방지", "손절원칙", "자산관리"]
            }
        }
    },
    "JKEcxZFbFik": {
        "primary": "economy",
        "data": {
            "video": {
                "id": "JKEcxZFbFik",
                "title": "트럼프, 호르무즈 미국 영토 주장…중동 불안에 고금리 압박 지속 [월가 뉴스레터]",
                "published": "2026-08-18T22:13:08+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=JKEcxZFbFik",
                "thumbnail": "https://img.youtube.com/vi/JKEcxZFbFik/hqdefault.jpg"
            },
            "analysis": {
                "summary": "도널드 트럼프 전 대통령의 <span class=\"text-violet-300 font-medium\">호르무즈 해협 통제권 및 파격적 지정학적 발언</span>과 중동 내 긴장 고조가 국제 유가 상방 압력과 미국 장기 국채금리 급등을 자극하고 있음. 인플레이션 재점화 우려로 연준의 금리 인하 기대가 후퇴하면서 월가 전반에 고금리 장기화(Higher for Longer) 경계감이 팽배함.",
                "key_claims": [
                    "중동 원유 수송로인 호르무즈 해협 봉쇄 및 군사적 긴장은 국제 유가 80달러 중후반대 안착을 유발하는 직접적 요인.",
                    "유가 상승과 대규모 미 국채 발행 물량이 맞물리며 10년물 국채금리가 4.5%를 돌파하는 등 금융시장 유동성을 압박.",
                    "지정학적 리스크 프리미엄과 정치적 불확실성이 복합 작용하여 주식시장의 밸류에이션 확장을 제한."
                ],
                "data_points": [
                    "WTI 원유 선물 가격 장중 배럴당 82~85달러선 등락",
                    "미국 10년물 및 30년물 국채금리 각각 4.5% 및 4.7% 근접"
                ],
                "signal": "bearish",
                "signal_reason": "지정학적 리스크와 유가 반등, 국채금리 상승의 삼중고가 단기 증시의 밸류에이션 조정을 유발할 가능성이 큼.",
                "key_companies": ["엑슨모빌(XOM)", "셰브론(CVX)"],
                "insight": "대선 국면의 정치적 강경 발언과 중동 안보 불안은 유가 및 금리를 자극해 주식 시장의 최대 적인 '고금리 장기화'를 강제하는 구조적 리스크임.",
                "action_point": "에너지 ETF 및 원자재 헤지 비중을 점검하고, 금리 민감 고밸류 성장주에 대한 단기 비중 조절 필요."
            },
            "classification": {
                "primary_topic": "economy",
                "secondary_topics": ["stock", "energy"],
                "tags": ["트럼프", "호르무즈", "국제유가", "미국국채금리", "지정학리스크"]
            }
        }
    },
    "KexGs35AOwA": {
        "primary": "tech",
        "data": {
            "video": {
                "id": "KexGs35AOwA",
                "title": "단기 수급에 흔들리지 말자…AI·반도체 장기 사이클에서 봐야 할 것들 | 정우창, 여도은, 허재무 [아침N투자]",
                "published": "2026-08-18T02:27:58+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=KexGs35AOwA",
                "thumbnail": "https://img.youtube.com/vi/KexGs35AOwA/hqdefault.jpg"
            },
            "analysis": {
                "summary": "단기적인 매크로 금리 노이즈와 수급 변동성에도 불구하고 <span class=\"text-cyan-300 font-semibold\">HBM 및 차세대 AI 반도체 사이클</span>은 2027~2028년까지 공급 부족이 지속되는 구조적 슈퍼사이클에 진입해 있음. 엔비디아 블랙웰 플랫폼 본격 양산과 맞물려 SK하이닉스, 삼성전자 등 핵심 메모리 공급사의 이익 체력이 역사적 최고치를 갱신할 것으로 전망됨.",
                "key_claims": [
                    "빅테크의 AI 인프라 투자(CapEx) 축소 조짐은 전혀 없으며 오히려 자체 커스텀 ASIC 및 고용량 HBM 주문량이 증가.",
                    "단기 주가 조정은 밸류에이션 부담을 덜어내는 건전한 숨고르기일 뿐, AI 칩 수요의 펀더멘털은 훼손되지 않음.",
                    "<span class=\"text-cyan-300 font-semibold\">HBM3E 12단 및 HBM4</span> 선점 경쟁에서 기술 격차를 입증한 기업들이 마진율 프리미엄을 독식할 것임."
                ],
                "data_points": [
                    "2026~2027년 글로벌 HBM 시장 연평균 성장률(CAGR) 45% 이상 전망",
                    "SK하이닉스 HBM3E 수율 80% 이상 안정화 및 2027년 물량 사전 완판"
                ],
                "signal": "bullish",
                "signal_reason": "단기 수급 조정 이후 실적 가시성이 가장 높은 반도체 섹터의 추가 상승 랠리가 전개될 가능성이 매우 높음.",
                "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "엔비디아(NVDA)", "한미반도체(042700)"],
                "insight": "AI 반도체는 과거 경기 순환형 메모리 사이클과 달리 맞춤형 고부가가치 수주 산업으로 체질이 변화하여, 높은 마진율과 긴 호황 주기를 유지함.",
                "action_point": "주가 조정 시점을 이용하여 HBM 밸류체인 및 선단 공정 반도체 소부장 대장주에 대한 비중 확대를 지속할 것."
            },
            "classification": {
                "primary_topic": "tech",
                "secondary_topics": ["stock", "economy"],
                "tags": ["HBM", "AI반도체", "SK하이닉스", "삼성전자", "반도체사이클"]
            }
        }
    },
    "NC5t7PmANGc": {
        "primary": "tech",
        "data": {
            "video": {
                "id": "NC5t7PmANGc",
                "title": "현금없이 300조원 버는 방법",
                "published": "2026-08-18T11:00:29+00:00",
                "channel_name": "Softdragon SOD",
                "url": "https://www.youtube.com/watch?v=NC5t7PmANGc",
                "thumbnail": "https://img.youtube.com/vi/NC5t7PmANGc/hqdefault.jpg"
            },
            "analysis": {
                "summary": "빅테크 및 스타트업들이 막대한 물리적 자본 없이 <span class=\"text-cyan-300 font-semibold\">AI 에이전트와 소프트웨어 플랫폼의 네트워크 효과</span>를 통해 수백조 원의 기업가치를 창출하는 현대 자본주의의 레버리지 메커니즘을 분석함. 한계비용이 '0'에 수렴하는 AI 소프트웨어 복제력과 글로벌 유통망 장악력이 부의 공식을 바꾸고 있음.",
                "key_claims": [
                    "물리적 공장이나 막대한 초기 자본 없이도 고성능 AI 에이전트 아키텍처를 구축하면 글로벌 단위로 폭발적 확장이 가능함.",
                    "데이터와 알고리즘의 결합이 전통 제조업 대비 수십 배 높은 영업이익률과 밸류에이션 멀티플을 부여받음."
                ],
                "data_points": [
                    "글로벌 빅테크 소프트웨어 마진율 70~80% 수준 기록",
                    "AI 스타트업들의 유니콘 기업 진입 속도 2배 단축"
                ],
                "signal": "bullish",
                "signal_reason": "AI 소프트웨어 및 플랫폼 기업들의 독점적 마진 구조와 무한 확장성이 장기 기업가치 성장을 보증함.",
                "key_companies": ["마이크로소프트(MSFT)", "팔란티어(PLTR)", "오픈AI"],
                "insight": "AI 시대의 부는 유형 자산을 보유한 기업이 아니라, 지능(Intelligence)을 코드로 캡슐화하여 전 세계에 실시간 배포하는 소프트웨어 기업으로 집중됨.",
                "action_point": "고마진 소프트웨어 플랫폼 및 AI 에이전트 서비스 선도 기업에 대한 장기적 안목의 투자 지속."
            },
            "classification": {
                "primary_topic": "tech",
                "secondary_topics": ["stock"],
                "tags": ["소프트웨어", "AI에이전트", "플랫폼비즈니스", "네트워크효과", "고마진"]
            }
        }
    },
    "NJrf_fFC9Js": {
        "primary": "etc",
        "data": {
            "video": {
                "id": "NJrf_fFC9Js",
                "title": "시간당 124.5mm, 거제 폭우가 기록적이었던 이유",
                "published": "2026-08-18T05:19:26+00:00",
                "channel_name": "안될과학 Unrealscience",
                "url": "https://www.youtube.com/watch?v=NJrf_fFC9Js",
                "thumbnail": "https://img.youtube.com/vi/NJrf_fFC9Js/hqdefault.jpg"
            },
            "analysis": {
                "summary": "거제 지역에 쏟아진 시간당 124.5mm의 기록적 극한 폭우를 초래한 <span class=\"text-amber-300 font-bold\">기상학적 메커니즘(선상 강수대 및 해수면 온도 상승)</span>을 과학적으로 분석함. 한반도 주변 해역의 이상 고수온과 남서풍을 타고 유입된 다량의 수증기가 좁은 지형에 정체되며 초강력 수증기 통로를 형성한 과정을 설명함.",
                "key_claims": [
                    "지구 온난화로 한반도 주변 해수면 온도가 예년 대비 2~3도 상승하여 대기 중 포함 가능한 수증기량이 급증함.",
                    "지형적 요인과 대기 상하층의 강한 기압골이 맞물려 비구름대가 특정 지역에 지속적으로 재생성되는 선상 강수대 형성.",
                    "기후변화로 인해 과거 100년 빈도의 극한 기상 재해가 연례화되는 추세임."
                ],
                "data_points": [
                    "거제 시간당 124.5mm 강수량: 역대 관측 사상 최고치 경신",
                    "해수면 온도 1도 상승 시 대기 중 수증기 포화량 약 7% 증가 (클라우지우스-클라페이롱 방정식)"
                ],
                "signal": "neutral",
                "signal_reason": "기후 과학 및 재난 방재 정보로 시장 투자 시그널과는 중립적임.",
                "key_companies": [],
                "insight": "기후 위기는 더 이상 미래의 예측이 아니라 인프라 안전 기준과 도시 방재 시스템 전면 재설계를 요구하는 실질적 현실임.",
                "action_point": "도시 치수 인프라 및 기후 재난 복구, 스마트 배수 시스템 관련 기술의 사회적 중요성 확인."
            },
            "classification": {
                "primary_topic": "etc",
                "secondary_topics": [],
                "tags": ["거제폭우", "기상이변", "선상강수대", "지구온난화", "방재과학"]
            }
        }
    },
    "OSDOJt27ufc": {
        "primary": "economy",
        "data": {
            "video": {
                "id": "OSDOJt27ufc",
                "title": "[박신영의 개장전요것만-8월18일] 채권자경단, 패닉 버튼 누를까 | 월가 '반도체 조정장 다시 오나' 긴장",
                "published": "2026-08-18T14:18:38+00:00",
                "channel_name": "한경 글로벌마켓",
                "url": "https://www.youtube.com/watch?v=OSDOJt27ufc",
                "thumbnail": "https://img.youtube.com/vi/OSDOJt27ufc/hqdefault.jpg"
            },
            "analysis": {
                "summary": "미국 재정 적자 폭증과 국채 입찰 부담으로 <span class=\"text-rose-400 font-medium\">채권자경단(Bond Vigilantes)의 국채 매도 공세</span>가 재개되며 미 10년물 금리가 5%를 위협하는 국면에 진입함. 금리 급등과 전력망 규제로 코어위브 등 AI 인프라 기업의 부담이 가중되는 가운데, 마이크론·AMD 등 주요 반도체주의 단기 조정 장세가 심화되고 있음.",
                "key_claims": [
                    "미국 정부의 무제한적 국채 발행에 반발하는 채권 시장의 프리미엄 요구로 장기 국채금리가 급등세 지속.",
                    "지방 정부의 전력 부족 및 요금 인상 규제가 AI 데이터센터 건설 속도에 일부 제동을 걸고 있음.",
                    "단기적으로 반도체와 빅테크 주가가 밸류에이션 부담과 고금리 충격으로 조정 압력을 받고 있으나, AI 추론 수요 증가는 인프라 확장의 하단을 지지함."
                ],
                "data_points": [
                    "미 10년물 국채금리 4.5% 상회 및 5% 터치 경계감 확대",
                    "마이크론, AMD 등 반도체 주요 종목 장전 4~5% 급락세 기록"
                ],
                "signal": "bearish",
                "signal_reason": "채권금리 급등과 전력 규제 노이즈가 맞물려 단기적으로 기술주 및 반도체 섹터의 변동성 확대가 불가피함.",
                "key_companies": ["엔비디아(NVDA)", "마이크론(MU)", "AMD(AMD)", "코어위브(CoreWeave)"],
                "insight": "채권 시장의 금리 반란은 과열된 주식 시장에 찬물을 끼얹는 가장 강력한 변수이며, 데이터센터 전력망 병목과 결합하여 단기 기술주 조정 폭을 키울 수 있음.",
                "action_point": "미 국채 입찰 수요와 10년물 금리 추이를 확인하며 레버리지 포지션을 축소하고 방어적 현금 비중을 확보할 것."
            },
            "classification": {
                "primary_topic": "economy",
                "secondary_topics": ["stock", "tech"],
                "tags": ["채권자경단", "미국국채금리", "반도체조정", "전력부족", "코어위브"]
            }
        }
    }
}

for vid, item in batch3_data.items():
    primary = item["primary"]
    out_dir = Path(f"data/analyzed/{primary}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{vid}.json"
    with open(out_file, "w", encoding="utf-8") as fp:
        json.dump(item["data"], fp, ensure_ascii=False, indent=2)
    
    pending_file = Path(f"data/pending/{vid}.json")
    if pending_file.exists():
        pending_file.unlink()
    print(f"[Batch 3 완료] {vid} -> data/analyzed/{primary}/{vid}.json")
