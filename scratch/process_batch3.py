import json
from pathlib import Path

# Define the analyzed data for Batch 3
batch_data = {
  "gKc4ZH2rjFk": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "gKc4ZH2rjFk",
        "title": "[26.06.10 오후 방송 전체보기] 역대급 반등 하루만에 급락...'널뛰기' 국내 증시, 반대매매 쏟아진다 [클로징벨 라이브]",
        "published": "2026-06-10T06:50:21+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=gKc4ZH2rjFk",
        "thumbnail": "https://img.youtube.com/vi/gKc4ZH2rjFk/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 국내 증시는 전날의 급등세를 하루 만에 반납하며 코스피가 4.5% 폭락(7,730선)하는 등 극단적인 <span class=\"text-rose-400 font-medium\">롤러코스터 장세</span>를 이어갔습니다.\n2. 옵션 만기일을 앞두고 외국인과 기관이 5조 8,000억 원 이상의 기록적인 동반 매도세를 쏟아냈으며, 고환율(1,525원선) 여파로 <span class=\"text-rose-400 font-medium\">반대매매 및 미수 정리 압박</span>이 가중되고 있습니다.\n3. 시장 전반의 급락세 속에서도 반도체 소부장 대장주인 PSK홀딩스(11% 급등) 및 일부 전력기기 관련주는 바닥에서 강한 반등을 나타내며 차별화에 성공했습니다.",
        "key_claims": [
          "외국인과 기관의 기록적 매도 폭탄은 단기 수급 불균형과 옵션 만기를 대비한 <span class=\"text-rose-400 font-medium\">선물 변동성 플레이</span>에 따른 것입니다.",
          "미수 거래 만기 도래와 주가 하락이 맞물리면서 기계적인 <span class=\"text-rose-400 font-medium\">미수 반대매매 매물</span>이 쏟아져 나와 시장 하락폭을 키우고 있습니다.",
          "지수 폭락에도 이익 성장이 확실한 반도체 소부장과 전력기기 업종의 하방 지지력이 확인되어 <span class=\"text-cyan-300 font-semibold\">실적주 위주의 수급 쏠림</span>이 강해지고 있습니다."
        ],
        "data_points": [
          "코스피 지수 4.5% 급락 (7,730포인트로 밀림)",
          "코스닥 지수 1.6% 하락 (952선 마감)",
          "코스피 시장 외국인 및 기관 순매도 합계: 약 5조 8,000억 원 돌파 (개인 매수가 흡수)",
          "원/달러 환율 1,525원대 돌파로 외화 유출 및 환차손 우려 증가",
          "반도체 소부장 대장주 PSK홀딩스 당일 약 11% 급등 마감"
        ],
        "signal": "bearish",
        "signal_confidence": "high",
        "signal_reason": "외국인·기관의 5조 8,000억 원대 패닉셀과 고환율에 따른 미수 반대매매 공포가 맞물려 단기 시장 수급 환경이 극도로 악화된 상태입니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)",
          "PSK홀딩스(037950)",
          "유진테크(084370)"
        ],
        "insight": "옵션 만기일과 지정학 불안이 겹친 국내 증시는 펀더멘탈 요인이 아닌 <span class=\"text-rose-400 font-medium\">기계적 반대매매(미수 상환)</span>로 인해 변동성이 과장되었습니다. 다만 지수가 급락함에 따라 밸류에이션 매력이 극대화되어 외국인의 선물 환매수 전환 여부가 단기 반등의 열쇠가 될 것입니다.",
        "action_point": "미수 및 신용 신규 진입을 철저히 금지하여 <span class=\"text-rose-400 font-medium\">반대매매 위험</span>에 노출되지 않도록 계좌를 관리하고, 소부장 및 전력기기 대장주 위주로 압축 대응해야 합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.8
      }
    }
  },
  "iCOAroQoml4": {
    "topic": "robot",
    "content": {
      "video": {
        "id": "iCOAroQoml4",
        "title": "중국 휴머노이드 궁금하셨다고요?ㅣ보이는 차이나ㅣ2026.6.11(목)",
        "published": "2026-06-11T00:50:20+00:00",
        "channel_name": "Smart Money by MiraeAsset ",
        "url": "https://www.youtube.com/watch?v=iCOAroQoml4",
        "thumbnail": "https://img.youtube.com/vi/iCOAroQoml4/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 중국 정부의 전략적 지원 하에 반도체, 우주항공과 더불어 휴머노이드 로봇이 핵심 육성 산업으로 선정되어 본토 과창판(STAR Market) 상장을 본격 준비 중입니다.\n2. 세계적 수준의 중국 휴머노이드 로봇 제조사 <span class=\"text-cyan-300 font-semibold\">유니트리(Unitree)</span>의 본토 과창판 상장이 임박해 차이나 로봇 섹터의 강력한 모멘텀이 형성되고 있습니다.\n3. 이미 홍콩에 상장된 유비테크에 이어 유니트리의 본토 상장은 단순 자금 조달을 넘어 국가적 대표 기업이자 국가 안보급 기술로 공인받았음을 의미합니다.",
        "key_claims": [
          "중국 정부가 미·중 기술 패권 경쟁에 대비하여 본토 STAR 마켓을 통해 자국 <span class=\"text-cyan-300 font-semibold\">독자 휴머노이드 하드웨어 공급망</span> 구축에 속도를 내고 있습니다.",
          "유니트리의 상장은 중국 내 벤처 캐피탈 자금 회수 및 대규모 상용화 투자를 이끌어내어 <span class=\"text-cyan-300 font-semibold\">물리적 AI의 단위 단가 인하</span>를 촉진할 것입니다.",
          "최근 젠슨 황의 휴머노이드 로봇 플랫폼 표준화 선언 및 지지가 중국 로봇 스타트업들의 기업 가치를 크게 올리는 촉매가 되고 있습니다."
        ],
        "data_points": [
          "중국 본토 기술 특화 시장 '과창판(STAR Market)'에 유니트리 상장 절차 추진 진행 중",
          "홍콩 증시 기존 상장 로봇사: 유비테크(UBTech)"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "중국 국가 차원의 휴머노이드 지원 및 유니트리 본토 상장 모멘텀은 단기 조정을 겪던 중국 로봇 산업 밸류에이션을 리레이팅할 강력한 엔진으로 작동할 것입니다.",
        "key_companies": [
          "유니트리(Unitree)",
          "유비테크(UBTech)",
          "엔비디아(NVDA)"
        ],
        "insight": "중국 본토의 과창판 상장은 홍콩 대비 심사가 훨씬 까다롭지만 상장 성공 시 애국 수급과 대규모 정부 펀드 자금의 즉각적인 수혜를 받습니다. 이는 유니트리가 글로벌 <span class=\"text-cyan-300 font-semibold\">보급형 휴머노이드 하드웨어 시장</span>을 대량 양산 및 가격 파괴(시간당 2달러 단가 실현)를 통해 선점하겠다는 전략적 야심을 보여줍니다.",
        "action_point": "유니트리 상장 일정에 따른 차이나 로봇 테마 및 국내 휴머노이드 정밀 액추에이터, <span class=\"text-cyan-300 font-semibold\">로봇 핵심 모션 제어 부품 기업</span>들의 낙수효과 가능성에 선제적으로 대비해야 합니다."
      },
      "classification": {
        "primary_topic": "robot",
        "relevance_score": 9.6
      }
    }
  },
  "IscrSSLWKv4": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "IscrSSLWKv4",
        "title": "트럼프 “이란은 대가를 치러야 할 것“…오라클, 자금 조달 우려에 시간외 급락 [월가 뉴스레터]",
        "published": "2026-06-10T23:19:27+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=IscrSSLWKv4",
        "thumbnail": "https://img.youtube.com/vi/IscrSSLWKv4/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 뉴욕 증시는 5월 근원 CPI가 예상을 밑돌며 안정 신호를 보냈으나, 트럼프 대통령의 <span class=\"text-rose-400 font-medium\">대이란 보복 공격 경고</span>로 지정학 리스크가 극대화되며 급락했습니다.\n2. 오라클은 4분기 견조한 클라우드 실적을 발표했음에도 데이터 센터 확장을 위한 400억 달러 추가 자금 조달 계획을 공개해 시간외 거래에서 주가가 급락했습니다.\n3. 슈퍼마이크로(SMCI) 역시 대규모 지분 가치 희석을 야기할 70억 달러 규모 자금 조달을 공시하여 기술주 매도 폭탄을 촉발했습니다.",
        "key_claims": [
          "소비자 물가 둔화세에 따른 연준의 금리 안정 기대감이 이란에 대한 트럼프 행정부의 <span class=\"text-rose-400 font-medium\">강력한 대립각 및 지정학 긴장</span>에 묻혀버렸습니다.",
          "오라클과 슈퍼마이크로의 급락은 인프라 설비를 확보하기 위한 막대한 투자 비용(CapEx)이 주주의 <span class=\"text-rose-400 font-medium\">지분 가치 희석 리스크</span>로 연결되고 있음을 의미합니다.",
          "미 국채 10년물 금리가 4.56%까지 반등하고 유가 상승 우려가 고조되는 등 거시 경제 여건의 변동성이 재확대되고 있습니다."
        ],
        "data_points": [
          "5월 미국 소비자물가지수(CPI) 전년 대비 4.2% 상승 (예상치 부합)",
          "근원 소비자물가지수(Core CPI) 전월 대비 0.2% 상승 (예상치 0.3% 하회)",
          "오라클 400억 달러 규모 데이터 센터 전용 자금 조달 및 유상증자 계획 발표",
          "슈퍼마이크로(SMCI) 70억 달러 규모 자금 조달 공시",
          "WTI 유가 3.47% 폭등하여 배럴당 91.26달러 기록, 미 국채 10년물 금리 4.56% 수준"
        ],
        "signal": "bearish",
        "signal_confidence": "high",
        "signal_reason": "양호한 인플레이션 수치를 무색하게 만드는 트럼프발 대이란 지정학 전쟁 위험 고조와 AI 빅테크들의 잇따른 대규모 유상증자/희석 악재가 시장 전반을 지배하고 있습니다.",
        "key_companies": [
          "오라클(ORCL)",
          "슈퍼마이크로컴퓨터(SMCI)",
          "아마존(AMZN)",
          "테슬라(TSLA)"
        ],
        "insight": "AI 패권 경쟁이 격화되면서 클라우드 및 서버 인프라 구축비 조달이 주가에 부담으로 작용하기 시작했습니다. 스페이스X 상장 대기 수급 쏠림과 겹쳐 <span class=\"text-rose-400 font-medium\">주주가치 희석 공포</span>가 시장의 차익 실현 빌미를 제공하고 있습니다.",
        "action_point": "유상증자 및 부채 발행 계획으로 변동성이 극대화된 종목의 무리한 저가 매수를 제한하고, 거시 리스크가 진정될 때까지 <span class=\"text-cyan-300 font-semibold\">현금 가중치가 높고 펀더멘탈이 우수한 방어주</span> 비중을 늘려야 합니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.4
      }
    }
  },
  "JnAh7IQULe4": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "JnAh7IQULe4",
        "title": "[홍장원의 불앤베어] 근원 상품 소비자 물가, 충격의 하락. 트럼프 \"이란 또 맞아야\"",
        "published": "2026-06-10T10:11:30+00:00",
        "channel_name": "매경월가월부",
        "url": "https://www.youtube.com/watch?v=JnAh7IQULe4",
        "thumbnail": "https://img.youtube.com/vi/JnAh7IQULe4/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 5월 미국 CPI는 전년 대비 4.2% 상승하며 3년 만에 가장 높은 수준을 보였으나, 상승분의 대다수가 전쟁 유가 상승에 기인한 일시적 요인으로 분석됩니다.\n2. 식품과 에너지를 제외한 근원 상품 물가는 오랜만에 0.1% 하락을 기록해 기저의 <span class=\"text-amber-300 font-bold\">디스인플레이션 흐름</span>이 여전히 유지되고 있음을 시사했습니다.\n3. 다만 트럼프 대통령이 미군 피해 우려에 대응해 이란에 추가 보복 타격을 선언하면서, 유가 불안에 의한 인플레이션 장기화 위험이 다시 시장을 압박하고 있습니다.",
        "key_claims": [
          "헤드라인 인플레이션의 폭등은 일시적 <span class=\"text-amber-300 font-bold\">에너지 쇼크</span> 때문이며, 기저의 상품과 주거 서비스 물가는 차츰 하향 안정되고 있습니다.",
          "미국의 높은 소비자 구매력 저하 및 실질 임금 감소세가 궁극적으로 기저의 소비 물가를 하향 안정시킬 것입니다.",
          "지정학적 갈등 장기화로 호르무즈 해협 위기가 지속되면 연준의 인플레이션 통제 경로에 <span class=\"text-rose-400 font-medium\">지속적인 상방 리스크</span>가 될 수 있습니다."
        ],
        "data_points": [
          "5월 CPI 전년 대비 4.2% 상승, 전월 대비 0.5% 상승 (예상치 부합)",
          "근원 CPI 전월 대비 0.2% 상승, 전년 대비 2.9% 상승 (예상치 하회)",
          "5월 에너지 가격 전월 대비 3.9% 상승 (전년 대비 23.5% 상승)",
          "근원 상품 물가 전월 대비 0.1% 하락 기록"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "기저 물가의 디스인플레이션 진전은 긍정적이나, 유가 반등을 촉발하는 트럼프 행정부의 강대강 중동 정책이 상존하여 방향성이 엇갈리고 있습니다.",
        "key_companies": [],
        "insight": "미국의 이번 CPI 수치는 기저 상품 인플레이션의 하향 안정이 현실화되고 있음을 입증했습니다. 유가 충격만 걷어낸다면 <span class=\"text-amber-300 font-bold\">금리 인하 테이블</span>이 다시 열릴 수 있으나, 중동 분쟁에 따른 원유 공급 리스크가 단기적인 통화 긴축 경계감을 유지시킬 것입니다.",
        "action_point": "유가 등 지정학 뉴스에 과민 반응하여 손절하기보다는 <span class=\"text-cyan-300 font-semibold\">실질 물가 하락 수혜 섹터(유통, 소비재)</span> 및 금리 고공행진에 하방 경직성을 보유한 금융 자산에 차분히 분할 매수로 접근하는 전략이 좋습니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.2
      }
    }
  },
  "JZiB7PWIze8": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "JZiB7PWIze8",
        "title": "\"금리 올라도 안 막아준다\"케빈 워시, 트럼프 애원 무시하나",
        "published": "2026-06-10T10:45:07+00:00",
        "channel_name": "교양이를 부탁해",
        "url": "https://www.youtube.com/watch?v=JZiB7PWIze8",
        "thumbnail": "https://img.youtube.com/vi/JZiB7PWIze8/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 미국 무디스의 신용등급 강등 경고의 원인인 <span class=\"text-rose-400 font-medium\">재정 적자 문제</span>가 계속 악화되면서 미 국채 금리 추가 급등 리스크가 상존합니다.\n2. 과거 연준 체제와 달리, 새로 출범한 케빈 워시 연준 의장은 채권 시장 변동성을 제거하기 위한 국채 매입(QE) 등 인위적 시장 개입에 나서지 않을 것임을 공고히 했습니다.\n3. 이에 따라 트럼프 행정부가 규제 완화 등을 내세워 조속한 금리 인하를 구두로 압박하고 있으나, 워시 의장의 <span class=\"text-rose-400 font-medium\">매파적/독립적 태도</span>로 갈등이 심화될 전망입니다.",
        "key_claims": [
          "재정 적자 폭발에 따른 미국의 신용등급 추가 강등 리스크는 국채 금리에 <span class=\"text-rose-400 font-medium\">신용 프리미엄 상승 압력</span>을 가할 것입니다.",
          "케빈 워시 의장의 연준은 인위적인 수급 방어(국채 매입)를 거부하므로 채권 시장의 장기 금리가 하방 통제 없이 <span class=\"text-rose-400 font-medium\">시장 수급에 의해 상승</span>할 것입니다.",
          "트럼프 정부의 금리 인하 요구와 연준의 독립적 긴축 의지 간의 정면 충돌은 채권 시장의 장기적인 불확실성 요인입니다."
        ],
        "data_points": [
          "지난해 5월 무디스 미국의 신용등급 전망 하향 조정 단행",
          "미국 국채 10년물 장기물 금리 수급 조절 부재로 인해 상방 압력 점증"
        ],
        "signal": "bearish",
        "signal_confidence": "high",
        "signal_reason": "연준의 채권 시장 불개입 원칙과 신용 프리미엄 결합에 따른 장기 국채 금리 상승 기조는 기업 조달 금리 상승 등 실물 경제 전반에 큰 비용 부담을 유발합니다.",
        "key_companies": [],
        "insight": "새 연준 체제는 채권 시장 구제자로서의 역할을 폐지하고 인플레이션 억제에만 초점을 맞추고 있습니다. 이는 재정 적자를 늘리는 트럼프 행정부의 정책적 확장세에 연준이 <span class=\"text-rose-400 font-medium\">금리 불개입 및 고금리 유지</span>로 강경하게 제동을 거는 양상입니다.",
        "action_point": "장기 금리 상방 압력이 지속될 것을 감안해 레버리지 투자를 지양하고, <span class=\"text-cyan-300 font-semibold\">재무 구조가 건전한 저부채 기업</span> 및 고금리 수혜를 직접 입는 대형 증권·은행주 위주로 방어적 포트폴리오를 구성해야 합니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.1
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
