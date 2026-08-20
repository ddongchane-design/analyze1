import json
from pathlib import Path

batch2 = [
    {
        "video": {
            "id": "BZdHWpfndFE",
            "title": "똑같이 쪄도 당뇨 위험은 더 높다? 한국인이 유독 취약한 이유 #교양이를부탁해 #비만 #다이어트 #체중감량",
            "published": "2026-08-02T09:30:03+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=BZdHWpfndFE",
            "thumbnail": "https://img.youtube.com/vi/BZdHWpfndFE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "한국인을 비롯한 동양인이 서양인에 비해 췌장 크기가 작고 인슐린 분비 능력이 떨어져, 동일한 체중 증가 조건에서도 <span class=\"text-rose-400 font-medium\">당뇨병 발병 위험</span>이 유독 높음을 신체 구조적 특성 관점에서 설명함. 마른 비만과 췌장 대사 부담 완화를 위한 식습관 관리가 중요함.",
            "key_claims": [
                "동양인은 췌장 베타세포 부피가 작아 동일 BMI 상황에서도 인슐린 저항성에 취약함.",
                "체중 수치보다 체지방률 및 내장지방 축적이 당뇨 발병에 더 결정적인 원인임."
            ],
            "data_points": [
                "동양인 평균 췌장 크기 및 인슐린 분비 능력: 서양인 대비 약 20~30% 저하"
            ],
            "signal": "na",
            "signal_reason": "의학 및 체질적 대사 특성을 설명하는 제네럴 헬스 콘텐츠임.",
            "key_companies": [],
            "insight": "한국인의 체질적 췌장 인슐린 분비 한계는 향후 연속혈당측정기(CGM) 및 비만/당뇨 관리 헬스케어 솔루션 수요 확대로 연결됨.",
            "action_point": "혈당 관리 및 당뇨 케어 기기/제약 밸류체인의 성장 잠재력을 가늠할 수 있음."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["당뇨병", "인슐린", "췌장", "한국인체질", "마른비만"]
        }
    },
    {
        "video": {
            "id": "BnYn0LOby7w",
            "title": "잘 나가던 펀드매니저, 모텔 샀다가 피눈물 흘렸다 (더휴식 김준하 대표)",
            "published": "2026-08-02T11:55:00+00:00",
            "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=BnYn0LOby7w",
            "thumbnail": "https://img.youtube.com/vi/BnYn0LOby7w/hqdefault.jpg"
        },
        "analysis": {
            "summary": "전직 펀드매니저 출신 창업가가 중소형 숙박시설(모텔) 자산운용 및 리노베이션 브랜드 사업(<span class=\"text-amber-300 font-bold\">더휴식</span>)에 도전하며 겪은 시행착오와 부동산 금융, 밸류애드(Value-add) 사업 모델을 실무적으로 솔직히 증언함. 금리 변동성과 오프라인 자산 관리의 난곡, 그리고 IT 기반 공간 효율화 솔루션의 중요성을 다룸.",
            "key_claims": [
                "부동산 자산 운용에서 단순 매입보다 운영 효율화(무인화, 브랜드화)를 통한 캡레이트(Cap Rate) 개선이 핵심임.",
                "고금리 기조하에서 레버리지 위주의 중소형 상업용 부동산 투자는 극심한 자금 압박을 유발함."
            ],
            "data_points": [
                "더휴식 숙박 공간 운영 펀드 및 관리 자산 규모 증대 사례 공유"
            ],
            "signal": "neutral",
            "signal_reason": "부동산 리노베이션 및 공간 운용의 현실적 어려움과 펀더멘털 투자 원칙을 제시하는 인터뷰임.",
            "key_companies": ["더휴식"],
            "insight": "상업용 부동산 시장은 단순 자본 이득(Capital Gain) 시대에서 운용 수익률(Operating Yield)을 극대화하는 IT/공간 기획 중심 밸류애드 시대 전환 중.",
            "action_point": "고금리 환경 속 리츠(REITs) 및 상업용 부동산 자산의 현금흐름 캡레이트 및 무인화 관리 능력 검증이 필수적임."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["부동산투자", "더휴식", "모텔리노베이션", "상업용부동산", "캡레이트"]
        }
    },
    {
        "video": {
            "id": "DSNM-eXlHqE",
            "title": "AI 급락과 마진콜? 가장 싼 반도체를 찾아야 하는 이유",
            "published": "2026-08-01T10:00:25+00:00",
            "channel_name": "수페TV",
            "url": "https://www.youtube.com/watch?v=DSNM-eXlHqE",
            "thumbnail": "https://img.youtube.com/vi/DSNM-eXlHqE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "AI 및 빅테크 기술주의 최근 조정이 레버리지 투자자들의 마진콜 및 수급 청산에 따른 단기 충격임을 설명하고, 이럴 때일수록 <span class=\"text-cyan-300 font-semibold\">밸류에이션(PER/PBR) 관점에서 가장 저평가된 반도체 소부장</span> 및 밸류체인 기업을 선별해야 함을 조언함. 엔비디아의 이익 상향 지속성과 하이퍼스케일러의 CapEx는 여전히 유효함.",
            "key_claims": [
                "레버리지 상품 몰락과 마진콜 청산으로 인한 변동성은 저가 매수의 기회로 작동함.",
                "단순히 1등 대장주만 따라가기보다 실적 대비 밸류에이션 멀티플이 매력적인 소부장 기업이 하방 안정성이 높음."
            ],
            "data_points": [
                "주요 글로벌 반도체 종목별 Forward PER 및 PBR 비교 데이터 제공"
            ],
            "signal": "bullish",
            "signal_reason": "AI 인프라 수혜 펀더멘털은 견고하며, 마진콜 및 레버리지 청산으로 주가가 바닥을 잡는 구간임.",
            "key_companies": ["엔비디아(NVDA)", "ASML(ASML)", "삼성전자(005930)", "SK하이닉스(000660)"],
            "insight": "시장 전체가 수급 이슈로 동반 폭락할 때는 이익 성장률(EPS Growth) 대비 멀티플이 과도하게 낮아진 저평가 꿀주식을 줍는 전략이 유효함.",
            "action_point": "Forward PER 밸류에이션 매력이 높은 메모리 및 반도체 공정 핵심 수혜주 중심으로 포트폴리오를 분할 재편할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech"],
            "tags": ["AI급락", "마진콜", "저평가반도체", "밸류에이션", "수페TV"]
        }
    },
    {
        "video": {
            "id": "DoRKA9Udcag",
            "title": "중국 반도체 쇼크의 진실, 한국은 정말 위기일까? | 전병서 중국경제금융연구소 소장 [주말인터뷰]",
            "published": "2026-08-02T02:00:08+00:00",
            "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=DoRKA9Udcag",
            "thumbnail": "https://img.youtube.com/vi/DoRKA9Udcag/hqdefault.jpg"
        },
        "analysis": {
            "summary": "중국의 반도체 자립화 및 수입 규제 구도 속에서, 중국의 성숙 공정(Legacy process) 및 CXMT 등의 낸드/D램 추격 속도와 <span class=\"text-cyan-300 font-semibold\">한국 반도체 기업들의 독점적 기술 격차(HBM 등)</span>를 깊이 있게 비교 분석함. 중국의 기술 굴기가 레거시 영역에서는 수급 압박을 가하지만, 선단 공정과 최첨단 AI 메모리 분야에서는 한국의 우위가 유지되고 있음을 지적함.",
            "key_claims": [
                "중국 CXMT, SMIC의 성장으로 범용 D램 및 성숙 공정 가격 하방 압력은 현실화됨.",
                "그러나 AI 필수재인 HBM3E 및 3D 낸드 고단화에서는 미·중 기술 통제로 인해 중국과의 격차가 최소 3~5년 유지됨.",
                "한국 기업은 레거시 비중을 줄이고 최첨단 HBM 파운드리/메모리 결합 생태계로 진화해야 함."
            ],
            "data_points": [
                "중국 글로벌 반도체 생산 점유율(레거시 부문): 30% 수준육박",
                "CXMT/SMIC의 굴기 및 미국 반도체 장비 규제 품목 목록 분석"
            ],
            "signal": "neutral",
            "signal_reason": "레거시 반도체의 중국발 공급 과잉 리스크와 최첨단 HBM 독점 수혜가 팽팽하게 맞서기 때문임.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "CXMT", "SMIC", "TSMC"],
            "insight": "중국 반도체 굴기의 위협은 레거시 품목에 국한되며, HBM 및 초미세 파운드리 기술 주도권을 쥔 한국 메모리 2사에 대한 구조적 프리미엄은 지속됨.",
            "action_point": "범용 메모리 의존도가 높은 중소형주 대신 HBM 및 고부가가치 서버용 D램 기술을 주도하는 투톱 대장주 위주로 선별 대응."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["중국반도체", "CXMT", "HBM격차", "레거시반도체", "전병서"]
        }
    },
    {
        "video": {
            "id": "FAT3g6vLNJk",
            "title": "뱅크시 충격적 정체 굳이 까발린 이유 (아츠인유 이세라 대표)",
            "published": "2026-08-02T05:55:38+00:00",
            "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=FAT3g6vLNJk",
            "thumbnail": "https://img.youtube.com/vi/FAT3g6vLNJk/hqdefault.jpg"
        },
        "analysis": {
            "summary": "얼굴 없는 스트리트 아티스트 <span class=\"text-amber-300 font-bold\">뱅크시(Banksy)</span>의 예술 세계와 그의 정체 공개를 둘러싼 현대 미술 경매 시장, 신비주의 마케팅 기법 및 작품 자산가치의 변동성을 분석함. 예술이 어떻게 자본주의 시장과 결합하여 막대한 자산 가치를 창출하는지 탐구함.",
            "key_claims": [
                "뱅크시의 익명성은 단순한 취향이 아닌 작품의 저항 정신과 시장 가치를 극대화하는 브랜드 전략임.",
                "현대 미술품 거래는 희소성과 스토리텔링이 자산 가격을 결정하는 대체 투자 시장임."
            ],
            "data_points": [
                "뱅크시 대표작 '풍선과 소녀' 경매 낙찰가 및 파쇄 퍼포먼스 후 가치 상승 사례"
            ],
            "signal": "na",
            "signal_reason": "현대 미술사 및 미술품 경매 시장의 특성을 소개하는 문화·예술 교양 영상임.",
            "key_companies": ["소더비", "크리스티"],
            "insight": "미술품 시장에서 자산 가치는 물질적 원가보다 '스토리텔링과 익명성 브랜딩'이라는 무형의 희소성 요소에 의해 폭발적으로 형성됨.",
            "action_point": "대체 자산 시장(미술품, 조각투자 등)의 가치 산정 방식과 브랜딩 효과를 교양 수준에서 숙지."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["뱅크시", "현대미술", "미술품경매", "대체자산", "아츠인유"]
        }
    },
    {
        "video": {
            "id": "FiC7qjeaQdE",
            "title": "아마존, 컨퍼런스콜 환호에 15%↑...30년물 국채금리 또 고점 돌파 [월가 뉴스레터]",
            "published": "2026-08-02T22:03:21+00:00",
            "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=FiC7qjeaQdE",
            "thumbnail": "https://img.youtube.com/vi/FiC7qjeaQdE/hqdefault.jpg"
        },
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">아마존(AMZN)</span>이 클라우드 AWS 매출 재가속 및 효율적인 CapEx 집행에 힘입어 실적 발표 후 주가가 15% 급등한 반면, 미국 <span class=\"text-rose-400 font-medium\">30년물 국채 금리</span>가 또다시 고점을 돌파하며 장기 금리 상방 압력이 기술주 밸류에이션을 위협하는 엇갈린 월가 상황을 전함. 빅테크 실적 차별화 장세가 가속화되고 있음.",
            "key_claims": [
                "아마존 AWS의 영업이익률과 AI 클라우드 수주 가속화가 주가 폭등의 주된 동력임.",
                "미국 장기 국채 발행 부담으로 30년물 금리가 고점을 재차 갱신하여 거시 금융 환경은 부담스러운 상태임.",
                "실적이 기대치에 못 미치는 빅테크는 급락하고 실적으로 입증한 빅테크는 급등하는 극단적 차별화 지속."
            ],
            "data_points": [
                "아마존(AMZN) 실적 발표 후 주가 상승률: +15%",
                "미국 30년물 국채 금리: 4.6%선 돌파 및 고점 재경신"
            ],
            "signal": "bullish",
            "signal_reason": "장기 금리 상승이라는 거시 악재에도 불구하고 AI 클라우드 실적이 증명된 대형 빅테크의 이익 창출력이 시장을 압도하기 때문임.",
            "key_companies": ["아마존(AMZN)", "마이크로소프트(MSFT)", "알파벳(GOOGL)", "엔비디아(NVDA)"],
            "insight": "금리가 높아진 시장 환경에서는 단순 스토리가 아닌 확실한 실적(AWS 클라우드 마진 등)을 뽑아내는 1등 빅테크만 상승세를 독식함.",
            "action_point": "AI 투자가 실제 클라우드 매출 실적으로 연결되는 아마존 등 실적 확인 기업 위주로 투자 집중."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy", "tech"],
            "tags": ["아마존", "AWS실적", "국채금리", "월가뉴스레터", "빅테크실적"]
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
    save_batch(batch2)
