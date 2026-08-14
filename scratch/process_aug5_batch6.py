import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch6_data = [
    # 1. 08rbkZEGD5I - 나무 아파트 건축 과학 (etc)
    {
        "id": "08rbkZEGD5I",
        "analysis": {
            "summary": "철골과 콘크리트보다 탄소 배출이 적고 구조적 강도가 우수한 <span class=\"text-cyan-300 font-semibold\">목조 공학 목재(CLT)</span>를 활용한 고층 아파트 건축의 과학적 원리를 다룸. 친환경 건축 자재 수요 급증과 <span class=\"text-amber-300 font-bold\">스마트 목조 공학</span>의 탄소 중립 효과를 해설함.",
            "key_claims": [
                "직교 적층 목재(CLT) 공법으로 10층 이상의 고층 마천루 건축이 가능해짐.",
                "탄소 포집 효과 및 콘크리트 대비 건축 공기 단축으로 친환경 스마트 건설의 대안 부상."
            ],
            "data_points": [
                "CLT 구조목 단위 강도: 기존 콘크리트 대비 2배 이상 우수",
                "건축 탄소 배출 절감률: 기존 공법 대비 40% 절감"
            ],
            "signal": "na",
            "signal_reason": "친환경 건축 자재 공학 교양 콘텐츠로 직접적인 금융 시그널과 무관함.",
            "key_companies": [],
            "insight": "친환경 신소재 건축 공학은 탄소 배출권 거래 및 ESG 규제 강화 시대를 대비하는 스마트 건설의 필수 지식임.",
            "action_point": "친환경 건축 신소재 및 모듈러 건축 관련 기술 보유 기업의 상식 차원 모니터링."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": ["energy"],
            "tags": ["CLT목조건축", "친환경소재", "탄소중립", "스마트건축", "안될과학"]
        }
    },
    # 2. 7Ed117Du39g - 팔란티어 대폭등 다음분기 하락 논란 (stock / tech)
    {
        "id": "7Ed117Du39g",
        "analysis": {
            "summary": "역대급 어닝 서프라이즈로 당일 15~30% 대폭등을 기록한 <span class=\"text-cyan-300 font-semibold\">팔란티어(PLTR)</span>의 주가 행보와 월가 일각에서 제기된 '다음 분기 성장률 둔화 우려'를 정밀 조명함. 높은 밸류에이션 부담에도 불구하고 <span class=\"text-cyan-300 font-semibold\">B2B AI AIP 수주</span>가 지속되는 한 주가 상방 압력이 우세함.",
            "key_claims": [
                "팔란티어의 AIP 플랫폼 매출 성장세가 30% 이상 폭발하며 B2B AI 최강자 입증.",
                "월가 일각의 다음 분기 착시 하락론은 밸류에이션 부담에 따른 기술적 수급 노이즈일 뿐 펀더멘털은 견고함."
            ],
            "data_points": [
                "팔란티어(PLTR) 실적 발표 당일 주가 상승률: +15%~+30% 기록",
                "AIP 플랫폼 가입 기업 수: 전 분기 대비 40% 폭증"
            ],
            "signal": "bullish",
            "signal_reason": "실적 대폭발 및 AIP B2B AI 플랫폼 수주 확정에 따른 강력한 상방 지지.",
            "key_companies": ["팔란티어(PLTR)", "엔비디아(NVDA)", "마이크로소프트(MSFT)"],
            "insight": "팔란티어는 AI 산업에서 진짜 현금을 버는 독보적 AI 파이프라인이며, 단기 밸류에이션 조정은 저점 진입 찬스를 제공함.",
            "action_point": "팔란티어의 시간외 및 개장 후 주가 눌림목 구간에서 분할 매수 전략 추천."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech"],
            "tags": ["팔란티어실적", "AIP플랫폼", "PLTR폭등", "월가반응", "월텍남"]
        }
    },
    # 3. n74QojP0g7k - 8월 4일 오후 코스피 거래대금 급감 코스닥 반등 (stock / economy)
    {
        "id": "n74QojP0g7k",
        "analysis": {
            "summary": "8월 4일 오후 장 마감 결과, 코스피가 거래대금 급감 속에 관망세를 보인 반면 <span class=\"text-cyan-300 font-semibold\">코스닥 반도체·바이오 소부장</span>으로 자금이 이동하며 차별화 반등이 나타난 마감 시황을 다룸. 대형주 쏠림 완화 이후 나타나는 <span class=\"text-amber-300 font-bold\">중소형주 순환매 장세</span>를 파헤침.",
            "key_claims": [
                "코스피 거래대금이 감소하며 지수가 박스권 횡보를 보인 반면 코스닥으로 온기가 확산.",
                "반도체 대장주 조정 틈을 타 기술력 우수 코스닥 소부장 장비주로 순환매 유입."
            ],
            "data_points": [
                "8월 4일 코스피 거래대금: 8.5조 원 수준 소강",
                "코스닥 반도체 장비 업종 상승률: 코스피 대비 +2%p 상회"
            ],
            "signal": "bullish",
            "signal_reason": "코스닥 중소형 실적주로의 온기 확산 및 순환매 활성화 호재 지지.",
            "key_companies": ["삼성전자(005930)", "원익IPS(030530)", "유진테크(084370)"],
            "insight": "대형주 거래대금이 잠시 쉴 때는 수급 빈집 상태인 코스닥 전공정 장비 및 바이오 실적 우량주가 최고의 대체 주도주로 활약함.",
            "action_point": "코스닥 실적 성장 반도체 장비주 및 우량 소부장에 20~30% 비중 분할 편입."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["오후증시", "거래대금급감", "코스닥반등", "순환매장세", "삼프로TV"]
        }
    },
    # 4. prrBYlmS3J0 - 코스피 구할 방법 밸류업 (stock / economy)
    {
        "id": "prrBYlmS3J0",
        "analysis": {
            "summary": "코스피의 만년 저평가(코리아 디스카운트)를 구하고 3,000~4,000 시 시대를 열 핵심 열쇠로 <span class=\"text-amber-300 font-bold\">주주환원율(자사주 소각 및 소액주주 권익) 강제</span>와 지배구조 상법 개정을 촉구함. 장기투자 문화 정착과 <span class=\"text-cyan-300 font-semibold\">정부 밸류업 지수 개편</span>이 필수적임.",
            "key_claims": [
                "국내 기업들의 낮은 자사주 소각률과 주주 환원 부재가 코스피 PBR 1.0배 이하 저평가의 주범임.",
                "상법 개정(이사 충실 의무 대상에 주주 포함)이 이뤄질 때 외국인 패시브 자금이 50조 원 이상 유입 가능."
            ],
            "data_points": [
                "한국 증시 주주환원율: 약 25% (미국 80%, 일본 50% 대비 현저히 낮음)",
                "밸류업 지수 개편 시 수혜 기대 금융/지주사 PBR 0.5배 하회"
            ],
            "signal": "bullish",
            "signal_reason": "주주환원 확대 정책 및 상법 개정 추진에 따른 코스피 저평가 해소 모멘텀.",
            "key_companies": ["KB금융(105560)", "신한지주(055550)", "삼성물산(028260)"],
            "insight": "코스피의 진짜 바닥을 구하는 무기는 기업들의 자사주 소각과 배당 확대이며, 밸류업 수혜 대형 금융주와 지주사는 안전한 상방 승부처임.",
            "action_point": "주주환원율이 높은 밸류업 지수 핵심 금융주 및 저PBR 지주사 비중 확대."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["코스피구하기", "밸류업", "주주환원율", "상법개정", "더블밸류업"]
        }
    },
    # 5. ub340z5199k - 클래리티 법안 통과 확률 27퍼 급락 (crypto / economy)
    {
        "id": "ub340z5199k",
        "analysis": {
            "summary": "미국 의회에서 <span class=\"text-violet-300 font-medium\">가상자산 클래리티 법안(Clarity Act)</span>의 연내 통과 확률이 윤리 수정안 마찰로 50%에서 27%로 급락한 악재 신호를 다룸. 입법 지연 우려로 인해 비트코인 및 알트코인 시장에 단기 관망 수급이 고조되고 있음.",
            "key_claims": [
                "미국 양당 간 윤리 수정안 마찰로 가상자산 규제 명확화 법안의 연내 표결이 지연될 리스크 커짐.",
                "법안 통과 지연 시 기관 자금 유입 속도가 일시적으로 둔화될 가능성."
            ],
            "data_points": [
                "Polymarket 기준 클래리티 법안 연내 통과 확률: 50% -> 27% 급락",
                "비트코인(BTC) 6만 4천 달러선 박스권 하단 테스트"
            ],
            "signal": "bearish",
            "signal_reason": "미국 규제 명확화 입법 지연 우려에 따른 크립토 시장 단기 악재 반영.",
            "key_companies": ["코인베이스(COIN)", "마이크로스트래티지(MSTR)"],
            "insight": "클래리티 법안의 통과 확률 하락은 단기 악재이나, 가상자산 제도권 진입이라는 거시적 대세 흐름을 바꿀 수는 없음.",
            "action_point": "입법 노이즈에 따른 비트코인 하락 시 추가 매수 찬스로 활용하되 중소형 알트코인 비중 축소."
        },
        "classification": {
            "primary_topic": "crypto",
            "secondary_topics": ["economy"],
            "tags": ["클래리티법안", "통과확률급락", "가상자산규제", "비트코인박스권", "크립토PLUS"]
        }
    },
    # 6. wjZaCA-8Hec - 데이터센터 옆 발전소 미국 전력난 (energy / stock)
    {
        "id": "wjZaCA-8Hec",
        "analysis": {
            "summary": "빅테크들이 AI 전력난을 해결하기 위해 <span class=\"text-amber-300 font-bold\">데이터센터 바로 옆에 전용 발전소(원자력/가스)</span>를 직접 건설하기 시작한 시장 최대 수혜주를 파헤침. 전력망 구축 지연을 우회하는 독립 전력망 및 <span class=\"text-cyan-300 font-semibold\">초고압 변압기/SMR</span> 관련 기업들의 사상 최대 수주 붐을 진단함.",
            "key_claims": [
                "미국 전력망 송전선 인허가에 3~5년이 걸리자 빅테크가 데이터센터 직결 발전소 건설로 방향 전환.",
                "가스 발전 및 SMR(소형모듈원자로), 초고압 변압기를 공급하는 전력 인프라 기업들이 최대 수혜."
            ],
            "data_points": [
                "미국 AI 데이터센터 직결 발전소 수주 규모: 2026년 조 단위 돌파",
                "HD현대일렉트릭, 효성중공업 수주잔고 연 40% 이상 폭증"
            ],
            "signal": "bullish",
            "signal_reason": "AI 데이터센터 전력 병목 해결을 위한 민간 발전 및 변압기 시장 폭발 호재.",
            "key_companies": ["HD현대일렉트릭(267260)", "효성중공업(298040)", "GE버노바(GEV)", "뉴스케일파워(SMR)"],
            "insight": "AI 투자의 핵심 제약인 '전력난'을 해결하는 가장 빠른 길은 데이터센터 직결 발전소이며, 이 분야 수혜주는 확실한 실적 우상향 엔진을 달음.",
            "action_point": "변압기 및 독립 전력망 수혜주(HD현대일렉트릭, 효성중공업)의 눌림목 매수 유효."
        },
        "classification": {
            "primary_topic": "energy",
            "secondary_topics": ["stock", "tech"],
            "tags": ["데이터센터발전소", "미국전력난", "변압기수혜", "SMR원자력", "이효석아카데미"]
        }
    },
    # 7. yCmLJYxYPjk - HBM4 가격 상승 원인 계산법 (tech / stock)
    {
        "id": "yCmLJYxYPjk",
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">HBM4 가격이 급등하는 이유</span>를 1b나노 D램 코어 다이 공정과 <span class=\"text-cyan-300 font-semibold\">4나노/3나노 파운드리 베이스 다이 단가</span>의 계산법을 통해 기술 경제학적으로 정밀 해설함. 로직 공정 융합으로 단가가 3~4배 상승함에 따라 메모리 제조사들의 마진율 폭증이 상등함.",
            "key_claims": [
                "HBM4부터 아랫단 베이스 다이에 스마트폰 AP급 선단 로직 공정(4나노/3나노)이 필수 적용되어 제조 원가와 판매가가 급증.",
                "삼성전자와 SK하이닉스-TSMC의 베이스 다이 수율 차이가 HBM4 시대의 이익률 향방을 결정짓게 됨."
            ],
            "data_points": [
                "HBM4 단가: 기존 HBM3E 대비 50%~100% 이상 판가(ASP) 상승 전망",
                "베이스 다이 로직 공정 비용 비중: 전체 HBM4 칩 원가의 30% 돌파"
            ],
            "signal": "bullish",
            "signal_reason": "HBM4 단가 상승(ASP 폭등)에 따른 한국 메모리 기업들의 역사적 최고 마진율 경신 기대.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "TSMC(TSM)", "시놉시스(SNPS)"],
            "insight": "HBM4 가격 상승은 단점이나 메모리 업체 입장에서는 파운드리급 고부가 마진을 챙기는 천재일우의 기회이며 주가 상승의 직결 연료임.",
            "action_point": "HBM4 판가 상승 및 베이스 다이 수율 모멘텀에 발맞추어 삼성전자 및 SK하이닉스 매수 강하게 유지."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock"],
            "tags": ["HBM4가격상승", "베이스다이단가", "삼성전자", "SK하이닉스", "안될공학"]
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
