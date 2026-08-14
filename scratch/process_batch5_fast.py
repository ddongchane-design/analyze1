import json
from save_batch_helper import save_analyses

batch5_results = [
  {
    "video": {
      "id": "i0daARsLUF4",
      "title": "[8월 13일 마감시황] 삼전닉스 다음은 어디?…상승 흐름 이어갈 다음 순환매를 찾아라ㅣ홍선애, 이권희, 김장열 [클로징벨 라이브]",
      "published": "2026-08-13T08:54:48+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=i0daARsLUF4",
      "thumbnail": "https://img.youtube.com/vi/i0daARsLUF4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "코스피가 외국인의 2조 4천억 원대 기록적 순매수에 힘입어 <span class=\"text-emerald-400 font-semibold\">3.56% 급등한 6,813선</span>으로 마감함. 미국 CPI 안정과 네오클라우드(네비우스, 코어위브)의 폭등이 국내 반도체 투톱으로 강하게 전이됨. 특히 시카고상품거래소(<span class=\"text-cyan-300 font-semibold\">CME</span>)가 10월 5일 엔비디아 GPU(H100, 블랙웰)의 시간당 임대료를 기초자산으로 하는 <span class=\"text-cyan-300 font-semibold\">'GPU 선물 상품'</span> 출시 계획을 공식 발표함에 따라, AI 컴퓨팅 파워가 공식적인 금융 기초자산(ABS 및 헤지 지표)으로 편입되는 획기적 계기가 마련됨. 반도체 PER이 4~5배에 불과해 역사적 하단에 머물러 있어 반등 여력이 충분함.",
      "key_claims": [
        "외국인의 2조 4천억 원 일방향 현물 순매수는 단순 단기 숏커버링을 넘어 새로운 성격의 중장기 큰손 자금이 유입되었음을 시사함.",
        "CME의 GPU 선물 상품 출시는 AI CapEx와 GPU 임대료에 대한 공식 가격 발견(Price Discovery) 기능을 제공해 시장 노이즈를 축소시킬 선행지표가 될 것임.",
        "삼성전자와 SK하이닉스의 현재 PER(4~5배)은 과거 반도체 저점 구간(4~8배 하단)으로 메모리 가격이 20~30% 하락하더라도 영업이익 훼손이 제한적임."
      ],
      "data_points": [
        "코스피 종가: 6,813 (+3.56%), 외국인 순매수 2조 4,270억 원, 기관 7,000억 원 매수.",
        "CME GPU 선물 상품 출시 예정일: 2026년 10월 5일 (H100 및 블랙웰 시간당 렌탈 인덱스 기초자산).",
        "삼성전자/SK하이닉스 PER: 현재 4~5배 수준 (과거 평균 4~8배 대비 극단적 저평가)."
      ],
      "signal": "bullish",
      "signal_reason": "외국인 2.4조 원 역대급 매수세 유입, CME의 GPU 선물 공식화로 인한 AI 인프라 금융화, 역사적 PER 최하단 밸류에이션 매력.",
      "key_companies": [
        "삼성전자(005930)",
        "SK하이닉스(000660)",
        "엔비디아(NVDA)",
        "주성엔지니어링(036930)",
        "원익IPS(240810)"
      ],
      "insight": "AI 컴퓨팅 파워(GPU 임대료)가 CME 선물 시장에 상장되는 것은 석유/원자재처럼 AI 연산력이 21세기 글로벌 경제의 핵심 인프라 원자재로 완전히 공인되었음을 뜻함.",
      "action_point": "외국인 대규모 순매수가 집중된 삼성전자/SK하이닉스와 핵심 소부장(주성엔지니어링, 원익IPS, HPSP)에 대한 비중 확대를 유지할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "tech",
        "economy"
      ],
      "tags": [
        "코스피급등",
        "외국인2.4조매수",
        "CME_GPU선물",
        "삼성전자",
        "SK하이닉스",
        "반도체PER바닥",
        "클로징벨"
      ]
    }
  },
  {
    "video": {
      "id": "iFtrqg24eP4",
      "title": "워싱턴을 움직인 건 결국 일본이었다",
      "published": "2026-08-13T14:15:12+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=iFtrqg24eP4",
      "thumbnail": "https://img.youtube.com/vi/iFtrqg24eP4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "일본 재무성이 엔화 가치 급락을 방어하기 위해 미국 재무부를 설득하여 7월 31일 미·일 당국의 <span class=\"text-cyan-300 font-semibold\">공동 외환시장 개입</span>을 이끌어낸 막전막후를 조명함. 일본이 보유한 미국 국채를 대량 매각할 경우 미국 장기금리가 폭등할 것을 우려한 미국 워싱턴 당국을 움직여 공동 개입 합의를 도출한 것은 일본 외환 당국의 고도의 외교적 승리로 평가됨.",
      "key_claims": [
        "일본 단독 개입만으로는 시장의 투기적 엔도 숏 베팅을 꺾을 수 없었기에 미국을 직접 끌어들여 공동 개입을 성사시킴.",
        "미국 국채 매각 리스크를 지렛대로 활용해 미국 재무부의 개입 협조를 이끌어낸 일본 재무성의 전략적 승리임."
      ],
      "data_points": [
        "미·일 외환시장 공동 개입 발표일: 7월 31일."
      ],
      "signal": "neutral",
      "signal_reason": "미·일 당국의 공동 개입으로 엔화 변동성은 진정되었으나, 엔 캐리 트레이드 청산 압력 및 글로벌 유동성 재편 과정에 대한 지속 관찰 필요.",
      "key_companies": [],
      "insight": "환율 문제는 개별 국가의 통화정책을 넘어 글로벌 기축통화국(미국)과 주요 채권국(일본) 간의 거시 금융 안보 협력의 핵심 고리로 작동함.",
      "action_point": "엔/달러 환율 안정 추이와 엔 캐리 청산 여파가 아시아 증시 및 신흥국 유동성에 미치는 파급 효과를 점검할 것."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": [
        "stock"
      ],
      "tags": [
        "엔화개입",
        "일본재무성",
        "미국국채",
        "외환시장",
        "엔캐리트레이드",
        "언더스탠딩"
      ]
    }
  },
  {
    "video": {
      "id": "jbhpvIt34j8",
      "title": "GPU 위에 메모리를 쌓는다…삼성·하이닉스의 승부수ㅣ김인엽의 실리콘밸리나우",
      "published": "2026-08-13T09:00:10+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=jbhpvIt34j8",
      "thumbnail": "https://img.youtube.com/vi/jbhpvIt34j8/hqdefault.jpg"
    },
    "analysis": {
      "summary": "실리콘밸리 'FMS 2026(Future of Memory and Storage)' 현장에서 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>와 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>가 GPU 바로 위에 메모리를 직접 적층하는 차세대 3D 아키텍처를 전격 공개함. 삼성전자는 GPU 위에 HBM을 올리고 TSV 밀도를 10배 높인 <span class=\"text-cyan-300 font-semibold\">ZHBM</span>(연산 성능 최대 8배, 전력 효율 3배 향상)과 온디바이스 AI 미니 데이터센터용 <span class=\"text-cyan-300 font-semibold\">Z-NAND 5</span>를 발표함. 반면 SK하이닉스는 SRAM과 HBM 사이의 새로운 메모리 계층인 <span class=\"text-cyan-300 font-semibold\">3D 적층 D램(Tier 0.5)</span>과 샌디스크·구글과 함께 OCP 개방형 표준으로 추진하는 <span class=\"text-cyan-300 font-semibold\">HBF(High Bandwidth Flash)</span>를 공개하며 치열한 차세대 기술 표준 경쟁에 돌입함.",
      "key_claims": [
        "AI 가속기의 '메모리 벽'을 극복하기 위해 메모리가 GPU 옆(2.5D)에서 GPU 위(3D 직접 적층)로 이동하는 패러다임 전환이 시작됨.",
        "삼성전자는 메모리-파운드리-패키징의 종합 반도체 수직 통합(IDM) 역량을, SK하이닉스는 OCP 표준화 및 빅테크(구글, 샌디스크) 연합 생태계를 승부수로 내세움.",
        "낸드 플래시 역시 단순 스토리지를 넘어 AI 연산에 초고속으로 데이터를 직결 공급하는 3D 적층 고대역폭 플래시(Z-NAND / HBF)로 진화함."
      ],
      "data_points": [
        "삼성전자 ZHBM 성능 목표: 기존 HBM5 대비 연산 성능 최대 8배, 전력 효율 3배 개선, TSV 밀도 10배 향상.",
        "SK하이닉스 메모리 6대 계층: SRAM -> 3D적층D램(Tier 0.5) -> HBM -> D램 -> HBF/로컬SSD -> CXL/스토리지.",
        "HBF(High Bandwidth Flash) 컨소시엄: SK하이닉스, 샌디스크, 구글, 텐스토렌트 등 참여."
      ],
      "signal": "bullish",
      "signal_reason": "메모리 반도체가 단순 범용 상품에서 GPU와 1:1 맞춤형 3D 통합 시스템으로 격상되며 한국 반도체 기업들의 기술 독점력 및 판가 협상력 극대화.",
      "key_companies": [
        "삼성전자(005930)",
        "SK하이닉스(000660)",
        "샌디스크(SNDK)",
        "엔비디아(NVDA)",
        "구글(GOOGL)"
      ],
      "insight": "3D 적층 메모리 시대의 도래는 칩 설계사(엔비디아, 구글)와 메모리 제조사 간의 결속을 '커스터마이징 맞춤형 시스템'으로 영구 고착화시켜 후발 주자(중국 CXMT 등)의 진입을 원천 차단함.",
      "action_point": "3D 적층 TSV 및 하이브리드 본딩 장비/소재 기업(한미반도체, HPSP, 에스티아이 등)과 차세대 메모리 주도권을 쥔 삼성전자/SK하이닉스를 지속 매수할 것."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": [
        "stock"
      ],
      "tags": [
        "FMS2026",
        "ZHBM",
        "3D적층D램",
        "HBF",
        "ZNAND",
        "삼성전자",
        "SK하이닉스",
        "실리콘밸리나우"
      ]
    }
  },
  {
    "video": {
      "id": "ktBqAFkDOeo",
      "title": "달라진 외국인 수급…하반기 포트폴리오 지금이라도 다시 짜야 할까?ㅣSK증권 PB [돈이 되는 주식]",
      "published": "2026-08-13T12:00:37+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=ktBqAFkDOeo",
      "thumbnail": "https://img.youtube.com/vi/ktBqAFkDOeo/hqdefault.jpg"
    },
    "analysis": {
      "summary": "7월 하락장을 주도했던 외국인 매도세가 8월 중순을 기점으로 강력한 순매수로 급전환됨에 따라 하반기 포트폴리오 리밸런싱 전략을 제시함. 인플레이션 둔화와 금리 인하 경로가 가시화되는 국면에서, 낙폭 과대 주도주인 <span class=\"text-cyan-300 font-semibold\">반도체(HBM 대장주)</span>를 핵심 코어 자산으로 복원하고, 정책 수혜주인 <span class=\"text-cyan-300 font-semibold\">조선·방산</span> 및 실적 호조세를 보이는 고배당 밸류업 종목을 적절히 배분할 것을 조언함.",
      "key_claims": [
        "외국인 수급의 추세적 복귀는 국내 증시의 바닥 다지기가 완료되었음을 나타내므로 현금 보유보다 주식 비중 확대로 전환해야 함.",
        "포트폴리오의 중심축은 여전히 AI 반도체 선도 기업이어야 하며, 단기 순환매 종목에 지나치게 흔들리지 말아야 함."
      ],
      "data_points": [
        "8월 중순 외국인 코스피 순매수 강도: 일간 2조 원대 이상 폭풍 유입 확인."
      ],
      "signal": "bullish",
      "signal_reason": "외국인 대규모 자금 유입 재개 및 하반기 매크로 환경(금리 안정) 개선에 따른 지수 상승 추세 복귀.",
      "key_companies": [
        "SK하이닉스(000660)",
        "삼성전자(005930)",
        "한화오션(042660)"
      ],
      "insight": "공포 국면에서 주도주를 매도하고 후발주로 이동한 투자자들의 손실이 커지는 전형적인 패턴이 반복되고 있으며, 결국 실적 펀더멘털을 갖춘 1등 주로 복귀하는 것이 최선의 전략임.",
      "action_point": "하반기 포트폴리오의 50% 이상을 AI 반도체 핵심 대형주로 채우고, 조선/방산 및 밸류업 고배당주로 리스크를 분산할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "economy"
      ],
      "tags": [
        "외국인수급",
        "포트폴리오전략",
        "하반기주식",
        "SK하이닉스",
        "삼성전자",
        "SK증권"
      ]
    }
  },
  {
    "video": {
      "id": "lT3WpArAMOs",
      "title": "환율은 왜 오르고 코스피는 왜 오를까?…신규 매수 반도체 vs 2차전지ㅣ홍선애, 이형석, 염승환 [여의도 인사이트]",
      "published": "2026-08-13T09:30:22+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=lT3WpArAMOs",
      "thumbnail": "https://img.youtube.com/vi/lT3WpArAMOs/hqdefault.jpg"
    },
    "analysis": {
      "summary": "달러/원 환율이 1,420원대로 높은 수준을 유지함에도 불구하고 코스피가 대형 반도체 위주로 3.5% 이상 폭등한 이례적 디커플링 장세를 염승환 이사가 심층 해설함. 환율 상승은 미 금리/중동 리스크에 따른 달러 강세 요인이 크지만, 외국인 투자자 입장에서는 원화 약세가 오히려 한국 대형 수출주의 가격 매력을 높이는 요인으로 작용함. 반도체는 HBM 독점력과 3D 적층 기술로 실적 가시성이 가장 높은 반면, 2차전지는 LFP 전환과 판가 하락으로 회복 속도가 완만하여 신규 매수 우선순위는 반도체에 두어야 한다고 분석함.",
      "key_claims": [
        "환율 상승(원화 약세)에도 불구하고 외국인이 2조 원 넘게 매수한 것은 한국 반도체 기업의 글로벌 AI 독점 경쟁력을 신뢰하기 때문임.",
        "신규 매수 관점에서는 실적 턴어라운드가 검증된 반도체 소부장을 최우선으로 고려해야 하며, 2차전지는 선별적 트레이딩으로 접근해야 함."
      ],
      "data_points": [
        "달러/원 환율: 1,420원대 유지 속 코스피 3.56% 급반등.",
        "외국인 코스피 순매수: 2.4조 원 집중 유입."
      ],
      "signal": "bullish",
      "signal_reason": "원화 약세 국면을 뚫고 들어오는 강력한 외국인 반도체 바스켓 매수세와 실적 펀더멘털 확인.",
      "key_companies": [
        "삼성전자(005930)",
        "SK하이닉스(000660)",
        "LG에너지솔루션(373220)"
      ],
      "insight": "환율과 주가의 고전적 역상관관계 공식이 깨지고, 글로벌 AI 인프라 공급망 내 핵심 지배력을 가진 섹터로 글로벌 유동성이 직접 돌파구를 찾고 있음.",
      "action_point": "환율 상승 노이즈에 위축되지 말고 반도체 투톱 및 전공정/후공정 핵심 소부장(주성엔지니어링, 한미반도체 등) 중심의 비중 확대를 지속할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "economy",
        "tech"
      ],
      "tags": [
        "환율과증시",
        "코스피폭등",
        "반도체vs2차전지",
        "염승환",
        "여의도인사이트",
        "외국인매수"
      ]
    }
  },
  {
    "video": {
      "id": "nO5npWPNTYI",
      "title": "[26.08.13 뉴욕 증시 풀버전] CPI 수치 확인 후 뉴욕 증시 혼조 마감...반도체주는 또 '환호'",
      "published": "2026-08-13T03:16:01+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=nO5npWPNTYI",
      "thumbnail": "https://img.youtube.com/vi/nO5npWPNTYI/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국 7월 소비자물가지수(CPI)가 시장 예상치에 완벽히 부합하며 인플레이션 재점화 우려를 잠재운 가운데, 뉴욕 증시는 지수별 혼조세 속에서도 <span class=\"text-cyan-300 font-semibold\">반도체 및 AI 인프라 섹터</span>가 독보적인 급등 랠리를 펼침. 네오클라우드 선도 기업 네비우스와 코어위브가 10~20% 폭등하고 엔비디아와 마이크론이 강세를 보이며 AI CapEx 확장에 대한 시장의 전폭적 신뢰를 확인함.",
      "key_claims": [
        "CPI 발표로 9월 FOMC 금리 인하 기대감이 기정사실화되면서 증시의 매크로 하방 리스크가 해소됨.",
        "일반 경기민감주 대비 AI 데이터센터 및 반도체 인프라 기업으로 시장 유동성이 집중되는 'AI 독주 장세'가 재확인됨."
      ],
      "data_points": [
        "미국 7월 CPI: 전년 동기 대비 예상치 부합하며 물가 안정 확인.",
        "AI 데이터센터 클라우드(네비우스/코어위브) 주가 10~20%대 폭등."
      ],
      "signal": "bullish",
      "signal_reason": "CPI 안정으로 인한 금리 하방 압력과 AI 하드웨어/데이터센터 인프라 기업들의 실적 폭발력 재확인.",
      "key_companies": [
        "엔비디아(NVDA)",
        "마이크론(MU)",
        "네비우스(NBIS)",
        "코어위브(CoreWeave)"
      ],
      "insight": "거시 경제의 완만한 둔화(소프트 랜딩) 국면에서는 성장을 증명하는 유일한 분야인 AI 테크 인프라로 기관의 자금 쏠림이 더욱 심화됨.",
      "action_point": "금리 인하 사이클 진입에 맞춰 AI 반도체 및 클라우드 인프라 수혜주에 대한 롱(Long) 포지션을 공격적으로 유지할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": [
        "economy",
        "tech"
      ],
      "tags": [
        "뉴욕증시",
        "CPI발표",
        "반도체환호",
        "네비우스",
        "코어위브",
        "삼프로TV라이브"
      ]
    }
  }
]

if __name__ == "__main__":
    save_analyses(batch5_results)
