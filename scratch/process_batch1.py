import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch1_data = [
    # 1. 1PRseRn4yzE - 폭염 원인 (etc)
    {
        "id": "1PRseRn4yzE",
        "analysis": {
            "summary": "2026년 여름 한반도를 강타한 기열 폭염의 과학적 원인으로 북태평양 고기압과 티베트 고기압의 이중 덮개 현상 및 <span class=\"text-amber-300 font-bold\">해수면 온도 상승</span>을 정밀 기상 데이터로 분석함. 지구 온난화로 인한 <span class=\"text-rose-400 font-medium\">기후 변화 리스크</span>가 일상화됨에 따라 전력 수요 폭증 및 열파 피해 대책 마련이 시급함.",
            "key_claims": [
                "이중 고기압 체증 현상으로 열기가 한반도 상공에 갇히는 열돔(Heat Dome) 상태 지속.",
                "지구 해수면 온도의 급상승이 기온 변동성을 지속적으로 유발함."
            ],
            "data_points": [
                "2026년 8월 한반도 평균 기온: 평년 대비 2.5℃ 이상 상승",
                "동해 및 전북 연안 해수면 온도: 최고 28~29℃ 기록"
            ],
            "signal": "na",
            "signal_reason": "순수 과학 지식 및 기상 기후 교양 콘텐츠로 직접적인 금융 시장 매매 시그널과 무관함.",
            "key_companies": [],
            "insight": "기후 변화에 따른 폭염의 장기화는 전력 인프라 부담 심화와 농축산물 물가 상승(애그플레이션)을 유발하는 구조적 요인임.",
            "action_point": "여름철 전력 피크 관련 에너지/전력망 테마 및 여름 계절주에 대한 단기 수급 변동성을 파악하는 참고 자료로 활용함."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": ["energy"],
            "tags": ["폭염", "기후변화", "열돔현상", "지구온난화"]
        }
    },
    # 2. 2MqUTuSFqQQ - 머스크 인재 발굴 및 조직 (tech / space)
    {
        "id": "2MqUTuSFqQQ",
        "analysis": {
            "summary": "일론 머스크의 <span class=\"text-cyan-300 font-semibold\">스페이스X</span> 및 테슬라 조직 경영 방식으로 최정예 천재 엔지니어를 집결시키고 극한의 생산성에 몰아넣는 독특한 기업 문화를 조명함. 높은 이탈률에도 불구하고 <span class=\"text-cyan-300 font-semibold\">재사용 로켓</span> 및 스타링크, 주행 AI 분야에서 독보적 기술 격차를 유지하는 원동력을 분석함.",
            "key_claims": [
                "머스크 특유의 '물리학 제1원리 기반 미션 부여'가 글로벌 인재 유치의 핵심 동력임.",
                "조직의 극한 효율성과 빠른 시행착오는 우주항공 및 자율주행 시장의 압도적 1위 유지 비결임."
            ],
            "data_points": [
                "스페이스X 스타링크 글로벌 가입자 수 및 로켓 발사 횟수 세계 1위 유지",
                "테슬라 FSD 주행 거리 데이터 및 인재 밀도 지표"
            ],
            "signal": "bullish",
            "signal_reason": "머스크 생태계(테슬라, 스페이스X, xAI)의 기술 혁신 속도와 압도적 인재 몰입도가 경쟁 우위를 지속 확고히 함.",
            "key_companies": ["테슬라(TSLA)", "스페이스X"],
            "insight": "머스크 생태계의 핵심은 칩이나 제조 장비 자체보다 빠른 실행력과 인재 밀도로 만들어내는 소프트웨어·하드웨어 융합 속도임.",
            "action_point": "테슬라 Robotaxi 및 스페이스X 밸류에이션 상승 모멘텀에 맞춰 관련 우주·자율주행 밸류체인을 관심 있게 관찰함."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["space", "stock"],
            "tags": ["일론머스크", "스페이스X", "테슬라", "기업문화", "스타링크"]
        }
    },
    # 3. 5Sce0mThJE4 - 삼성 HBM4 베이스다이 4나노 (tech / stock)
    {
        "id": "5Sce0mThJE4",
        "analysis": {
            "summary": "삼성전자가 차세대 <span class=\"text-cyan-300 font-semibold\">HBM4</span>에서 베이스 다이(Base Die) 생산에 4나노 로직 공정을 채택하여 경쟁사 차별화를 시도하는 기술 전략을 해설함. 신호 전달과 전력 효율 관리가 극대화되는 HBM4 시대에는 <span class=\"text-cyan-300 font-semibold\">삼성 파운드리</span> 수직 통합 경쟁력과 <span class=\"text-cyan-300 font-semibold\">TSMC</span> 생태계 간 격돌이 본격화될 전망임.",
            "key_claims": [
                "HBM4부터 인터페이스 폭이 2048비트로 확장되어 베이스 다이의 전력/타이밍 처리 복잡성이 대폭 증가함.",
                "삼성전자는 메모리와 파운드리를 모두 갖춘 수직 통합 이점을, SK하이닉스는 TSMC 생태계 결합 이점을 활용함."
            ],
            "data_points": [
                "HBM4 대역폭: 단일 스택당 초당 3TB 이상 (2048비트 핀 탑재)",
                "삼성 파운드리 4나노 베이스 다이 적용 발표"
            ],
            "signal": "bullish",
            "signal_reason": "HBM4 기술 규격 격변 과정에서 로직 반도체 융합이 강화되어 한국 메모리 기업들의 단가 상승 및 실적 개선세가 기대됨.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "TSMC(TSM)", "시놉시스(SNPS)"],
            "insight": "HBM4부터 반도체 경쟁은 단순 D램 적층 기술이 아니라 아랫단 베이스 로직 다이의 전력 효율과 시스템 파운드리 검증 능력으로 이동함.",
            "action_point": "삼성전자 파운드리 4나노 수율 안정화 및 SK하이닉스-TSMC 밸류체인의 HBM4 샘플 양산 시점에 주가 반등 주시."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock"],
            "tags": ["HBM4", "베이스다이", "삼성전자", "SK하이닉스", "TSMC", "4나노"]
        }
    },
    # 4. 7Zc1Db8V1S4 - 종부세 개편 및 엔화 구출 작전 (economy / stock)
    {
        "id": "7Zc1Db8V1S4",
        "analysis": {
            "summary": "정부의 초고가·비거주 주택 종합부동산세 과세 강화안과 미-일 당국의 <span class=\"text-amber-300 font-bold\">엔화 방어 구출 작전</span>이 글로벌 금융 시장 및 국내 증시에 미치는 여파를 정밀 취재함. 엔/달러 환율이 급격히 변동함에 따라 <span class=\"text-rose-400 font-medium\">엔 캐리 트레이드 청산 리스크</span>가 재차 고조되고 있음.",
            "key_claims": [
                "국내 부동산 세제 개편으로 다주택자 및 고가 보유자의 세부담 증가 기대.",
                "미국과 일본의 개입으로 엔화 가치가 강세 반전 시 글로벌 자산 시장 청산 우려 확산."
            ],
            "data_points": [
                "종부세 1가구 1주택 장기보유특별공제 한도 10억 원 하향 추진",
                "엔/달러 환율 급변동 구간 150엔대 진입 및 외환 당구 수급 개입"
            ],
            "signal": "neutral",
            "signal_reason": "부동산 규제 강화 정책과 엔화 환율 변동성 확대가 유동성을 위축시킬 수 있어 시장 관망세 형성.",
            "key_companies": ["삼성전자(005930)", "KB금융(105560)"],
            "insight": "엔화 강세 전환은 엔 캐리 트레이드 물량의 회수를 자극하여 코스피를 포함한 신흥국 증시 변동성을 일시적으로 확대시킴.",
            "action_point": "엔/달러 환율 변화 추이 및 외국인 매도세 완화 여부를 체크하며 대형주 저점 분할 매수 타이밍 탐색."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["종부세", "엔화방어", "엔캐리트레이드", "부동산정책", "뉴스3"]
        }
    },
    # 5. 7qcyIGwDc1Y - AI 직격탄 맞은 인도, 의대 쏠림 (tech / economy)
    {
        "id": "7qcyIGwDc1Y",
        "analysis": {
            "summary": "생성형 AI 도입 확산으로 인도의 핵심 산업인 <span class=\"text-cyan-300 font-semibold\">IT 아웃소싱 서비스</span> 및 소프트웨어 개발 일자리가 감소하자 현지 인재들이 의대로 대거 몰리는 구조적 사회 현상을 다룸. 단순 코딩과 고객지원의 <span class=\"text-rose-400 font-medium\">AI 대체 속도</span>가 예상을 상회하며 인력 시장 재편이 급속도로 진행 중임.",
            "key_claims": [
                "인도 IT 거두(TCS, 인포시스 등)의 주니어 개발자 채용이 급감하고 의대 입시 경쟁이 과열됨.",
                "생성형 AI가 하급 IT 일자리를 빠르게 대체하며 신흥국 인력 공급 모델에 타격을 줌."
            ],
            "data_points": [
                "인도 IT 서비스 기업 신규 채용 규모: 전년 대비 약 30~40% 감소",
                "인도 전국 의학입학시험(NEET) 응시자 수 사상 최대 경신"
            ],
            "signal": "bearish",
            "signal_reason": "글로벌 IT 아웃소싱 및 단순 레거시 소프트웨어 외주 산업의 수익성 악화 우려 심화.",
            "key_companies": ["인포시스(INFY)", "TCS", "애벌론"],
            "insight": "AI 혁명은 선진국 기업의 비용 절감을 이끄는 동시에 단순 외주에 의존하던 신흥국 IT 노동 시장의 생존 구도를 완전히 바꾸고 있음.",
            "action_point": "단순 외주 IT 솔루션 업체보다 독자적인 프론티어 AI 모델 및 하이엔드 서비스를 보유한 빅테크 기업 위주 투자가 유효함."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["economy"],
            "tags": ["인도IT", "AI대체", "생성형AI", "아웃소싱", "고용시장"]
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
