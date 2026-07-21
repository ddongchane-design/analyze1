import json
from pathlib import Path

# Batch 1 analysis data
batch1_data = {
  "0fc4SaAwfH8": {
    "topic": "crypto",
    "content": {
      "video": {
        "id": "0fc4SaAwfH8",
        "title": "'주춤한 AI, 유동성은 어디로?' 힘 못 쓰는 비트코인, MSTR은 8거래일 연속 하락 | 서동주, 김동환, 오진석 미디어 에디터 [크립토 PLUS]",
        "published": "2026-06-29T04:31:52+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=0fc4SaAwfH8",
        "thumbnail": "https://img.youtube.com/vi/0fc4SaAwfH8/hqdefault.jpg"
      },
      "analysis": {
        "summary": "AI 랠리가 일시적으로 주춤하면서 유동성이 <span class=\"text-cyan-300 font-semibold\">러셀 2000</span> 및 가치주/헬스케어 섹터로 분산되는 순환매가 관찰됨. 반면 <span class=\"text-rose-400 font-medium\">비트코인(BTC)</span>은 6만 달러 지지선이 붕괴되며 약세를 지속하고 있고, 대형 채굴 기업들은 AI 데이터센터 공급 파워로의 피봇을 가속화하고 있음. 비트코인 ETF 자금 역시 역대급 순유출세를 기록하며 단기 수급 부담이 가중됨.",
        "key_claims": [
          "AI 픽아웃 우려 속에서 기관 자금이 이탈하여 <span class=\"text-cyan-300 font-semibold\">헬스케어</span> 및 배당주 중심의 방어주 섹터로 유동성 순환매가 발생함.",
          "비트코인은 가격 상승 모멘텀의 부재로 인해 투자 매력도가 하락하는 <span class=\"text-rose-400 font-medium\">노잼 장세</span>에 진입하며 6만 달러선 아래로 밀림.",
          "<span class=\"text-cyan-300 font-semibold\">마이크로스트레티지(MSTR)</span>는 보통주 추가 증자 부담과 우선주(STRC) 프리미엄 붕괴 리스크로 인해 8거래일 연속 급락함."
        ],
        "data_points": [
          "비트코인 가격: 6만 달러선 하회 및 YTD 대비 30% 이상 하락 기록",
          "ETF 및 크립토 펀드 자금: 최근 30일간 금 및 비트코인에서 120억 달러 유출, 반도체 ETF로 200억 달러 이상 유입",
          "마이크로스트레티지(MSTR) 주가: 8거래일 연속 하락하며 2년 반 만에 최저치 경신"
        ],
        "signal": "neutral",
        "signal_reason": "비트코인 ETF의 대규모 순유출세 가속화와 주가 하락은 악재이나, 장기적 가치 보존 처로서의 입지는 유지되고 있어 단기 횡보 우려를 반영해 중립으로 판단함.",
        "key_companies": [
          "마이크로스트레티지(MSTR)",
          "코인베이스(COIN)",
          "테슬라(TSLA)"
        ],
        "insight": "크립토 시장은 높은 변동성 대비 실질적이고 가시적인 ROI를 즉각 입증하는 AI 테크 기업들에 비해 자금 흡수력이 떨어져 노잼 장세를 겪고 있음. MSTR처럼 무리한 레버리지를 활용하는 기업의 주당 가치(BPS) 희석 우려와 채굴사들의 <span class=\"text-cyan-300 font-semibold\">AI 데이터센터 인프라</span> 전환 속도가 향후 크립토 시장 재편의 핵심 쟁점이 될 것임.",
        "action_point": "비트코인 ETF 유출 흐름과 6만 달러선 탈환 여부를 보수적으로 모니터링하며, MSTR 보통주 등 레버리지 주식보다는 AI 인프라 기업으로 성공적인 체질 개선을 선언한 <span class=\"text-cyan-300 font-semibold\">비트팜(킬 인프라스트럭처)</span> 등에 선별적으로 관심을 가질 필요가 있음."
      },
      "classification": {
        "primary_topic": "crypto",
        "secondary_topics": ["stock", "economy"],
        "tags": ["비트코인유출", "마이크로스트레티지", "순환매장세", "AI데이터센터", "러셀2000"]
      }
    }
  },
  "24yMBRhcisQ": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "24yMBRhcisQ",
        "title": "\"中 무역흑자 반토막 내서 눈속임\" 직격탄 날린 美 경제학자ㅣ이상은의 워싱턴나우",
        "published": "2026-06-29T03:05:00+00:00",
        "channel_name": "한경 글로벌마켓",
        "url": "https://www.youtube.com/watch?v=24yMBRhcisQ",
        "thumbnail": "https://img.youtube.com/vi/24yMBRhcisQ/hqdefault.jpg"
      },
      "analysis": {
        "summary": "미국 경제학계 내에서 글로벌 불균형의 근본 원인이 중국에 있으며, 보호무역을 위한 <span class=\"text-rose-400 font-medium\">관세 및 중상주의 정책</span>이 불가피하다는 목소리가 힘을 얻고 있음. 미 외교협회(CFR)의 브레드 세처 연구원은 중국 외환당국이 국제수지 통계를 조작하여 흑자 규모를 대폭 축소 보고(공식 4천억 달러 vs 실제 1조 달러 추정)하고 있다고 폭로함. 이러한 안보 갈등 구도는 철강 및 자동차 등 한국의 제조업 생태계에도 무역 제재 불똥으로 작용할 우려를 자극함.",
        "key_claims": [
          "중국은 전기차, 배터리, 태양광 분야에서 정부 보조금을 통해 인위적인 <span class=\"text-rose-400 font-medium\">차이나 쇼크 2.0</span>을 유도하여 서방 제조업을 실존적으로 위협함.",
          "미국 경제학자들은 자유무역 체제 실험의 실패를 인정하고, 관세 장벽과 <span class=\"text-rose-400 font-medium\">세이프가드 등 무역 방어 도구</span>를 즉각 가동할 것을 권고함.",
          "미국 무역 당국(USTR)은 한국의 과거 제조업 육성 이력을 언급하며 한국 역시 무역 흑자 조작 도매금으로 묶어 제재할 가능성이 농후함."
        ],
        "data_points": [
          "미국 1분기 GDP 성장률 확정치: 2.1% (잠정치 대비 +0.5%p 상향 조정)",
          "중국 무역 흑자 규모 불일치: 공식 국제수지 4,000억 달러 vs 세처의 관세 통계 기반 실제 흑자 1조 달러 수준 추정",
          "유럽 경상흑자 규모: 아일랜드로의 다국적 기업 이익 이전 효과 배제 시 GDP의 2% 미만으로 하향 조정"
        ],
        "signal": "bearish",
        "signal_reason": "미국이 정파에 무관하게 보호무역 장벽과 중상주의 관세 정책을 강화하는 세계관으로 회귀함에 따라, 무역 의존도가 높은 한국의 제조업 생태계에 장기 규제 리스크가 심화될 것임.",
        "key_companies": [
          "포스코(005490)",
          "폭스바겐",
          "애플"
        ],
        "insight": "글로벌 무역 질서가 자유무역에서 강대국 간의 중상주의적 대결 구도로 전환되고 있음. 특히 중국이 '공장 없는 제조' 통계 왜곡을 통해 경상수지를 숨기고 있다는 학계의 정밀 분석은 미국의 <span class=\"text-rose-400 font-medium\">관세 장벽 정당화 논리</span>를 더욱 견고히 하고 있으며, 이는 한국과 같은 수출 강국에 직접적인 안보 리스크로 직결됨.",
        "action_point": "미국 USTR의 한국산 제조업 부품(특히 철강, 자동차) 관련 301조 조사 등 관세 규제 추이를 긴밀히 모니터링해야 하며, 장기적 규제 우회를 위해 글로벌 생산 설비의 <span class=\"text-cyan-300 font-semibold\">현지화(Localization)</span>를 적극 추진하는 기업 위주로 투자 리스크를 분산해야 함."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["차이나쇼크2.0", "브레드세처", "관세장벽", "무역적자", "보호무역주의"]
      }
    }
  },
  "4hKM4dezUjc": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "4hKM4dezUjc",
        "title": "삼성·SK 2000조원 승부수…호남 반도체·영남 피지컬 AI | 중국산 메모리 사게 해달라는 애플…'1인당 100억' 번 키옥시아 | 권순우 삼프로TV 기자 [뉴스3]",
        "published": "2026-06-28T23:28:07+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=4hKM4dezUjc",
        "thumbnail": "https://img.youtube.com/vi/4hKM4dezUjc/hqdefault.jpg"
      },
      "analysis": {
        "summary": "삼성전자와 SK하이닉스가 호남 반도체 클러스터, 영남 피지컬 AI, 충청 OLED 등 전국적 범주에 걸쳐 총 <span class=\"text-cyan-300 font-semibold\">2,000조 원 규모의 초대형 투자</span> 계획을 본격화함. 최태원 SK 회장은 HBM/AI 메모리 병목을 방지하기 위해 5년 내 전체 웨이퍼 생산 능력을 2배로 확장하여 단가를 점진적으로 인하하고 중국의 추격을 원천 봉쇄하기로 결단함. 한편, 애플은 부품 마진 방어를 위해 중국산 D램(CXMT) 사용 승인을 미국 상무부에 긴밀히 로비하고 있음.",
        "key_claims": [
          "국내 반도체 대기업들의 2,000조 원 투자는 단기 이익 축소 리스크가 존재하나, 장기 AI 인프라 선점을 위한 대승적 차원의 <span class=\"text-cyan-300 font-semibold\">인프라 투자</span> 배팅임.",
          "최태원 SK 회장은 AI 칩 공급 모델의 생존과 HBM 독점 비난 차단을 위해 2030년까지 <span class=\"text-cyan-300 font-semibold\">웨이퍼 CapEx 증설</span>을 대폭 가속화하겠다고 선언함.",
          "애플은 메모리 가격 인상에 따른 자사 기기 가격 상승(20%) 압박을 줄이기 위해 중국 공급망 완화를 청원 중이나 미국 의회의 <span class=\"text-rose-400 font-medium\">국가 안보 규제</span> 장벽으로 무산될 공산이 큼."
        ],
        "data_points": [
          "삼성·SK 전국 클러스터 총 투자액: 약 2,000조 원 수준 돌파 추정",
          "SK하이닉스 5개년 증설 목표: 전체 웨이퍼 생산 능력 2배 확대 (용인 2패브 등 가동 가속)",
          "LS일렉트릭 생산 시설 증설: 미국 유타 배전반 공장 2,500억 원 투자, 기존 대비 6배 확장",
          "삼성전기 서버용 MLCC 공급 협상 규모: 글로벌 빅테크와 5,000억 원 안팎 공급 조율 중",
          "키옥시아 주식 가치 재평가: 베인캐피탈 출자 지분 600명 임직원 1인당 100억 원 대 분배 (SK하이닉스 간접 출자분 약 10조 원 이상 평가이익 유력)"
        ],
        "signal": "bullish",
        "signal_reason": "삼성과 SK의 초대형 2,000조 원 투자와 글로벌 빅테크의 기기용 수동소자(MLCC) 및 송배전망 기기(배전반) 쇼티지 발주 급증은 한국의 하이테크 밸류체인의 성장 가시성을 고도로 입증함.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)",
          "LS일렉트릭(010120)",
          "삼성전기(009150)"
        ],
        "insight": "AI 데이터센터 인프라와 배전반, 정밀 수동소자(MLCC)의 쇼티지가 2030년까지 장기화될 것이라는 확신에 기반하여 기업들이 사상 최대의 CapEx 경쟁을 시작함. SK하이닉스의 웨이퍼 생산량 2배 증설 결정은 HBM 단가를 현실화하는 동시에 싼값에 시장을 잠식하려는 <span class=\"text-cyan-300 font-semibold\">중국 CXMT 등 메모리사들의 진입 장벽</span>을 공고화하는 효과를 발휘할 것임.",
        "action_point": "미국 현지 데이터센터 건설 증가에 맞추어 설비를 6배로 확충한 <span class=\"text-cyan-300 font-semibold\">LS일렉트릭</span> 및 단가 3배 고부가가치 서버용 MLCC 계약 가시성이 열린 <span class=\"text-cyan-300 font-semibold\">삼성전기</span>를 최우선 편입하고, 용인 및 호남 클러스터 확장에 따른 전공정 소부장 장비 수혜주를 점진적으로 확대해야 함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["tech", "energy", "robot"],
        "tags": ["반도체클러스터", "최태원회장", "배전반증설", "서버용MLCC", "애플로비"]
      }
    }
  },
  "4uQY8yc09fY": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "4uQY8yc09fY",
        "title": "2026년 상반기 결산 | 월스트리트파인더ㅣ2026.6.29(월)",
        "published": "2026-06-29T00:26:27+00:00",
        "channel_name": "Smart Money by MiraeAsset ",
        "url": "https://www.youtube.com/watch?v=4uQY8yc09fY",
        "thumbnail": "https://img.youtube.com/vi/4uQY8yc09fY/hqdefault.jpg"
      },
      "analysis": {
        "summary": "2026년 상반기 글로벌 주요국 증시 중 코스피가 연초 대비 약 95% 상승하며 MVP를 기록하였고, 이는 주가 상승폭을 크게 초과한 <span class=\"text-amber-300 font-bold\">실적 및 EPS 개선(120% 폭증)</span>에 기반한 건강한 펀더멘탈 랠리임. 전체 시총 증가분의 90%를 반도체(삼성전자, SK하이닉스)가 견인하였고, 하이닉스는 역사상 최초로 시총 1위로 전환됨. 다만 시장 과열과 매매 쏠림으로 사이드카 29회, 서킷브레이커 5회(6월만 3회) 등 역사상 최다 시장 안정 조치가 발동됨.",
        "key_claims": [
          "한국 증시 상승은 버블이 아닌 D램 공급 부족 및 고단가 장기 공급 계약 체결로 확보된 <span class=\"text-cyan-300 font-semibold\">안전 마진(Forward PER 10배 미만)</span>에 근거한 결과임.",
          "금리 장기화 우려와 지수 7,000~8,000선 급등에 따른 스케일 효과로 리스크 프리미엄(V코스피)이 역사적 임계점에 도달했으나 평균 회귀 성향에 따라 하향 조정될 것임.",
          "상반기 반도체 대형주 중심의 랠리 쏠림으로 인해 코스닥 자금이 코스피로 이탈하는 <span class=\"text-rose-400 font-medium\">머니무브 현상</span>이 극대화되며 코스닥 상대 비율은 사상 최저 수준으로 추락함."
        ],
        "data_points": [
          "코스피 상반기 시가총액 증가: 연초 3,883조 원에서 7,590조 원으로 약 95% 폭증",
          "반도체 시총 증가 기여도: 3,200조 원 (전체 증가분의 90% 차지)",
          "밸류에이션 지표: LTM PER 25배 vs 선행 Forward PER 10배 미만 기록",
          "시장 안전 조치 횟수: 상반기 사이드카 29회 발동 (2008년 금융위기 당시 26회 상회)",
          "상반기 반도체 수출액: 1,900억 ~ 2,000억 달러 수준 (2000년 이래 역대 최대 규모)",
          "코스닥 대 코스피 상대 지수 비율: 0.1068로 30년 역사상 역대 최저 수준 기록"
        ],
        "signal": "bullish",
        "signal_reason": "상반기 코스피 수출 데이터와 기업의 EPS 상승폭이 연초 대비 120% 폭증하여 밸류에이션 매력이 탄탄하고, 반도체 공급 병목에 의한 수익성 하방 안정성이 굳건함.",
        "key_companies": [
          "SK하이닉스(000660)",
          "삼성전자(005930)",
          "SK(034730)",
          "SK스퀘어(402340)"
        ],
        "insight": "한국 증시는 HBM 및 인프라 쇼티지를 주무기로 사상 최대의 실적 서프라이즈를 달성했으나, 대형주 쏠림과 프로그램 매매 과열로 시장 안정화 장치가 금융위기 수준을 넘어 극도로 가동됨. 하반기는 급격한 가격 상승세가 둔화되고 이익 실현 속도에 주가가 안착하는 완만한 기간 조정 흐름을 보일 가능성이 높음.",
        "action_point": "지수 고밀도 성장에 따른 V코스피 변동성 고조를 감안해 포트폴리오의 과밀 투자는 피하고, 자사주 소각 등 주주환원 확대가 가시화되는 대형 지주사 및 지분법 수혜주(<span class=\"text-cyan-300 font-semibold\">SK, SK스퀘어</span>) 중심의 분할 진입 기회를 포착해야 함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["상반기결산", "시총1위역전", "V코스피", "코스닥상대지수", "반도체수출"]
      }
    }
  },
  "_uQAsHzWoKY": {
    "topic": "etc",
    "content": {
      "video": {
        "id": "_uQAsHzWoKY",
        "title": "[김정운의 소통의 심리학 4부] 한국인만 느끼는 억울함 바로 '이것' 때문이다 | 문화심리학자 김정운 박사",
        "published": "2026-06-28T11:55:25+00:00",
        "channel_name": "언더스탠딩_Understanding",
        "url": "https://www.youtube.com/watch?v=_uQAsHzWoKY",
        "thumbnail": "https://img.youtube.com/vi/_uQAsHzWoKY/hqdefault.jpg"
      },
      "analysis": {
        "summary": "한국인 특유의 정서인 '억울함'과 <span class=\"text-amber-300 font-bold\">MBTI·명품(하차감)</span> 등 존재 확인 수단에 비정상적으로 집착하는 현상을 문화심리학적 관점에서 설명함. 팬데믹 이후 관계 단절로 개인의 존재 불안이 심화되자 자기를 입증하기 위해 타인의 기준(테스트)에 의존하는 행태가 강화됨. 이에 반해 유럽 사회는 오랜 근대화를 통해 개인의 존재적 불안을 '취향(빌둥/산책자/방랑자)'이라는 성장의 계기로 극복하는 사회적 기술을 구축함.",
        "key_claims": [
          "한국인들이 팬데믹 이후 구글 검색에서 독보적으로 <span class=\"text-cyan-300 font-semibold\">MBTI</span>를 탐색한 배경에는 타인과의 단절에서 온 극심한 존재론적 불안감이 작용함.",
          "일제강점기와 한국전쟁으로 전통적 정체성 맥락이 리셋되자, 한국인들은 명함, 아파트 평수, 직급 등 계량화된 '입학 시험식 테스트'에 합격해야만 교양인으로 인정받는 강박에 갇힘.",
          "자신의 주체적 정체성이 타인(사회적 타자)의 평가에만 종속되어 입증에 실패할 때, 한국인 특유의 번역 불가능한 한(恨)의 정서인 <span class=\"text-rose-400 font-medium\">억울함</span>이 발현되며, 이것이 SNS를 통해 집단적 분노와 적대감으로 표출되기 쉬움."
        ],
        "data_points": [
          "한국의 MBTI 구글 검색 빈도: 타 국가 및 일본 대비 압도적인 1위 기록 (2019년 이후 폭증)",
          "독일의 방랑 기능공 전통: 제조업 표준 장인 인정을 받기 위해 3년 1일 동안 타 도시에서 의무 방랑 수행 습속"
        ],
        "signal": "neutral",
        "signal_reason": "문화심리학적인 인간 심리 구조 분석과 한국인들의 집단적 불안 극복 방안을 설명하는 내용으로, 비즈니스 및 금융 마케팅(취향/브랜딩)에 응용 가능한 중립적 인문학 관점임.",
        "key_companies": [],
        "insight": "한국인들은 외적 지표(명함, 차량 하차감)로만 존재를 증명하려 하기에 지위가 상실될 때(은퇴 등) 바보가 되는 극심한 정체성 박탈감을 느낌. 이에 반해 독일의 '방랑자(Wanderer)'를 통한 내면 성숙(Bildung), 프랑스의 '산책자(Flâneur)' 등 고유한 취향은 개인이 사회적 타자의 시선으로부터 자유롭게 <span class=\"text-cyan-300 font-semibold\">내면적 정체성</span>을 지탱하는 강력한 심리적 방어막으로 작동함.",
        "action_point": "사회적 테스트에 강박적으로 순응하거나 SNS 상의 집단 분노 및 적대감 조장에 휩쓸리기보다는, 자신만의 미적·도덕적 <span class=\"text-cyan-300 font-semibold\">주체적 취향(Bildung)</span>을 발굴하고 기계적인 내면 관리를 통해 정신적 리스크를 통제해야 함."
      },
      "classification": {
        "primary_topic": "etc",
        "secondary_topics": [],
        "tags": ["소통심리학", "억울함정서", "존재불안", "독일방랑자", "취향미학"]
      }
    }
  },
  "ACKpyyg6fRQ": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "ACKpyyg6fRQ",
        "title": "중간선거 앞두고 금리 인상?..워시의 작전은 | 강달러 도대체 언제까지 | 월가백브리핑",
        "published": "2026-06-28T03:00:34+00:00",
        "channel_name": "한경 글로벌마켓",
        "url": "https://www.youtube.com/watch?v=ACKpyyg6fRQ",
        "thumbnail": "https://img.youtube.com/vi/ACKpyyg6fRQ/hqdefault.jpg"
      },
      "analysis": {
        "summary": "반도체 공급 부족 및 칩 판가 인상으로 제품 가격이 전반적으로 상승하는 <span class=\"text-rose-400 font-medium\">칩플레이션(Chiplaytion)</span>이 도래하며 가계 물가 압박이 고조됨. 미국의 막대한 재정적자 지출과 스페이스X, 오라클 등 테크 기업들의 회사채 홍수로 인해 WTI 유가 급락에도 불구하고 채권 시장 금리가 높은 수준으로 제한되어 있음. 미국 대선을 앞두고 연준(Fed)의 구두 개입(Hawkish talk)을 통한 기대인플레 통제 시도가 이어지며 달러 초강세가 고착화됨.",
        "key_claims": [
          "미국의 강력한 재정지출이 지속되며 가계 소비 여력을 지탱하고 있으나, 국채 공급 폭증이 <span class=\"text-rose-400 font-medium\">채권 금리 상방 압력</span>으로 직결되고 있음.",
          "애플이 원자재 가격 부담을 빌미로 기기 가격을 대폭 인상함에 따라, IT 제조 대장주의 가격 인상을 신호탄으로 삼은 전방위 <span class=\"text-rose-400 font-medium\">칩플레이션 동참</span>이 확산될 우려가 제기됨.",
          "연준의 연내 실제 금리 인상 단행 여부는 미지수이나 대선 전까지 구두 개입(Oral Intervention)을 통해 채권 시장의 긴축 효과를 유도하는 책략을 지속할 것임."
        ],
        "data_points": [
          "기대 인플레이션: WTI 유가 배럴당 70달러선 붕괴 영향으로 2.5%에서 2.2%로 30bp 하락",
          "환율 및 채권: 원/달러 환율 1,540원선 도달 및 엔화 약세(162엔 돌파) 가속화"
        ],
        "signal": "bearish",
        "signal_reason": "회사채 공급 과잉과 미국의 강한 소비에 따른 채권 금리의 고공행진, 애플 주도의 서비스/기기 단가 인상 압박(칩플레이션), 그리고 고금리가 9월 대선 전까지 긴축적인 담론을 유지할 것이기 때문임.",
        "key_companies": [
          "스페이스X",
          "애플",
          "오픈AI"
        ],
        "insight": "AI 투자를 위한 테크 기업들의 사상 최대 채권 발행이 채권 시장의 수급 소화 불량을 초래하고 있으며, 이는 금리 하락을 억제하는 실질적 복병이 됨. 대장주인 <span class=\"text-cyan-300 font-semibold\">애플</span>의 9월 신제품 가격 20~30% 인상 예측은 가뜩이나 끈적한 코어 인플레이션에 기름을 붓는 촉매가 될 것이며, 이로 인해 달러 초강세(원화 약세) 장기화 리스크가 가중됨.",
        "action_point": "달러 강세 및 고금리 장기화 기조에 대비해 현금 창출 능력이 보장된 미국 고부가 제조 인프라 기업 중심의 보수적 배분을 고수하고, 금리 변동성에 취약한 고멀티플 레버리지 자산에 대한 노출은 일부 축소해야 함."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock"],
        "tags": ["칩플레이션", "연준구두개입", "회사채공급", "달러강세", "미국대선금리"]
      }
    }
  }
}

# Write and clean up
pending_dir = Path("data/pending")
analyzed_base_dir = Path("data/analyzed")

for video_id, info in batch1_data.items():
    topic = info["topic"]
    content = info["content"]
    
    topic_dir = analyzed_base_dir / topic
    topic_dir.mkdir(parents=True, exist_ok=True)
    analyzed_path = topic_dir / f"{video_id}.json"
    analyzed_path.write_text(json.dumps(content, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved: {analyzed_path}")
    
    pending_path = pending_dir / f"{video_id}.json"
    if pending_path.exists():
        pending_path.unlink()
        print(f"Deleted pending: {pending_path}")
