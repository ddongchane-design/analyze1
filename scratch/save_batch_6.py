import json
import os
from pathlib import Path

batch6_data = {
    "oZf7-Es6xGI": {
        "primary": "tech",
        "data": {
            "video": {
                "id": "oZf7-Es6xGI",
                "title": "[지식뉴스] \"메모리 반도체, 이제 미 30년물 금리를 보면 답 나옵니다\"…주식은 오히려 후행지표! 지금 삼성·하이닉스를 보는 법 / 교양이를 부탁해",
                "published": "2026-08-18T13:19:08+00:00",
                "channel_name": "교양이를 부탁해",
                "url": "https://www.youtube.com/watch?v=oZf7-Es6xGI",
                "thumbnail": "https://img.youtube.com/vi/oZf7-Es6xGI/hqdefault.jpg"
            },
            "analysis": {
                "summary": "메모리 반도체 사이클의 진정한 선행지표는 주가가 아니라 <span class=\"text-cyan-300 font-semibold\">빅테크 기업들의 30년물 초장기 회사채 발행 금리와 수요</span>임. 구글, 아마존, MS 등 하이퍼스케일러들이 장기 회사채를 원활히 조달하여 데이터센터 및 HBM 주문을 집행할 수 있는지가 반도체 수급과 기업가치를 결정하는 본질적 메커니즘을 규명함.",
                "key_claims": [
                    "빅테크의 AI CapEx 자금 조달 창구인 초장기 회사채 시장의 수급이 반도체 주문의 가장 정확한 선행 지표임.",
                    "구글이 6%대 초고금리에도 30년물 회사채를 성공적으로 완판한 것은 향후 10~20년간 AI 인프라 투자 회수율에 대한 시장 신뢰가 확고함을 증명.",
                    "삼성전자와 SK하이닉스의 주가는 단기 수급보다 이러한 빅테크 장기 파이낸싱 흐름에 후행하여 동행함."
                ],
                "data_points": [
                    "구글(알파벳) 30년물 회사채 6.3% 발행 및 목표 조달액 초과 달성",
                    "하이퍼스케일러 연간 CapEx 규모 2,000억 달러 돌파 및 메모리 비중 확대"
                ],
                "signal": "bullish",
                "signal_reason": "빅테크의 장기 채권 조달 성공은 AI 인프라 투자 및 HBM/서버 DRAM 수요가 수년간 꺾이지 않을 것임을 확증함.",
                "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "알파벳(GOOGL)", "마이크로소프트(MSFT)"],
                "insight": "반도체 투자는 단기 주가 차트가 아니라, 빅테크가 채권 시장에서 조달한 실탄이 데이터센터와 HBM 칩 주문으로 흘러들어가는 자금줄을 추적하는 것이 핵심임.",
                "action_point": "빅테크 기업들의 회사채 발행 스프레드와 분기별 실적 발표 내 CapEx 가이던스를 연동하여 반도체 비중을 관리할 것."
            },
            "classification": {
                "primary_topic": "tech",
                "secondary_topics": ["economy", "stock"],
                "tags": ["메모리반도체", "30년물회사채", "빅테크CapEx", "SK하이닉스", "삼성전자"]
            }
        }
    },
    "qUWh38JbLbc": {
        "primary": "economy",
        "data": {
            "video": {
                "id": "qUWh38JbLbc",
                "title": "이자만 국방비보다 많다? 미국 덮친 40조 달러 빚 #교양이를부탁해 #엔화 #미국국채 #베센트 #미국부채",
                "published": "2026-08-18T11:30:07+00:00",
                "channel_name": "교양이를 부탁해",
                "url": "https://www.youtube.com/watch?v=qUWh38JbLbc",
                "thumbnail": "https://img.youtube.com/vi/qUWh38JbLbc/hqdefault.jpg"
            },
            "analysis": {
                "summary": "미국 국가부채가 40조 달러를 돌파하며 <span class=\"text-rose-400 font-medium\">연간 국채 이자 지급액만 1조 달러를 넘어 사상 최초로 국방비 예산을 추월</span>한 충격적인 재정 현실을 고발함. 고금리가 지속될수록 눈덩이처럼 불어나는 이자 부담이 미국 정부의 정책 운신 폭을 좁히고 장기 국채금리의 상방을 압박하고 있음.",
                "key_claims": [
                    "미국 정부의 순이자 지출이 1조 달러를 돌파하여 국방비 및 메디케어 지출을 초과함.",
                    "부채 이자를 갚기 위해 신규 국채를 더 발행해야 하는 악순환(부채의 폰지화) 구조에 진입.",
                    "결국 미국은 성장을 통해 GDP를 키우거나(AI 생산성) 인플레이션으로 빚을 녹여내는 방법 외에 선택지가 없음."
                ],
                "data_points": [
                    "미국 연방정부 총부채 35조~40조 달러 도달",
                    "연간 국채 이자 지급액 1.1조 달러(미국 국방 예산 약 8,500억 달러 초과)"
                ],
                "signal": "bearish",
                "signal_reason": "미국 재정 적자 심화와 국채 발행 과다는 장기 국채금리의 구조적 고공행진과 달러화 신뢰도에 장기적 하방 압력으로 작용함.",
                "key_companies": [],
                "insight": "미국의 이자 비용 폭증은 연준이 금리를 영구히 높게 유지하기 어렵게 만들며, 장기적으로 통화 가치 하락과 실물 자산 선호로 이어질 수밖에 없음.",
                "action_point": "미국 재정 적자 추이와 국채 발행 동향을 모니터링하며 금, 비트코인 등 통화 가치 하락 헤지 자산의 분산 배치를 검토."
            },
            "classification": {
                "primary_topic": "economy",
                "secondary_topics": ["stock"],
                "tags": ["미국부채", "국채이자지출", "국방비초과", "재정적자", "국채금리"]
            }
        }
    },
    "qeg4M8uNJ5E": {
        "primary": "tech",
        "data": {
            "video": {
                "id": "qeg4M8uNJ5E",
                "title": "[문지웅의 빅머니 LIVE] 2분기 낸드 매출 77% 증가 | 2027~2028년 HBM 수요 폭발 | 10년물 금리 5% 돌파할까 촉각",
                "published": "2026-08-18T21:58:31+00:00",
                "channel_name": "매경월가월부",
                "url": "https://www.youtube.com/watch?v=qeg4M8uNJ5E",
                "thumbnail": "https://img.youtube.com/vi/qeg4M8uNJ5E/hqdefault.jpg"
            },
            "analysis": {
                "summary": "AI 서버향 엔터프라이즈 eSSD 수요 폭발로 <span class=\"text-cyan-300 font-semibold\">2분기 글로벌 낸드(NAND) 매출이 전년 대비 77% 급증</span>한 가운데, 2027~2028년 HBM 수요가 차세대 AI 가속기와 맞물려 폭발적 팽창세를 보일 것으로 전망됨. 미국 10년물 국채금리의 5% 돌파 여부가 시장의 단기 밸류에이션 변수로 떠오름.",
                "key_claims": [
                    "DRAM에 이어 NAND 플래시 역시 eSSD 중심의 공급 부족 및 판가 급등으로 실적 서프라이즈 견인.",
                    "HBM 수요는 2026년에 그치지 않고 엔비디아 루빈(Rubin) 및 차세대 아키텍처 출시와 함께 2028년까지 구조적 쇼티지 지속.",
                    "미 10년물 국채금리 5% 돌파 시 단기 기술주 멀티플 조정 가능성 있으나 실적 펀더멘털이 하락을 방어할 것임."
                ],
                "data_points": [
                    "글로벌 NAND 매출 전년 대비 77% 급증 및 eSSD 마진율 대폭 개선",
                    "미 10년물 국채수익률 4.5% 상회 및 5.0% 터치 경계감 형성"
                ],
                "signal": "bullish",
                "signal_reason": "DRAM과 NAND의 동반 수급 개선과 HBM 2028년 장기 계약 확정이 메모리 반도체 업계의 역대급 실적 지속성을 뒷받침함.",
                "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "웨스턴디지털(WDC)", "마이크론(MU)"],
                "insight": "AI 인프라는 초고속 연산을 위한 HBM과 대용량 데이터 저장을 위한 초고용량 eSSD를 동시에 요구하며 메모리 반도체 전체를 호황기로 이끌고 있음.",
                "action_point": "낸드 턴어라운드 수혜가 더해진 종합 메모리 반도체 및 고용량 SSD 컨트롤러 밸류체인에 대한 비중 확대."
            },
            "classification": {
                "primary_topic": "tech",
                "secondary_topics": ["stock", "economy"],
                "tags": ["NAND매출급증", "eSSD", "HBM수요폭발", "SK하이닉스", "국채금리5%"]
            }
        }
    },
    "rnSUBEpzcGw": {
        "primary": "etc",
        "data": {
            "video": {
                "id": "rnSUBEpzcGw",
                "title": "날씨를 조종해서 무기로 쓴다?!",
                "published": "2026-08-18T03:00:10+00:00",
                "channel_name": "안될과학 Unrealscience",
                "url": "https://www.youtube.com/watch?v=rnSUBEpzcGw",
                "thumbnail": "https://img.youtube.com/vi/rnSUBEpzcGw/hqdefault.jpg"
            },
            "analysis": {
                "summary": "요오드화은을 살포하는 인공강우 및 구름 씨뿌리기(Cloud Seeding)에서 출발하여, 베트남전 당시의 '뽀빠이 작전' 등 <span class=\"text-amber-300 font-bold\">기상 조작 기술(Weather Modification)의 역사와 군사적 활용 실태</span>를 과학적으로 분석함. 유엔의 환경개조기술금지협약(ENMOD) 등 국제 규제와 현대 기상 제어의 과학적 한계를 규명함.",
                "key_claims": [
                    "구름 씨뿌리기를 통한 국지적 강우 유도는 과학적으로 입증되었으나, 초대형 태풍이나 가뭄을 인위적으로 조작하는 것은 에너지 규모상 불가능에 가까움.",
                    "과거 군사적 기상 무기화 시도 이후 국제 협약으로 기상 환경의 무기 사용이 엄격히 금지됨."
                ],
                "data_points": [
                    "베트남전 미군의 뽀빠이 작전(몬순 강우 연장 작전) 사례",
                    "1978년 발효된 유엔 환경개조기술금지협약(ENMOD)"
                ],
                "signal": "neutral",
                "signal_reason": "대기 과학 및 역사 교양 콘텐츠로 금융 투자 시그널과는 중립적임.",
                "key_companies": [],
                "insight": "기상 제어 기술은 군사 무기보다는 인공강우, 안개 소산, 가뭄 완화 등 농업 및 공공 안전 목적으로 발전하고 있음.",
                "action_point": "가뭄 방재 및 인공강우, 대기 환경 정화 기술에 대한 상식적 참고."
            },
            "classification": {
                "primary_topic": "etc",
                "secondary_topics": [],
                "tags": ["기상조작", "인공강우", "뽀빠이작전", "ENMOD", "대기과학"]
            }
        }
    },
    "sN0xErOlBxo": {
        "primary": "stock",
        "data": {
            "video": {
                "id": "sN0xErOlBxo",
                "title": "고금리에 AI반도체주 하락..미국증시 약세 | 데일리 라이브 | 2026.8.19(수)",
                "published": "2026-08-18T23:07:58+00:00",
                "channel_name": "Smart Money by MiraeAsset ",
                "url": "https://www.youtube.com/watch?v=sN0xErOlBxo",
                "thumbnail": "https://img.youtube.com/vi/sN0xErOlBxo/hqdefault.jpg"
            },
            "analysis": {
                "summary": "미국 장기 국채금리가 연일 상승세를 이어가며 밸류에이션 부담이 누적된 엔비디아, 마이크론, 브로드컴 등 <span class=\"text-cyan-300 font-semibold\">AI 반도체 기술주가 일제히 조정을 받으며 미국 증시 약세 마감</span>함. 7월 FOMC 의사록 공개를 앞두고 연준의 매파적 스탠스 지속 경계감이 위험 자산 선호 심리를 제한함.",
                "key_claims": [
                    "10년물 국채금리 4.5% 안착과 유가 반등이 맞물려 기술주 중심의 차익 매물 출회를 자극.",
                    "필라델피아 반도체 지수가 단기 급등 후 기술적 저항선에 부딪히며 숨고르기 국면에 진입.",
                    "실적 발표를 앞둔 빅테크들의 눈높이 검증 과정이 진행 중이나, 구조적 AI 성장 추세는 유지됨."
                ],
                "data_points": [
                    "필라델피아 반도체 지수(SOX) -2.1% 하락 마감",
                    "엔비디아 -2.3%, 마이크론 -4.8%, AMD -4.2% 하락 기록"
                ],
                "signal": "neutral",
                "signal_reason": "대세 하락 전환이 아닌 국채금리 상승에 따른 고PER 주식들의 단기 기술적 기간 조정임.",
                "key_companies": ["엔비디아(NVDA)", "마이크론(MU)", "AMD(AMD)", "브로드컴(AVGO)"],
                "insight": "금리 상승기에는 기술주가 단기 변동성을 겪지만, 실적 시즌이 본격화되면 실제 이익을 증명하는 반도체 주도주 중심으로 빠르게 반등이 전개됨.",
                "action_point": "반도체 레버리지 상품 비중을 축소하고, 금리 고점 확인 시점까지 주도 반도체 종목에 대한 분할 매수 대기."
            },
            "classification": {
                "primary_topic": "stock",
                "secondary_topics": ["tech", "economy"],
                "tags": ["미국증시", "AI반도체하락", "필라델피아반도체", "FOMC경계감", "국채금리"]
            }
        }
    },
    "sarhEmTgbIE": {
        "primary": "stock",
        "data": {
            "video": {
                "id": "sarhEmTgbIE",
                "title": "[26.08.18 오전 방송 전체보기] 다시 돌아온 삼전닉스에도 FOMC 의사록·중동전쟁이 변수...극복할 수 있을까?",
                "published": "2026-08-18T03:16:30+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=sarhEmTgbIE",
                "thumbnail": "https://img.youtube.com/vi/sarhEmTgbIE/hqdefault.jpg"
            },
            "analysis": {
                "summary": "삼성전자와 SK하이닉스 투톱이 저점에서 반등하며 지수 견인을 시도하고 있으나, <span class=\"text-amber-300 font-bold\">7월 FOMC 의사록 발표와 중동 지정학적 위기 고조</span>가 국내 증시의 추가 상승 탄력을 제약하고 있음. 환율 상승 압력과 외국인 수급 변동성을 점검하며 매크로 변수 극복 가능성을 다각도로 진단함.",
                "key_claims": [
                    "국내 반도체 대장주의 실적 개선세는 뚜렷하나 환율과 유가 등 거시 환경이 수급 확장을 제약함.",
                    "FOMC 의사록에서 금리 인하 경로에 대한 매파적 언급이 확인될 경우 단기 변동성 확대 불가피.",
                    "중동 리스크로 인한 원자재 가격 불안은 조선, 방산, 에너지 등 대체 섹터로의 수급 분산을 유도."
                ],
                "data_points": [
                    "코스피 2,700선 공방 및 원/달러 환율 1,385원선 상회",
                    "외국인 국내 주식 현물 소폭 순매수 대비 선물 시장 대규모 변동성 연출"
                ],
                "signal": "neutral",
                "signal_reason": "반도체 펀더멘털은 양호하나 매크로 및 지정학적 불확실성이 상단을 막고 있어 박스권 횡보 가능성이 높음.",
                "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "한화에어로스페이스(012450)"],
                "insight": "글로벌 매크로 변수가 혼재된 구간에서는 지수 베팅보다 매크로 무풍지대에 위치한 고수익 수출 주도주에 집중하는 포트폴리오 압축이 필수적임.",
                "action_point": "FOMC 의사록 결과와 환율 안정세를 확인하며 반도체 및 방산 실적 대형주에 대한 비중 분할 유지."
            },
            "classification": {
                "primary_topic": "stock",
                "secondary_topics": ["economy", "tech"],
                "tags": ["삼전닉스", "FOMC의사록", "중동전쟁", "원달러환율", "코스피전망"]
            }
        }
    }
}

for vid, item in batch6_data.items():
    primary = item["primary"]
    out_dir = Path(f"data/analyzed/{primary}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{vid}.json"
    with open(out_file, "w", encoding="utf-8") as fp:
        json.dump(item["data"], fp, ensure_ascii=False, indent=2)
    
    pending_file = Path(f"data/pending/{vid}.json")
    if pending_file.exists():
        pending_file.unlink()
    print(f"[Batch 6 완료] {vid} -> data/analyzed/{primary}/{vid}.json")
