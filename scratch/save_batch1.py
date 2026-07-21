import json
from pathlib import Path

batch1_data = {
  "eTcK9K0GW8U": {
    "primary": "tech",
    "data": {
      "video": {
        "id": "eTcK9K0GW8U",
        "title": "증권사들이 하이닉스 주가 500만원을 예상하는 이유",
        "published": "2026-06-16T11:00:38+00:00",
        "channel_name": "Softdragon SOD",
        "url": "https://www.youtube.com/watch?v=eTcK9K0GW8U",
        "thumbnail": "https://img.youtube.com/vi/eTcK9K0GW8U/hqdefault.jpg"
      },
      "analysis": {
        "summary": "골드만삭스에 따르면 일반 챗봇은 1,000개 토큰을 소비하지만, 24시간 작동하는 <span class=\"text-cyan-300 font-semibold\">AI 에이전트</span>는 하루에 10만 개 이상의 토큰을 소비함. 직접 행동해야 하는 AI 에이전트의 활성화는 향후 <span class=\"text-amber-300 font-bold\">토큰 쇼티지</span>(부족) 시대를 유발할 것임. 이로 인해 메모리 수요가 폭증하며 심각한 <span class=\"text-cyan-300 font-semibold\">메모리 쇼티지</span> 현상을 일으키는 기폭제가 될 전망임.",
        "key_claims": [
          "AI 에이전트 시대의 도래는 기하급수적인 토큰 소모로 인해 토큰 쇼티지 시대를 열 것임.",
          "토큰 쇼티지는 결국 반도체 시장의 메모리 쇼티지로 이어지게 될 것임."
        ],
        "data_points": [
          "일반 챗봇 소비 토큰: 약 1,000개",
          "24시간 작동 AI 에이전트 하루 소비 토큰: 10만 개 이상"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "AI 에이전트 보급으로 토큰 소모량이 100배 이상 급증하면서 필수 하드웨어인 <span class=\"text-cyan-300 font-semibold\">메모리 반도체</span> 수요가 구조적으로 폭발할 것이기 때문임.",
        "key_companies": ["SK하이닉스", "골드만삭스"],
        "insight": "단순 대화형 챗봇에서 스스로 행동하는 AI 에이전트로 패러다임이 전환됨에 따라 컴퓨팅 자원 및 토큰 소모량이 급증함. 이는 결국 반도체 기업들의 공급 능력을 초과하는 <span class=\"text-cyan-300 font-semibold\">메모리 병목 현상</span>을 가져와 HBM 등 고대역폭 메모리와 초고속 메모리 제조업체들의 장기적 가격 협상력과 영업이익을 극대화하게 됨.",
        "action_point": "AI 에이전트 기반 서비스 상용화 속도에 맞춰 메모리 반도체 리더인 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>와 삼성전자의 장기 성장성에 지속 투자하는 전략이 필요함."
      },
      "classification": {
        "primary_topic": "tech",
        "secondary_topics": ["stock"],
        "tags": ["AI에이전트", "토큰쇼티지", "메모리쇼티지", "SK하이닉스"]
      }
    }
  },
  "7T-1UQs2l8k": {
    "primary": "tech",
    "data": {
      "video": {
        "id": "7T-1UQs2l8k",
        "title": "중국 3단계 자율주행 절대 안 나오는 이유",
        "published": "2026-06-16T14:15:09+00:00",
        "channel_name": "언더스탠딩_Understanding",
        "url": "https://www.youtube.com/watch?v=7T-1UQs2l8k",
        "thumbnail": "https://img.youtube.com/vi/7T-1UQs2l8k/hqdefault.jpg"
      },
      "analysis": {
        "summary": "자율주행 <span class=\"text-cyan-300 font-semibold\">L3(레벨3)</span> 단계부터는 사고 발생 시 운전 책임이 운전자가 아닌 자율주행 시스템에 귀속됨. 이로 인해 법적 책임 리스크를 회피하고자 중국 등 글로벌 제조사들은 기능이 FSD급이어도 L3 명칭 대신 <span class=\"text-amber-300 font-bold\">L2 플러스</span>(L2+)로 호칭하고 있음. 결과적으로 사고 책임 부담 때문에 전 세계적으로 L3 레벨의 자율주행 시스템 도입은 거의 괴멸 상태를 보이고 있음.",
        "key_claims": [
          "L3 단계부터는 운전자의 전방 주시 의무가 사라지고 운전 책임이 시스템으로 넘어가기 때문에 기업들이 이를 회피하려고 함.",
          "제조사들이 FSD 수준의 자율주행 기능을 구현하더라도 법적 책임을 면하기 위해 L2플러스로 명명함."
        ],
        "data_points": [],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "기술적으로 자율주행 고도화가 이뤄지고 있으나 제조사들의 <span class=\"text-rose-400 font-medium\">법적 책임 문제</span>로 상용 L3 자율주행의 제도적 보급이 지연되고 있기 때문임.",
        "key_companies": [],
        "insight": "자율주행 기술의 완성도와 별개로, 법적 책임 소재의 변곡점인 L3 단계의 도입은 글로벌 메이커들에게 극심한 <span class=\"text-rose-400 font-medium\">소송 및 제조 책임 리스크</span>를 안겨줌. 따라서 시장은 안전과 규제 리스크를 우회하면서도 성능을 극대화할 수 있는 L2+ 하이브리드 노선을 지속 채택할 것으로 보임.",
        "action_point": "자율주행 산업 투자 시 완전자율주행(L3 이상) 기대감만으로 접근하기보다는, 현실적인 타협안인 <span class=\"text-cyan-300 font-semibold\">ADAS 및 L2+ 솔루션</span> 공급으로 매출을 일으키는 소부장 및 소프트웨어 솔루션 기업에 주목해야 함."
      },
      "classification": {
        "primary_topic": "tech",
        "secondary_topics": ["etc"],
        "tags": ["자율주행", "L3", "법적책임", "L2플러스"]
      }
    }
  },
  "68zIflSMB7M": {
    "primary": "economy",
    "data": {
      "video": {
        "id": "68zIflSMB7M",
        "title": "하반기 증시 최대 변수 '이것'? 빅테크 운명 가를 AI 수익화 #교양이를부탁해",
        "published": "2026-06-16T11:15:16+00:00",
        "channel_name": "교양이를 부탁해",
        "url": "https://www.youtube.com/watch?v=68zIflSMB7M",
        "thumbnail": "https://img.youtube.com/vi/68zIflSMB7M/hqdefault.jpg"
      },
      "analysis": {
        "summary": "시장은 막대한 설비 투자를 단행하는 <span class=\"text-cyan-300 font-semibold\">AI 비즈니스의 실질적 수익화</span>와 가능성(Feasibility) 증명을 요구하기 시작함. 스페이스X, 엔트로픽, 오픈AI 등 초대형 기업들의 상장 대기 및 빅테크(알파벳, 메타 등)의 <span class=\"text-amber-300 font-bold\">유상증자 자금 조달</span> 흐름이 가시화되고 있음. 고금리 환경에서 부채 조달 대신 고평가된 주식을 활용한 유상증자를 선택하면서 주주 가치 희석 우려가 발생함.",
        "key_claims": [
          "AI 기업들이 막대한 자금을 퍼부었으므로 이제는 구체적인 실적과 실현 가능성을 증명해야 하는 시점임.",
          "고금리 부담으로 인해 기업들이 채권 발행(빚)보다 고평가된 주가를 바탕으로 주식 발행(유상증자)을 통한 자본 조달을 선호함."
        ],
        "data_points": [],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "막대한 투자를 집행한 빅테크들의 <span class=\"text-rose-400 font-medium\">수익화 입증 부담</span>이 가중되는 시기이며, 자금 조달을 위한 유상증자 압박이 기존 주주가치를 단기적으로 희석할 수 있기 때문임.",
        "key_companies": ["스페이스X", "엔트로픽", "오픈AI", "알파벳(GOOGL)", "메타(META)"],
        "insight": "AI 투자 광풍이 인프라 확충 단계에서 수익화 검증 단계로 넘어가고 있음. 고금리 기조가 지속되는 환경에서 빅테크들은 높은 주가를 지지대 삼아 주주 환원보다는 <span class=\"text-amber-300 font-bold\">자본 조달(유상증자)</span>을 택해 현금을 장전하고 있으며, 이는 시장 전체의 유동성 흡수와 단기 멀티플 압박으로 작용할 가능성이 큼.",
        "action_point": "빅테크 및 AI 기업들의 공격적 증설이 장기 동력임은 분명하나, 당분간은 유상증자 공시나 실적 발표 시 <span class=\"text-cyan-300 font-semibold\">AI 매출 비중</span> 및 수익성 지표를 엄격히 필터링하며 신중하게 접근할 필요가 있음."
      },
      "classification": {
        "primary_topic": "economy",
        "secondary_topics": ["stock", "tech"],
        "tags": ["AI수익화", "유상증자", "자금조달", "고금리"]
      }
    }
  },
  "Z9jBG44swEg": {
    "primary": "stock",
    "data": {
      "video": {
        "id": "Z9jBG44swEg",
        "title": "오를만큼 올랐다? 빈센트가 본 코스피 현 주소 |  빈센트 & 정프로 [더블 체크]",
        "published": "2026-06-16T08:49:47+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=Z9jBG44swEg",
        "thumbnail": "https://img.youtube.com/vi/Z9jBG44swEg/hqdefault.jpg"
      },
      "analysis": {
        "summary": "코스피 지수가 최고 수준에 도달했으나, 장기적인 관점에서 보면 여전히 갈 길이 먼 <span class=\"text-amber-300 font-bold\">상승 여력</span>이 존재함. 매크로 및 섹터 환경이 약하더라도 각 분야에서 확실한 <span class=\"text-cyan-300 font-semibold\">주도주</span>를 공략하는 여주사(이왕 살 거면 주도주를 사라) 전략을 권장함. 특히 AI 시대의 핵심 수혜주인 메모리 반도체와 화장품 분야의 특정 종목(아모레퍼시픽 등)이 매수 우위에 있음을 강조함.",
        "key_claims": [
          "지수가 많이 오른 것처럼 보여도 장기적 관점에서는 여전히 갈 길이 멀며 기회가 있음.",
          "시장 환경이 약한 섹터일지라도 그 안의 주도주는 탄력 있게 움직이므로 반드시 1등 주도주를 매수해야 함.",
          "AI 시대 메모리 반도체는 여전히 시장의 강력한 주도주 지위를 유지함."
        ],
        "data_points": [],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "코스피의 장기적 우상향 추세가 훼손되지 않았으며, <span class=\"text-cyan-300 font-semibold\">메모리 반도체</span>라는 확실한 글로벌 주도주 섹터가 시장을 견인하고 있기 때문임.",
        "key_companies": ["아모레퍼시픽(090430)"],
        "insight": "지수의 단기 고점 인식에 따른 불안감보다 중요한 것은 '섹터 내 주도주 쏠림 현상'임. 전체 지수의 큰 폭등이 없더라도 AI 반도체 공급망이나 미국 중심 수출 성장세가 확인되는 뷰티(화장품) 등 <span class=\"text-cyan-300 font-semibold\">글로벌 경쟁력을 갖춘 기업</span>으로 자금이 집중되는 차별화 장세가 지속될 것임.",
        "action_point": "지수 추종형 인덱스 펀드보다는 AI 반도체 밸류체인(삼성전자, SK하이닉스) 및 글로벌 K-뷰티 수출 호조를 보이는 <span class=\"text-cyan-300 font-semibold\">업종 내 1등 주도주</span>를 선별하여 비중을 확대하는 전략을 유지해야 함."
      },
      "classification": {
        "primary_topic": "stock",
        "secondary_topics": ["economy"],
        "tags": ["코스피전망", "주도주전략", "메모리반도체", "K뷰티"]
      }
    }
  },
  "GGHGoFKtniM": {
    "primary": "energy",
    "data": {
      "video": {
        "id": "GGHGoFKtniM",
        "title": "중동 전쟁 이후의 유가, 왜 이전 가격으로 못 돌아가나 #교양이를부탁해",
        "published": "2026-06-16T12:15:13+00:00",
        "channel_name": "교양이를 부탁해",
        "url": "https://www.youtube.com/watch?v=GGHGoFKtniM",
        "thumbnail": "https://img.youtube.com/vi/GGHGoFKtniM/hqdefault.jpg"
      },
      "analysis": {
        "summary": "중동 전쟁 종식 후 호르무즈 해협이 개방되더라도 국제 유가가 전쟁 이전 수준(배럴당 60달러)으로 즉각 하락하기는 어려움. 이란(오펙 생산 능력 3위), 사우디, 카타르, UAE 등의 <span class=\"text-violet-300 font-medium\">에너지 생산/가스 시설 파괴</span>로 생산 재건에 최소 6개월에서 2년의 시간이 소요되기 때문임. 추가로 재발 우려에 따른 용선료, 선원 인건비, <span class=\"text-rose-400 font-medium\">해상 보험료 상승</span> 등 운송비 부담이 영구적으로 상향 평준화된 것도 유가를 지지하는 원인임.",
        "key_claims": [
          "전쟁이 끝나 호르무즈 해협이 개방되어도 에너지 공급량이 예전 수준으로 바로 회복될 수 없음 (인프라 복구에 6개월~2년 소요).",
          "호르무즈 위험 프리미엄으로 인해 용선료, 인건비, 보험료 등 운송 비용이 구조적으로 증가함."
        ],
        "data_points": [
          "전쟁 이전 국제 유가: 배럴당 60달러 수준",
          "현재 국제 유가 수준: 배럴당 약 90달러 수준 (피크 120달러 기록 후)",
          "이란 산유국 능력 순위: 오펙(OPEC) 내 3위"
        ],
        "signal": "neutral",
        "signal_confidence": "medium",
        "signal_reason": "유가가 전쟁 이전 수준(60달러대)으로 빠르게 회귀하기 어려워 고유가 기조가 장기화됨에 따라, 글로벌 <span class=\"text-rose-400 font-medium\">인플레이션 압박</span>과 금리 인하 지연 리스크가 장기화될 수 있기 때문임.",
        "key_companies": [],
        "insight": "원유 공급선이 열리더라도 지정학적 불안이 남긴 상흔(시설 파괴 및 보험료 상향)은 물류 및 에너지 공급망 전체에 <span class=\"text-violet-300 font-medium\">영구적인 추가 비용 구조</span>를 장착시킴. 이는 에너지 가격의 하방 지지선을 높이고 고물가 장기화 요인으로 작용함.",
        "action_point": "유가의 빠른 안정화를 가정한 공격적인 금리 인하 수혜주 투자(중소형 성장주 등) 비중을 일시적으로 조율하고, 전통 <span class=\"text-cyan-300 font-semibold\">에너지 기업 및 조선/해운 물류</span> 업종의 마진 방어 능력을 평가해 포트폴리오를 구성해야 함."
      },
      "classification": {
        "primary_topic": "energy",
        "secondary_topics": ["economy"],
        "tags": ["국제유가", "지정학적리스크", "운송비상승", "보험료상승"]
      }
    }
  }
}

pending_dir = Path("data/pending")
analyzed_root = Path("data/analyzed")

for video_id, item in batch1_data.items():
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

print("Batch 1 processing completed successfully.")
