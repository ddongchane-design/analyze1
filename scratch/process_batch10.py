import json
from pathlib import Path

# Define the analyzed data for Batch 10
batch_data = {
  "ywxFo29e2JA": {
    "topic": "etc",
    "content": {
      "video": {
        "id": "ywxFo29e2JA",
        "title": "Show me market! #2026년 5월 고객자산배분전략 #shorts",
        "published": "2026-05-11T00:00:00+00:00",
        "channel_name": "미래에셋증권",
        "url": "https://www.youtube.com/watch?v=ywxFo29e2JA",
        "thumbnail": "https://img.youtube.com/vi/ywxFo29e2JA/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 5월 시장 자산 배분 전략으로 점진적 리스크온(Risk-on) 관점이 제시되었습니다.\n2. 유가 변동성 헷지를 위해 <span class=\"text-amber-300 font-bold\">금을 통한 위험 관리</span>를 병행하고, AI 반도체 및 전력 인프라 등 2분기 주도 섹터의 분할 매수를 제안했습니다.\n3. 2분기 모멘텀이 극대화되는 <span class=\"text-cyan-300 font-semibold\">우주 테마</span>를 신규 포트폴리오 기회로 제시했습니다.",
        "key_claims": [
          "5월 시장은 단순 추격 매수보다 물가, 금리 부담을 고려한 <span class=\"text-amber-300 font-bold\">단계적 확인 매수</span>가 유효합니다.",
          "반도체와 전력 인프라 외에 2분기에 모멘텀이 촉발되는 우주 항공 테마가 매력적인 분산 기회가 됩니다.",
          "포트폴리오의 안정성 밸런스를 잡기 위해 실물 안전 자산인 금의 헤지 비중을 유지해야 합니다."
        ],
        "data_points": [
          "5월 자산 배분 제안: 점진적 리스크온 비중 확대",
          "추천 포트폴리오: 반도체, 전력 인프라, 우주 테마, 금(Gold)"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "실적 장세 유입 기대가 있으나, 유가 상승에 의한 물가 경계가 남아 있어 점진적인 비중 조절을 제안합니다.",
        "key_companies": [
          "미래에셋증권(006800)"
        ],
        "insight": "5월 시장 전략은 금리 경계 심리가 상존하는 가운데 AI 전방 하드웨어와 우주라는 신규 개척 분야로의 영리한 분산 투자를 권고하고 있습니다.",
        "action_point": "반도체와 우주 섹터 중심으로 요일별 분할 매수하되, 자산의 10% 내외는 금 관련 자산으로 헷지하는 것이 바람직합니다."
      },
      "classification": {
        "primary_topic": "etc",
        "relevance_score": 8.0
      }
    }
  },
  "z5NSiy8N3IA": {
    "topic": "space",
    "content": {
      "video": {
        "id": "z5NSiy8N3IA",
        "title": "아르테미스 Ⅲ 우주인, 스펙이 영화보다 더하다",
        "published": "2026-06-11T06:00:00+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=z5NSiy8N3IA",
        "thumbnail": "https://img.youtube.com/vi/z5NSiy8N3IA/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. NASA의 아르테미스 III 달 남극 도킹 미션에 투입될 우주비행사들의 고스펙과 풍부한 베테랑 경험을 소개했습니다.\n2. 4개의 학위와 장비 개발 이력을 지닌 안드레 더글라스, 미국 최장 우주 체류 기행을 한 프랭크 루비오 등이 선발되었습니다.\n3. 이탈리아 최고참 우주인 루카 파르미타노, 90종 기종을 조종한 탑건 출신 랜디 브레스닉 등 과학적/공학적 역량을 겸비한 전문가들로 팀이 구성되었습니다.",
        "key_claims": [
          "달 착륙 도킹 미션은 극도의 위험성이 따르기 때문에 파일럿 및 기계 제어 전문가 등 <span class=\"text-cyan-300 font-semibold\">베테랑 중의 베테랑</span> 위주로 차출되었습니다.",
          "선발된 우주인들은 단순 조종사가 아니라 의사, 공학 박사 등 멀티 태스킹이 가능한 <span class=\"text-cyan-300 font-semibold\">융합형 인재</span>들입니다.",
          "우주 유영 중 헬멧 내부 물 고임 같은 생사 갈림길의 사고를 극복한 정신력 보유자들이 주축을 이룹니다."
        ],
        "data_points": [
          "아르테미스 III(Artemis III) 달 도킹 유인 우주 미션 우주비행사 선발 완료",
          "탑건 출신 랜디 브레스닉: 90여 개 기종 조종, 비행 시간 7,000시간 이상 기록"
        ],
        "signal": "na",
        "signal_confidence": "high",
        "signal_reason": "우주 비행사들의 프로필과 미션 준비 상황을 다룬 정보성 교양 콘텐츠로, 상업적 투자 시그널을 도출하기에는 적합하지 않습니다.",
        "key_companies": [
          "NASA",
          "스페이스X"
        ],
        "insight": "아르테미스 계획의 최종 달 착륙에 투입될 인력의 수준은 극도로 조율되어 있으며, 이는 상업 우주 개발 단계로 진입하기 전 국가 단위의 기술적 완성도와 신뢰성을 높이기 위한 전략적 결정입니다.",
        "action_point": "민간 우주 개발에 앞서 유인 달 착륙 인프라 기술을 보유한 NASA 및 락히드마틴 등 글로벌 방산/우주 기업들의 장기 연구 개발 가이드라인으로 참고할 가치가 있습니다."
      },
      "classification": {
        "primary_topic": "space",
        "relevance_score": 7.5
      }
    }
  },
  "zkNjd_eAMog": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "zkNjd_eAMog",
        "title": "반도체만이 아닙니다, 이번 슈퍼 사이클 한국이 끝까지 1등인 결정적 증거가 있습니다ㅣ김효진 신영증권 박사 [풀영상]",
        "published": "2026-06-11T07:00:00+00:00",
        "channel_name": "이호석아카데미",
        "url": "https://www.youtube.com/watch?v=zkNjd_eAMog",
        "thumbnail": "https://img.youtube.com/vi/zkNjd_eAMog/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. AI 기술 혁신이 자아내는 폭발적 생산성 때문에 기존의 금리 인상 시 주가 하락 공식이 깨지며 시장의 <span class=\"text-amber-300 font-bold\">금리 민감도가 급격히 하락</span>했습니다.\n2. 효율이 증가할 때 비용 감소로 오히려 수요가 폭증하는 <span class=\"text-cyan-300 font-semibold\">제본스의 역설(Jevons' Paradox)</span>이 개발자 채용 시장 및 AI 메모리 인프라 소비에서 뚜렷하게 증명되고 있습니다.\n3. 한국은 과거 유가 충격에 극도로 취약했으나, 현재는 강력해진 반도체 수출 체력이 원유 수입 비용 증가를 완벽히 상쇄(헷지)하여 <span class=\"text-cyan-300 font-semibold\">매크로 안정성을 구조적으로 확보</span>했습니다.",
        "key_claims": [
          "연준 내부에서도 AI의 생산성 파급력에 대한 명확한 합의가 없어 통화 정책의 일관된 기조가 무력화되었습니다.",
          "OpenAI와 앤스로픽이 10~11월 상장을 공식 목표로 삼고 있어 하반기까지 AI 가속기 및 <span class=\"text-cyan-300 font-semibold\">HBM 수요 증설 경쟁</span>은 멈추지 않을 것입니다.",
          "과거에는 유가 상승 시 주식회사 대한민국 전체의 무역수지가 박살 났으나, 현재는 반도체 가격의 높은 마진이 <span class=\"text-violet-300 font-medium\">에너지 비용을 압도</span>하고 있습니다."
        ],
        "data_points": [
          "한국과 대만 반도체 수출 급증세 지속 (수출액 전년 대비 50% 이상 폭증 기록)",
          "글로벌 AI 랩들의 모델 업그레이드 주기 단축: 과거 1년 주기에서 최근 3주 단위로 가속화",
          "앤스로픽, 오픈AI 상장 목표 시점: 2026년 10월~11월 타겟팅 설정",
          "역사적 수치: 2010년대 중반 이전 원유 수입액이 반도체 수출액의 2배 규모였으나 현재는 반도체 수출액이 압도적 우위"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "미국의 고금리 장기화 불안에도 불구하고 AI 특이점 가속화로 반도체 CapEx의 정점이 연장되고 있으며, 한국 무역 구조가 에너지 리스크를 자체 극복할 만큼 체력이 개선되었습니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)",
          "신영증권(001720)",
          "네이버(035420)"
        ],
        "insight": "AI 생산성 파급력은 거시 인플레이션 논리를 무력화할 정도로 폭발적입니다. 특히 효율성이 오를 때 수요가 줄어드는 대신 오히려 시장이 기하급수적으로 확장되는 '제본스의 역설'은 모바일 AIPC 및 소프트웨어 에이전트 시장 전체의 장기 팽창을 지지합니다.",
        "action_point": "거시 유가 상승이나 미 연준의 금리 변동 발언으로 인해 국내 주도주들이 동반 조정을 받을 때, 흔들리지 말고 포트폴리오 내 반도체 대형주 비중을 과감히 높여가야 합니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.7
      }
    }
  },
  "zztLNzwdvv8": {
    "topic": "etc",
    "content": {
      "video": {
        "id": "zztLNzwdvv8",
        "title": "Risk-on, but flexible! #2026년 6월 고객자산배분전략 #shorts",
        "published": "2026-06-11T08:00:00+00:00",
        "channel_name": "미래에셋증권",
        "url": "https://www.youtube.com/watch?v=zztLNzwdvv8",
        "thumbnail": "https://img.youtube.com/vi/zztLNzwdvv8/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 6월 자산 배분 전략으로 선별적 리스크온 유지와 더불어 단기 변동성에 대비한 <span class=\"text-amber-300 font-bold\">일부 차익 실현(현금 확보)</span>을 추천했습니다.\n2. 메모리, 전력, 네트워크 등 AI 인프라 전반으로 수혜가 확산되고 있으나, 지정학 및 긴장 완화 협상 기조에 따른 변동성을 유념해야 합니다.\n3. 채권은 단기 중심으로 조율하고, 대체 자산에서는 금 대신 <span class=\"text-cyan-300 font-semibold\">전략 금속 및 희토류 포트폴리오</span>를 대안으로 제시했습니다.",
        "key_claims": [
          "6월 시장은 1분기 어닝 서프라이즈 온기가 이어지나 기술적 과열 구간에 진입해 숨고르기가 필요합니다.",
          "미 중앙은행의 긴축 기조 전환 논쟁 및 이란 지정학적 회담 일정 등 시장을 흔들 매크로 변수가 많습니다.",
          "포트폴리오의 탄력성을 위해 금보다 전기차 및 첨단 소부장에 필수적인 희토류/전략금속 비중 확대를 추천합니다."
        ],
        "data_points": [
          "6월 자산 배분 제안: 선별적 리스크온 유지 및 부분 차익 실현",
          "추천 포트폴리오: 단기 채권, 전략 금속 및 희토류, AI 인프라(메모리/전력)"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "실적 모멘텀은 굳건하나, 지수의 기술적 고점 이격 발생과 대외 지정학 이벤트에 유연하게 대처할 수 있도록 현금 비중 확대를 제안합니다.",
        "key_companies": [
          "미래에셋증권(006800)"
        ],
        "insight": "6월 시장은 주도 테마의 장기 상승력을 신뢰하되, 돌발 변수(FMC, 지정학) 충격을 완화할 수 있도록 방어용 현금 소총과 특수 희토류 자산 믹스를 균형 있게 배분하는 기민함이 요구됩니다.",
        "action_point": "AI 반도체 및 전력 관련 보유 지분 중 일부(10~15%)를 매도해 현금화하고, 단기 국채 및 희토류 관련 자산의 편입 비율을 소폭 늘리는 자산 리밸런싱을 권고합니다."
      },
      "classification": {
        "primary_topic": "etc",
        "relevance_score": 8.2
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
