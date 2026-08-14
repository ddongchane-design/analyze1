import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch5_data = [
    # 25. ZubsEwUFgr0 - 팔란티어 30퍼 폭등 기술주 매도 종료 (stock / space)
    {
        "id": "ZubsEwUFgr0",
        "analysis": {
            "summary": "실적 폭발을 기록한 <span class=\"text-cyan-300 font-semibold\">팔란티어가 시간외 포함 30% 폭등</span>하며 월가에서 \"기술주 매도세가 공식 종료되었다\"는 진단이 나온 소식을 전달함. <span class=\"text-cyan-300 font-semibold\">스페이스X</span> 역시 호실적을 발표했으나 단기 자금 재투자로 보합권을 형성하며 기술주 전반의 강세장 재가동을 알림.",
            "key_claims": [
                "팔란티어의 AIP 가입 고객 수 폭증이 AI 소프트웨어의 실질 수익화 시대를 증명함.",
                "월가 주요 IB들이 기술주 매도 세션의 청산을 선언하고 AI 대장주 저점 매수를 권고."
            ],
            "data_points": [
                "팔란티어(PLTR) 주가: 당일 최대 30% 폭등 기록",
                "스페이스X 스타링크 연간 매출액 가이던스 이익률 35% 달성"
            ],
            "signal": "bullish",
            "signal_reason": "팔란티어의 30% 폭등과 기술주 매도 청산 선언으로 강력한 상방 모멘텀 확보.",
            "key_companies": ["팔란티어(PLTR)", "스페이스X", "엔비디아(NVDA)", "테슬라(TSLA)"],
            "insight": "AI 소프트웨어의 실적 대폭발은 밸류에이션 논란을 잠재우는 최고의 치료제이며 기술주 랠리 2라운드의 개막 신호임.",
            "action_point": "기술주 저점 매도세 종료 신호에 맞춰 팔란티어 및 관련 인프라 수혜주 매수 유지."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["space", "tech"],
            "tags": ["팔란티어30프로폭등", "기술주매도종료", "스페이스X실적", "빅머니LIVE", "매경월가월부"]
        }
    },
    # 26. b6R9NntPR6g - 불공정한 주식시장 개인 대응 전략 (stock / economy)
    {
        "id": "b6R9NntPR6g",
        "analysis": {
            "summary": "공매도, 정보 접근성, 기관 수급 쏠림 등으로 불공정함이 부각되는 국내 주식시장에서 개인 투자자가 승리하는 법으로 <span class=\"text-amber-300 font-bold\">장기 이익 성장이 담보된 대형 우량주 전염 투자</span>와 단기 단타 매매 지양을 제안함. 시장 노이즈를 극복하는 원칙 투자를 강조함.",
            "key_claims": [
                "단기 트레이딩에서는 정보와 시스템을 쥔 기관/외국인에게 개인이 불리할 수밖에 없음.",
                "HBM 및 핵심 주도업종 등 실질 영업이익이 급증하는 1등주에 장기 투자할 때 승률 극대화."
            ],
            "data_points": [
                "개인 단기 트레이더의 연간 손실 확률: 80% 상회",
                "이익 성장 1등주 3년 이상 장기 보유 시 연평균 수익률 15% 상회"
            ],
            "signal": "bullish",
            "signal_reason": "실적 성장 우량주 장기 투자를 통한 불공정 시장 극복 방안 제시.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "HD현대중공업(329180)"],
            "insight": "불공정한 게임장에서 이기는 유일한 길은 판을 바꾸는 것이며, 기관도 팔 수 없는 사상 최대 실적 대장주를 모아가는 것임.",
            "action_point": "잡주 단타를 중단하고 HBM 반도체 및 조선 1등 우량주 위주로 장기 투자 체계 전환."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["불공정시장", "개인투자전략", "장기가치투자", "1등주투자", "아침N투자"]
        }
    },
    # 27. ftsAECXnuDE - 고금리 무릅쓰고 AI투자 늘리는 빅테크 (stock / tech)
    {
        "id": "ftsAECXnuDE",
        "analysis": {
            "summary": "고금리 환경에도 불구하고 빅테크 기업들이 AI CapEx(설비투자)를 꺾지 않고 오히려 대폭 늘리는 이유를 분석함. 주가 일시 조정에도 불구하고 <span class=\"text-cyan-300 font-semibold\">AI 데이터센터 및 반도체 실수요</span>는 꺾이지 않았으며, <span class=\"text-cyan-300 font-semibold\">SK하이닉스·삼성전자</span>의 HBM 공급 부족 구조가 지속됨을 김장열 유니스토리 센터장이 정밀 진단함.",
            "key_claims": [
                "빅테크의 AI 투자 축소 우려는 기우이며, 빅4 합산 CapEx는 전년비 30% 이상 계속 확장.",
                "HBM3E 및 HBM4의 2026년 완판 상태가 유지되어 한국 메모리 기업들의 강한 마진 지지."
            ],
            "data_points": [
                "2026년 빅테크 4사 합산 CapEx: 2,000억 달러 이상 최고치 경신",
                "SK하이닉스 HBM 2026년 생산 물량 완판 공시"
            ],
            "signal": "bullish",
            "signal_reason": "빅테크 AI CapEx 확장 지속 및 한국 HBM 반도체 완판 호재 정밀 반영.",
            "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "엔비디아(NVDA)", "마이크로소프트(MSFT)"],
            "insight": "반도체 주가 조정은 단기 수급 불균형 때문이며, 빅테크의 천문학적 AI 투자금이 계속 흘러드는 한 메모리 슈퍼사이클은 정당함.",
            "action_point": "반도체 조정 시 쫄지 말고 SK하이닉스 및 삼성전자를 분할 저점 매수."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["고금리AI투자", "빅테크CapEx", "SK하이닉스", "삼성전자", "오늘의주식"]
        }
    },
    # 28. jyVCxZzayzs - 태풍 시원해지는 과학 (etc)
    {
        "id": "jyVCxZzayzs",
        "analysis": {
            "summary": "태풍이 통과한 후 기온이 일시적으로 낮아지거나 시원해지는 <span class=\"text-amber-300 font-bold\">대기 혼합 및 연안 상승류 열교환 과학</span>을 해설함. 차가운 하층 해수면 물이 상층으로 섞이며 기온 변동을 일으키는 지형 기상 메커니즘을 전달함.",
            "key_claims": [
                "태풍의 강한 바람이 해수면 상하층을 뒤섞어 수온을 일시적으로 떨어뜨림.",
                "태풍 통과 후 북쪽의 찬 공기 유입 여부에 따라 기온 하강 폭이 달라짐."
            ],
            "data_points": [
                "태풍 통과 후 해수면 수온 하강 폭: 약 1~3℃ 하향 효과",
                "폭염 해소 지속 기간 평균 2~3일 유효"
            ],
            "signal": "na",
            "signal_reason": "순수 자연 기상학 관련 교양 지식 콘텐츠로 직접적 금융 시그널 없음.",
            "key_companies": [],
            "insight": "기상 변화는 지구 열 균형을 맞추는 자연의 피드백이며, 환경 변화 지표를 상식 차원에서 파악함.",
            "action_point": "여름철 기후 및 열파 관련 이슈를 참고 자료로 상식 체득."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["태풍과기온", "해수면혼합", "기상과학", "안될과학"]
        }
    },
    # 29. kbsosU9QyJ8 - 한국주식 묻어두면 안되는 이유 (stock / economy)
    {
        "id": "kbsosU9QyJ8",
        "analysis": {
            "summary": "한국 주식시장이 미국과 달리 <span class=\"text-rose-400 font-medium\">주도주가 매년 바뀌는 높은 변동성 구조</span>를 가지고 있어 무작정 장기 방치(무지성 장기투자)하는 것이 위험할 수 있음을 분석함. 산업 사이클 변화와 <span class=\"text-amber-300 font-bold\">시장의 수급 주도주 교체</span>에 발맞춘 정기적 리밸런싱이 필수적임.",
            "key_claims": [
                "코스피는 지수 박스피 특성상 10년 전 시총 상위주 중 살아남은 기업 비중이 낮음.",
                "단순 묻어두기 투자가 아니라 사이클 펀더멘털을 확인하며 주도 섹터(반도체/방산/차세대)로 정기 교체해야 함."
            ],
            "data_points": [
                "과거 10년 간 코스피 시총 상위 10개 기업 주도주 교체율: 60% 상회",
                "미국 S&P500 우상향 우수성과 코스피 박스권 변동성 비교"
            ],
            "signal": "neutral",
            "signal_reason": "한국 증시의 특성에 맞는 주기적 액티브 리밸런싱 전략 필요성 강조.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "POSCO홀딩스(005490)"],
            "insight": "국내 투자는 미국식 장기 방치 투자가 아닌, 이익 사이클이 상향되는 주도 섹터(현재 반도체/방산)를 쥔 채 주기적으로 포트폴리오를 점검하는 능동성이 핵심임.",
            "action_point": "퇴물 섹터를 정리하고 현재 이익이 증가하는 주도주 중심으로 포트폴리오 정기 리밸런싱."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["주도주교체", "한국주식특성", "리밸런싱", "장기투자주의", "교양이를부탁해"]
        }
    },
    # 30. klQhgmoXvUg - 트럼프에 현혹 말라 엔비디아 거센 후폭풍 (tech / stock)
    {
        "id": "klQhgmoXvUg",
        "analysis": {
            "summary": "트럼프의 대중국 반도체 추가 제재 및 정치적 언론 수사에 현혹되지 말고, <span class=\"text-cyan-300 font-semibold\">엔비디아 블랙웰(Blackwell) 출하</span>와 빅테크 CapEx의 실질 현금흐름을 체크할 것을 지적함. 정치 노이즈 뒤에 숨겨진 <span class=\"text-cyan-300 font-semibold\">AI 랠리의 진짜 돈줄(클라우드 수주)</span>을 정밀 파헤침.",
            "key_claims": [
                "정치적 립서비스와 미-중 선거 노이즈보다 엔비디아의 블랙웰 칩 양산 수율이 핵심임.",
                "빅테크의 클라우드 매출 성장이 지속되는 한 엔비디아 후폭풍은 일시적 해프닝에 불과함."
            ],
            "data_points": [
                "엔비디아 Blackwell B200 랙 스케일 출하량 가이던스 유지",
                "미국 빅테크 클라우드 합산 분기 매출액 사상 최대 기록"
            ],
            "signal": "bullish",
            "signal_reason": "정치 노이즈를 뛰어넘는 엔비디아 및 AI 클라우드 펀더멘털 견고함 반영.",
            "key_companies": ["엔비디아(NVDA)", "SK하이닉스(000660)", "TSMC(TSM)"],
            "insight": "정치적 소음은 펀더멘털을 흔들지 못하며, 엔비디아 블랙웰 양산과 HBM3E/4 공급망이 AI 랠리의 진정한 본체임.",
            "action_point": "트럼프 노이즈로 엔비디아 및 SK하이닉스가 일시 조정받을 때 적극 매수 대응."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock", "economy"],
            "tags": ["엔비디아후폭풍", "트럼프노이즈", "블랙웰B200", "AI돈줄", "교양이를부탁해"]
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
