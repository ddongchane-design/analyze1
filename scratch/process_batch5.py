import json
from pathlib import Path

# Define the analyzed data for Batch 5
batch_data = {
  "RSOtKvknTKg": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "RSOtKvknTKg",
        "title": "흔들리는 시장... 대응 전략은 무엇? | 박병창 MP파트너스 대표 [마켓 인사이드]",
        "published": "2026-06-10T06:45:21+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=RSOtKvknTKg",
        "thumbnail": "https://img.youtube.com/vi/RSOtKvknTKg/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 미국 반도체 기술주 중심의 하락과 동조화되어 코스피가 단기 조정을 겪는 것은 10주간 연속 상승에 따른 정상적인 <span class=\"text-amber-300 font-bold\">수급 과열 해소 과정(매물 소화)</span>입니다.\n2. 음봉이 크게 떨어진 이후 모멘텀 부재로 지수가 하락 테스트를 진행 중이지만, 이는 대세 하락장 전환보다는 단기적인 이격도 조정 흐름에 해당합니다.\n3. 단기 일희일비식 초단타 매매(인파이터)보다는 시장 흐름을 여유 있게 바라보며(아웃복서) 리스크 관리와 비중 조절에 힘써야 할 구간입니다.",
        "key_claims": [
          "최근의 주가 급락은 장기 상승 추세선의 붕괴가 아닌, 과매수권에 진입했던 기술주들의 <span class=\"text-rose-400 font-medium\">단기 매물 압박 해소</span> 과정입니다.",
          "미국 증시 및 반도체 지수의 변동성이 여전히 높아 국내 증시도 며칠간 추가 하방 테스트를 진행하는 <span class=\"text-rose-400 font-medium\">불안정한 수급 구간</span>이 이어질 수 있습니다.",
          "시장 고수를 모방해 추격 매수나 조급한 매도를 하기보다 현금 및 안전자산 비중을 보유하며 지지선 형성을 기다리는 것이 합리적입니다."
        ],
        "data_points": [
          "주봉 기준 최근 코스피 약 10주 연속 상승세를 기록한 후 상단 채널에서 조정 진입",
          "나스닥 및 필라델피아 반도체 지수 단기 4~5일 연속 하락 영향 동조화"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "추세 붕괴의 신호는 없으나 단기 변동성과 추가 지지선 확인 과정이 여전히 진행 중이므로 신중한 관망이 요구되는 중립 상태입니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)"
        ],
        "insight": "지수가 장기 상승폭의 피로를 해소하기 위해 가격 조정을 받는 국면입니다. 이러한 매물 소화 과정을 거쳐야 향후 <span class=\"text-cyan-300 font-semibold\">실적 시즌 돌입 시</span> 더 견고한 상승 지지대를 형성할 수 있습니다.",
        "action_point": "과도한 공격적 레버리지 투자를 자제하여 계좌의 안전성을 유지하고, 지수가 60일 이동평균선 등 <span class=\"text-cyan-300 font-semibold\">주요 지지 구간</span>에 진입할 때 주도주 분할 매수를 개시하는 전략이 필요합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.4
      }
    }
  },
  "ss9v_xP806I": {
    "topic": "tech",
    "content": {
      "video": {
        "id": "ss9v_xP806I",
        "title": "테슬라 자율주행도 여기선 찬밥입니다 (KB증권 아시아시장팀 박수현 팀장)",
        "published": "2026-06-10T12:00:16+00:00",
        "channel_name": "언더스탠딩_Understanding",
        "url": "https://www.youtube.com/watch?v=ss9v_xP806I",
        "thumbnail": "https://img.youtube.com/vi/ss9v_xP806I/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 중국 내 자율주행 시장은 테슬라의 FSD 도입 기대감에도 불구하고, 로컬 데이터와 신뢰도를 선점한 <span class=\"text-cyan-300 font-semibold\">모멘타(Momenta) 및 화웨이(Huawei)</span> 등의 현지 업체들이 강한 주도권을 쥐고 있습니다.\n2. 중국 정부는 전국적으로 자율주행 레벨 2부터 레벨 4까지 동시다발적인 시범구를 지정해 기술 간 치열한 실전 경쟁과 인프라 고도화를 유도하고 있습니다.\n3. 가성비를 앞세운 중국 토종 전기차와 고도로 현지화된 ADAS(자율주행보조) 연동 기술로 인해 테슬라의 중국 내 입지 및 점유율이 심각한 위협을 받고 있습니다.",
        "key_claims": [
          "중국 전기차 시장의 빠른 기술 상향 평준화로 인해 자율주행 소프트웨어 영역마저 중국 로컬 업체들의 <span class=\"text-cyan-300 font-semibold\">데이터 현지 점유율 독점</span>이 심화되고 있습니다.",
          "지역별 동시다발적 시범 배포를 통한 규제 샌드박스 활성화는 중국 자율주행 경쟁력을 <span class=\"text-amber-300 font-bold\">글로벌 최상위 수준</span>으로 빠르게 도약시키는 핵심 동력입니다.",
          "자율주행의 핵심인 AI 인지 및 모션 데이터 처리에 있어 화웨이가 중국 내 벤더 생태계를 빠르게 통합하고 있습니다."
        ],
        "data_points": [
          "중국 내 자율주행 시범 도시 테스트 단계: ADAS(L2)부터 자율주행 무인화(L4)까지 동시 적용",
          "중국 로컬 대표 자율주행 기술 기업: 모멘타(Momenta), 화웨이(Huawei)"
        ],
        "signal": "bearish",
        "signal_confidence": "high",
        "signal_reason": "테슬라의 핵심 성장 비전인 자율주행(FSD) 경쟁력이 최대 시장인 중국에서 현지 로컬 동맹(화웨이 등)의 저가 및 맞춤 데이터 공세로 위상이 위협받고 있습니다.",
        "key_companies": [
          "테슬라(TSLA)",
          "화웨이(Huawei)"
        ],
        "insight": "중국의 모빌리티 시장은 소프트웨어 주도권마저 철저히 로컬 기업들 위주로 재편되고 있습니다. 테슬라의 중국 내 시장 장악력 회복은 쉽지 않을 것이며, 자국 반도체 자급화 기조와 결합한 <span class=\"text-violet-300 font-medium\">중국 중심의 독자 자율주행 플랫폼</span>이 글로벌 시장의 위협으로 부상할 것입니다.",
        "action_point": "테슬라의 중국 및 아시아 시장 밸류에이션 둔화 리스크를 감안해 전기차 완제품 투자에는 신중을 기하고, 로컬 자율주행 시스템에 부품을 공급하는 <span class=\"text-cyan-300 font-semibold\">국내 정밀 센서 및 모빌리티 PCB 부품사</span>로 포커스를 전환해야 합니다."
      },
      "classification": {
        "primary_topic": "tech",
        "relevance_score": 9.5
      }
    }
  },
  "Swfnylswdk4": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "Swfnylswdk4",
        "title": "백화점주 놓쳤다면 호텔주? 지금 봐야 할 포인트ㅣ명민준, 강아랑, 정태근 [주린이 구조대]",
        "published": "2026-06-10T12:45:12+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=Swfnylswdk4",
        "thumbnail": "https://img.youtube.com/vi/Swfnylswdk4/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 고환율 및 인바운드 외국인 소비 급증 영향으로 명품 판매가 호조를 보인 백화점주가 이미 역사적 랠리를 펼침에 따라, 다음 순환매 후보로 <span class=\"text-cyan-300 font-semibold\">호텔 및 카지노, 관광 개발 업종</span>이 지목되고 있습니다.\n2. 해외 여행객 유입 속도 대비 내수 백화점 소비 비중을 넘어서는 호텔/레저 섹터의 영업이익 턴어라운드가 가시화되고 있습니다.\n3. 시장 전반의 대형 반도체 기술주 변동성 국면에서 밸류에이션 매력과 안정적 외화 수입 구조를 가진 리프레시 업종이 대안처로 부상 중입니다.",
        "key_claims": [
          "엔저 수혜를 보던 일본 관광객 유입과 원화 약세 효과가 결합해 한국 관광 및 <span class=\"text-amber-300 font-bold\">인바운드 레저 소비 볼륨</span>이 구조적으로 팽창하고 있습니다.",
          "신세계, 현대백화점 등 명품 백화점주 상승에 이어 호텔신라, 파라다이스 같은 리조트/레저 관련 기업으로의 <span class=\"text-cyan-300 font-semibold\">수급 이동(섹터 로테이션)</span> 징후가 나타납니다.",
          "전기차와 달리 유가 및 거시 리스크 방어가 용이한 무형의 서비스/관광 인프라 업종의 방어력이 돋보입니다."
        ],
        "data_points": [
          "외국인 인바운드 관광객 결제액 급증 수치 및 신세계 본점 등 유통주 주가 3월 대비 약 2배 급등 데이터 공유"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "원화 약세 기조 장기화로 외국인 유입 혜택을 직접 받는 유통 섹터의 훈풍이 아직 오르지 않은 호텔 및 카지노, 관광 인프라 업종으로 확산되어 순환매 턴어라운드가 기대됩니다.",
        "key_companies": [
          "호텔신라(008770)",
          "파라다이스(034230)",
          "롯데관광개발(032350)",
          "신세계(004170)"
        ],
        "insight": "백화점 대형주들의 밸류에이션 리레이팅이 완료된 시점에서, 동일한 환율 효과(수혜)를 공유하면서 상대적으로 주가가 바닥권에 머물고 있는 <span class=\"text-cyan-300 font-semibold\">호텔/면세점/카지노 섹터</span>의 밸류에이션 매력이 극대화되었습니다. 실질적인 실적 턴어라운드가 지표로 증명되는 단계입니다.",
        "action_point": "이미 주가가 크게 상승한 명품 유통 대형주 신규 매수는 지양하고, 수급이 돌기 시작하는 <span class=\"text-cyan-300 font-semibold\">호텔신라 및 카지노 대장주</span>를 선제적으로 매수해 포트폴리오의 매크로 헷지 수단으로 활용하는 전략이 유리합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.2
      }
    }
  },
  "Uqpf0G9__n0": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "Uqpf0G9__n0",
        "title": "[지식뉴스] \"그거 착시예요, 이제 연준 풋(Fed Put)은 끝났습니다\" 지금 AI•반도체가 흔들리는 진짜 이유 (ft.김명실 iM증권 연구위원) / 교양이를 부탁해",
        "published": "2026-06-10T10:45:20+00:00",
        "channel_name": "교양이를 부탁해",
        "url": "https://www.youtube.com/watch?v=Uqpf0G9__n0",
        "thumbnail": "https://img.youtube.com/vi/Uqpf0G9__n0/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 미국 고용 지표의 겉보기 강세는 실업자 분류 및 왜곡에 따른 착시이며, 실제 가계 실질 임금 하락과 구매력 감퇴로 인해 <span class=\"text-rose-400 font-medium\">실물 경기 둔화 리스크</span>가 심화되고 있습니다.\n2. CME 페드워치(FedWatch) 기준 12월 연준의 연내 금리 인하 확률은 1% 미만으로 전락한 반면, 1회 이상 인상 확률은 72.3%로 폭증하는 등 정책 방향성의 대대적인 수정이 일어났습니다.\n3. 시장의 장기 심리 마진호선이었던 미 국채 10년물 4.5% 돌파 및 30년물 5.0% 돌파는 연준이 더 이상 증시를 방어하지 않는다는 <span class=\"text-rose-400 font-medium\">'연준 풋(Fed Put)의 종말'</span>을 의미합니다.",
        "key_claims": [
          "실질 소득 감소와 가계 구매력 이탈은 미국 경기 둔화의 명확한 신호이며, 최근의 견조한 지표들은 통계적 <span class=\"text-rose-400 font-medium\">고용 분류 왜곡 착시</span>에 해당합니다.",
          "미 국채 금리의 지속적 상승과 금리 인하 차단(동결 및 추가 인상 테이블 복귀)은 할인율을 높여 그간 밸류에이션 버블을 지탱하던 <span class=\"text-rose-400 font-medium\">기술 성장주들의 자금 이탈</span>을 촉발합니다.",
          "연준은 경제 고용 훼손을 방치하지 않는 선에서 통화 긴축 주기를 이전 예측보다 더 길고 강력하게 끌고 갈 가능성이 높습니다."
        ],
        "data_points": [
          "CME 패드워치 12월 FOMC 기준 금리 인하 확률: 0.8%로 급감 (동결 확률 26.9%)",
          "12월 FOMC 기준 추가 금리 인상(1회 이상) 베팅 확률: 72.3%로 폭증",
          "미 국채 10년물 금리 심리적 마진호선인 4.5% 돌파, 30년물 금리 5.0% 상향 돌파"
        ],
        "signal": "bearish",
        "signal_confidence": "high",
        "signal_reason": "연준 풋의 공식적인 소멸과 추가 금리 인상 확률의 급증(72%), 미국 국채 금리 동반 폭등은 자산 가격 평가 기준을 재조정해 시장의 하방 변동성을 키우고 있습니다.",
        "key_companies": [],
        "insight": "시장은 오랜 기간 연준이 결국 완화(금리 인하)로 돌아서 증시를 부양할 것이라는 안도감(Fed Put)을 가졌으나, 재정 적자 심화와 인플레 압박으로 인해 이 가정이 완전히 붕괴되었습니다. 이는 시장 밸류에이션의 구조적 <span class=\"text-rose-400 font-medium\">할인율 상승 압박</span>으로 연결되고 있습니다.",
        "action_point": "금리 고공행진에 민감한 고부채 중소형 성장주와 기술 레버리지 상품을 축소하고, <span class=\"text-cyan-300 font-semibold\">실제 현금 수익성(Cash-flow)</span>이 증명되는 반도체 독점 기업 및 이자율 상승 수혜 대형 금융 섹터로 대피해야 합니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.6
      }
    }
  },
  "vqiQOKmaMGA": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "vqiQOKmaMGA",
        "title": "\"고점 예측 금지\" 어차피 주도주 바뀌지 않습니다. 진짜 챙겨야 할 대응의 영역은?ㅣ홍선애, 박병창 MP파트너스 [여의도 인사이트]",
        "published": "2026-06-10T21:47:30+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=vqiQOKmaMGA",
        "thumbnail": "https://img.youtube.com/vi/vqiQOKmaMGA/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 극심한 시장 변동성(사이드카 빈번 작동) 속에서 개인 투자자들은 조급한 단기 거래(인파이터)를 지양하고, 시장 흐름을 한 발짝 물러서서 관망하는 <span class=\"text-cyan-300 font-semibold\">아웃복서의 태도</span>를 견지해야 합니다.\n2. 증시의 단기 고점을 인위적으로 예단하여 주도주를 성급히 처분하기보다는, 하방이 확인된 핵심 반도체 주도주 비중을 유지하는 전략이 합리적입니다.\n3. 매크로 충격과 옵션 만기, 증자 이슈에 따른 단기 수급 왜곡 속에서 리스크(레버리지) 통제 및 포트폴리오 압축만이 실질적인 대응의 영역입니다.",
        "key_claims": [
          "시장 참여자들이 단기 급등락에 흥분하고 절망하는 심리적 롤러코스터는 장기 자산 성장에 해가 되므로 <span class=\"text-amber-300 font-bold\">객관적 거리두기</span>가 최우선입니다.",
          "단기 밸류에이션 고평가 논란에도 불구하고 AI 패러다임과 기업 실적 모멘텀상 <span class=\"text-cyan-300 font-semibold\">핵심 반도체 주도주의 위상</span>은 쉽게 변화하지 않을 것입니다.",
          "개인이 통제할 수 없는 매크로(전쟁, 유가, 금리) 변수 예측에 몰두하기보다는 자신의 <span class=\"text-rose-400 font-medium\">신용/미수 레버리지 비율 축소</span>와 같은 대응에 집중해야 합니다."
        ],
        "data_points": [
          "옵션 만기 및 지정학(미국-이란 보복 타격)에 따른 양시장 변동성 급증 상황 언급"
        ],
        "signal": "neutral",
        "signal_confidence": "high",
        "signal_reason": "단기 고점 확인과 매물 출회 국면이지만 주도주 위상의 훼손은 포착되지 않아 무리한 비중 축소나 신규 추격 매수 대신 계좌 내 리스크를 다스리는 중립적 관찰 구간입니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)"
        ],
        "insight": "변동성 국면에서 투자의 성패는 종목 예측이 아니라 자금의 성격(레버리지 유무)이 결정합니다. 고가 매수 대기 자금이 충분한 반도체 대장주는 <span class=\"text-cyan-300 font-semibold\">단기 매물 압박</span>을 소화한 뒤 강하게 반등할 것입니다.",
        "action_point": "인위적인 단기 고점 매도 베팅(인버스 등)이나 섣부른 테마주 이동을 피하고, 60일선 등 기술적 지지선 안착을 확인한 뒤 <span class=\"text-cyan-300 font-semibold\">삼성전자 및 하이닉스</span>를 모아가는 기본형 전략에 충실해야 합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.5
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
