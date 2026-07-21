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
  "cgAYeXmICfk": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["레버리지ETF", "ETF규제", "수급교란", "반대매매", "코스피폭락"],
    "analysis": {
      "summary": "최근 코스피 지수가 9% 폭락하고 선물이 -10%에 육박하는 급락세를 보인 주원인은 지정학적 매크로 악재보다 국내 <span class=\"text-rose-400 font-medium\">단일 종목 레버리지 ETF</span>에 대한 정부의 규제 움직임 때문입니다. 회전율을 하루 100%로 제한한다는 등 강력한 규제 루머가 돌자, 고회전율로 거래하던 기관 및 전문 투자자들이 선제적으로 청산에 나서며 <span class=\"text-rose-400 font-medium\">수급의 꼬임</span>과 투매를 촉발시켰습니다.",
      "key_claims": [
        "한국 반도체 투톱(삼성전자, SK하이닉스)을 추종하는 레버리지 ETF의 거래 대금 쏠림이 50%를 초과하는 비정상적 구조가 조정을 심화시켰습니다.",
        "레버리지 ETF의 일일 회전율을 100%로 제한하는 규제 방안이 거론되자 전문 트레이더들이 시장 이탈을 대비해 주식을 대량 매도했습니다.",
        "미수 및 신용 상환 기한이 도래하면서 아침 9시 전후에 반대매매 매물이 쏟아져 나와 주가 하락 폭을 키우는 악순환이 발생하고 있습니다."
      ],
      "data_points": [
        "단일 종목 레버리지 ETF 상위 5개 비중: 전체 ETF 거래의 약 52% 수준",
        "레버리지 ETF 도입 이후 개인 순매수 총합: 약 14조 원 (SK하이닉스 9조 원, 삼성전자 5조 원)",
        "국내 코스피 선물 일일 하락률: 최대 -9.95% 기록"
      ],
      "signal": "bearish",
      "signal_reason": "규제 실행 여부를 둘러싼 정책 혼선이 해소되기 전까지는 단기 거래 대금 축소와 레버리지 청산에 따른 주가 하락 압력이 우세합니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "한국 증시의 고질적인 수급 취약성이 금융 당국의 규제 발표와 맞물리며 변동성을 극대화했습니다. 꼬리가 몸통을 흔드는(Wag the dog) 파생/레버리지 규제 노이즈가 단기적으로 시장의 체력을 크게 갉아먹고 있습니다.",
      "action_point": "정부 규제안의 세부 사항이 발표되고 수급 꼬임이 완화되는 7월 중순까지 레버리지 상품 이용을 줄이고, 현금 비중을 늘려 보수적으로 대처해야 합니다."
    }
  },
  "eP7akLz_ecA": {
    "primary_topic": "crypto",
    "secondary_topics": ["stock"],
    "tags": ["디파이", "토큰재매입", "로빈후드L2", "코인베이스", "크립토수익성"],
    "analysis": {
      "summary": "크립토 시장의 가치 평가 기준이 기술적 낭만에서 기업 재무제표와 같은 <span class=\"text-amber-300 font-bold\">사업적 가치 및 수익성</span>으로 빠르게 이전하고 있습니다. 가상자산 하락장 속에서도 실질 거래 수수료를 활용해 토큰 재매입(Buyback)을 집행하는 디파이(DeFi) 프로젝트들이 비트코인 대비 높은 수익률을 올렸습니다. 또한 로빈후드, 코인베이스 등 전통 <span class=\"text-cyan-300 font-semibold\">핀테크 플랫폼</span>이 1세대 디파이의 유동성을 활용해 결합하는 흐름이 대세로 자리 잡고 있습니다.",
      "key_claims": [
        "2023년 강세장과 달리, 2026년 하락장에서는 단순한 기술적 혁신보다는 실질 수익 창출력과 바이백 실행력이 토큰 가격을 결정합니다.",
        "크립토 생태계에서 가장 안정적이고 압도적인 이익을 내는 섹터는 덱스(DEX) 및 선물 거래 플랫폼 등 거래 중개 비즈니스입니다.",
        "로빈후드가 자체 레이어 2(L2) 체인을 런칭하며 일주일 만에 3억 달러의 유동성을 끌어모은 것은 핀테크와 디파이 결합의 대표적 사례입니다."
      ],
      "data_points": [
        "비트코인 등락률 대비 토큰 재매입 프로젝트 성과: 비트코인 -17% 하회 시, 수익형 디파이 프로젝트는 평균 +30% 아웃퍼폼",
        "로빈후드 자체 레이어 2 런칭 초기 자금 유입: 출시 1주일 만에 3억 달러 돌파"
      ],
      "signal": "neutral",
      "signal_reason": "크립토 전체 시장은 침체기이나, 실질 캐시플로우가 나오는 우량 디파이(DeFi) 프로토콜 및 대형 플랫폼 협업 체인은 견고한 성장세를 보이기 때문입니다.",
      "key_companies": ["로빈후드(HOOD)", "코인베이스(COIN)", "Uniswap", "Aave"],
      "insight": "가상자산도 주식 시장처럼 '이익을 내지 못하면 버려지는' 가치 평가 정상화 단계를 지나고 있습니다. 대형 웹2 핀테크 플랫폼들이 백엔드 유동성 공급원으로 스트레스 테스트를 거친 1세대 디파이 프로토콜을 적극 채택하고 있어 공급망이 소수 우량주 위주로 재편됩니다.",
      "action_point": "수익 모델이 불분명한 유행성 알트코인 투자는 전면 지양하고, 수수료 수익 및 바이백을 실행하며 핀테크 대기업과 연동되는 메이저 디파이 코인 위주로 접근해야 합니다."
    }
  },
  "G5wIYYNxDBI": {
    "primary_topic": "robot",
    "secondary_topics": ["tech", "stock"],
    "tags": ["3대메가프로젝트", "피지컬AI", "3M전략", "휴머노이드", "로봇부품국산화"],
    "analysis": {
      "summary": "정부가 반도체, AI 데이터 센터와 함께 <span class=\"text-cyan-300 font-semibold\">피지컬 AI(로봇)</span>를 국가 산업 경쟁력 강화를 위한 '3대 메가 프로젝트'로 공식 선정하고 집중 육성합니다. 이에 따라 제조업 AI 전환을 위한 '3M 전략'이 가동되어 매년 1천 대 규모의 업종 특화 로봇 보급이 추진됩니다. 또한, 핵심 부품인 <span class=\"text-cyan-300 font-semibold\">액추에이터, 로봇손, 센서</span>의 국산화를 유도하고 3년 내 범용 파운데이션 모델을 개발하여 글로벌 휴머노이드 시장 점유율을 1%에서 20%로 도약시키겠다는 구체적 로드맵을 제시했습니다.",
      "key_claims": [
        "정부는 로봇 활용 선도국에서 로봇 제조 강국으로 거듭나기 위해 제조업 AI 전환(MAX), 부품 국산화(MASTER), 지역 거점 양산(MASS PRODUCTION)의 '3M 전략'을 제시했습니다.",
        "물리적 법칙을 따르는 로봇 데이터 수집의 높은 난이도를 해결하기 위해, 실제 제조 현장 데이터와 시뮬레이션 합성 데이터를 융합하는 데이터 체계를 구축합니다.",
        "국방, 교육, 재난 대응 등 공공 조달을 활용해 대규모 초기 수요를 창출하고 국민 성장 펀드를 연계하여 투자를 지원합니다."
      ],
      "data_points": [
        "글로벌 휴머노이드 시장 내 국내 점유율 목표치: 현재 약 1% 수준 -> 2030년까지 20% 달성 계획",
        "로봇 전문인력 육성 목표: 향후 5년간 10,000명 양성",
        "로봇 개발을 위한 물리 데이터 셋 격차: 기존 LLM(약 10만 년 데이터) 대비 피지컬 AI 데이터는 약 1만 시간에 불과하여 시뮬레이션 합성 데이터 병행 필수"
      ],
      "signal": "bullish",
      "signal_reason": "로봇 산업이 국가 주권 프로젝트로 격상되며 국산 부품 R&D 예산 집중 및 공공 수요 대량 발주 등 직접적이고 실질적인 정책 수혜가 장기 보장되기 때문입니다.",
      "key_companies": ["두산로보틱스", "레인보우로보틱스", "현대차그룹", "에스피지"],
      "insight": "단순 자동화 장비 수준에 머물던 국내 로봇 산업이 국가 전략 핵심 인프라인 '피지컬 AI'로 거듭났습니다. R&D 세액 공제, 파운드리 구축 및 공공 우선 구매가 보장됨으로써 소프트웨어(파운데이션 모델)와 하드웨어(액추에이터/감속기)의 국산 밸류체인 전반이 고속 성장을 이룰 것입니다.",
      "action_point": "성장주 약세로 최근 밸류에이션 조정을 거친 로봇 완제품 제조사 및 국산화 핵심 부품사(액추에이터, 감속기, 로봇손)를 중심으로 장기 관점의 비중 확대를 추천합니다."
    }
  },
  "GtLDChEfQgc": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["외국인이탈", "환율변수", "미국금리인상", "달러강세", "코스피이탈"],
    "analysis": {
      "summary": "코스피 최고치 국면에서 외국인 투자자들이 이탈하는 핵심 원인은 원화 약세(환율 상승) 리스크 때문입니다. 연초의 미 연준 금리 인하 기대가 완전히 무너지고 오히려 미국 예외주의 성장과 높은 장기 금리가 유지되면서, 글로벌 자본이 금리가 더 높은 미국 국채와 회사채 자산으로 쏠리고 있습니다. 환율의 추가 약세를 방어하고 외국인이 유입되기 위해서는 연준의 추가 <span class=\"text-rose-400 font-medium\">금리 인상 우려</span>가 완화되고 원화 가치가 안정되어야 합니다.",
      "key_claims": [
        "외국인의 코스피 이탈은 국내 기업 펀더멘털의 악화가 아닌 강달러 대비 원화 가치의 약세 방어가 어렵다는 환율 리스크에서 출발합니다.",
        "미국 경제의 양호한 성장세로 인해 장기 금리가 떨어지지 않아 글로벌 자금이 금리 메리트가 높은 미국의 국채/회사채로 유출되고 있습니다."
      ],
      "data_points": [
        "미 연준 올해 금리 경로 전망: 연초 2~3회 인하 기대 -> 최근 연내 추가 인상(1~2회) 우려로 선회"
      ],
      "signal": "neutral",
      "signal_reason": "원화 약세 압력에 따른 외국인 자금 이탈은 매크로 금리 스프레드에 기인하므로 단기적인 원-달러 환율 안정이 급선무이기 때문입니다.",
      "key_companies": ["국민연금", "삼성전자", "SK하이닉스"],
      "insight": "환율이 1,400원대를 상회하는 상태에서는 외국인 입장에서는 코스피 주가가 올라도 환차손으로 인해 수익이 상쇄됩니다. 결국 연준의 추가 긴축 신호가 잦아들거나 물가 지수가 안정을 찾는 등의 대외 매크로 트리거가 필요합니다.",
      "action_point": "환율의 방향성을 결정할 내일의 미국 CPI 지표와 금리 추이를 면밀히 모니터링하며, 포트폴리오의 대외 환 노출 자산과 내수 방어주 비율을 적절히 조절해야 합니다."
    }
  },
  "hebAdr1puu4": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["SK하이닉스ADR", "호르무즈해협", "유가폭등", "긴축우려", "금리상승"],
    "analysis": {
      "summary": "최근 뉴욕 증시는 <span class=\"text-rose-400 font-medium\">SK하이닉스 ADR 9.3% 급락</span> 여파로 반도체주들이 무더기 폭락하며 투심이 크게 위축되었습니다. 여기에 도널드 트럼프 전 대통령의 '호르무즈 해협 안보 수호 대가로 20% 통행료 부과' 발언으로 유가가 10% 가까이 폭등(WTI 78달러 돌파)했습니다. 설상가상으로 연준의 대표 매파 크리스토퍼 월러 이사가 추가 물가 자극 시 금리 인상이 불가피하다고 직격탄을 날려 10년물 국채 금리가 4.62%까지 치솟고 긴축 공포가 재현되었습니다.",
      "key_claims": [
        "SK하이닉스의 미국 상장 주식(ADR)이 9.32% 하락하며 상장 당일 가격 수준인 152달러까지 폭락하여 글로벌 반도체 동반 매도를 주도했습니다.",
        "트럼프의 호르무즈 해협 이권 주장은 지정학 갈등을 부채질하여 WTI 유가를 10%에 육박하게 급등시켰고, 해상 수송량을 즉각 반토막 냈습니다.",
        "월러 연준 이사는 근원 인플레이션의 주범으로 관세 외에도 유가와 AI 인프라 구축 비용을 지목하며 필요시 기준금리 인상을 직접 검토해야 한다고 강조했습니다."
      ],
      "data_points": [
        "SK하이닉스 ADR 등락률: -9.32% 하락 (152.35달러, 상장 공모가 149달러선 근접)",
        "국제 유가 등락률: WTI 기준 9.38% 급등 (배럴당 78.11달러), 브렌트유 80달러선 재돌파",
        "미국 10년물 국채 금리: 4.622% 돌파 (5.3bp 상승)",
        "연준의 7월 기준금리 인상 확률: 선물 시장 기준 43%까지 급상승"
      ],
      "signal": "bearish",
      "signal_reason": "하이닉스 ADR 폭락에 따른 반도체 밸류 체인의 동반 조정, 유가 폭등에 의한 인플레이션 자극, 매파적 연준 이사의 금리 인상 위협이 겹쳤기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "엔비디아(NVDA)", "마이크론(MU)", "인텔(INTC)", "샌디스크"],
      "insight": "반도체 공급 과잉 논란과 대외 매크로 악재(유가 폭등, 금리 재인상 확률 급증)가 절묘하게 교차했습니다. 특히 AI 인프라 확장에 따른 하드웨어 가격 상승이 역으로 글로벌 인플레이션의 원인(AI 인플레이션)으로 지목받으며 긴축의 명분을 주고 있는 아이러니한 구조입니다.",
      "action_point": "미국의 금리 상승에 정비례해 변동성이 극대화될 반도체 장비 및 빅테크 종목에 대한 현금 보호 전략을 펴고, 유가 폭등 수혜주(에너지, 상사) 위주로 단기 피난처를 마련해야 합니다."
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
