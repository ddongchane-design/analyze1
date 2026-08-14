import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch6_data = [
    # 26. UiaxTZ88WhM - 로보티즈 재평가 유니트리 21조 충격 (robot / tech)
    {
        "id": "UiaxTZ88WhM",
        "analysis": {
            "summary": "중국 휴머노이드 로봇 기업 <span class=\"text-cyan-300 font-semibold\">유니트리(Unitree)</span>의 기업가치 21조 원 평가 충격 속에서 국내 로봇 액추에이터 및 감속기 전문기업 <span class=\"text-cyan-300 font-semibold\">로보티즈</span>의 본격 재평가 모멘텀을 파헤침. 피지컬 AI와 감속기/모터 부품의 국산화 수요가 <span class=\"text-amber-300 font-bold\">휴머노이드 로봇 생태계</span>의 핵으로 부상 중임.",
            "key_claims": [
                "유니트리의 초고평가는 휴머노이드 로봇 산업이 실험실을 벗어나 대량 양산 단계로 진입했음을 입증함.",
                "로보티즈의 자율주행 로봇 및 초소형 감속기/액추에이터 기술력이 글로벌 밸류체인 재평가를 이끔."
            ],
            "data_points": [
                "중국 유니트리(Unitree) 기업가치: 약 21조 원(150억 달러 이상) 인정 논의",
                "로보티즈 액추에이터 매출 성장률: 전년 대비 40% 이상 가속"
            ],
            "signal": "bullish",
            "signal_reason": "휴머노이드 로봇 밸류에이션 급등에 따른 국내 핵심 로봇 부품주 재평가 강한 호재 작용.",
            "key_companies": ["로보티즈(108860)", "유니트리", "레인보우로보틱스(277810)", "두산로보틱스(454910)"],
            "insight": "휴머노이드 로봇은 AI의 소프트웨어가 물리적 몸체(액추에이터/감속기)를 입는 완성형이며, 핵심 부품 기업의 재평가가 시작됨.",
            "action_point": "로보티즈 및 국내 감속기/액추에이터 기술을 보유한 핵심 로봇 부품주의 눌림목 저점 매수."
        },
        "classification": {
            "primary_topic": "robot",
            "secondary_topics": ["tech", "stock"],
            "tags": ["로보티즈", "유니트리", "휴머노이드", "액추에이터", "엔지니어TV"]
        }
    },
    # 27. V7E0WTylYhc - 대혼돈 7월 주식시장 줄여야 할 것 (stock / economy)
    {
        "id": "V7E0WTylYhc",
        "analysis": {
            "summary": "7월 주식시장의 극심한 혼돈과 변동성을 겪은 투자자들에게 당장 줄여야 할 요소로 <span class=\"text-rose-400 font-medium\">과도한 부채(신용/레버리지)</span>와 <span class=\"text-rose-400 font-medium\">뇌동매매 잦은 매매 횟수</span>를 지목함. 신환종 박사가 제안하는 원금 보존과 안정적 이익을 달성하는 자산 리밸런싱 전략을 제시함.",
            "key_claims": [
                "변동성 장세에서 망하는 지름길은 레버리지를 늘려 한 번에 원금을 복구하려는 욕심임.",
                "포트폴리오 내 현금 비중을 늘리고 포모(FOMO) 현상에 쏠린 테마주 추격 매수를 중단해야 함."
            ],
            "data_points": [
                "개인 투자자 신용 융자 반대매매 계좌 수: 7월 말 급증 기록",
                "자산배분 포트폴리오의 최악 하락률(MDD) 방어력: 단일 종목 대비 50% 이상 우수"
            ],
            "signal": "neutral",
            "signal_reason": "위험 관리 우선 강조 및 과도한 레버리지 줄이기를 통한 계좌 안정화 국면 제안.",
            "key_companies": [],
            "insight": "하락장에서 살아남는 자가 결국 다음 상승장의 결실을 독식하며, 계좌 멸망을 막는 최고의 방패는 현금성 자산과 채권 버퍼임.",
            "action_point": "신용 융자를 완전히 상환하고 계좌 내 현금 비중을 최소 20~30%로 늘려 안정성 확보."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["위험관리", "레버리지줄이기", "자산배분", "하락장생존", "이효석아카데미"]
        }
    },
    # 28. XHoSgDrdkAA - 클래리티 법 윤리 수정안 크립토 (crypto / economy)
    {
        "id": "XHoSgDrdkAA",
        "analysis": {
            "summary": "미국 의회 통과를 앞둔 <span class=\"text-violet-300 font-medium\">가상자산 클래리티 법안(Clarity Act)</span>에 윤리 수정안 및 SEC-CFTC 관할권 새 변수가 등장함에 따른 암호화폐 시장 파장을 심층 다룸. 규제 명확화 호재와 윤리 심사 규제 강화 변수가 <span class=\"text-cyan-300 font-semibold\">비트코인 및 알트코인 수급</span>을 흔들고 있음.",
            "key_claims": [
                "클래리티 법 통과 시 가상자산의 법적 지위가 명확해져 기관 자금 유입 가속화 가능.",
                "윤리 수정안 추가로 개별 규제 당국의 승인 절차가 복잡해질 단기 변수 발생."
            ],
            "data_points": [
                "비트코인(BTC) 6만5천 달러 선 공방 및 기관 ETF 유입액 지표",
                "미국 의회 가상자산 입법 표결 일정 점검"
            ],
            "signal": "neutral",
            "signal_reason": "법안 통과 기대감과 수정안에 따른 지연 불확실성이 교차하는 매크로 팽팽한 국면.",
            "key_companies": ["코인베이스(COIN)", "마이크로스트래티지(MSTR)"],
            "insight": "가상자산 시장의 제도권 진입은 거스를 수 없는 대세이나, 법안 세부 수정안의 문구 하나가 단기 수급 폭풍을 부를 수 있음.",
            "action_point": "미국 법안 표결 진행 상황을 모니터링하며 비트코인 및 이더리움 중심의 대장주 위주로 매매 한정."
        },
        "classification": {
            "primary_topic": "crypto",
            "secondary_topics": ["economy", "stock"],
            "tags": ["클래리티법", "가상자산규제", "비트코인", "크립토PLUS", "디지털애셋"]
        }
    },
    # 29. XmK7mpuhfUo - 26.08.03 오전 뉴욕증시 아마존 애플 (stock / tech)
    {
        "id": "XmK7mpuhfUo",
        "analysis": {
            "summary": "8월 3일 뉴욕증시가 AI 투자 우려를 털어내고 상승 마감한 풀 시황을 다룸. 클라우드 및 AI 매출 호조를 기록한 <span class=\"text-cyan-300 font-semibold\">아마존(+15%)</span>이 폭등한 반면, 아이폰 중국 판매 둔화 우려가 작용한 <span class=\"text-cyan-300 font-semibold\">애플(-7%)</span>은 하락하여 빅테크 간 뚜렷한 양극화가 펼쳐짐.",
            "key_claims": [
                "AWS 클라우드 매출 성장 재가속이 아마존 주가를 15% 폭등시키는 원동력이 됨.",
                "애플은 중화권 실적 약세와 AI 서비스 출시 지연 우려로 주가 차별화 하락."
            ],
            "data_points": [
                "아마존(AMZN) 주가: 당일 +15% 폭등 마감",
                "애플(AAPL) 주가: 당일 -7% 급락 마감",
                "나스닥 종합지수: +1.5% 상승 마감"
            ],
            "signal": "bullish",
            "signal_reason": "아마존의 호실적으로 AI 클라우드 실적 우려 해소 및 증시 반등 동력 확보.",
            "key_companies": ["아마존(AMZN)", "애플(AAPL)", "엔비디아(NVDA)", "마이크로소프트(MSFT)"],
            "insight": "빅테크 묶음 투자의 시대는 갔으며, 클라우드와 AI 가속기 실적을 직접 내는 아마존·엔비디아와 그렇지 못한 기업 간의 주가 엇갈림이 심화됨.",
            "action_point": "아마존 및 AI 클라우드 CapEx 수혜가 직접 연동되는 반도체/서버 부품주 위주의 선별 매수."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["오전증시", "아마존폭등", "애플급락", "뉴욕증시", "삼프로TV"]
        }
    },
    # 30. ZZ09tf_FNr8 - 26.08.03 오후 코스피 폭등후유증 급락 (stock / economy)
    {
        "id": "ZZ09tf_FNr8",
        "analysis": {
            "summary": "8월 3일 국내 증시가 전일 사상 최대 폭등 후유증으로 하루 만에 급락한 오후 마감 시황을 방송 전체보기로 정리함. <span class=\"text-rose-400 font-medium\">외국인 선물/현물 동시 매도</span>와 엔화 강세 기류가 복합 작용하여 지수 하락 압력을 가했으며 이번 주 증시의 핵심 관건을 제시함.",
            "key_claims": [
                "폭등 직후 나타난 차익 실현 물량과 외환 시장 엔화 변동성이 한국 증시의 걸림돌로 작용.",
                "삼성전자 및 SK하이닉스의 하단 지지선 확인과 미국 옵션 만기일 수급이 이번 주 분수령."
            ],
            "data_points": [
                "코스피 지수 하락 폭: 전일 상승분 중 일부 반납 (약 2.4% 하락)",
                "외국인 거래소 순매도: 6,000억 원 상회"
            ],
            "signal": "bearish",
            "signal_reason": "폭등 후유증 차익 실현과 엔화 환율 변동성에 따른 단기 변동성 확대 장세.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "LG에너지솔루션(373220)"],
            "insight": "사상 최대 폭등 후 급락은 전형적인 변동성 장세의 특징이며, 펀더멘털 손상이 아니므로 저점 매수자에게는 진입 기회를 제공함.",
            "action_point": "이번 주 외국인 수급의 매도세 진정 여부를 확인하고 반도체 대장주 지지선 부근 분할 매수."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["오후증시", "폭등후유증", "코스피급락", "외국인매도", "삼프로TV"]
        }
    }
]

def run():
    for item_data in batch6_data:
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
