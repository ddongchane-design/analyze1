import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agents.harness import validate_item

batch2_data = [
    # 7. CDcNeA-L52k - ISA 5년 만기 제한 논란 (stock / economy)
    {
        "id": "CDcNeA-L52k",
        "analysis": {
            "summary": "개인자산관리계좌(ISA)의 <span class=\"text-rose-400 font-medium\">5년 만기 재가입 제한</span> 세제 규정이 복리 효과를 저해하고 장기 투자자들의 10~20년 자산 증식 계획을 가로막는 세제 불합리성을 비판함. 금융투자소득세 개편과 맞물려 장기 저축성 <span class=\"text-amber-300 font-bold\">자산 형성 세제 혜택 확대</span> 필요성을 역설함.",
            "key_claims": [
                "ISA 5년 만기 강제 해지 및 재가입 조항이 의무 가입 기간 갱신 시 불필요한 세금 비과세 한도 소진 유발.",
                "장기 가치 투자를 유도하기 위해서는 영구 비과세 및 만기 연장 혜택이 부여되어야 함."
            ],
            "data_points": [
                "국내 ISA 총 가입자 수: 500만 명 돌파",
                "ISA 계좌 내 비과세 한도: 일반형 200만 원, 서민형 400만 원 산정"
            ],
            "signal": "neutral",
            "signal_reason": "세제 개편 논란으로 인한 자산 형성제도 제도적 불확실성 반영.",
            "key_companies": [],
            "insight": "자산배분 투자자에게 ISA 계좌는 필수 장기 무기이나, 제도적 만기 제한 노이즈를 감안해 계좌 해지 및 재가입 시점을 전략적으로 계산해야 함.",
            "action_point": "ISA 만기 도래 시 연금저축 계좌 이전 및 비과세 한도 재활용 전략을 세울 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["ISA계좌", "세제혜택", "장기투자", "복리효과", "이효석아카데미"]
        }
    },
    # 8. EdI7nnuTwzU - 코스피 6000 버티면 8000 목표 9300 (stock / economy)
    {
        "id": "EdI7nnuTwzU",
        "analysis": {
            "summary": "대신증권 리서치센터의 장기 코스피 타깃 지수 전망(6,000선 하단 지지 시 장기 8,000~9,300 포인트 목표)을 정밀 분석함. <span class=\"text-cyan-300 font-semibold\">한국 반도체 및 방산 이익 성장</span>과 정부 밸류업 정책이 맞물려 한국 증시의 장기 밸류에이션 리레이팅이 전개될 것을 역설함.",
            "key_claims": [
                "코스피 지수는 단기 변동성에도 불구하고 글로벌 AI 반도체 공급망 중심축으로서 이익 체력이 급증함.",
                "PBR 1.0배 탈출과 주주환원 확대 정책이 성공할 경우 장기 지수 목표 달성 가능."
            ],
            "data_points": [
                "대신증권 제시 코스피 상방 타깃: 장기 8,000~9,300pt 시나리오 제시",
                "한국 기업 합산 영업이익: 2026년 역대 최대 경신 전망"
            ],
            "signal": "bullish",
            "signal_reason": "한국 증시의 펀더멘털 기반 상방 잠재력 및 장기 밸류에이션 재평가 강한 낙관론.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "KB금융(105560)"],
            "insight": "코스피의 상방은 닫혀있는 것이 아니며, HBM을 쥔 반도체와 주주환원이 결합될 때 지수는 대세 상승 길목에 진입함.",
            "action_point": "단기 급락 조정에 흔들리지 말고 한국 대표 실적주 및 밸류업 지수 편입주 매수 체계 유지."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy", "tech"],
            "tags": ["코스피전망", "대신증권", "리레이팅", "밸류업", "여의도인사이트"]
        }
    },
    # 9. Esdy2Wum9Ts - 한국 반도체 주가 향방 증명할 것 (stock / tech)
    {
        "id": "Esdy2Wum9Ts",
        "analysis": {
            "summary": "한국 반도체 기업 주가 향방의 핵심 결정 요인으로 <span class=\"text-cyan-300 font-semibold\">HBM4 커스텀 로직 다이 수율</span>과 <span class=\"text-cyan-300 font-semibold\">빅테크 AI CapEx의 잉여현금 이익 입증</span>을 제시함. 3분기 실적 발표에서 메모리 업체들이 가격 상승세 지속성을 증명하는 것이 주가 반등의 키임.",
            "key_claims": [
                "HBM3E 공급 과잉 우려는 허구이며 HBM4 기술 진화 과정에서의 수율 입증이 핵심임.",
                "빅테크의 AI 투자 지속성과 메모리 가격(ASP) 상승이 확인되어야 반도체 주가 멀티플 상향."
            ],
            "data_points": [
                "HBM4 커스텀 다이 핀 속도: 최대 13~16Gbps 달성",
                "삼성전자 및 SK하이닉스 2026년 HBM 출하 비중: 전체 D램 매출의 30% 이상"
            ],
            "signal": "bullish",
            "signal_reason": "HBM 선점과 ASP 상승에 힘입어 한국 메모리 반도체 실적 우상향 지속.",
            "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "TSMC(TSM)"],
            "insight": "반도체주 주가는 소문에 흔들릴 수 있지만 결국 ASP 상승과 HBM4 수율이라는 실질 숫자가 주가를 우상향시킴.",
            "action_point": "반도체 주가 조정 시 HBM 독점력을 가진 SK하이닉스 및 삼성전자 저점 분할 매수."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech"],
            "tags": ["한국반도체향방", "HBM4수율", "SK하이닉스", "삼성전자", "글로벌인터뷰"]
        }
    },
    # 10. FxJ9qPhjDmg - 주도주 안 돌아온다 삼전닉스 이후 준비 (stock / tech)
    {
        "id": "FxJ9qPhjDmg",
        "analysis": {
            "summary": "삼전닉스 중심의 반도체 쏠림 장세 이후를 준비하는 포트폴리오 전략으로 <span class=\"text-cyan-300 font-semibold\">차세대 주도주(피지컬 AI 로봇, 바이오, 방산)</span>로의 확산 가능성을 정밀 진단함. 반도체 랠리가 정체될 때 자금이 흘러갈 <span class=\"text-amber-300 font-bold\">후속 실적 주도주</span>를 선점할 것을 권고함.",
            "key_claims": [
                "반도체 대장주가 쉴 때 시장의 유동성은 다음 이익 개폭발 섹터(방산, 바이오, 로봇)로 이동함.",
                "단일 테마 몰빵 투자는 사이클 변동에 취약하므로 섹터 간 순환매 차단막 구축 필요."
            ],
            "data_points": [
                "바이오/방산 수주잔고 증가율: 전년 대비 40% 이상 증대",
                "코스닥 로봇/바이오 거래대금 비중 점진적 상승"
            ],
            "signal": "bullish",
            "signal_reason": "주도주 다변화 및 후속 이익 성장 섹터로의 순환매 확장 호재 반영.",
            "key_companies": ["삼성바이오로직스(207940)", "한화에어로스페이스(012450)", "레인보우로보틱스(277810)"],
            "insight": "삼전닉스 다음을 준비하는 자만이 주도주 교체기에서도 안정적인 복리 수익을 챙길 수 있음.",
            "action_point": "반도체 이외에 이익 성장성이 확실한 방산 및 바이오 대장주를 포트폴리오에 20~30% 편입."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "robot"],
            "tags": ["삼전닉스이후", "차세대주도주", "방산바이오", "순환매", "주린이구조대"]
        }
    },
    # 11. GOvNGd_TZPg - 한국 외환 후진국 리스크 (economy / stock)
    {
        "id": "GOvNGd_TZPg",
        "analysis": {
            "summary": "런던 외환 트레이더 김준규 대표와의 정밀 인터뷰를 통해 한국 외환 시장의 역외 거래 한계와 <span class=\"text-rose-400 font-medium\">원/달러 환율 구조적 변동성 리스크</span>를 파헤침. NDF 시장 외화 수급 불균형이 코스피 외국인 자금 유출입을 증폭시키는 취약한 외환 구조를 지적함.",
            "key_claims": [
                "한국 외환 시장의 폐쇄적 거래 시간과 얇은 수급층이 환율 급변동을 가속화함.",
                "외국인 투자자 입장에서 원화 환리스크 헤지 비용이 증가하여 패시브 자금 진입의 걸림돌 작용."
            ],
            "data_points": [
                "원/달러 환율 NDF 역외 거래대금 비중: 서울 외환시장 거래량 상회",
                "한국 MSCI 선진국 지수 편입 걸림돌 1위: 외환시장 개방성 부족"
            ],
            "signal": "neutral",
            "signal_reason": "외환 시장 구조 개혁 과제 및 환율 변동성에 따른 증시 관망 기조.",
            "key_companies": [],
            "insight": "환율은 증시의 거울이며, 원화의 외환 시장 개방 및 구조 개선이 전제되어야 한국 증시의 만년 저평가(코리아 디스카운트)가 해소됨.",
            "action_point": "원/달러 환율 변동 시 외국인 수급 이동 패턴을 체크하고 환율 안정 시점 저점 매수."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["stock"],
            "tags": ["외환후진국", "원달러환율", "NDF역외거래", "MSCI선진국", "언더스탠딩"]
        }
    },
    # 12. HGAfB97Z4Kk - 물타기 금지 본전심리 극복 (stock / economy)
    {
        "id": "HGAfB97Z4Kk",
        "analysis": {
            "summary": "하락하는 나쁜 종목에 무분별하게 물타기를 실행하는 투자자들의 <span class=\"text-rose-400 font-medium\">본전 심리(Sunk Cost Fallacy)</span> 위험을 경고함. 펀더멘털이 훼손된 종목의 물타기는 계좌의 기회비용을 박탈하므로, <span class=\"text-amber-300 font-bold\">확실한 주도주 저점 매수</span>로 교체 매매할 것을 제안함.",
            "key_claims": [
                "본전 심리에 사로잡혀 손실 종목에 물을 타면 계좌 전체가 정체되고 기회비용을 잃게 됨.",
                "주가가 내린 종목보다 이익이 상향되는 주도 우량주로의 잡초 솎아내기 교체 매매가 필수적임."
            ],
            "data_points": [
                "개인 투자자 물타기 종목 손실 보존률: 20% 미만 저조",
                "이익 상향 주도주 교체 매매 시 계좌 회복 속도 3배 고속"
            ],
            "signal": "bullish",
            "signal_reason": "잡초 종목 과감한 손절 및 핵심 실적 우량주 집중을 통한 계좌 회복 가이드.",
            "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
            "insight": "투자의 성공은 잃은 종목에서 본전을 찾는 것이 아니라, 가장 강하고 확실한 종목으로 자금을 옮겨 복리로 계좌를 회복하는 데 있음.",
            "action_point": "모멘텀을 잃은 잡동사니 종목을 정리하고 HBM 및 방산 대장주로 교체 매수."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy"],
            "tags": ["물타기금지", "본전심리", "교체매매", "계좌회복", "주린이구조대"]
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
