import json
import os
from pathlib import Path

batch1_data = {
    "0q2xi2-19_o": {
        "primary": "etc",
        "data": {
            "video": {
                "id": "0q2xi2-19_o",
                "title": "피를 주입했더니 회춘이 된다고?!",
                "published": "2026-08-18T09:00:15+00:00",
                "channel_name": "안될과학 Unrealscience",
                "url": "https://www.youtube.com/watch?v=0q2xi2-19_o",
                "thumbnail": "https://img.youtube.com/vi/0q2xi2-19_o/hqdefault.jpg"
            },
            "analysis": {
                "summary": "젊은 쥐와 늙은 쥐의 혈관을 외과적으로 연결하는 <span class=\"text-cyan-300 font-semibold\">병체결합(Parabiosis)</span> 실험을 통해 젊은 피의 특정 인자가 늙은 개체의 뇌신경 세포 및 장기 기능을 회복시키는 항노화 메커니즘을 규명함. 과거의 무분별한 수혈 위험성을 극복하고 혈장 내 유효 단백질(GDF11, 클로토 등) 및 희석 기전을 활용한 정밀 <span class=\"text-amber-300 font-bold\">역노화 바이오 치료제</span> 연구가 가속화되고 있음.",
                "key_claims": [
                    "병체결합 실험 결과, 젊은 혈액 성분 유입 시 신경 재생 및 인지 기능 개선이 실제로 관찰됨.",
                    "단순 전혈 주입은 거부 반응 및 심혈관 부작용이 크므로 혈장 내 특정 <span class=\"text-cyan-300 font-semibold\">회춘 인자 단백질</span>을 선별 추출하거나 노화 혈장을 정화하는 기술이 핵심임.",
                    "글로벌 바이오 기업 및 빅테크 펀딩이 집중되며 단순 수명 연장을 넘어 건강수명(Healthspan) 극대화 산업으로 진화 중임."
                ],
                "data_points": [
                    "1950년대 클라이브 맥케이 교수의 초기 파라바이오시스 실험부터 2010년대 스탠퍼드 토니 위스-코레이 교수의 뇌 인지기능 회복 연구까지 70년 연구사",
                    "노화 혈장 교체 치료(TPE) 임상 및 알츠하이머 대상 바이오마커 개선 지표 확인"
                ],
                "signal": "neutral",
                "signal_reason": "장기적 헬스케어 혁신 테마이나 아직 초기 임상 및 규제 검증 단계로 즉각적인 상용화 수익화에는 시간이 소요됨.",
                "key_companies": ["알카헤스트(Alkahest)", "유스바이오"],
                "insight": "노화 정복 연구는 비과학적 민간요법에서 분자생물학적 혈액 프로테오믹스(단백질체학) 및 세포 리프로그래밍 치료 분야로 패러다임이 전환되고 있음.",
                "action_point": "항노화 및 알츠하이머 표적 단백질 치료제를 개발하는 바이오테크 및 헬스케어 플랫폼 파이프라인의 장기 임상 데이터에 주목할 필요가 있음."
            },
            "classification": {
                "primary_topic": "etc",
                "secondary_topics": ["tech"],
                "tags": ["항노화", "역노화", "바이오테크", "파라바이오시스", "혈장치료"]
            }
        }
    },
    "0z_ELrowFmw": {
        "primary": "robot",
        "data": {
            "video": {
                "id": "0z_ELrowFmw",
                "title": "\"산업 초강대국 독일도 일본도 두손 두발 다 들었다\"…로봇 패권이 현대차 밸류체인으로 넘어가는 진짜 이유 | 정지훈 박사 [2부]",
                "published": "2026-08-18T23:00:07+00:00",
                "channel_name": "이효석아카데미",
                "url": "https://www.youtube.com/watch?v=0z_ELrowFmw",
                "thumbnail": "https://img.youtube.com/vi/0z_ELrowFmw/hqdefault.jpg"
            },
            "analysis": {
                "summary": "글로벌 제조 강국인 독일과 일본이 소프트웨어와 피지컬 AI 융합에서 뒤처지면서, <span class=\"text-cyan-300 font-semibold\">보스턴 다이내믹스</span>를 보유하고 대량 양산 및 부품 밸류체인을 완비한 <span class=\"text-cyan-300 font-semibold\">현대차그룹</span>이 차세대 휴머노이드 로봇 패권의 핵심 축으로 부상하고 있음. 로봇 생태계는 정밀 하드웨어 제조력과 AI 파운데이션 모델, 실시간 제어 소프트웨어의 수직 계열화가 승패를 결정짓는 국면으로 진입함.",
                "key_claims": [
                    "독일·일본의 전통 정밀기계 산업은 뛰어난 하드웨어를 보유했으나 AI 소프트웨어 및 시뮬레이션 기반 학습 역량 결여로 피지컬 AI 전환에 한계 봉착.",
                    "<span class=\"text-cyan-300 font-semibold\">현대차그룹</span>은 보스턴 다이내믹스의 로보틱스 원천기술과 현대모비스, 현대위아, 현대오토에버 등 완성도 높은 제조·양산 공급망을 동시에 쥐고 있음.",
                    "테슬라 옵티머스와 함께 실제 생산 공장에 투입되어 피지컬 데이터를 흡수할 수 있는 유일한 글로벌 제조사 진영임."
                ],
                "data_points": [
                    "보스턴 다이내믹스 아틀라스(전동식)의 완전 자율 작업 전환 테스트 진행",
                    "현대차 싱가포르 글로벌 혁신센터(HMGICS) 및 현대차 완성차 공장 내 로봇 실증 배치 확대"
                ],
                "signal": "bullish",
                "signal_reason": "로봇 하드웨어의 대량 양산 경쟁력과 피지컬 AI 실데이터 수집 능력을 동시에 갖춘 현대차 밸류체인의 구조적 재평가 가능성이 높음.",
                "key_companies": ["현대차(005380)", "현대모비스(012330)", "현대오토에버(307950)", "테슬라(TSLA)"],
                "insight": "피지컬 AI 시대의 최종 승자는 단순 AI 모델 개발사가 아니라, 로봇을 수만 대 단위로 균일하게 찍어내고 실제 공장에서 발생하는 물리적 인터랙션 데이터를 실시간 학습시킬 수 있는 완성차 기반 밸류체인임.",
                "action_point": "보스턴 다이내믹스의 상용화 일정 및 현대차 그룹 내 로봇 부품(액추에이터, 감속기, 전장제어 SW) 공급사들의 가치 재평가에 주목할 필요가 있음."
            },
            "classification": {
                "primary_topic": "robot",
                "secondary_topics": ["tech", "stock"],
                "tags": ["현대차", "보스턴다이내믹스", "피지컬AI", "휴머노이드", "현대모비스"]
            }
        }
    },
    "4gTGeMwtV6Q": {
        "primary": "tech",
        "data": {
            "video": {
                "id": "4gTGeMwtV6Q",
                "title": "아마존이 20년 전에 짜놓은 설계도 하나가, 지금 AI 투자 지도를 그대로 다시 그리고 있었습니다 | 정지훈 박사 [1부]",
                "published": "2026-08-18T22:00:34+00:00",
                "channel_name": "이효석아카데미",
                "url": "https://www.youtube.com/watch?v=4gTGeMwtV6Q",
                "thumbnail": "https://img.youtube.com/vi/4gTGeMwtV6Q/hqdefault.jpg"
            },
            "analysis": {
                "summary": "2000년대 초반 제프 베조스가 주창한 서비스 지향 아키텍처(SOA)와 API 기반 모듈화 설계가 현재 <span class=\"text-cyan-300 font-semibold\">AWS 클라우드</span>와 AI 에이전트 인프라 생태계의 표준으로 작용하고 있음. 인프라에서 시작해 모델(파운데이션), 애플리케이션 플랫폼(베드록)으로 이어지는 계층별 인터페이스 통제력이 빅테크 간 <span class=\"text-amber-300 font-bold\">AI 플랫폼 패권</span>을 결정하고 있음.",
                "key_claims": [
                    "아마존의 내부 시스템 모듈화 선언(API 강제화)이 클라우드 혁명을 낳았듯, AI 역시 복잡한 파운데이션 모델을 API 레고 블록처럼 연결하는 에이전트 아키텍처로 진화함.",
                    "단일 초거대 모델 개발 경쟁을 넘어 고객이 다양한 모델(앤트로픽, 메타, 독자 모델)을 결합해 파이프라인을 구축할 수 있게 돕는 플랫폼 사업자가 진정한 락인(Lock-in)을 형성함.",
                    "하드웨어 칩(트레이니엄/인퍼런시아)부터 클라우드 데이터센터, 에이전트 프레임워크까지 완결형 밸류체인을 구축한 기업이 장기 생존할 것임."
                ],
                "data_points": [
                    "아마존 베드록(Bedrock) 내 멀티모델 채택률 급증 및 앤트로픽 파트너십 투자 확대",
                    "AWS 클라우드 인프라 기반 자체 AI 가속기(Trainium2) 도입 비중 확대"
                ],
                "signal": "bullish",
                "signal_reason": "클라우드 락인 효과와 독자 AI 칩 및 모듈형 플랫폼을 바탕으로 한 빅테크의 현금 창출력과 인프라 장악력이 지속적으로 강화됨.",
                "key_companies": ["아마존(AMZN)", "엔비디아(NVDA)", "마이크로소프트(MSFT)", "알파벳(GOOGL)"],
                "insight": "AI 투자의 핵심은 어떤 단일 모델이 최고 성능을 내는가가 아니라, 엔터프라이즈 기업들이 데이터와 업무를 맡길 수 있는 안전하고 유연한 '모듈형 인프라 플랫폼'을 누가 쥐고 있는가임.",
                "action_point": "빅테크 클라우드 3사의 자체 AI 가속기 침투율과 B2B 에이전트 워크플로우 플랫폼 수익화 지표를 모니터링해야 함."
            },
            "classification": {
                "primary_topic": "tech",
                "secondary_topics": ["economy", "stock"],
                "tags": ["아마존", "AWS", "AI플랫폼", "베드록", "모듈화아키텍처"]
            }
        }
    },
    "5EL1HIZ3e10": {
        "primary": "etc",
        "data": {
            "video": {
                "id": "5EL1HIZ3e10",
                "title": "조선식 지진 측정법, 노벨상 받아도 됨",
                "published": "2026-08-18T14:15:08+00:00",
                "channel_name": "언더스탠딩_Understanding",
                "url": "https://www.youtube.com/watch?v=5EL1HIZ3e10",
                "thumbnail": "https://img.youtube.com/vi/5EL1HIZ3e10/hqdefault.jpg"
            },
            "analysis": {
                "summary": "조선왕조실록과 승정원일기 등 역사 기록에 남겨진 정밀한 <span class=\"text-amber-300 font-bold\">지진 관측 및 기술 방식</span>이 현대 지진학 및 계측 표준과 놀라울 정도로 부합함을 조명함. 사기그릇 물결, 처마 흔들림, 가옥 파손 정도 등 물리적 현상을 계급화하여 기록한 조선의 체계적 데이터 측정 역량을 재평가함.",
                "key_claims": [
                    "조선시대 지진 기록은 진도와 규모를 정밀하게 추정할 수 있는 정량적 묘사를 체계적으로 갖추고 있음.",
                    "현대 계측기가 없던 시절에도 다각적인 물리 지표를 관찰하여 국가적 재난 대응 및 역사 데이터베이스를 구축함."
                ],
                "data_points": [
                    "조선왕조실록 내 지진 관련 상세 기록 수천 건 보유",
                    "현대 지진학자들의 한반도 역사 지진 진도 맵핑 연구 활용"
                ],
                "signal": "neutral",
                "signal_reason": "역사 과학 및 교양 콘텐츠로 시장 투자 시그널과는 중립적임.",
                "key_companies": [],
                "insight": "정밀한 데이터 축적과 관측 체계는 과학적 분석과 국가 시스템 안정성의 기초 토대임을 보여줌.",
                "action_point": "한반도 지진 데이터 및 방재 인프라 고도화 관련 공공 안전 기술에 대한 상식적 참고."
            },
            "classification": {
                "primary_topic": "etc",
                "secondary_topics": [],
                "tags": ["역사과학", "지진관측", "조선왕조실록", "기록문화"]
            }
        }
    },
    "5_UnOxyJZzY": {
        "primary": "economy",
        "data": {
            "video": {
                "id": "5_UnOxyJZzY",
                "title": "삼전닉스도 S&P500도 실적 서프라이즈...매크로 공포에도 증시가 버티는 이유ㅣ홍선애, 김한진 삼프로TV 이코노미스트 [여의도 인사이트]",
                "published": "2026-08-18T09:04:52+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=5_UnOxyJZzY",
                "thumbnail": "https://img.youtube.com/vi/5_UnOxyJZzY/hqdefault.jpg"
            },
            "analysis": {
                "summary": "미국 장기 국채금리 급등과 지정학적 불안이라는 매크로 역풍 속에서도 <span class=\"text-cyan-300 font-semibold\">빅테크 및 반도체 기업들의 강력한 실적 서프라이즈</span>가 증시 하단을 탄탄하게 지지하고 있음. 금리 상승으로 인한 밸류에이션 부담과 AI CapEx 투자 회수율에 대한 시장의 줄다리기가 팽팽하지만, 알파벳의 대규모 장기 회사채 흥행 등 기업들의 실질적 자금 동원력과 AI 투자 집행 의지는 여전히 견고함.",
                "key_claims": [
                    "미 10년물 국채금리가 4.5%를 웃도는 고금리 환경에서도 S&P500 기업 이익 성장률이 예상치를 상회하며 시장을 견인.",
                    "구글의 30년물 6.3% 회사채 발행에 막대한 수요가 몰렸듯, 초우량 빅테크의 AI 인프라 투자 의지는 고금리 충격을 흡수 중.",
                    "단기적으로 금리 피로도가 누적될 수 있으나, AI 생산성 혁신이 본격화되는 한 시장 붕괴보다는 건전한 섹터 순환매 양상이 이어질 것임."
                ],
                "data_points": [
                    "미국 10년물 국채수익률 4.5~5.0% 근접 및 채권시장 변동성 확대",
                    "빅테크 2분기 어닝 서프라이즈 비율 80% 상회 및 AI 관련 자본지출(CapEx) 가이던스 상향"
                ],
                "signal": "bullish",
                "signal_reason": "매크로 고금리 압박보다 기업들의 압도적인 이익 펀더멘털과 AI 인프라 투자 지속성이 증시의 장기 상승 동력을 뒷받침함.",
                "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "알파벳(GOOGL)", "마이크로소프트(MSFT)"],
                "insight": "고금리는 부실 기업을 솎아내고 현금 창출력이 압도적인 빅테크 및 메모리 반도체 독점 기업들로의 자금 쏠림을 더욱 가속화시키는 거름망 역할을 하고 있음.",
                "action_point": "매크로 금리 노이즈로 인한 일시적 조정 시 고수익성과 독점적 공급력을 갖춘 반도체 및 AI 주도주를 분할 매수하는 전략이 유효함."
            },
            "classification": {
                "primary_topic": "economy",
                "secondary_topics": ["stock", "tech"],
                "tags": ["매크로", "미국국채금리", "실적서프라이즈", "반도체", "AICapEx"]
            }
        }
    },
    "6TKmlsKCBh8": {
        "primary": "economy",
        "data": {
            "video": {
                "id": "6TKmlsKCBh8",
                "title": "\"부자를 더 만들어라\" 미국이 AI를 키우는 이유 #교양이를부탁해 #엔화 #미국국채 #베센트 #미국부채",
                "published": "2026-08-18T12:00:34+00:00",
                "channel_name": "교양이를 부탁해",
                "url": "https://www.youtube.com/watch?v=6TKmlsKCBh8",
                "thumbnail": "https://img.youtube.com/vi/6TKmlsKCBh8/hqdefault.jpg"
            },
            "analysis": {
                "summary": "미국의 막대한 국가부채와 국채 이자 부담을 해결하기 위해 미국 정부가 선택한 핵심 전략은 <span class=\"text-amber-300 font-bold\">AI 주도 경제 성장과 자산 가치 상승을 통한 세수 극대화</span>임. 엔비디아 등 빅테크 주가 상승과 신규 고소득층 창출이 미국 재정 펀더멘털을 지탱하는 본질적 원동력으로 작용함.",
                "key_claims": [
                    "정부 재정의 핵심 펀더멘털은 세금 징수 능력이며, 부채를 갚기 위해 고소득 자산가를 대거 육성해야 함.",
                    "AI 생태계 육성은 기업 가치 폭등과 자본이득세 확대로 직결되어 미국 국채 신뢰도를 유지시키는 핵심 기둥임."
                ],
                "data_points": [
                    "미국 국가부채 35조~40조 달러 돌파 국면",
                    "빅테크 중심 S&P500 시총 비중 확대 및 자본이득세 수입 비중 증가"
                ],
                "signal": "bullish",
                "signal_reason": "미국 정부의 정책적 방향이 AI 산업 성장과 주식 시장 부양을 통한 세수 확보에 맞춰져 있어 중장기 AI 정책 수혜가 지속될 것임.",
                "key_companies": ["엔비디아(NVDA)", "마이크로소프트(MSFT)"],
                "insight": "미국 국채 위기론의 해법은 긴축이 아니라 AI를 통한 생산성 폭발과 자산 버블 유도를 통한 GDP 대비 부채비율 희석 전략임.",
                "action_point": "미국 정부의 재정 전략과 이해관계를 같이하는 핵심 미국 빅테크 주도주에 대한 중장기 비중 유지가 유리함."
            },
            "classification": {
                "primary_topic": "economy",
                "secondary_topics": ["tech", "stock"],
                "tags": ["미국부채", "AI육성", "세수확대", "엔비디아", "재정정책"]
            }
        }
    }
}

for vid, item in batch1_data.items():
    primary = item["primary"]
    out_dir = Path(f"data/analyzed/{primary}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{vid}.json"
    with open(out_file, "w", encoding="utf-8") as fp:
        json.dump(item["data"], fp, ensure_ascii=False, indent=2)
    
    pending_file = Path(f"data/pending/{vid}.json")
    if pending_file.exists():
        pending_file.unlink()
    print(f"[Batch 1 완료] {vid} -> data/analyzed/{primary}/{vid}.json")
