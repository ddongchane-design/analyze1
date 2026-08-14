import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch3_data = [
    # 11. F-XdAjbA1JQ - 8월 첫 거래일 빅테크 데이 (stock / tech)
    {
        "id": "F-XdAjbA1JQ",
        "analysis": {
            "summary": "8월 첫 거래일을 맞아 뉴욕증시에서 진행된 <span class=\"text-cyan-300 font-semibold\">빅테크 실적 데이</span>의 시장 파장과 업종별 주가 향방을 종합 분석함. <span class=\"text-cyan-300 font-semibold\">팔란티어</span>의 어닝 서프라이즈와 스페이스X의 긍정적 이익 지표가 호재로 작용했으나 기술주 전반의 변동성은 상존함.",
            "key_claims": [
                "팔란티어의 AIP 플랫폼 매출 급증이 B2B AI 실적 가시성을 입증함.",
                "빅테크 간 실적 차별화(아마존 상승 vs 애플 보합)로 인한 개별 종목 장세 심화."
            ],
            "data_points": [
                "팔란티어(PLTR) 시간외 거래 12% 이상 폭등",
                "아마존(AMZN) 실적 발표 후 주가 15% 상승 기록"
            ],
            "signal": "bullish",
            "signal_reason": "AI 관련 대표기업들의 실적 확인을 통해 펀더멘털 기반 상방 모멘텀이 재차 확인됨.",
            "key_companies": ["팔란티어(PLTR)", "아마존(AMZN)", "애플(AAPL)", "스페이스X"],
            "insight": "AI 투자는 막연한 기대감 단계에서 실제 매출과 이익으로 증명하는 2라운드 실적 장세로 전환됨.",
            "action_point": "B2B 엔터프라이즈 AI 매출 성장을 입증한 팔란티어 및 하이퍼스케일러 핵심 수혜주 중심으로 포트폴리오 재편."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "space"],
            "tags": ["빅테크데이", "팔란티어", "아마존", "실적장세", "미래에셋"]
        }
    },
    # 12. FLG912fnsuE - 워렌버핏 공부없는 투자는 없다 (stock / economy)
    {
        "id": "FLG912fnsuE",
        "analysis": {
            "summary": "워렌 버핏의 투자 철학을 바탕으로 극심한 <span class=\"text-rose-400 font-medium\">증시 변동성 장세</span>에서 기업의 내재 가치 및 현금 창출 능력을 정밀 분석하는 투자 원칙을 제시함. 철저한 기업 분석과 밸류체인 공부 없는 투자는 단순한 투기에 불과함을 경고함.",
            "key_claims": [
                "워렌 버핏 역시 매일 기업 재무제표와 현금흐름 보고서를 정독하며 학습을 게을리하지 않음.",
                "시장의 소음과 쏠림 현상에 휩쓸리지 않고 안전지대(Margin of Safety)를 확보해야 함."
            ],
            "data_points": [
                "버크셔 해서웨이 가용 현금성 자산: 역대 최대 수준 보유 중",
                "닷컴 버블 및 금융위기 당시 버핏의 매수 타임 정밀 분석"
            ],
            "signal": "bullish",
            "signal_reason": "하락장 및 조정을 좋은 우량 기업을 싸게 살 수 있는 저점 매수 기회로 활용할 것을 권장.",
            "key_companies": ["버크셔해서웨이(BRK.A)", "애플(AAPL)"],
            "insight": "주가가 떨어질 때 공포에 질려 도망치는 것이 아니라, 가치 대비 저평가된 훌륭한 주식을 주울 수 있는 자산 재분배의 기회임.",
            "action_point": "현금 비중을 일정 유지하면서 확신이 있는 대형 우량주의 저점 분할 매수 리스트를 작성할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["워렌버핏", "가치투자", "기업분석", "저점매수", "교양이를부탁해"]
        }
    },
    # 13. FvQF06brkAQ - AI 랠리 2라운드 승부는 실적 (stock / space)
    {
        "id": "FvQF06brkAQ",
        "analysis": {
            "summary": "뉴욕증시의 AI 랠리가 <span class=\"text-cyan-300 font-semibold\">실적 확인 국면</span>으로 접어든 가운데, <span class=\"text-cyan-300 font-semibold\">스페이스X</span>의 첫 실적 공개와 엔화 가치 안정을 위한 트럼프 및 미-일 외환 공조 기류를 브리핑함. 머스크의 우주·AI 생태계 확장과 일본 엔화 방어 작전이 시장의 새로운 방향성을 좌우함.",
            "key_claims": [
                "스페이스X 실적 수치 공개는 민간 우주산업 밸류에이션 재평가의 분수령이 됨.",
                "트럼프의 엔화 방어 지원 발언이 미-일 환율 개입 가능성을 높이며 엔화 급락을 일시 저지함."
            ],
            "data_points": [
                "스페이스X 2026년 가동 실적 매출 발표",
                "엔/달러 환율 트럼프 발언 직후 하락 반전"
            ],
            "signal": "bullish",
            "signal_reason": "빅테크 및 민간 우주 기업들의 실제 실적 호조와 환율 불안 완화 기조가 호재로 작동.",
            "key_companies": ["스페이스X", "테슬라(TSLA)", "팔란티어(PLTR)"],
            "insight": "AI 랠리는 단순한 기대감 폭발에서 민간 우주산업과 결합된 실질적 현금 창출력 검증 단계로 업그레이드됨.",
            "action_point": "우주항공 및 AI 플랫폼 기업의 실적 지표를 확인하며 밸류체인 핵심주 위주로 매수 대응."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["space", "economy"],
            "tags": ["AI실적랠리", "스페이스X", "엔화방어", "트럼프", "뉴욕브리핑"]
        }
    },
    # 14. G6qGr2BxYbQ - AI 투자를 흔드는 다음 경고 신호 (economy / stock)
    {
        "id": "G6qGr2BxYbQ",
        "analysis": {
            "summary": "AI 투자를 위축시킬 수 있는 <span class=\"text-rose-400 font-medium\">다음 매크로 경고 신호</span>로 미국 빅테크 CapEx 증가율 둔화, 전력망 부족에 따른 데이터센터 착공 지연, 그리고 <span class=\"text-rose-400 font-medium\">미국 경기 둔화 우려</span>를 삼프로TV 이코노미스트가 정밀 진단함.",
            "key_claims": [
                "AI 데이터센터 확장 속도가 글로벌 전력 기지 구축 및 변압기 공급 한계에 부딪히고 있음.",
                "미국 실업률 상승 및 소비 심리 위축이 빅테크 기업들의 광고 및 클라우드 매출에 불확실성 부여."
            ],
            "data_points": [
                "미국 전력망 대기 순번 및 변압기 리드타임: 3~4년 소요",
                "2026년 하반기 미국 ISM 제조업 지수 및 고용 지표 약세"
            ],
            "signal": "neutral",
            "signal_reason": "AI 기술의 장기 잠재력은 명확하나 병목 요인(전력/매크로)에 의한 단기 숨고르기 장세 예상.",
            "key_companies": ["엔비디아(NVDA)", "GE버노바(GEV)", "HD현대일렉트릭(267260)"],
            "insight": "AI 투자의 실질적 병목은 이제 반도체 칩 부족이 아닌 '전력 인프라(변압기/전력망)'와 '매크로 경기 침체 여부'로 옮겨짐.",
            "action_point": "전력망 관련 수혜주(변압기, 수냉 쿨링)의 눌림목 매수와 함께 금리 인하 수혜주에 대한 균형 잡힌 접근."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock", "energy"],
            "tags": ["AI경고신호", "전력망병목", "매크로진단", "CapEx둔화", "여의도인사이트"]
        }
    },
    # 15. HJxQSYD3pyQ - CXMT 공포 과장 반도체 경고 (tech / stock)
    {
        "id": "HJxQSYD3pyQ",
        "analysis": {
            "summary": "중국 반도체 기업 <span class=\"text-cyan-300 font-semibold\">CXMT</span>의 레거시 D램 물량 공세 공포가 시장에서 과장되었음을 28년차 반도체 전문 센터장의 정밀 조사를 통해 입증함. 미국의 첨단 반도체 장비 통제로 중국으로의 고급 장비 유입이 차단된 상태이며, 한국의 <span class=\"text-cyan-300 font-semibold\">HBM 및 DDR5</span> 주도권은 견고함.",
            "key_claims": [
                "CXMT 등 중국 업체의 생산 능력 확대는 범용 레거시(DDR4 이하)에 국한되며 첨단 HBM 영역 침투 불가.",
                "미국 극자외선(EUV) 및 노광 장비 제재가 효과적으로 작용하여 중국의 기술 추격 속도가 현저히 제한됨."
            ],
            "data_points": [
                "CXMT의 글로벌 D램 시장 점유율: 레거시 위주 5% 내외",
                "HBM 시장 내 한국 기업(SK하이닉스, 삼성전자) 합산 점유율: 90% 이상"
            ],
            "signal": "bullish",
            "signal_reason": "중국 반도체 위협론에 따른 한국 메모리 반도체 주가의 과도한 조정은 매수 기회임.",
            "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "ASML(ASML)"],
            "insight": "중국 반도체 공포는 펀더멘털을 반영하지 못한 헛소문성 소음이며, 고성능 HBM을 쥐고 있는 국내 메모리 대장주들의 기술 격차는 확고함.",
            "action_point": "CXMT 공포로 주가가 과도하게 하락할 때 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>와 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>를 적극 저점 매수하는 전략 권장."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock"],
            "tags": ["CXMT공포", "반도체장비제재", "SK하이닉스", "삼성전자", "HBM선점"]
        }
    }
]

def run():
    for item_data in batch3_data:
        vid = item_data["id"]
        pending_path = Path(f"data/pending/{vid}.json")
        if not pending_path.exists():
            print(f"Pending file {vid} not found!")
            continue
        raw = json.loads(pending_path.read_text(encoding="utf-8"))
        video_obj = raw["video"]
        
        full_item = {
            "video": video_obj,
            "analysis": item_data["analysis"],
            "classification": item_data["classification"]
        }
        
        valid, errors = validate_item(full_item)
        if not valid:
            print(f"Validation failed for {vid}: {errors}")
            continue
            
        primary = item_data["classification"]["primary_topic"]
        out_dir = Path(f"data/analyzed/{primary}")
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{vid}.json"
        
        out_file.write_text(json.dumps(full_item, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[SUCCESS] Saved {out_file}")
        pending_path.unlink()
        print(f"[DELETED] {pending_path}")

if __name__ == "__main__":
    run()
