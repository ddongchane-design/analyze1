import json
import os
from pathlib import Path

batch4_data = {
    "SKi3puP_kjQ": {
        "primary": "crypto",
        "data": {
            "video": {
                "id": "SKi3puP_kjQ",
                "title": "비트코인 한 달 만에 3% 급등…반등 지속될까? 금리·규제·수급 변수 점검  | 김동환, 박상혁 디지털애셋 편집장 [크립토 PLUS]",
                "published": "2026-08-18T02:48:00+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=SKi3puP_kjQ",
                "thumbnail": "https://img.youtube.com/vi/SKi3puP_kjQ/hqdefault.jpg"
            },
            "analysis": {
                "summary": "비트코인이 지지부진한 횡보세를 뚫고 반등을 시도하는 가운데, <span class=\"text-amber-300 font-bold\">미국 대선 정국의 가상자산 친화적 정책 공약</span>과 비트코인 현물 ETF로의 기관 자금 순유입 재개가 상승 모멘텀을 형성하고 있음. 마운트곡스 상환 등 대형 오버행(잠재 매도 물량) 이슈가 시장에서 점진적으로 소화되며 하방 경직성이 강화됨.",
                "key_claims": [
                    "미국 정치권(공화/민주 양당)의 가상자산 규제 명확화 및 비트코인 전략비축 자산화 논의가 기관 신뢰도를 제고.",
                    "독일 정부 압류 물량 및 마운트곡스 채권자 배분 등 시장을 짓누르던 공급 충격이 상당 부분 시장에 선반영 및 흡수됨.",
                    "금리 인하 사이클 진입 시 글로벌 유동성 확장의 최대 수혜 자산으로 비트코인이 다시 부각될 전망."
                ],
                "data_points": [
                    "비트코인 현물 ETF 주간 순유입액 수억 달러 반등",
                    "거래소 내 비트코인 보유 잔고 5년 래 최저치 경신(장기 보유자 축적 지속)"
                ],
                "signal": "bullish",
                "signal_reason": "수급적 오버행 해소와 기관 자금의 꾸준한 ETF 매입, 대선 정책 수혜 기대감이 중기 상승 추세를 지지함.",
                "key_companies": ["마이크로스트래티지(MSTR)", "코인베이스(COIN)", "블랙록(BLK)"],
                "insight": "비트코인은 개인 투기 자산에서 기관 연기금과 글로벌 자산운용사의 대체 포트폴리오 핵심 자산으로 완전히 제도권화되었음.",
                "action_point": "거시 유동성 완화 국면에 대비해 비트코인 및 이더리움 현물 ETF 위주의 점진적 분할 적립 전략 유지."
            },
            "classification": {
                "primary_topic": "crypto",
                "secondary_topics": ["economy", "stock"],
                "tags": ["비트코인", "크립토", "현물ETF", "오버행해소", "디지털자산"]
            }
        }
    },
    "VvjnB_Lznfc": {
        "primary": "tech",
        "data": {
            "video": {
                "id": "VvjnB_Lznfc",
                "title": "AI 토큰 10배 폭증…반도체 공급 부족은 2028년까지 계속된다ㅣ김장열 유니스토리자산운용 리서치센터장 [집중 오늘의 주식]",
                "published": "2026-08-18T11:30:16+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=VvjnB_Lznfc",
                "thumbnail": "https://img.youtube.com/vi/VvjnB_Lznfc/hqdefault.jpg"
            },
            "analysis": {
                "summary": "AI 에이전트 서비스와 다중 모달(Multimodal) 추론의 대중화로 <span class=\"text-cyan-300 font-semibold\">AI 토큰 생성량이 기존 대비 10배 이상 폭증</span>하고 있어, HBM과 첨단 패키징 등 고성능 반도체 공급 부족 현상이 2028년까지 장기화될 것으로 전망됨. 빅테크들의 데이터센터 인프라 지출은 일시적 유행이 아닌 필수 생존 투자로 자리잡음.",
                "key_claims": [
                    "단순 검색용 챗봇을 넘어 자율 에이전트가 작동하면서 추론 단계의 컴퓨팅 및 메모리 대역폭 소모량이 기하급수적으로 폭증.",
                    "TSMC의 CoWoS 어드밴스드 패키징과 SK하이닉스의 <span class=\"text-cyan-300 font-semibold\">HBM3E/HBM4</span> 공급 능력이 2027~2028년까지 타이트한 수급 상태를 유지할 것임.",
                    "반도체 사이클의 피크아웃 우려는 기우이며, 구조적 공급 제한으로 인해 제조사들의 높은 영업이익률이 장기 지속됨."
                ],
                "data_points": [
                    "글로벌 AI 추론 토큰 소모량 전년 대비 1,000% 급증",
                    "2026~2028년 첨단 패키징 및 HBM 라인 가동률 100% 근접 유지 전망"
                ],
                "signal": "bullish",
                "signal_reason": "AI 토큰 폭증에 따른 전방 수요의 구조적 팽창과 공급 병목이 반도체 슈퍼사이클의 지속 기간을 대폭 연장함.",
                "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "TSMC(TSM)", "엔비디아(NVDA)"],
                "insight": "AI 투자는 모델 학습(Training)에서 실시간 추론(Inference) 시대로 무게중심이 이동하며, 막대한 토큰 처리를 위한 광대역 메모리 수요를 끝없이 창출하고 있음.",
                "action_point": "단기 주가 등락에 연연하지 말고 2028년까지 구조적 실적 성장이 보장된 메모리 반도체 대장주와 첨단 패키징 장비주를 뚝심 있게 보유할 것."
            },
            "classification": {
                "primary_topic": "tech",
                "secondary_topics": ["stock", "economy"],
                "tags": ["AI토큰", "HBM", "반도체슈퍼사이클", "SK하이닉스", "추론컴퓨팅"]
            }
        }
    },
    "YcAL8pSe59M": {
        "primary": "stock",
        "data": {
            "video": {
                "id": "YcAL8pSe59M",
                "title": "[26.08.18 오후 방송 전체보기] 코스피 6거래일 만에 하락, 엇갈리는 반도체 투톱…코스닥은 순환매 장세",
                "published": "2026-08-18T11:05:47+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=YcAL8pSe59M",
                "thumbnail": "https://img.youtube.com/vi/YcAL8pSe59M/hqdefault.jpg"
            },
            "analysis": {
                "summary": "연일 상승세를 이어가던 코스피가 6거래일 만에 숨고르기에 들어가며 하락 마감함. <span class=\"text-cyan-300 font-semibold\">삼성전자와 SK하이닉스 간 수급 차별화</span>가 나타난 가운데, 코스닥 시장에서는 2차전지와 바이오, 로봇 등 낙폭과대 테마로의 빠른 순환매가 전개됨. 외국인 선물 매도와 원/달러 환율 상승이 지수 상단을 제약함.",
                "key_claims": [
                    "지수 연속 상승에 따른 피로감과 미국 장기 국채금리 반등이 맞물려 차익실현 매물 출회.",
                    "대형 반도체주 내에서도 HBM 경쟁력 차이에 따른 외국인 매매 패턴의 양극화가 뚜렷해짐.",
                    "코스닥 중소형주는 주도 섹터의 단기 휴식기를 틈타 빠른 키 맞추기 순환매 랠리가 지속됨."
                ],
                "data_points": [
                    "코스피 지수 -0.85% 하락 마감 및 외국인 선물 순매도 1조 원 상회",
                    "원/달러 환율 1,380원대 중반 등락"
                ],
                "signal": "neutral",
                "signal_reason": "추세 이탈이 아닌 상승 피로도에 따른 건전한 눌림목 조정이며, 섹터별 순환매가 유지되고 있음.",
                "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "에코프로비엠(247540)", "알테오젠(196170)"],
                "insight": "지수 고점대에서의 일시적 조정은 건강한 손바뀜 과정이며, 이때 상대적으로 낙폭이 작고 기관 순매수가 유입되는 차기 주도 섹터를 선별해야 함.",
                "action_point": "순환매 장세에 편승한 추격 매수보다는 HBM 대장주 및 수출 실적주가 조정받을 때 분할 매수로 대응하는 전략이 유리함."
            },
            "classification": {
                "primary_topic": "stock",
                "secondary_topics": ["economy", "tech"],
                "tags": ["코스피마감", "반도체투톱", "순환매", "코스닥", "외국인수급"]
            }
        }
    },
    "ZOEzPW5mazY": {
        "primary": "economy",
        "data": {
            "video": {
                "id": "ZOEzPW5mazY",
                "title": "금리를 누르려고 미국이 이미 손대기 시작한 게 있습니다. 미국의 깡패같은 반칙을 하한번 정리해 봤습니다",
                "published": "2026-08-18T11:00:59+00:00",
                "channel_name": "이효석아카데미",
                "url": "https://www.youtube.com/watch?v=ZOEzPW5mazY",
                "thumbnail": "https://img.youtube.com/vi/ZOEzPW5mazY/hqdefault.jpg"
            },
            "analysis": {
                "summary": "미국 재무부가 막대한 국채 이자 부담을 피하고 장기 국채금리 폭등을 억제하기 위해 <span class=\"text-amber-300 font-bold\">단기 국채(T-bill) 과다 발행과 국채 바이백(Buyback)</span> 등 변칙적인 유동성 조작 기법(금융 억압)을 동원하고 있는 실태를 파헤침. 연준의 양적긴축(QT) 효과를 재무부가 사실상 무력화하며 시중 유동성을 억지로 지탱하고 있음.",
                "key_claims": [
                    "재무부는 장기채 대신 단기 국채 비중을 역사적 상한선(20%)을 훨씬 초과해 발행함으로써 장기 금리 상승을 인위적으로 억누름.",
                    "역레포(RRP) 자금을 시장으로 유인해 국채를 인수하게 만드는 '스텔스 양적완화(Stealth QE)'를 실행 중임.",
                    "이러한 반칙성 정책은 단기적으로 시장 충격을 막지만, 향후 인플레이션 재점화 및 달러 패권에 대한 잠재적 신뢰 저하를 초래할 수 있음."
                ],
                "data_points": [
                    "미국 국채 발행 중 단기채(T-bills) 비중 22~25% 상회",
                    "연준 역레포 잔액 2조 달러에서 수천억 달러대로 급감(유동성 시장 방출)"
                ],
                "signal": "neutral",
                "signal_reason": "단기적으로는 증시 유동성을 지탱하는 호재이나, 중장기적으로 인플레이션 및 재정 건전성 악화 리스크가 누적됨.",
                "key_companies": [],
                "insight": "미국 정부는 공식적인 금리 인하 전이라도 재무부의 부채관리 기술을 총동원해 시장 금리를 통제하고 자산 시장을 방어하는 정치경제학적 플레이를 펼치고 있음.",
                "action_point": "미 재무부의 분기별 국채 발행 계획(QRA)과 T-bill 비중 발표를 핵심 매크로 지표로 상시 추적해야 함."
            },
            "classification": {
                "primary_topic": "economy",
                "secondary_topics": ["stock"],
                "tags": ["미국재무부", "단기국채발행", "금융억압", "역레포", "스텔스QE"]
            }
        }
    },
    "Zj-eQirPEAU": {
        "primary": "crypto",
        "data": {
            "video": {
                "id": "Zj-eQirPEAU",
                "title": "토큰화 시장 350억 달러 성장…실제 자금은 누가 사고 있나 | 김동환, 조동현 언디파인드랩스 대표 [크립토 PLUS]",
                "published": "2026-08-18T03:21:25+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=Zj-eQirPEAU",
                "thumbnail": "https://img.youtube.com/vi/Zj-eQirPEAU/hqdefault.jpg"
            },
            "analysis": {
                "summary": "블록체인 기반의 <span class=\"text-cyan-300 font-semibold\">실물자산 토큰화(RWA, Real World Assets)</span> 시장 규모가 350억 달러를 돌파하며 가파른 성장세를 보임. 블랙록의 BUIDL 펀드와 프랭클린 템플턴 등 글로벌 메이저 자산운용사들이 미국 국채와 머니마켓펀드(MMF)를 온체인 토큰화하여 가상자산 헤지펀드 및 디파이(DeFi) 프로토콜의 담보 자산으로 공급하는 실질적 자금 흐름을 분석함.",
                "key_claims": [
                    "RWA 시장 성장의 핵심 동력은 가상자산 생태계 내부의 안정적인 무위험 미국 국채 이자 수익(연 5% 수준) 수요임.",
                    "블랙록, 프랭클린 템플턴 등 제도권 공룡들의 진입으로 온체인 토큰화 증권의 결제 인프라 표준화가 급진전.",
                    "스테이블코인을 넘어 전통 채권, 부동산, 사모펀드로 RWA 적용 대상이 급격히 확장되는 중."
                ],
                "data_points": [
                    "글로벌 온체인 RWA 시장 규모 350억 달러 돌파",
                    "블랙록 BUIDL 펀드 설정액 5억 달러 초고속 돌파 및 이더리움 기반 결제 점유율 확대"
                ],
                "signal": "bullish",
                "signal_reason": "전통 금융 자본의 블록체인 인프라 채택이 본격화되면서 크립토 생태계의 실질적 펀더멘털과 수수료 수익 모델이 강화됨.",
                "key_companies": ["블랙록(BLK)", "이더리움(ETH)", "체인링크(LINK)"],
                "insight": "토큰화(RWA)는 단순한 테마가 아니라 24시간 실시간 결제와 글로벌 자본 접근성을 무기로 전통 자본시장의 백오피스를 대체하는 금융 인프라 혁명임.",
                "action_point": "RWA 결제 인프라의 표준 플랫폼인 이더리움 및 온체인 데이터 오라클 리더인 체인링크 생태계 확장에 주목할 것."
            },
            "classification": {
                "primary_topic": "crypto",
                "secondary_topics": ["tech", "stock"],
                "tags": ["RWA", "실물자산토큰화", "블랙록BUIDL", "미국국채토큰", "디파이"]
            }
        }
    },
    "_p95IhXyBAU": {
        "primary": "stock",
        "data": {
            "video": {
                "id": "_p95IhXyBAU",
                "title": "미장 복귀는 지능순? 나스닥 고점인데 지금 투자해도 될까?",
                "published": "2026-08-18T10:00:25+00:00",
                "channel_name": "수페TV",
                "url": "https://www.youtube.com/watch?v=_p95IhXyBAU",
                "thumbnail": "https://img.youtube.com/vi/_p95IhXyBAU/hqdefault.jpg"
            },
            "analysis": {
                "summary": "나스닥 지수가 역사적 신고가 부근에 위치하여 고점 부담이 커진 상황에서, 포모(FOMO)에 휩쓸려 몰빵하기보다 <span class=\"text-cyan-300 font-semibold\">목적별 ETF(QQQ, QLD, JEPQ 등)를 조합한 분할 적립 및 현금흐름 창출 전략</span>을 제시함. 나스닥100의 장기 복리 성장성과 배당 성장형 커버드콜의 방어력을 결합하는 실전 포트폴리오를 설계함.",
                "key_claims": [
                    "미국 빅테크의 독점적 이익 창출력은 여전히 유효하므로 나스닥 시장을 떠나기보다 진입 방식(적립식 분할)을 바꿔야 함.",
                    "성장 중심의 QQQ/QLD와 월배당 인컴을 창출하는 JEPQ를 믹스하여 주가 횡보 및 하락장에서도 배당 재투자를 통한 심리적 안정성 확보.",
                    "고점 매수 두려움은 일정 주기의 정액 분할 투자(DCA)를 통해 매수 단가를 평준화함으로써 극복 가능."
                ],
                "data_points": [
                    "나스닥100(QQQ) 20년간 연평균 수익률(CAGR) 13~15% 수준 기록",
                    "JEPQ 월배당 연 환산 수익률 9~10% 및 배당 성장 추이 분석"
                ],
                "signal": "bullish",
                "signal_reason": "미국 테크 기업들의 구조적 성장성에 기반한 장기 적립식 분할 투자는 여전히 가장 승률 높은 투자 전략임.",
                "key_companies": ["애플(AAPL)", "마이크로소프트(MSFT)", "엔비디아(NVDA)", "알파벳(GOOGL)"],
                "insight": "시장의 타이밍을 맞추려 하기보다 우상향하는 미국 핵심 혁신 기업 ETF를 시간과 분할 매수를 무기로 꾸준히 모아가는 것이 개인 투자자의 필승법임.",
                "action_point": "거치식 일시 매수를 지양하고 월별 분할 적립식 매수 및 월배당 ETF를 활용한 배당 재투자 루틴을 구축할 것."
            },
            "classification": {
                "primary_topic": "stock",
                "secondary_topics": ["economy"],
                "tags": ["나스닥투자", "미국ETF", "QQQ", "JEPQ", "분할적립식"]
            }
        }
    }
}

for vid, item in batch4_data.items():
    primary = item["primary"]
    out_dir = Path(f"data/analyzed/{primary}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{vid}.json"
    with open(out_file, "w", encoding="utf-8") as fp:
        json.dump(item["data"], fp, ensure_ascii=False, indent=2)
    
    pending_file = Path(f"data/pending/{vid}.json")
    if pending_file.exists():
        pending_file.unlink()
    print(f"[Batch 4 완료] {vid} -> data/analyzed/{primary}/{vid}.json")
