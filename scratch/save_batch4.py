import json
from pathlib import Path

batch4_data = {
  "xSTIribGifU": {
    "primary": "space",
    "data": {
      "video": {
        "id": "xSTIribGifU",
        "title": "저는 스페이스X 이렇게 준비합니다. (나스닥 편입, 락업 해제, ETF 비교)",
        "published": "2026-06-16T11:00:07+00:00",
        "channel_name": "수페TV",
        "url": "https://www.youtube.com/watch?v=xSTIribGifU",
        "thumbnail": "https://img.youtube.com/vi/xSTIribGifU/hqdefault.jpg"
      },
      "analysis": {
        "summary": "나스닥에 상장한 <span class=\"text-cyan-300 font-semibold\">스페이스X</span>의 핵심 사업구조는 위성 통신(스타링크), 로켓 발사, AI 인프라(Grok 및 데이터센터 임대)로 구분됨. 구글·앤트로픽과의 연간 260억 달러(약 40조 원) 규모 데이터센터 임대 계약을 통해 막대한 현금 흐름을 창출하고 있으며, 7월 4일 <span class=\"text-amber-300 font-bold\">나스닥 100 지수 편입</span>에 따른 295억 달러의 패시브 자금 유입 기대감과 8월 말부터 시작되는 <span class=\"text-rose-400 font-medium\">보호예수(락업) 해제 물량</span>이 맞설 예정임. 우주 산업은 2016년 AI 태동기 수준으로, 변동성을 고려해 국내외 우주 테마 ETF(ACE, KODEX 등)를 활용한 분산 투자가 권장됨.",
        "key_claims": [
          "스페이스X는 단순 우주선 발사 기업이 아니라, 글로벌 위성 통신망(점유율 71%)과 연간 40조 원 규모의 AI 데이터센터 임대 사업을 영위하는 테크 인프라 기업임.",
          "상장 유통 물량이 4.9%로 극히 적어 초기 변동성이 심하며, 7월 초 나스닥 100 지수 편입 호재와 8월 말 이후의 단계적 락업 해제 악재가 줄다리기를 벌일 것임.",
          "스페이스X 편입 여부에 따라 국내외 우주 항공 ETF의 수익률이 갈리고 있어, 비중 및 투자 성향에 맞춘 ETF 선택이 현실적 대안임."
        ],
        "data_points": [
          "스타링크 위성 인터넷 매출 성장률: 전년 대비 71.4%",
          "글로벌 위성 통신 시장 스타링크 점유율: 71% 수준",
          "현재 가동 위성 수 및 최종 목표: 현재 약 1만 개 → 최종 42,000개",
          "글로벌 로켓 발사 횟수 중 스페이스X 점유율: 83% 수준",
          "구글 및 앤트로픽 대상 데이터센터 임대 매출: 연간 약 260억 달러 (원화 약 40조 원)",
          "스페이스X 상장 유통 주식 비율: 4.9% 수준",
          "나스닥 100 편입 시 패시브 매수 예상 수요: 약 295억 달러 (약 40조 원)",
          "락업 물량 단계적 해제 개시: Q2 실적 발표 시점 (8월 말~9월 초) 전체 락업 물량의 20% 해제 시작"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "스타링크의 독점적 성장과 연간 40조 원에 달하는 <span class=\"text-cyan-300 font-semibold\">AI 데이터센터 임대 캐시카우</span>를 확보했고, 7월 초 대규모 지수 편입 패시브 수급이 유입될 예정이기 때문임. 단, 8월 말 락업 해제 시점의 변동성은 경계해야 함.",
        "key_companies": ["스페이스X", "알파벳(GOOGL)", "테슬라(TSLA)", "로켓랩(RKLB)", "비아셋"],
        "insight": "스페이스X 상장이 우주 산업의 강력한 촉매제이나, 본업인 발사 매출보다 구글/앤트로픽에 GPU 연산력을 공급하는 데이터센터 임대(CapEx 비즈니스)가 캐시카우 역할을 하고 있다는 점이 기업 가치평가의 핵심임. 또한 타 우주 기업 임원들의 최고점 내부자 매도가 포착되고 있어, 우주 테마 전반에 거품이 꼈는지 개별 기업의 재무 상태를 엄격히 분별할 필요가 있음.",
        "action_point": "직접 투자는 유통 물량 부족과 락업 해제 변동성으로 위험하므로, 스페이스X 비중이 높은 국내외 우주 항공 ETF(<span class=\"text-cyan-300 font-semibold\">ACE 미국우주테크액티브</span> 또는 <span class=\"text-cyan-300 font-semibold\">KODEX 우주항공</span>)를 활용해 포트폴리오의 5~10% 수준에서 장기 적립식으로 투자하는 전략이 안전함."
      },
      "classification": {
        "primary_topic": "space",
        "secondary_topics": ["stock", "tech"],
        "tags": ["스페이스X상장", "락업해제", "나스닥100편입", "우주항공ETF"]
      }
    }
  },
  "9NRydL2bQic": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "9NRydL2bQic",
        "title": "SK하이닉스, 미국 상장 후 100조원 주주환원? | 소프트뱅크 BD 풋옵션 만기 다가오자 삼성전자 들썩? | 류종은 삼프로TV 기자 [뉴스3]",
        "published": "2026-06-16T23:26:47+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=9NRydL2bQic",
        "thumbnail": "https://img.youtube.com/vi/9NRydL2bQic/hqdefault.jpg"
      },
      "analysis": {
        "summary": "SK하이닉스가 자금 조달 및 인프라 투자를 위해 지분 2.5% 규모의 <span class=\"text-cyan-300 font-semibold\">나스닥 ADR 상장</span>(약 40조 원 조달)을 추진하는 과정에서 주주 희석 우려를 달래기 위한 백조 원대 주주환원설이 제기됨(회사 측은 금액에 대해 사실무근이라 부인했으나 FCF 기준 산술적 실현 가능성은 존재). 또한 6월 20일 만기인 소프트뱅크의 <span class=\"text-cyan-300 font-semibold\">보스턴 다이내믹스 풋옵션</span> 행사 여부 및 삼성전자의 지분 인수 루머가 주목받고 있으며, 한화가 KAI 지분을 9.04%로 늘려 2대 주주로 올라서며 방산 합병 시나리오가 대두됨.",
        "key_claims": [
          "SK하이닉스가 미국 나스닥 ADR 상장을 통해 약 40조 원의 유동성을 확보하여 클러스터 건설 자금으로 활용할 계획이나, 주주들은 신주 발행에 따른 지분 희석을 우려함.",
          "향후 3년간 SK하이닉스의 누적 잉여현금흐름(FCF)이 500조 원을 상회할 것으로 전망되어, 회사 규정(FCF 50% 환원)에 따른 100조 원 규모 주주환원은 재무적으로 충분히 가능함.",
          "보스턴 다이내믹스 지분 10%에 대한 소프트뱅크의 풋옵션 결정(6월 20일)에 따라 현대차의 추가 인수 또는 삼성전자, 구글 등과의 전략적 동맹 지분 양수 여부가 결정될 것임.",
          "한화그룹이 한국항공우주(KAI) 지분을 확보해 2대 주주로 부상하면서, 대기업 주도의 종합 방산 및 우주항공 기업화(독과점 논란 포함)를 가속화하고 있음."
        ],
        "data_points": [
          "SK하이닉스 나스닥 ADR 상장 추진 비중: 전체 지분의 2.5% 수준 (약 40조 원 규모)",
          "SK하이닉스 연간 잉여현금흐름(FCF) 전망: 올해 약 145조 원, 내년 약 225조 원 수준 (3년 누적 500조 원 돌파 예상)",
          "SK그룹 시가총액: 약 2,019조 원 (이 중 SK하이닉스 비중이 약 1,700조 원 수준)",
          "현대차 보스턴 다이내믹스 인수 계약 상 IPO 의무 기한: 4년 (올해 6월 20일 풋옵션 만기)",
          "한화의 한국항공우주(KAI) 보유 지분율: 9.04% (수출입은행에 이어 2대 주주 등극)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "SK하이닉스의 ADR 상장을 통한 40조 원 대규모 자금 확보 및 2027년까지 500조 원 이상 기대되는 압도적인 <span class=\"text-cyan-300 font-semibold\">잉여현금흐름(FCF) 체력</span>이 증명되었으며, 보스턴 다이내믹스 및 KAI 등 로봇/방산 M&A 모멘텀이 강화되고 있기 때문임.",
        "key_companies": ["SK하이닉스(000660)", "한화에어로스페이스(012450)", "한국항공우주(047810)", "삼성전자(005930)", "현대자동차(005380)"],
        "insight": "SK하이닉스의 ADR 상장은 단기 지분 희석 노이즈로 작용할 수 있으나, 미국 시장 상장을 통해 글로벌 밸류에이션 할증을 받고 대규모 전 공정 투자를 적기에 집행할 재무적 기초를 닦는 장기 호재임. 또한 한화의 카이 지분 인수는 경남권에 메가 항공방산 클러스터를 형성하여 규모의 경제와 글로벌 방산 수출 침투율을 끌어올릴 중대 변곡점임.",
        "action_point": "ADR 상장 공시 및 락업/희석 우려로 SK하이닉스 주가가 일시적으로 조정받을 때 적극적인 분할 매수 기회로 활용하고, 국내 방산 독과점 수혜 및 카이 인수 기대감이 실리는 <span class=\"text-cyan-300 font-semibold\">한화에어로스페이스</span>의 비중을 포트폴리오 내에서 우호적으로 가져가야 함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "space"],
        "tags": ["SK하이닉스ADR", "주주환원정책", "보스턴다이내믹스풋옵션", "한화KAI인수"]
      }
    }
  },
  "lmJtJFOu6qc": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "lmJtJFOu6qc",
        "title": "미국이 금리 올려도, 한국 주식은 버틴다? 그 이유는요… | 신영증권 김효진 박사[글로벌 인터뷰]",
        "published": "2026-06-16T22:58:49+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=lmJtJFOu6qc",
        "thumbnail": "https://img.youtube.com/vi/lmJtJFOu6qc/hqdefault.jpg"
      },
      "analysis": {
        "summary": "신임 연준 의장 <span class=\"text-cyan-300 font-semibold\">케빈 워시</span>는 기준 금리는 낮게 유지하되 비대해진 <span class=\"text-amber-300 font-bold\">대차대조표(자산 규모) 축소</span>(QT)에 집중하는 독특한 통화 정책을 펼칠 것임. 연준 자산 1조 달러 축소는 금리 25bp 인상과 유사한 효과를 내며 장기 금리 상승 요인으로 작용하나, 워시는 AI가 가져올 생산성 혁신과 디플레이션 효과를 신뢰하고 있음. 한국 증시는 <span class=\"text-cyan-300 font-semibold\">AI 메모리 병목</span>(HBM 등) 독점력과 이미 저평가된 밸류에이션 덕분에 고금리 압박에도 상대적으로 높은 버팀목(내성)을 지니고 있음.",
        "key_claims": [
          "케빈 워시 의장은 2008년 이후 배가 된 6.5조 달러 규모의 비대한 연준 자산을 축소하는 데 최우선 순위를 둘 것임.",
          "워시의 성향은 기준 금리 수준에 대해서는 낮게 가져가려 하나(비둘기), 대차대조표 축소에는 완강하여(매) 시장이 일방적으로 매파/비둘기파로 해석하기 어려움.",
          "연준 자산 축소는 장기 국채 금리 상승을 유발해 주가 할인율 부담을 키우지만, 한국 증시는 글로벌 AI 반도체 벨류체인 중심의 수출 성장세와 저평가 매력으로 매크로 민감도가 낮아짐."
        ],
        "data_points": [
          "2008년 금융위기 이전 연준 자산 규모: 약 1조 달러 수준",
          "팬데믹 당시 연준 자산 최고치: 약 9조 달러",
          "현재 연준 자산 규모: 약 6.5조 달러",
          "연준 자산 축소의 금리 인상 환산 효과: 1조 달러 축소 당 약 25bp(0.25%) 인상 효과와 동일"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "유가 하락과 이란 종전은 긍정적이나, 연준의 <span class=\"text-rose-400 font-medium\">대차대조표 축소(QT) 본격화</span>에 따른 장기 금리 상승 우려가 밸류에이션 부담을 주기 때문에 종합적인 효과는 중립적임.",
        "key_companies": [],
        "insight": "워시의 통화 정책은 단기 금리(기준 금리)는 낮게 묶어 경기 침체 우려를 덜어주는 대신, 장기 금리(대차대조표 축소)를 자극하여 자본 시장의 유동성을 서서히 말리는 '페인트가 마르는 식의(Slow but persistent)' 통제임. 이러한 환경에서는 고평가된 자산보다 실질적인 실적 턴어라운드를 보여주고 저평가 메리트가 있는 한국의 <span class=\"text-cyan-300 font-semibold\">반도체 소부장 주도주</span>가 유용한 피난처가 될 수 있음.",
        "action_point": "연준의 QT 가이드라인 발표에 맞춰 장기 금리 상승에 취약한 고부채 중소형주 비중은 조절하고, AI 메모리 핵심 밸류체인(<span class=\"text-cyan-300 font-semibold\">SK하이닉스, 삼성전자</span>) 및 하반기 실적 가시성이 높은 저PBR 우량주 중심의 투자 포지션을 강화해야 함."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["대차대조표축소", "케빈워시의장", "장기국채금리", "한국증시내성"]
      }
    }
  },
  "BIdvqL9iwIc": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "BIdvqL9iwIc",
        "title": "스페이스X, '커서' 개발사 $600억 인수 확정ㅣ제프리스, 최선호주로 'GE버노바' 선정ㅣ웨드부시 \"엔비디아 자사주 매입위해 회사채 발행“ㅣ홍키자의 매일뉴욕",
        "published": "2026-06-16T14:14:40+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=BIdvqL9iwIc",
        "thumbnail": "https://img.youtube.com/vi/BIdvqL9iwIc/hqdefault.jpg"
      },
      "analysis": {
        "summary": "<span class=\"text-cyan-300 font-semibold\">스페이스X</span>가 AI 코딩 도구 '커서(Cursor)' 개발사인 니스피어(Anysphere)를 600억 달러(약 90조 원) 전액 주식 교환 방식으로 인수함. 이로 인해 스페이스X 주가는 16% 급등하며 아마존을 제치고 글로벌 시가총액 4~5위로 도약함. 반면 마이크로소프트는 AI 수익성 과장 의혹으로 주주 소송이 제기되어 2% 하락했고, 제프리스는 전력망/인프라 수혜주로 <span class=\"text-cyan-300 font-semibold\">GE 버노바(GEV)</span>를 최선호주로 선정함.",
        "key_claims": [
          "스페이스X가 AI 코딩 도구 개발사를 600억 달러에 인수하여 우주 인프라와 AI 데이터센터 소프트웨어 시너지를 강화함.",
          "마이크로소프트가 AI 매출 기여도를 과장했다는 이유로 경찰·소방 연기금으로부터 집단 소송을 당해 주가 조정을 받음.",
          "유가 하락은 이란과의 개략적인 종전 서명(MOU) 호재를 선반영했으나, 실제 해협 지뢰 제거 및 통행 정상화에는 상당한 시일이 소요될 것임.",
          "미국 공장 리쇼어링과 데이터센터 증설용 장비 수요로 인해 투자은행(모건스탠리 등), 중장비(캐터필러), 반도체 장비(램리서치 등)가 동반 신고가를 기록하는 '미국 예외주의'가 나타남."
        ],
        "data_points": [
          "스페이스X의 니스피어(커서 개발사) 인수 규모: 600억 달러 (약 90조 원) 전액 주식 교환",
          "국내 서학개미들의 스페이스X 일일 결제 규모: 약 1조 2천억 원",
          "미국 5월 수입물가지수 상승률: 전월 대비 1.9% (시장 예상치 1.0% 상회)",
          "석유류 제외 비석유 수입물가지수 상승률: 전월 대비 0.8%"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "스페이스X의 공격적인 AI 우량 유니콘 인수와 미국 리쇼어링/인프라 투자가 이끄는 <span class=\"text-cyan-300 font-semibold\">자본재/장비/금융 섹터의 동반 신고가</span> 랠리가 미국 예외주의 경제 체력을 강력히 입증하고 있기 때문임.",
        "key_companies": ["스페이스X", "마이크로소프트(MSFT)", "GE 버노바(GEV)", "캐터필러(CAT)", "모건스탠리(MS)", "엔비디아(NVDA)"],
        "insight": "스페이스X가 천문학적인 자사 몸값(고평가 주식)을 화폐처럼 활용해 90조 원 규모의 핵심 AI 소프트웨어 기업(Cursor 개발사)을 무혈 입성시킨 것은 머스크 특유의 자본 레버리지 기술의 극치임. 또한 미시간 연기금의 MS 소송은 향후 빅테크들의 AI 실질 수익성 검증을 압박하는 기폭제가 될 것이며, 이는 단순 소프트웨어보다 실물이 오가는 반도체 장비 및 전력망/인프라(GE 버노바, 캐터필러)의 투자 안전성을 더욱 돋보이게 함.",
        "action_point": "AI 거품 논란에서 자유롭고 미국 설비투자(CapEx) 사이클의 직접 수혜를 입는 <span class=\"text-cyan-300 font-semibold\">GE 버노바(GEV) 및 전력/반도체 장비 우량주</span> 비중을 유지하고, 단기 변동성이 확대되는 스페이스X와 주주 소송 리스크가 불거진 MS의 비중 조절에 유의해야 함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "space"],
        "tags": ["스페이스X커서인수", "MS주주소송", "GE버노바타픽", "미국예외주의"]
      }
    }
  },
  "NFWVgMrAVPw": {
    "primary": "crypto",
    "data": {
      "video": {
        "id": "NFWVgMrAVPw",
        "title": "'빅테크와 월가의 원픽은 하이퍼리퀴드' 내러티브 붕괴한 이더리움에서 발 빼는 기관들 | 서동주, 김동환, 조동현 언디파인 랩스 대표 [크립토 PLUS]",
        "published": "2026-06-16T04:30:39+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=NFWVgMrAVPw",
        "thumbnail": "https://img.youtube.com/vi/NFWVgMrAVPw/hqdefault.jpg"
      },
      "analysis": {
        "summary": "이더리움의 핵심 내러티브가 '전통 금융 대체(100% 온체인)'에서 <span class=\"text-rose-400 font-medium\">50% 하이브리드 온/오프체인</span> 구조로 축소됨. AI 기술 고도화로 온체인 해킹이 전년 대비 70% 폭증하자, 기관들은 리스크 회피를 위해 수수료 수취 금융을 커스터디(앵커리지 등)를 통한 오프체인 담보 관리 방식으로 변경함. 반면 오더북 유동성을 빌려주는 <span class=\"text-cyan-300 font-semibold\">하이퍼리퀴드(Hyperliquid)</span>와 실물자산 토큰화(RWA)는 유통 레일로서 입지를 다지고 있어, 가상자산이 전통 금융의 하위 전송 인프라로 편입되는 변화가 일어남.",
        "key_claims": [
          "AI 기반 해킹 위협 증가로 기관 투자자들이 100% 온체인 자산 예치를 극도로 경계하며 디파이 리스크가 부각됨.",
          "이더리움은 스마트 컨트랙트 금융 플랫폼이란 꿈에서 벗어나 금융 상품의 전송 및 최종 청산을 담당하는 단순 유통 레일로 재정의되고 있음.",
          "이더리움 재단은 중립성 이념을 깎아내고 비즈니스 수주를 위해 영업 조직(이더리움 엔터프라이즈)을 스핀오프(분사)해 상업적 세일즈에 나서기 시작함.",
          "하이퍼리퀴드는 빌더 코드를 통해 빅테크/전통 핀테크에 오더북 유동성을 API처럼 공급하는 유통 플랫폼으로서 강한 실적을 내고 있음."
        ],
        "data_points": [
          "2026년 가상자산 온체인 해킹 사고 건수: 전년 대비 70% 증가",
          "하이퍼리퀴드 온체인 유동성 공급 수수료 수익: 약 4,000만 달러 이상",
          "하이퍼리퀴드 오더북 활용 고객 중 빅테크/대형 IT 비율: 40% 수준"
        ],
        "signal": "bearish",
        "signal_confidence": "medium",
        "signal_reason": "탈중앙화 및 온체인 금융 대체라는 이더리움의 프리미엄 가치 동력이 해킹 리스크와 <span class=\"text-rose-400 font-medium\">기관의 오프체인 회귀</span>로 인해 희석되고 있고 수수료 소각 메커니즘이 약화되었기 때문임.",
        "key_companies": ["블랙록", "JP모건(JPM)"],
        "insight": "가상자산 시장이 '탈중앙화 이념'에서 '철저한 유통 효율 및 영업력'의 영역으로 전환되고 있음. 이더리움조차 자존심을 꺾고 상업 세일즈 분사를 단행하는 상황에서, 시장 가치는 기술력보다 기관용 RWA 레일 선점(블랙록 BUIDL 등)이나 실물 금융(JP모건 전용 프라이빗 체인 등)에 쏠리게 될 것임.",
        "action_point": "이더리움의 단독 금융 지배력 약화를 반영해 포트폴리오 내 가상자산 배분을 비트코인 중심으로 안정화하고, 솔라나 및 모나드 등 <span class=\"text-cyan-300 font-semibold\">고속/저비용 유통 레일 경쟁자</span>들의 약진과 전통 금융사(블랙록, JP모건)의 자체 토큰화 채택 추이를 예의주시해야 함."
      },
      "classification": {
        "primary_topic": "crypto",
        "secondary_topics": ["economy"],
        "tags": ["이더리움내러티브", "RWA토큰화", "하이퍼리퀴드", "온체인해킹"]
      }
    }
  }
}

pending_dir = Path("data/pending")
analyzed_root = Path("data/analyzed")

for video_id, item in batch4_data.items():
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

print("Batch 4 processing completed successfully.")
