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

batch_7 = {
  "_b1ZRGOvhCk": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["반도체저점반등", "문샷KimiK3평가", "AMD헬리오스채택", "루멘텀의견상향", "화웨이광연결"],
    "analysis": {
      "summary": "한경 글로벌마켓 빈난새 기자는 뉴욕 증시 개장 전, 반도체 및 AI 하드웨어 섹터가 기술적 조정을 마치고 저가 매수세 유입(나스닥 100 선물 +0.9%)으로 반등세를 보이고 있다고 전했습니다. 월가는 중국의 초거대 AI 모델 Kimi K3 출시가 오히려 더 많은 메모리와 컴퓨팅 자원을 요구할 뿐이라고 평가 절하했으며, AMD가 마이크로소프트를 자사 AI 랙 시스템인 '헬리오스'의 신규 고객사로 확보하고 바클레이스가 광모듈 업체 루멘텀의 투자의견을 매수로 상향하며 하드웨어 펀더멘탈의 건조함을 입증했습니다.",
      "key_claims": [
        "월가는 중국의 2.8조 파라미터 Kimi K3 모델에 대해, 연산 폭증으로 가동 이틀 만에 신규 가입을 차단하는 등 결국 초고용량 메모리 및 가속기 투자를 부추기는 결과로 이어질 것이라 진단했다.",
        "AMD는 엔비디아의 통합 시스템에 대응하는 AI 랙 시스템 '헬리오스(Helios)'의 신규 고객사로 마이크로소프트를 확보하며 4.6% 급등했다.",
        "바클레이스는 엔비디아의 광모듈 지연 루머가 사실무근임을 확인하며 광통신 부품사 루멘텀(Lumentum)의 투자의견을 매수로 상향 조정했다."
      ],
      "data_points": [
        "루멘텀 투자의견 조정: 바클레이스에서 중립에서 매수(Buy)로 상향 조정",
        "AMD 주가 변동: 마이크로소프트 고객사 합류 발표로 프리마켓 4.6% 급등"
      ],
      "signal": "positive",
      "signal_reason": "중국 AI 기술 추격이 역설적으로 반도체 대규모 수요를 촉진한다는 월가의 합의가 형성되었고, 마이크로소프트의 AMD 헬리오스 도입 및 광통신 부품사 루멘텀의 투자의견 상향 등 AI 인프라 수요 지속 호재가 다수 출현했기 때문입니다.",
      "key_companies": ["AMD(AMD)", "Lumentum(LITE)", "NVIDIA(NVDA)", "Microsoft(MSFT)"],
      "insight": "엔비디아뿐 아니라 AMD의 헬리오스 랙 채택 증가 및 광통신 모듈 수요 확대는 하드웨어 인프라 투자의 병목이 계속 확장되고 있음을 보여줍니다. 미세 지연 루머나 중국발 가성비 AI 위협론은 하드웨어 기업들의 구조적 성장 경로를 훼손하지 못합니다.",
      "action_point": "단기 조정으로 밸류에이션 매력이 부각된 반도체 소형 우량주 및 광통신 모듈 제조사(루멘텀 등)에 대한 저점 비중 확대를 고려하고, 하반기 칩셋 공급을 책임지는 국내 메모리 및 부품 밸류체인의 안정적 성장에 무게를 두어야 합니다."
    }
  },
  "S8Ww3ztKA9Y": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["미군중동전사", "구조적디젤쇼티지", "구조적원유제고", "구글프로즌2칩", "아이렌대형계약"],
    "analysis": {
      "summary": "한경 글로벌마켓 김종학 특파원은 뉴욕 증시가 장중 상승세를 유지하다 장 후반 애플의 차익 실현(-2%)과 미군 전사자 증가에 따른 지정학적 긴장감으로 흘러내리며 마감했다고 보도했습니다. 기술주 단에서는 구글의 전력·연산 비용을 10배 절감하는 추론 전용 칩 '프로즌 버전2(Frozen 2)' 개발 소식과 코어위브에 클라우드 계약을 체결한 아이렌(IREN)의 20% 급등, 루멘텀의 투자의견 상향이 겹치며 실적 확인 전 하방 경직성을 시험하고 있습니다.",
      "key_claims": [
        "미군의 이란 공습 및 이란의 보복 공격으로 미군 누적 전사자가 17명에 달해 트럼프 전 대통령이 보복을 경고하는 등 중동 리스크가 유가를 고공행진하게 만들고 있다.",
        "구글이 제미나이의 기본 추론 능력을 칩 자체에 내장해 전력 효율과 처리 속도를 6~10배 개선하는 신형 커스텀 칩 '프로즌 버전2(Frozen 2)'를 개발 중이다.",
        "클라우드 공급사인 아이렌(Iren)이 코어위브 등과 대형 클라우드 서비스 계약(28억 달러)을 체결해 연간 매출 목표를 조기 달성하며 20% 가까이 폭등했다."
      ],
      "data_points": [
        "아이렌(IREN) 실적 성과: 28억 달러 규모 다년 계약 체결로 주가 20%대 급등",
        "중동 군사 충돌 피해: 주말 미군 3명 사망, 1명 실종 (누적 17명 전사)"
      ],
      "signal": "neutral",
      "signal_reason": "구글의 신규 AI 칩 개발 및 테크주(아이렌, 루멘텀)의 실적 호재 등 긍정적 개별 요인과, 중동 전쟁의 사상자 발생 및 미 대선 주자들의 보복 경고 등 매크로 불안을 유발하는 부정적 요인이 상충하기 때문입니다.",
      "key_companies": ["Alphabet(GOOGL)", "IREN(IREN)", "Apple(AAPL)", "SpaceX"],
      "insight": "빅테크들은 천문학적 AI 투자 효율을 입증하기 위해 소프트웨어 최적화뿐 아니라 '추론 내장형 커스텀 실리콘(Frozen 2)' 등 전용 하드웨어 개발로 비용 구조를 획기적으로 낮추는 생존 전략을 펴고 있습니다. 중동 지정학적 위협이 단기 노이즈를 만들고 있으나 빅테크의 AI 효율화 경쟁은 쉼 없이 지속되고 있습니다.",
      "action_point": "유가 변동을 예의주시하되 AI 인프라 단가 인하 및 고효율화를 선도하는 빅테크(구글)와 이에 수혜를 받는 전용 인프라 공급사(아이렌, 루멘텀)의 비중을 긍정적으로 가져가는 것이 바람직합니다."
    }
  },
  "RVlWBnjF-oM": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["구조적공급부족", "K자형주가괴리", "재번스의역설", "오라클신용강등", "테슬라FCF전망"],
    "analysis": {
      "summary": "매경월가월부 문지웅 기자는 뉴욕 증시가 장 후반 하락 전환했으나 반도체 섹터의 펀더멘탈은 견조하다고 분석했습니다. JP모건은 메모리 반도체의 구조적 공급 부족이 2028년까지 지속될 것이라며 업종 비중확대 의견을 제시했고, 중국 Kimi K3의 컴퓨팅 한계로 인한 가입 중단 사태는 AI 고도화가 하드웨어 수요를 폭증시키는 '재번스의 역설'을 입증했으며, 구글의 신형 AI 칩 '프로즌(Frozen)' 개발 소식도 비용 효율성 개선 기대를 높이고 있습니다.",
      "key_claims": [
        "JP모건은 필라델피아 반도체 지수의 하락과 반도체 기업들의 실적 우상향 간의 괴리(K자형 악어입 괴리)가 너무 심해졌다며, 2028년까지의 공급 부족을 근거로 비중 확대를 권고했다.",
        "중국 Kimi K3의 컴퓨팅 파워 한계 봉착은 AI 성능 고도화가 정량적으로 더 많은 GPU, HBM, SSD 탑재를 강제한다는 점을 실증하여 메모리 반도체 산업의 강력한 장기 호재이다.",
        "아마존, 구글 등 하이퍼스케일러들의 CAPEX 지출로 현금흐름이 말라가고 있으며, 특히 오라클(Oracle)은 현금 고갈로 CDS 스프레드가 200bp로 폭증하고 신용등급이 BBB-로 강등되어 재정적 한계를 드러내고 있다."
      ],
      "data_points": [
        "오라클 CDS 스프레드: 200bp 돌파 (일반 테크 평균 80~90bp 대비 대폭 상회)",
        "테슬라 프리 캐시플로우(FCF) 전망: 2분기 32억 달러 적자 전환 우려 (1분기 14.4억 달러 흑자 대비 급감 예상)"
      ],
      "signal": "positive",
      "signal_reason": "JP모건의 구조적 반도체 쇼티지 진단과 중국 AI 모델의 컴퓨팅 용량 한계 도달이 장기 메모리 반도체 수요(Q)를 강력하게 지지하며, 주가와 이익 간의 비이성적인 괴리가 조만간 좁혀질 가능성이 크기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "NVIDIA(NVDA)", "오라클(ORCL)"],
      "insight": "오라클의 신용등급 강등과 FCF 적자는 빅테크들의 자금력 차별화가 진행되고 있음을 뜻합니다. 자본력이 튼튼한 알파벳, 메타 등 최고 우량 하이퍼스케일러들은 투자를 유지하겠지만, 레버리지가 높은 하위 하이퍼스케일러들은 CAPEX 조정 압박을 받을 것입니다. 그러나 반도체 기업들에게는 전 세계적 서버 메모리 공급 부족이라는 구조적 대세가 우세합니다.",
      "action_point": "단기 밸류에이션 괴리가 심해진 국내 반도체 대형주(삼성전자, SK하이닉스)의 저가 분할 매수 기조를 견지하고, 테슬라와 오라클 같이 FCF 현금 고갈 리스크가 있는 고부채 테크주에 대해서는 보수적인 포지션 관리를 추천합니다."
    }
  },
  "bWxWET2_57g": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["반도체저점반등", "KimiK3부하량", "하닉ADR하락", "수급꼬임여진", "반도체쇼티지"],
    "analysis": {
      "summary": "월가 뉴스레터는 뉴욕 증시가 지정학적 리스크와 알파벳 실적 대기 심리로 소폭 하락했으나 마이크론, 브로드컴 등 AI 하드웨어 섹터는 저가 매수 유입으로 반등 마감했다고 전했습니다. 특히 JP모건이 2028년까지의 반도체 공급 부족을 근거로 비중 확대를 권고했고, 중국 Kimi K3의 급증하는 연산 부하가 결국 메모리 반도체(DDR5, HBM, SSD) 수요를 가속화하는 핵심 동력으로 작용할 것이라는 전망이 지지력을 형성했습니다.",
      "key_claims": [
        "뉴욕 증시 하락에도 마이크론(+1.95%), 마벨(+3.3%), 루멘텀(+4.47%) 등 AI 하드웨어 및 광통신 섹터는 동반 상승하여 바닥 다지기를 시도했다.",
        "중국 스타트업의 Kimi K3 서비스 폭주 및 컴퓨팅 한계 고백은 기술적으로 메모리 성능과 대역폭의 한계 극복을 위해 메모리 반도체의 정량적 투입을 대폭 늘려야 함을 뜻한다.",
        "단, 국내 투자자들에게 아쉬운 점은 미 증시 내 반도체 반등에도 불구하고 SK하이닉스 ADR만 소폭 하락 마감하여 한국 시장의 수급 꼬임 여진이 남아있음을 시사했다."
      ],
      "data_points": [
        "반도체 종목 등락: 마벨 +3.3%, 마이크론 +1.95%, 루멘텀 +4.47% 반등"
      ],
      "signal": "positive",
      "signal_reason": "뉴욕 증시의 AI 하드웨어 밸류체인이 저점 반등 흐름에 안착했고, 중국 초거대 AI 경쟁이 메모리 공급 부족을 장기화시킨다는 구조적 펀더멘탈의 신뢰성이 재확인되었기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "마이크론 테크놀로지(MU)", "마벨 테크놀로지(MRVL)", "Lumentum"],
      "insight": "미 증시 반도체 상승에도 SK하이닉스 ADR이 하락한 것은 국내 파생상품(2배 레버리지 ETF) 규제 조치 및 리밸런싱 수급 불균형의 잔재 때문입니다. 이는 주가 펀더멘탈 요인이 아니므로 시간 경과에 따라 글로벌 마이크론 등 동종업계 주가와 동조화되며 해소될 것입니다.",
      "action_point": "해외 반도체 및 광통신 소부장 섹터의 반등 온기가 국내로 확산될 것을 염두에 두고, 수급 왜곡으로 과조정된 SK하이닉스 및 삼성전자 본주의 보유 비율을 그대로 유지할 것을 권장합니다."
    }
  },
  "Ro9JNJkpTvY": {
    "primary_topic": "tech",
    "secondary_topics": ["stock"],
    "tags": ["GLP1비만치료제", "도파민보상회로", "알코올니코틴억제", "중독치료적응증", "뇌과학혁신"],
    "analysis": {
      "summary": "위고비, 마운자로 등 GLP-1 계열 비만 치료제가 단순한 식탐 제어를 넘어 뇌의 도파민 분비 보상 경로를 제어함으로써 술과 담배, 도박 등에 대한 중독성 갈망(Craving)을 차단하는 신규 부작용(적응증 확장성)이 글로벌 환자들 사이에서 광범위하게 확인되고 있습니다. 이는 뇌과학 기반의 중독 치료라는 새로운 의료 파이프라인의 실현 가능성을 높여 바이오텍 분야의 추가적인 가치 리레이팅 동력으로 분석됩니다.",
      "key_claims": [
        "GLP-1 비만 치료제가 뇌의 쾌락 보상 신호를 직접 무디게 만들어 알코올, 니코틴, 쇼핑 등 의존성 중독 행위에 대한 차단 효과를 유도한다.",
        "글로벌 주요 제약사들의 관련 임상이 개시됨에 따라 중독 치료 시장으로의 공식 진입이 예고된다."
      ],
      "data_points": [
        "약물 기전: 뇌의 중추 신경계 내 보상 반응 억제를 통한 강박 억제"
      ],
      "signal": "positive",
      "signal_reason": "비만 신약의 치료 범위가 뇌 과학 및 중독 치료제라는 거대 시장으로 정식 연계되면서, 글로벌 신약 개발사와 원료 밸류체인 기업들의 장기 수익성이 증명되기 때문입니다.",
      "key_companies": ["Novo Nordisk(NVO)", "Eli Lilly(LLY)"],
      "insight": "비만 치료제의 중독 차단 효과는 인류의 소비 패턴 변화를 촉발할 수 있는 파괴력을 내포하고 있습니다. 주류, 담배 등 도파민 의존성 전통 비즈니스에 대한 부정적 요인인 반면, 헬스케어 섹터에는 전례 없는 다목적 혁신 신약 프리미엄이 지속 부과될 것입니다.",
      "action_point": "글로벌 비만약 독점 기업들에 대한 중장기 투자 관점을 긍정적으로 유지하며, 주류 및 가공식품 산업의 장기 밸류에이션 제약 압박 요인으로 간주해야 합니다."
    }
  }
}

for vid, data in batch_7.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 7 completed!")
