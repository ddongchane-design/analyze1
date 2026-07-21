import json
from pathlib import Path

# Define the analyzed data for Batch 1
batch_data = {
  "-0qO3WVXFe0": {
    "topic": "space",
    "content": {
      "video": {
        "id": "-0qO3WVXFe0",
        "title": "[LIVE] 자국 월드컵도 외면하는 미국인…SpaceX엔 450조가 몰렸다 | 이나연 특파원",
        "published": "2026-06-10T21:47:31+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=-0qO3WVXFe0",
        "thumbnail": "https://img.youtube.com/vi/-0qO3WVXFe0/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 5월 미국 CPI가 에너지 가격 급등 영향으로 전년 대비 4.2% 상승하며 3년 만에 최고치를 기록했으나, 근원 CPI는 안정세를 유지하며 <span class=\"text-amber-300 font-bold\">소비 둔화 조짐</span>을 나타냈습니다.\n2. 미국 내 개최되는 월드컵에 대한 자국 소비자의 관심이 매우 낮아 티켓 가격 부담 등으로 기업들이 가이던스에서 월드컵 효과를 제외하고 있습니다.\n3. 6월 12일 상장하는 <span class=\"text-cyan-300 font-semibold\">스페이스X(SpaceX)</span>의 IPO 공모에 물량의 4배가 넘는 450조 원 이상의 기관 주문이 대거 몰리며 역사적 상장을 예고했습니다.",
        "key_claims": [
          "미국 인플레이션은 이란 전쟁에 따른 <span class=\"text-amber-300 font-bold\">유가 급등</span>과 소비 한계가 억제하는 상반된 흐름을 보이고 있습니다.",
          "백화점과 에어비앤비 등 현지 소비 지표에서 월드컵 기대로 선반영된 물가에 비해 <span class=\"text-rose-400 font-medium\">실제 소비 수요는 위축</span>되는 양상입니다.",
          "스페이스X는 135달러 단일 고정가 방식을 채택해 기관 초과 주문 수요가 상장 후 <span class=\"text-cyan-300 font-semibold\">강력한 매수 대기 자금</span>으로 작용할 예정입니다."
        ],
        "data_points": [
          "5월 CPI 전년 대비 4.2% 상승 (3년 만에 최고치)",
          "휘발유 가격 5월 말 갤런당 4.56달러 돌파 (4년 만에 최고치)",
          "시간당 실질 소득 전년 대비 0.7% 하락 (3년 만에 최대 하락폭)",
          "스페이스X 공모가 주당 135달러 단일 고정가, 공모 물량 5억 5,560만 주, 조달 금액 약 750억 달러",
          "스페이스X 청약 자금 공모 물량의 4배 이상(약 3,000억 달러, 450조 원 이상) 돌파",
          "스페이스X 상장 시가총액 약 1조 8,000억 달러(약 2,738조 원) 수준 전망"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "스페이스X IPO에 전례 없는 450조 원 이상의 자금이 유입되어 <span class=\"text-cyan-300 font-semibold\">우주산업 섹터</span> 전반에 강력한 호재 및 활성화 시그널을 제공합니다.",
        "key_companies": [
          "스페이스X",
          "테슬라(TSLA)",
          "쉐이크쉑(SHAK)",
          "코카콜라(KO)",
          "나이키(NKE)"
        ],
        "insight": "스페이스X의 1조 8,000억 달러 시총 규모 상장은 가격 범위를 올리지 않는 고정가 공모 방식을 활용하여 3,000억 달러 규모의 <span class=\"text-cyan-300 font-semibold\">기관 대기 수급</span>을 만들어 냈습니다. 이는 상장 첫날 극단적 변동성을 초래할 가능성이 있으나 중장기적으로 우주 인터넷 및 민간 우주 인프라 섹터의 성장을 견인할 것입니다.",
        "action_point": "개인 배정 비율(30%)이 높아 첫날 락업 해제 물량 등으로 인한 <span class=\"text-rose-400 font-medium\">단기 변동성 리스크</span>에 유의하며, 스페이스X 상장 이후 우주 섹터 전반의 밸류에이션 재평가 흐름을 주시해야 합니다."
      },
      "classification": {
        "primary_topic": "space",
        "relevance_score": 9.5
      }
    }
  },
  "23cy_CJsfZ8": {
    "topic": "tech",
    "content": {
      "video": {
        "id": "23cy_CJsfZ8",
        "title": "45년 윈텔 시대는 가고 '윈비디아'가 온다 | 김인엽의 실리콘밸리나우",
        "published": "2026-06-10T10:00:40+00:00",
        "channel_name": "한경 글로벌마켓",
        "url": "https://www.youtube.com/watch?v=23cy_CJsfZ8",
        "thumbnail": "https://img.youtube.com/vi/23cy_CJsfZ8/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 마이크로소프트는 빌드 2026에서 엔비디아의 AI 반도체를 탑재한 초소형 개발자용 데스크톱 <span class=\"text-cyan-300 font-semibold\">서피스 RTX 스파크 데브박스</span>를 공개하며 애플의 맥미니와 본격 대결을 선언했습니다.\n2. AI 에이전트 구동 시 개인정보 유출 및 파일 무단 삭제 등 안전성 위협을 막기 위해 윈도우 OS 단에서 보호하는 <span class=\"text-cyan-300 font-semibold\">보안 컨테이너(MXC)</span> 기술을 구현했습니다.\n3. 데이터 센터의 극심한 전력 및 물 공급 부족 병목현상을 해소하기 위해 경량 AI 모델 <span class=\"text-cyan-300 font-semibold\">아이온(Ion) 1.0</span>을 출시하고 기기 내 온디바이스 AI 비중을 극대화하고 있습니다.",
        "key_claims": [
          "데이터 센터의 물리적 확장 한계와 <span class=\"text-amber-300 font-bold\">전력망 부족 병목</span>을 극복하기 위해 온디바이스 AIPC로의 분산 연산 처리는 필연적인 흐름입니다.",
          "MS와 엔비디아가 주축이 된 <span class=\"text-cyan-300 font-semibold\">'윈비디아' 동맹</span>은 애플의 온디바이스 에이전트 시장 독점을 견제하고 40년 PC 패러다임을 바꿀 것입니다.",
          "안전 장치인 MXC 컨테이너의 도입으로 그동안 보안 우려로 미뤄졌던 기업들의 <span class=\"text-cyan-300 font-semibold\">AI 에이전트 솔루션</span> 도입이 본격화될 전망입니다."
        ],
        "data_points": [
          "개발자용 AIPC '서피스 RTX 스파크 데브 박스' 공개 (RTX GPU 탑재, 최대 1페타플롭스 연산 속도)",
          "20코어 CPU 및 118GB 통합 메모리 탑재",
          "자체 경량 AI 모델 '아이온 1.0'(Ion 1.0) 출시 (요약용 Instruct 모델 및 1,450억 파라미터 기반 Plan 모델 2종)",
          "미래형 분산 디바이스 프로젝트 '솔라라(Solara)' 공개"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "엔비디아의 하드웨어와 마이크로소프트의 소프트웨어 시너지를 활용한 초고성능 온디바이스 AIPC 생태계가 실체화되면서 반도체 및 AI 시장에 강력한 활력을 불어넣고 있습니다.",
        "key_companies": [
          "마이크로소프트(MSFT)",
          "엔비디아(NVDA)",
          "애플(AAPL)",
          "인텔(INTC)",
          "퀄컴(QCOM)"
        ],
        "insight": "AI 에이전트 활성화에 따른 토큰 비용 급증과 <span class=\"text-rose-400 font-medium\">서버 인프라 전력 부족 리스크</span>는 빅테크가 온디바이스 소형 경량 언어모델(SLM)에 강력한 공세를 가하는 핵심 요인입니다. 이번 협력은 오랜 PC 파트너십 구도(윈텔)를 허물고 인공지능 기반 <span class=\"text-cyan-300 font-semibold\">엔비디아-MS 독점 체제</span>를 다지는 계기가 될 것입니다.",
        "action_point": "온디바이스 하드웨어에 필수적인 고성능 통합 메모리 및 초고속 연산 칩 부품 공급망을 선점한 반도체 밸류체인과 고화질 작업 툴(Blender, Solidworks 등) 및 <span class=\"text-cyan-300 font-semibold\">AI 에이전트 인프라 기업</span>들의 중장기 성장 수혜를 눈여겨보아야 합니다."
      },
      "classification": {
        "primary_topic": "tech",
        "relevance_score": 9.8
      }
    }
  },
  "a-A6tmNBPBI": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "a-A6tmNBPBI",
        "title": "모델Y 국내 판매 1위에 머스크 '엄지척'…\"중국산 전기차 몰려온다” | 류종은 삼프로TV 기자 [뉴스3]",
        "published": "2026-06-10T23:18:44+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=a-A6tmNBPBI",
        "thumbnail": "https://img.youtube.com/vi/a-A6tmNBPBI/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 삼성전자가 미국 DNA 시퀀싱 정밀 유전체 전문기업 <span class=\"text-cyan-300 font-semibold\">엘리먼트 바이오사이언스</span>에 2,667억 원을 투자해 1대 주주로 등극하며 개인 맞춤형 바이오·헬스케어 사업 확장을 가속화합니다.\n2. 지난달 국내 자동차 시장에서 중국 상하이 공장 제조분 수입 모델Y가 8,000대 이상 팔려 수입차 1위를 기록했으나, 테슬라는 유럽 시장 판매량 급감 및 중국 내 경쟁 심화 문제를 겪고 있습니다.\n3. 원화 약세(원/달러 환율 1,540원선 돌파) 영향으로 외국인 관광객들의 국내 명품 및 백화점 소비가 폭발적으로 급증하여 백화점 3사 주가가 3월 대비 거의 두 배 가까이 급등했습니다.",
        "key_claims": [
          "삼성이 확보한 고정밀 DNA 시퀀싱 기술은 웨어러블 디바이스와 융합되어 스마트폰을 잇는 미래 <span class=\"text-cyan-300 font-semibold\">초개인화 헬스케어 엔진</span>의 핵심 축이 될 것입니다.",
          "글로벌 판매 둔화에도 불구하고 한국에서 중국산 테슬라 전기차가 큰 인기를 끄는 등 국내 완성차 시장에서 <span class=\"text-rose-400 font-medium\">내수 업체들의 입지 타격</span>이 가속화되고 있습니다.",
          "백화점은 단순한 내수 업종에서 원화 약세 수혜를 누리는 <span class=\"text-amber-300 font-bold\">수출급 외화 획득 수단</span>으로 체질 개선 및 재평가가 진행 중입니다."
        ],
        "data_points": [
          "삼성전자 엘리먼트 바이오사이언스에 1억 7,500만 달러(약 2,667억 원) 투자, 약 20% 지분 확보로 1대 주주 등극",
          "글로벌 정밀의료 시장 규모: 2025년 125조 원에서 2034년 407조 원으로 3배 이상 성장 전망",
          "테슬라 모델Y 지난달 국내 판매량 8,000대 이상 기록하여 수입 및 국산차 포함 전체 1위 달성",
          "국내 판매 테슬라 중 76%가 중국 상하이 기기 제조 수입산이며 전체 브랜드 수입 비중의 94% 차지",
          "5월 현대차 국내 내수 판매량 전년 동기 대비 23% 급감",
          "1~5월 백화점/아울렛 카드 누적 결제액 19조 2,700억 원 기록(전년 동기 대비 11.2% 증가)",
          "Q1 신세계백화점 본점 내 외국인 결제액 전년 동기 대비 98% 급증"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "대기업의 신규 바이오 포트폴리오 확보 및 원화 약세에 따른 유통·내수 대형주들의 외화 수혜 모멘텀이 증명되어 중장기적으로 주가 반등 요인으로 작용합니다.",
        "key_companies": [
          "삼성전자(005930)",
          "테슬라(TSLA)",
          "신세계(004170)",
          "현대백화점(069960)",
          "롯데쇼핑(023530)",
          "현대자동차(005380)"
        ],
        "insight": "삼성의 바이오 플랫폼 및 웨어러블 연동 전략은 디바이스 마진 둔화를 예방하려는 장기 포석이며, 신세계·현대·롯데 백화점의 신고가 랠리는 환율 효과가 극대화된 <span class=\"text-amber-300 font-bold\">인바운드 쇼핑 급증</span>에 기인합니다. 이는 매크로 변동성 장세에서 견고한 대안 투자처로 기능하고 있음을 시사합니다.",
        "action_point": "삼성이 주도하는 고기능 헬스케어 센서 밸류체인과 환율 약세 수혜가 이어지는 <span class=\"text-cyan-300 font-semibold\">명품 판매 대형 유통주</span>의 단기 모멘텀에 올라타되, 파업 및 내수 침체 리스크가 있는 완성차 제조업종에는 보수적으로 접근해야 합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.2
      }
    }
  },
  "azGfwU9tgyY": {
    "topic": "etc",
    "content": {
      "video": {
        "id": "azGfwU9tgyY",
        "title": "빛이 위에서 오는 게 아니었다고? 지금까지 착각하고 있던 빛의 과학",
        "published": "2026-06-10T11:00:02+00:00",
        "channel_name": "안될과학 Unrealscience",
        "url": "https://www.youtube.com/watch?v=azGfwU9tgyY",
        "thumbnail": "https://img.youtube.com/vi/azGfwU9tgyY/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 런던 조명 디자이너 안효영 대표를 초청하여 무대 조명의 원리와 신경미학을 바탕으로 빛이 인간의 시선 및 감정에 미치는 깊은 영향력을 탐색했습니다.\n2. 인류가 오랫동안 태양광에 노출되면서 형성된 '빛은 위에서 온다'는 편견으로 인해 발생하는 오목·볼록 입체 착시(크레이터 일루션) 현상을 설명했습니다.\n3. 아침에 잠을 깨우는 480nm 영역의 청록빛 반응 신경세포(IPRGC)와 저녁 휴식을 돕는 노란빛의 생물학적 작용을 규명하고 기술 변화와 디자이너의 전망을 다뤘습니다.",
        "key_claims": [
          "빛의 각도와 음영 패턴은 동일한 인물의 얼굴이라도 감정 상태를 완전히 다르게 왜곡하여 인지하게 만드는 <span class=\"text-amber-300 font-bold\">신경미학적 힘</span>을 지닙니다.",
          "눈의 시각 정보 처리 기능과 별개로 멜라토닌 분비와 <span class=\"text-cyan-300 font-semibold\">인체 생체 리듬</span>에 직접적인 각성을 유도하는 IPRGC 신경절 세포의 생리학적 중요성이 강조됩니다.",
          "LED 시대의 도래로 에너지 효율성은 향상되었으나 단파장 조합에 의한 연색성(CRI) 하락 및 <span class=\"text-rose-400 font-medium\">아날로그 감성 훼손</span>은 여전한 과제로 꼽힙니다."
        ],
        "data_points": [
          "인체 생체 리듬 및 각성에 기여하는 망막 신경절 세포 IPRGC 발견",
          "IPRGC가 가장 민감하게 반응하는 파장 대역 480nm (청록색 계열)",
          "자연 태양광과 유사한 스펙트럼 재현 정도를 나타내는 CRI 지수 (최고치 100 기준 텅스텐 전구가 근접)"
        ],
        "signal": "na",
        "signal_confidence": "high",
        "signal_reason": "이 영상은 순수 과학 및 일상 기술 지식을 다루는 인터뷰 콘텐츠로, 직접적인 금융 투자 정보나 기업 분석 목적에 적합하지 않습니다.",
        "key_companies": [],
        "insight": "빛에 대한 인간의 인지는 생체 시계 학습 및 진화론적 요인에 의해 지배받습니다. 조명 기술은 백열전구에서 LED로 급진적으로 이전하며 소형화 및 빠른 색변환 등 스마트 연출을 촉진하고 있으나, 자연 그대로의 연색성을 완벽히 구현하는 데는 한계가 있어 <span class=\"text-cyan-300 font-semibold\">정밀 스펙트럼 튜닝 솔루션</span>에 대한 수요가 점차 증가할 것입니다.",
        "action_point": "순수 과학 교양 자료로 참고하되, 스마트 헬스케어 디바이스 내 수면 및 각성 유도 라이팅 기술과 온디바이스 생체 센싱 조명 칩을 양산하는 <span class=\"text-cyan-300 font-semibold\">차세대 LED 스펙트럼 관련 부품 기업</span>의 동향을 장기적으로 점검하는 용도로 활용할 수 있습니다."
      },
      "classification": {
        "primary_topic": "etc",
        "relevance_score": 5.0
      }
    }
  },
  "b5f1Ld5teYo": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "b5f1Ld5teYo",
        "title": "폭락장에도 강한 종목은 있다. 문제는 매수 타이밍입니다ㅣ명민준, 강아랑, 이권희 [주린이 구조대]",
        "published": "2026-06-10T12:30:26+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=b5f1Ld5teYo",
        "thumbnail": "https://img.youtube.com/vi/b5f1Ld5teYo/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 극심한 시장 변동성(사이드카/서킷 브레이커 연속 발생)과 단기 급락은 그동안 코스피의 과도한 오버페이스에 따른 자연스러운 <span class=\"text-amber-300 font-bold\">이격도 좁히기(기간 조정)</span> 국면으로 분석됩니다.\n2. 미국 빅테크 기술주 하락의 실질적 원인은 금리 우려뿐 아니라 초대형 스페이스X IPO 청약을 앞두고 기관 투자자들이 현금을 확보하고자 <span class=\"text-cyan-300 font-semibold\">반도체 주식 비중을 강제로 축소</span>하고 있기 때문입니다.\n3. 지수 손절선은 갭 상승 구간이자 60일 이동평균선과 인접한 6,936선이며, 하방 경직성을 지지하는 핵심 지표는 빅테크 기업들의 AI 투자 대비 실질적 <span class=\"text-amber-300 font-bold\">이익 창출 능력(Monetization)</span>입니다.",
        "key_claims": [
          "국내 증시의 극단적 변동성은 글로벌 반도체 및 미국 시총 상위주들의 수급 조절에 과하게 예민하게 연쇄 반응하는 <span class=\"text-rose-400 font-medium\">한국 시장의 규모 한계</span> 때문입니다.",
          "기관 수급 블랙홀로 떠오른 스페이스X의 450조 원 규모 청약 자금 쏠림은 기존 주식시장의 단기 <span class=\"text-rose-400 font-medium\">유동성 일시 흡수 원인</span>으로 작용합니다.",
          "지수 자체의 밸류에이션(삼성전자, SK하이닉스 등)이 4~5배 수준으로 낮기 때문에 구조적 버블 붕괴 국면이 아닌 <span class=\"text-cyan-300 font-semibold\">매수 관점의 하방 지지</span>가 유효합니다."
        ],
        "data_points": [
          "코스피 5월 4일 종가 6,936선 (과거 갭 구간 및 향후 강력한 기술적 데드라인/손절선)",
          "삼성전자 및 SK하이닉스의 현지 PER 밸류에이션이 5배 수준까지 하락 조정",
          "미국 빅테크의 AI 설비투자(CapEx) 회수 지표로 구글 어닝 서프라이즈 및 앤스로픽 흑자 전환 지표 언급"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "단기 급락은 밸류에이션 버블이 아닌 일시적인 수급 이벤트(스페이스X IPO 대비 현금화)와 이격도 조절 과정에 불과하므로 펀더멘탈 대비 주가가 현저히 저평가되는 <span class=\"text-cyan-300 font-semibold\">과매수 해소 기회</span>로 작용합니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)",
          "네이버(035420)",
          "스페이스X",
          "마이크론(MU)"
        ],
        "insight": "주식 시장의 밸류에이션은 15배 수준에 달해야 버블 경고가 유의미하나, 현재 삼성전자 및 하이닉스는 실적 대비 한 자릿수 PER에 머물고 있습니다. 미국 빅테크의 AI 투자 수익성 훼손이 증명되지 않는 한, 금리 경계감과 수급 쏠림으로 인한 급락은 장기적 관점에서 <span class=\"text-cyan-300 font-semibold\">매력적인 진입 가격</span>을 제시합니다.",
        "action_point": "단기 변동성에 일희일비하기보다는 FMC 및 마이크론/삼성전자 실적 발표 등 다가오는 7월 어닝 시즌까지 호흡을 길게 잡고, SK하이닉스 200만 원 이하 및 삼성전자 30만 원 이하 수준에서 <span class=\"text-cyan-300 font-semibold\">대표 대형주 비중 확대</span> 기회로 삼아야 합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.6
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
