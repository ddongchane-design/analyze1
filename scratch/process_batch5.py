import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch5_data = [
    # 21. OOcs0iDXKZk - 국채금리 상승 빅테크 강세 미증시 (stock / tech)
    {
        "id": "OOcs0iDXKZk",
        "analysis": {
            "summary": "미국 10년물 국채 금리 상승에도 불구하고 <span class=\"text-cyan-300 font-semibold\">빅테크 실적 기대감</span>이 뉴욕 증시 상승을 이끈 월가 시황을 정리함. <span class=\"text-cyan-300 font-semibold\">아마존</span>과 <span class=\"text-cyan-300 font-semibold\">팔란티어</span>의 견고한 실적 발표가 국채 금리 부담을 상쇄하며 기술주 중심 반등세를 끌어냄.",
            "key_claims": [
                "국채 금리가 4.0% 선을 위협했으나 빅테크 이익 모멘텀이 금리 상승 압력을 압도함.",
                "AI 실적 가시성이 확보된 기업 위주로 숏커버링 매수세 유입."
            ],
            "data_points": [
                "미국 10년물 국채 금리: 3.98%~4.02% 변동",
                "나스닥 지수: 전일 대비 1.2% 상승 마감"
            ],
            "signal": "bullish",
            "signal_reason": "금리 상승에도 양호한 빅테크 실적이 증시 연착륙 및 랠리를 지지함.",
            "key_companies": ["아마존(AMZN)", "팔란티어(PLTR)", "애플(AAPL)", "엔비디아(NVDA)"],
            "insight": "금리가 높아지더라도 현금 유보율이 높고 AI 이익 성장을 입증한 빅테크는 금리 국면을 우회하는 독주 체제를 구축함.",
            "action_point": "국채 금리 상방 압력에도 버티는 펀더멘털 우량 빅테크 위주의 포트폴리오를 유지할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["국채금리", "빅테크강세", "나스닥상승", "팔란티어", "미래에셋"]
        }
    },
    # 22. Pfu8rWMGwoQ - 반도체 다 팔지 마라 하반기 대형주 (stock / tech)
    {
        "id": "Pfu8rWMGwoQ",
        "analysis": {
            "summary": "반도체 주가 조정 시 전량 매도하는 성급함을 경계하며, 하반기 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span> 및 <span class=\"text-cyan-300 font-semibold\">삼성전자</span> 비중을 고수한 채 포트폴리오 균형을 맞추는 바벨 전략을 제안함. <span class=\"text-amber-300 font-bold\">방산·조선·바이오</span> 등 대체 주도주를 결합한 분산 투자가 유효함.",
            "key_claims": [
                "반도체 사이클은 끝나지 않았으며 사이클 중간의 일시적 주가 과열 해소 과정임.",
                "하반기 포트폴리오 안정화를 위해 반도체+방산/조선/금융주 조합의 자산 배분 제안."
            ],
            "data_points": [
                "SK하이닉스 HBM3E 분기 출하량 역대 최대 기록",
                "하반기 방산/조선 업종 수주 잔고 사상 최대 경신 중"
            ],
            "signal": "bullish",
            "signal_reason": "반도체 펀더멘털 지속 우상향 판단 및 하반기 주도주 조합을 통한 이익 안정성 확보.",
            "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "한화에어로스페이스(012450)", "HD한국조선해양(009540)"],
            "insight": "반도체를 다 파는 극단적 투자는 지양해야 하며, 반도체 대장주를 중심에 두고 방산과 조선을 믹스하는 균형 전략이 승률을 높임.",
            "action_point": "반도체 보유 비중을 40~50% 유지하되 남은 비중을 방산 및 실적 개선주로 포트폴리오 리밸런싱."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "shipbuilding"],
            "tags": ["반도체매도금지", "SK하이닉스", "바벨전략", "방산주", "오늘의주식"]
        }
    },
    # 23. SuxZtr5qh6A - 스페이스X 시총 40조달러 팔란티어 (stock / space)
    {
        "id": "SuxZtr5qh6A",
        "analysis": {
            "summary": "스페이스X의 장기 시가총액 추정치(최대 40조 달러 논의)와 실적 공개 파장, 그리고 <span class=\"text-cyan-300 font-semibold\">팔란티어</span>의 시간외 12% 폭등 어닝 서프라이즈를 심층 다룸. <span class=\"text-cyan-300 font-semibold\">M7 빅테크 기업들</span>이 실적 발표 후 주가 재정비 과정을 거치며 질주를 시작함.",
            "key_claims": [
                "스페이스X 스타링크 및 Starship 사업의 성장성이 구글 및 테슬라를 넘어서는 평가 유도.",
                "팔란티어의 수주 잔고 폭증이 공공·B2B AI 시장의 실질적 폭발을 증명함."
            ],
            "data_points": [
                "스페이스X 기업가치 장기 전망치 40조 달러 시나리오 제시",
                "팔란티어(PLTR) 2분기 매출 전년 대비 27% 증가 및 시간외 12% 폭등"
            ],
            "signal": "bullish",
            "signal_reason": "우주 기술 및 AI 실적주들의 압도적 성장 지표 확인에 따른 강력한 강세장 유지.",
            "key_companies": ["스페이스X", "팔란티어(PLTR)", "테슬라(TSLA)", "엔비디아(NVDA)"],
            "insight": "미래 기술의 두 축인 우주 네트워크(스페이스X)와 엔터프라이즈 AI(팔란티어)가 기대를 현실 숫자로 가시화하고 있음.",
            "action_point": "팔란티어 및 우주항공 연관 테슬라 밸류체인 수혜주의 눌림목 매수 타깃 설정."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["space", "tech"],
            "tags": ["스페이스X40조달러", "팔란티어어닝서프라이즈", "M7질주", "스타링크", "빅머니LIVE"]
        }
    },
    # 24. Sx4pdZmml4Q - 삼전닉스국민연금 코스피 기능별자산배분 (stock / economy)
    {
        "id": "Sx4pdZmml4Q",
        "analysis": {
            "summary": "삼성전자, SK하이닉스, 그리고 국민연금의 대규모 수급 흔들기로 코스피 변동성이 극대화된 상황에서 개인 투자자가 생존하는 핵심 투자법으로 <span class=\"text-amber-300 font-bold\">기능별 자산배분</span>을 제시함. 자산을 공격형(반도체/AI), 방어형(고배당/채권), 현금성 버퍼로 구분해 운용해야 함.",
            "key_claims": [
                "국민연금의 포트폴리오 리밸런싱 매도와 대형주 쏠림 현상이 지수 변동성을 증폭시킴.",
                "단일 종목이나 단일 섹터에 몰빵하지 않고 기능별(성장/소득/안정)로 리밸런싱해야 살아남음."
            ],
            "data_points": [
                "국민연금 코스피 비중 조절 매매 규모: 월간 조 단위 수급 변동 유발",
                "기능별 자산배분 적용 시 연 변동성 30% 이상 감소 효과"
            ],
            "signal": "neutral",
            "signal_reason": "대형주 수급 쏠림과 기관 매매로 인한 장세 변동성 우려에 따른 중립적 배분 추천.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "KB금융(105560)"],
            "insight": "기관과 외국인의 거대한 수급 폭풍 속에서 개인 투자자의 최고 무기는 계좌의 무기화(기능별 자산배분)를 통한 리스크 분산임.",
            "action_point": "전체 계좌를 성장성(반도체 40%), 안정성(고배당주 30%), 현금 버퍼(30%)로 나누어 장기 리밸런싱 가동."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["자산배분", "국민연금수급", "삼성전자", "SK하이닉스", "이효석아카데미"]
        }
    },
    # 25. TzaGQbc6Ih4 - The Next Question for AI 8월자산배분 (stock / tech)
    {
        "id": "TzaGQbc6Ih4",
        "analysis": {
            "summary": "2026년 8월 리테일 고객 자산배분 가이드로서 <span class=\"text-cyan-300 font-semibold\">AI 랠리의 다음 질문(The Next Question for AI)</span>에 답하는 전략을 수립함. 단순 칩 제조업체 중심 투자를 넘어 AI 응용 서비스, 전력망 인프라, 그리고 금융주와의 균형 잡힌 <span class=\"text-amber-300 font-bold\">자산배분 포트폴리오</span> 구축을 권고함.",
            "key_claims": [
                "AI 투자 패러다임이 하드웨어 칩 독주에서 융합 인프라 및 소프트웨어 실적주로 확대.",
                "고금리 장기화 대응을 위한 고배당 금융주 및 미국 채권 결합 포트폴리오 추천."
            ],
            "data_points": [
                "2026년 8월 추천 포트폴리오 비중: AI 인프라 40%, 고배당/금융 30%, 현금 30%",
                "미국 빅테크 인프라 소프트웨어 영업이익률 전년비 5%p 상승"
            ],
            "signal": "bullish",
            "signal_reason": "AI 확산에 따른 주도주 다변화 및 8월 포트폴리오 리밸런싱 호재 반영.",
            "key_companies": ["엔비디아(NVDA)", "팔란티어(PLTR)", "신한지주(055550)"],
            "insight": "8월 투자 전략의 핵심은 'AI의 다음 단계가 무엇인가'에 답할 수 있는 실적주와 채권/현금 버퍼의 동시 구축임.",
            "action_point": "가이드라인에 따라 보유 자산 중 불확실한 중소형주를 줄이고 AI 인프라와 배당주로 배분 조정."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["자산배분가이드", "AI다음질문", "8월전략", "포트폴리오", "미래에셋"]
        }
    }
]

def run():
    for item_data in batch5_data:
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
