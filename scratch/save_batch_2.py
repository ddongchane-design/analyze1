import json
import os
from pathlib import Path

batch2_data = {
    "9HqM5TWN9qc": {
        "primary": "stock",
        "data": {
            "video": {
                "id": "9HqM5TWN9qc",
                "title": "새로운 주도주를 못 찾겠다면? 다섯개 섹터로 대응하는 순환매 투자 전략ㅣ명민준, 박세미, 황유현 [주린이 구조대]",
                "published": "2026-08-18T12:30:03+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=9HqM5TWN9qc",
                "thumbnail": "https://img.youtube.com/vi/9HqM5TWN9qc/hqdefault.jpg"
            },
            "analysis": {
                "summary": "반도체 원톱 장세 이후 지수 변동성이 확대되는 구간에서 <span class=\"text-amber-300 font-bold\">5대 핵심 섹터(반도체, 조선, 방산, 전력기기, 헬스케어)</span>를 활용한 분산 및 순환매 포트폴리오 전략을 제시함. 지수 고점 부근에서는 추격 매수보다 눌림목 구간에 진입한 실적 확인 종목을 선제적으로 분할 매집하는 리밸런싱이 유효함.",
                "key_claims": [
                    "지수 상단이 제한된 박스권에서는 단일 종목 집중보다 실적 모멘텀이 살아있는 5대 핵심 섹터 간 <span class=\"text-cyan-300 font-semibold\">순환매 타이밍 매매</span>가 리스크 대비 수익률이 우수함.",
                    "조선과 방산은 글로벌 지정학 및 수주 사이클 호황이 뒷받침되며, 전력기기는 AI 데이터센터 증설에 따른 구조적 성장 지속.",
                    "단기 급등한 테마주 추격을 피하고 기관/외국인 수급이 비어있는 실적 바닥 통과 섹터를 공략해야 함."
                ],
                "data_points": [
                    "국내 증시 코스피 2,700~2,850선 박스권 등락 및 거래대금 분산 추이",
                    "조선 3사 3년치 이상 수주잔고 확보 및 전력 인프라 북미 수출 마진율 고공행진"
                ],
                "signal": "neutral",
                "signal_reason": "시장 전체의 폭발적 상승보다는 섹터별 손바뀜이 활발한 순환매 장세로 민첩한 리밸런싱 대응이 요구됨.",
                "key_companies": ["HD현대일렉트릭(267260)", "한화에어로스페이스(012450)", "HD한국조선해양(009540)", "삼성바이오로직스(207940)"],
                "insight": "순환매 장세에서는 오르는 종목을 쫓아가기보다 펀더멘털이 훼손되지 않은 주도 섹터의 단기 조정을 기회로 삼는 바벨 전략이 계좌 변동성을 낮추는 정석임.",
                "action_point": "반도체 이외에 전력기기 및 방산 등 글로벌 수주 잔고가 탄탄한 2선 주도주들의 눌림목 분할 매수 타이밍을 점검해야 함."
            },
            "classification": {
                "primary_topic": "stock",
                "secondary_topics": ["economy", "energy"],
                "tags": ["순환매", "섹터전략", "조선", "방산", "전력기기", "포트폴리오"]
            }
        }
    },
    "9QB1cb8pQIA": {
        "primary": "economy",
        "data": {
            "video": {
                "id": "9QB1cb8pQIA",
                "title": "미 국채 샀다가 파산? 실리콘밸리은행이 망한 이유 #교양이를부탁해 #엔화 #미국국채 #베센트 #미국부채",
                "published": "2026-08-18T11:15:33+00:00",
                "channel_name": "교양이를 부탁해",
                "url": "https://www.youtube.com/watch?v=9QB1cb8pQIA",
                "thumbnail": "https://img.youtube.com/vi/9QB1cb8pQIA/hqdefault.jpg"
            },
            "analysis": {
                "summary": "가장 안전한 무위험 자산으로 여겨지는 <span class=\"text-amber-300 font-bold\">미국 장기 국채</span>를 대거 매입했던 실리콘밸리은행(SVB)이 급격한 기준금리 인상으로 인한 채권 평가손실과 단기 예금 인출(뱅크런)이 맞물리며 파산에 이른 구조적 원인을 설명함. 장기 금리 상승기 금융기관의 자산-부채 만기 불일치(듀레이션 리스크)의 치명성을 경고함.",
                "key_claims": [
                    "미국 국채 자체의 부도 위험이 아니라, 금리 급등으로 인한 <span class=\"text-rose-400 font-medium\">채권 매매가격 폭락</span>이 금융기관 자본을 잠식함.",
                    "단기 예금 부채와 장기 채권 자산 간의 만기 미스매칭 관리에 실패하면 초우량 은행도 순식간에 유동성 위기에 직면함."
                ],
                "data_points": [
                    "SVB 보유 미 국채 및 MBS 만기보유증권(HTM)의 수백억 달러 미실현 손실",
                    "스마트폰 뱅킹을 통한 36시간 만의 420억 달러 초고속 예금 인출"
                ],
                "signal": "bearish",
                "signal_reason": "장기 국채금리가 재차 4.5~5.0%대로 치솟을 경우 중소형 은행 및 비은행 금융권의 채권 평가손실 리스크가 재부각될 우려가 있음.",
                "key_companies": ["SVB Financial(파산)", "뉴욕커뮤니티뱅코프(NYCB)"],
                "insight": "금리 상승 국면에서는 신용 리스크뿐만 아니라 금리 변동에 따른 듀레이션 자산 평가손실이 금융 시스템의 가장 취약한 고리가 됨.",
                "action_point": "미국 장기 국채금리 고공행진에 따른 미국 중소형 지역은행 및 상업용 부동산 대출 연체율 추이를 면밀히 모니터링해야 함."
            },
            "classification": {
                "primary_topic": "economy",
                "secondary_topics": ["stock"],
                "tags": ["SVB파산", "미국국채", "금리상승", "채권평가손", "금융리스크"]
            }
        }
    },
    "DPOrtYANtUo": {
        "primary": "stock",
        "data": {
            "video": {
                "id": "DPOrtYANtUo",
                "title": "부담스러운 국채금리 상승..미국증시 약세 | 데일리 라이브 | 2026.8.18(화)",
                "published": "2026-08-18T11:16:28+00:00",
                "channel_name": "Smart Money by MiraeAsset ",
                "url": "https://www.youtube.com/watch?v=DPOrtYANtUo",
                "thumbnail": "https://img.youtube.com/vi/DPOrtYANtUo/hqdefault.jpg"
            },
            "analysis": {
                "summary": "미국 10년물 국채금리가 다시 4.5% 수준으로 반등하면서 기술주 중심의 나스닥과 S&P500이 차익실현 매물로 약세를 보임. 엔비디아 실적 발표를 앞둔 관망 심리와 유가 반등, FOMC 의사록 발표 경계감이 겹치며 단기 <span class=\"text-amber-300 font-bold\">밸류에이션 부담 완화 과정</span>이 진행 중임.",
                "key_claims": [
                    "국채금리 상승 압력이 밸류에이션 부담이 큰 고PER 성장주에 즉각적인 하방 압력으로 작용.",
                    "실적 시즌 막바지 핵심 이벤트인 <span class=\"text-cyan-300 font-semibold\">엔비디아 실적 및 블랙웰 출하 가이던스</span> 확인 전까지 지수 횡보 가능성 큼.",
                    "경기 둔화 우려보다는 금리 및 채권 공급 물량 부담에 따른 기술적 조정 양상임."
                ],
                "data_points": [
                    "미국 10년물 국채금리 4.48% 상승 및 달러 인덱스 104선 안착",
                    "나스닥 지수 -0.8% 하락 마감 및 필라델피아 반도체 지수 단기 숨고르기"
                ],
                "signal": "neutral",
                "signal_reason": "펀더멘털 훼손이 아닌 금리 반등과 대형 이벤트 앞둔 단기 기간 조정 국면으로 판단됨.",
                "key_companies": ["엔비디아(NVDA)", "애플(AAPL)", "마이크로소프트(MSFT)"],
                "insight": "금리 상승기에는 지수 전체의 추세적 상승보다 실적이 뒷받침되는 개별 종목 장세로 압축되므로 실적 발표 결과에 따른 종목 선별이 필수적임.",
                "action_point": "엔비디아 실적 발표 및 컨퍼런스콜에서 언급될 차세대 칩 양산 일정과 데이터센터 수요 코멘트를 최종 확인 후 포지션 조정."
            },
            "classification": {
                "primary_topic": "stock",
                "secondary_topics": ["economy", "tech"],
                "tags": ["미국증시", "국채금리", "엔비디아", "나스닥", "단기조정"]
            }
        }
    },
    "E4gz6V0LNR0": {
        "primary": "space",
        "data": {
            "video": {
                "id": "E4gz6V0LNR0",
                "title": "스페이스X 10GW 데이터센터 누가 쓸까?",
                "published": "2026-08-18T08:00:05+00:00",
                "channel_name": "안될공학 - IT 테크 신기술",
                "url": "https://www.youtube.com/watch?v=E4gz6V0LNR0",
                "thumbnail": "https://img.youtube.com/vi/E4gz6V0LNR0/hqdefault.jpg"
            },
            "analysis": {
                "summary": "<span class=\"text-cyan-300 font-semibold\">스페이스X</span>가 추진하는 10GW급 초대형 데이터센터 구상은 단순한 지상 전력 공급을 넘어 스타링크 우주 통신망과 <span class=\"text-cyan-300 font-semibold\">xAI(Grok)</span>, 테슬라 자율주행(FSD) 및 휴머노이드 로봇(옵티머스)의 두뇌 인프라로 직결됨. 우주 태양광 및 텍사스 테네시 메가 데이터센터 클러스터를 결합해 전력 병목을 돌파하려는 머스크 생태계의 야심을 분석함.",
                "key_claims": [
                    "10GW는 원자력 발전소 10기에 맞먹는 막대한 전력 규모로, 기존 빅테크 데이터센터 총합을 압도하는 수준임.",
                    "이 막대한 컴퓨팅 파워의 실질 사용자는 xAI의 차세대 거대언어모델 훈련 및 테슬라 로보택시·옵티머스 피지컬 AI 클라우드임.",
                    "스페이스X의 스타링크 고속 통신과 결합하여 전 세계 오지 및 우주 궤도까지 커버하는 독점적 분산 AI 인프라 구축 목표."
                ],
                "data_points": [
                    "스페이스X 및 xAI 멤피스 콜로서스 데이터센터 10만 개 이상 H100/H200 GPU 클러스터 가동",
                    "10GW 전력 소모 규모: 대도시 전체 전력 소비량 수준"
                ],
                "signal": "bullish",
                "signal_reason": "우주 발사체 및 위성 통신 독점에 이어 AI 슈퍼컴퓨팅 인프라까지 수직 통합하는 스페이스X/xAI의 기업가치 상승 모멘텀이 강력함.",
                "key_companies": ["스페이스X", "테슬라(TSLA)", "엔비디아(NVDA)"],
                "insight": "전력망 병목이 AI 확장의 최대 걸림돌로 떠오른 상황에서 자체 발전 인프라와 10GW급 데이터센터를 선점하는 자가 AGI 경쟁의 최종 승기를 잡게 됨.",
                "action_point": "스페이스X 상장(IPO) 모멘텀과 함께 테슬라의 AI 컴퓨팅 자산 가치 및 차세대 전력 장비 기업들과의 연계성을 주목할 것."
            },
            "classification": {
                "primary_topic": "space",
                "secondary_topics": ["tech", "energy"],
                "tags": ["스페이스X", "10GW데이터센터", "xAI", "스타링크", "전력인프라"]
            }
        }
    },
    "Es5j8cypZvs": {
        "primary": "economy",
        "data": {
            "video": {
                "id": "Es5j8cypZvs",
                "title": "환율조작국이라더니... 미국이 엔화 개입한 이유 #교양이를부탁해 #엔화 #미국국채 #베센트 #미국부채",
                "published": "2026-08-18T11:00:13+00:00",
                "channel_name": "교양이를 부탁해",
                "url": "https://www.youtube.com/watch?v=Es5j8cypZvs",
                "thumbnail": "https://img.youtube.com/vi/Es5j8cypZvs/hqdefault.jpg"
            },
            "analysis": {
                "summary": "미국 재무부가 과거 환율조작국 지정을 경고하던 태도를 바꿔 일본 당국의 <span class=\"text-amber-300 font-bold\">엔화 매수 시장 개입을 묵인·공조한 본질적 이유</span>는 일본의 미 국채 투매를 방어하기 위함임. 엔화 가치 방어를 위해 일본이 보유 중인 미 국채를 대거 매각할 경우 미국 국채금리가 폭등하여 미국 재정에 치명타가 되기 때문임.",
                "key_claims": [
                    "일본은 전 세계 최대의 미국 국채 보유국(1.1조 달러 이상)으로, 엔화 방어를 위한 달러 확보 시 미 국채 매각이 불가피함.",
                    "미국은 자국 국채금리 급등을 막기 위해 일본의 통화 방어 조치와 금리 인상을 일정 수준 용인하는 밀월 관계를 형성함."
                ],
                "data_points": [
                    "일본 보유 미국 국채 잔액: 약 1조 1,000억 달러 돌파",
                    "엔/달러 환율 150~160엔대 변동성과 일본은행(BOJ) 외환시장 개입 규모"
                ],
                "signal": "neutral",
                "signal_reason": "엔화 강세 전환 시 엔 캐리 트레이드 청산 변동성이 발생할 수 있으나, 미-일 정책 공조로 시스템 위기 가능성은 제어됨.",
                "key_companies": [],
                "insight": "글로벌 환율 정책은 단순한 무역 경쟁력이 아니라 각국의 '국채 시장 안정'과 부채 방어를 위한 치밀한 지정학적 금융 역학에 의해 결정됨.",
                "action_point": "엔/달러 환율 추이와 일본은행의 금리 인상 스케줄이 글로벌 유동성 및 미 국채금리에 미치는 파급 효과를 예의주시해야 함."
            },
            "classification": {
                "primary_topic": "economy",
                "secondary_topics": ["stock"],
                "tags": ["엔화개입", "미국국채", "일본보유국채", "환율전쟁", "엔캐리"]
            }
        }
    },
    "FbUJlYgKDoY": {
        "primary": "stock",
        "data": {
            "video": {
                "id": "FbUJlYgKDoY",
                "title": "이중바닥 믿었는데 왜 또 저점을 깰까...개미 털기 피해 진짜 주도주 가려내는 법ㅣ명민준, 박세미, 이지환 [주린이 구조대]",
                "published": "2026-08-18T13:30:36+00:00",
                "channel_name": "삼프로TV_3ProTV",
                "url": "https://www.youtube.com/watch?v=FbUJlYgKDoY",
                "thumbnail": "https://img.youtube.com/vi/FbUJlYgKDoY/hqdefault.jpg"
            },
            "analysis": {
                "summary": "기술적 분석상의 단순 '이중바닥(W자)' 패턴만 믿고 진입했다가 가짜 반등에 속아 손실을 보는 개인 투자자들을 위해 <span class=\"text-cyan-300 font-semibold\">기관·외국인의 선물 매매 패턴과 수급 털기 메커니즘</span>을 분석함. 차트 저점 지지 여부보다 업종 실적 턴어라운드와 메이저 수급 유입이 동반되는 진짜 주도주 선별법을 제시함.",
                "key_claims": [
                    "장 초반 갭상승 후 장중 선물 매도로 전강후약을 만드는 패턴은 전형적인 개인 심리 흔들기 및 물량 털기 기법임.",
                    "차트의 이중바닥이 지지력을 가지려면 직전 저점 대비 거래량 감소 후 반등 시 외국인 순매수가 확정적으로 붙어야 함.",
                    "주도주는 급락장에서 지수보다 덜 빠지고 저점을 높이며 가장 먼저 전고점을 회복하는 종목군에서 나옴."
                ],
                "data_points": [
                    "외국인 코스피 선물 1조 원 이상 순매수 후 장중 전매도로 전환되는 변동성 패턴 분석",
                    "반도체 대형주 장중 7~8% 급등 후 보합권 회귀 등 변동폭 확대"
                ],
                "signal": "neutral",
                "signal_reason": "단기 수급 흔들기로 지수 변동성이 크므로 차트만 보고 추격 매수하기보다 분할 매수와 실적 팩트 체크가 필수적임.",
                "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
                "insight": "시장의 페이크에 당하지 않는 유일한 방법은 차트의 모양에 매몰되지 않고, 업황 사이클상 공급 부족과 판가 상승이 명확한 1등 주도주를 흔들릴 때 모아가는 것임.",
                "action_point": "단기 갭상승 시 뇌동매수를 자제하고, 장 마감 기준 외국인 선물/현물 수급 연속성과 주도주 저점 지지력을 확인한 후 진입할 것."
            },
            "classification": {
                "primary_topic": "stock",
                "secondary_topics": ["tech"],
                "tags": ["이중바닥", "개미털기", "외국인수급", "선물매매", "주도주선별"]
            }
        }
    }
}

for vid, item in batch2_data.items():
    primary = item["primary"]
    out_dir = Path(f"data/analyzed/{primary}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{vid}.json"
    with open(out_file, "w", encoding="utf-8") as fp:
        json.dump(item["data"], fp, ensure_ascii=False, indent=2)
    
    pending_file = Path(f"data/pending/{vid}.json")
    if pending_file.exists():
        pending_file.unlink()
    print(f"[Batch 2 완료] {vid} -> data/analyzed/{primary}/{vid}.json")
