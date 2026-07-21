import json
from pathlib import Path

batch7_data = {
  "28GFiZhKECI": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "28GFiZhKECI",
        "title": "정치가 망친 부동산 서울 아파트 씨 말랐다 (‘재테크 불변의 법칙’ 저자 아기곰 작가)",
        "published": "2026-06-16T12:25:04+00:00",
        "channel_name": "언더스탠딩_Understanding",
        "url": "https://www.youtube.com/watch?v=28GFiZhKECI",
        "thumbnail": "https://img.youtube.com/vi/28GFiZhKECI/hqdefault.jpg"
      },
      "analysis": {
        "summary": "서울 내 신축 아파트 부족은 2015년 이후 지속된 서울시의 <span class=\"text-rose-400 font-medium\">재개발·재건축 제한 규제</span> 때문이며, 택지가 고갈된 서울의 유일한 주택 공급 수단은 결국 재건축·재개발뿐임. 외곽 신도시 개발은 직주근접을 해쳐 GTX 등 교통 인프라 부설에 따른 <span class=\"text-amber-300 font-bold\">사회적 비용만 가중</span>시키므로 도심 내 용적률을 300~500% 이상으로 대폭 상향하는 고밀도 개발이 요구됨. 다만 규제 완화 시 발생하는 이주 및 멸실 과정에서의 단기 전월세난과 집값 상승(3~5년)은 장기 안정을 위해 감내해야 할 필수적 과정임.",
        "key_claims": [
          "서울 및 수도권 핵심지에 신축 아파트를 공급하려면 도심 내 재건축·재개발의 사업성을 보장하고 용적률을 300~500% 이상으로 풀어주는 고밀 개발이 필수적임.",
          "수도권 외곽의 신도시 건설은 직장과의 거리가 멀어져 도로 및 교통망 확충에 대규모 사회적 비용을 소모하는 비효율적 공급 방식임.",
          "재건축 초과이익 환수제, 분양가 상한제 등 과도한 기부채납 요건이 중층 아파트(기존 용적률 200%)의 사업성을 악화시켜 민간 공급을 마비시킴."
        ],
        "data_points": [
          "서울 아파트 기존 용적률 수준: 저층 개포동 5층(용적률 약 100%) -> 현재 35층(용적률 300% 수준)으로 공급 확대 사례",
          "중층 음마 아파트 기획안 용적률 수준: 기존 200% -> 신속통합기획 적용 시 330% 수령 (그러나 추가 분담금 가구당 3억~4억 원 수준 발생)"
        ],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "서울 도심 공급 규제 완화 기조는 긍정적이나, <span class=\"text-rose-400 font-medium\">단기 이주 멸실에 따른 전월세 상승 리스크</span>와 공사비 인상으로 인한 정비사업 착공 지연이 공존하기 때문임.",
        "key_companies": [],
        "insight": "정치적 규제가 시장 원리(도심 고밀 개발 수요)를 억누를 때 자산 디스카운트와 인위적 공급난이 동반됨. 재개발 규제를 완화하면 착공 전까지 5년간 가격 불안정을 유발하나 이를 두려워해 막아두는 것은 결국 미래 서울 아파트 가치(안전 자산 파킹 수요)를 폭등시키는 영구적 원인이 됨.",
        "action_point": "단기적인 갭 투자 포모에 휩쓸려 무리한 부채를 일으키기보다, 서울 핵심 입지의 재건축 사업성이 보장된 정비사업 추진 단지 및 <span class=\"text-cyan-300 font-semibold\">대형 건설 우량주</span>를 장기적 관점에서 저점 분할 매수하는 전략이 안전함."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock", "etc"],
        "tags": ["서울아파트공급", "재개발재건축", "용적률완화", "부동산정책"]
      }
    }
  },
  "hI1AFp1TJDo": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "hI1AFp1TJDo",
        "title": "[6월 16일 마감시황] 구천피보다 중요한 변화 시작! '시장의 착각' 세 가지. '도파민 장세'는 끝났다?ㅣ홍선애, 이권희, 김장열 [클로징벨 라이브]",
        "published": "2026-06-16T09:30:42+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=hI1AFp1TJDo",
        "thumbnail": "https://img.youtube.com/vi/hI1AFp1TJDo/hqdefault.jpg"
      },
      "analysis": {
        "summary": "코스피가 외국인과 기관의 1.3조 원 순매수에 힘입어 2% 상승한 8,718선으로 마감했으나 코스닥은 1.4% 급락해 양극화가 이어짐. 특히 <span class=\"text-cyan-300 font-semibold\">LIG넥스원</span>이 독일 방산 공룡인 <span class=\"text-cyan-300 font-semibold\">라인메탈(Rheinmetall)</span>과 차세대 미사일 나토 시장 진출 합작 법인 설립을 전격 발표하며 방산 섹터의 급등을 주도함. 한편 AI 데이터센터 내 MLCC 탑재 비중이 30%를 넘어서면서 <span class=\"text-cyan-300 font-semibold\">삼성전기</span>의 패키지 솔루션 가치가 부각됨.",
        "key_claims": [
          "외국인 자금이 현선물 시장에서 3거래일 연속 대규모 매수세를 보이며 국내 증시의 든든한 버팀목 역할을 수행함.",
          "독일 라인메탈과의 합작 소식은 LIG넥스원이 개별 기업 한계를 딛고 나토 표준 무기 체계에 진입하는 강력한 수출 이정표가 됨.",
          "미-이란 평화 합의 타결로 방산 수주 계약이 축소될 것이라는 시장의 우려가 악재 소멸로 현실 확인되면서 숏커버링 자금이 대거 재유입됨."
        ],
        "data_points": [
          "코스피 마감 지수 및 외국인 순매수 규모: 8,718선 마감 (외국인 약 1.3조 원 현물 순매수)",
          "최근 기관 방산 섹터 매도 규모 및 턴어라운드: 한화에어로스페이스 노이즈로 인한 동반 매도 이후 LIG넥스원 호재로 외국인 매수 3달 연속 누적 확인"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "외국인의 강력한 대형주 직접 순매수 유입과 함께 <span class=\"text-cyan-300 font-semibold\">나토 시장용 LIG넥스원-라인메탈 합작 법인</span>이라는 독점적 수출 호재가 방산과 기계 부문의 밸류에이션을 견고하게 올리고 있기 때문임.",
        "key_companies": ["LIG넥스원(079550)", "삼성전기(009150)", "한화오션(042660)", "HD현대중공업(329180)"],
        "insight": "지정학 리스크 해소 국면에서 방산이 하락할 것이라는 통념은 잘못되었으며, 평화 합의 이후 각국의 국방력 재정비(외양간 고치기)와 나토 인프라 재건 국방비 집행으로 방산 기계 수요는 더욱 지속 가능해짐. 특히 KDDX 수주에 성공한 한화오션과 유럽 방산 공급망을 잡은 LIG넥스원은 단순 테마가 아닌 실질 매출 구조가 뒷받침됨.",
        "action_point": "방산/조선 밸류체인 내 탑픽인 <span class=\"text-cyan-300 font-semibold\">LIG넥스원</span>과 <span class=\"text-cyan-300 font-semibold\">한화오션</span>의 주도주 비중을 유지하고, MLCC 세트 판매 단가 상승이 시작된 삼성전기는 목표가 단기 조정 시 분할 매수로 대응하는 장기 레이더가 필요함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["LIG넥스원합작", "라인메탈유럽진출", "삼성전기MLCC", "방산주숏커버링"]
      }
    }
  },
  "E8BMnRLZWsQ": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "E8BMnRLZWsQ",
        "title": "복지천국 버린 스웨덴 70% 상속세도 없앴다 ('부자 미국 가난한 유럽' 저자 손진석 기자)",
        "published": "2026-06-16T07:55:37+00:00",
        "channel_name": "언더스탠딩_Understanding",
        "url": "https://www.youtube.com/watch?v=E8BMnRLZWsQ",
        "thumbnail": "https://img.youtube.com/vi/E8BMnRLZWsQ/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1990년대 초 극심한 재정 적자 위기를 겪은 스웨덴은 지난 30년간 강도 높은 복지 구조조정과 친시장적 개혁을 추진하며 복지 천국에서 <span class=\"text-cyan-300 font-semibold\">미국식 실용적 자본주의 체제</span>로 변모함. 2004~2005년에 걸쳐 상속세와 증여세를 완전히 폐지하고, 전력, 발전, 교육, 요양 등 상당수 공공 영역을 민영화하여 재정 건전성을 비약적으로 올림. 그 결과 인구 대비 억만장자 비율이 미국을 추월할 만큼 부자들의 금융 천국으로 안착함.",
        "key_claims": [
          "스웨덴은 GDP 대비 사회복지 지출 비율을 과거 70% 수준에서 현재 프랑스(57%)보다 현저히 낮은 49% 수준(독일 수준)으로 낮춰 허리띠를 졸라맴.",
          "상속세 및 증여세를 과감히 철폐하고 부유세를 없애 해외로 이탈하던 스웨덴 내 자본가(이케아 등) 및 부유층 자산을 스웨덴 내부로 성공적으로 유입시킴.",
          "교육, 요양 시스템에 민간 주도 경쟁 모델을 도입하고 공공부채 이자 지급 비율을 기존 11%에서 0.7% 수준으로 축소하여 완벽한 재정 건전화를 완수함."
        ],
        "data_points": [
          "스웨덴 인구 수 및 억만장자 수: 인구 약 1,000만 명 (인구 5,000만 명인 한국과 억만장자 수 31명으로 동일해 인구비율상 5배 수준)",
          "스웨덴 공공부채 이자 지급 비율 추이: 과거 국가 위기 시절 GDP 대비 10.9% -> 현재 0.7% 수준으로 급감",
          "연금 소득 대체율 수준: 최대 65% 수준으로 EU 평균보다 낮으며 OECD 평균 수준에 머무름"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "전통적인 높은 복지 지출의 덫에서 탈피해 <span class=\"text-cyan-300 font-semibold\">감세(상속세 폐지) 및 민영화</span>를 바탕으로 재정의 우량 체력을 키웠고, 그 결과 글로벌 자본이 매력적으로 안착하는 초우량 자본주의 경제 구조를 마련했기 때문임.",
        "key_companies": [],
        "insight": "스웨덴의 사례는 높은 상속세와 복지 지출이 무조건 복지 국가의 선을 의미하는 것이 아니며, 오히려 재정 위기를 불렀던 주범이었음을 가리킴. 상속세를 없애 국내 기업 대물림을 돕고 자본의 국외 유출을 막는 정책 개혁이 장기적으로 국부를 보존하고 억만장자 활성화를 이끄는 생산적 경로임을 실증하고 있음.",
        "action_point": "스웨덴의 감세 체질 개선 흐름은 한국의 상속세 인하 및 주주환원 분리과세 등 밸류업 세제 개편의 모범 사례로 다뤄질 것이므로, 상속세 인하 혜택을 크게 받을 <span class=\"text-cyan-300 font-semibold\">저PBR 자산 가치주 및 지주사 우량주</span> 비중을 포트폴리오 내에 우호적으로 확보해두는 전략이 적절함."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock", "etc"],
        "tags": ["스웨덴세제개혁", "상속세폐지", "민영화개혁", "재정건전화"]
      }
    }
  },
  "8p3Jw-GI1UY": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "8p3Jw-GI1UY",
        "title": "[26.06.16 오후 방송 전체보기] 하이닉스의 힘? SK 그룹주 시총 2천 조 돌파! 증시 주도권은 여전히 '삼전닉스'...고환율 정상화는 언제쯤? [클로징벨 라이브]",
        "published": "2026-06-16T11:00:49+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=8p3Jw-GI1UY",
        "thumbnail": "https://img.youtube.com/vi/8p3Jw-GI1UY/hqdefault.jpg"
      },
      "analysis": {
        "summary": "<span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>의 급등 및 지주사 SK의 동반 상승으로 SK그룹 합산 시가총액이 역사적인 <span class=\"text-cyan-300 font-semibold\">2,000조 원</span>을 돌파하며 국내 증시의 26%를 점유함. SK하이닉스의 미국 나스닥 ADR 상장(40조 원 조달)에 대한 글로벌 롱 펀드(홍콩 자금 등)의 강력한 기대감이 작용함. 또한 회사 측은 부인했으나 FCF 50% 배분 기준상 100조 원대 자사주 매입/주주환원은 재무적으로 달성 가능한 시나리오로 부각됨.",
        "key_claims": [
          "SK그룹 시가총액이 2,000조 원을 돌파하며 코스피 내 비중을 크게 올려, 타 대기업 그룹 대비 강력한 수급 쏠림을 발생시킴.",
          "미국 나스닥 ADR 상장을 통해 지분 2.5%를 예탁 발행하여 40조 원의 인프라 투자 실탄을 마련하고 마이크론 대비 디스카운트를 해소할 예정임.",
          "삼성전자가 퀄컴 파운드리 수주 실패 및 HBM 단기 물량 선점 지연 루머를 겪는 동안 SK하이닉스는 ADR 모멘텀과 HBM 독점력을 공고히 다짐."
        ],
        "data_points": [
          "SK그룹 합산 시가총액: 역사적 2,019조 원 돌파 (국내 코스피 시총의 약 26% 점유)",
          "SK하이닉스 ADR 상장 규모: 전체 지분의 약 2.5% (원화 약 40조 원 규모)",
          "삼성전자 및 하이닉스 영업이익 컨센서스: 2분기 삼성전자 약 9.8조 원, SK하이닉스 약 7.1조 원 기대 (일반 D램 범용 50% 폭등이 기여)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "SK하이닉스가 미국 상장(ADR)을 통한 글로벌 재평가와 수급 개선을 완벽히 이끌고 있으며, 향후 3년간 FCF 500조 원 상회를 바탕으로 한 <span class=\"text-cyan-300 font-semibold\">초대형 자사주 매수 및 주주환원</span> 기대감이 장기 투자 자금을 강하게 견인하기 때문임.",
        "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "SK스퀘어(402340)", "SK(034730)"],
        "insight": "하이닉스의 ADR 상장은 지분 희석 노이즈가 아닌, 미국 시장 직접 상장을 통해 단숨에 글로벌 밸류에이션 리레이팅을 노리는 묘수임. 100조 원 주주환원설 부인 공시는 일정 및 규모 조율 과정의 기밀 유지 차원으로 이해해야 하며, 최태원 회장의 지배력 강화(락업 해제 시 자사주 원복 효과)와 엮인 그룹사 시너지의 전략적 포석이 숨겨져 있음.",
        "action_point": "ADR 상장 시점의 단기 주가 흔들림은 적극적인 비수기 저가 매입 기회이며, 하이닉스 지분을 지배하고 주주환원의 직접 수혜를 입는 지주사 <span class=\"text-cyan-300 font-semibold\">SK스퀘어</span> 및 <span class=\"text-cyan-300 font-semibold\">SK</span>의 비중을 포트폴리오 내에서 대폭 우호적으로 구성해야 함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "economy"],
        "tags": ["SK그룹시총2000조", "하이닉스ADR상장", "100조원주주환원설", "최태원회장지배력"]
      }
    }
  },
  "tyGE1ML_KPg": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "tyGE1ML_KPg",
        "title": "[26.06.16 오전 방송 전체보기] 미·이란 종전 합의 속 뉴욕증시 상승 마감...스페이스X, 연일 '급등'",
        "published": "2026-06-16T03:20:33+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=tyGE1ML_KPg",
        "thumbnail": "https://img.youtube.com/vi/tyGE1ML_KPg/hqdefault.jpg"
      },
      "analysis": {
        "summary": "도널드 트럼프 행정부의 중재 하에 미국과 이란이 종전 양해각서(MOU)에 공식 서명하고 <span class=\"text-violet-300 font-medium\">호르무즈 해협 재개방</span>을 결행하여 국제 유가가 배럴당 70달러대로 하락 안착함. 에너지 가격 진정은 인플레이션 압력을 덜어 신임 연준 의장 케빈 워시의 긴축 경계론을 차단하고 매크로 랠리 여건을 형성함. 한편 상장 첫날 시총 2.1조 달러를 기록한 <span class=\"text-cyan-300 font-semibold\">스페이스X</span>는 나스닥 100 편입 매수세와 레버리지 ETF SPEX 상장에 힘입어 폭등세를 이어감.",
        "key_claims": [
          "미-이란 임시 합의안에 따라 호르무즈 해협 통행 선박수가 공식 통계보다 조용히 급증하며 원유 및 원자재 공급 병목이 완벽히 해결됨.",
          "이스라엘의 네타냐후 총리가 합의안에 반발하고 있으나, 트럼프 행정부의 강경 압박으로 중동 지정학 전쟁 종료 흐름은 기정사실화됨.",
          "그동안 지정학 종전 리스크 때문에 매수를 유보했던 펀드 매수 대기 자금이 유가 안정화와 함께 방산주(LIG넥스원 등)로 강하게 유입되며 숏커버링이 발생함."
        ],
        "data_points": [
          "호르무즈 해협 실제 일일 통행 추정량: 블룸버그 상업 선박 추적 650건 대비 미국 조용한 호위선 포함 약 1,000건 돌파 확인",
          "국제 유가 밴드 변화: 지정학 갈등 당시 100달러선 지지 -> 평화 협상 타결 후 브랜드유 83달러, WTI 77.5달러선으로 하향 안착",
          "스페이스X 상장 패시브 매수 예상 규모: 나스닥 100 및 대형 지수 조기 편입에 따른 강제 패시브 매수세 약 270억~295억 달러 추정"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "중동 전쟁 종료 공식화에 따른 <span class=\"text-violet-300 font-medium\">유가 80달러선 하향 붕괴</span>로 글로벌 디스인플레이션이 가속화되고 있으며, 스페이스X의 2.1조 달러 상장 안착이 위험 자산 선호 심리를 강력히 뒷받침하고 있기 때문임.",
        "key_companies": ["스페이스X", "LIG넥스원(079550)", "한화에어로스페이스(012450)"],
        "insight": "종전 합의로 인해 방산주가 하락할 것이라는 통념과 달리, 종전 소식은 오히려 짓누르던 지정학 종전 공포(악재)를 해소하여 매수 대기 세력의 숏커버링 폭발(방산주 폭등)을 유도함. 스페이스X 상장은 단순 발사 비즈니스를 넘어 xAI의 거대 컴퓨팅 자산 결합 가치를 증시가 흡수하는 거대한 자본 수용 과정임.",
        "action_point": "유가 안정화로 멀티플 리레이팅 수혜를 볼 <span class=\"text-cyan-300 font-semibold\">반도체 소부장 및 빅테크</span> 비중을 적극 확대하고, 수급 해소로 신고가 랠리를 시작한 국내 우량 방산 섹터(<span class=\"text-cyan-300 font-semibold\">LIG넥스원, 한화에어로스페이스</span>)를 여전히 비중 유지 포지션으로 보유해야 함."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock", "space"],
        "tags": ["미이란종전합의", "호르무즈해협개방", "유가70달러선", "스페이스X폭등"]
      }
    }
  }
}

pending_dir = Path("data/pending")
analyzed_root = Path("data/analyzed")

for video_id, item in batch7_data.items():
    primary = item["primary"]
    data = item["data"]
    
    dest_dir = analyzed_root / primary
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / f"{video_id}.json"
    
    dest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[분석 저장 완료] {dest_path}")
    
    pending_file = pending_dir / f"{video_id}.json"
    if pending_file.exists():
        pending_file.unlink()
        print(f"[대기파일 삭제] {pending_file}")

print("Batch 7 processing completed successfully.")
