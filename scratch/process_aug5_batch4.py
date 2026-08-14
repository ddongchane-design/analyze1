import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch4_data = [
    # 19. R840lTdtCSw - 일본 홋카이도 땅값 30년 버블 넘어 (economy / stock)
    {
        "id": "R840lTdtCSw",
        "analysis": {
            "summary": "일본 홋카이도 공항 및 반도체 연합체 <span class=\"text-cyan-300 font-semibold\">라피더스(Rapidus)</span> 공장 건설 지역의 토지 가격이 30년 전 자산 버블 시절을 돌파하는 부동산 폭등 현상을 와세다대 박상준 교수가 해설함. 국가 차원의 <span class=\"text-amber-300 font-bold\">반도체 공급망 재건 투자가 지각변동</span>을 일으키고 있음.",
            "key_claims": [
                "라피더스의 2나노 반도체 공장 유치가 홋카이도 치토세 지역 땅값을 30년 만에 최고치로 견인.",
                "외국인 관광객 급증과 반도체 인프라 투자가 결합하여 일본 지방 부동산 재평가를 유도."
            ],
            "data_points": [
                "홋카이도 치토세 반도체 공장 주변 지가 상승률: 연 30% 이상 폭등",
                "일본 정부 라피더스 반도체 지원금: 1조 엔 이상 집행"
            ],
            "signal": "bullish",
            "signal_reason": "반도체 국가 인프라 투자 확대로 일본 부동산 및 지방 경제 부활 호재.",
            "key_companies": ["라피더스", "소프트뱅크", "도쿄엘렉트론"],
            "insight": "반도체 공장 유치는 단순한 제조업 유치를 넘어 인구 유입과 지역 지가 상승, 지방 금융 부활로 이어지는 거대한 경제적 연쇄 반응임.",
            "action_point": "일본 반도체 공급망 관련 소부장 기업 및 부동산 자산 보유 기업의 장기 재평가 관찰."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock", "tech"],
            "tags": ["홋카이도땅값", "라피더스", "일본반도체", "부동산버블", "언더스탠딩"]
        }
    },
    # 20. Rm_i4mZxLC0 - 구글 로보틱스 집중 이유 (robot / tech)
    {
        "id": "Rm_i4mZxLC0",
        "analysis": {
            "summary": "구글(Google DeepMind)이 단순 소프트웨어 AI 에이전트를 넘어 <span class=\"text-cyan-300 font-semibold\">피지컬 로보틱스(RT-2, Gemini Robotics)</span> 분야에 집중하는 근본 이유를 기술 구조 관점에서 다룸. 가상 세계의 텍스트 데이터를 넘어 현실 세계의 물리적 상호작용 데이터를 확보하는 것이 <span class=\"text-amber-300 font-bold\">차세대 AGI의 필연적 관문</span>임.",
            "key_claims": [
                "AI의 다음 데이터 부족(Data Wall) 문제를 해결하기 위해 물리적 로봇 멀티모달 데이터 수집이 필수적임.",
                "구글의 로봇 파운데이션 모델이 정밀 제어 및 인간 협업 로봇 상용화를 이끌고 있음."
            ],
            "data_points": [
                "구글 딥마인드 RT-2/Gemini 기반 로봇 학습 데이터 수집량: 전년 대비 5배 증가",
                "글로벌 로보틱스 시장 규모 2030년까지 연평균 30% 성장"
            ],
            "signal": "bullish",
            "signal_reason": "빅테크(구글)의 피지컬 로보틱스 대규모 투자로 로봇 산업 전반의 성장 가속화.",
            "key_companies": ["구글(GOOGL)", "레인보우로보틱스(277810)", "두산로보틱스(454910)"],
            "insight": "구글의 로보틱스 올인은 AI가 화면을 벗어나 물리적 현실 세계로 진출하는 거대한 수순이며, 피지컬 AI 부품 기업들의 가치를 극대화시킴.",
            "action_point": "로봇 관제 파운데이션 모델 관련 소프트웨어 기업 및 국내 로봇 협력사 저점 매수."
        },
        "classification": {
            "primary_topic": "robot",
            "secondary_topics": ["tech", "stock"],
            "tags": ["구글로보틱스", "피지컬AI", "GeminiRobotics", "AGI관문", "엔지니어TV"]
        }
    },
    # 21. TiQvRYsugiY - 26.08.04 오전 유가 급락 뉴욕증시 다우 신고가 (stock / economy)
    {
        "id": "TiQvRYsugiY",
        "analysis": {
            "summary": "8월 4일 뉴욕증시에서 WTI 국제 유가가 5% 급락함에 따라 인플레이션 우려가 완화되고, <span class=\"text-amber-300 font-bold\">다우 지수가 사상 최고치</span>를 경신한 풀 시황을 방송 전체보기로 다룸. 유가 하락이 소비재 및 테크 기업의 인플레이션 비용 압박을 해소하며 강세장을 견인함.",
            "key_claims": [
                "WTI 유가가 배럴당 72달러선으로 급락하며 인플레이션 완화 호재 작용.",
                "팔란티어 등 빅테크 어닝 서프라이즈와 유가 급락이 결합해 뉴욕증시 랠리 주도."
            ],
            "data_points": [
                "WTI 국제 유가: 당일 -5.2% 급락 마감 (배럴당 72.3달러)",
                "다우존스 산업평균지수: 사상 최고치 경신 마감"
            ],
            "signal": "bullish",
            "signal_reason": "유가 하락에 따른 물가 안정과 다우지수 신고가 경신이 강한 매수 투심 유발.",
            "key_companies": ["팔란티어(PLTR)", "캐터필러(CAT)", "아마존(AMZN)", "엔비디아(NVDA)"],
            "insight": "유가 하락은 연준의 금리 인하 명분을 강화해주며, 실적이 뒷받침되는 미국 증시의 대세 상승 궤적을 굳히는 촉매제임.",
            "action_point": "인플레이션 완화 수혜를 받는 빅테크 우량주 및 소비재 대장주 비중 확대."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy", "tech"],
            "tags": ["오전증시", "유가급락", "다우사상최고치", "뉴욕증시", "삼프로TV"]
        }
    },
    # 22. WwQgD7hkhso - 중국 역대급 의료사고 은폐 (etc)
    {
        "id": "WwQgD7hkhso",
        "analysis": {
            "summary": "중국 내 대형 병원의 역대급 의료 사고 및 장기 매매 은폐 사건이 폭로됨에 따른 사회적 파장과 불투명한 시스템 리스크를 조명함. 중국 바이오 및 헬스케어 섹터에 대한 <span class=\"text-rose-400 font-medium\">글로벌 자본의 신뢰성 훼손</span>이 가속화되고 있음.",
            "key_claims": [
                "중국 의료 체계의 불투명성과 사고 은폐가 중국 바이오 기업들의 글로벌 임상 신뢰성을 깎아내림.",
                "미국 생물보안법(Biosecurity Act) 추진과 맞물려 중국 CDMO 기업 탈출 촉진."
            ],
            "data_points": [
                "중국 주요 헬스케어 지수 하락세 지속",
                "미국 생물보안법 규제 대상 중국 바이오 기업 수주 취소 사례"
            ],
            "signal": "bearish",
            "signal_reason": "중국 헬스케어/바이오 신뢰성 훼손 및 글로벌 투자 자금 유출 반영.",
            "key_companies": ["우시바이오로직스", "삼성바이오로직스(207940)"],
            "insight": "중국 바이오 악재 및 신뢰성 이탈은 국내 반사 수혜를 받는 한국 CDMO 기업(삼성바이오로직스 등)의 대체 불가능한 불씨가 됨.",
            "action_point": "중국 바이오 탈출 수혜를 입는 삼성바이오로직스 및 국내 우량 CDMO 기업에 관심 확대."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": ["stock"],
            "tags": ["중국의료사고", "생물보안법", "중국바이오위험", "CDMO반사수혜", "SOD"]
        }
    },
    # 23. YKVN5RuxOg8 - 월 300만원 은퇴 위험 노후 자산 (economy / stock)
    {
        "id": "YKVN5RuxOg8",
        "analysis": {
            "summary": "은퇴 후 월 300만 원 생활비에 의존하는 고정 자산 구조가 고물가 및 장수 리스크 앞에서 얼마나 취약한지 분석함. 단순 원금 소진형 은퇴관에서 탈피해 <span class=\"text-amber-300 font-bold\">배당 성장주 및 자산배분 현금흐름 체계</span>를 구축해야 은퇴 후 자산 고갈 위험을 막을 수 있음을 강조함.",
            "key_claims": [
                "물가상승률(인플레이션)을 반영하지 못하는 고정 은퇴 자금은 10~15년 후 실질 구매력이 반토막 남.",
                "주식 배당 재투자 및 리밸런싱을 통한 자산 현금흐름 유지가 노후 생활의 핵심 안전판임."
            ],
            "data_points": [
                "연 3% 인플레이션 시 20년 후 300만 원의 실질 가치: 약 166만 원으로 감소",
                "미국 배당성장 ETF(SCHD 등) 10년 평균 배당 성장률: 연 8~10% 수준"
            ],
            "signal": "bullish",
            "signal_reason": "배당 성장주 및 현금흐름 자산배분 기반 노후 준비에 대한 구체적 해법 제시.",
            "key_companies": ["SCHD", "JEPI", "KB금융(105560)"],
            "insight": "은퇴 자산 관리의 본질은 돈을 까먹는 것이 아니라 현금성 배당 이익이 물가 상승률보다 빠르게 늘어나게 만드는 구조를 설계하는 것임.",
            "action_point": "월 배당 ETF 및 국내 우량 고배당주를 적립식으로 모아 은퇴 포트폴리오 강화."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["은퇴준비", "배당성장주", "노후자산관리", "인플레이션리스크", "수페TV"]
        }
    },
    # 24. YwZlX3KMyMw - 팔란티어 15퍼 급등 캐터필러 호실적 (stock / economy)
    {
        "id": "YwZlX3KMyMw",
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">팔란티어(+15% 폭등)</span>의 역대 최대 실적 가이던스 상향과 경기 가늠자인 <span class=\"text-cyan-300 font-semibold\">캐터필러의 어닝 서프라이즈</span>를 뉴욕 브리핑으로 전함. 미-이란 합의 초안 마련 소식으로 엔화 약세가 재개되고 유가가 하락하며 증시 연착륙 랠리를 자극함.",
            "key_claims": [
                "팔란티어의 B2B AI 매출 증가가 실적 가이던스 폭증을 이끌며 주가를 15% 폭등시킴.",
                "중장비 대장주 캐터필러 호실적은 글로벌 인프라 투자 지속성을 입증함."
            ],
            "data_points": [
                "팔란티어(PLTR) 주가: 당일 +15% 폭등 마감",
                "캐터필러(CAT) 영업이익: 시장 예상치 15% 상회"
            ],
            "signal": "bullish",
            "signal_reason": "팔란티어 및 캐터필러의 호실적 발표가 테크와 전통 인프라 동반 강세장 입증.",
            "key_companies": ["팔란티어(PLTR)", "캐터필러(CAT)", "엔비디아(NVDA)"],
            "insight": "AI 소프트웨어(팔란티어)와 전통 중장비 인프라(캐터필러)가 동시 실적 폭발을 기록하는 것은 미 증시의 실적 장세 기반이 단단함을 보여줌.",
            "action_point": "팔란티어 수혜주 및 글로벌 인프라/방산 연관 대장주 저점 매수."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy", "tech"],
            "tags": ["팔란티어폭등", "캐터필러어닝서프라이즈", "뉴욕브리핑", "실적장세", "매경월가월부"]
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
