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

batch_2 = {
  "B7wXqwO2EI0": {
    "primary_topic": "economy",
    "secondary_topics": ["tech"],
    "tags": ["소재의한계", "철강산업혁명", "자원민족주의", "대체불가대한민국", "희토류보복"],
    "analysis": {
      "summary": "산업혁명을 가능케 했던 핵심 한계가 철강 소재였듯, 현대 첨단 AI 및 데이터센터 산업의 성패 역시 반도체 소재, 희토류, 전력 기기 및 특수 합금 등 '물리적 소재의 공급 한계'에 의해 결정됩니다. 국가 간 첨단 소재 및 자원의 무기화(자원민족주의)가 격화되는 환경에서 국산 대체 불가 핵심 소재 밸류체인의 전략적 가치가 더욱 높아지고 있습니다.",
      "key_claims": [
        "산업혁명 당시 증기기관의 출현과 확산을 보장한 것은 철강 소재의 상용화였듯, 소재는 인류 기술 발전의 한계를 정의한다.",
        "글로벌 자원민족주의와 희토류·첨단 소재 무기화가 현실화되면서 공급망 내 대체 불가능한 소재 기술을 지닌 포스코그룹 등 독점 기업의 체력에 주목해야 한다.",
        "AI 소프트웨어와 반도체 장비의 한계선 또한 최첨단 소재 패키징(유리 기판, 특수 CCL 등)과 전력 소재에 의해 제약받게 된다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "첨단 기술 성장의 병목이 디지털 알고리즘에서 물리적 자원·소재로 이동하며 소재 기업의 전략적 가치는 높아지나, 자원 분쟁 리스크가 공존하기 때문입니다.",
      "key_companies": ["POSCO홀딩스(005490)"],
      "insight": "AI와 첨단 제조의 진정한 병목은 소프트웨어가 아닌 소재입니다. 특수 합금, 희귀 금속, 첨단 기판 소재 등 대체 불가능한 물리적 재료를 쥔 기업이 장기 패권을 쥐게 됩니다.",
      "action_point": "자원 무기화 시대에 대응하여 국산화율이 높고 대체 불가능한 특수 소재 및 차세대 기판 소재 밸류체인을 장기 파이프라인으로 구성해야 합니다."
    }
  },
  "7xxvZ4AOEYs": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["DRAM수출단가폭등", "LTA파기조건분석", "SMCI시간외급등", "트럼프관세만료", "마이클버리그림자부채"],
    "analysis": {
      "summary": "하이닉스 ADR(+13.8%)과 마이크론(+12.2%), SOXL(+15.6%)이 폭등한 가운데 7월 20일 기준 한국 DRAM 수출 단가가 전년 대비 527%, 전월 대비 22% 폭등해 반도체 실적 가시성이 탄탄함을 입증했습니다. 번스타인(Bernstein)은 현물 가격 급락과 위약금 조건을 비교해 LTA(장기공급계약)의 파기 가능성을 분석하며 현재는 현물가가 높아 LTA가 매우 견고하다고 진단했습니다. 반면 7월 24일 무역법 관세 만료에 따른 트럼프 301조 추가 관세 지정 위험과 AI 데이터센터 SPV의 3,000억 달러 우회 그림자 부채(마이클 버리가 지적) 리스크는 지속 관찰 과제입니다.",
      "key_claims": [
        "한국 7월 20일 누적 DRAM 수출 단가는 전년비 527%, 전월비 22% 폭등하여 범용 DRAM 중심의 폭발적인 수익성 개선을 입증했다.",
        "번스타인 분석에 따르면 LTA(장기공급계약)는 현물 가격이 LTA 최저 구매가 및 위약금 차감액 이하로 폭락하지 않는 한 파기되지 않으므로 현재의 LTA 구속력은 강고하다.",
        "마이클 버리는 하이퍼스케일러들이 데이터센터 구축 시 장부에 부채를 잡지 않기 위해 특수목적법인(SPV)과 사모펀드(아폴로 등)를 거쳐 3,000억 달러의 그림자 부채(Shadow Debt)를 유발한 순환 거래 구조의 위험성을 경고했다."
      ],
      "data_points": [
        "한국 DRAM 수출 단가 상승률: 전년비 +527%, 전월비 +22% (반도체 수출 중 DRAM 비중 55%)",
        "NAND 및 HBM 수출 단가: 전년비 수백% 높은 수준이나 전월비 NAND -22%, HBM -8% 소폭 조정",
        "주요 지표: 하이닉스 ADR +13.75%, 마이크론 +12.17%, 샌디스크 +14.27%, SOXL +15.58%, 램ETF +21.72%",
        "트렌드포스 전망: 낸드(NAND) 공급 부족 해소 시점은 2027년 하반기 전망"
      ],
      "signal": "positive",
      "signal_reason": "DRAM 수출 단가의 폭발적 상승과 LTA 계약의 탄탄한 구속력, 마이크론·하이닉스 ADR 폭등이 수급 악재를 압도하며 강력한 주가 반등을 이끌고 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "Micron(MU)", "Super Micro Computer(SMCI)"],
      "insight": "월가의 부정적 리포트에도 불구하고 DRAM 수출 단가 전월비 +22% 폭등이라는 실증 데이터가 하이닉스와 마이크론의 실적을 증명하고 있습니다. LTA 파기 우려는 현물가가 고공행진하는 현 시점에서는 시기상조입니다.",
      "action_point": "DRAM 수출 단가 호조에 직결되는 메모리 대형주(SK하이닉스)의 적극적 매수 관점을 유지하고, 7월 24일 관세 발표 및 SPV 부채 논란의 추이를 주시해야 합니다."
    }
  },
  "TkDRltnF5Ng": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "crypto"],
    "tags": ["미중9월AI회담", "워터마크조사", "클래리티법안타결", "슈퍼마이크로급등", "애플리스구독"],
    "analysis": {
      "summary": "미국과 중국이 오는 9월 AI 안전 및 지적재산권 회담 개최에 합의한 가운데, 미 재무부가 중국 LLM(Kimi K3 등) 내 미국 모델 워터마크 기술 도용 조사를 가동했습니다. 크립토 규제안인 클래리티 법안(Clarity Act)의 상원 막판 타결 기대감으로 코인베이스(+9%) 및 암호화폐 관련주가 급등했으며, 슈퍼마이크로컴퓨터(SMCI)가 마진 폭증으로 시간에 15~20% 폭등하고 TSMC가 10% 가격 인상을 단행하는 등 테크 호재가 쏟아졌습니다. 애플은 기가당 단가 상승 극복을 위해 '아이폰 구독/리스 프로그램'을 전격 추진 중입니다.",
      "key_claims": [
        "미국과 중국이 9월 양자 AI 회담을 열어 안보, 군사 및 워터마크 도용 문제를 논의할 예정이나 양국 간 기술 자원 전쟁은 가속되고 있다.",
        "크립토 클래리티 법안의 상원 윤리 조항 타결 임박 소식에 비트코인이 $66,000를 회복하고 코인베이스(+9%), 서클(+8.5%) 등 관련주가 강세를 보였다.",
        "슈퍼마이크로컴퓨터(SMCI)는 4분기 마진율이 15~17%로 컨센서스를 대폭 상회하며 장외에서 15~20% 폭등했다.",
        "애플은 고가 단말기 부담 완화 및 재고 축소를 위해 아이폰 구독·리스형 보상 판매 프로그램을 전격 도입했다."
      ],
      "data_points": [
        "주요 종목 상승률: 코인베이스 +9%, 서클 +8.5%, SMCI 시간외 +15~20%, TSMC +5.48%, 인텔 +8.64%, 네비우스 +18%",
        "구글 알파벳 신규 모델: 제미나이 3.5 플래시 사이버 및 3.6 플래시 (토큰 사용량 17% 절감)"
      ],
      "signal": "positive",
      "signal_reason": "크립토 법안 타결 호재와 슈퍼마이크로컴퓨터의 마진 폭등, 비트코인 및 테크 주도주들의 일제히 일어난 폭등세가 지수 반등을 견인하고 있기 때문입니다.",
      "key_companies": ["Super Micro Computer(SMCI)", "TSMC(TSM)", "Coinbase(COIN)", "Apple(AAPL)", "Intel(INTC)"],
      "insight": "애플의 하드웨어 구독 모델 도입은 높은 칩셋 및 장비 단가 상승을 소비자에게 매달 리스료 형태로 분할 전가하려는 신규 수익화 전략입니다. 테크사들은 가격 인상분을 소비자와 기업에 성공적으로 전가하고 있습니다.",
      "action_point": "가상자산 법안 수혜주(코인베이스) 및 마진 폭증이 확인된 AI 서버 랙 밸류체인(SMCI, 델)에 매수세를 배분하고, 미중 AI 회담 관련 보복 조치 발표를 모니터링해야 합니다."
    }
  },
  "kmGYIP9lKhU": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["개장전요것만", "정제마진폭등", "금저가매수론", "TSMC가격인상", "반도체실적킹"],
    "analysis": {
      "summary": "한경 빈난새 기자는 장 개장 전 나스닥(+1.4%)과 반도체주 상승세를 전하며, 러시아 정제 시설 타격으로 국제 정제 마진이 폭증해 유가(WTI $84.1, 브렌트 $90.9) 상승 압력이 지속되고 있다고 분석했습니다. 월스트리트저널(WSJ)이 금($4,062)의 저가 매수 타당성을 보도한 가운데, TSMC의 10% 가격 인상 공시는 고물가·고금리 매크로 속에서도 가격 결정력(Pricing Power)을 지닌 반도체가 유일한 '실적 킹(King)'임을 증명했습니다.",
      "key_claims": [
        "러시아 정제 시설 타격 및 정제유 수출 금지로 원유보다 정제 마진(휘발유, 디젤, 항공유)이 급등하여 인플레이션 우려를 자극하고 있다.",
        "TSMC의 내년 10% 가격 인상 단행은 고금리·고환율 국면에서도 원가 인상분을 고객사로 온전히 전가할 수 있는 독점적 가격 결정력을 증명했다.",
        "미국 달러와 채권 금리가 동시에 고점을 갱신하고 있으나, 마이크론(+6%), 샌디스크(+7%) 등 실적이 확실한 반도체로 자금이 쏠리고 있다."
      ],
      "data_points": [
        "유가 및 금속: WTI $84.1/bbl, 브렌트유 $90.9/bbl, 금 $4,062/oz (+1%), 은 $59.3/oz (+4%)",
        "국채 금리: 미 10년물 국채 금리 4.60%선 회복"
      ],
      "signal": "positive",
      "signal_reason": "TSMC의 가격 인상 능력이 증명하듯 반도체 업종의 독보적인 가격 결정력과 펀더멘탈 우위가 국채 금리 및 인플레이션 악재를 무력화하고 있기 때문입니다.",
      "key_companies": ["TSMC(TSM)", "Micron(MU)", "GE Vernova(GEV)", "Caterpillar(CAT)"],
      "insight": "인플레이션과 고금리 국면에서 승리하는 기업은 원가 상승분을 고객에게 100% 넘길 수 있는 독점적 가격 결정력을 지닌 기업뿐입니다. TSMC와 HBM 공급사가 그 대표적인 예시입니다.",
      "action_point": "독점적 전가 능력이 확인된 첨단 반도체 파운드리 및 대표 메모리 밸류체인 비중을 굳건히 유지하고, 금 및 인프라 기기(GE버노바)주를 우량 보조 축으로 삼아야 합니다."
    }
  },
  "X8NEHXVbGKk": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["인텔인력감축", "포티넷파운드리수주", "미중9월회담", "반도체급반등"],
    "analysis": {
      "summary": "미국과 중국의 9월 AI 샌프란시스코/베이징 회담 일정 타결 소식 속에, 인텔(INTC)이 비용 구조 개선을 위한 대규모 인력 감축 공시 및 포티넷(Fortinet)과의 차세대 보안 칩 파운드리 수주 계약 체결 소식으로 주가가 8.64% 급등했습니다. 그동안 시장 하락을 이끌던 반도체 수급 꼬임이 완화되며 기술주 전반으로 저가 매수세가 가파르게 유입되는 흐름입니다.",
      "key_claims": [
        "인텔이 대대적인 구조조정(인력 감축)과 함께 포티넷의 차세대 보안 칩 파운드리 수주 성과를 내며 주가가 8.64% 폭등했다.",
        "미중 양국이 9월 AI 정상급 회담을 결정함에 따라 기술 안보 규제에 대한 불확실성이 일단 소강 상태에 접어들었다.",
        "매도세가 과도했던 필라델피아 반도체 지수와 주요 밸류체인으로 전반적인 숏커버링 및 기술적 반등 자금이 강하게 유입되었다."
      ],
      "data_points": [
        "인텔(INTC) 주가 상승률: +8.64%"
      ],
      "signal": "positive",
      "signal_reason": "인텔의 파운드리 수주 및 구조조정 성과와 반도체 주도주 전반의 강한 기술적 반등세가 시장 불안 심리를 빠르게 잠재우고 있기 때문입니다.",
      "key_companies": ["Intel(INTC)", "Fortinet(FTNT)", "NVIDIA(NVDA)"],
      "insight": "인텔의 파운드리 수주는 미 정부의 반도체 국산화(CHIPS Act) 지원 의지와 맞물려 의미 있는 바닥 신호를 제공합니다. 비용 절감과 고객사 확보가 동시에 이뤄지는 턴어라운드 흐름입니다.",
      "action_point": "턴어라운드 모멘텀이 발생한 인텔과 보안 칩 밸류체인의 단기 반등 추세를 모니터링하며 기술주 포트폴리오를 유지해야 합니다."
    }
  }
}

for vid, data in batch_2.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 2 completed!")
