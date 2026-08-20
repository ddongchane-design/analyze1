import json
from pathlib import Path

batch5 = [
    {
        "video": {
            "id": "WbyANFDUvPs",
            "title": "AI 서밋, 숫자보다 중요한 변화 | 실리콘밸리뷰 | 원호섭 특파원",
            "published": "2026-08-01T23:00:13+00:00",
            "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=WbyANFDUvPs",
            "thumbnail": "https://img.youtube.com/vi/WbyANFDUvPs/hqdefault.jpg"
        },
        "analysis": {
            "summary": "실리콘밸리 현지 AI 서밋 현장 취재를 통해 단순 수치적 성장을 넘어 AI가 기업의 <span class=\"text-cyan-300 font-semibold\">실질적 비즈니스 워크플로우(에이전틱 AI)</span>로 전면 채택되는 질적 변화 패러다임을 전달함. AI 모델의 벤치마크 점수 경쟁보다 현업 ROI 입증이 엔터프라이즈 도입의 핵심 잣대로 작용함.",
            "key_claims": [
                "AI 경쟁의 핵심 축이 단순 LLM 모델 파라미터 크기에서 실무 자동화를 완수하는 에이전틱 AI(Agentic AI)로 이동함.",
                "실리콘밸리 빅테크 및 스타트업들은 구체적인 비용 절감 및 매출 창출(ROI)을 입증해야 투자금을 유치하는 국면임."
            ],
            "data_points": [
                "실리콘밸리 AI 서밋 참가 기업 및 에이전트 도입 비율 사례 분석"
            ],
            "signal": "bullish",
            "signal_reason": "AI 기술이 뜬구름 잡는 연구 단계를 지나 실질적 기업 생산성 혁신 및 이익 창출 단계로 안착하고 있기 때문임.",
            "key_companies": ["엔비디아(NVDA)", "마이크로소프트(MSFT)", "OpenAI"],
            "insight": "AI 생태계의 패러다임은 모델 수치 경쟁에서 '기업 업무 자동화 및 워크플로우 에이전트'라는 실질적 수익화 단계로 대전환 중임.",
            "action_point": "에이전틱 AI 도구를 기업용 ERP/SaaS 서비스에 가장 효과적으로 결합하는 테크 기업 중심 선별 보유."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock", "economy"],
            "tags": ["AI서밋", "실리콘밸리", "에이전틱AI", "원호섭", "ROI입증"]
        }
    },
    {
        "video": {
            "id": "Wumw8v9eLZI",
            "title": "'코스모스'의 뜻은 #코스모스 #칼세이건 #지웅배 #북언더스탠딩",
            "published": "2026-08-02T14:15:14+00:00",
            "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=Wumw8v9eLZI",
            "thumbnail": "https://img.youtube.com/vi/Wumw8v9eLZI/hqdefault.jpg"
        },
        "analysis": {
            "summary": "칼 세이건의 고전 명작 '코스모스(Cosmos)'의 어원적 의미인 '질서 정연한 우주(Chaos의 반대)'와 우주를 바라보는 인류의 과학적·철학적 통찰을 조명함. 천문학 지식과 우주관의 확장을 다룸.",
            "key_claims": [
                "코스모스는 무질서한 카오스(Chaos)에서 조화와 질서를 갖춘 세계를 의미함."
            ],
            "data_points": [],
            "signal": "na",
            "signal_reason": "우주 천문학 및 도서 리뷰 교양 숏폼 콘텐츠로 투자와 직접적 무관.",
            "key_companies": [],
            "insight": "우주 과학적 통찰은 인류의 지적 경계를 확장하고 우주 항공 산업의 장기적 학술적 기반을 다짐.",
            "action_point": "우주 과학 및 인문학적 교양 지식 습득."
        },
        "classification": {
            "primary_topic": "space",
            "secondary_topics": ["etc"],
            "tags": ["코스모스", "칼세이건", "천문학", "북언더스탠딩", "지웅배"]
        }
    },
    {
        "video": {
            "id": "_jO1zz4xnMg",
            "title": "7조원 매물 폭탄? 스트래티지 또 파나, 비트코인 전망",
            "published": "2026-08-02T04:00:05+00:00",
            "channel_name": "디파이 농부 조선생 | Professor Jo",
            "url": "https://www.youtube.com/watch?v=_jO1zz4xnMg",
            "thumbnail": "https://img.youtube.com/vi/_jO1zz4xnMg/hqdefault.jpg"
        },
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">마이크로스트래티지(MSTR)</span> 및 대형 기관들의 <span class=\"text-rose-400 font-medium\">7조 원 규모 비트코인(BTC) 매물 출회</span> 소문과 관련된 수급적 사실관계를 검증함. 비트코인 온체인 데이터 및 마이닝 헤지 수급, ETF 자금 유출입 추이를 바탕으로 크립토 시장의 하방 지지력과 향후 시나리오를 예측함.",
            "key_claims": [
                "마이크로스트래티지의 비트코인 매도설은 지배구조 특성상 과장된 루머이며, 실제 전환사채 및 자산 보유는 안정적임.",
                "단기 7조 원 수준의 채굴자 및 레버리지 매물 소화 과정 이후 6만 달러선 중반 재진입 가능성이 높음."
            ],
            "data_points": [
                "비트코인(BTC) 온체인 물량 및 마이크로스트래티지 총 보유량 통계"
            ],
            "signal": "neutral",
            "signal_reason": "대규모 수급 매물 압박 루머와 온체인 지지력 확인이 대립하는 단기 박스권 구간이기 때문임.",
            "key_companies": ["마이크로스트래티지(MSTR)", "비트코인(BTC)"],
            "insight": "가상자산 시장의 매물 폭탄 루머는 공포감을 유발하지만, 현물 ETF 수급과 온체인 장기 홀더들의 물량 흡수력이 바닥을 받치고 있음.",
            "action_point": "비트코인 현물 ETF 자금 수지 및 온체인 보유 비율 확인 후 분할 대응."
        },
        "classification": {
            "primary_topic": "crypto",
            "secondary_topics": ["stock", "economy"],
            "tags": ["비트코인", "마이크로스트래티지", "매물폭탄", "가상자산전망", "조선생"]
        }
    },
    {
        "video": {
            "id": "eRqLWRAkmhc",
            "title": "체중은 그대로, 건강검진은 빨간불? 내 몸속에 몰래 쌓인 '이것' #교양이를부탁해 #비만 #다이어트 #체중감량",
            "published": "2026-08-02T09:00:02+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=eRqLWRAkmhc",
            "thumbnail": "https://img.youtube.com/vi/eRqLWRAkmhc/hqdefault.jpg"
        },
        "analysis": {
            "summary": "겉보기 체중은 정상이나 장기 사이에 몰래 쌓이는 <span class=\"text-rose-400 font-medium\">내장지방 및 이소성 지방(Ectopic Fat)</span>의 위협을 경고함. 내장지방이 대사성 혈관계 질환과 지방간, 인슐린 저항성을 악화시키는 기전을 설명함.",
            "key_claims": [
                "체중 수치보다 장기 주변 이소성 지방 및 내장지방 농도가 진짜 건강 위험 지표임.",
                "정제 탄수화물 과다 섭취가 내장지방 축적의 가장 강력한 촉매제임."
            ],
            "data_points": [
                "정상 체중 내장비만 환자의 대사 증후군 발병률 비중"
            ],
            "signal": "na",
            "signal_reason": "대사 건강 및 내장비만을 경고하는 의학 숏폼 지식 영상임.",
            "key_companies": [],
            "insight": "현대인 대사 건강의 주적은 단순 체중이 아닌 내장지방이며, 식습관 정화와 대사 기능 관리가 최우선 과제임.",
            "action_point": "건강검진 지표 및 대사 관리 헬스케어 동향 참고."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["내장지방", "이소성지방", "건강검진", "대사증후군"]
        }
    },
    {
        "video": {
            "id": "gQFZDoj5ZXU",
            "title": "구약성경보다 먼저 존재했던 이야기… 메소포타미아에서 찾은 성경의 기원 | 주원준 한님성서연구소 수석연구원 [에인션트]",
            "published": "2026-08-02T06:00:33+00:00",
            "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?gQFZDoj5ZXU",
            "thumbnail": "https://img.youtube.com/vi/gQFZDoj5ZXU/hqdefault.jpg"
        },
        "analysis": {
            "summary": "메소포타미아 문명의 점토판 문헌(길가메시 서사시 등)과 구약성경 간의 문화적·고고학적 연관성을 정밀히 고찰함. 고대 문명의 서사 체계가 인류 문화사와 고고학 연구에 미친 기원의 가치를 깊이 있게 다룸.",
            "key_claims": [
                "고대 고고학 유물과 메소포타미아 쐐기문자는 성서 고고학 및 인류 문명사의 기원을 밝히는 열쇠임.",
                "문화적 서사는 이웃 문명 간의 지속적 교류와 수용을 통해 진화함."
            ],
            "data_points": [
                "메소포타미아 쐐기문자 점토판 발굴 연대 및 기록 내역"
            ],
            "signal": "na",
            "signal_reason": "고고학 및 고대 역사 문명 연구를 탐구하는 문화 교양 콘텐츠임.",
            "key_companies": [],
            "insight": "고대 문명의 역사적 유산은 인류의 지적 인문학적 자산이자 문화적 연속성을 입증하는 고고학적 가치임.",
            "action_point": "인문 고고학적 지식 습득."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["메소포타미아", "고고학", "구약성경", "길가메시", "주원준"]
        }
    },
    {
        "video": {
            "id": "hN_fGhqQH1M",
            "title": "폭락의 주범이 꺾이고 반등의 시작일까? 이 지표를 봐야 합니다",
            "published": "2026-08-02T15:46:47+00:00",
            "channel_name": "이효석아카데미",
            "url": "https://www.youtube.com/watch?v=hN_fGhqQH1M",
            "thumbnail": "https://img.youtube.com/vi/hN_fGhqQH1M/hqdefault.jpg"
        },
        "analysis": {
            "summary": "주가 폭락을 유도했던 <span class=\"text-rose-400 font-medium\">엔화 캐리 트레이드 청산 및 장기 국채 금리 급등세</span>가 일시적으로 진정되는 시점에서, 추세적 반등을 확인하기 위해 필수적으로 추적해야 할 <span class=\"text-cyan-300 font-semibold\">핵심 마크로 지표(엔/달러 환율, 실질 금리, 빅테크 이익 수정 비율)</span>를 제시함.",
            "key_claims": [
                "엔화 강발 폭락 압력이 멈추면서 자산 시장 변동성 지수(VIX)가 진정되고 있음.",
                "주가 반등의 지속성은 단순 가격 낙폭이 아니라 EPS(주당순이익) 상향 조정 비율이 유지되는지에 달려 있음."
            ],
            "data_points": [
                "엔/달러 환율 변동 폭 및 미국 10년물 실질금리 수치",
                "글로벌 빅테크 이익 수정 비율(Earnings Revision Ratio)"
            ],
            "signal": "bullish",
            "signal_reason": "폭락의 핵심 주범이었던 환율 및 실질 금리 불안감이 꺾이고 실적 모멘텀 지표가 살아나고 있기 때문임.",
            "key_companies": ["엔비디아(NVDA)", "SK하이닉스(000660)", "삼성전자(005930)"],
            "insight": "시장의 공포감이 극에 달할 때 매도 주범 지표(엔화/금리)의 피크아웃을 확인하면 주가 최적의 기술적 반등 타점을 잡을 수 있음.",
            "action_point": "엔/달러 환율 및 빅테크 이익 수정 비율 지표를 모니터링하며 주도주 매수 대응."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["엔화캐리", "반등지표", "실질금리", "이익수정비율", "이효석"]
        }
    }
]

def save_batch(batch):
    for item in batch:
        primary = item["classification"]["primary_topic"]
        vid = item["video"]["id"]
        out_dir = Path(f"data/analyzed/{primary}")
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{vid}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
        print(f"[저장 완료] {out_file}")
        
        pending_file = Path(f"data/pending/{vid}.json")
        if pending_file.exists():
            pending_file.unlink()
            print(f"[삭제 완료] {pending_file}")

if __name__ == "__main__":
    save_batch(batch5)
