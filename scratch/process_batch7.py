import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch7_data = [
    # 31. a5ImJQLXB6w - 크립토 시장 4가지 변화 (crypto / stock)
    {
        "id": "a5ImJQLXB6w",
        "analysis": {
            "summary": "2026년 암호화폐 시장의 4가지 핵심 구조적 변화로 <span class=\"text-violet-300 font-medium\">미국 입법 명확화</span>, 비트코인 래핑 자산 증가, <span class=\"text-cyan-300 font-semibold\">실물 자산 토큰화(RWA)</span>, 그리고 기관 채권 연계 상품의 확산을 조명함. 제도권 자금 수입구 확충이 크립토 장기 생존의 밑거름이 되고 있음.",
            "key_claims": [
                "미국 법안 통과 수순으로 비트코인과 이더리움 중심의 기관 포트폴리오 편입 가속.",
                "RWA(실물자산 토큰화) 시장 급성장이 기존 전통 금융과의 경계를 무너뜨림."
            ],
            "data_points": [
                "글로벌 RWA 운용 자산 규모: 약 100억 달러 수평 돌파",
                "기관용 비트코인 수탁(Custody) 자금 유입액 사상 최대 경신"
            ],
            "signal": "bullish",
            "signal_reason": "제도화 진행과 실물 자산 토큰화(RWA) 시장 팽창에 따른 구조적 호재 반영.",
            "key_companies": ["코인베이스(COIN)", "블랙록(BLK)"],
            "insight": "크립토 투자는 더 이상 투기성 밈코인이 아니라 전통 금융의 국채 및 부동산 자산과 결합하는 신금융 인프라로 체질 개선됨.",
            "action_point": "RWA 및 비트코인 현물 ETF 우량 수혜 기관 중심의 장기 가치 저장 수단 비중 확대."
        },
        "classification": {
            "primary_topic": "crypto",
            "secondary_topics": ["stock", "economy"],
            "tags": ["크립토변화", "RWA", "비트코인제도화", "미국법안", "크립토PLUS"]
        }
    },
    # 32. iDry02aKBsY - 팔란티어 실적 스페이스X 보호예수 (stock / space)
    {
        "id": "iDry02aKBsY",
        "analysis": {
            "summary": "개장 전 미국 증시 쟁점으로 <span class=\"text-cyan-300 font-semibold\">팔란티어</span>의 높은 밸류에이션 부담에 따른 실적 발표 후 주가 반응과 <span class=\"text-cyan-300 font-semibold\">스페이스X</span>의 공매도·보호예수 관련 시장 기류를 점검함. 호실적 발표에도 시장 눈높이에 따라 주가 흔들림이 나타날 수 있음을 경고함.",
            "key_claims": [
                "팔란티어는 고PER 주식 특성상 실적 발표 시 시장 기대를 크게 뛰어넘어야 주가 상승 유지.",
                "스페이스X는 락업(보호예수) 해제 물량 부담에도 장기 이익 성장 기대감이 주가 상방 지지."
            ],
            "data_points": [
                "팔란티어 선행 PER: 70배 이상 유지",
                "스페이스X 스타링크 2분기 가입자 수 400만 명 육박"
            ],
            "signal": "neutral",
            "signal_reason": "실적 성장세는 입증되었으나 높은 밸류에이션에 따른 개장 전 변동성 상존.",
            "key_companies": ["팔란티어(PLTR)", "스페이스X", "테슬라(TSLA)"],
            "insight": "밸류에이션이 높은 초우량 성장주는 실적 서프라이즈 후의 차익 실현 변동성을 견뎌내는 배짱이 필요한 구역임.",
            "action_point": "개장 전 변동성으로 급락 시 펀더멘털을 확인한 후 눌림목 진입 타이밍으로 활용."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["space", "tech"],
            "tags": ["팔란티어실적", "스페이스X보호예수", "개장전요것만", "미국증시", "한경글로벌"]
        }
    },
    # 33. jUhsBTSZLOc - 팔란티어 급등 다우 사상최고치 (stock / tech)
    {
        "id": "jUhsBTSZLOc",
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">팔란티어</span>가 B2B AI 실적 랠리에 힘입어 시간외 12% 급등하고 <span class=\"text-amber-300 font-bold\">다우 지수가 사상 최고치</span>를 경신한 월가 호재를 상세 타전함. AI 수익화 가능성이 가시화되면서 증시 전반에 연착륙 및 강세장 열기가 재확산됨.",
            "key_claims": [
                "팔란티어의 AIP 플랫폼 고객 수가 30% 이상 폭증하며 수익성 증대를 증명함.",
                "다우 지수의 사상 최고치 경신은 빅테크 외 전통 제조/금융주로의 온기 확산을 의미."
            ],
            "data_points": [
                "팔란티어(PLTR) 시간외 거래: 12% 폭등 기록",
                "다우존스 산업평균지수: 사상 최고치 경신 마감"
            ],
            "signal": "bullish",
            "signal_reason": "팔란티어의 강력한 어닝 서프라이즈와 다우지수 신고가 경신이 시장 투심을 전면 개선시킴.",
            "key_companies": ["팔란티어(PLTR)", "골드만삭스(GS)", "마이크로소프트(MSFT)"],
            "insight": "AI 랠리는 더 이상 뜬구름 잡는 거품이 아니며, 팔란티어처럼 실질적 매출과 이익을 가시화하는 기업이 시장을 사상 최고치로 인도함.",
            "action_point": "AI 수익화가 입증된 팔란티어 및 관련 B2B AI 소프트웨어 대장주 매수 유지."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["팔란티어급등", "다우사상최고치", "월가뉴스레터", "AI수익화", "삼프로TV"]
        }
    },
    # 34. mXJn3NfqboA - 시장 국면 판단 대응 월스트리트파인더 (stock / economy)
    {
        "id": "mXJn3NfqboA",
        "analysis": {
            "summary": "8월 현재 글로벌 금융 시장 국면을 <span class=\"text-amber-300 font-bold\">실적 장세 과도기</span> 및 연준 금리 인하 기대감이 교차하는 중기 횡보 구간으로 진단함. 주가 조정을 공포로 보지 않고 <span class=\"text-cyan-300 font-semibold\">핵심 펀더멘털 대형주 저점 매수</span>의 국면 대응 전략을 월가 분석가를 통해 소개함.",
            "key_claims": [
                "현재 시장은 밸류에이션 부담 완화 과정에 있으며 실적 모멘텀이 살아있는 한 강세장 기조 유지.",
                "미국 연준의 금리 인하 재개가 다가옴에 따라 채권 및 기술주 동시 혜택 가능성."
            ],
            "data_points": [
                "월스트리트 주요 IB 2026년 하반기 S&P 500 타깃 지수 상향",
                "연준 FedWatch 9월 금리 인하 가능성 80% 상회"
            ],
            "signal": "bullish",
            "signal_reason": "시장 국면이 침체가 아닌 이익 성장의 소화 과정이며 금리 인하 수혜 기대 반영.",
            "key_companies": ["엔비디아(NVDA)", "아마존(AMZN)", "애플(AAPL)"],
            "insight": "시장의 변동성은 펀더멘털이 훼손된 것이 아니라 실적 상승에 맞춰 주가 숨고르기를 진행하는 정상적인 국면 진통임.",
            "action_point": "주가 조정 시 도망치지 말고 반도체 및 빅테크 우량주 저점 분할 매수 대응 전략 실행."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy", "tech"],
            "tags": ["시장국면판단", "월스트리트파인더", "저점매수대응", "금리인하", "미래에셋"]
        }
    },
    # 35. qxm9hQ2zPfk - 삼전닉스 들어가실 분 필수 시청 (stock / tech)
    {
        "id": "qxm9hQ2zPfk",
        "analysis": {
            "summary": "삼성전자와 SK하이닉스 매수를 고민하는 투자자들에게 필수적인 <span class=\"text-cyan-300 font-semibold\">HBM 수율 및 3분기 실적 가이던스</span> 판단 기준을 정밀 제시함. 단기 주가 흔들림에도 불구하고 <span class=\"text-amber-300 font-bold\">메모리 반도체 슈퍼사이클</span>의 중심 축은 흔들리지 않음을 강조함.",
            "key_claims": [
                "삼성전자의 HBM3E 8단/12단 퀄테스트 통과 여부가 하반기 주가 갭상승의 핵심 트리거임.",
                "SK하이닉스의 HBM3E 독점적 점유율과 사상 최대 영업이익 체력은 하단을 공고히 지지함."
            ],
            "data_points": [
                "SK하이닉스 3분기 영업이익 추정치: 6조 원 이상 경신 전망",
                "삼성전자 DS부문 이익 개선 폭 전년비 200% 이상 급증"
            ],
            "signal": "bullish",
            "signal_reason": "삼성전자·SK하이닉스의 HBM 실적 성장세가 확고하여 강력한 저점 매수 시그널 제시.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
            "insight": "삼전과 닉스는 대한민국 증시의 핵심 엔진이며, 단기 조정 구간은 저점에 주울 수 있는 최고의 복리 기회임.",
            "action_point": "주가 급락 시 쫄지 말고 삼성전자와 SK하이닉스 비중을 분할로 확대할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech"],
            "tags": ["삼전닉스", "삼성전자", "SK하이닉스", "HBM수율", "더블밸류업"]
        }
    },
    # 36. rKt6k8GejzU - 미국증시 강세장 메모리 다음은 비메모리 (stock / tech)
    {
        "id": "rKt6k8GejzU",
        "analysis": {
            "summary": "미국 증시가 강세장을 이어가는 과정에서 메모리 반도체 랠리에 이어 <span class=\"text-cyan-300 font-semibold\">비메모리 파운드리 및 팹리스</span>로 온기가 확산되는 반도체 순환매 구조를 다룸. <span class=\"text-cyan-300 font-semibold\">TSMC, 엔비디아, 브로드컴</span> 등 글로벌 비메모리 대장주들의 우상향 모멘텀을 정밀 분석함.",
            "key_claims": [
                "메모리 반도체(HBM) 주가 급등 이후 시장 자금의 다음 목적지는 파운드리 및 커스텀 ASIC 비메모리 분야임.",
                "AI 가속기 시장 확대로 인한 맞춤형 칩(ASIC) 설계 및 TSMC 선단 공정 가동률이 사상 최고 수준 지속."
            ],
            "data_points": [
                "TSMC 3나노/2나노 공정 가동률: 100% 풀 가동",
                "브로드컴(AVGO) 커스텀 AI 칩 매출 성장률: 전년 대비 50% 이상 폭증"
            ],
            "signal": "bullish",
            "signal_reason": "메모리에서 비메모리로 이어지는 글로벌 반도체 순환매 호재 반영.",
            "key_companies": ["TSMC(TSM)", "엔비디아(NVDA)", "브로드컴(AVGO)", "삼성전자(005930)"],
            "insight": "반도체 강세장은 메모리 한 영역에 그치지 않고 파운드리 및 커스텀 ASIC 설계로 온기가 확산되는 대형 사이클임.",
            "action_point": "TSMC 밸류체인 및 국내 반도체 디자인하우스/가온칩스 등 비메모리 관련 수혜주 동시 관심."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["미국증시강세장", "비메모리반도체", "TSMC", "브로드컴", "글로벌인터뷰"]
        }
    },
    # 37. u-l8tYf7Zu4 - 콘서트 즐기는 과학적 방법 (etc)
    {
        "id": "u-l8tYf7Zu4",
        "analysis": {
            "summary": "콘서트 및 음향 무대 현장에서 라이브 음악을 가장 완벽하고 안전하게 즐기는 <span class=\"text-amber-300 font-bold\">음향 물리학 및 청각 보호 과학</span>을 엔플라잉(N.Flying)과의 초대석 토크로 해설함. 스피커 위치에 따른 음압 전달 및 이명 예방을 위한 청음 팁을 전달함.",
            "key_claims": [
                "콘서트장 내 스피커 주파수 특성 및 음압 레벨(dB)에 따라 최적의 청음 구역이 결정됨.",
                "고음역대 데시벨 폭발 시 이명 예방을 위한 뮤지션용 이어플러그 착용의 중요성."
            ],
            "data_points": [
                "콘서트 라이브 음압 레벨: 평균 100~110dB 육박",
                "청각 손상 방지 가이드 기준 85dB 이상 장시간 노출 위험"
            ],
            "signal": "na",
            "signal_reason": "음향 물리학 및 밴드 문화 교양 콘텐츠로 직접적인 증시 시그널과 무관함.",
            "key_companies": ["엔플라잉"],
            "insight": "음향 공학과 청각 보호 과학은 단순한 라이브 감상을 넘어 일상 속 청각 건강을 키우는 실용적 지식임.",
            "action_point": "라이브 공연 및 엔터테인먼트 산업의 현장 기술 요소에 대한 교양 지식으로 참고."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["콘서트과학", "음향물리학", "청각보호", "엔플라잉", "안될과학"]
        }
    }
]

def run():
    for item_data in batch7_data:
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
