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

# Batch 3 analyses
batch_3 = {
  "SnJKGFIYD8M": {
    "primary_topic": "tech",
    "secondary_topics": ["stock", "economy"],
    "tags": ["한국AI", "AI스타트업", "VC투자", "빅테크독점", "거품론"],
    "analysis": {
      "summary": "대부분의 국내 AI 스타트업들이 빅테크의 강력한 글로벌 독점력에 밀려 고사할 위험에 처해 있으며, 정부 세금으로 매칭된 <span class=\"text-rose-400 font-medium\">VC(벤처캐피탈) 펀드</span> 상당수가 공중 분해될 것이라는 전문가들의 경고가 나왔습니다. 차별화된 핵심 기술 없이 빅테크의 API를 활용해 외형만 포장한 국내 AI 서비스들은 냉정한 <span class=\"text-rose-400 font-medium\">거품 붕괴</span>를 피하기 어렵습니다.",
      "key_claims": [
        "대부분의 국내 AI 스타트업들은 빅테크의 완성형 AI 프로덕트와의 경쟁력에서 완전히 뒤처져 생존이 극히 어렵다.",
        "정부 재원으로 조성되어 AI 꼬리표를 달고 무분별하게 집행된 VC 투자 펀드들이 대거 손실(부도) 처리될 리스크가 매우 크다.",
        "변방의 작은 로컬 AI 서비스는 글로벌 거인들의 기술 장벽과 사용자 쏠림 현상을 극복할 실질적인 유인이 없다."
      ],
      "data_points": [
        "국내 AI 스타트업 VC 투자: 국가 세금 기반 매칭 펀드 위주 집행 (공중 분해 가능성 경고)"
      ],
      "signal": "bearish",
      "signal_confidence": "high",
      "signal_reason": "독자적인 원천 기술이나 비즈니스 장벽 없이 거대 언어 모델(LLM) API에 의존하는 로컬 AI 서비스들의 시장 퇴출이 시작되어, 관련 투자 자금의 급격한 회수 및 밸류에이션 붕괴가 불가피하기 때문입니다.",
      "key_companies": ["네이버", "카카오"],
      "insight": "모든 기술 혁신 주기마다 반복되는 '닷컴 버블'의 형태가 AI 생태계에서도 고개를 들고 있습니다. 빅테크가 장악한 AI 기본 인프라와 플랫폼 생태계 위에서 단순 래퍼(Wrapper) 역할만 하는 국내 스타트업들은 실질적인 사용자 고착(Lock-in) 효과를 내지 못합니다. 이는 세금으로 조성된 모태펀드와 VC 생태계 전반의 <span class=\"text-rose-400 font-medium\">부실화 악순환</span>으로 연결될 우려가 큽니다.",
      "action_point": "실체적인 매출과 독점 기술이 부재한 AI 스타트업에 대한 투자를 극도로 경계하고, 자체 인프라와 강력한 자본력 및 생태계를 장악한 <span class=\"text-cyan-300 font-semibold\">글로벌 빅테크 플랫폼</span> 및 확실한 반도체 파트너십을 맺은 기업으로 압축하여 대응해야 합니다."
    }
  },
  "TQSnaNSF1fI": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["삼전닉스", "이성의언어", "감정의언어", "금투세논란", "삼성SDI흑자전환", "키움증권이자수익"],
    "analysis": {
      "summary": "최근 증시는 삼성전자 자사주 취득과 SK하이닉스 ADR 나스닥 상장이라는 명확한 펀더멘탈 요인(<span class=\"text-cyan-300 font-semibold\">이성의 언어</span>)에도 불구하고, 금투세 논란 및 해외 연준 금리 인상 공포 등 노이즈로 인한 심리적 변동성(<span class=\"text-rose-400 font-medium\">감정의 언어</span>)이 극에 달해 있습니다. 시장 변동성에 휩쓸려 무분별하게 비중을 넓히기보다, 3분기 흑자전환이 예상되는 <span class=\"text-cyan-300 font-semibold\">삼성SDI</span>나 고금리 환경에서 이자수익(신용 및 예수금 낙전) 수혜를 누리는 <span class=\"text-cyan-300 font-semibold\">증권주(키움증권 등)</span>, 반도체 주도주 등으로 포트를 철저히 압축해야 할 때입니다.",
      "key_claims": [
        "주식시장은 펀더멘탈과 AI 모멘텀이 유지되는 이성의 지배 하에 있다가도, 단기 하락 국면에서는 투자자 공포와 이익 확정 욕구라는 감정이 시장을 지배하게 된다.",
        "최근 논란이 되는 금융투자소득세(금투세)는 세수가 크게 흔들리고 부동산 및 증시 전반에 미칠 부정적 파장을 고려할 때 법안 통과가 쉽지 않으며, 지나친 심리적 공포에 가깝다.",
        "고객 예탁금 130조 원 및 신용융자 잔고 급증으로 증권사들은 거래 수수료가 정체되더라도 7~9% 고금리 신용 이자 및 예수금 낙전수익(이자 혜택 미지급 자금 운용)을 통해 막대한 이자수익을 거두고 있다."
      ],
      "data_points": [
        "국내 증권사 신용공여 잔고 규모: 약 36~37조 원",
        "증권사 신용융자 이자율 범위: 평균 연 7% ~ 9% 수준 형성",
        "삼성SDI 2026년 매출 전망: 16조 원(올해) -> 내년 20조 원, 내후년 24조 원 돌파 (3분기 흑자전환 예상)",
        "주택 구입 자금 출처: 30~40대 주택 구매자 중 6%(약 4.8조 원)가 주식 투자 이익으로 자금 조달했다고 신고"
      ],
      "signal": "bullish",
      "signal_confidence": "medium",
      "signal_reason": "단기 노이즈로 변동성이 극대화되었으나 반도체 투톱의 펀더멘탈이 탄탄하고, 고금리 장기화의 직접적인 수혜를 입는 증권주 및 실적 턴어라운드를 앞둔 일부 2차전지 대형주로의 압축 투자 매력이 돋보이기 때문입니다.",
      "key_companies": ["삼성SDI(006400)", "키움증권(039490)"],
      "insight": "시장의 변동성을 활용하는 것은 철저하게 감정을 배제하는 이성적인 접근입니다. 주식 매매 대금이 늘어난 상황에서 고금리가 장기화되자, 증권사들은 수수료 경쟁에서 벗어나 <span class=\"text-amber-300 font-bold\">신용 거래 이자 및 예탁금 이자 마진</span>이라는 안정적인 수익 기틀을 강화했습니다. 이는 IT/플랫폼을 활용해 비용을 통제하고 있는 핀테크 증권사들에게 더욱 강력한 레버리지 요인으로 작용합니다.",
      "action_point": "공포에 편승한 투매를 자제하고, 3분기 실적 개선세가 뚜렷한 <span class=\"text-cyan-300 font-semibold\">삼성SDI</span>와 이자 마진 수혜를 입는 <span class=\"text-cyan-300 font-semibold\">키움증권</span> 등 확실한 어닝 모멘텀을 가진 대장주로 자산을 집중 배정해야 합니다."
    }
  },
  "UJ1ARYdPmEw": {
    "primary_topic": "economy",
    "secondary_topics": ["tech"],
    "tags": ["데이터센터반대", "님비현상", "아마존", "실리콘밸리", "인프라지연"],
    "analysis": {
      "summary": "글로벌 빅테크 기업들이 AI 지배력을 선점하기 위해 대규모 설비 투자를 진행하고 있으나, 전력망 과부하와 농업용 수자원 고갈을 우려하는 미국 현지 주민들의 <span class=\"text-rose-400 font-medium\">데이터센터 건설 반대 운동(NIMBY)</span>이 새로운 리스크로 급부상했습니다. 지난해 미국 내에서 주민 반대와 소송으로 인해 지연되거나 무산된 데이터센터 프로젝트 규모는 무려 220조 원에 달합니다. 아마존의 고향인 시애틀을 비롯해 덴버, 미네애폴리스 등 미국 대도시에서 잇따라 데이터센터 건설 중단 모라토리엄을 선언하고 있습니다.",
      "key_claims": [
        "미국 캘리포니아 농업 중심지 길로이(Gilroy)에서 아마존의 축구장 30개 크기 데이터센터 건설에 대해, 지하수 고갈 및 리튬 배터리 화재 위험을 이유로 주민들의 격렬한 반대 시위가 벌어졌다.",
        "시애틀 시의회는 아마존 소속 현직 엔지니어들조차 \"빅테크의 AI 경쟁이 지역 사회 전력과 자원을 황폐화하고 있다\"고 폭로함에 따라, 20MW 이상 데이터센터 신규 건설을 1년간 전면 중단(모라토리엄)하기로 결정했다.",
        "중국은 엔지니어적 사고로 일단 신속하게 인프라를 건설하는 반면, 미국은 변호사적 소송과 절차, 영향 평가 제도로 인해 인프라 구축 속도가 구조적으로 지체되는 병목 현상이 발생하고 있다."
      ],
      "data_points": [
        "길로이 아마존 데이터센터 부지 규모: 약 56에이커 (227만 ㎡), 건물 연면적 4만 ㎡, 전력 49MW",
        "미국 내 주민 반대로 중단/지연된 데이터센터 프로젝트 규모: 지난해 최소 1,700억 달러 (약 220조 원), 올해 1분기 기준 75건 (1,300억 달러)",
        "시애틀 모라토리엄 규제 대상: 20MW 이상 신규 데이터센터 건설 1년간 전면 금지",
        "메타(Meta) 사회적 면허 취득 투자액: 메타 인력 아카데미에 1억 1,500만 달러(약 1,600억 원) 투입해 숙련직 양성 및 데이터센터 인접 지역 일자리 보장"
      ],
      "signal": "bearish",
      "signal_confidence": "medium",
      "signal_reason": "빅테크의 초대형 AI CAPEX 예산이 확보되었음에도 불구하고, 미국 전역의 환경 소송 및 모라토리엄 조치로 실제 데이터센터가 완공되어 가동되는 시점이 최소 1~2년 늦어지는 실질적 인프라 병목 현상이 발생하고 있기 때문입니다.",
      "key_companies": ["아마존(AMZN)", "메타(META)", "마이크로소프트(MSFT)"],
      "insight": "AI 패권 전쟁의 속도전에서 빅테크의 가장 큰 복병은 기술이 아닌 지역 민심(소셜 라이선스)입니다. 데이터센터가 막대한 전력과 물을 소모하면서 정작 지역 고용 창출 효과는 미미하다는 인식이 확산됨에 따라, 모라토리엄과 소송이 들불처럼 일어나고 있습니다. 이에 대응해 <span class=\"text-cyan-300 font-semibold\">메타</span>가 1,600억 원 규모의 직업 훈련 프로그램을 데이터센터 부지 주민들에게 무상 제공하여 일자리를 보장하는 등 우회책(보험료 지불)을 쓰고 있으나, 규제 지연 비용은 인프라 밸류체인 전반의 비용 증가와 매출 실현 지연으로 연결됩니다.",
      "action_point": "데이터센터 인프라 건설 지연 리스크를 감안할 때, 단순 건설/부동산 관련 수혜주보다는 병목 현상을 우회할 수 있는 <span class=\"text-cyan-300 font-semibold\">에너지 인프라 효율화 및 전력 기기 솔루션 기업</span> 또는 냉각 기술(액침 냉각) 특화 기업으로 포트폴리오를 압축하는 것이 타당합니다."
    }
  },
  "UuI9XHOg2Hs": {
    "primary_topic": "economy",
    "secondary_topics": ["stock", "tech"],
    "tags": ["SK하이닉스ADR", "WTI유가폭락", "미국소비자물가", "바이트댄스대출", "엔화약세"],
    "analysis": {
      "summary": "글로벌 매크로 환경은 중동 및 지정학 리스크 완화로 <span class=\"text-amber-300 font-bold\">국제유가(WTI)가 3% 폭락</span>하여 71달러 선으로 내려앉으면서, 물가 상승 및 긴축 우려가 다소 완화되었습니다. 그러나 원·달러 환율이 1,540원대, 엔화는 161엔을 돌파하는 등 달러 강세 압박이 아시아 외환 시장을 뒤흔들고 있습니다. 기업 단에서는 SK하이닉스가 45조 원대 ADR 발행을 통한 나스닥 상장을 가시화했으며, 중국 <span class=\"text-cyan-300 font-semibold\">바이트댄스</span>는 AI 데이터센터 확장을 위해 사상 최대 규모의 해외 대출을 추진하고 있습니다.",
      "key_claims": [
        "호르무즈 해협 통행 우려 완화 및 이란 선박 운송 안정화로 유가와 정제 유가가 급락해 원자재발 인플레이션 공포가 진정되었다.",
        "틱톡의 모기업 바이트댄스는 AI 기술 격차를 좁히기 위해 역대 최대 규모인 108억 달러의 해외 신디케이트 대출을 받아 GPU 및 AI 인프라 구축에 올인하고 있다.",
        "BofA가 연내 3회 금리 인상 가능성으로 예측을 뒤집었으나, 패드워치 상으로는 연내 1회(39.1%) 혹은 2회(31.8%) 인상 등 다양한 컨센서스가 엇갈리고 있다."
      ],
      "data_points": [
        "WTI 유가: 3% 급락한 71달러 선 기록",
        "브렌트유: 3% 이상 하락한 74.6달러 기록",
        "엔·달러 환율: 달러당 161.75엔 돌파 (162엔대 테스트 전망)",
        "바이트댄스 해외 신디케이트 대출 조달 규모: 108억 달러 (중국 비금융 기업 사상 최대)",
        "금 가격 하루 변동률: 3% 넘게 하락하며 4,000달러 선 위태",
        "은 가격 변동률: 5.6% 급락하며 58달러 기록"
      ],
      "signal": "neutral",
      "signal_confidence": "medium",
      "signal_reason": "유가 폭락은 원자재 인플레이션 압력을 낮춰 증시에 긍정적이지만, 연준의 추가 금리 인상 망령이 여전히 시장에 남아 있고 급격한 원화 및 엔화 약세(달러화 초강세)가 외국인 수급의 일시적 이탈을 야기할 수 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "바이트댄스"],
      "insight": "유가 하락과 달러화 강세가 동시에 일어나는 독특한 매크로 터널을 지나고 있습니다. 중국 <span class=\"text-cyan-300 font-semibold\">바이트댄스</span>가 창사 이래 최대인 14조 원 규모 해외 펀딩을 감행하는 것은 지정학적 AI 반도체 공급 차단 장벽을 넘어서기 위한 막대한 자금력 확보 전쟁을 의미합니다. 동시에 국내 가상자산 규제 강화 및 이더리움 재단 예산 40% 감축은 가상자산 시장 전반의 일시적 신뢰 하락과 수급 위축 요인으로 남을 것입니다.",
      "action_point": "고환율로 인한 환차익 수혜가 예상되는 수출 주도 대형 기술주(<span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>) 중심의 포트폴리오 비중을 유지하고, 금/은 등 귀금속 및 원자재 레버리지 파생 상품은 변동성 확대로 리스크가 크므로 단기 접근을 피해야 합니다."
    }
  },
  "V9l0FaDexLw": {
    "primary_topic": "stock",
    "secondary_topics": ["tech", "economy"],
    "tags": ["SK하이닉스ADR", "나스닥상장", "지방클러스터", "용인반도체", "자사주매입"],
    "analysis": {
      "summary": "SK하이닉스가 최대 45.5조 원 규모의 미국 ADR(주식예탁증서)을 신규 발행하여 7월 10일 미국 나스닥 시장에 직상장합니다. 조달된 대규모 투자금은 전액 용인 클러스터와 청주 패키징 공장의 시설 자금으로 사용될 예정이며, 주주 가치 희석을 방어하기 위해 대규모 <span class=\"text-amber-300 font-bold\">주주 환원 및 자사주 소각</span>을 병행할 것으로 예상됩니다. 한편, 논란이 되었던 지방 반도체 클러스터 분산 이전안은 용인 원안 유지를 골자로 마무리 단계에 들어섰습니다.",
      "key_claims": [
        "SK하이닉스는 1,779만 주의 대규모 신주 발행을 동반한 나스닥 상장을 진행하며, 미국 현지 패시브 펀드 자금의 직접 유입을 통해 글로벌 기업 가치를 제고한다.",
        "증자 규모가 45.5조 원에 달해 발생할 수 있는 주당 가치 희석 악재는 상장 직후 발표될 강력한 주주환원(소각 등) 및 압도적인 시설 투자 성과로 충분히 상쇄 가능하다.",
        "야당의 반도체 클러스터 지방 분산 압박(법안 발의 등)에 대해, 정부는 기업의 투자 효율성과 용인 부지 확보 완성도를 감안하여 기존 용인 클러스터 안을 그대로 유지하기로 잠정 결론지었다."
      ],
      "data_points": [
        "SK하이닉스 ADR 발행 신주 수량: 17,794,355 주",
        "예상 발행가액: 주당 2,555,500 원 (달러화 환산 발행)",
        "총 조달 목표 자금: 45조 4,725억 원 규모",
        "ADR 나스닥 상장 및 거래 개시일: 7월 10일",
        "국내 시장 신주 예탁 및 상장일: 7월 29일"
      ],
      "signal": "bullish",
      "signal_confidence": "high",
      "signal_reason": "유상증자의 성격이 주주가치 훼손형 채무 상환이 아닌 글로벌 자본을 유치한 초대형 인프라 시설 투자(EUV 장비 및 패키징 공장)용이며, 미국 증시 직상장으로 하이닉스의 밸류에이션 상단이 마이크론 수준으로 높아지는 계기가 되기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "SK하이닉스의 미국 상장은 코리아 디스카운트라는 제도적 족쇄를 스스로 푸는 중대한 결단입니다. 유상증자 타이틀로 단기적인 개인들의 투매가 발생할 수 있으나, 미국 시장의 풍부한 테크 패시브 유동성을 확보하여 글로벌 경쟁자인 <span class=\"text-cyan-300 font-semibold\">마이크론</span>과의 밸류에이션 갭을 축소하려는 전략입니다. 클러스터 분산 이전에 대한 정치적 노이즈가 제거되고 용인 허브 구축이 확정된 것 또한 투자 확실성을 대폭 높였습니다.",
      "action_point": "단기 유증 공시 충격으로 발생할 수 있는 주가 조정을 적극적인 비중 확대(추가 매수) 기회로 활용하고, 7월 10일 나스닥 상장 전후로 미국 ETF 편입 수급 동향을 철저히 추적해야 합니다."
    }
  }
}

for vid, data in batch_3.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 3 completed!")
