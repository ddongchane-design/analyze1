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

# Batch 2 analyses
batch_2 = {
  "2JQWDZU_icE": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["SK하이닉스ADR", "나스닥상장", "바이오주", "리가켐바이오", "고환율"],
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">SK하이닉스(000660)</span>가 45조 원 규모의 ADR 나스닥 상장을 7월 10일로 확정 지으며 용인 클러스터와 청주 패키징 공장 등 반도체 인프라 투자 실탄을 확보했습니다. 한편, 미국 나스닥 바이오 지수의 사상 최고치 랠리에도 불구하고 국내 바이오 업종은 장기 바닥권에 머물러 있어 진입 전 추세 전환 확인이 필요합니다. 원·달러 환율이 1,540원대까지 급등했으나 대기 수급 요인에 따른 일시적 현상으로 분석됩니다.",
      "key_claims": [
        "SK하이닉스의 ADR 나스닥 상장과 유상증자(45.5조 원)는 단기 주주가치 희석 우려보다 장기 설비 투자 재원 확보 및 미국 시장 재평가(Re-rating)라는 호재 성격이 더 짙다.",
        "국내 바이오 주식(리가켐바이오 등)은 낙폭과대에 따른 일시적 반등에 추격 매수하기보다 전고점을 확실히 뚫고 안착하는 추세적 흐름을 확인하고 진입해야 안전하다.",
        "최근의 고환율(1,540원선)은 한국인들의 스페이스X 투자 자금 환전(3조 원 규모) 및 해외 기관 리밸런싱 수급 요인이 겹친 단기 과열 양상이다."
      ],
      "data_points": [
        "SK하이닉스 ADR 나스닥 상장 확정일: 7월 10일 (7월 9일 가격 결정)",
        "SK하이닉스 ADR 발행 규모: 45조 4,355억 원 (신주 1,779만 주)",
        "SK하이닉스 예상 발행가액: 2,555,000 원",
        "국내 투자자 최근 3일간 스페이스X 투자 환전 규모: 약 3조 원",
        "원·달러 환율: 장중 1,547~1,549원대 터치",
        "KOSPI 및 KOSDAQ 종가: KOSPI 3.3% 상승(8,471), KOSDAQ 3.26% 상승"
      ],
      "signal": "bullish",
      "signal_confidence": "medium",
      "signal_reason": "SK하이닉스의 글로벌 상장 본격화와 대규모 인프라 투자 확정은 국내 반도체 기업들의 밸류에이션 매력을 높이고, 고환율 장기화가 단기적으로 수출 대기업들의 환차익 어닝 서프라이즈로 연결될 수 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "리가켐바이오(141080)"],
      "insight": "주식시장의 수급 구조가 글로벌 차원에서 재편되고 있습니다. SK하이닉스의 ADR 상장은 마이크론과 TSMC 등 글로벌 반도체 기업들과의 직접적인 비교 평가(Peer Valuation)를 가능하게 해 코리아 디스카운트 해소에 기여할 것입니다. 또한 국내 가계 자금이 <span class=\"text-cyan-300 font-semibold\">스페이스X</span> 등 미국 비상장/테크 자산으로 직접 환전 및 유출되는 흐름은 원화 약세의 하방 지지 요인이 됨과 동시에, 국내 서민 물가에는 부담으로 작용하는 양날의 검입니다.",
      "action_point": "ADR 상장 이후 수급 유입 및 자사주 매입 소각 등 주주환원 정책 구체화를 모니터링하며 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span> 비중을 안정적으로 유지하되, 바이오 업종은 확실한 전고점 돌파(리가켐바이오 16만 5천원선 안착) 이후 추가 매수 타이밍을 조율해야 합니다."
    }
  },
  "ICoVvcF3ODs": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["SK하이닉스ADR", "반도체독주", "미국지수규제", "고환율", "수급분석"],
    "analysis": {
      "summary": "국내 증시는 <span class=\"text-cyan-300 font-semibold\">마이크론</span>의 호실적 호재로 반도체 중심의 강한 쏠림이 지속되는 반면, 코스닥 및 기타 소외 업종은 하루 단위 급등락만 거듭하며 연속성 없는 양상을 보여주고 있습니다. SK하이닉스의 45.5조 원 유상증자 기반 미국 ADR 상장은 글로벌 기관들의 매수 패시브 자금 유치 및 밸류에이션 리레이팅 관점에서 호재로 평가됩니다. 한편 미국 금융당국이 단일 종목 지수 비중을 제한하는 <span class=\"text-rose-400 font-medium\">소수 집중형 지수 규제</span>를 강화하면서 거대 빅테크 선물 거래 제약이라는 새로운 리스크가 제기되었습니다.",
      "key_claims": [
        "KOSPI는 연간 플러스 성장인 반면 KOSDAQ은 연간 마이너스로 주도주(반도체)와 주변주의 극단적인 양극화가 이어지고 있다.",
        "비반도체 섹터(바이오, 조선, 방산 등) 보유 투자자들은 막연히 싸다고 물타기를 하기보다, 해당 섹터 내 1등 대장주로 자금을 압축하여 교체 매매를 진행하는 것이 생존률을 높인다.",
        "미국의 단일 종목 지수 비중 30% 제한 규정(소수 집중형 지수)은 시총 비중이 비대해진 엔비디아나 마이크로소프트의 선물 파생상품 거래를 강제로 정지시킬 수 있는 잠재적 리스크다."
      ],
      "data_points": [
        "KOSDAQ YTD 상승률: 어제 2% 상승했음에도 연간 기준 -1% (KOSPI는 연간 플러스 지속)",
        "SK하이닉스 시간외 주가 상승률: ADR 상장 발표 후 약 5% 급등",
        "미국 소수 집중형 지수 규제 기준: 단일 종목 비중 30% 초과, 혹은 상위 5개 종목 합산 비중 60% 초과 시 지수 파생상품 거래 제한"
      ],
      "signal": "neutral",
      "signal_confidence": "high",
      "signal_reason": "마이크론 실적과 하이닉스 ADR 등 반도체 펀더멘탈은 견고하나, 지수 쏠림 심화로 타 섹터의 수급 고갈이 심각하며 미국 빅테크의 지수 비중 한계 규제 및 레버리지 리밸런싱 변동성이 하반기 지수 상단을 짓누를 우려가 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "반도체 독주 장세의 이면에는 철저한 수급 눈치보기가 존재합니다. 반도체가 랠리를 보일 때 타 섹터의 상승 연속성이 단절되는 현상은 시장 전반의 거래 대금 부족과 특정 빅테크로의 매수 쏠림 현상을 방증합니다. 특히 미국 테크 기업들의 급성장으로 지수 내 단일 비중이 규제선에 근접했다는 소식은 향후 패시브 ETF 및 선물 파생 상품의 수급 단절을 야기할 수 있어 각별한 대비가 필요합니다.",
      "action_point": "반도체 주도주 편입 기조를 유지하되, 주변 섹터(조선, 바이오)의 경우 반드시 2·3등주를 정리하고 1등 대장주로 압축 배정하는 <span class=\"text-amber-300 font-bold\">포트폴리오 재배치</span>를 단행해야 합니다."
    }
  },
  "JifZJZWWlPk": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["마이크론마진", "HBM가격협상", "삼성전자", "SK하이닉스", "소부장"],
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">마이크론</span>의 총 마진이 에르메스나 샤넬 등 명품 브랜드를 능가하는 84.9%를 기록하며 시장을 놀라게 했습니다. 이는 연말과 내년에 예정된 <span class=\"text-amber-300 font-bold\">HBM 공급 가격 재협상</span>에서 삼성전자와 SK하이닉스 역시 높은 단가와 이익률을 쟁취할 수 있다는 강력한 힌트입니다. 용산 WM센터 랩(Wrap) 포트폴리오는 시장 대비 50~60%의 초과 수익률을 기록하고 있으며, 여전히 반도체 소부장 전공정 및 패키징 기업에 주목하고 있습니다.",
      "key_claims": [
        "마이크론의 총 마진 84.9%는 HBM을 비롯한 AI 전용 D램의 독점적 지위를 입증하며, 국내 반도체 투톱의 7월 실적 발표 기대감을 대폭 끌어올린다.",
        "현재 HBM 공급 가격은 작년에 협상된 단가 기준이므로, 향후 가격 재협상이 본격 반영되는 연말 및 내년에 실적 퀀텀 점프가 일어날 것이다.",
        "삼성전자는 비교적 저평가 매력이 크고, SK하이닉스는 강력한 HBM 모멘텀과 ADR 상장 수혜를 입어 투자자 성향에 따라 선택할 수 있는 닉전/전닉 장세이다."
      ],
      "data_points": [
        "마이크론 Q3 마진율: 84.9% 기록 (시장 기대치 대폭 상회)",
        "용산 WM센터 Wrap 포트폴리오 성과: 코스피 BM 대비 50~60% 상회",
        "HBM 가격 인상폭: 기존 D램 대비 약 4배 수준 형성"
      ],
      "signal": "bullish",
      "signal_confidence": "high",
      "signal_reason": "마이크론의 기록적인 마진율은 AI 하드웨어 수요자가 가격 결정권을 칩 생산자에게 양보하고 있음을 보여주는 가장 명백한 증거이며, 가격 재협상 사이클 진입으로 삼성전자와 SK하이닉스의 마진 확대가 보장되어 있기 때문입니다.",
      "key_companies": ["마이크론(MU)", "SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "메모리 제조사가 명품 패션 하우스급의 이익률을 내는 기이한 장세가 지속되고 있습니다. 이는 AI 가속기 시장의 핵심 부품인 HBM의 희소성과 가치를 증명합니다. 삼성전자가 HBM4 규격으로 빠른 선회를 꾀하고 SK하이닉스가 HBM3E 및 ADR 상장을 바탕으로 추가 수급을 흡수하는 가운데, 대기 자금은 여전히 국내 반도체 대장주의 실적 확대에 가중치를 두고 있습니다.",
      "action_point": "단기 유상증자 공시에 따른 노이즈에 흔들리지 말고 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>와 <span class=\"text-cyan-300 font-semibold\">삼성전자</span> 투톱 비중을 든든히 유지하고, 낙폭이 과대했던 코스닥 <span class=\"text-cyan-300 font-semibold\">반도체 소부장 전공정 및 부품주</span>를 선별 매수하는 포지션이 유효합니다."
    }
  },
  "Rb4PDaiE_kY": {
    "primary_topic": "tech",
    "secondary_topics": ["economy"],
    "tags": ["중국AI", "과창판", "바이트댄스", "딥시크", "국산GPU"],
    "analysis": {
      "summary": "중국 인공지능(AI) 산업은 미국의 대중국 제재 속에서 **자본 유치, 국산 GPU 도입, 인프라 투자**를 하나로 연결하는 독자적인 중국식 선순환 생태계를 성공적으로 구축하고 있습니다. 상하이 루자주의 경제 포럼에서 증감회 주석은 첨단 기술 기업을 지원하기 위해 과창판 상장 특례를 확대하겠다고 발표했습니다. 틱톡의 모기업인 <span class=\"text-cyan-300 font-semibold\">바이트댄스</span>는 자체 탑바우 서비스를 위해 2선 국산 GPU 도입을 확대하고 있으며, 대표 AI 스타트업 <span class=\"text-cyan-300 font-semibold\">딥시크(DeepSeek)</span>는 국가 및 빅테크 자본을 대규모로 조달했습니다.",
      "key_claims": [
        "중국 자본 시장(증감회 우칭 주석)은 AI, 바이오 등 첨단 기업의 원활한 상장과 자금 조달을 위해 과창판(Star Market) 상장 요건을 파격적으로 완화하고 국가 자본을 투입하고 있다.",
        "바이트댄스는 화웨이, 캠브리콘 외에 2선 GPU 기업인 '일루바타 코어엑스'의 칩 5만 개 이상을 수입/검증하기 시작하여 AI 인프라 국산화 생태계를 2선 기업까지 다변화하고 있다.",
        "스타트업 딥시크는 단순 재무적 투자가 아닌 텐센트, CATL, 국가 AI 펀드 등 전방위 국가대표 동맹을 구축하여 인재 유치와 자체 국산 데이터센터 인프라 확장을 도모한다."
      ],
      "data_points": [
        "바이트댄스 중국 AI 비서 서비스: 탑바우 (중국 내 수개월째 AI 앱 점유율 1위)",
        "바이트댄스의 일루바타 칩 신규 구매 예정 수량: 최소 5만 개",
        "딥시크 신규 외부 자금 조달 규모: 약 500억 위안",
        "중국 빅테크의 AI 설비투자(CAPEX) 성장률 전망: 2026년 기준 전년비 25% 이상 증가"
      ],
      "signal": "bullish",
      "signal_confidence": "medium",
      "signal_reason": "미국 제제 우회를 넘어 중국 내부에서 자체 반도체 설계, 제조, 파생 서비스(LLM)에 이르는 강력한 수직 계열화 생태계가 구축되고 있으며, 중국 자본시장 정책 지원과 대형 펀드가 이를 강하게 뒷받침하고 있기 때문입니다.",
      "key_companies": ["바이트댄스", "화웨이", "텐센트", "CATL"],
      "insight": "중국은 AI 반도체 공급 차단이라는 외풍을 맞으며 오히려 국산 칩 제조 역량을 한 차원 끌어올리고 있습니다. 바이트댄스가 2선 GPU 브랜드의 대량 매수를 시작한 것은 중국 내부 AI 가속기 생태계의 다양화와 기술 신뢰도가 검증되고 있음을 시사합니다. 또한 <span class=\"text-cyan-300 font-semibold\">딥시크</span>가 CATL(전력 공급)과 텐센트(응용 서비스)를 우군으로 확보하고 네몽골에 대형 자체 데이터센터를 설립하려는 시도는 국가 전략 차원의 AI 주권 확보 움직임으로 읽어야 합니다.",
      "action_point": "글로벌 자산 배분 관점에서 코리아 디스카운트 및 미·중 제재 리스크를 분산하기 위해, 중국 과창판 기술주 지수를 추종하는 <span class=\"text-cyan-300 font-semibold\">국내외 ETF 상품</span>에 일부 자산을 나누어 배정하는 긴 안목의 전략이 유효합니다."
    }
  },
  "S86P-vnX_Xg": {
    "primary_topic": "tech",
    "secondary_topics": ["stock"],
    "tags": ["HBF", "낸드플래시", "샌디스크특허", "SK하이닉스AIN", "엔비디아CMX"],
    "analysis": {
      "summary": "AI 가속기 메모리의 절대 강자인 HBM의 자리를 위협할 차세대 메모리 기술로 낸드 플래시 기반의 **HBF(High Bandwidth Flash)**가 부상하고 있습니다. 샌디스크와 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>는 비휘발성 특성으로 리프레시 전력 소모를 획기적으로 줄일 수 있는 HBF 표준화를 추진 중이며, OCP(Open Compute Project)를 통해 빠른 시장 안착을 노리고 있습니다. 반면, 엔비디아는 HBM과 낸드를 패키징으로 직접 묶기보다 고속 네트워크로 연동되는 <span class=\"text-cyan-300 font-semibold\">CMX(Context Memory Storage)</span> 아키텍처를 제시해 다른 해법을 모색하고 있습니다.",
      "key_claims": [
        "HBF는 비휘발성인 낸드 플래시의 장점을 활용해, 데이터를 유지하기 위해 끊임없이 전력을 소모해야 하는 디램 기반 HBM의 치명적인 전력 및 발열 문제를 극복하고자 한다.",
        "낸드는 본질적으로 디램보다 속도가 느리지만, 수많은 채널과 다이, 플레인을 로직 다이로 묶는 극단적인 병렬화 구조를 적용해 초당 테라바이트(TB/s) 단위 대역폭을 확보한다.",
        "엔비디아는 GPU 패키지의 온도/수명 부하를 덜기 위해, 스펙트럼X 고속 네트워크를 통해 외부에 전용 스토리지를 두고 여러 GPU가 캐시(KV캐시)를 분할 공유하는 CMX 계층을 도입했다."
      ],
      "data_points": [
        "1세대 HBF 목표 스펙: 낸드 다이 16개 적층, 용량 512GB, 읽기 대역폭 1.6TB/s (2026 하반기 샘플, 2027 초 시스템 상용화 목표)",
        "HBF 로드맵 전망: 2세대 2TB/s, 3세대는 3.2TB/s 대역폭 및 스택당 최대 1.5TB 용량 목표",
        "TLC를 SLC 모드(pSLC)로 전환 시: 용량이 1/3로 줄어드는 대신, 셀 작동 속도와 내구성(PE cycle) 및 데이터 보존력 극대화"
      ],
      "signal": "bullish",
      "signal_confidence": "medium",
      "signal_reason": "AI 연산 모델 확장에 따른 HBM의 물리적/비용적 탑재 한계를 극복하기 위해, 차세대 낸드 기반 고대역폭 솔루션 표준화가 시작되었으며 이는 메모리 3사의 새로운 부가가치 성장 동력(NAND 리레이팅)이 될 수 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "샌디스크", "엔비디아(NVDA)", "삼성전자(005930)"],
      "insight": "HBM의 높은 가격 and 대기 전력 소모(리프레시)는 모바일 에이전트와 추론 중심 AI 서버 양산의 커다란 발림돌입니다. 샌디스크가 낸드 플래시의 오류와 인디어런스(쓰기 내구성) 한계를 극복하기 위해 pSLC 제어 및 오류정정(LDPC) 기능을 탑재한 HBF 특허를 내놓은 것은 메모리 적층의 새로운 패러다임을 뜻합니다. 다만 <span class=\"text-cyan-300 font-semibold\">엔비디아</span>는 이와 상반되는 CMX 네트워크 기반 공유 스토리지를 밀고 있어, 향후 온보드 가중치용 HBF와 원격 KV캐시용 CMX가 어떻게 상호 보완하며 AI 인프라를 지배할지 주목할 만합니다.",
      "action_point": "HBF 기술 표준을 OCP에서 먼저 추진하고 샌디스크와 협력 중인 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>의 차세대 메모리 선점 효과를 주시하면서, 낸드 적층 수혜 기업 및 8월 OCP 코리아 테크데이의 규격 확정 동향을 예의주시해야 합니다."
    }
  }
}

for vid, data in batch_2.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 2 completed!")
