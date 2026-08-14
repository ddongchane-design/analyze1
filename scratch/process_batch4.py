import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch4_data = [
    # 16. HycRCI-bVxE - 양극화 소비 다이소와 샤넬 (economy / stock)
    {
        "id": "HycRCI-bVxE",
        "analysis": {
            "summary": "한국 내수 소비 시장이 중가형 브랜드의 침체 속에 <span class=\"text-amber-300 font-bold\">초저가(다이소)</span>와 <span class=\"text-amber-300 font-bold\">초고가 명품(샤넬)</span>으로 양극화되는 현상을 소비 트렌드 및 유통 구조 관점에서 분석함. 중산층 소비 위축과 실질 소득 정체가 유통 산업 재편을 가속화하고 있음.",
            "key_claims": [
                "어중간한 가격대의 중간 브랜드는 외면받고 가성비 극대화 상품과 초명품으로 소비가 분할됨.",
                "고물가·고금리 장기화로 가계의 실질 처분가능소득이 줄어든 영향이 양극화 소비로 표출됨."
            ],
            "data_points": [
                "다이소 연간 매출액 사상 최대 경신 및 1,000원~5,000원 균일가 비중 90% 이상",
                "백화점 명품관 매출 비중 지속 상승 반면 중저가 패션 상점 휴폐업증가"
            ],
            "signal": "neutral",
            "signal_reason": "내수 전반의 경기 둔화 우려 속에 초저가 유통 및 럭셔리 특화 기업으로 수혜 쏠림.",
            "key_companies": ["아성다이소", "신세계(004170)", "현대백화점(069960)"],
            "insight": "소비 양극화는 단순한 취향 변화가 아닌 고금리 장기화가 만든 소득 양극화의 반영이며, 유통/소비재 투자 시 명확한 수혜 기업 선택이 필수적임.",
            "action_point": "중간대 마진율이 훼손되는 유통주를 피하고, 초가성비 리테일러 플랫폼 또는 확실한 하이엔드 브랜드 소유 기업에 집중."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["소비양극화", "다이소", "샤넬", "내수경기", "언더스탠딩"]
        }
    },
    # 17. KXi1XbpRXpc - 구글 현금흐름과 CapEx (tech / stock)
    {
        "id": "KXi1XbpRXpc",
        "analysis": {
            "summary": "알파벳(구글)이 검색 및 광고 사업에서 막대한 매출을 올림에도 불구하고 <span class=\"text-cyan-300 font-semibold\">잉여현금흐름(FCF)</span>이 정체되는 이유를 파헤침. AI 경쟁 심화에 따라 <span class=\"text-rose-400 font-medium\">AI 데이터센터 및 설비투자(CapEx)</span> 자금 지출이 천문학적으로 늘어난 점이 주요 원인임.",
            "key_claims": [
                "구글의 본업 수익성은 최고 수준이나 AI 서버 및 전동 칩(TPU/GPU) 구매 CapEx가 FCF를 압박함.",
                "클라우드 및 검색 AI 인프라 선점을 위한 현금 소진 속도가 과거 닷컴 시절을 방증함."
            ],
            "data_points": [
                "구글 분기 CapEx 지출액: 130억 달러 이상 돌파",
                "잉여현금흐름(FCF) 이익률: 매출 대비 하락 기조"
            ],
            "signal": "neutral",
            "signal_reason": "압도적 본업 이익 창출력과 천문학적 AI 투자비 지출이 상쇄되어 장기 관망 관점 유지.",
            "key_companies": ["구글(GOOGL)", "엔비디아(NVDA)"],
            "insight": "AI 군비 경쟁 시대에는 매출 증대 이상으로 FCF(잉여현금)를 방어하며 효율적 AI 인프라를 구축하는 기업만이 승리할 수 있음.",
            "action_point": "구글의 AI 검색 전환율 및 TPU v5/v6 도입에 따른 자사주 매입 체력 유지를 점검할 것."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock"],
            "tags": ["구글 CapEx", "잉여현금흐름", "AI투자비용", "알파벳", "교양이를부탁해"]
        }
    },
    # 18. LOU26aSgarY - 레버리지 악순환과 시장 반등 (stock / economy)
    {
        "id": "LOU26aSgarY",
        "analysis": {
            "summary": "글로벌 증시 급변동 과정에서 신용융자 및 반대매매로 인한 <span class=\"text-rose-400 font-medium\">레버리지 악순환 청산</span>이 증시 급락을 가속화한 기전을 조명함. 반대매매 물량이 일단락된 후 나타나는 <span class=\"text-amber-300 font-bold\">기술적 반등 국면</span>에서 반등의 지속성과 수급 주체를 평가함.",
            "key_claims": [
                "과도한 신용 레버리지 털어내기 과정이 진정되어야 비로소 진바닥이 형성됨.",
                "단기 기술적 반등 시에는 수급 빈집 상태인 대형 실적주로의 자금 유입이 빠르게 진행됨."
            ],
            "data_points": [
                "국내 신용융자 잔고: 폭락 전 대비 1~2조 원 대폭 감소",
                "코스피 기술적 반등 마지노선 200일 이동평균선 수준 제시"
            ],
            "signal": "bullish",
            "signal_reason": "레버리지 매물 청산 완료에 따른 악성 수급 해소 및 과도한 과매도 구간 진입 판단.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
            "insight": "레버리지 청산 폭풍이 지나간 자리는 투매의 잔해 속에 알짜 주식을 최적의 가격에 주울 수 있는 바닥 매수 구간임.",
            "action_point": "신용 잔고 감소와 반대매매 일단락 신호를 확인하고 반도체 및 실적 개선 대형주 저점 매수 가동."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["레버리지악순환", "반대매매청산", "기술적반등", "코스피바닥", "아침N투자"]
        }
    },
    # 19. Mmre5PhOKj8 - 코스피 15퍼 하락시켰던 엔화 변수 (economy / stock)
    {
        "id": "Mmre5PhOKj8",
        "analysis": {
            "summary": "과거 코스피를 15% 이상 폭락시켰던 <span class=\"text-amber-300 font-bold\">엔화 청산 패닉</span> 경험을 되짚으며, 일본은행(BOJ)의 금리 인상 및 엔화 급등 변수가 한국 증시에 불러올 충격을 다룸. 엔/달러 환율 하락이 이끄는 <span class=\"text-rose-400 font-medium\">엔 캐리 트레이드 청산 리스크</span>가 신흥국 증시를 재차 흔들 가능성을 경고함.",
            "key_claims": [
                "일본의 금리 인상 및 엔화 강세 전환은 글로벌 유동성 축소의 시발점임.",
                "외국인 자금이 엔 캐리 자금과 연계되어 있어 국내 주식시장에서의 자금 유출 변수로 작용."
            ],
            "data_points": [
                "과거 BOJ 금리 인상 시 코스피 하락 폭: 최대 15% 기록",
                "엔/달러 환율 140엔 진입 시 한국 증시 외국인 순매도 규모"
            ],
            "signal": "bearish",
            "signal_reason": "엔화 강세 전환에 따른 글로벌 리스크 오프(위험자산 회피) 수급 압력 우려.",
            "key_companies": ["삼성전자(005930)", "현대차(005380)"],
            "insight": "엔화 향방은 국내 주식시장의 자금 유출입을 결정하는 리트머스 시험지이며, 엔 캐리 청산 신호 시 신중한 위험 관리가 필수적임.",
            "action_point": "엔/달러 환율 및 BOJ 금리 결정 추이를 주시하고 환율 변동성 국면에서 방어주 비중 확대 검토."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["엔화변수", "엔캐리청산", "BOJ금리인상", "코스피폭락", "주린이구조대"]
        }
    },
    # 20. Nvpu5RUjEWo - 8월 갭하락 출발 대형 호재 도망치지 마라 (stock / economy)
    {
        "id": "Nvpu5RUjEWo",
        "analysis": {
            "summary": "8월 증시의 시가 갭하락 출발이 악성 매물을 한 번에 털어내는 <span class=\"text-amber-300 font-bold\">대형 반전 호재</span>가 될 수 있음을 역설함. 공포 심리에 휩쓸려 도망치지 말고, 과매도 구간에서 형성되는 <span class=\"text-cyan-300 font-semibold\">대형 우량주 저점 매수 기회</span>를 신중히 포착할 것을 당부함.",
            "key_claims": [
                "증시의 시가 갭하락은 악성 투매 매물을 소화하는 수급 정화 과정임.",
                "8월 중후반으로 갈수록 실적 및 금리 인하 기대감이 재차 부각되어 전강후강 패턴 가능성."
            ],
            "data_points": [
                "과거 갭하락 음봉 후 양봉 전환 확률 70% 상회",
                "코스피 PBR 0.85배 근접 시 역사적 바닥 형성"
            ],
            "signal": "bullish",
            "signal_reason": "갭하락에 따른 과매도 바닥 신호 발생 및 저가 매수세 유입 가능성 정밀 반영.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "한화에어로스페이스(012450)"],
            "insight": "남들이 공포에 질려 투매할 때 나타나는 갭하락은 진짜 우량주를 저점에 줍는 절호의 수급 찬스임.",
            "action_point": "갭하락 시 당황하여 섣부른 손절을 하기보다 펀더멘털이 견고한 대형 반도체/방산주 저점 분할 매수 대응."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["갭하락호재", "전강후강", "저점매수", "공포매수", "주린이구조대"]
        }
    }
]

def run():
    for item_data in batch4_data:
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
