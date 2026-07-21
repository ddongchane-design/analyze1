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
  "Ctsa5j5TlAA": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["SK하이닉스", "메모리공급부족", "최태원회장", "HBM수요", "용인반도체클러스터"],
    "analysis": {
      "summary": "SK하이닉스 최태원 회장은 AI 반도체 수요가 기하급수적으로 폭발하고 있으며 <span class=\"text-cyan-300 font-semibold\">공급 부족 현상</span>이 지속될 것이라고 밝혔습니다. 곽노정 사장은 2027년이 역사상 최악의 공급 부족 해가 될 것으로 전망했으며, 삼성전자는 용인 클러스터 첫 공장 가동을 2029년으로 앞당기기로 했습니다. 고객사들은 HBM 등 메모리를 5~6배 이상 원하고 있어 과거와 같은 공급 과잉 사이클은 쉽게 오지 않을 전망입니다.",
      "key_claims": [
        "반도체 공급 부족은 일시적인 현상이 아니며, 고객사들의 주문량에 근거할 때 <span class=\"text-amber-300 font-bold\">2030년까지 지속될 가능성</span>이 있습니다.",
        "삼성전자의 용인 1공장 가동이 2029년으로 앞당겨지는 등 국내 기업들이 <span class=\"text-cyan-300 font-semibold\">설비투자(CapEx) 속도전</span>에 진입했습니다.",
        "SK하이닉스는 단순 제조를 넘어 필요한 만큼 빌려 쓰는 CXL 기반 <span class=\"text-cyan-300 font-semibold\">서비스형 메모리(MaaS)</span>로 비즈니스 모델을 다변화하고 있습니다."
      ],
      "data_points": [
        "SK하이닉스 ADR 종가: 공모가 대비 13% 상승한 168달러 마감",
        "삼성전자 용인 반도체 클러스터 1공장 첫 가동 시점: 2029년으로 1~2년 단축 설정",
        "HBM 및 기존 디램 공급 부족 전망 기한: 2028년 2분기(UBS 단기 전망) ~ 2030년(업계 실무진 전망)",
        "고객사 요구 공급 규모: 현재 생산 능력 계획 대비 대여섯 배 수준의 공급을 희망"
      ],
      "signal": "bullish",
      "signal_reason": "핵심 고객사의 대규모 장기 계약 체결 및 예상치를 상회하는 폭발적인 수요 데이터가 증명되어 반도체 업황의 장기 호황 가능성이 매우 높기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "반도체 공급 과잉 사이클의 정석은 설비투자 증가에 따른 하락 전환이었으나, AI 학습량 폭증으로 인한 <span class=\"text-cyan-300 font-semibold\">메모리 부족 현상</span>이 이를 깨고 있습니다. 국내 대기업들이 설비 속도를 당기고 포트폴리오를 다변화하는 것은 시장 장악력을 극대화하기 위한 움직임입니다.",
      "action_point": "과거의 공급 과잉 프레임에 갇혀 기술주 비중을 줄이기보다는, 장기 공급 계약 수혜가 확인되는 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span> 및 용인 가동 일정을 단축한 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>의 비중 확대를 최우선으로 검토해야 합니다."
    }
  },
  "DfgXcw2a5Pg": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["메모리파운드리", "커스텀HBM", "초격차전략", "삼성전자", "SK하이닉스"],
    "analysis": {
      "summary": "중국 메모리 반도체 업계의 거센 추격을 뿌리치기 위해서는 단순 양적 확장(수평적 확장)을 넘어 <span class=\"text-amber-300 font-bold\">질적 차별화(수직적 확장)</span>가 필수적입니다. AI 빅테크 하이퍼스케일러들은 독자적인 AI 칩에 맞춰 메모리를 고도로 커스터마이즈해 주기를 강력하게 요구하고 있습니다. 메모리 제조 공정이 개별 맞춤형 설계로 전환되는 <span class=\"text-cyan-300 font-semibold\">메모리 파운드리</span> 패러다임이 한국 기업들의 핵심 돌파구입니다.",
      "key_claims": [
        "중국의 저가 물량 공세를 이기기 위해서는 기술 장벽이 높은 <span class=\"text-cyan-300 font-semibold\">커스텀 HBM</span> 등의 질적 초격차로 전환해야 합니다.",
        "빅테크들의 자체 실리콘(ASIC) 도입이 늘어나면서 메모리와 시스템 반도체의 경계가 무너지는 <span class=\"text-amber-300 font-bold\">융합형 메모리 시대</span>가 도래하고 있습니다.",
        "단순 조립 형태를 탈피해 패키징과 공정 자체를 맞춤 제공하는 메모리 파운드리가 핵심 경쟁 우위 요소입니다."
      ],
      "data_points": [
        "중국의 추격 범위: 레거시 디램 및 낸드 분야에서 대규모 물량 공세 가속화"
      ],
      "signal": "bullish",
      "signal_reason": "커스텀 메모리 수요 폭증은 범용 가격 등락 리스크를 방어하고, 한국 기업들이 독점적인 기술 멀티플을 추가로 부여받는 계기가 되기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "AI 칩 시장의 미세화 한계를 극복하기 위해 메모리가 직접 시스템 성능을 보조하는 구조로 가고 있습니다. <span class=\"text-cyan-300 font-semibold\">메모리 파운드리</span> 기술을 선제 확보한 기업이 다가올 수십 년간의 반도체 공급망 헤게모니를 장악할 것입니다.",
      "action_point": "하이퍼스케일러와 공동 개발을 가속화하고 있는 커스텀 반도체 관련 기술을 보유한 디자인하우스 및 <span class=\"text-cyan-300 font-semibold\">어드밴스드 패키징(Advanced Packaging)</span> 수혜주에 대한 투자를 집중해야 합니다."
    }
  },
  "Dmgc7OfFjNM": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["삼성파운드리", "앤스로픽", "커스텀HBM", "미중패권경쟁", "구글TPU"],
    "analysis": {
      "summary": "글로벌 빅테크의 CapEx 투자가 작년 대비 약 두 배 급증하며 디램 가격이 600% 이상 폭등하는 사상 초유의 슈퍼 사이클이 전개 중입니다. 앤스로픽의 클로드 B2B 채택 폭발과 구글의 TPU 독자 노선 가속화가 <span class=\"text-cyan-300 font-semibold\">커스텀 HBM</span> 수요를 견인하고 있습니다. 미국은 10나노 이하 파운드리의 TSMC 쏠림 완화를 위해 텍사스에 거점을 둔 <span class=\"text-cyan-300 font-semibold\">삼성전자 파운드리</span>를 미중 안보 분산의 핵심 파트너로 활용할 수밖에 없습니다.",
      "key_claims": [
        "앤스로픽(Anthropic)은 강력한 보안성을 지닌 AI 헌법 모델 클로드로 B2B 시장에서 흑자 전환에 성공하며 <span class=\"text-amber-300 font-bold\">AI 실질 수익화</span>를 주도하고 있습니다.",
        "미국 정부는 대만 TSMC에 대한 안보 의존도(10나노 이하 90% 이상 점유)를 낮추기 위해 <span class=\"text-cyan-300 font-semibold\">삼성 파운드리 및 인텔</span>을 강력한 대안으로 육성 중입니다.",
        "애플의 독점 생산 의뢰로 TSMC와 삼성 파운드리의 격차가 크게 벌어졌으나, 미국의 리스크 분산 및 신규 빅테크 수주로 삼성 파운드리의 턴어라운드 기회가 오고 있습니다."
      ],
      "data_points": [
        "디램 가격 1년 전 대비 상승률: 약 600% 이상 폭등",
        "하이퍼스케일러 전체 CapEx 투자 규모: 과거 약 4,000억 달러 수준에서 올해 7,000억 ~ 8,000억 달러로 급증",
        "글로벌 10나노 이하 파운드리 TSMC 시장 점유율: 약 90% 이상 점유 (국가 안보 리스크 지목)",
        "과거 삼성전자 파운드리 점유율 추이: 약 18% ~ 19% 고점에서 7% ~ 8% 수준으로 하락"
      ],
      "signal": "bullish",
      "signal_reason": "빅테크 실적 및 AI 비즈니스 모델 수익화가 확인되고 있으며, 미국 안보 전략상 텍사스 삼성 파운드리 가동률 상승이 확실시되기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "앤스로픽", "구글(GOOGL)", "TSMC(TSM)"],
      "insight": "반도체는 이제 순수 경제 논리가 아닌 <span class=\"text-violet-300 font-medium\">지경학적 패권 전략</span>에 맞춰 강제로 재편되고 있습니다. TSMC 단일 공급망 리스크에 노출된 미국 빅테크들은 텍사스에 최신 패키징 라인을 갖춘 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>로 눈을 돌릴 수밖에 없는 구조적 수혜를 누리게 됩니다.",
      "action_point": "삼성전자의 메모리 호실적 외에도 장기적으로 <span class=\"text-cyan-300 font-semibold\">파운드리 사업부 적자 축소 및 수주 확대</span> 모멘텀에 베팅하여 대형 기술주 포트폴리오를 다변화해야 합니다."
    }
  },
  "ETtzfE6XJhE": {
    "primary_topic": "space",
    "secondary_topics": ["tech"],
    "tags": ["창정10비", "재사용로켓", "메탄엔진", "스페이스X", "차세대발사체"],
    "analysis": {
      "summary": "중국이 '창정 10비' 로켓의 1단 부스터 해상 그물 회수에 성공하며 미국의 로켓 재사용 독점 체제를 10년 만에 깨뜨렸습니다. 중국은 수직 착륙 대신 바지선 그물망에 고리를 거는 독창적인 기술로 로켓 무게를 획기적으로 줄였습니다. 이에 맞서 한국은 차세대 발사체 사업을 등유 기반 1회용에서 <span class=\"text-cyan-300 font-semibold\">액체 메탄 엔진 재사용 방식</span>으로 전환하며 우주 기술 경쟁력을 추격하고 있습니다.",
      "key_claims": [
        "중국의 이번 그물 회수 성공은 미국의 <span class=\"text-rose-400 font-medium\">우주 재사용 기술 독점권</span>을 무력화한 지정학적 이정표입니다.",
        "재사용 발사체의 글로벌 최신 트렌드는 그을음이 적은 메탄 추진제, 3D 프린팅 엔진 제작, 수직 착륙 기술로 통일되고 있습니다.",
        "한국은 2032년 달 착륙선 발사를 목표로 차세대 발사체 사업을 <span class=\"text-cyan-300 font-semibold\">메탄 기반 재사용 로켓</span>으로 전면 수정하여 개발 중입니다."
      ],
      "data_points": [
        "창정 10비 로켓 추력: 이륙 추력 890톤으로 팰컨 9(770~780톤) 대비 강력",
        "재사용 로켓용 탑재량: 저궤도 기준 약 16톤 탑재 가능",
        "한국 차세대 발사체 개발 예산 규모: 당초 약 2.3조 원에서 재사용 전환 시 약 5.6조 원 이상 소요 전망",
        "스페이스X 팰컨 9 단일 부스터 최다 재사용 횟수: 35회 돌파 및 40회 목표 진행 중"
      ],
      "signal": "neutral",
      "signal_reason": "우주 지경학적 기술 성과로 방산 및 항공우주 산업의 장기 모멘텀은 긍정적이나, 단기적인 금융 시장 수익화에는 다소 시간이 필요하기 때문입니다.",
      "key_companies": ["한화에어로스페이스(012450)", "HD현대중공업(329180)", "현대로템(064350)", "SpaceX"],
      "insight": "로켓 재사용은 우주 산업의 상업성을 좌우하는 가장 강력한 무기이며, 중국이 그물망 포획이라는 대안적 성공 경로를 제시했습니다. 한국 역시 메탄 기반 재사용으로 사업 계획을 긴급 수정하여 <span class=\"text-violet-300 font-medium\">글로벌 우주 패권 경쟁</span>에 정면으로 동참했습니다.",
      "action_point": "스페이스X 및 블루 오리진 공급망에 이미 진입한 국내 특수 소재/엔진 부품 기업 및 국가 차원의 차세대 발사체 사업 주도권을 쥔 <span class=\"text-cyan-300 font-semibold\">한화에어로스페이스</span>의 장기 성장 잠재력에 계속 관심을 유지해야 합니다."
    }
  },
  "HFAspbOn2T8": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["최태원회장", "SK하이닉스", "ADR상장", "반도체사이클", "액면분할"],
    "analysis": {
      "summary": "최태원 SK그룹 회장은 미국 ADR 성공적 상장에 대해 반도체 강세 사이드카 속에서도 149달러 이상의 가치를 굳건히 지키겠다는 의지를 밝혔습니다. 미국 중심의 공급망 재편 및 리쇼어링 요구에는 전력, 용수 등 조건이 맞을 때 투자하겠다는 <span class=\"text-violet-300 font-medium\">철저한 고객 수요 기반 전략</span>을 고수하고 있습니다. AI 반도체는 이제 시작 단계이며 저장할 메모리 요구량은 무한히 늘어나 기존의 패턴과는 다른 구조적 장기 상승 사이드카에 있음을 재확인했습니다.",
      "key_claims": [
        "인공지능(AI) 시장은 여전히 유아기(4~5세) 수준으로, 본격적인 성년기로 성장할 때까지 <span class=\"text-amber-300 font-bold\">기하급수적인 메모리 수요 확장</span>이 필연적입니다.",
        "중국 메모리 업체들의 흑자 전환과 대규모 IPO는 국내 반도체 산업에 대한 <span class=\"text-rose-400 font-medium\">기술 캐치업 위협</span>을 높이고 있어 고유의 속도전이 필요합니다.",
        "액면 분할이나 키옥시아 지분 활용과 같은 주주가치 극대화 정책은 시장 흐름과 재무 상황에 맞춰 유연하게 검토 중입니다."
      ],
      "data_points": [
        "최태원 회장이 제시한 ADR 안정 마지노선 주가: 149달러선 이상 유지 목표",
        "메모리 반도체 공급 능력 한계 요인: 신규 공장 건설 시 대규모 전력, 용수, 장비 리드타임이 큰 병목으로 작용"
      ],
      "signal": "bullish",
      "signal_reason": "AI 로드맵의 초입성 및 공급자 지배력이 강한 구조적 병목이 굳건하며, 주가 방어 및 글로벌 밸류에이션 리레이팅 의지가 확고하기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)"],
      "insight": "최태원 회장이 언급한 'AI 유아기론'은 현재의 반도체 과열 논란을 정면으로 반박하며 장기 메모리 소요를 설명합니다. 지정학적 리스크 속에서도 공장 이전 압박에 섣불리 굴하지 않고 <span class=\"text-violet-300 font-medium\">공급 안전성(Supply Security)</span>을 전략 카드로 사용하는 영리한 경영을 보여줍니다.",
      "action_point": "SK하이닉스의 <span class=\"text-cyan-300 font-semibold\">글로벌 ADR 상장 효과</span>에 힘입어 해외 자금 유입 수혜를 받을 수 있는 반도체 장비 및 부품 공급사들의 밸류에이션 재평가 국면에 주목해야 합니다."
    }
  },
  "JF6oUUk1JZE": {
    "primary_topic": "robot",
    "secondary_topics": ["tech"],
    "tags": ["피지컬AI", "휴머노이드", "액추에이터", "골드만삭스", "로보티즈"],
    "analysis": {
      "summary": "챗GPT가 나오기 전 GPT-3가 존재했던 것처럼, 휴머노이드 역시 3~4년 내에 대중화의 변곡점인 <span class=\"text-amber-300 font-bold\">챗GPT 모먼트</span>를 맞이할 전망입니다. 골드만삭스는 한국이 자동차 산업의 기계/전장 제조 축적 노하우를 바탕으로 글로벌 휴머노이드 부품망의 30%를 독식할 것으로 전망했습니다. 인건비보다 저렴한 로봇 가동 비용과 인력 부족 현상이 피컬 AI(Physical AI) 혁명을 강제하고 있습니다.",
      "key_claims": [
        "휴머노이드 하드웨어 가격이 1만 달러(중고차 가격) 수준으로 하락할 때 <span class=\"text-amber-300 font-bold\">수요의 기하급수적 대중화</span>가 촉발됩니다.",
        "로봇 산업의 진정한 경쟁 우위는 하드웨어 자체보다 수천 대의 로봇 현장 운용을 통해 축적하는 <span class=\"text-cyan-300 font-semibold\">플릿 데이터(Fleet Data)</span> 선순환 체계에 있습니다.",
        "현재 로봇 공급망 및 액추에이터 관련 전장 기업들은 자동차 경기 둔화 우려로 극도로 저평가되어 있는 <span class=\"text-rose-400 font-medium\">매력적인 매수 구간</span>입니다."
      ],
      "data_points": [
        "골드만삭스 한국 휴머노이드 글로벌 공급망 점유율 전망치: 2035년 기준 약 30% 달성 예상",
        "2050년 글로벌 휴머노이드 및 AI 로봇 누적 운용 대수 전망치: 약 10억 대(모건스탠리) ~ 40억 대(시티리서치) 도달",
        "보급형 휴머노이드 목표 도달 가격: 10,000달러(약 1,300만 원) 이하",
        "로봇 시간당 기대 운영 인건비: 약 2달러(약 2,600원) 수준으로 경제성 확보"
      ],
      "signal": "bullish",
      "signal_reason": "하드웨어 표준화 초입 단계에서 핵심 부품 기업들의 밸류에이션 매력도가 뛰어나며, 빅테크의 피지컬 AI 투자가 본격화되고 있기 때문입니다.",
      "key_companies": ["로보티즈(103030)", "현대차(005380)", "현대모비스(012330)", "Tesla(TSLA)"],
      "insight": "디지털 세계에 갇혀 있던 생성형 AI가 현실 세계를 조작하는 <span class=\"text-cyan-300 font-semibold\">피지컬 AI(임바디드 AI)</span>로 넘어오고 있습니다. 한국은 완성차 부품 생태계가 정교하게 조율되어 있어, 로봇 액추에이터와 감속기 분야에서 세계적인 공급망 승자가 될 것입니다.",
      "action_point": "자동차 전장 및 감속기 부문 저평가 매력도가 높은 <span class=\"text-cyan-300 font-semibold\">현대차/현대모비스</span>와 로봇 플랫폼 및 액추에이터 전문 기업인 <span class=\"text-cyan-300 font-semibold\">로보티즈</span> 등 로봇 공급망 관련 핵심 기업을 중장기 관점에서 선제 매수해야 합니다."
    }
  },
  "Lbt7aPJCpGk": {
    "primary_topic": "etc",
    "secondary_topics": ["tech"],
    "tags": ["삼성전자", "인재유출", "조직문화", "노사갈등", "메타"],
    "analysis": {
      "summary": "최근 삼성전자 노사 갈등 심화와 신뢰 관계 훼손으로 인해 국내 반도체 핵심 천재 인력들이 <span class=\"text-rose-400 font-medium\">메타 등 미국 빅테크</span>로 이탈하는 현상이 가속화되고 있습니다. AI 시대에는 다수의 범재보다 극소수의 천재 한 명이 지니는 기술적 파급력이 압도적으로 거세지고 있습니다. 이직 시 급여 상승은 물론 글로벌 최전선 커리어 확보 측면에서 삼성전자가 인재 락인을 위해 풀어야 할 조직 문화적 숙제가 큽니다.",
      "key_claims": [
        "삼성전자의 경쟁력 약화 원인은 단순히 기술의 부재가 아닌, <span class=\"text-rose-400 font-medium\">핵심 천재 인재들의 락인 실패</span>와 인사/보상 체계의 경직성에 있습니다.",
        "미국 빅테크로의 이직은 개발자 입장에서 급여 상승 및 압도적인 <span class=\"text-cyan-300 font-semibold\">AI 개발 인프라 경험</span>을 제공합니다.",
        "조직의 노사 갈등과 내부 신뢰 붕괴는 장기 연구 과제 연속성에 악영향을 주어 기술 초격차 유지를 저해합니다."
      ],
      "data_points": [
        "이직 대상 빅테크: 메타(Meta), 구글(Google) 등 실리콘밸리 선두 기업들 선호"
      ],
      "signal": "na",
      "signal_reason": "대기업의 노사 갈등 및 인재 유출이라는 내부 기업 문화를 분석하는 인사이드 성격의 영상으로, 직접적인 투자 기회를 담고 있지 않기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "메타(META)"],
      "insight": "AI와 반도체 패권 경쟁의 본질은 돈이나 공장 부지 이전에 <span class=\"text-cyan-300 font-semibold\">최정상급 엔지니어 확보</span>에 달려 있습니다. 삼성이 관료주의와 보상 갈등을 빠르게 해결하지 못한다면, 보유한 지식 자산이 실리콘밸리로 급속히 누출되는 구조적 난관에 직면할 것입니다.",
      "action_point": "삼성전자의 경쟁력 지표를 추적할 때 단순히 분기 실적 수치뿐 아니라, <span class=\"text-rose-400 font-medium\">핵심 연구 인력의 이탈 동향</span> 및 성과 보상 체계 개선 여부를 주요 내부 리스크 요인으로 상시 점검해야 합니다."
    }
  }
}

for vid, val in batch_data.items():
    save_and_delete(vid, val["primary_topic"], val["secondary_topics"], val["tags"], val["analysis"])
print("Batch 2 processing completed.")
