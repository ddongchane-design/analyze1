import json
from pathlib import Path

# Define the analyzed data for Batch 8
batch_data = {
  "lLRomqo5jCc": {
    "topic": "crypto",
    "content": {
      "video": {
        "id": "lLRomqo5jCc",
        "title": "전쟁 합의 기대감과 CPI 그리고 트럼프 한마디에 요동치는 비트코인과 글로벌 시장 | 서동주, 김동환, 박상혁 디지털애셋 편집장 [크립토 PLUS]",
        "published": "2026-06-11T02:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=lLRomqo5jCc",
        "thumbnail": "https://img.youtube.com/vi/lLRomqo5jCc/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 미국이 이란 폭격을 개시했으나, 트럼프 대통령이 '이란 당국자와 직접 합의를 조율 중이며 곧 끝날 것'이라고 언급하여 시장은 <span class=\"text-amber-300 font-bold\">극적 타결 기대감</span>으로 반등을 모색했습니다.\n2. 5월 미국 CPI 물가지수는 전년 대비 4.2% 상승해 예상치에 부합했으나, 연준이 금리 인하를 논의하기에는 <span class=\"text-rose-400 font-medium\">아직 인플레이션 압력이 높은 수준</span>으로 진단됩니다.\n3. 그레이스케일 온체인 지표에 따르면 비트코인은 현재 <span class=\"text-cyan-300 font-semibold\">저평가 매수 구간</span>에 진입해 있으며, 6만 달러 부근이 기술적 저점으로 분석됩니다.",
        "key_claims": [
          "지정학적 리스크(이란 공습) 발발 시 단기 급락 후 트럼프의 '속전속결 타결' 기대가 작동해 <span class=\"text-amber-300 font-bold\">위험 자산 반등 흐름</span>을 유도하고 있습니다.",
          "미국 3배 레버리지 ETF의 합산 거래량이 역사상 최대치를 달성하며 주식 시장의 <span class=\"text-rose-400 font-medium\">상승장 후반부 투기 과열 조짐</span>이 보이고 있습니다.",
          "비트코인 신규 채굴량 대비 기관 매도세가 단기 최저 수준을 보이지만, 온체인 펀더멘탈상 <span class=\"text-cyan-300 font-semibold\">장기 저점 지지력</span>이 형성되었습니다."
        ],
        "data_points": [
          "비트코인 가격 61,000달러~63,000달러 선 등락 흐름",
          "5월 미국 CPI 전년 대비 4.2% 상승 (소수점 둘째자리 0.27% 수준)",
          "트럼프 취임일 대비 메이저 알트코인(도지코인 등) 마이너스 78% 이상 하락 기록",
          "비트코인 신규 발행량 대비 채굴자/기관 매도 압력 마이너스 464% 수준 기록"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "지정학적 타결 기대와 온체인 저평가 지표가 호재로 작용하지만, 3배 레버리지 과열과 여전한 기관 매도 압력 및 CPI 둔화 부족으로 변동성 장세가 이어집니다.",
        "key_companies": [
          "그레이스케일",
          "마이크로스트레티지(MSTR)"
        ],
        "insight": "지정학적 폭격 노이즈에 대한 시장의 반응은 과거 학습 효과로 인해 내성이 생겼으며, 트럼프의 '협상을 위한 단기 타격' 스탠스를 적극 신뢰하고 있습니다. 다만, 세배 레버리지 투기적 쏠림이 사상 최고치인 점은 유동성 증발 국면에서 단기 청산에 주의해야 함을 경고합니다.",
        "action_point": "박스권 하단인 6만 달러 초반에서는 온체인 저평가 신호를 기반으로 한 <span class=\"text-cyan-300 font-semibold\">점진적 분할 매수</span>가 유리하며, 고배율 레버리지 상품 투자는 지양해야 합니다."
      },
      "classification": {
        "primary_topic": "crypto",
        "relevance_score": 9.4
      }
    }
  },
  "onr-XSRe3PI": {
    "topic": "crypto",
    "content": {
      "video": {
        "id": "onr-XSRe3PI",
        "title": "스페이스X 가격을 추종하는 토큰 나왔다! 하지만 실제 주주가 되는 건 아닙니다 | 서동주, 김동환, 최윤영 한화투자증권 팀장 [크립토 PLUS]",
        "published": "2026-06-11T02:30:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=onr-XSRe3PI",
        "thumbnail": "https://img.youtube.com/vi/onr-XSRe3PI/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 글로벌 가상자산 거래소 바이비트가 백드 에셋(Backed Asset)과 협업하여 스페이스X의 상장 전 주가 익스포저를 제공하는 <span class=\"text-cyan-300 font-semibold\">프리 IPO 추종 토큰(X스톡)</span> 청약을 출시했습니다.\n2. 본 상품은 100% 실물 주식 1:1 담보 매칭이 아닌 현금성 자산을 믹스한 <span class=\"text-violet-300 font-medium\">구조화 채무 증서(Tracker Certificate)</span> 형태로 의결권 등 실제 주주 권리는 보장되지 않습니다.\n3. 전통 비상장 주식 투자의 진입 장벽을 낮춘 혁신이나, 비상장 특성상의 단일 오라클 가격 의존과 얕은 유동성으로 인한 <span class=\"text-rose-400 font-medium\">가격 괴리/청산 리스크</span>가 존재합니다.",
        "key_claims": [
          "글로벌 블록체인 거래소들이 RWA(실물자산 토큰화) 기술을 이용해 비상장 주식에 대한 <span class=\"text-cyan-300 font-semibold\">개인 리테일 접근성</span>을 빠르게 확대하고 있습니다.",
          "토큰화 주식 RWA 시장 규모는 올해 초 22억 달러에서 6개월 만에 <span class=\"text-cyan-300 font-semibold\">145% 급성장</span>하며 RWA 섹터 내 핵심으로 부상했습니다.",
          "미국 CFTC/SEC 규제권 밖의 거래소 합성 자산은 기초 주식과의 큰 시세 이격이 발생해도 법적인 <span class=\"text-rose-400 font-medium\">투자자 보호 장치</span>를 받기 어렵습니다."
        ],
        "data_points": [
          "바이비트 스페이스X 프리 IPO 토큰 청약 개시 (최소 투자 금액 100달러, USDC 기준)",
          "토큰화 주식 RWA 시장 규모: 연초 22억 달러 대비 약 145% 증가",
          "5월 말 하이퍼리퀴드 디파이 내 스페이스X 무기한 선물 45% 일시 급락 및 청산 노이즈 발생"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "전통 비상장 투자 장벽 해소 측면은 긍정적이나, 의결권이 없고 발행사(백드 에셋)의 신용도 및 비상장 주식 시세 괴리율, 거래소의 CS 미비 우려 등 리스크 요인이 많아 경계가 필요합니다.",
        "key_companies": [
          "바이비트",
          "백드에셋(Backed)",
          "스페이스X",
          "앤스로픽",
          "크라켄"
        ],
        "insight": "스페이스X RWA 토큰 상품은 SPV를 통한 지분 직접 양도가 아니므로 비상장사의 양도 금지 조항(Transfer restrictions) 규제를 회회하는 영리한 우회 전술입니다. 그러나 제도권 밖의 유동성이 얕은 합성 자산 시장은 호재/악재 시점에 극단적인 청산 스퀴즈가 발생할 수 있음을 보여줍니다.",
        "action_point": "소액으로 스페이스X 상장 모멘텀에 올라타는 용도로는 고려해 볼 수 있으나, 거래소 오라클 왜곡으로 인한 강제 청산 리스크가 있으므로 레버리지 활용이나 고액 투자는 극히 삼가야 합니다."
      },
      "classification": {
        "primary_topic": "crypto",
        "relevance_score": 8.8
      }
    }
  },
  "PNJZEmqF68U": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "PNJZEmqF68U",
        "title": "\"이란 타격\" 뉴욕 증시 박살.. \"데이터센터 건설 취소\" 악재까지 ㄷㄷ..",
        "published": "2026-06-11T00:00:00+00:00",
        "channel_name": "주식유치원_삼프로TV",
        "url": "https://www.youtube.com/watch?v=PNJZEmqF68U",
        "thumbnail": "https://img.youtube.com/vi/PNJZEmqF68U/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 뉴욕 증시는 지정학적 이란 공격 개시와 더불어 비상장 클라우드 사 '크루소(Crusoe)'의 <span class=\"text-violet-300 font-medium\">1.8GW 데이터센터 건설 중단</span> 악재가 겹치며 나스닥이 2% 폭락했습니다.\n2. 크루소의 건설 중단은 글로벌 AI 수요 둔화가 아닌 와이오밍 의회의 전력 공급 및 수자원 환경 규제에 따른 <span class=\"text-rose-400 font-medium\">로컬 전력 병목 리스크</span>에 기인합니다.\n3. 같은 날 5GW 규모의 대규모 데이터센터 신규 계약 체결 호재는 무시되고 악재에 과민 반응한 점을 고려하면, 수급 털기를 위한 <span class=\"text-rose-400 font-medium\">의도적 공포 조장</span> 성격이 짙습니다.",
        "key_claims": [
          "지방 자치단체의 환경 규제와 전력 인프라 지연 이슈가 마치 AI 인프라 투자 전체의 침체인 양 <span class=\"text-rose-400 font-medium\">시장 오해</span>로 증폭되었습니다.",
          "미국의 단기 이란 공습 카드는 전면전 확대 의도보다는 조기 휴전 및 협상을 끌어내기 위한 트럼프식 <span class=\"text-amber-300 font-bold\">압박 전술</span>의 성격이 큽니다.",
          "시장의 호재(5GW 추가 계약) 대비 악재에만 크게 반응하는 현재의 주가 흐름은 밸류에이션 버블 해소를 위한 <span class=\"text-amber-300 font-bold\">기술적 털기 구간</span>으로 봐야 합니다."
        ],
        "data_points": [
          "나스닥 지수 하루 동안 2% 급락 마감",
          "네오클라우드 기업 '크루소' 와이오밍 1.8GW 데이터센터 건설 무기한 중단 선언",
          "동일 시점에 타 빅테크 사의 5GW 데이터센터 신규 구축 계약 공식 공시"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "전력/규제적 리스크의 실체화로 데이터센터 속도 조절이 발생한 것은 사실이나, 본질적인 AI CapEx 수요는 훼손되지 않은 과매도 구간입니다.",
        "key_companies": [
          "크루소(Crusoe)",
          "오라클(ORCL)",
          "블룸에너지(BE)"
        ],
        "insight": "데이터센터 취소 뉴스는 지역 전력 가격 상승에 반대하는 와이오밍주의 로컬 민심과 관련 규제 탓으로, AI 하드웨어 수요 붕괴로 읽는 것은 오류입니다. 지수의 단기 과밀 상태에서 노이즈를 핑계 삼아 레버리지를 터는 통상적인 선물 옵션 만기 수급 과정으로 분석됩니다.",
        "action_point": "데이터센터 전력 공급원으로 부각되었던 에너지 칩셋 및 친환경 발전 관련 기업의 주가 조정을 <span class=\"text-cyan-300 font-semibold\">장기 저점 매수</span> 기회로 잡고, 매크로 공포에 동참하지 않는 담대함이 필요합니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.1
      }
    }
  },
  "QiLSOVPK2DY": {
    "topic": "tech",
    "content": {
      "video": {
        "id": "QiLSOVPK2DY",
        "title": "AI 전쟁 속 애플의 선택은?",
        "published": "2026-06-11T01:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=QiLSOVPK2DY",
        "thumbnail": "https://img.youtube.com/vi/QiLSOVPK2DY/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 애플은 자사의 차세대 파운데이션 모델 학습 및 연산을 위해 <span class=\"text-cyan-300 font-semibold\">구글 제미나이(Gemini)와 구글 클라우드</span> 기술을 공식 채택하기로 발표했습니다.\n2. 사용자가 경험하는 앞단의 인터페이스는 여전히 애플 고유의 시리(Siri)와 <span class=\"text-cyan-300 font-semibold\">애플 인텔리전스</span>로 구동되며, 뒷단의 고성능 연산 시 구글 클라우드를 빌려 쓰는 방식입니다.\n3. 온디바이스에서 처리하기 어려운 데이터가 유출되는 것을 막기 위해 자체 실리콘 기반 서버에서 사용자 데이터를 무보존 처리하는 <span class=\"text-cyan-300 font-semibold\">프라이빗 클라우드 컴퓨트(PCC)</span> 환경을 접목했습니다.",
        "key_claims": [
          "애플은 AI 파운데이션 모델 개발 속도의 격차를 메우기 위해 독자 개발을 고집하지 않고 구글과의 <span class=\"text-cyan-300 font-semibold\">기술 동맹</span>을 선택했습니다.",
          "사용자의 개인정보 보안을 최우선으로 지키기 위해 클라우드 연산 구간에 하드웨어 레벨의 <span class=\"text-rose-400 font-medium\">프라이버시 통제(PCC)</span>를 강화하고 있습니다.",
          "구글과 애플의 연합은 마이크로소프트-OpenAI 연합의 독점적 온디바이스 및 서비스 지배력을 강력하게 견제하려는 <span class=\"text-cyan-300 font-semibold\">빅테크 합종연횡</span>의 결과물입니다."
        ],
        "data_points": [
          "애플 파운데이션 모델 백엔드에 구글 제미나이 모델 공식 연동",
          "클라우드 보안 실행 환경 '프라이빗 클라우드 컴퓨트(Private Cloud Compute)' 구축",
          "구글 클라우드와 애플 실리콘 서버 기술 융합 진행"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "애플의 사용자 기반(iOS)과 구글의 압도적인 LLM 파워가 결합되면서, AI 대중화 및 모바일 기기 교체 수요(Supercycle)를 유의미하게 자극할 생태계가 마련되었습니다.",
        "key_companies": [
          "애플(AAPL)",
          "구글(GOOGL)"
        ],
        "insight": "애플의 제미나이 채택은 온디바이스 AI 시장의 표준 장악을 위한 전략적 굴복이자 협력입니다. 기기 내 연산(On-device)과 프라이빗 서버(PCC)의 이중 레이어 아키텍처는 향후 스마트폰 제조사들이 지향해야 할 개인정보 보호 기반 AI 에이전트의 완성형 모델이 될 것입니다.",
        "action_point": "애플과 구글 클라우드 동맹의 최대 수혜를 입는 모바일 부품 및 전방 메모리 패키징 기업, 그리고 고성능 NPU 가속기 생태계에 편입된 관련 기업들에 주목해야 합니다."
      },
      "classification": {
        "primary_topic": "tech",
        "relevance_score": 9.7
      }
    }
  },
  "T85lFoEtIrc": {
    "topic": "tech",
    "content": {
      "video": {
        "id": "T85lFoEtIrc",
        "title": "반도체 랠리 끝났나? 시장 흔들리는 진짜 이유 (HSL 파트너스 이형수 대표) | 2026년 06월 10일 녹화",
        "published": "2026-06-11T01:30:00+00:00",
        "channel_name": "언더스탠딩_Understanding",
        "url": "https://www.youtube.com/watch?v=T85lFoEtIrc",
        "thumbnail": "https://img.youtube.com/vi/T85lFoEtIrc/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 반도체 슈퍼 사이클의 병목 현상이 과거의 단순 단일 D램 공급 부족(점)에서 기판, 신소재, 전력 등 <span class=\"text-violet-300 font-medium\">복합 다단한 구조적 병목(선/면)</span>으로 진화하고 있습니다.\n2. AI 서버 전력량이 렉당 10kW에서 GB200 기준 120kW 이상으로 12배 폭증함에 따라, 고열을 견디기 위한 <span class=\"text-cyan-300 font-semibold\">신소재(유리섬유, 특수 기판) 쇼티지</span>가 새롭게 부각되고 있습니다.\n3. 스케일링 법칙(컴퓨팅/데이터/알고리즘)에 의해 빅테크의 선점 투자 경쟁은 가속화될 것이며, 피크아웃 우려와 달리 펀더멘탈은 극히 견조합니다.",
        "key_claims": [
          "과거처럼 공장 증설 후 공급 과잉으로 폭락하는 단조로운 디램 사이클 대신, <span class=\"text-cyan-300 font-semibold\">패키징 기판과 전력망 부품</span>이 얽힌 새로운 복합 슈퍼 사이클이 열렸습니다.",
          "미국의 국지적 전력 공급 및 규제 병목으로 인한 착공 지연은 메모리 재고 부족이 지속되고 있어 <span class=\"text-rose-400 font-medium\">실질적인 수요 차질을 초래하지 않습니다</span>.",
          "AI 개발 특이점 속도가 예상보다 수배 빠르며, 후발 기업이 저렴하게 추격할 타이밍이 존재하지 않으므로 빅테크들은 <span class=\"text-amber-300 font-bold\">선점 경쟁(CapEx)을 멈출 수 없습니다</span>."
        ],
        "data_points": [
          "대만 올해 경제 성장률 14% 전망 (AI 공급망 핵심국으로 최고치 경신)",
          "AI 서버 랙당 전력 사용량: 호퍼(H100) 40~80kW에서 블랙웰(GB200) 120~150kW 수준으로 폭증",
          "기판용 고특성 유리섬유 전 세계 독점: 일본 니또보(Nitto Boseki) 주가 신고가 행진",
          "특수 절연 기판용 화학 CCL 전 세계 독점: 일본 레조낙(Resonac) 쇼티지 직면"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "전력 밀도 폭증으로 인해 반도체 기판(FC-BGA), 특수 소재(니또보, 레조낙), MLCC, 아날로그 IC 등 신규 병목 체인이 연쇄 발생해 메모리 및 장비 밸류체인의 이익 상승을 지지합니다.",
        "key_companies": [
          "니또보(Nitto Boseki)",
          "레조낙(Resonac)",
          "삼성전기(009150)",
          "SK하이닉스(000660)",
          "삼성전자(005930)",
          "엔비디아(NVDA)"
        ],
        "insight": "AI 투자의 핵심 동력은 B2C 챗봇이 아닌 기업들의 API 도입을 통한 생산성 혁신입니다. 병목 지점이 HBM에서 패키징 신소재 및 수동소자(MLCC)로 확산되고 있는 것은 메모리 제조사들에게 피크아웃이 아닌 장기 마진 믹스 개선의 기회를 제공합니다.",
        "action_point": "반도체 피크아웃 공포로 인한 단기 주가 하락은 적극적인 <span class=\"text-cyan-300 font-semibold\">우량 메모리 및 소재/부품주 추가 매수</span> 기회이며, 특히 일본의 핵심 정밀 소재 밸류체인과 국내의 MLCC/기판 대형주를 공략해야 합니다."
      },
      "classification": {
        "primary_topic": "tech",
        "relevance_score": 9.8
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
