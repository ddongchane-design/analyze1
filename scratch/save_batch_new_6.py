import json
from pathlib import Path

def save_analysis(video_id, primary_topic, analysis_data, classification_data):
    pending_file = Path(f"data/pending/{video_id}.json")
    if not pending_file.exists():
        print(f"Pending file not found: {video_id}")
        return
    
    try:
        pending_data = json.loads(pending_file.read_text(encoding="utf-8"))
        video_data = pending_data.get("video", {})
    except Exception as e:
        print(f"Error reading pending {video_id}: {e}")
        return
    
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
    
    try:
        pending_file.unlink()
        print(f"Removed pending: {pending_file}")
    except Exception as e:
        print(f"Error removing pending {video_id}: {e}")
        
    synthesis_cache = Path(f"data/synthesis/{primary_topic}.json")
    # economy.json 캐시는 사용자 수동 수정본이 있으므로 절대 삭제하지 않음
    if primary_topic != "economy" and synthesis_cache.exists():
        try:
            synthesis_cache.unlink()
            print(f"Invalidated cache: {synthesis_cache}")
        except Exception as e:
            print(f"Error invalidating cache: {e}")

analyses = {
  "yxUqIdN8m2k": {
    "primary": "stock",
    "analysis": {
      "summary": "뉴욕 증시가 단기 급등에 따른 차익 실현 압력과 대규모 자금 쏠림 현상으로 인해 <span class=\"text-rose-400 font-medium\">기간 조정 국면</span>에 진입했으며, 지표상의 뚜렷한 악재가 없음에도 변동성이 심화되고 있습니다.",
      "key_claims": [
        "골드만삭스와 바클레이즈 트레이더들은 금요일의 급락이 일시적 현상이 아니며, <span class=\"text-rose-400 font-medium\">극단적인 기술주 포지션 과밀</span>에 따른 심각한 지수 변동성 증폭 위험을 경고했다.",
        "시티그룹은 한국 증시의 AI 및 기술 대형주 쏠림 변동성을 우려했으며, 매수 심리가 너무 과열되어 기대치가 충족되지 않을 시 <span class=\"text-rose-400 font-medium\">추가 하락 가능성</span>이 높다고 지적했다.",
        "트럼프의 중재로 이란-이스라엘 갈등이 일시 완화되어 유가가 80달러 중반대로 진정되는 흐름이나, 오만해 미 헬기 추락 등 국지적 노이즈가 완충력을 저해하고 있다."
      ],
      "data_points": [
        "마이크론 프리마켓 상승분을 모두 반납하고 장중 하락 후 막판 반등하는 롤러코스터 분봉 흐름 연출",
        "스페이스X 상장 청약에 약 2,500억 달러 이상의 막대한 유동성이 묶여 있어 기술주 저가 매수세 차단"
      ],
      "signal": "bearish",
      "signal_reason": "기술주 및 반도체 섹터의 지배적인 매수 심리 이면에 포지션 과밀화 리스크가 도사리고 있으며, 스페이스X IPO에 따른 대형 수급 교란이 단기 반등세를 지속 억누르고 있습니다.",
      "key_companies": ["NVIDIA", "Micron", "Intel", "SpaceX"],
      "insight": "지수 자체의 하락폭보다 개별 주식 안에서의 극심한 편차가 발생하는 K자형 장세이며, 이는 <span class=\"text-rose-400 font-medium\">다컴 버블 직전의 쏠림 현상</span>과 유사한 기술주 내부의 밸류에이션 양극화를 반영합니다.",
      "action_point": "단기 반등(데드캣 바운스)을 신규 매수 기회로 착각하기 쉬운 구간이므로, 현금 비중을 유지하며 다가오는 미국 CPI 물가 지표 발표와 수급 진정을 확인한 뒤 대응하는 것이 안전합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["뉴욕증시", "기간조정", "기술주쏠림", "스페이스X청약", "변동성경고", "삼프로TV"]
    }
  },
  "zoOgEj5vIik": {
    "primary": "stock",
    "analysis": {
      "summary": "블랙 먼데이의 급락 충격을 딛고 코스피 8%대, 코스닥 6%대 폭등하며 <span class=\"text-amber-300 font-bold\">8천피 선을 조기 탈환</span>했으나, 단기 급등 피로감과 곧 발표될 미국 CPI 물가 지표에 대한 경계 심리가 동시에 작용하고 있습니다.",
      "key_claims": [
        "중동 지정학적 위기 완화 및 트럼프의 종전 압박 발언이 전날의 과도한 공포성 하락을 상쇄시키는 강력한 되돌림 랠리를 견인했다.",
        "반도체 공급망의 펀더멘탈 성장 전망은 유효하며, 글로벌 목표주가 상향 릴레이 속에 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>가 15.9% 폭등하는 등 반도체 투톱이 시장 반등의 기둥 역할을 했다.",
        "반면 젠슨 황의 출국 이후 단기 재료 소멸과 피지컬 AI 상용화 지연 우려가 겹치며 <span class=\"text-cyan-300 font-semibold\">LG전자</span>와 <span class=\"text-cyan-300 font-semibold\">네이버</span> 등 일부 파트너사 주가는 큰 폭의 조정을 겪었다."
      ],
      "data_points": [
        "코스피 지수 8.18% 폭등하여 8,096선 마감, 코스닥 지수 6.19% 급등하여 967선 마감",
        "SK하이닉스 15.9% 폭등한 220만 원대 회복, 삼성전자 8.97% 폭등한 32만 원대 도달"
      ],
      "signal": "neutral",
      "signal_reason": "전일 하락폭을 상당 부분 만회하며 제자리를 찾았으나, 장 후반 외국인의 하방 베팅 전환과 미국 CPI 경계감으로 인해 추가 급등 동력은 제한적인 숨 고르기 장세입니다.",
      "key_companies": ["SK하이닉스", "삼성전자", "LG전자", "네이버", "삼성전기"],
      "insight": "폭락 후 폭등하는 과도한 하루살이 변동성은 한국 증시의 <span class=\"text-rose-400 font-medium\">단기 수급 및 레버리지 노출도</span>가 비정상적으로 높다는 방증이며, 지수가 안정 국면에 들어서야 비로소 중소형 개별 섹터의 액티브 랠리가 나타날 것입니다.",
      "action_point": "변동성 상단에서 무리하게 추격 매수하기보다, 조정 시마다 비축해 둔 현금을 분할 투입하고 고금리 장기화 우려에 훼손되지 않는 반도체 주도 소부장에 집중하는 자세가 유효합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["코스피8천선", "폭락후급등", "외국인매도전환", "반도체주도", "피지컬AI조정", "삼프로TV"]
    }
  },
  "ZxCsi4rBTQY": {
    "primary": "stock",
    "analysis": {
      "summary": "개인과 외국인의 동반 매도세 속에서 오랜만에 기관(투신, 연기금)이 1조 원 대규모 순매수로 유입되며 <span class=\"text-amber-300 font-bold\">하반기 증시 수급의 결정적 변화</span>를 예고하고 있으며, 지수 정체기 이후 펼쳐질 액티브 순환매 장세를 준비해야 합니다.",
      "key_claims": [
        "그간 외국인 독주와 개인 수급에 밀렸던 국내 기관 투자자들이 대거 유입되면서 반도체 일변도에서 바이오 등 코스닥 전반으로 매수 온기가 확산되었다.",
        "미 증시의 마이크론 등 반도체 15%대 널뛰기는 스페이스X 상장 청약에 <span class=\"text-cyan-300 font-semibold\">3,000억 달러 규모의 수급 진공</span>이 발생했기 때문이며, 경제 지표 훼손에 의한 것이 아니다.",
        "하반기 증시는 코스피 200 등 주요 지수 리밸런싱과 액티브 ETF 설정액 증가로 인해 기관 중심의 차별화된 종목 순환 장세가 강화될 것이다."
      ],
      "data_points": [
        "기관이 코스피 반등 당일 대규모 매수를 기록하며 지수 하방을 강력 방어",
        "미국 스페이스X 청약 증거금이 최대 2,500억~3,000억 달러로 폭증해 단기 펀드 유동성 흡수"
      ],
      "signal": "bullish",
      "signal_reason": "스페이스X 청약 종료 후 막대한 환불금이 다시 시장으로 환류되고, 국내 기관들이 실적 리밸런싱 종목 사냥에 적극 나서면서 증시 전반의 수급 다변화와 복원력이 개선되고 있습니다.",
      "key_companies": ["삼성전자", "SK하이닉스", "SpaceX", "Oracle"],
      "insight": "지수가 고점을 경신하며 질주하기보다는 일정한 밴드에 가치는 횡보 국면이 올 가능성이 크며, 이 경우 <span class=\"text-amber-300 font-bold\">지수 구성 종목 리밸런싱 수혜주</span>들과 실적 기반 개별 강소주들이 대형주 대비 초과 수익을 달성하는 장세가 펼쳐집니다.",
      "action_point": "대형주 올인이 아닌, 6월 말 코스피200 및 코스닥150 지수 편입 예상 후보 종목과 하반기 기관 순매수 유입이 두드러지는 바이오·소부장 우량주로의 포트폴리오 다각화가 적기입니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "tech"],
      "tags": ["기관순매수", "수급변화", "스페이스X환불금", "지수리밸런싱", "순환매장세", "삼프로TV"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["analysis"], info["classification"])
