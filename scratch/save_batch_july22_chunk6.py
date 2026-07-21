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

batch_6 = {
  "PC2ATdiqTaI": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["5000조투자청구서", "무역수지적자위험", "GDP대비투자", "주주환원차질", "정책금융부채"],
    "analysis": {
      "summary": "한국의 장기 반도체 인프라 투자 계획(5,000조 원 상당)은 국가 GDP(약 2,300조 원)의 2배를 상회하여, 삼성전자와 SK하이닉스의 연간 400조 원대 영업이익을 10년 이상 전액 쏟아부어도 모자란 극단적 부채 의존도를 유발하고 있습니다. 이 이익은 장부상 이익일 뿐 매출채권 및 주주환원(배당·자사주)으로 분산되므로, 국책 대출과 정책 금융에 의존한 무리한 인프라 집행이 무역 수지 적자 반전 및 국가 신용 리스크 청구서로 돌아올 수 있습니다.",
      "key_claims": [
        "한국의 5,000조 원대 반도체 인프라 프로젝트는 국가 GDP의 2배 수준으로, 삼전·하이닉스 합산 영업이익 400조 원을 10년 넘게 전액 투입해야 하는 과밀 베팅이다.",
        "영업이익 중 상당수는 장부상 이익이며 주주환원 및 주주 배당에 사용되므로, 인프라 비용의 대부분은 국책 대출과 시중 부채로 충당되어 매크로 신용 리스크를 키운다."
      ],
      "data_points": [
        "한국 총 인프라 투자 계획: 5,000조 원 (한국 GDP 2,300조 원의 2배 초과)",
        "삼성전자+SK하이닉스 피크 영업이익 합산: 약 400조 원 추정"
      ],
      "signal": "negative",
      "signal_reason": "GDP의 2배에 달하는 부채 기반 인프라 과밀 투자가 무역수지 적자 반전과 기업의 주주환원 재원 고갈을 유발하는 중장기 매크로 리스크이기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "반도체 호황에 착시되어 국가 GDP 2배의 부채 인프라를 지으면 수급 둔화 시 감당 불가능한 이자 청구서로 돌아옵니다. 자본 효율성 점검이 필요합니다.",
      "action_point": "과도한 CAPEX 집행으로 재무 비효율이 우려되는 하드웨어 전용 밸류체인보다 현금 유동성이 우수한 종목으로 포트폴리오를 안분해야 합니다."
    }
  },
  "Dpb3r3wbjic": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["미국ETF정립식", "환율매수타이밍", "나스닥100수익률", "환노출vs환헤지", "환율패턴분석"],
    "analysis": {
      "summary": "수페TV는 238주(4.5년) 동안 미국 지수 ETF를 매주 적립식 매수한 실제 결과를 공개했습니다. 나스닥 100이 +72.1%(연 20% 이상), S&P 500이 +57.3%의 높은 성과를 거두었습니다. 최근 환율이 1,470원대로 하락했으나, 역사적 통계상 한 달간 환율이 3% 이상 하락한 뒤 다음 달 반등할 확률은 76.5%에 달하므로 현재 시점에서는 환노출 상품(지수 ETF) 비중을 높여 환차익과 주가 상승을 동시에 노리는 전략이 유리합니다.",
      "key_claims": [
        "238주간 매주 정립식 매수한 나스닥 100 수익률은 +72.1%, S&P 500은 +57.3%로 꾸준함이 시장 예측을 압도했다.",
        "1981년 이후 원달러 환율 데이터 분석 결과, 한 달간 3% 이상 환율이 하락한 직후 다음 달 환율이 반등할 확률은 76.5%이다.",
        "환율 1,470원대 이탈 국면에서는 환헤지보다 환노출 ETF 비중을 늘려 장기 우상향 환차익 및 지수 상승을 동시에 취해야 한다."
      ],
      "data_points": [
        "238주 정립식 수익률: 나스닥 100 +72.1% (연 20%+), S&P 500 +57.3% (연 20%+)",
        "환율 하락 후 반등 확률: 1개월간 3% 이상 하락 시 다음 달 상승 확률 76.5%"
      ],
      "signal": "positive",
      "signal_reason": "미국 지수 ETF의 매주 정립식 매수 성과의 우수성이 입증되었고, 1,470원대 환율 구간이 환노출 매수의 높은 통계적 승률을 보이기 때문입니다.",
      "key_companies": ["Kodex 미국나스닥100(TR)", "Kodex 미국S&P500TR"],
      "insight": "환율 1,470원 하락 국면은 공포가 아닌 환노출 ETF 저가 매수의 최적 기회입니다. 정립식 매수는 고점 저점 예측 없이도 연 20% 수익을 안겨줍니다.",
      "action_point": "원달러 환율 1,470원대에서 Kodex 미국나스닥100 및 S&P500 환노출 ETF를 매주 정립식으로 꾸준히 모아가는 전략을 추천합니다."
    }
  },
  "HQkjs71O_6k": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["여의도인사이트", "20주선이탈", "10일선저항선", "이중바닥확인", "기관수급핵심"],
    "analysis": {
      "summary": "박병창 MP파트너스 대표는 코스피 지수가 7월 14일 저점에서 이중 바닥을 다지고 반등했으나, 1년 동안 깨지지 않던 20주 이동평균선(7,070pt)을 이탈했음을 지적했습니다. 단기적으로 10일 이동평균선 및 7,070선 위로 조속히 복귀해야 심리적 안정선이 형성되며, 개인 투매를 받아내는 기관 및 외국인 수급의 추세적 합류가 8월 랠리의 필수 조건입니다.",
      "key_claims": [
        "코스피 지수가 7월 14일 전저점에서 이중 바닥을 다지며 반등했으나, 20주 이동평균선(7,070pt) 하향 이탈로 저항선 테스트가 남아있다.",
        "개인만의 매수로는 장기 랠리가 불가능하며, 기관과 외국인의 대형주 동반 순매수 합류가 확인되어야 8,000pt 탈환이 가능하다."
      ],
      "data_points": [
        "코스피 기술적 저항선: 10일 이동평균선 및 20주선 (7,070pt 복귀 여부가 관건)"
      ],
      "signal": "neutral",
      "signal_reason": "전저점 이중 바닥 형성으로 공포는 진정되었으나 7,070pt 이동평균선 지지 여부를 수급상 확인해야 하는 변곡점이기 때문입니다.",
      "key_companies": [],
      "insight": "기술적으로 7,070pt 위로 지수가 복귀하는 것을 확인하는 것이 중요합니다. 외국인과 기관의 바스켓 매수 전환이 진짜 랠리의 신호탄입니다.",
      "action_point": "7,070pt 저항선 돌파 여부를 모니터링하면서, 수급이 유입되는 대형 반도체 및 방산주 위주로 이중 바닥 지지점 매수를 유효하게 가져갑니다."
    }
  },
  "tfy0Qi7L7Bc": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["실적과주가이격", "실적추종믿음", "분할매수전략", "심리적공포극복"],
    "analysis": {
      "summary": "빈센트 전문가는 주가와 실적 간의 이격(괴리)이 극도로 벌어져 불거진 시장 공포는 심리적 착시에 불과하다고 진단했습니다. 반도체 및 대형주 실적 성장은 확고하므로 주가는 반드시 실적을 추종하여 폭등할 것이라는 분석 아래, 공포를 딛고 1년 분할 매수로 포트폴리오를 채워 넣을 것을 강하게 권고합니다.",
      "key_claims": [
        "현재의 코스피 하락은 기업 실적 펀더멘탈과 주가 간의 이격도가 극대로 벌어진 심리적 왜곡 현상이다.",
        "주가는 결국 기업 실적의 궤적을 따라 수렴하므로 공포에 털리지 말고 안분 분할 매수로 우량주를 모아가야 한다."
      ],
      "data_points": [],
      "signal": "positive",
      "signal_reason": "주가와 펀더멘탈 실적 간의 극단적 이격이 조만간 주가의 실적 수렴 랠리로 해소될 것으로 확신하기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "실적은 치솟는데 주가만 떨어진 자리는 역사적으로 최적의 분할 매수 기회였습니다. 공포감 수급 불안은 이격 해소 랠리로 수렴합니다.",
      "action_point": "실적 대비 과조정된 반도체 대형주를 중심으로 분할 매수를 꾸준히 집행해야 합니다."
    }
  },
  "JSaUwNYAvdg": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["상상속고통", "하이닉스언더슈팅", "ROE90%밸류", "실적숫자확인", "스테이전략"],
    "analysis": {
      "summary": "이효석 대표는 세네카의 명언('우리는 현실보다 상상 속에서 더 자주 고통받는다')을 인용해, 딥시크이나 터보퀀트, Kimi K3 등 실체 없는 상상 속의 공포로 주가가 과도하게 빠졌다고 지적했습니다. 현실의 반도체 수출 데이터와 실적 숫자는 여전히 압도적이며, ROE 90%를 상회하는 SK하이닉스의 주당 가치는 90만 원 이상이 확정적이므로 현재의 18만~20만 원선 주가는 극단적 '언더슈팅'입니다. 무서워도 던지지 말고 버티는 '스테이(Stay)' 전략이 정답입니다.",
      "key_claims": [
        "주가 폭락은 실체 없는 상상 속의 공포(메모리 피크아웃 우려 등)가 만든 환영이며, 실제 반도체 수출 데이터 및 영업이익 숫자는 최고조를 기록 중이다.",
        "SK하이닉스는 ROE가 90%를 상회하므로 PBR 2배만 주어도 90만 원 이상의 가치가 정당화되며, 현재의 18만~20만 원 주가는 명백한 언더슈팅이다.",
        "시장의 소음과 상상 속 공포에 쫄지 말고, 숫자가 돌아올 때까지 우량 반도체 주식을 고수하는 '스테이(Stay)' 전략을 취해야 한다."
      ],
      "data_points": [
        "SK하이닉스 적정 가치 및 ROE: ROE 90% 상회, 주당 90만 원 가치 정당화 (현 주가 18만~20만 원선은 과조정)"
      ],
      "signal": "positive",
      "signal_reason": "실제 수출 데이터와 ROE 90% 숫자가 하이닉스의 90만 원 적정 가치를 정당화하며, 현재 주가의 언더슈팅이 강력한 반등을 예약하고 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "현실의 실적 데이터는 완벽한데 상상 속 공포(노이즈)로 주가가 언더슈팅할 때가 진짜 거장의 매수 타임입니다. 스테이(Stay)하십시오.",
      "action_point": "SK하이닉스 18만~20만 원선의 언더슈팅 구간에서 절대 매도하지 말고, 강력히 보유(Stay) 및 저점 추매를 단행해야 합니다."
    }
  }
}

for vid, data in batch_6.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 6 completed!")
