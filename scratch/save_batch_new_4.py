import json
from pathlib import Path

def save_and_delete(video_id, primary_topic, secondary_topics, tags, analysis_data):
    pending_path = Path(f"data/pending/{video_id}.json")
    if not pending_path.exists():
        print(f"Warning: {pending_path} does not exist.")
        return
        
    pending_data = json.loads(pending_path.read_text(encoding="utf-8"))
    video_data = pending_data["video"]
    
    classification_data = {
        "primary_topic": primary_topic,
        "secondary_topics": secondary_topics,
        "tags": tags
    }
    
    analyzed_dir = Path(f"data/analyzed/{primary_topic}")
    analyzed_dir.mkdir(parents=True, exist_ok=True)
    
    result_path = analyzed_dir / f"{video_id}.json"
    result_path.write_text(
        json.dumps({
            "video": video_data,
            "analysis": analysis_data,
            "classification": classification_data
        }, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"Saved: {result_path}")
    
    pending_path.unlink()
    print(f"Deleted pending: {pending_path}")
    
    synthesis_cache = Path(f"data/synthesis/{primary_topic}.json")
    if primary_topic != "economy" and synthesis_cache.exists():
        synthesis_cache.unlink()
        print(f"Invalidated cache: {synthesis_cache}")

batch_data = {
  "bDI7Nns6Cvk": {
    "primary_topic": "etc",
    "secondary_topics": [],
    "tags": ["감탄의효과", "인정욕구", "소통기술", "인정문화", "동기부여"],
    "analysis": {
      "summary": "방청객의 기계적인 호응이 강사의 내재적 동기를 자극해 실제 명강의로 이어지는 과정을 조명하며, 소통에서의 <span class=\"text-cyan-300 font-semibold\">상호 피드백의 힘</span>을 설명합니다. 단순한 칭찬의 영역을 넘어 상대방의 행동에 진심 어린 놀라움과 가치를 부여하는 '감탄'이 소통의 주체를 긍정적으로 변화시키는 선순환을 유도합니다. 한국 사회에 타인의 도전을 인정하고 함께 감탄해 주는 <span class=\"text-amber-300 font-bold\">성숙한 지지와 공감의 문화</span>가 더욱 확산되어야 할 시점입니다.",
      "key_claims": [
        "처음에는 기계적으로 유도된 감탄 리액션이었을지라도 강사에게 전달되는 순간 <span class=\"text-cyan-300 font-semibold\">자기효능감และ 흥미를 폭발</span>시키는 뇌 과학적 촉매 역할을 합니다.",
        "소통 주체 간의 교감이 강화되면서 수동적인 방청 분위기가 자발적인 동참과 <span class=\"text-amber-300 font-bold\">몰입의 선순환 구조</span>로 변화합니다.",
        "일방적인 평가나 칭찬보다 상대의 가치를 극대화하는 '감탄의 리액션'이 개인과 공동체의 심리적 기초 체력을 키우는 핵심 열쇠입니다."
      ],
      "data_points": [
        "효과적인 의사소통 메커니즘: 기계적 리액션 -> 내재적 동기 부여 -> 자발적 몰입과 주의 집중 전환"
      ],
      "signal": "na",
      "signal_reason": "대중 강연 경험을 토대로 소통과 공감 문화의 중요성을 역설하는 인문 심리 에세이 형식의 콘텐츠이므로 금융 투자와의 연관성은 없습니다.",
      "key_companies": [],
      "insight": "개인의 성과 창출과 조직의 생산성은 단순한 물질적 보상뿐 아니라, 서로의 노력에 대해 아낌없이 박수치고 <span class=\"text-amber-300 font-bold\">감탄을 표현하는 문화</span> 속에서 극대화됩니다. 이는 인적 자본의 창의성을 자극하는 보이지 않는 인프라입니다.",
      "action_point": "조직 내 소통 효율성 제고 및 구성원 동기 부여 프로그램을 검토할 때, 피드백의 정성적 수준을 평가 위주에서 <span class=\"text-cyan-300 font-semibold\">상호 지지와 감탄 중심</span>으로 재설계해야 합니다."
    }
  },
  "epEDUo3dhJc": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["SK하이닉스상장", "메타자체칩", "애플소송", "호르무즈해협", "우주데이터센터"],
    "analysis": {
      "summary": "빅테크 실적 시즌을 앞두고 미국 S&P500 지수가 전고점에 재임박한 가운데, SK하이닉스가 미국 나스닥 ADR 상장 첫날 약 13% 급등하며 <span class=\"text-cyan-300 font-semibold\">글로벌 메모리 반도체 랠리</span>를 재점화했습니다. 메타의 자체 AI 칩 양산 임박 소식과 함께 마이크로소프트 등의 견조한 AI CAPEX 투자가 지속되며 거품 우려가 완화되었습니다. 다만 중동 호르무즈 해협의 이란 혁명수비대와 미군의 공습 대치로 인한 <span class=\"text-violet-300 font-medium\">지정학적 리스크</span>와 유가 변동성 관리가 금주 CPI 발표와 맞물려 핵심 변수로 작용할 전망입니다.",
      "key_claims": [
        "SK하이닉스의 ADR(SKY) 데뷔전 성공은 글로벌 유동성이 한국 메모리 반도체 밸류체인의 독보적 지위를 인정하고 <span class=\"text-cyan-300 font-semibold\">멀티플 리레이팅</span>을 시작했음을 의미합니다.",
        "애플의 오픈 AI 영업비밀 유출 소송 제기는 하드웨어 중심 애플이 AI 소프트웨어 리더십 경쟁에서 겪는 <span class=\"text-rose-400 font-medium\">구조적 초조함</span>이 표출된 결과입니다.",
        "이란 혁명수비대의 선박 미사일 공격과 미군의 보복 공습으로 호르무즈 해협 긴장이 고조되었으나, 트럼프 대선 가도 인플레 억제 압박에 따라 <span class=\"text-violet-300 font-medium\">제한적 긴장 상태</span>로 유지될 가능성이 높습니다."
      ],
      "data_points": [
        "SK하이닉스 미국 나스닥 ADR(SKY) 상장 첫날 종가 상승률: 공모가(149달러) 대비 13% 급등한 168달러 마감",
        "메타(Meta) 주가 당일 급등률: 자체 인프라 칩 개발 가시화로 6% 상승 기록",
        "미국 GDP 성장에서 AI 지출(Spending)이 기여하는 비중: 약 25% 이상 차지"
      ],
      "signal": "bullish",
      "signal_reason": "빅테크 기업들의 강력한 실적 기대감과 AI 인프라 수요의 견조함이 하이닉스 나스닥 데뷔 흥행과 글로벌 지수 최고점 근접으로 증명되고 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "Meta(META)", "Apple(AAPL)"],
      "insight": "ADR 상장을 통한 대규모 자금 확보와 글로벌 시장 편입은 SK하이닉스의 마이크론 대비 밸류에이션 할인을 해소하는 결정적 계기입니다. AI 소프트웨어(메타 등)의 비용 통제와 하드웨어(반도체)의 실질 이익이 교차하며 <span class=\"text-cyan-300 font-semibold\">실적 위주의 견고한 장세</span>가 이어지고 있습니다.",
      "action_point": "ADR 프리미엄이 안착함에 따라 국내 반도체 본주 및 관련 장비 밸류체인을 포트폴리오 핵심으로 보유하되, 호르무즈 해협 긴장에 대비한 <span class=\"text-violet-300 font-medium\">에너지 및 유가 수혜주</span>를 헤지 자산으로 배치할 필요가 있습니다."
    }
  },
  "gpSB9o6W4GY": {
    "primary_topic": "tech",
    "secondary_topics": ["economy"],
    "tags": ["삼성기초연구", "대기업R&D", "장기투자", "과학기술선순환", "실패용인문화"],
    "analysis": {
      "summary": "대한민국 대기업들, 특히 삼성전자가 매년 대규모 자금을 미래 과학기술과 기초 연구에 장기 투자하며 국내 과학 인프라 발전을 주도하고 있습니다. 10년 뒤의 장기적 성과를 내다보는 끈기 있는 투자 기조와 실패를 용인하는 연구 문화가 뒷받침될 때 비로소 국가적인 <span class=\"text-cyan-300 font-semibold\">초격차 기술 확보</span>가 가능합니다. 대기업들의 선도적인 기술 재투자는 한국 과학 기술계 전반에 우수 인재 육성과 지식 축적이라는 <span class=\"text-amber-300 font-bold\">선순환 생태계</span>를 정착시키는 원동력입니다.",
      "key_claims": [
        "당장의 단기 이익 창출에 연연하지 않고 기초 과학과 핵심 공학에 수조 원 규모의 <span class=\"text-cyan-300 font-semibold\">장기 R&D 투자</span>를 단행하는 문화가 필수적입니다.",
        "삼성, SK, LG, 현대차 등 대기업들의 상생형 미래 연구 지원 사업이 국내 대학 및 연구원들의 원천 기술 경쟁력을 한 단계 레벨업하고 있습니다.",
        "실패를 단순한 손실이 아닌 미래 지적 자산의 축적 과정으로 인정하는 유연한 기업 문화가 혁신적 성과의 기반이 됩니다."
      ],
      "data_points": [
        "삼성전자의 연간 기초 및 원천 기술 연구 투자 규모: 미래기술육성사업 등을 통해 지속적인 재원 투입"
      ],
      "signal": "neutral",
      "signal_reason": "대기업들의 기초 과학 투자 의의와 긍정적 파급 효과를 설명하는 거시적 관점의 콘텐츠로, 개별 기업의 단기 주가 흐름을 직접적으로 움직이는 요소는 아니기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "LG화학(051910)"],
      "insight": "글로벌 공급망 재편 속에서 하드웨어와 소재 원천 기술 확보는 국가 안보와도 직결됩니다. 기업들이 단기 분기 실적에만 매몰되지 않고 <span class=\"text-cyan-300 font-semibold\">원천 기술 포트폴리오</span>를 넓혀갈 수 있도록 유인하는 세제 혜택 등 정책적 뒷받침이 더욱 중요해지고 있습니다.",
      "action_point": "자체적인 원천 기술 R&D 역량을 지니고 연구 개발비 비중을 지속적으로 늘려가는 국내 대기업들을 <span class=\"text-amber-300 font-bold\">중장기 자산 가치주</span> 관점에서 연금 포트폴리오에 편입하는 전략이 유효합니다."
    }
  },
  "jIRollX6Y6E": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["미중전략경쟁", "제네시스미션", "젠슨황라인", "염수리튬추출", "스맥오버지층"],
    "analysis": {
      "summary": "미중 갈등이 단순한 냉전을 넘어 사실상의 양강이 대치하는 <span class=\"text-violet-300 font-medium\">준양극 체제(Semi-bipolar)</span>로 진입함에 따라, 미국은 국가 안보 차원의 AI 총력전인 '제네시스 미션(Genesis Mission)'을 선포했습니다. 과거의 일방적 규제를 넘어 압도적인 인프라 격차를 조성하려는 미국의 AI 군비 경쟁(CAPEX 투자가 국방비 상회 전망)은 반도체 동맹국들을 묶는 '젠슨 황 라인'을 형성하고 있습니다. 또한 핵심 광물의 중국 의존도를 해소하기 위해 텍사스 스맥오버 지층 등의 <span class=\"text-cyan-300 font-semibold\">지하 염수 리튬 상업 채취 법제화</span>를 추진하며 장기 공급망 자립화에 시동을 걸었습니다.",
      "key_claims": [
        "중국의 실질 국력(GDP 및 실질 체력 복합 지표)은 과거 전성기 소련을 상회하므로, 현재의 미중 패권 경쟁은 더욱 치열하고 장기적인 <span class=\"text-violet-300 font-medium\">기술 블록화 양상</span>을 보입니다.",
        "미국의 신규 국가 AI 행정명령인 '제네시스 미션'과 'AI 액션 플랜'은 AI 컴퓨터와 HBM 메모리 공급망을 전략적 안보 자산으로 명문화하여 <span class=\"text-cyan-300 font-semibold\">수조 달러 규모의 연방 재정 및 민간 유동성 유입</span>을 강제합니다.",
        "중국의 핵심 광물 무기화에 맞서 미 육군 군수지 내 '스맥오버 지층' 등에서 지하 염수 리튬을 시추·추출하는 대규모 프로젝트가 셰일 오일 혁명에 준하는 <span class=\"text-amber-300 font-bold\">미국 내 광물 독립의 트리거</span>가 될 수 있습니다."
      ],
      "data_points": [
        "냉전기 미-소 GDP 격차 수준: 소련은 전성기에도 미국 GDP의 40% ~ 50% 수준에 불과",
        "미국 빅테크의 연간 AI 인프라 지출(CAPEX) 전망치 합계: 미국의 연간 국방 예산(약 1조 달러)을 상회할 것으로 전망",
        "리튬 수요 증가 속도: 연평균 30% 이상 폭증하며 2030년 공급 부족 국면 도달 예상"
      ],
      "signal": "bullish",
      "signal_reason": "미국 정부가 AI 기술 패권 사수를 위해 반도체, HBM, 전력 기기뿐 아니라 자국 내 핵심 광물(리튬 추출) 공급망 구축에 무제한적인 재정적·법적 지원을 투입하기 시작했기 때문입니다.",
      "key_companies": ["Tesla(TSLA)", "MP Materials(MP)", "Albemarle(ALB)"],
      "insight": "AI 인프라 경쟁은 민간의 비즈니스 영역을 넘어 국가 생존이 걸린 <span class=\"text-violet-300 font-medium\">현대판 맨해튼 프로젝트</span>로 격상되었습니다. 셰일 혁명이 원유 시장의 판도를 바꿨듯, 텍사스 염수 리튬 상업화 법안은 원자재 공급망 구도를 근본적으로 뒤흔들 수 있는 중장기 메가 트렌드입니다.",
      "action_point": "미국 내 리튬 시추 및 신공법(Direct Lithium Extraction, DLE)을 적용하여 사업권을 획득하는 미국 독립계 에너지/광업 선도 기업들을 선제 발굴하고, <span class=\"text-cyan-300 font-semibold\">전력 인프라 및 핵심 메모리 반도체 동맹주</span>에 대한 투자 비중을 늘려야 합니다."
    }
  },
  "jVTQyKVHg4Q": {
    "primary_topic": "space",
    "secondary_topics": ["tech"],
    "tags": ["재사용로켓", "창정로켓", "그물회수방식", "자세제어기술", "중국우주개발"],
    "analysis": {
      "summary": "중국이 해상 바지선에 설치된 강철 그물과 로켓의 금속 걸이를 활용하여 재사용 로켓(창정 시리즈)의 1단 부스터를 회수하는 독특한 우주 기술 테스트에 성공했습니다. 이 방식은 스페이스X가 사용하는 무거운 착륙 다리를 로켓 본체에 장착하지 않아도 되므로 <span class=\"text-cyan-300 font-semibold\">탑재하중(Payload) 효율성</span>을 극대화할 수 있는 장점이 있습니다. 다만 한 치의 오차도 없이 지정된 속도로 그물망에 걸려야 하므로, 초고난도 자세 제어 및 <span class=\"text-cyan-300 font-semibold\">실시간 정밀 유도 시스템</span>의 신뢰성 검증이 핵심 조건입니다.",
      "key_claims": [
        "착륙 다리를 포기하는 대신 발사체의 무게를 줄여 위성 탑재 용량을 확보하는 <span class=\"text-cyan-300 font-semibold\">구조적 경량화 설계</span>를 실현했습니다.",
        "1단 부스터 하강 과정에서 대기권 재진입 열 하중을 견디며 여러 차례 엔진을 껐다 켜는 '제점화 및 자세 제어 기술'을 완전히 입증했습니다.",
        "중국의 이번 강철 그물 회수 성공은 스페이스X의 독점에 대응하는 중국 우주 기구의 재사용 발사체 기술이 임계점을 넘었음을 증명합니다."
      ],
      "data_points": [
        "로켓 회수 테스트 거리: 발사장에서 해상 바지선 회수 지점까지 약 430km 이격",
        "재사용 필수 검증 3대 요소: 엔진 다중 제점화 기술, 고속 자세 제어 능력, 정밀 목표물 포획 시스템"
      ],
      "signal": "neutral",
      "signal_reason": "중국의 우주 발사체 기술적 진보를 객관적으로 다룬 정보성 콘텐츠로, 국내외 민간 우주 기업의 단기 밸류에이션에 즉각적인 상하방 영향을 주진 않기 때문입니다.",
      "key_companies": ["SpaceX"],
      "insight": "우주 인터넷망 구축을 위한 위성 발사 수요가 폭발하는 가운데, 발사체 회수를 통한 단가 절감 경쟁이 미국과 중국의 <span class=\"text-cyan-300 font-semibold\">우주 패권 레이스</span>로 번지고 있습니다. 착륙 다리 방식과 그물 회수 방식의 효율성 비교는 향후 민간 우주 기업들의 표준 아키텍처 수립에 나침반이 될 것입니다.",
      "action_point": "재사용 발사체의 필수인 엔진 제점화 밸브 및 <span class=\"text-cyan-300 font-semibold\">우주용 자세 제어 센서 부품</span>을 제작하는 글로벌 공급망 및 방산·우주 밸류체인 내 강소기업들을 선별 관찰할 필요가 있습니다."
    }
  },
  "q9s_TdkV03U": {
    "primary_topic": "etc",
    "secondary_topics": [],
    "tags": ["베르나르베르베르", "소설작법", "창작근육", "영혼의왈츠", "이색인터뷰"],
    "analysis": {
      "summary": "프랑스의 거장 소설가 베르나르 베르베르가 출연하여 매일 정해진 시간 동안 규칙적인 집필을 이어가는 '상상력 근육 훈련'의 중요성과 사람과의 만남을 통해 얻는 영감의 원천에 대해 심도 있게 논합니다. 소설 작법의 본질은 유려한 묘사(피부)보다 독자를 놀라게 할 탄탄한 스토리 라인(뼈대)을 구축하고 주인공에게 가혹한 시련을 준 뒤 이를 극복하게 만드는 데 있습니다. 작가는 독자 스스로 자신의 내면을 들여다보고 삶의 어려움을 헤쳐나갈 <span class=\"text-amber-300 font-bold\">희망의 기운</span>을 전하는 이야기꾼이어야 합니다.",
      "key_claims": [
        "소설 쓰기나 창작 활동은 타고난 재능에만 의존하는 것이 아니라, 조깅처럼 매일 10분이라도 반복 훈련하여 <span class=\"text-amber-300 font-bold\">창의성 근력</span>을 단련해야 성공할 수 있습니다.",
        "독자들에게 깊은 몰입감을 주려면 예상 가능한 구조를 탈피하여 주인공이 겪는 갈등의 강도를 <span class=\"text-cyan-300 font-semibold\">예측 불가능한 방식으로 극대화</span>해야 합니다.",
        "훌륭한 창작은 골방에서의 독서보다 다양한 문화권을 여행하고 낯선 이들과의 깊은 대화를 통해 타인의 수수께끼(비밀)를 발견하는 과정에서 탄생합니다."
      ],
      "data_points": [
        "베르나르 베르베르 누적 집필 도서 권수: 총 35권 저술",
        "집필 비결: 매일 아침 정해진 시간 동안 매일 글을 쓰는 꾸준한 습관(Régularité)의 유지"
      ],
      "signal": "na",
      "signal_reason": "베스트셀러 소설가의 창작관, 예술 철학 및 인간의 심리적 영감 획득 방식을 주제로 한 문화·인문 다큐멘터리 성격의 대담이기 때문입니다.",
      "key_companies": [],
      "insight": "모든 창의적 콘텐츠 산업의 핵심은 대중의 깊은 공감대를 자아내는 인간의 심리 메커니즘을 꿰뚫는 데 있습니다. 기준점을 심플하게 조율해 대중과 호흡하되, 인간의 영혼과 전생이라는 깊이 있는 소재를 <span class=\"text-amber-300 font-bold\">독창적인 서사</span>로 가공해 내는 균형 감각이 명작의 요건입니다.",
      "action_point": "엔터테인먼트, 출판, 콘텐츠 창작 및 스토리텔링 플랫폼 관련 투자 검토 시, 기계적인 알고리즘 매칭 외에 인간의 <span class=\"text-cyan-300 font-semibold\">근본적 지적 호기심과 영감</span>을 자극하는 오리지널 IP 보유 기업의 무형 자산 가치에 초점을 맞춰야 합니다."
    }
  },
  "qhEkWjExlPg": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["레거시반도체", "캐시카우", "HBM집중우려", "배터리선례", "메모리리스크"],
    "analysis": {
      "summary": "글로벌 배터리 시장에서 한국이 중국에 점유율을 잠식당했던 아픈 선례를 반도체 산업에서도 엄중한 교훈으로 되새겨야 합니다. HBM 등 고부가가치 차세대 반도체의 화려함에만 모든 자본과 엔지니어 역량을 쏟아붓다가는, 가장 든든한 캐시카우 역할을 해온 <span class=\"text-rose-400 font-medium\">범용 메모리(레거시 D램 및 낸드) 시장</span>의 주도권을 통째로 중국 등 추격국에 내줄 수 있습니다. 첨단 초격차 연구 개발과 함께 튼튼한 현금 흐름의 뿌리가 되는 성숙 반도체 영역의 원가 경쟁력과 핵심 점유율 유지가 필수적입니다.",
      "key_claims": [
        "범용 레거시 메모리는 기술 장벽이 낮아 보이나 전 세계 시스템 빌더와 모바일 등에 대량 공급되는 핵심 <span class=\"text-cyan-300 font-semibold\">안정적 현금 창출원(Cash Cow)</span>입니다.",
        "배터리 산업에서 NCM 삼원계 하이엔드 기술에 집착하다 LFP 범용 시장을 뺏긴 것처럼, HBM 올인 전략은 범용 디램 부문에서 <span class=\"text-rose-400 font-medium\">중국 제조사의 점유율 잠식 리스크</span>를 증폭시킵니다.",
        "중장기 생존을 위해서는 프리미엄 고부가 반도체와 대량 양산 범용 메모리의 <span class=\"text-cyan-300 font-semibold\">포트폴리오 양손잡이 전략</span>이 반드시 실행되어야 합니다."
      ],
      "data_points": [
        "메모리 반도체 현금 흐름 근간: 연간 대량 양산형 레거시 LPDDR, 범용 DDR4/DDR5 및 eMMC/UFS 낸드 플래시 비중"
      ],
      "signal": "neutral",
      "signal_reason": "특정 기업의 즉각적인 실적 훼손보다는 반도체 업계의 중장기 자원 배분 전략과 범용 부문 경쟁 강도 상승에 대한 구조적 우려를 환기시키는 콘텐츠이기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "글로벌 공급망이 기술 안보 중심으로 분절되더라도, 볼륨 마켓인 중저가 IT 디바이스향 레거시 반도체의 시장 규모는 압도적입니다. 하이엔드에만 치중된 투자는 단기 불황 국면에서 <span class=\"text-rose-400 font-medium\">급격한 실적 변동성 노출</span>이라는 부작용을 낳을 수 있습니다.",
      "action_point": "반도체 포트폴리오 다변화 수준을 검토하여 최첨단 HBM 외에 범용 D램 및 낸드 부문에서도 압도적인 생산 단가 우위와 <span class=\"text-cyan-300 font-semibold\">공정 효율성</span>을 지키고 있는 메모리 리더 기업을 선별하여 투자 비중을 조절해야 합니다."
    }
  },
  "qqfDPQNboCw": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["SK하이닉스ADR", "KV캐시", "아시브레너포트폴리오", "맞춤형HBM4", "엔비디아루빈"],
    "analysis": {
      "summary": "SK하이닉스의 미국 나스닥 ADR 상장(티커: SKY) 첫날 13% 가까운 급등은 마이크론 대비 밸류에이션 저평가(코리아 디스카운트) 해소와 글로벌 인프라 자금 유입의 서막을 열었습니다. 5년 내 캐파 2배 증설 발표에도 공급 리드타임 제약으로 <span class=\"text-cyan-300 font-semibold\">메모리 쇼티지 장기화</span>가 유력하며, 온디바이스 AI 및 GPU 성능 향상에 따른 'KV 캐시(Key-Value Cache)' 저장용 메모리 수요가 전방위로 폭증하고 있습니다. 2027년 레거시 디램 피크아웃 우려 속에서도, 커스텀 HBM4 등 독보적인 <span class=\"text-cyan-300 font-semibold\">고마진 맞춤형 HBM 생태계</span>가 락인(Lock-in) 효과를 발휘하며 메모리 업계의 중장기 리레이팅을 이끌 전망입니다.",
      "key_claims": [
        "하이닉스 나스닥 ADR은 본주 대비 약 15%의 역사적 프리미엄을 적용받아 252만 원선에 안착하며 코리아 디스카운트를 해소하는 <span class=\"text-cyan-300 font-semibold\">영구적 밸류에이션 상승 발판</span>을 마련했습니다.",
        "대화의 이전 맥락 정보를 임시 저장하는 'KV 캐시' 연산이 고도화됨에 따라 차세대 칩(엔비디아 루빈 등) 내부의 LPDDR5X 및 HBM4 메모리 용량 요구치가 전 세대 대비 최대 3배 급증합니다.",
        "2027년부터는 단순 가격(P) 상승에 의존하던 범용 메모리 사이클에서 벗어나, 빅테크 커스텀 스펙에 특화된 HBM 위주의 가격(P)과 물량(Q)의 동반 우상향인 <span class=\"text-amber-300 font-bold\">이익의 고도화 구간</span>으로 진입합니다."
      ],
      "data_points": [
        "SK하이닉스 미국 ADR(SKY) 공모가 대비 마감 주가 상승폭: 13% 수준 상승한 168달러 기록 (원화 약 252만 원선으로 본주 대비 15% 프리미엄 형성)",
        "차세대 엔비디아 루빈(Rubin) 울트라 CPU/GPU 탑재 스펙: 베라 CPU 옆 LPDDR5X 용량 약 1.5TB(3배 폭증), GPU 옆 HBM4 탑재 용량 약 288GB(1.5배 증가)",
        "메모리 부문 이익 기여도 비중: 현재 영업이익 기준 범용 디램 70%, HBM 30% 수준 기여 중",
        "아시브레너 AI 인프라 헤지펀드 운용자금 규모: 약 30조 원 규모 돌파 (코어위브, TSMC, 마이크론, 전력 인프라 등 병목 부문에 집중 투자)"
      ],
      "signal": "bullish",
      "signal_reason": "미국 ADR을 통한 풍부한 글로벌 기관 자금 유입 경로가 뚫렸고, KV 캐시 최적화 요구 및 차세대 GPU용 HBM4의 독보적인 수량 증가와 맞춤형 고마진 생태계 구조가 입증되었기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "로보티즈(103030)", "TSMC(TSM)"],
      "insight": "메모리가 과거 원자재(Commodity) 성격의 범용 사이클에서 벗어나 GPU 기업들과 동맹을 맺는 <span class=\"text-cyan-300 font-semibold\">커스텀 맞춤형 안보 전략 자산</span>으로 전환되고 있습니다. 오픈 OpenAI 핵심 출신 아시브레너의 30조 원 펀드가 네오 클라우드와 메모리, 전력에 집중 포지셔닝한 것 역시 인프라 병목 구간에 대한 확신을 보여줍니다.",
      "action_point": "단기적인 매크로 수급 노이즈로 메모리 반도체 주가가 흔들리는 국면마다, HBM4 패키징 해자를 선점한 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span> 본주 비중을 과감히 늘리고 로보티즈 등 오픈소스 로봇 손 액추에이터 수혜주도 분할 포착해야 합니다."
    }
  }
}

for vid, val in batch_data.items():
    save_and_delete(vid, val["primary_topic"], val["secondary_topics"], val["tags"], val["analysis"])
print("Batch 4 processing completed.")
