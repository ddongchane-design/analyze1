import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch3_data = [
    # 13. HpkH0cd4qTI - 멀쩡한 코어 식어가는 주변 AI버블 (tech / stock)
    {
        "id": "HpkH0cd4qTI",
        "analysis": {
            "summary": "AI 산업에서엔비디아·TSMC 등 <span class=\"text-cyan-300 font-semibold\">핵심 코어 반도체</span>는 멀쩡하지만, 수익화에 실패한 <span class=\"text-rose-400 font-medium\">주변 AI 응용 애플리케이션 및 스타트업</span>의 자금 난이 심화되는 '버블의 경고 신호'를 조명함. 닷컴 버블과 마찬가지로 핵심 인프라와 단순 서비스 간 주가 양극화가 뚜렷해짐.",
            "key_claims": [
                "엔비디아 등 코어 칩셋 기업은 사상 최대 영업이익을 유지하나 하위 AI 응용업체는 폐업 증가.",
                "AI 서비스의 실질 과금 모델 창출 여부가 주가 지속성의 성패를 좌우함."
            ],
            "data_points": [
                "AI 코어 반도체 마진율: 70% 유지 반면 단순 AI 서비스 마진율: -20% 적자",
                "글로벌 AI 스타트업 2분기 벤처캐피털(VC) 투자액 25% 축소"
            ],
            "signal": "neutral",
            "signal_reason": "코어 반도체의 강력한 실적과 주변부 스타트업 둔화 경고 신호 상충.",
            "key_companies": ["엔비디아(NVDA)", "TSMC(TSM)", "오픈AI"],
            "insight": "AI 버블 논란 속에서 살아남는 핵심은 '코어 반도체 및 확실한 과금력을 가진 플랫폼'이며, 껍데기뿐인 AI 서비스 래퍼 기업을 걸러내는 선별 눈이 필요함.",
            "action_point": "단순 AI 테마 중소형주를 정돈하고 코어 하드웨어(엔비디아, SK하이닉스) 및 1등 플랫폼에 집중."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock"],
            "tags": ["AI버블경고", "코어반도체", "엔비디아", "닷컴버블비교", "교양이를부탁해"]
        }
    },
    # 14. IjuduomAPOg - AMD 아쉬운 가이던스 급락 S&P500 신고가 (stock / tech)
    {
        "id": "IjuduomAPOg",
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">AMD</span>가 분기 실적 발표 후 3분기 가이던스 미흡으로 시간외 급락한 반면, 빅테크 강세에 힘입어 <span class=\"text-amber-300 font-bold\">S&P500 지수가 사상 최고치</span>를 경신한 월가 소식을 다룸. AI 가속기 시장에서 엔비디아의 독주 체제와 2위 그룹 간 격차가 재확인됨.",
            "key_claims": [
                "AMD의 MI300/MI325 가속기 매출 가이던스가 시장의 높은 기대를 만족시키지 못해 시간외 하락.",
                "S&P500 신고가 경신은 빅테크 전반의 실적 연착륙 신호를 반영함."
            ],
            "data_points": [
                "AMD 시간외 주가: 약 6~7% 급락 기록",
                "S&P500 지수: 사상 최고치(5,600pt 이상) 재경신 마감"
            ],
            "signal": "bullish",
            "signal_reason": "개별 기업(AMD) 가이던스 아쉬움에도 S&P500 신고가 경신으로 미 증시 대세 상승 입증.",
            "key_companies": ["AMD(AMD)", "엔비디아(NVDA)", "마이크로소프트(MSFT)"],
            "insight": "AI 가속기 시장은 엔비디아의 절대 강세 속에 2위 후발주자(AMD)와의 이익 격차가 커지는 1등 독식 구조가 더 공고해짐.",
            "action_point": "AMD 조정 시 엔비디아 및 HBM 공급 체인 대장주(SK하이닉스)의 절대 우위를 재확인하고 매수 유지."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["AMD급락", "SP500신고가", "월가뉴스레터", "엔비디아독주", "삼프로TV"]
        }
    },
    # 15. NXP5ZFI_tPM - 호르무즈 해협 이란 트럼프 지정학 (economy / energy)
    {
        "id": "NXP5ZFI_tPM",
        "analysis": {
            "summary": "이란이 호르무즈 해협 통제권 강화를 주장하고 트럼프의 중동 외교 카드가 부상함에 따라 <span class=\"text-violet-300 font-medium\">국제 유가 및 지정학적 수급 신호</span>가 다시 요동칠 수 있음을 분석함. 원유 수송선 통제권 이슈가 수면 위로 올라오며 <span class=\"text-rose-400 font-medium\">에너지 물가 상방 리스크</span>가 인플레이션을 재자극할 가능성을 경고함.",
            "key_claims": [
                "호르무즈 해협 봉쇄 또는 봉쇄 위협은 글로벌 해상 원유 수송의 20%를 마비시키는 지정학적 뇌관임.",
                "트럼프의 중동 외교 수완과 미-이란 간 밀당이 유가 80달러선 돌파 여부를 좌우함."
            ],
            "data_points": [
                "호르무즈 해협 일일 원유 수송량: 약 2,000만 배럴 (글로벌 20%)",
                "WTI 유가 변동성 범위: 70달러대 중반에서 지정학 노이즈 시 급등"
            ],
            "signal": "neutral",
            "signal_reason": "지정학적 리스크 노이즈 재발로 인한 유가 및 매크로 시장 관망세 형성.",
            "key_companies": ["S-Oil(010950)", "SK이노베이션(096770)", "한국석유(004090)"],
            "insight": "중동 정세의 기습적 노이즈는 유가와 해운 운임을 자극하여 물가 하락을 둔화시키는 유동성 복병으로 작용할 수 있음.",
            "action_point": "국제 유가 추이를 체크하며 에너지 관련 헤지 종목 및 방산/해운주 수급 모니터링."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["energy", "stock"],
            "tags": ["호르무즈해협", "이란지정학", "국제유가", "트럼프중동", "교양이를부탁해"]
        }
    },
    # 16. P7CM0Soo8mw - 국채 금리 급등 워시 국채 시장 (crypto / economy)
    {
        "id": "P7CM0Soo8mw",
        "analysis": {
            "summary": "미국 재무부의 국채 발행 입찰과 워시(Wash) 거래 논란 속에 <span class=\"text-amber-300 font-bold\">글로벌 국채 금리가 급등</span>한 매크로 현상을 분석함. 국채 금리 상승에도 불구하고 디지털 자산 시장으로 기관 수급 및 <span class=\"text-cyan-300 font-semibold\">비트코인 가치 저장 파킹 자금</span> 유입세가 지속되고 있음.",
            "key_claims": [
                "미국 10년물 국채 금리가 발행 물량 부담으로 급등하며 위험자산 멀티플을 압박함.",
                "비트코인은 달러 및 국채 변동성을 방어하는 디지털 금(Gold)으로서의 입지를 다짐."
            ],
            "data_points": [
                "미국 10년물 국채 금리: 4.10%선 돌파 테스트",
                "비트코인 6만 5천 달러 하단 지지력 형성"
            ],
            "signal": "bullish",
            "signal_reason": "국채 금리 급등 부담에도 비트코인의 기관 수급 하단 지지력 증명.",
            "key_companies": ["마이크로스트래티지(MSTR)", "코인베이스(COIN)"],
            "insight": "국채 금리가 뛰는 장세에서 비트코인은 단순 투기 자산이 아닌 달러 헤지용 디지털 자산으로 차별화되는 모멘텀을 얻음.",
            "action_point": "비트코인 현물 ETF 자금 유입액을 모니터링하며 크립토 대장주 저점 편입 유지."
        },
        "classification": {
            "primary_topic": "crypto",
            "secondary_topics": ["economy", "stock"],
            "tags": ["국채금리급등", "비트코인디지털금", "국채입찰", "크립토PLUS", "삼프로TV"]
        }
    },
    # 17. PiW3NKCU0NM - 개장전 AI 랠리 재시동 스페이스X 칼날 (stock / space)
    {
        "id": "PiW3NKCU0NM",
        "analysis": {
            "summary": "개장 전 미국 증시에서 <span class=\"text-cyan-300 font-semibold\">AI 랠리가 다시 시동</span>을 거는 가운데, 월가 일각에서 스페이스X의 락업 해제 및 높은 밸류에이션에 대해 경고한 '떨어지는 칼날' 논란을 정밀 조명함. 빅테크 실적 호조가 테크주 반등을 주도 중임.",
            "key_claims": [
                "아마존과 팔란티어의 실적 폭발이 AI 랠리 재가동의 불씨를 당김.",
                "스페이스X는 단기 비상장 보호예수 물량 우려에도 스타링크 장기 실적 성장세 확고."
            ],
            "data_points": [
                "나스닥 선물 지수: 개장 전 +1.0% 이상 강세",
                "스페이스X 스타링크 연간 매출액 가이던스 상향"
            ],
            "signal": "bullish",
            "signal_reason": "AI 랠리 재가동 및 빅테크 펀더멘털 회복에 따른 강한 개장 전 매수 신호.",
            "key_companies": ["팔란티어(PLTR)", "아마존(AMZN)", "스페이스X", "테슬라(TSLA)"],
            "insight": "월가의 단기 락업 우려는 우량 기술주의 성장 궤적을 꺾지 못하며, AI 랠리는 실적이라는 강력한 엔트로피로 재시동됨.",
            "action_point": "AI 랠리 수혜 중심인 반도체 대장주 및 빅테크 밸류체인 수혜주 저점 진입."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["space", "tech"],
            "tags": ["AI랠리재시동", "스페이스X", "개장전요것만", "미국증시", "한경글로벌"]
        }
    },
    # 18. QU_k-8LU2JM - 8월 4일 마감 삼전닉스만 사면 안된다 (stock / tech)
    {
        "id": "QU_k-8LU2JM",
        "analysis": {
            "summary": "8월 4일 국내 증시 마감 시황을 통해 '삼전닉스만 맹목적으로 사던 장세는 끝났다'고 선언하며 하반기 수익률을 결정할 <span class=\"text-amber-300 font-bold\">포트폴리오 다변화 전략</span>을 제시함. 반도체를 유지하되 <span class=\"text-cyan-300 font-semibold\">방산, 조선, 코스닥 전공정 소부장</span>으로 자산을 균형 배치해야 함.",
            "key_claims": [
                "반도체 대장주 쏠림 장세에서 개별 실적 개선주 및 코스닥 장비주로의 자금 순환매 시작.",
                "하반기 금리 인하 및 밸류업 수혜주(금융, 방산)를 섞는 균형 포트폴리오가 이익 승률 높임."
            ],
            "data_points": [
                "8월 4일 코스닥 지수: 코스피 대비 상대적 강세 마감",
                "코스닥 전공정 소부장 장비주 당일 3~5% 수급 반등"
            ],
            "signal": "bullish",
            "signal_reason": "주도주 다변화 및 순환매 장세 개막에 따른 하반기 포트폴리오 상방 확신.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "한화에어로스페이스(012450)", "원익IPS(030530)"],
            "insight": "반도체 외길 투자에서 벗어나 이익 성장 폭이 큰 방산·조선·소부장으로 자산을 분산시키는 전략이 8월 수익률의 분수령임.",
            "action_point": "반도체 비중을 적정 유지하고 방산 및 코스닥 우량 장비주를 30% 수준 분할 편입."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["마감시황", "포트폴리오전략", "삼전닉스이후", "순환매", "클로징벨"]
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
