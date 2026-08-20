import json
from pathlib import Path

batch3 = [
    {
        "video": {
            "id": "GnvOL9FVbu4",
            "title": "심판일까 공일까..워시의 정체는 | 월가백브리핑",
            "published": "2026-08-02T03:00:38+00:00",
            "channel_name": "한경 글로벌마켓",
            "url": "https://www.youtube.com/watch?v=GnvOL9FVbu4",
            "thumbnail": "https://img.youtube.com/vi/GnvOL9FVbu4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "연준 의장 차기 지목 인사 케빈 워시(Kevin Warsh)의 통화 정책 성향과 월가의 거시 통화적 해석을 분석함. 그가 과거 매파적 입장에서 벗어나 생산성 증대를 통한 적정 금리 유지를 강조하는 <span class=\"text-amber-300 font-bold\">실용주의적 통화관</span>을 피력하면서 금리 인하 기대감과 금융 시장 안정 의지가 교차함.",
            "key_claims": [
                "케빈 워시는 교조적 매파가 아닌 생산성 혁신과 공급 측면 물가 안정을 중시하는 인물임.",
                "연준의 자산 매각 속도 조절 및 고금리 고착화 우려 완화 가능성이 월가에 온기를 불어넣음."
            ],
            "data_points": [
                "미 연준 피벗 예상 시기 및 케빈 워시 지명에 따른 채권 금리 반응"
            ],
            "signal": "neutral",
            "signal_reason": "차기 연준 인사 지명 수혜와 통화 정책 피벗 의구심이 균형을 이루는 거시 모니터링 구간임.",
            "key_companies": [],
            "insight": "통화 당국의 지도부 교체 논의는 금리 경로의 불확실성을 축소시키고 자산 시장의 중장기 밸류에이션 하단을 탄탄하게 형성해 줌.",
            "action_point": "연준 인사들의 매파/비둘기파 스탠스 변화와 미국 10년물 국채 금리 트렌드를 계속 추적할 것."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["케빈워시", "연준의장", "월가백브리핑", "통화정책", "금리피벗"]
        }
    },
    {
        "video": {
            "id": "HNGStDCiUGY",
            "title": "반도체 급락세 진정되었나? 하반기 반도체투자는 빅테크만 봐서는 안됩니다 | 김장열 유니스토리자산운용 리서치센터 [글로벌 인터뷰]",
            "published": "2026-08-02T22:51:21+00:00",
            "channel_name": "삼프로TV_3ProTV",
            "url": "https://www.youtube.com/watch?v=HNGStDCiUGY",
            "thumbnail": "https://img.youtube.com/vi/HNGStDCiUGY/hqdefault.jpg"
        },
        "analysis": {
            "summary": "하반기 반도체 투자 전략으로 빅테크 7개사에만 매몰되지 말고, <span class=\"text-cyan-300 font-semibold\">소부장 독점 기술 기업과 메모리 벨류체인 핵심 수혜주</span>로 시선을 넓혀야 함을 강조함. 7월 급락세가 진정되면서 HBM 수급 숏티지와 파운드리 수주 실적이 뒷받침되는 펀더멘털주 위주의 하반기 랠리가 기대됨.",
            "key_claims": [
                "빅테크의 CapEx 부담 지적은 과도하며 실제 서버 및 가속기 주문량은 2027년까지 꽉 차 있음.",
                "하반기 수익률 측면에서는 1등 대장주보다 주가 하락폭이 컸던 핵심 반도체 소부장(장비/소재)의 반등 탄력이 더 클 수 있음."
            ],
            "data_points": [
                "2026년 하반기 HBM3E 및 HBM4 수주 가이던스 상향",
                "글로벌 빅테크 CapEx 총액 상향 추세"
            ],
            "signal": "bullish",
            "signal_reason": "반도체 급락세가 일단락되고 이익 추정치 상승에 따른 소부장 순환매 랠리 여건이 무르익었기 때문임.",
            "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "TSMC", "엔비디아(NVDA)"],
            "insight": "반도체 급락 이후의 진정한 주가 상승은 단순 지수 상승이 아닌 실적 개선이 뚜렷한 소부장 알짜 기업들의 밸류에이션 갭 메우기로 진행됨.",
            "action_point": "빅테크 외에도 HBM 공급망에 엮인 핵심 중소형 반도체 소부장 종목들을 눌림목 매수 타겟으로 설정."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech"],
            "tags": ["반도체하반기전망", "김장열", "HBM수혜주", "반도체소부장", "빅테크CapEx"]
        }
    },
    {
        "video": {
            "id": "JxGLfSiLsVs",
            "title": "냄새나고 비좁아도, 대체할 수 없는 도시.. 15초 벨소리가 만든 세계, 그 마지막 이야기 | 바이아메리카 in 뉴욕",
            "published": "2026-08-01T00:00:18+00:00",
            "channel_name": "한경 글로벌마켓",
            "url": "https://www.youtube.com/watch?v=JxGLfSiLsVs",
            "thumbnail": "https://img.youtube.com/vi/JxGLfSiLsVs/hqdefault.jpg"
        },
        "analysis": {
            "summary": "뉴욕시의 높은 주거비와 비좁은 물리적 한계에도 불구하고, 금융 자본과 혁신 인재, 통신 및 문화 인프라가 융합하며 대체 불가능한 <span class=\"text-amber-300 font-bold\">글로벌 도시 생태계</span>를 형성하는 메커니즘을 조명함. 15초 벨소리(노키아/이동통신 혁명 등)로 대표되는 글로벌 인프라 결합이 가져온 도시의 역사적 가치를 재해석함.",
            "key_claims": [
                "뉴욕은 단순 주거 공간을 넘어 글로벌 금융 자본과 인재 밀집에 따른 네트워크 효과가 무한 창출되는 곳임.",
                "도시의 경쟁력은 외형적 깨끗함보다 경제적 유인과 혁신 생태계 보유 여부로 결정됨."
            ],
            "data_points": [
                "뉴욕 월가 금융 자본 집적도 및 주거 밀도 통계"
            ],
            "signal": "na",
            "signal_reason": "글로벌 도시 경제학과 뉴욕의 생태적 특성을 조망하는 글로벌 탐방 교양 콘텐츠임.",
            "key_companies": [],
            "insight": "글로벌 자본과 인재가 집결하는 메가시티의 인프라 및 부동산 네트워크 효과는 고금리 시대에도 강한 상방 독점력을 지님.",
            "action_point": "글로벌 메가시티 중심의 자산 가치 상방 독점력 현상을 이해하고 거시적 인프라 트렌드에 적용."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": ["economy"],
            "tags": ["뉴욕", "바이아메리카", "도시경제학", "월가생태계"]
        }
    },
    {
        "video": {
            "id": "MFzDl06dU7Y",
            "title": "꿈이 있어야 앞으로 나아갈 수 있습니다",
            "published": "2026-08-02T11:00:26+00:00",
            "channel_name": "안될과학 Unrealscience",
            "url": "https://www.youtube.com/watch?v=MFzDl06dU7Y",
            "thumbnail": "https://img.youtube.com/vi/MFzDl06dU7Y/hqdefault.jpg"
        },
        "analysis": {
            "summary": "과학 탐구와 동기 부여를 주제로 한 동기부여 미니 숏폼 브이로그/동영상 콘텐츠로, 비전과 과학적 탐구 정신이 인류 문명과 인재 성장에 미치는 영향을 짧게 전달함.",
            "key_claims": [
                "명확한 꿈과 기술적 탐구 정신이 과학 기술 발전의 원동력임."
            ],
            "data_points": [],
            "signal": "na",
            "signal_reason": "순수 과학 동기부여 메시지를 다루는 short-form 동영상임.",
            "key_companies": [],
            "insight": "기술 혁신과 과학 발전의 근본적 동기는 과학자 개개인의 거대한 호기심과 지적 탐구 정신에 기반함.",
            "action_point": "과학 커뮤니케이션 및 융합 인재 육성의 중요성에 대한 교양적 이해."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["과학탐구", "동기부여", "안될과학", "꿈"]
        }
    },
    {
        "video": {
            "id": "MjgQfbxRKtY",
            "title": "\"나이 먹으니 살이 안 빠져요\" 몸이 제일 먼저 버린 '이것'",
            "published": "2026-08-02T10:00:20+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=MjgQfbxRKtY",
            "thumbnail": "https://img.youtube.com/vi/MjgQfbxRKtY/hqdefault.jpg"
        },
        "analysis": {
            "summary": "노화 진행에 따른 기초대사량 감소와 근육량 자발적 손실(근감소증)이 나잇살의 진짜 원인임을 의학적으로 해설함. 체중 감량 시 단순 단식이 아닌 <span class=\"text-cyan-300 font-semibold\">근육량 보존 및 단백질 섭취</span>가 대사 건강을 지키는 유일한 방법임을 강조함.",
            "key_claims": [
                "연령 증가 시 인체는 근육을 우선적으로 분해하여 기초 대사율을 저하시킴.",
                "근육 저하 방지 없는 다이어트는 대사율 낙폭을 키워 요요와 고혈당을 유발함."
            ],
            "data_points": [
                "30대 이후 10년당 평균 근육량 감소 비율: 약 3~8%"
            ],
            "signal": "na",
            "signal_reason": "노화 및 대사 의학 지식을 전달하는 의학/건강 숏폼 영상임.",
            "key_companies": [],
            "insight": "고령화 사회 진입에 따라 근감소증 치료제 및 고단백 헬스케어 식품 시장이 지속 성장할 거시적 사회 환경 반영.",
            "action_point": "헬스케어 및 근감소증 관련 항노화 바이오 부문의 트렌드를 지켜볼 것."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["근감소증", "노화", "기초대사량", "근육보존", "나잇살"]
        }
    },
    {
        "video": {
            "id": "NSiLb7YEfC8",
            "title": "중국 애들이 요즘 이상하다",
            "published": "2026-08-02T11:00:13+00:00",
            "channel_name": "Softdragon SOD",
            "url": "https://www.youtube.com/watch?v=NSiLb7YEfC8",
            "thumbnail": "https://img.youtube.com/vi/NSiLb7YEfC8/hqdefault.jpg"
        },
        "analysis": {
            "summary": "중국 내부 기술 기업들과 청년 노동력이 저비용 고효율 AI 소프트웨어 개발 및 <span class=\"text-cyan-300 font-semibold\">딥시크(DeepSeek)</span> 등 오픈소스 AI 생태계에 사활을 걸며 글로벌 빅테크의 독점에 파동을 일으키는 최신 테크 동향을 다룸. 미국 제재를 회피하기 위한 저비용 모델 혁신이 거세지고 있음.",
            "key_claims": [
                "중국 AI 씬은 고성능 GPU 부족을 소프트웨어 알고리즘 최적화 및 오픈소스 진영 결집으로 돌파하고 있음.",
                "딥시크 등 저비용 AI 모델의 등장으로 미국 빅테크의 API 가격 인하 치킨게임이 촉발됨."
            ],
            "data_points": [
                "중국 딥시크(DeepSeek) 모델 개발 비용: 미국 빅테크 대비 1/10 이하 수준"
            ],
            "signal": "neutral",
            "signal_reason": "중국의 오픈소스 AI 모델 추격이 인프라 비용 단가를 낮추는 긍정 효과와 빅테크 마진 압박이라는 위험을 동시 내포함.",
            "key_companies": ["딥시크(DeepSeek)", "엔비디아(NVDA)", "텐센트", "알리바바"],
            "insight": "미국의 미세 공정 규제가 역설적으로 중국 개발자들로 하여금 모델 경량화 및 오픈소스 효율 혁신을 가속화시키게 만듦.",
            "action_point": "오픈소스 모델 확산으로 인한 클라우드 토큰 단가 인하 및 온디바이스 AI 응용 소프트웨어 기업들의 기회를 포착."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock", "economy"],
            "tags": ["중국AI", "딥시크", "오픈소스AI", "DeepSeek", "테크혁신"]
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
    save_batch(batch3)
