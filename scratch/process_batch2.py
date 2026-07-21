import json
from pathlib import Path

# Define the analyzed data for Batch 2
batch_data = {
  "E4GVkK6GLcU": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "E4GVkK6GLcU",
        "title": "좋은 종목을 사도 빚투하면 망합니다ㅣ차영주 와이즈경제연구소 소장 [집중 오늘의 주식]",
        "published": "2026-06-10T11:30:15+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=E4GVkK6GLcU",
        "thumbnail": "https://img.youtube.com/vi/E4GVkK6GLcU/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 최근 국내 증시는 극단적인 심리 쏠림으로 매수·매도 사이드카가 번갈아 작동하는 등 <span class=\"text-rose-400 font-medium\">극심한 변동성 장세</span>를 연출하고 있습니다.\n2. 현재 조정 폭은 약 16% 수준으로 과거 3월 조정(20%) 대비 평이하며, 올해 상장사 영업이익 전망치(800조 원 이상)를 감안할 때 코스피 10,000선 상승 관점은 유효합니다.\n3. 시장 변동성에 대응하기 위해서는 신용 거래 및 미수 매매 등 레버리지를 축소하고, 반도체 등 확실한 <span class=\"text-cyan-300 font-semibold\">실적 기반 주도주</span>로 포트폴리오를 압축해야 합니다.",
        "key_claims": [
          "외국인의 반도체(SK하이닉스 등) 비중 소폭 축소는 이익 전망 변화가 아닌 <span class=\"text-amber-300 font-bold\">단기 포트폴리오 리밸런싱 및 현금 확보</span> 차원입니다.",
          "미수 거래와 같은 레버리지 투자는 성공 확률이 30% 미만인 <span class=\"text-rose-400 font-medium\">단순 배팅</span>에 불과하므로 극단적 변동성 장세에서 반드시 배제해야 합니다.",
          "비주도주(코스닥 및 2차전지 등)는 영업이익 성장세 대비 지수가 선반영되어 있어 당분간 주도주(반도체)와의 <span class=\"text-rose-400 font-medium\">수급 양극화</span>가 지속될 것입니다."
        ],
        "data_points": [
          "올해 6월 코스피 최고점 8,933포인트, 최저점 7,440포인트 (고점 대비 약 16% 조정)",
          "지난 3월 지정학 조정기 코스피 6,347에서 5,059포인트까지 하락 (약 20% 조정)",
          "올해 국내 상장사 총 영업이익 전망치: 약 800조 원 이상 (전년 약 450조 원 대비 급증)",
          "비주도주 영업이익 총합: 전년 250조 원에서 올해 280조 원 수준으로 약 15% 증가 전망"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "상장사 이익 성장이 훼손되지 않은 상황에서 발생하는 단기 수급 조정이므로, 레버리지를 정리하고 실적 우량주를 모아가기에 최적의 기회입니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)",
          "두산로보틱스(454910)",
          "LG전자(066570)"
        ],
        "insight": "반도체를 제외한 비주도주 섹터는 실적 성장 대비 지수가 과도하게 올라있어 매수 매력도가 떨어집니다. 반면 삼성전자와 SK하이닉스는 강력한 이익 모멘텀을 보유하고 있어 <span class=\"text-cyan-300 font-semibold\">하방 경직성</span>이 뚜렷하며, 조정 완료 후 시장 재상승을 주도할 것입니다.",
        "action_point": "미수 및 신용 거래 비중을 신속히 축소하여 <span class=\"text-rose-400 font-medium\">반대매매 리스크</span>에 대응하고, 하이닉스 200만 원 이하 및 삼성전자 30만 원 이하 등 주요 가격대에서 분할 매수로 대응하는 전략이 유리합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.7
      }
    }
  },
  "ejHArVAYc70": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "ejHArVAYc70",
        "title": "[김종학의 뉴욕, 지금-6월11일] 미 소비자물가지수, 3년 만에 최고 | 오라클, 아마존, TSMC, 슈퍼마이크로, 세레브라스, 스페이스X, 크래커배럴, 데번에너",
        "published": "2026-06-10T21:19:50+00:00",
        "channel_name": "한경 글로벌마켓",
        "url": "https://www.youtube.com/watch?v=ejHArVAYc70",
        "thumbnail": "https://img.youtube.com/vi/ejHArVAYc70/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 뉴욕 증시는 다우 1.87%, 나스닥 1.98% 하락하며 기술주 위주의 급격한 차익 실현과 <span class=\"text-rose-400 font-medium\">스페이스X IPO 수급 분산 우려</span>로 한 달간의 상승분을 반납했습니다.\n2. 5월 미국 CPI는 에너지 상승으로 전년 대비 4.2% 올라 3년 만에 최고를 기록했으나, 변동성이 큰 에너지를 제외한 코어 CPI는 전월 대비 0.2%로 안도감을 주었습니다.\n3. 오라클, TSMC는 양호한 실적을 발표했으나, 슈퍼마이크로컴퓨터(SMCI)의 70억 달러 자금 조달 발표 및 오라클의 유상증자 우려로 주가가 폭락하며 투자 심리가 악화되었습니다.",
        "key_claims": [
          "이란 보복 공격 등으로 인한 <span class=\"text-amber-300 font-bold\">유가 상승세</span>가 미 CPI 헤드라인을 자극했으나, 속을 들여다보면 실질 구매력 저하에 따른 소비 둔화 조짐이 뚜렷합니다.",
          "미국 연준(FOMC) 회의를 앞두고 연말 금리 인상론이 대두되는 등 <span class=\"text-rose-400 font-medium\">통화 긴축 우려</span>가 재점화되고 있습니다.",
          "슈퍼마이크로(SMCI)와 오라클의 대규모 자금 조달(증자) 계획은 빅테크의 AI 설비투자 비용 부담과 <span class=\"text-rose-400 font-medium\">기존 주주가치 희석 우려</span>를 키우고 있습니다."
        ],
        "data_points": [
          "다우지수 1.87% 하락(49,918.78), 나스닥 1.98% 하락(25,169.05)",
          "5월 미국 소비자물가지수(CPI) 전년 대비 4.2% 상승 (3년 만에 최고치)",
          "근원 소비자물가지수(Core CPI) 전월 대비 0.2% 상승, 전년 대비 2.9% 상승",
          "WTI 국제 유가 3.47% 상승한 배럴당 91.26달러 기록",
          "실질 임금 상승률 물가 상승분(4.2%) 대비 낮은 3.4% 증가로 실질 소득 감소세",
          "오라클 Q4 매출 191억 8,000만 달러 기록 (클라우드 인프라 57억 9,000만 달러)",
          "슈퍼마이크로컴퓨터(SMCI) 주가 27.9% 폭락 (70억 달러 유상증자 및 자금 조달 우려)",
          "TSMC 월 매출 약 20조 6,000억 원 기록 (전년 대비 30% 증가)"
        ],
        "signal": "bearish",
        "signal_confidence": "medium",
        "signal_reason": "주요 기업들의 대규모 자금 조달에 따른 지분 희석 우려와 유가 불안에 따른 긴축 경계감이 작용해 기술주 전반에 강력한 매도 압력을 가하고 있습니다.",
        "key_companies": [
          "슈퍼마이크로컴퓨터(SMCI)",
          "오라클(ORCL)",
          "TSMC(TSM)",
          "아마존(AMZN)",
          "엔비디아(NVDA)"
        ],
        "insight": "최근 기술주 조정의 이면에는 기업들의 AI 인프라 투자(CapEx) 확대에 따른 <span class=\"text-rose-400 font-medium\">자본 희석(유상증자) 리스크</span>와 스페이스X 초대형 IPO 청약을 위한 기관들의 반도체 현금화 압박이 존재합니다. 이는 단순한 펀더멘탈의 훼손보다 단기 수급 교란에 가깝습니다.",
        "action_point": "유상증자 공시로 낙폭이 과도한 반도체 기기주(SMCI 등)는 당분간 보수적으로 관망하되, 실적 성장이 견고한 <span class=\"text-cyan-300 font-semibold\">대형 기술주 및 파운드리 대장주(TSMC)</span>의 차익 매물 소화 과정을 분할 매수 기회로 포착해야 합니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.5
      }
    }
  },
  "elRrWiXSYUs": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "elRrWiXSYUs",
        "title": "\"금리 인하는 없다?\" 미 국채 금리 어디까지 올라가나 #교양이를부탁해",
        "published": "2026-06-10T10:45:07+00:00",
        "channel_name": "교양이를 부탁해",
        "url": "https://www.youtube.com/watch?v=elRrWiXSYUs",
        "thumbnail": "https://img.youtube.com/vi/elRrWiXSYUs/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 미국 국채 10년물 금리의 기본 시나리오는 연준의 <span class=\"text-amber-300 font-bold\">하이어 런거(Higher for Longer)</span> 기조 강화에 따라 최고 4.9% 수준까지 상승할 전망입니다.\n2. 정부 재정 적자 확대와 매크로 환경의 불확실성이 지속되면서 장기물 국채 금리에 추가적으로 최소 50bp 수준의 상승 압력이 유효합니다.\n3. 연준이 단순 동결을 넘어 추가 긴축 신호를 보낼 경우 금리가 5.0% 이상으로 치솟아 트럼프 정부와의 심각한 갈등 구도가 형성될 수 있습니다.",
        "key_claims": [
          "새로운 연준 의장 체제 출범 이후 연말 및 내년 상반기까지 금리 인하는 차단되고 <span class=\"text-rose-400 font-medium\">고금리 장기화</span>가 고착화될 것입니다.",
          "미 국채 10년물 금리는 현재 4.4% 선에서 대내외적 재정 여건 악화로 추가 상승할 수 있는 <span class=\"text-rose-400 font-medium\">상방 위험</span>이 열려 있습니다.",
          "금리가 5% 선을 돌파해 시장 스트레스 환경이 극대화되는 시나리오는 연준과 트럼프 행정부 간의 정치적 대립을 심화시킬 리스크 요인입니다."
        ],
        "data_points": [
          "미국 10년물 국채 금리 현재 약 4.4% 수준",
          "기본 시나리오 하의 10년물 국채 금리 고점 전망치: 4.9% (약 50bp 추가 상승 여력)",
          "극단적 시나리오 기준 국채 금리 상방 가이드: 5.0% 이상"
        ],
        "signal": "bearish",
        "signal_confidence": "high",
        "signal_reason": "미국 국채 금리의 지속적인 상방 압력 및 연준의 고금리 장기화 기조는 자산 시장 전반의 밸류에이션을 압박하고 기술 성장주의 하방 압력을 가중시킵니다.",
        "key_companies": [],
        "insight": "미국 국채 금리 상승은 매크로 재정 적자와 연준의 긴축 의지가 결합한 결과입니다. 10년물 4.9% 시나리오는 시장에 지속적인 <span class=\"text-rose-400 font-medium\">이자 비용 부담 및 할인율 상승 리스크</span>로 작용해 지수의 상단을 제한할 것입니다.",
        "action_point": "미국 국채 10년물 금리가 4.8~4.9% 저항선에 다다를 때 기술 성장주에 대한 리스크 관리를 철저히 하고, 포트폴리오 내 <span class=\"text-cyan-300 font-semibold\">고배당주 및 현금 창출력이 뛰어난 가치주</span> 비중을 늘려 금리 변동성에 대비해야 합니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.0
      }
    }
  },
  "eq_XgSdFJ1Y": {
    "topic": "space",
    "content": {
      "video": {
        "id": "eq_XgSdFJ1Y",
        "title": "영화 ’빅쇼트' 아이스먼 “스페이스X 살 이유도, 숏 칠 이유도 없다” #shorts",
        "published": "2026-06-10T10:11:53+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=eq_XgSdFJ1Y",
        "thumbnail": "https://img.youtube.com/vi/eq_XgSdFJ1Y/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 영화 '빅쇼트'의 실제 모델인 아이스먼은 <span class=\"text-cyan-300 font-semibold\">스페이스X(SpaceX)</span>의 자본 집약도 급증(1분기 매출 대비 CapEx 215%)과 높은 밸류에이션에 대해 회의적인 시각을 드러냈습니다.\n2. 일론 머스크의 AI 기업(Grok)은 세계적 수준으로 보기 어려우며, 스페이스X가 미래 가치의 85%를 AI에 걸고 있어 공상 과학 소설 같은 과평가 영역에 있다고 평가했습니다.\n3. 다만 머스크 관련 기업에 공매도(숏)를 쳤던 투자자들이 과거에 큰 손해를 입은 사례가 많아 공매도는 실행하지 않고 관망하겠다고 밝혔습니다.",
        "key_claims": [
          "스페이스X는 스타링크/우주 인프라를 넘어 AI를 기업의 핵심 TAM(28.5조 달러)으로 제시하고 있으나 이는 <span class=\"text-rose-400 font-medium\">과도하게 부풀려진 기대감</span>입니다.",
          "테슬라의 영업이익이 지난 4년간 감소했고 전기차 경쟁이 심화되는 등 일론 머스크 관련 자산의 <span class=\"text-rose-400 font-medium\">기초 펀더멘탈 약화</span> 우려가 존재합니다.",
          "스페이스X의 평가 가치는 매우 터무니없으나, 수급과 일론 머스크 프리미엄으로 인해 <span class=\"text-rose-400 font-medium\">공매도는 극도로 위험</span>하므로 배제해야 합니다."
        ],
        "data_points": [
          "스페이스X 2023 회계연도 매출 대비 자본 지출(CapEx) 비중: 42%",
          "스페이스X 2026년 1분기 매출 대비 자본 지출(CapEx) 비중: 215%로 급증",
          "스페이스X가 정의하는 총 잠재 시장 규모(TAM): 28조 5,000억 달러 (이 중 85%가 AI 영역)",
          "테슬라의 영업이익 4년 연속 감소 추세"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "밸류에이션 과열 우려와 일론 머스크에 숏을 치는 것의 과거 위험성이 상존하여 시장 참여자들이 매수와 매도 어느 쪽도 쉽게 베팅하기 어려운 중립 영역입니다.",
        "key_companies": [
          "스페이스X",
          "테슬라(TSLA)"
        ],
        "insight": "스페이스X의 미래 가치 산정이 AI와 스타링크의 비현실적 성장 시나리오에 기반해 있다는 경고입니다. 특히 매출의 두 배가 넘는 자본 투입(CapEx)은 자금 조달 리스크를 키울 수 있으나, <span class=\"text-cyan-300 font-semibold\">독점적 수급 효과</span>와 탄탄한 기관 대기 매수세 때문에 상장 직후의 주가는 밸류에이션과 별개로 움직일 가능성이 큽니다.",
        "action_point": "스페이스X 상장 초기 밸류에이션 과열 구간에서는 추격 매수를 자제하되, 시장의 높은 변동성을 이용한 단기 공매도 역시 지양하며 장기적인 <span class=\"text-cyan-300 font-semibold\">자본 효율성 및 AI 실적 증명</span> 과정을 지켜보아야 합니다."
      },
      "classification": {
        "primary_topic": "space",
        "relevance_score": 8.8
      }
    }
  },
  "gDf8_uX3koQ": {
    "topic": "tech",
    "content": {
      "video": {
        "id": "gDf8_uX3koQ",
        "title": "한중일 모두 제쳐버린 대만 근황",
        "published": "2026-06-10T11:00:16+00:00",
        "channel_name": "Softdragon SOD",
        "url": "https://www.youtube.com/watch?v=gDf8_uX3koQ",
        "thumbnail": "https://img.youtube.com/vi/gDf8_uX3koQ/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 대만의 1인당 GDP가 약 42,100달러를 돌파하며 한국과 일본을 제치고 동아시아 최고 수준으로 도약했습니다.\n2. 대만 관광객들의 한국 내 카드 결제액이 일본과 중국 관광객의 두 배 수준에 달해 국내 유통·관광 업계의 큰손으로 부상했습니다.\n3. 이러한 대만의 성장은 <span class=\"text-cyan-300 font-semibold\">TSMC, 폭스콘, 미디어텍</span> 등 글로벌 AI 반도체 공급망의 핵심 제조 허브를 독점 장악한 덕분입니다.",
        "key_claims": [
          "글로벌 AI 및 반도체 호황에 힘입어 대만 제조업과 국민 소득이 <span class=\"text-amber-300 font-bold\">동아시아 내 최상위권</span>으로 고성장하고 있습니다.",
          "대만 내 반도체 관련 낙수 효과로 가계 소득이 급증하면서 해외 소비(한국 등) 규모도 <span class=\"text-amber-300 font-bold\">폭발적인 증가세</span>를 보이고 있습니다.",
          "TSMC를 필두로 한 대만의 반도체 생태계 시가총액은 이미 한국 대표 기술주들의 시총 총합을 능가하는 경쟁력을 갖췄습니다."
        ],
        "data_points": [
          "대만 1인당 GDP: 약 42,100달러 돌파 (한국 및 일본 추월)",
          "한국 내 대만 관광객 카드 결제액 규모: 일본 및 중국 관광객 결제액 대비 약 2배 수준 기록"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "글로벌 AI 반도체 생산 독점 체제에 기반한 대만의 GDP 성장은 반도체 공급망 전반의 장기 호황과 수혜 강도가 극단적으로 강력함을 방증합니다.",
        "key_companies": [
          "TSMC(TSM)",
          "폭스콘(Foxconn)",
          "미디어텍"
        ],
        "insight": "반도체 제조 기술력을 독점한 국가의 국부 성장세를 단적으로 보여줍니다. TSMC와 미디어텍 등 <span class=\"text-cyan-300 font-semibold\">대만 반도체 삼각 동맹</span>의 성장 에너지는 AI 사이클의 지속성을 나타내는 가장 강력한 지표입니다.",
        "action_point": "대만 반도체 공급망에 장비를 납품하거나 함께 패키징 협력을 수행하는 <span class=\"text-cyan-300 font-semibold\">국내 소부장(소재·부품·장비) 반도체 대장주</span>에 대한 비중 확대를 우선적으로 고려해야 합니다."
      },
      "classification": {
        "primary_topic": "tech",
        "relevance_score": 9.4
      }
    }
  }
}

# Write results and clean up pending
pending_dir = Path("data/pending")
analyzed_base_dir = Path("data/analyzed")

for video_id, info in batch_data.items():
    topic = info["topic"]
    content = info["content"]
    
    # Write to analyzed path
    topic_dir = analyzed_base_dir / topic
    topic_dir.mkdir(parents=True, exist_ok=True)
    analyzed_path = topic_dir / f"{video_id}.json"
    analyzed_path.write_text(json.dumps(content, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved: {analyzed_path}")
    
    # Delete from pending
    pending_path = pending_dir / f"{video_id}.json"
    if pending_path.exists():
        pending_path.unlink()
        print(f"Deleted pending: {pending_path}")
