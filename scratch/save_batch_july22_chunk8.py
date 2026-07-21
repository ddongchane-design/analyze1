import json
from pathlib import Path

def save_and_delete(video_id, primary_topic, secondary_topics, tags, analysis_data):
    pending_path = Path(f"data/pending/{video_id}.json")
    if not pending_path.exists():
        print(f"Error: {pending_path} does not exist.")
        return
        
    pending_data = json.loads(pending_path.read_text(encoding="utf-8"))
    video_data = pending_data["video"]
    
    classification_data = {
        "primary_topic": primary_topic,
        "secondary_topics": secondary_topics,
        "tags": tags
    }
    
    analyzed_dir = Path(f"data/analyzed/{primary_topic}")
    analyzed_dir.mkdir(parents=True, exist_ok=True)
    
    result_path = analyzed_dir / f"{video_id}.json"
    result_path.write_text(
        json.dumps({
            "video": video_data,
            "analysis": analysis_data,
            "classification": classification_data
        }, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"Saved: {result_path}")
    
    pending_path.unlink()
    print(f"Deleted pending: {pending_path}")
    
    synthesis_cache = Path(f"data/synthesis/{primary_topic}.json")
    if synthesis_cache.exists():
        synthesis_cache.unlink()

batch_8 = {
  "rVETeBo2H9c": {
    "primary_topic": "tech",
    "secondary_topics": ["crypto", "stock"],
    "tags": ["DTCC토큰화", "실시간결제T0", "게임스탑사태진실", "증거금대란해소", "블록체인증권"],
    "analysis": {
      "summary": "미국 예탁결제원(DTCC)이 7월 15일 주식 증권 토큰화 파일럿을 전격 시작했습니다. 과거 게임스탑 사태 당시 로빈후드가 매수 버튼을 뽑았던 근본 원인은 T+2 청산 시차 동안 결제소 증거금(37억 달러) 부담 때문이었으나, 블록체인 기반 T+0 실시간 결제 토큰화가 도입됨에 따라 마진콜 및 유동성 대란 없는 차세대 미 증권 시장 결제망이 완성될 것입니다.",
      "key_claims": [
        "DTCC의 7월 15일 토큰화 파일럿 런칭은 기존 T+2 결제 시차에 따른 결제소 증거금 대란과 매수 버튼 뽑기 파행을 근본 해소한다.",
        "블록체인 상의 T+0 실시간 결제 인프라는 증권사의 담보 납입 유동성 위험을 제로화하여 자본 효율성을 비약적으로 높인다."
      ],
      "data_points": [
        "DTCC 토큰화 증권 파일럿 시작일: 2026년 7월 15일"
      ],
      "signal": "positive",
      "signal_reason": "DTCC의 토큰화 실시간 결제 도입으로 미국 증권 시장의 유동성 청산 위험이 소멸하고 블록체인 금융(RWA)의 상용화가 가속화되기 때문입니다.",
      "key_companies": ["Robinhood(HOOD)", "Coinbase(COIN)"],
      "insight": "주식 토큰화는 단순 코인 이슈가 아닌 미국 금융 백엔드 50년 배관의 대혁신입니다. T+0 실시간 결제는 증권 시장의 제도적 안정성을 극대화합니다.",
      "action_point": "RWA 토큰화 및 암호화폐 결제 백엔드 솔루션사(코인베이스, 로빈후드)의 성장성에 주목해야 합니다."
    }
  },
  "yh6Uy6L3As4": {
    "primary_topic": "crypto",
    "secondary_topics": ["stock", "economy"],
    "tags": ["클래리티법안합의", "백악관윤리조항", "중동휴전모멘텀", "트럼프지지율", "가상자산법안"],
    "analysis": {
      "summary": "백악관이 크립토 클래리티 법안(Clarity Act)의 윤리 조항 패키지에 전격 동의하며 법안 상원 상정 가능성이 급부상했습니다. 미군 사상자 발생 및 후티의 바브엘만데브 해협 봉쇄 악재 속에서도 물밑 10일 휴전 협상 소식이 전달되며 시장 불안 심리가 다소 안정화되고 있습니다.",
      "key_claims": [
        "백악관이 클래리티 법안의 핵심 걸림돌이었던 윤리 조항에 합의함에 따라 가상자산 규제 명확성 법안 통과 가시성이 대폭 높아졌다.",
        "미중동 군사 갈등 속에서도 물밑 10일 휴전안 타진이 전개되며 원유 공급 차질 공포가 기술적 반등으로 완화되었다."
      ],
      "data_points": [
        "트럼프 지지율: 40.5% (취임 직후 53% 대비 하락세 유지)"
      ],
      "signal": "positive",
      "signal_reason": "백악관의 클래리티 법안 윤리 조항 합의로 가상자산 제도화 통과 가능성이 극대화되고 지정학적 휴전 타진이 호재로 작용하기 때문입니다.",
      "key_companies": ["Coinbase(COIN)", "Circle"],
      "insight": "크립토 클래리티 법안 통과 가능성은 가상자산의 법적 지위를 보장하는 역사적 이정표입니다. 기관 자금 유입의 대물꼬가 틉니다.",
      "action_point": "법안 통과 수혜주인 코인베이스 및 비트코인 현물 ETF 관망 자금의 유입에 맞춰 매수 관점을 유지합니다."
    }
  },
  "EeCisxB7z0M": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["키미K3가격비교", "오픈웨이트메모리", "하이닉스ADR스프레드", "구글자체TPU", "중동협상"],
    "analysis": {
      "summary": "뉴욕증시 브리핑은 중동 긴장감 속에서도 중국 Kimi K3가 과제당 $0.95 비용으로 오픈AI($1.04) 대비 불과 10% 저렴한 수준에 머물러 딥시크식 '치킨 게임' 우려를 무력화했다고 전했습니다. 스마트카르마의 더글라스 킴은 SK하이닉스 미국 ADR 프리미엄(30~50%)이 15%선으로 축소되는 차익거래가 전개되며 본주 반등 탄력이 강화될 것으로 분석했습니다.",
      "key_claims": [
        "Kimi K3의 운용 비용은 오픈AI 최첨단 모델 대비 10% 저렴한 수준으로, 시장을 왜곡하는 덤핑이 아니며 오픈 웨이트 특성상 메모리 시장 전체 파이를 키운다.",
        "미국 SK하이닉스 ADR에 붙었던 30~50%의 과도한 프리미엄이 15%로 축소되며 본주와 ADR 간 차익거래 매수세가 강하게 유입되고 있다.",
        "구글이 2028년 배치를 목표로 제미나이 최적화 전용 칩을 개발하여 비구조적 데이터 속도를 개선하고 있다."
      ],
      "data_points": [
        "Kimi K3 vs OpenAI 과제당 운용 비용: $0.95 vs $1.04 (불과 10% 차이)",
        "SK하이닉스 ADR 프리미엄: 기존 30~50%에서 15% 수준으로 축소 진행 중"
      ],
      "signal": "positive",
      "signal_reason": "Kimi K3 노이즈 해소와 SK하이닉스 ADR 차익거래 유입, 구글 등의 AI 투자 확대가 확인되어 반도체 본주 반등을 자극하기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "Alphabet(GOOGL)", "Broadcom(AVGO)"],
      "insight": "중국 AI 모델의 비용 덤핑 공포는 10% 차이에 불과한 해프닝이었습니다. SK하이닉스 본주의 갭 메우기 반등 랠리가 속도를 낼 것입니다.",
      "action_point": "ADR 프리미엄 축소 수혜를 입는 SK하이닉스 본주 및 AI 빅테크(구글, 알파벳)에 대한 매수 관점을 더욱 강화해야 합니다."
    }
  },
  "4Nv9WgJ5iwM": {
    "primary_topic": "tech",
    "secondary_topics": ["stock"],
    "tags": ["키미K32.8조파라미터", "MoE연산효율", "KVCache폭증", "eSSD수요급증", "GPUHBM필수"],
    "analysis": {
      "summary": "안될공학 분석은 중국 Kimi K3(2.8조 파라미터, 100만 토큰 컨텍스트, MoE 구조)가 GPU/HBM 수요를 줄이기는커녕 오히려 폭증시킨다는 기술적 진실을 입증했습니다. 토큰당 16개 전문가만 활성화해 추론 연산을 2.5배 효율화하더라도, 2.8조 개의 거대 파라미터를 HBM 메모리에 항상 상주시켜야 하므로 수십 대의 GPU와 HBM 탑재가 필수적입니다. 또한 100만 토큰 컨텍스트 처리 시 KV 캐시 용량이 폭증하여 외장 DDR5 및 eSSD 추가 구매가 선택이 아닌 필수가 됩니다.",
      "key_claims": [
        "Kimi K3의 MoE 구조는 토큰당 연산량을 줄여줄 뿐, 2.8조 개의 거대한 파라미터 자체를 HBM 메모리에 상주시존시켜야 하므로 GPU 및 HBM 수요 감소 우려는 기술적 무지에서 비롯된 착시이다.",
        "100만 토큰에 달하는 초장문 문맥을 처리할 때 발생하는 KV 캐시 메모리 폭증은 HBM만으로 감당할 수 없어 엔터프라이즈 SSD(eSSD)와 대용량 DDR5의 필연적 수요 폭발을 유발한다."
      ],
      "data_points": [
        "Kimi K3 스펙: 2.8조 파라미터, 100만 토큰 컨텍스트, 896개 전문가 중 16개 활성화",
        "효율화 지표: 동일 연산 대비 실질 효율 2.5배 증가"
      ],
      "signal": "positive",
      "signal_reason": "Kimi K3 MoE 기술이 GPU 및 HBM 탑재량 상주를 강제하고, 100만 토큰 KV 캐시용 eSSD/DDR5 폭발을 유발하여 반도체 초장기 호황을 보장하기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "NVIDIA(NVDA)"],
      "insight": "MoE 모델은 연산 횟수를 줄여줄 뿐 메모리 상주 용량을 줄이지 못합니다. 장문 컨텍스트(100만 토큰) 처리는 HBM과 eSSD를 동시에 집어삼키는 블랙홀입니다.",
      "action_point": "MoE AI 모델 확산의 최고 수혜 분야인 HBM3E/HBM4 공급사(SK하이닉스)와 eSSD/DDR5 제조업체(삼성전자) 비중을 굳건히 고수해야 합니다."
    }
  },
  "iDfsy3rjiP0": {
    "primary_topic": "etc",
    "secondary_topics": ["tech"],
    "tags": ["히트돔원리", "단열압축", "기상학과학", "폭염분석"],
    "analysis": {
      "summary": "안될과학 기상학 특강은 최근 글로벌 폭염을 유발하는 '히트돔(Heat Dome)' 현상의 핵심 원리가 마찰열이 아닌 공기 가라앉음에 따른 '단열 압축(Adiabatic Compression)'과 거대한 기압 뚜껑 효과임을 지형적 과학 원리로 해설한 교양 영상입니다.",
      "key_claims": [
        "히트돔 폭염은 공기가 상공에서 하강하며 눌려 기온이 치솟는 단열 압축 원리에 의해 형성된다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "기상학적 과학 교양 영상으로 증시 수급에 직접적 영향이 없기 때문입니다.",
      "key_companies": [],
      "insight": "단열 압축과 히트돔 현상은 기후 변화로 인한 전력 및 에어컨 인프라 과부하의 과학적 배경을 설명합니다.",
      "action_point": "여름철 기후 및 에너지 전력망 인프라 수요 지표의 기초 참고자료로 활용합니다."
    }
  },
  "gNbjV--PHcg": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["실적피크아웃의구심", "매출상회비율둔화", "내용연수연장착시", "금리달러압박", "엔비디아마이크론독점"],
    "analysis": {
      "summary": "한경 빈난새 특파원은 S&P 500기업들의 2분기 EPS 상회 비율(88%)과 서프라이즈 폭(5.2%)이 역대급임에도 주가 반응이 미적지근한 4가지 이유를 분석했습니다. 이익 성장의 37%를 엔비디아와 마이크론 단 2개사가 독식하는 극심한 편중, 매출 상회 비율 둔화(80%->76%)에 따른 '비용 절감형 이익 착시' 의구심, 메타 등 빅테크의 서버 감가상각 연수 연장(5년->5.5년)에 따른 장부상 착시, 그리고 미 10년물 국채 금리(4.6%)와 달러 강세 압력이 밸류에이션 상단을 제한하고 있습니다.",
      "key_claims": [
        "S&P 500 전체 이익 증가분의 37%를 엔비디아와 마이크론 단 2개 기업이 독점할 정도로 호실적 편중이 극심하다.",
        "매출 상회 비율이 76%로 낮아져 기업들이 허리띠를 졸라매어(비용 절감) 만든 이익이 아니냐는 질적 의구심과 감가상각 연장 착시 논란이 제기된다.",
        "미 10년물 국채 금리(4.6%)와 강달러 지속이 고평가 기술주들의 밸류에이션(PER)을 조이는 거시적 억제기로 작동 중이다."
      ],
      "data_points": [
        "S&P 500 2분기 실적 지표: EPS 상회 비율 88%, 이익 서프라이즈 폭 5.2%",
        "실적 편중: 엔비디아+마이크론 2개사가 전체 이익 증가분의 37% 차지",
        "매출 상회 비율: 1분기 80% -> 2분기 76%로 둔화",
        "금리: 미 10년물 국채 금리 4.6%선 상주"
      ],
      "signal": "neutral",
      "signal_reason": "역대급 실적 호조가 확인되었으나 이익의 질적 편중 및 금리·달러 고공행진이 당분간 주가의 상단을 제약하는 박스권 국면을 형성하기 때문입니다.",
      "key_companies": ["NVIDIA(NVDA)", "Micron(MU)", "Meta(META)"],
      "insight": "이익 증가분의 37%를 쥔 엔비디아와 마이크론 등 실증 주도주로만 자금이 집중되는 '양극화 장세'입니다. 소수 주도주 외의 어설픈 잡주는 주가 반등이 더딥니다.",
      "action_point": "이익을 실제로 쥐고 있는 독점 주도주(엔비디아, 마이크론, SK하이닉스)로 포트폴리오 쏠림을 더욱 강화하고 비주도주는 과감히 교체해야 합니다."
    }
  }
}

for vid, data in batch_8.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 8 completed!")
