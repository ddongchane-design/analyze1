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
        print(f"Invalidated cache: {synthesis_cache}")

# Batch 6 analyses
batch_6 = {
  "XKAhMLlV00U": {
    "primary_topic": "robot",
    "secondary_topics": ["tech", "stock"],
    "tags": ["디백스", "김녹원", "NPU", "피지컬AI", "애플엔지니어", "초저전력반도체"],
    "analysis": {
      "summary": "피지컬 AI와 디바이스용 AI(온디바이스 AI)의 핵심은 통신 두뇌가 아닌 로봇/디바이스 내부에 직접 탑재되는 초저전력 반도체(NPU)입니다. 엔비디아의 임베디드 칩(젯슨 등)은 140W의 높은 전력을 소비해 모바일/로봇 구동에 한계가 있는 반면, 디백스의 NPU는 <span class=\"text-cyan-300 font-semibold\">5W 수준의 초저전력</span>으로 20배 높은 전성비를 제공합니다. 김녹원 대표는 애플의 극한의 최적화 설계 철학(OS와 하드웨어 사용 패턴 매칭)을 바탕으로 버터가 녹지 않을 정도의 초저발열 반도체 양산에 성공했습니다.",
      "key_claims": [
        "피지컬 AI와 디바이스용 AI(온디바이스 AI)의 핵심은 통신 두뇌가 아닌 로봇/디바이스 내부에 직접 탑재되는 초저전력 반도체(NPU)이다.",
        "엔비디아의 임베디드 칩(젯슨 등)은 140W의 높은 전력을 소비해 모바일/로봇 구동에 한계가 있는 반면, 디백스의 MPU는 5W 수준의 초저전력으로 20배 높은 전성비를 제공한다.",
        "애플 출신 엔지니어로서 애플의 극한의 최적화 설계 철학(OS와 하드웨어 사용 패턴 매칭)을 활용하여 버터가 녹지 않을 정도의 초저발열 반도체 양산에 성공했다."
      ],
      "data_points": [
        "엔비디아 젯슨 소비 전력: 약 140W",
        "디백스 NPU 소비 전력: 약 5W",
        "디백스 NPU 전성비: 동일 전력 기준 GPU 대비 20배 연산 성능"
      ],
      "signal": "bullish",
      "signal_confidence": "high",
      "signal_reason": "전력 제약이 심각한 엣지 디바이스 및 피지컬 AI 로봇 시장에서 독보적인 전성비를 제공하는 로컬 NPU 칩의 상업적 양산 성공이 확인되었기 때문입니다.",
      "key_companies": ["디백스(DeepX)", "애플", "엔비디아", "시스코"],
      "insight": "피지컬 AI의 대중화를 위해서는 가볍고 전력을 덜 먹으면서 고성능을 내는 엣지 NPU가 필수적입니다. 디백스(DeepX)는 전성비(단위 전력당 연산 성능)에서 엔비디아의 기존 GPU 기반 임베디드 라인업(Jetson) 및 여타 MPU 경쟁사 대비 압도적인 저발열 및 초저전력 설계 장벽을 구축하며 모바일, 로봇, 공장 자동화 시장의 표준 칩 자리를 선점하려 하고 있습니다.",
      "action_point": "피지컬 AI 로봇 및 자율주행 디바이스의 본격 양산 시대를 앞두고, 전력 제약 문제를 완벽하게 해결하는 <span class=\"text-cyan-300 font-semibold\">온디바이스 NPU 기업(디백스 등)</span>의 칩 채택 현황을 주시하고, 관련 모터/감속기 등 로봇 부품 생태계로 투자를 넓혀야 합니다."
    }
  },
  "Yr1mtuxN_ww": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["반도체급락", "버블붕괴비판", "토큰가격하락", "케펙스유지", "수급쏠림"],
    "analysis": {
      "summary": "최근 반도체 주가의 급락은 AI 사이클의 정점이나 <span class=\"text-rose-400 font-medium\">버블 붕괴</span>가 아니라, 그동안 누적된 수급 쏠림 현상과 마이크론 실적 경계감이 트리거가 된 건강한 조정입니다. 중국산 오픈 웨이트 모델의 약진으로 인해 AI 토큰 단가가 급락하며 빅테크의 수익성에 의문이 제기되었으나, 하이퍼스케일러들의 <span class=\"text-cyan-300 font-semibold\">설비투자(CapEx) 계획</span>은 여전히 꺾이지 않고 탄탄하게 유지되고 있습니다. S&P 500 신고가 경신에도 이익 전망이 빠르게 상향되며 주가수익비율(PER)은 오히려 1월보다 낮아졌습니다.",
      "key_claims": [
        "최근 반도체 주가의 급락은 AI 사이클의 정점이나 버블 붕괴가 아니라, 그동안 누적된 수급 쏠림 현상과 마이크론 실적 경계감이 트리거가 된 건강한 조정이다.",
        "중국산 오픈 웨이트 모델의 유입 등으로 인해 AI 토큰 단가가 하락하며 빅테크의 수익성에 의문이 제기되었으나, 하이퍼스케일러들의 설비투자(CapEx) 계획은 전혀 꺾이지 않았다.",
        "S&P 500이 신고가를 경신했음에도 불구하고 기업들의 이익 전망이 동반 상향되면서 주가수익비율(PER)은 오히려 1월보다 낮아진 상태로 버블과 거리가 멀다."
      ],
      "data_points": [
        "S&P 500 밸류에이션: 주가 최고치 도달에도 불구, 이익 전망치 상향으로 인해 12개월 선행 PER은 지난 1월 대비 하락"
      ],
      "signal": "bullish",
      "signal_confidence": "high",
      "signal_reason": "AI 서비스 단가 인하 압력에도 하이퍼스케일러들의 인프라 구매(CapEx) 의향은 지속적으로 증가하고 있으며, 실적 대비 밸류에이션이 오히려 합리적 수준으로 복귀했기 때문입니다.",
      "key_companies": ["SK하이닉스", "마이크론"],
      "insight": "AI 토큰 단가 하락과 수익성 회의론(딥시크 모먼트 등)이 단기적인 주가 하락의 핑계가 되었으나, 실제 빅테크들의 인프라 지출(CapEx) 의지는 강력하게 유지되고 있습니다. 기업 이익이 주가보다 빠르게 올라와 밸류에이션 부담이 오히려 낮아졌으므로, 단기 변동성은 거품 붕괴의 전조가 아닌 쏠림 매물의 해소 과정으로 이해해야 합니다.",
      "action_point": "버블 붕괴 공포에 휩쓸려 반도체 주식을 투매하기보다는, <span class=\"text-cyan-300 font-semibold\">실질 자본 지출(CapEx)의 강세</span>와 낮아진 <span class=\"text-amber-300 font-bold\">선행 PER 밸류에이션</span>을 기회로 삼아 주도주를 분할 매수하는 관점이 타당합니다."
    }
  },
  "ZqqgffrAZuE": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["소부장", "반도체장비", "마이크론가이드", "변동성관리", "실적차별화"],
    "analysis": {
      "summary": "마이크론이 시장 예상을 뛰어넘는 호실적과 향후 가이드를 제시함에 따라, 세온(Sell on) 우려를 불식시키고 반도체 업계 전반에 대형 호재를 확인시켰습니다. 삼성전자와 SK하이닉스 투톱이 실적을 굳힌 후, 턴어라운드의 온기가 중소형 반도체 소부장(소재/부품/장비) 기업들로 본격 확산되는 단계에 접어들었습니다. 다만 소부장 섹터는 본질적으로 <span class=\"text-rose-400 font-medium\">변동성 리스크가 크고</span> 기업별 실적 차별화가 심할 것입니다.",
      "key_claims": [
        "마이크론이 시장 예상을 뛰어넘는 호실적과 향후 가이드를 제시함에 따라, 세온(Sell on) 우려를 불식시키고 반도체 업계 전반에 대형 호재를 확인시켰다.",
        "삼성전자와 SK하이닉스 투톱이 자리를 잡은 이후, 실적 턴어라운드의 온기가 중소형 반도체 소부장(소재/부품/장비) 기업들로 본격 확산되는 단계에 접어들었다.",
        "소부장 섹터는 본질적으로 변동성이 크고 기업별 실적 회복 속도가 크게 차별화되므로, 일괄적인 테마성 매수보다 실질적 매출 성장을 내는 기업 선별이 중요하다."
      ],
      "data_points": [
        "코스피/코스닥 소부장 기업 실적: 마이크론 실적 가이드 공개 후 소부장 장비주 중심으로 3~10%대 상승세 관찰"
      ],
      "signal": "bullish",
      "signal_confidence": "medium",
      "signal_reason": "대장주의 강력한 실적 확인 이후 장비 및 부품 투자 낙수 효과가 관련 밸류체인(소부장)으로 확산되면서, 개별 장비사들의 수주 모멘텀이 본격 가동되기 때문입니다.",
      "key_companies": ["마이크론", "삼성전자", "SK하이닉스"],
      "insight": "대장주의 랠리 이후 소부장으로 낙수 효과가 번지는 것은 메모리 반도체 업황 개선 주기마다 반복되는 전형적인 흐름입니다. 다만 소부장 업체들의 주가는 철저히 개별 실적 회복의 강도에 따라 양극화될 것이므로, 막연한 업황 턴어라운드 기대보다는 수혜가 확실한 공정 소재 및 HBM 관련 전공정/후공정 핵심 장비사로 타겟을 좁혀야 합니다.",
      "action_point": "반도체 랠리의 확산 국면에서 실질 실적 개선세가 뚜렷한 <span class=\"text-cyan-300 font-semibold\">HBM 관련 핵심 소부장 기업</span>을 선별하고, 높은 <span class=\"text-rose-400 font-medium\">소부장 변동성 리스크</span>를 고려해 포트폴리오를 분산 구성해야 합니다."
    }
  }
}

for vid, data in batch_6.items():
    save_and_delete(
        video_id=vid,
        primary_topic=data["primary_topic"],
        secondary_topics=data["secondary_topics"],
        tags=data["tags"],
        analysis_data=data["analysis"]
    )
print("Batch 6 completed!")
