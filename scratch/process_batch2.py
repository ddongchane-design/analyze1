import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch2_data = [
    # 6. 8nPuwC3V-C0 - 코스피 마감시황 (stock / economy)
    {
        "id": "8nPuwC3V-C0",
        "analysis": {
            "summary": "8월 3일 국내 증시가 전일 역대급 폭등 이후 하루 만에 재차 급락하며 <span class=\"text-rose-400 font-medium\">외국인 순매도 전환</span>과 엔화 강세 재개에 따른 변동성을 겪음. 코스피 반도체 대장주(<span class=\"text-cyan-300 font-semibold\">삼성전자</span>, <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>)가 약세를 보이며 지수 하락을 주도했으나 실적 장세 국면 진입에 따른 개별 종목 차별화가 진행되고 있음.",
            "key_claims": [
                "전일 사상 최대 폭등에 따른 차익 실현 물량과 엔/달러 환율 하락(엔화 강세)이 복합 작용함.",
                "외국인 수급의 일시적 차익 실현에도 불구하고 3분기 실적 개선 대장주의 펀더멘털은 양호함."
            ],
            "data_points": [
                "8월 3일 코스피 지수: 전일 대비 약 2~3%대 하락 마감",
                "외국인 유가증권시장 순매도 규모: 5,000억 원 이상 돌아서"
            ],
            "signal": "bearish",
            "signal_reason": "전일 폭등 후 차익 실현 매물 및 엔화 강세 우려로 인한 단기 기술적 조정 국면 형성.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "현대차(005380)"],
            "insight": "8월 초 국내 증시는 엔화 환율 변동성과 미국 빅테크 실적 발표 일정에 맞춰 일별 극심한 변동성을 연출하는 주가 진통 구간임.",
            "action_point": "지수 급락 시 당황한 뇌동매도를 자제하고 차세대 HBM 및 확실한 실적 모멘텀을 가진 대형주 중심의 분할 매수 기회 모색."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy", "tech"],
            "tags": ["코스피", "마감시황", "외국인매도", "SK하이닉스", "삼성전자", "클로징벨"]
        }
    },
    # 7. BURH5pWhQjs - 엔달러 개입 베선트 (economy / stock)
    {
        "id": "BURH5pWhQjs",
        "analysis": {
            "summary": "트럼프 2기 재무장관 지명 가능성이 거론되는 스콧 베선트의 <span class=\"text-amber-300 font-bold\">엔/달러 환율 개입</span> 및 미 달러화 정책 관련 경고성 발언을 정밀 조명함. 미국 정부와 일본 재무성의 환율 시장 공동 개입 가능성과 <span class=\"text-rose-400 font-medium\">글로벌 자금 흐름의 요동</span>에 신중한 접근이 필요함.",
            "key_claims": [
                "미국 재무부의 달러 약세 용인 혹은 일본 엔화 방어 공조가 구체화될 경우 환율 변동성 극대화.",
                "엔 캐리 트레이드 청산 압력이 미국 채권 및 주식 시장의 조정 원인으로 작용 가능."
            ],
            "data_points": [
                "엔/달러 환율 변동 범위: 155엔대에서 140엔대 후반 진입 논의",
                "미국 10년물 국채 금리 반응 및 외환시장 거래대금 급증"
            ],
            "signal": "neutral",
            "signal_reason": "미-일 통화 정책 및 환율 개입 불확실성이 상존하여 시장 매수/매도 시그널이 팽팽히 대립 중.",
            "key_companies": [],
            "insight": "엔화 환율의 급격한 변동은 단순한 외환 이슈가 아니라 글로벌 레버리지 자금의 이동을 결정짓는 최고 중요 매크로 변수임.",
            "action_point": "엔/달러 환율 145엔 하회 여부를 주시하면서 환율 민감도가 높은 수출주와 금융주의 비중을 조정할 필요가 있음."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["베선트", "엔달러환율", "미국재무부", "엔캐리", "워싱턴나우"]
        }
    },
    # 8. C5kPhK7HBEQ - 한국 AI의 최대 문제점 (tech / stock)
    {
        "id": "C5kPhK7HBEQ",
        "analysis": {
            "summary": "한국 AI 생태계가 독자적인 프론티어 LLM 및 <span class=\"text-cyan-300 font-semibold\">초대형 데이터센터 인프라</span> 확보 부족으로 인해 미국 빅테크 플랫폼 종속 심화라는 구조적 한계에 직면했음을 지적함. 정부 차원의 <span class=\"text-amber-300 font-bold\">AI 그래픽 처리장치(GPU) 자원 지원</span> 및 자체 데이터 주권 확보가 미흡하면 경쟁에서 낙오될 수 있음.",
            "key_claims": [
                "국내 기업들의 H100/B200 등 고성능 AI 반도체 보유량이 빅테크 한 개 기업의 10분의 1 수준에 불과함.",
                "소버린 AI 구현을 위한 국가적 초거대 컴퓨팅 파크 구축이 시급함."
            ],
            "data_points": [
                "국내 AI 기업 전체 보유 GPU 수량: 글로벌 빅테크 대비 현저히 낮음",
                "글로벌 AI 모델 성능 벤치마크 상위권 내 한국 독자 모델 비중 저조"
            ],
            "signal": "bearish",
            "signal_reason": "국내 소프트웨어 AI 기업들의 독자 인프라 부재로 인한 장기 수익성 및 기술 자립도 우려 반영.",
            "key_companies": ["네이버(035420)", "카카오(035720)"],
            "insight": "AI 패권 싸움은 단순한 알고리즘 개발이 아닌 자본력에 기반한 초거대 GPU 클러스터 및 데이터센터 확보 싸움임.",
            "action_point": "국내 단순 AI 래퍼(Wrapper) 서비스 기업보다 AI 반도체 인프라 하드웨어 및 수냉식 냉각 부품 공급사에 집중 투자."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock", "economy"],
            "tags": ["한국AI", "GPU인프라", "소버린AI", "빅테크종속", "SOD"]
        }
    },
    # 9. DdfKlOlFOIg - 빅테크 숨은빚 2,390조원 AI제국 (tech / stock)
    {
        "id": "DdfKlOlFOIg",
        "analysis": {
            "summary": "글로벌 빅테크 기업들이 AI 데이터센터 구축 및 장비 도입을 위해 운용리스 및 사모펀드 딜을 활용해 숨겨둔 <span class=\"text-rose-400 font-medium\">막대한 부채(2,390조 원 상당)</span>가 회계상 리스크로 부각됨을 파헤침. AI 투자 대비 현금 회수(ROI) 시점이 지연될 경우 <span class=\"text-rose-400 font-medium\">빅테크 신용 등급 및 CapEx 축소</span> 경고등이 켜질 수 있음.",
            "key_claims": [
                "빅테크의 AI 데이터센터 장비 대량 구매 뒤에는 대규모 부채와 오프밸런스(부외부채) 리스 계약이 숨어있음.",
                "AI 서비스의 매출 창출 속도가 데이터센터 투자 비용 증가 속도를 따라잡지 못하는 갭 발생."
            ],
            "data_points": [
                "글로벌 빅테크 합산 AI 관련 가용 부채 및 리스 계약 규모: 약 2,390조 원 추정",
                "빅테크 4사(빅4) 2026년 합산 CapEx: 2,000억 달러 돌파"
            ],
            "signal": "bearish",
            "signal_reason": "AI 투자 회수 지연 우려와 회계상 숨은 부채 리스크로 인한 빅테크 주가 조정 압력 증가.",
            "key_companies": ["마이크로소프트(MSFT)", "구글(GOOGL)", "아마존(AMZN)", "메타(META)"],
            "insight": "AI 버블 논란의 본질은 기술 혁신 자체보다 빅테크 기업들의 무리한 부채 기반 CapEx 지출과 이익 회수 속도 간의 불일치에 있음.",
            "action_point": "빅테크 실적 발표 시 잉여현금흐름(FCF) 및 CapEx 가이던스 변화를 철저히 모니터링할 것."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock", "economy"],
            "tags": ["빅테크숨은빚", "AICapEx", "AI버블", "데이터센터", "SOD"]
        }
    },
    # 10. EsyLVY47bX8 - 실적 대박 주가는 왜? AI 산업과 주식은 다르다 (stock / tech)
    {
        "id": "EsyLVY47bX8",
        "analysis": {
            "summary": "빅테크 기업들이 호실적을 발표하고도 주가가 급락하는 기현상을 분석하며, <span class=\"text-amber-300 font-bold\">AI 산업의 성장성</span>과 <span class=\"text-rose-400 font-medium\">주식 시장의 높은 기대치(밸류에이션)</span> 사이의 간극을 해설함. 닷컴버블 당시와 유사하게 실적 수치 자체보다 높은 벨류에이션 부담이 주가 발목을 잡는 국면임.",
            "key_claims": [
                "산업이 성장한다고 해서 해당 테마 주가가 무조건 계속 상승하는 것은 아님 (선반영 과다).",
                "투자자들은 단순 실적 호조를 넘어 마진율 유지와 현금흐름 재투자의 효율성을 원하고 있음."
            ],
            "data_points": [
                "2026년 2분기 빅테크 실적 발표 후 당일 주가 반응: 실적 상회에도 -3%~-7% 변동",
                "빅테크 평균 PER: 과거 5년 평균 상단 상회"
            ],
            "signal": "neutral",
            "signal_reason": "실적 성장세는 견고하나 밸류에이션 재평가 과정에서 강한 상하방 횡보 장세 예상.",
            "key_companies": ["엔비디아(NVDA)", "애플(AAPL)", "마이크로소프트(MSFT)"],
            "insight": "주가는 현재의 실적 수치보다 미래 이익의 할인율과 기대치 갱신 속도에 반응하므로, 최고 실적이 발표되는 순간이 단기 상투가 될 수 있음.",
            "action_point": "실적 발표 직후의 주가 변동성 착시를 피하고, 밸류에이션 부담이 낮아진 눌림목에서 분할 진입하는 신중함 필요."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech"],
            "tags": ["AI버블", "빅테크실적", "주식과산업", "닷컴버블비교", "교양이를부탁해"]
        }
    }
]

def run():
    for item_data in batch2_data:
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
