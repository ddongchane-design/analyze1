import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch1_data = [
    # 1. 3atEi76lZbk - 오픈AI 상장 AI 랠리 변곡점 (tech / stock)
    {
        "id": "3atEi76lZbk",
        "analysis": {
            "summary": "생성형 AI 생태계의 기틀을 연 <span class=\"text-cyan-300 font-semibold\">오픈AI(OpenAI)</span>의 향후 기업공개(IPO) 추진 전망과 시장 변곡점을 조명함. 오픈AI의 상장이 <span class=\"text-amber-300 font-bold\">AI 랠리의 최후 빅이벤트</span>이자 밸류에이션 재평가의 본질적 분수령이 될 것임을 파헤침.",
            "key_claims": [
                "오픈AI의 기업가치는 1,000억 달러 이상을 상회하며 글로벌 자금의 블랙홀이 될 전망임.",
                "상장 성공 여부는 막대한 서버 운용비와 이익 회수(ROI) 체력의 검증대가 됨."
            ],
            "data_points": [
                "오픈AI 가용 기업가치 전망: 1,000억~1,500억 달러 이상 추정",
                "챗GPT 유료 구독자 및 B2B 기업 고객 수 연 2배 성장"
            ],
            "signal": "bullish",
            "signal_reason": "오픈AI 상장 모멘텀이 전 세계 AI 생태계 및 빅테크 주가 밸류에이션을 한 단계 더 도약시키는 계기 제공.",
            "key_companies": ["오픈AI", "마이크로소프트(MSFT)", "엔비디아(NVDA)"],
            "insight": "오픈AI 상장은 AI 랠리의 끝이 아니라 비상장 기대감 영역에서 공개 시장의 검증 및 실질 현금 흐름 평가 단계로 넘어가는 축복의 변곡점임.",
            "action_point": "마이크로소프트 등 오픈AI 대규모 지분 보유 기업 및 연관 인프라 핵심주의 저점 매수 관점 유지."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock"],
            "tags": ["오픈AI상장", "오픈AI", "마이크로소프트", "AI버블", "교양이를부탁해"]
        }
    },
    # 2. 79eFtzXerps - 일본 메가뱅크 부활 시총 1위 (economy / stock)
    {
        "id": "79eFtzXerps",
        "analysis": {
            "summary": "일본 도쿄 증시에서 <span class=\"text-cyan-300 font-semibold\">메가뱅크(MUFG 등)</span>가 40년 만에 시가총액 1위에 등극하는 금융 부활 배경을 파헤침. 일본은행(BOJ)의 마이너스 금리 해제와 <span class=\"text-amber-300 font-bold\">엔화 강세 전환 기류</span>가 은행업 이자마진 정상화를 이끌어냄.",
            "key_claims": [
                "일본 금융권은 장기 디플레이션을 탈출하고 마이너스 금리 종료로 예대마진이 급증함.",
                "도쿄증권거래소의 주주환원 자사주 매입 강제 정책이 메가뱅크 주가를 사상 최고치로 견인."
            ],
            "data_points": [
                "MUFG(미쓰비시UFJ) 등 메가뱅크 시가총액: 40년 만에 일본 증시 최상위 등극",
                "일본 정책 금리 인상에 따른 순이자마진(NIM) 상승 폭: 약 20~30bp 호전"
            ],
            "signal": "bullish",
            "signal_reason": "일본 금융주의 구조적 체질 개선과 주주환원 확대가 주가 밸류에이션 재평가로 직결됨.",
            "key_companies": ["MUFG", "SMFG", "소프트뱅크"],
            "insight": "일본 금융주의 부활은 디플레이션 탈출의 증거이며, 국내 주주환원 밸류업 정책 관련 금융주에도 긍정적 벤치마크 역할을 함.",
            "action_point": "국내 밸류업 지수 관련 우량 금융주(KB금융, 신한지주)의 주주환원 확대에 맞춘 분할 매수."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["일본메가뱅크", "BOJ금리인상", "주주환원", "MUFG", "교양이를부탁해"]
        }
    },
    # 3. 7k7fW9Z4Hsc - 태풍 기상 과학 (etc)
    {
        "id": "7k7fW9Z4Hsc",
        "analysis": {
            "summary": "여름철 태풍이 한반도로 직진하는 대기 순환 및 <span class=\"text-amber-300 font-bold\">북태평양 고기압의 가장자리 경로</span>를 공학 기상학적으로 해설함. 기후 변화에 따른 해수면 온도 상승이 태풍의 세력을 유지시키는 과학적 메커니즘을 전달함.",
            "key_claims": [
                "태풍 이동 경로는 기압계 배치와 고기압 가장자리를 따라 결정됨.",
                "해수면 온도가 28℃ 이상으로 유지되면 태풍이 한반도 상륙 시에도 강한 세력을 유지함."
            ],
            "data_points": [
                "태풍 발생 해역 수온: 평년 대비 1.5℃ 상회",
                "한반도 영향 태풍 빈도 및 전력/농업 피해 통계"
            ],
            "signal": "na",
            "signal_reason": "기상 및 기후 공학 관련 과학 교양 콘텐츠로 직접적인 주식 투자 시그널 없음.",
            "key_companies": [],
            "insight": "태풍과 폭염의 장기화는 단순한 일기 예보를 넘어 계절성 파괴와 인프라 관리 비용 증대를 가져오는 환경 변수임.",
            "action_point": "여름철 태풍 관련 피해 방제주 및 재해 복구 관련 테마 수급 변화를 참고용으로 활용."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": ["energy"],
            "tags": ["태풍경로", "기상학", "북태평양고기압", "기후변화", "안될과학"]
        }
    },
    # 4. 9L8qImk598Q - 도요타 제친 시총 60배 기업 (stock / tech)
    {
        "id": "9L8qImk598Q",
        "analysis": {
            "summary": "일본 주식시장에서 자동차 거두 도요타의 시가총액을 위협하며 1년 반 만에 시총 60배 뛴 <span class=\"text-cyan-300 font-semibold\">반도체 소재/장비 기업(키옥시아 밸류체인 연관)</span>의 폭발적 성장을 파헤침. 일본 반도체 소부장 기업들의 경쟁력 회복과 <span class=\"text-cyan-300 font-semibold\">글로벌 공급망 재편</span> 수혜를 진단함.",
            "key_claims": [
                "일본 소부장 테크 기업이 반도체 패키징 및 첨단 노광 재료 분야에서 독점적 지위를 확보함.",
                "글로벌 빅테크의 반도체 투자 확대가 일본 핵심 소부장 기업 주가를 폭등시킴."
            ],
            "data_points": [
                "해당 기업 시가총액 상승률: 1.5년 만에 60배 폭증",
                "도쿄증시 반도체 소부장 지수 사상 최고치 경신"
            ],
            "signal": "bullish",
            "signal_reason": "반도체 패키징 및 에칭 소재 독점력을 가진 소부장 기업들의 강한 이익 상향 지지.",
            "key_companies": ["도요타(TM)", "키옥시아", "도쿄엘렉트론(TEL)"],
            "insight": "완성차 중심의 전통 제조업에서 첨단 반도체 소재·부품 장비 기업으로 일본 증시의 주도주 교체가 진행 중임.",
            "action_point": "국내 반도체 유기발광 및 HBM 특화 장비/소재 우량주(원익IPS, 유진테크 등)에 대한 관심 증대."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["도요타제친기업", "일본반도체소부장", "키옥시아", "도쿄증시", "교양이를부탁해"]
        }
    },
    # 5. A68mt9FAA4c - 서울 아파트 안 짓는 이유 (economy / stock)
    {
        "id": "A68mt9FAA4c",
        "analysis": {
            "summary": "서울 내 신규 아파트 공급이 정체되는 핵심 원인으로 <span class=\"text-rose-400 font-medium\">공사비 폭등(자재비 및 인건비)</span>과 재개발 조합과 시공사 간의 PF 분쟁을 취재함. 건설사들의 수주 보수성 강화로 인해 <span class=\"text-amber-300 font-bold\">서울 신축 아파트 희소성</span>이 극대화되고 있음.",
            "key_claims": [
                "평당 공사비가 800만~1,000만 원 이상으로 폭등하여 사업성이 악화됨.",
                "건설사들이 위험 부채를 피하기 위해 재개발 사업지 수주를 선별적으로 축소 중."
            ],
            "data_points": [
                "서울 신규 아파트 착공 물량: 전년 대비 40% 이상 감소",
                "평당 건설 공사비 지수: 3년 전 대비 35% 이상 상승"
            ],
            "signal": "neutral",
            "signal_reason": "신축 아파트 희소성에 따른 매매가 하단 지지 및 건설사 실적 보수성 교차.",
            "key_companies": ["GS건설(006360)", "DL이앤씨(375500)", "HD현대산업개발(294870)"],
            "insight": "건설업계의 공사비 원가율 악화는 단기 수주 축소를 부르지만, 입지가 뛰어난 서울 핵심지 신축 부동산의 프리미엄을 유지시키는 원인임.",
            "action_point": "대형 건설주의 경우 우발채무 PF 위험이 없는 원가율 우수 대형사 위주로 선별 접근."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["서울아파트공급", "공사비폭등", "부동산PF", "건설사수주", "언더스탠딩"]
        }
    },
    # 6. BQR6H2nURss - 공허의 8월 7월 회복 기간 (stock / economy)
    {
        "id": "BQR6H2nURss",
        "analysis": {
            "summary": "7월 말 진행된 증시 변동성 후유증으로 시작된 '공허의 8월' 거래대금 감소 현상을 진단함. 하반기 연준 금리 인하와 <span class=\"text-amber-300 font-bold\">실적 개선 대형주 매수세</span>가 본격화되면 8월 중후반부터 강한 지수 회복이 전개될 것을 기대함.",
            "key_claims": [
                "8월 초는 뚜렷한 주도 수급 없이 거래대금이 일시 소강상태를 보이는 숨고르기 구간임.",
                "2분기 및 3분기 실적 추정치가 상향되는 반도체/방산 업종이 지수 회복의 열쇠임."
            ],
            "data_points": [
                "코스피 일일 거래대금: 10조 원 미만으로 감소",
                "3분기 영업이익 전년비 50% 이상 증가 섹터: 반도체 및 방산"
            ],
            "signal": "bullish",
            "signal_reason": "거래대금 바닥 및 주도주 펀더멘털 견고에 따른 8월 중후반 회복 장세 진입 전망.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "한화에어로스페이스(012450)"],
            "insight": "8월 초의 거래대금 가뭄은 투매가 끝난 후 나타나는 지수 소강 국면이며, 실적주 중심의 매집 적기임.",
            "action_point": "거래대금 바닥 구간에서 실적 상향주를 줍는 분할 매수 대응."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["공허의8월", "거래대금감소", "실적개선주", "더블크루", "삼프로TV"]
        }
    }
]

def run():
    for item_data in batch1_data:
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
