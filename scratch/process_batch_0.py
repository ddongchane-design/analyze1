import json
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scratch.batch_save import save_batch

batch_0 = [
  {
    "video": {
      "id": "-B26rsrjD08",
      "title": "후배 삐질까봐 작전 강행, 일본군 10만명 몰살당했다 | 북언더스탠딩 | 일본 제국은 왜 실패하였는가? | 비즈니스 칼럼니스트 박소령",
      "published": "2026-08-12T12:25:31+00:00",
      "channel_name": "언더스탠딩_Understanding",
      "url": "https://www.youtube.com/watch?v=-B26rsrjD08",
      "thumbnail": "https://img.youtube.com/vi/-B26rsrjD08/hqdefault.jpg"
    },
    "analysis": {
      "summary": "일본 제국의 실패 원인을 경영학 관점에서 파고든 서적 《실패의 본질》을 다루며, 모호한 목적, 과도한 낙관론과 <span class=\"text-rose-400 font-medium\">컨틴전시 플랜(플랜 B)의 부재</span>, 경직된 조직 문화가 초래한 조직적 참사를 조명함. 힘센 경쟁자가 존재하는 상황이나 불확실한 시장 환경에서 기업 리더십이 <span class=\"text-amber-300 font-bold\">목표의 명확화</span>와 손절 라인(시나리오 플래닝)을 사전에 설정해야만 멸망을 피할 수 있음을 강조함.",
      "key_claims": [
        "목적과 전략이 애매하고 추상적이면 하위 조직 간 커뮤니케이션 혼선과 실패를 초래함.",
        "최악의 시나리오와 손절 기준(컨틴전시 플랜) 없이 무조건적 정신력과 단기전에 올인하는 것은 조직을 파멸로 이끎.",
        "리더와 핵심 인재 간 투명한 의사 결정 공유와 유연한 체계 구축이 불확실성 시기의 핵심임."
      ],
      "data_points": [
        "일본 태평양 전쟁 6대 전투 분석 사례 소개 (미드웨이, 과달카날, 인팔 작전 등)"
      ],
      "signal": "neutral",
      "signal_reason": "경영학적 실패 사례 분석 및 리스크 관리를 통한 조직 체질 개선 및 의사결정 프로세스 검토를 제안함.",
      "key_companies": ["청기화타운", "언더스탠딩", "도쿄증권거래소"],
      "insight": "승자의 과거 성공 경험(과거의 이긴 경험)에 얽매여 환경 변화와 리스크 시나리오를 배제한 채 올인하는 조직은 거시 환경 변동에 가장 취약함.",
      "action_point": "신규 사업 추진 및 투자 시 최악의 경우를 대비한 <span class=\"text-rose-400 font-medium\">손절매 라인과 플랜 B</span>를 사전에 수립하고 명확한 1순위 목적에 자원을 집중할 것."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["경영학", "실패의본질", "조직관리", "손절라인", "컨틴전시플랜"]
    }
  },
  {
    "video": {
      "id": "12eGAYc3BO4",
      "title": "삼성전자 휴머노이드 첫 시연, 왜 경영진에게만 공개했을까?",
      "published": "2026-08-11T10:17:02+00:00",
      "channel_name": "엔지니어TV",
      "url": "https://www.youtube.com/watch?v=12eGAYc3BO4",
      "thumbnail": "https://img.youtube.com/vi/12eGAYc3BO4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">삼성전자</span>가 RX 부문 R&D 캠퍼스에서 개발 중인 휴머노이드 로봇의 첫 시연을 경영진 대상으로 비밀리에 진행함. 카메라 비전 기반 실시간 센싱, 초소형 모듈형 <span class=\"text-cyan-300 font-semibold\">액추에이터</span> 및 센서 기술이 대거 적용되었으며, 내부 테스트 완료 후 외부 공개 시기를 조율 중인 <span class=\"text-amber-300 font-bold\">피지컬 AI</span> 전략의 일환으로 풀이됨.",
      "key_claims": [
        "삼성전자가 경영진 대상 비밀 시연을 진행하며 차세대 휴머노이드 상용화 단계 진입을 시사함.",
        "액추에이터, 카메라 센싱, 배터리 등 핵심 로봇 부품을 계열사(삼성SDI 등)와 연계하여 자체 내재화 추진."
      ],
      "data_points": [
        "시연 장소: 삼성전자 RX 부문 R&D 캠퍼스"
      ],
      "signal": "bullish",
      "signal_reason": "삼성전자의 휴머노이드 로봇 기술 시연으로 피지컬 AI 및 대기업 주도의 로봇 생태계 확장 기대감이 한층 높아짐.",
      "key_companies": ["삼성전자(005930)", "삼성SDI(006400)", "1X Technologies", "OpenAI"],
      "insight": "빅테크와 국내 제조 대기업의 피지컬 AI 경쟁이 가속화되면서 핵심 모션 기술인 액추에이터와 정밀 카메라 밸류체인의 가치가 급상승함.",
      "action_point": "삼성전자의 로봇 공급망 진입이 유력한 domestic 액추에이터 및 정밀 센서 관련주의 실적 모멘텀을 주시할 것."
    },
    "classification": {
      "primary_topic": "robot",
      "secondary_topics": ["tech", "stock"],
      "tags": ["삼성전자휴머노이드", "피지컬AI", "액추에이터", "카메라비전", "로봇시연"]
    }
  },
  {
    "video": {
      "id": "1ukZmekLSGg",
      "title": "구구단보다 도형 곱셈법부터 배우는 중국 아이들",
      "published": "2026-08-12T07:05:42+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=1ukZmekLSGg",
      "thumbnail": "https://img.youtube.com/vi/1ukZmekLSGg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "중국의 기초 교육 과정에서 구구단 암기 대신 도형 선긋기를 통한 <span class=\"text-cyan-300 font-semibold\">기하학적 곱셈법</span>을 도입하여 직관적인 수리 사고력을 키우는 교육 방식을 소개함. 단순 암기 위주 교육에서 벗어나 인공지능 시대에 필요한 <span class=\"text-amber-300 font-bold\">시각적 사고(Visual Thinking)</span>와 알고리즘적 문제 해결력을 기르는 데 집중하고 있음.",
      "key_claims": [
        "수치 암기가 아닌 선과 교점을 이용한 시각적 곱셈법으로 직관적 사고 훈련.",
        "AI 시대를 대비한 수리적 사고 체계의 체질 개선 시도."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "교육 방식 및 인재 양성 트렌드 소개 영상으로 시장 시그널은 중립적임.",
      "key_companies": [],
      "insight": "AI 및 테크 인재 확보를 위한 기초 학문 교육 패러다임이 단순 암기에서 직관적 알고리즘 이해로 전환되고 있음.",
      "action_point": "글로벌 AI 인재 육성을 위한 교육 테크 솔루션 및 창의 교육 관련 트렌드 파악."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["etc"],
      "tags": ["도형곱셈법", "중국교육", "수리사고력", "시각적사고", "AI교육"]
    }
  },
  {
    "video": {
      "id": "5wJyoYznBWk",
      "title": "시작부터 만기까지, 중개형ISA 한편으로 끝내기!",
      "published": "2026-08-12T01:00:02+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=5wJyoYznBWk",
      "thumbnail": "https://img.youtube.com/vi/5wJyoYznBWk/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">중개형 ISA</span> 계좌의 납입한도 이월 제도, 주식·ETF·채권 등 다양한 자산에 대한 <span class=\"text-amber-300 font-bold\">다각화 투자(자산배분)</span> 혜택, 그리고 3년 만기 후 연금계좌 이전 시 추가 세액공제 활용법을 다룸. 절세 및 투자 효율성을 극대화하기 위해 하루라도 일찍 가입해 한도를 축적하고 만기 자금을 연금으로 전환하는 순환 전략을 제시함.",
      "key_claims": [
        "ISA 계좌는 매년 2천만 원씩 납입한도가 누적 이월되므로 조기 가입이 유리함.",
        "단일 주식 몰빵 대신 주식, 채권, 리츠 등 다변화 자산배분으로 변동성 장세에 대응 가능.",
        "만기 자금을 60일 이내 연금계좌로 전환 시 최대 10% 추가 세액공제 혜택 부여."
      ],
      "data_points": [
        "ISA 연간 납입한도: 매년 2,000만 원 (최대 1억 원까지 이월 축적 가능)",
        "연금 전환 시 세액공제: 이전 금액의 10% (최대 300만 원 한도)"
      ],
      "signal": "bullish",
      "signal_reason": "절세 혜택 및 장기 연금 전환 혜택을 통한 개인 투자자들의 자산 형성 가이드로서 유용함.",
      "key_companies": ["미래에셋증권"],
      "insight": "고금리·고물가 시대에 단순 예적금을 넘어 절세 계좌(ISA)를 기반으로 한 복리 및 자산 배분 전략이 자산가치의 핵심 보루임.",
      "action_point": "ISA 계좌를 미개설했다면 즉시 개설하여 연간 납입한도를 확보하고, 만기 시 연금저축/IRP 이전 혜택을 적극 활용할 것."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["중개형ISA", "절세혜택", "자산배분", "연금전환", "세액공제"]
    }
  },
  {
    "video": {
      "id": "8x5zrRG4kus",
      "title": "지지율 30%대 폭락한 트럼프 민주당도 못 웃는 이유 #교양이를부탁해 #미국중간선거 #트럼프 #미국정치",
      "published": "2026-08-12T11:45:20+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=8x5zrRG4kus",
      "thumbnail": "https://img.youtube.com/vi/8x5zrRG4kus/hqdefault.jpg"
    },
    "analysis": {
      "summary": "트럼프 전 대통령의 지지율이 30%대로 하락했음에도 불구하고, 민주당 내 <span class=\"text-rose-400 font-medium\">강경 좌파 세력 확산</span>과 기성 정치인에 대한 유권자 반발로 인해 민주당이 반사이익을 얻지 못하는 미국 정국의 <span class=\"text-violet-300 font-medium\">정치적 양극화</span> 상황을 분석함. 중간선거를 앞두고 양당 모두 확고한 주도권을 잡지 못하면서 정책 불확실성이 지속되고 있음.",
      "key_claims": [
        "트럼프의 정치적 실책에도 민주당 지도부 및 기성 의원들의 지지율 회복 부진.",
        "민주당 내부의 강경 좌파 득세로 중앙 중도파 유권자 이탈 가능성 부각.",
        "미국 중간선거를 앞둔 지정학 및 거시 정책 불확실성 지속."
      ],
      "data_points": [
        "트럼프 지지율: 30%대 기록"
      ],
      "signal": "neutral",
      "signal_reason": "미국 정국의 정치적 불확실성과 양극화 노이즈가 금융 시장에 관망세를 형성함.",
      "key_companies": [],
      "insight": "선거를 앞둔 미국의 정치적 내홍과 극단화는 거시 경제 정책(관세, 세제, 규제)의 예측 가능성을 떨어뜨리는 리스크 요인임.",
      "action_point": "미국 중간선거 국면에서의 관세 정책 및 입법 불확실성에 대비하여 기술주 및 정책 민감주의 비중 조절 필요."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": ["economy"],
      "tags": ["미국중간선거", "트럼프지지율", "미국정치", "양극화", "정책불확실성"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_0)
    print(f"Processed batch 0: {n} items saved.")
