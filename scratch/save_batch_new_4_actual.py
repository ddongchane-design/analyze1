import json
from pathlib import Path

def save_and_delete(video_id, primary_topic, secondary_topics, tags, analysis_data):
    pending_path = Path(f"data/pending/{video_id}.json")
    if not pending_path.exists():
        print(f"Warning: {pending_path} does not exist.")
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
    if primary_topic != "economy" and synthesis_cache.exists():
        synthesis_cache.unlink()
        print(f"Invalidated cache: {synthesis_cache}")

batch_data = {
  "NDiyXbv_CZM": {
    "primary_topic": "etc",
    "secondary_topics": [],
    "tags": ["열사병", "습구온도", "기후변화", "체온조절", "건강관리"],
    "analysis": {
      "summary": "폭염 상황에서 인간의 생명을 위협하는 결정적 요인은 단순 최고 기온이 아닌 높은 습도(습구 온도)입니다. 대기 중 습도가 꽉 차면 땀 증발을 통한 체온 조절 능력이 상실되어 중심 체온이 계속 상승하고, <span class=\"text-rose-400 font-medium\">열사병</span>으로 이어집니다. 최근 연구들은 건강한 성인이라도 기존 예측치보다 훨씬 낮은 습구 온도에서도 심각한 생명 위협을 받을 수 있다고 경고합니다.",
      "key_claims": [
        "습도가 높으면 체내의 땀이 증발하지 않아 체온 발산이 차단되고 중심 체온이 비정상적으로 급등합니다.",
        "습구 온도가 35도 미만인 28도 부근이더라도 노약자나 만성 질환자에게는 치명적인 폭염 피해(사망 위험 등)를 유발할 수 있습니다."
      ],
      "data_points": [
        "이론적 생존 상한선 습구 온도 기준: 35도 수준 (그늘에서 가만히 물을 마셔도 생물학적 한계)",
        "2003년 유럽 대규모 폭염 사망자 당시 습구 온도: 약 28도 수준 (이보다 낮은 습도 조건에서도 치명적 영향 입증)"
      ],
      "signal": "na",
      "signal_reason": "여름철 기후 변화와 인체 열사병 발병 메커니즘을 규명하는 대중 과학 콘텐츠로, 주식 시장에 대응하는 투자 정보가 아닙니다.",
      "key_companies": [],
      "insight": "기후 온난화에 따른 습도 상승은 노동 생산성을 급감시키는 물리적 요인입니다. 단순 에어컨 수요 확대를 넘어 산업 전반의 야외 근로 안전 지침 개정과 보건 인프라 확충에 중대한 함의를 제공합니다.",
      "action_point": "해당 영상은 투자 판단 대상이 아니므로, 기후 관련 시사 교양 정보로만 활용하고 자산 배분 전략에서는 배제합니다."
    }
  },
  "NfCq0lC5n5Q": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["수급교란", "레버리지ETF", "평가손실", "DRAM수출", "저가매수"],
    "analysis": {
      "summary": "최근 국내 반도체주의 급락세는 펀더멘털의 변동이 아닌 외국인의 파생 상품 장난과 개인의 레버리지 쏠림이 낳은 <span class=\"text-rose-400 font-medium\">수급 붕괴 현상</span>입니다. 외국인들은 현물을 매도하고 선물을 하락시켜 레버리지 ETF의 기계적 리밸런싱 투매를 유도하고 있습니다. 이로 인해 삼성전자와 SK하이닉스의 가치 대비 주가수익비율(PER)은 내년 이익 기준 4.x배 수준까지 낮아지며 비이성적 영역에 진입했습니다.",
      "key_claims": [
        "기업 가치(삼성전자, SK하이닉스 호실적)는 변한 것이 없으나 단일 종목 레버리지 ETF와 결합된 수급 쏠림이 외국인의 타겟이 되어 하방 변동성이 커졌습니다.",
        "개인 투자자들이 하락장에서 물타기를 위해 SK하이닉스 2배 레버리지 등을 매수할수록, LP(유동성공급자)들의 기계적 청산이 더 많은 본주 투매를 유발하는 역설이 지속됩니다.",
        "주요 반도체 품목별 수출 데이터를 보면 낸드와 DRAM 모듈 가격은 일부 조정을 겪었으나 범용 D램 및 HBM의 수출 총액 성장 추세는 여전히 견고합니다."
      ],
      "data_points": [
        "급락으로 환산된 삼성전자 내년 예상 실적 기준 PER: 약 4배 중반 수준 (역사적 하단 영역)",
        "외국인 선물 매도 물량 숏커버링 전환 규모: 장중 1.4조 원 순매도 -> 장막판 5,000억 원대로 대량 걷어 올림"
      ],
      "signal": "neutral",
      "signal_reason": "외국인의 파생 시장 가격 왜곡(장난)과 레버리지 매물 소화 과정이 진행 중이어서 추가 하락을 단정하긴 어려우나 수급 회복에 다소 시간이 필요하기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "주가가 쌀 때 사고 비쌀 때 파는 것이 정석이지만, 레버리지 쏠림 장세에서는 공포심에 휩싸여 최저점에서 손절하고 최고점에서 추격 매수하는 우를 범하기 쉽습니다. 펀더멘털(이익)이 굳건한데 주가만 빠진 상태이므로 현재 시점에서의 매도는 실익이 없습니다.",
      "action_point": "미수나 신용 레버리지는 절대 사용하지 말고, 이미 보유한 우량 반도체 지분은 섣부른 손절보다는 실적 시즌의 피크아웃 오해 해소 시까지 관망하는 것이 현명합니다."
    }
  },
  "OP6FjNHfxl4": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["호르무즈통행세", "유가폭등", "SK하이닉스ADR", "애플신고가", "긴축공포"],
    "analysis": {
      "summary": "한국 반도체주의 폭락 충격에 이어 도널드 트럼프 전 대통령의 '호르무즈 해협 20% 통행료 부과' 선언이 덮치며 국제 유가(WTI)가 9.4% 폭등했습니다. 이에 뉴욕 증시도 반도체주 위주로 동반 급락했으나, 애플은 아이폰 18과 폴더블폰에 대한 하반기 기대감(목표가 365달러 상향)으로 <span class=\"text-cyan-300 font-semibold\">사상 최고가</span>를 새로 썼습니다. 유가 급등과 월러 연준 이사의 매파 발언으로 10년물 국채 금리가 4.6%를 돌파하여 시장 전반의 긴축 공포가 강화되었습니다.",
      "key_claims": [
        "트럼프 전 대통령이 호르무즈 해협을 지나는 모든 화물의 20%를 미국이 안전 보장 대가(통행료)로 징수하겠다고 주장하며 유가 폭등을 자극했습니다.",
        "SK하이닉스 ADR은 본주 하락폭(-15%)을 반영해 9% 이상 급락한 152.35달러로 내려앉으며 상장 첫날 상승폭을 대부분 반납했습니다.",
        "시티그룹이 가을 폴더블폰 흥행을 이유로 애플의 목표가를 365달러로 대폭 올리면서, 기술주 하락 장세 속에서 애플 홀로 사상 최고치를 경신했습니다."
      ],
      "data_points": [
        "WTI 유가 상승률: 9.4% 폭등 (배럴당 78.11달러), 브렌트유 80달러선 상회 (83달러 기록)",
        "트럼프 20% 통행료 기반 VLCC(초대형유조선) 1척당 징수액 계산: 약 3,000만 달러 (이란 요구액 200만 달러의 15배 수준)",
        "SK하이닉스 ADR 거래량: 약 5,000만 주 이상 거래 (미국 마이크론 거래량 3,400만 주를 대폭 추월)"
      ],
      "signal": "bearish",
      "signal_reason": "유가 폭등이 물가 상승을 유발하여 연준의 금리 인하 기대감을 지연시키고, 반도체 공급망에 대한 비용 부담을 한층 높이고 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "애플(AAPL)", "마이크론(MU)", "샌디스크"],
      "insight": "트럼프의 돌출성 20% 통행세 트윗은 글로벌 해상 운송 비용을 극단적으로 추정하게 만들어 유가 폭등을 유발했습니다. 지정학 불확실성이 상존하는 와중에 연준마저 추가 인상 카드를 만지작거리고 있어, 가치주(에너지/은행)와 성장주(빅테크) 간의 차별화가 심화되고 있습니다.",
      "action_point": "금리 급등의 피해가 큰 레버리지 테크주 비중은 줄이고, 사상 최고가를 갱신한 애플 중심의 온디바이스 AI 밸류체인과 에너지 원자재 섹터로 리스크를 분산해야 합니다."
    }
  },
  "QMyEr0KQDbc": {
    "primary_topic": "etc",
    "secondary_topics": [],
    "tags": ["안될과학", "비트박스", "사운드이펙트", "인간문화재", "실험예능"],
    "analysis": {
      "summary": "과학 예능 채널 안될과학에서 글로벌 비트박서 윙(WING)을 초대하여 마이크 기전 및 구강 구조를 통한 독창적인 사운드 묘사(비트박스 및 이색 소리)의 원리를 탐구하고, 유쾌한 사운드 배틀을 진행했습니다.",
      "key_claims": [
        "비트박스는 단순 소리 묘사를 넘어 구강 압력 조절과 호흡의 공명을 조율하는 고난도 신체 예술 활동입니다."
      ],
      "data_points": [],
      "signal": "na",
      "signal_reason": "순수 대중 예능/유머형 시사 과학 토크쇼 영상이므로 투자 시그널이 존재하지 않습니다.",
      "key_companies": [],
      "insight": "이 콘텐츠는 소리 음향 정보의 과학적 해설을 예능 포맷으로 전달하는 데 목적이 있습니다. 주식 투자 및 자산 관리 판단과는 무관합니다.",
      "action_point": "본 영상은 주식 시장의 흐름 분석이나 자산 포트폴리오 관리와 전혀 연관이 없는 흥미 위주의 콘텐츠이므로 투자 의사 결정 대상에서 완전 제외합니다."
    }
  },
  "rQBWsbxYl10": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["이동평균선", "리밸런싱", "포트폴리오", "반도체급락", "주린이구조대"],
    "analysis": {
      "summary": "주가 급락 장세에서는 자신이 보유한 개별 종목과 지수(Index)의 강도를 비교하여 매매 우선순위를 판단해야 합니다. 시장 지수가 회복 흐름을 보일 때, 지수보다 강하게 치고 나가는 종목(20일선 위에 위치)은 비중을 유지하되, 지수의 반등폭에 미치지 못하고 바닥을 맴도는 약한 종목은 <span class=\"text-rose-400 font-medium\">보유 비중의 70% 수준을 정리</span>하는 리밸런싱 기준을 가져야 합니다.",
      "key_claims": [
        "지수가 회복될 때 개별 종목이 20일 이동평균선 이상으로 복귀하는지 여부로 주도주와 소외주를 선별해야 합니다.",
        "지수 상승률보다 유독 약하고 20일선 아래에서 맴도는 약세 종목은 향후 포트폴리오 재편 시 가장 먼저 과감히 정리(최대 70% 비중 축소)하는 우선순위가 요구됩니다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "급락장에서 낙폭과대주들 중 펀더멘털에 기반한 기술적 반등 강도가 차별화될 것이므로, 철저한 종목 교체 매매 준비를 조언하는 가이드라인이기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "모든 주식이 같이 빠졌더라도 반등 시기에는 실적 강도에 따라 상승 속도가 완전히 달라집니다. 지수보다 약한 소외주를 쥐고 있기보다, 지수 대비 강한 복원력을 보여주는 주도 실적주로 압축하는 결단력이 장기 성과를 결정합니다.",
      "action_point": "향후 1~2주간의 기술적 반등 시점에 20일 이동평균선에 복귀하지 못하는 부실/소외 종목의 비중을 축소하고, 반등 복원력이 강한 반도체·IT 주도주로 리밸런싱을 진행해야 합니다."
    }
  },
  "TtLOy4-DhNo": {
    "primary_topic": "etc",
    "secondary_topics": [],
    "tags": ["노안", "라식부작용", "안과질환", "시력교정술", "신경안과"],
    "analysis": {
      "summary": "라식이나 라섹 등 시력교정 수술을 받은 환자들이 노화에 따라 노안을 마주했을 때 더 심각한 시각적 불편함을 겪게 되는 의학적 원인을 설명합니다. 시력교정술로 평평해진 각막 곡률은 노안용 다초점 렌즈 처방을 어렵게 만들며, 뇌가 변형된 시각 신호에 적응하는 속도가 느려져 안구 건조와 두통을 수반하는 복합 노안 부작용을 일으키게 됩니다.",
      "key_claims": [
        "젊은 시절 각막을 절삭하는 시력교정술(라식/라섹)을 받은 환자는 수정체 조절력이 떨어지는 노년기에 들어설 때 시각적 왜곡과 야간 눈부심이 더 심해집니다.",
        "라식 환자의 노안 치료는 단순 돋보기 안경 처방보다 각막 상태에 맞춘 맞춤형 RGP 렌즈나 제한된 특수 노안 백내장 수술 등을 신중히 선택해야 합니다."
      ],
      "data_points": [],
      "signal": "na",
      "signal_reason": "시력교정 수술 환자들의 노안 발병 특징과 치료 대안에 관한 순수 보건/의학 정보이므로 금융 투자 시그널과 무관합니다.",
      "key_companies": [],
      "insight": "이 정보는 헬스케어 및 안과 의료 기기 분야의 장기 수요 변화를 유추해 볼 수 있는 단서(노안 교정 특수 렌즈 수요 증대 등)를 제공하지만 직접적인 주식 매매 추천과는 거리가 멉니다.",
      "action_point": "순수 의학 상식 정보이므로 자산 관리 및 포트폴리오 전략 수립 대상에서 배제합니다."
    }
  }
}

for video_id, item in batch_data.items():
    save_and_delete(
        video_id=video_id,
        primary_topic=item["primary_topic"],
        secondary_topics=item["secondary_topics"],
        tags=item["tags"],
        analysis_data=item["analysis"]
    )
