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
  "UmzqXxgQ1-c": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["SK하이닉스", "수출데이터", "반도체소부장", "ADR상장", "전력기기"],
    "analysis": {
      "summary": "SK하이닉스가 미국 ADR 상장 첫날 13% 가까이 급등하며 국내 반도체 대형주 및 소부장(소재·부품·장비) 전반에 강력한 <span class=\"text-cyan-300 font-semibold\">자금 유입 모멘텀</span>을 제공하고 있습니다. 7월 1~10일 수출 잠정치 결과, 지난달 시장 우려와 달리 D램 수출 금액은 전월비 29%, 단가는 16% 급증하며 반도체 피크아웃 우려를 종식시켰습니다. 반도체 전공정 및 노광 장비(ASML 등) 쇼티지 속에 글로벌 메가 프로젝트 증설이 시작되어 장비주의 장기 우상향 흐름이 굳건합니다.",
      "key_claims": [
        "SK하이닉스의 미국 상장은 마이크론 대비 현저히 저평가된 멀티플 격차를 해소하고, 중장기 <span class=\"text-cyan-300 font-semibold\">주주환원 정책 확대</span>로 연결될 것입니다.",
        "7월 초의 반도체 주가 개파락은 일시적인 수출 단가 왜곡 데이터로 인한 과도한 우려(MOM 마이너스 착시)였음이 최신 데이터로 입증되었습니다.",
        "용인 1공장 일정을 단축하는 등 삼성/하이닉스의 메가 프로젝트 발주로 인해 내년부터 <span class=\"text-cyan-300 font-semibold\">전공정 장비 수주 대란</span>이 본격화됩니다."
      ],
      "data_points": [
        "SK하이닉스 미국 ADR 데뷔전 당일 주가 상승률: 약 13% 수준 급등",
        "7월 1일 ~ 10일 기준 디램 수출 금액 상승률: 전월 동기 대비 29% 급증",
        "동 기간 디램 수출 단가 상승률: 전월 동기 대비 16% 상승",
        "화장품 및 기타 수출주 대비 반도체 및 전력기기의 고점 대비 하락 폭: 약 30% ~ 40% 수준의 과도한 조정 기록"
      ],
      "signal": "bullish",
      "signal_reason": "실제 수출 데이터의 강력한 턴어라운드가 확인되었고, 글로벌 ADR 자금 유입 및 대규모 용인 클러스터 장비 발주가 대기 중이기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "원익IPS(240810)"],
      "insight": "7월 수출 데이터 복귀는 시장의 반도체 피크아웃 논란이 데이터 착시에서 기인한 노이즈였음을 명확히 보여줍니다. 단기 변동성은 불가피하나, 향후 20년에 걸친 <span class=\"text-cyan-300 font-semibold\">메가 증설 사이클</span> 하에서 전공정 장비의 누적 수주는 역대 최대치를 경신할 전망입니다.",
      "action_point": "최근 겪은 과도한 조정 구간을 소부장 대장주인 <span class=\"text-cyan-300 font-semibold\">원익IPS</span> 및 반도체 장비 밸류체인의 분할 매수 적기로 활용하고, 전력기기 등 낙폭과대 실적주도 병행 확보해야 합니다."
    }
  },
  "VwiN_8N6KiQ": {
    "primary_topic": "tech",
    "secondary_topics": ["stock"],
    "tags": ["방열소재", "베이퍼챔버", "어드밴스드패키징", "TIM", "스마트폰발열"],
    "analysis": {
      "summary": "스마트폰 성능이 비약적으로 향상되면서 열을 외부로 방출하는 전체 열 경로 최적화가 모바일 하드웨어의 새로운 핵심 과제로 대두되고 있습니다. <span class=\"text-cyan-300 font-semibold\">TIM(열 접합제)</span>과 대형 베이퍼 챔버(Vapor Chamber) 등 방열 솔루션이 효과적으로 연동되어야 내부 부품 파손을 예방할 수 있습니다. 향후 모바일 기기 설계는 단일 칩 효율뿐만 아니라 패키징 단계부터 외부 하우징까지 아우르는 <span class=\"text-cyan-300 font-semibold\">통합 방열 디자인</span>을 필수로 요구합니다.",
      "key_claims": [
        "AP(어플리케이션 프로세서) 상부에 디램과 열 저항이 높은 재료가 밀집되면 내부 열을 제때 끌어오지 못하는 <span class=\"text-rose-400 font-medium\">패키징 병목 현상</span>이 발생합니다.",
        "미세 미소 트랜지스터 제조 경쟁 외에 스마트폰 외부 프레임으로 열을 빠르게 전도시키는 소재 결합 기술이 실제 구동 성능을 좌우합니다.",
        "AP에서 패키지, 패키지에서 외부 베이퍼 챔버로 이어지는 전체 경로 상의 열 저항을 낮추는 신소재 결합이 핵심 차별화 요소입니다."
      ],
      "data_points": [
        "열 전달 차단 요소: AP와 디램 적층 시 발생하는 열 저항 및 상부 TIM 미세 틈새 공극"
      ],
      "signal": "neutral",
      "signal_reason": "스마트폰 방열 및 어드밴스드 패키징 소재의 구조적 중요성을 기술적으로 설명하는 콘텐츠로, 특정 기업의 단기 밸류에이션 변화를 즉각 야기하진 않기 때문입니다.",
      "key_companies": ["삼성전자(005930)"],
      "insight": "AP 칩의 온디바이스 AI 연산 부하가 증가함에 따라 모바일 기기의 쓰로틀링(성능 강제 저하)을 막을 <span class=\"text-cyan-300 font-semibold\">방열 패키징 신소재</span>와 대형 베이퍼 챔버 도입 비중이 구조적으로 증가하고 있습니다.",
      "action_point": "모바일 방열 신소재 부품 및 스마트폰 고성능 <span class=\"text-cyan-300 font-semibold\">베이퍼 챔버</span>를 제조하는 부품 밸류체인 기업들의 제품 채택 여부를 모니터링할 필요가 있습니다."
    }
  },
  "XlQ1GCi3ULw": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["코스피상단", "기업순이익", "반도체수출", "PER멀티플", "한국증시"],
    "analysis": {
      "summary": "한국 상장사들의 전체 순이익이 올해 730조 원, 내년에는 946조 원에 달할 것으로 예상되며 코스피의 장기 지수 상단이 이론적으로 <span class=\"text-amber-300 font-bold\">11,450포인트</span>까지 열릴 수 있습니다. 이는 반도체 수출 폭증과 글로벌 IT 인프라 확장에 힘입은 실질 이익 체력의 급성장에 기반합니다. 과거 200조 원 수준의 이익으로 코스피 2,000~3,000을 유지했던 점을 고려할 때, 지수 급등은 프리미엄 버블이 아닌 철저한 <span class=\"text-amber-300 font-bold\">실물 실적 기반</span>입니다.",
      "key_claims": [
        "한국 기업들의 내년 예상 순이익 946조 원에 역사적 평균 PER인 9.9배를 곱하면 코스피 예상 시가총액은 <span class=\"text-amber-300 font-bold\">9,365조 원</span> 수준에 달하게 됩니다.",
        "과거 박스피(2,000~3,000포인트) 시절 대비 전체 상장사의 연간 순이익 기초 체력이 약 4.7배 이상 팽창했습니다.",
        "단순 주가 버블이 아니라 수출 단가 상승 및 견조한 반도체 무역 흑자에 기반하므로 지수 전망의 신뢰도가 매우 높습니다."
      ],
      "data_points": [
        "올해 한국 상장사 전체 예상 순이익: 약 730조 원 수준",
        "내년 한국 상장사 전체 예상 순이익: 약 946조 원 수준",
        "과거 박스피 시절 연간 전체 순이익 수준: 약 200조 원 안팎",
        "2010년 이후 코스피 평균 PER 멀티플 배수: 9.9배 수준"
      ],
      "signal": "bullish",
      "signal_reason": "전체 상장사의 실물 이익 전망치가 과거 대비 전례 없이 높은 레벨로 수직 상승하고 있어 장기 지수의 하방이 견고하고 상방이 열려 있기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "코스피의 밸류에이션 버블 우려와 달리 현재의 지수 수준은 철저한 이익 실적에 의해 뒷받침되고 있습니다. <span class=\"text-cyan-300 font-semibold\">반도체 주도주</span>의 압도적인 무역 수지 개선 효과가 전체 증시의 체급을 완전히 다른 차원으로 레벨업하고 있습니다.",
      "action_point": "단기 거시 경제 불안이나 유동성 변동으로 지수가 일시 하락하더라도, <span class=\"text-amber-300 font-bold\">내년 순이익 946조 원의 실물 체력</span>을 믿고 장기 포트폴리오의 국내 증시 비중을 굳건히 유지해야 합니다."
    }
  },
  "XxPL1UGJ07A": {
    "primary_topic": "etc",
    "secondary_topics": ["economy"],
    "tags": ["노벨상과학자", "예체능공통점", "글로벌네트워크", "학습자본", "민태기소장"],
    "analysis": {
      "summary": "노벨상 수상자 등 최고 수준의 석학들은 일반 과학자에 비해 피아노, 미술, 체육 등 비(非)지능적 예체능 활동 수준이 매우 높으며 이는 <span class=\"text-amber-300 font-bold\">글로벌 학술 네트워크 코어 서클</span>에 안착하는 핵심 매개체 역할을 합니다. 사이언스 논문에 따르면 어린 시절부터 오직 한 우물만 파는 스파르타식 조기 교육이 세계적 탑티어로 성공할 확률은 10% 미만입니다. 한국 기초과학계가 노벨상 문턱을 넘으려면 인문·예술적 사교 역량과 다양성 중심의 <span class=\"text-amber-300 font-bold\">학습 자본 구축</span>이 시급합니다.",
      "key_claims": [
        "노벨상 과학자의 94%는 프로 수준의 피아노 리사이틀, 시인 등단, 전시회 개최 등 깊이 있는 <span class=\"text-amber-300 font-bold\">예술적 취미</span>를 지니고 있습니다.",
        "헬름홀츠의 음악 살롱과 같이 음악·미술 등 예체능적 공감대는 당대 최고의 석학 및 정책 결정자들과 <span class=\"text-violet-300 font-medium\">긴밀한 글로벌 인적 네트워킹</span>을 맺는 핵심 수단입니다.",
        "학술적 성과에만 매몰되어 해외 학회에서도 자국인끼리만 뭉치는 폐쇄적인 네트워킹 한계를 극복해야 글로벌 핵심 무대에 진입할 수 있습니다."
      ],
      "data_points": [
        "노벨상 수상자의 취미/예술 활동 통계 분석 비중: 비(非)수상 학자 대비 수십 배 이상 높은 참여율 기록",
        "사이언스(Science) 논문 분석: 한 우물만 파는 영재 교육의 최상위권 안착 성공률은 10% 미만"
      ],
      "signal": "na",
      "signal_reason": "과학사 연구와 교육 및 인적 네트워킹의 방법론에 초점을 맞춘 인문 교양 콘텐츠로 금융 투자 자산과의 직접적 상관관계는 없습니다.",
      "key_companies": [],
      "insight": "기초과학의 초격차 혁신은 골방의 단일 연구보다 열린 환경에서의 다양한 아이디어 크로스오버와 <span class=\"text-violet-300 font-medium\">휴먼 네트워크</span>를 통해 탄생합니다. 다방면의 재능을 축적한 융합형 인재 양성을 촉진하는 환경 조성이 국가 경쟁력의 근간입니다.",
      "action_point": "교육 및 인적 인프라 관련 정책 변화를 주시하고, 단기 성과에 집착하는 R&D 투자 구조에서 탈피하여 장기 기초연구 생태계를 지원하는 지적 인프라 기업군을 선별해야 합니다."
    }
  },
  "YjQpZv_dsKI": {
    "primary_topic": "robot",
    "secondary_topics": ["tech"],
    "tags": ["텐던방식", "로보티즈", "1XNEO", "피지컬AI", "로봇손"],
    "analysis": {
      "summary": "로봇의 범용 작업을 위해 1X NEO가 채택한 <span class=\"text-cyan-300 font-semibold\">텐던(Tendon, 와이어 구동) 방식</span>의 로봇 손이 대량 생산 라인 출하를 시작하며 기술 경쟁을 촉발하고 있습니다. 텐던 방식은 모터를 전완근에 배치해 손가락을 극도로 가볍고 섬세하게 만들 수 있어 감자칩 쥐기 등의 미세 작업에 탁월하나, 복잡한 와이어 조립 공정과 마찰 내구성 한계로 단가가 높습니다. 향후 로봇 손 시장은 하드웨어 조립 효율성과 센서 기반 <span class=\"text-cyan-300 font-semibold\">피지컬 AI(임바디드 AI)</span> 데이터 확보가 성패를 가를 것입니다.",
      "key_claims": [
        "텐던 힘줄 손은 손가락 내부에 모터가 없어 <span class=\"text-cyan-300 font-semibold\">가볍고 섬세한 제어</span>(±0.2mm 오차)가 가능하지만, 고중량 작업 시 파손 위험이 큽니다.",
        "로봇 손 제조 단가를 낮추고 양산 안정성을 확보하려면 복잡한 수작업 와이어 케이블링 공정의 자동화 및 <span class=\"text-cyan-300 font-semibold\">초소형 액추에이터</span> 기술이 뒷받침되어야 합니다.",
        "로봇 손의 최종 진화는 두뇌를 거치지 않고 촉각 센서 데이터로 즉시 판단해 반응하는 로컬 '피지컬 AI' 선순환 휠에 있습니다."
      ],
      "data_points": [
        "1X NEO 로봇 손 자유도 스펙: 손목 3자유도, 손가락 22자유도 총 25자유도 구현",
        "1X 로봇 손 올해 생산 목표 대수: 10,000개 양산 목표 수립",
        "로봇 손 위치 정밀도 오차 수준: ±0.2mm 이내 초정밀 구현",
        "텐던 와이어 구동 반복 내구성 테스트 수준: 약 200만 회 작동 보증 완료"
      ],
      "signal": "bullish",
      "signal_reason": "가전 및 물류 등 범용 서비스형 휴머노이드 보급을 위해 대규모 로봇 손 및 전용 액추에이터 부품 수요가 본격적인 대량 양산 국면에 진입했기 때문입니다.",
      "key_companies": ["로보티즈(103030)", "Tesla(TSLA)", "1X"],
      "insight": "생성형 AI가 하드웨어 몸체를 지닌 <span class=\"text-cyan-300 font-semibold\">피지컬 AI</span>로 확장되는 길목에서 정밀 제어 모터와 힘줄 구동용 핵심 부품의 수요가 가파르게 증가하고 있습니다. 특히 텐던 방식용 와이어 구조와 초소형 다이나믹셀 액추에이터는 진입 장벽이 높은 부품 영역입니다.",
      "action_point": "글로벌 로봇 손 설계(오르카 등)에서 핵심 정밀 모터 부품으로 널리 사용되고 있는 다이나믹셀 제조업체인 <span class=\"text-cyan-300 font-semibold\">로보티즈</span>의 부품 공급 계약 및 휴머노이드 전장 수혜 가능성에 적극 주목해야 합니다."
    }
  },
  "ZvcZ39g26uY": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["코스피전망", "PER멀티플", "기업순이익", "실물이익", "밸류에이션"],
    "analysis": {
      "summary": "최근 코스피 지수의 장기적 레벨업 흐름은 단순한 멀티플 확장 버블이 아닌, <span class=\"text-amber-300 font-bold\">실물 기업 순이익의 폭증</span>에 철저히 기반하고 있습니다. 2010년 이후 코스피의 역사적 평균 PER인 9.9배를 내년 상장사 전체 예상 순이익 946조 원에 대입하면 지수 상단은 이론적으로 <span class=\"text-amber-300 font-bold\">11,450포인트</span>에 도달합니다. 반도체 수출 개선으로 무역 수지가 획기적으로 개선되며 국내 증시의 이익 기초 체력이 과거 박스피 시절 대비 4배 이상 커졌습니다.",
      "key_claims": [
        "주가 지수의 본질은 결국 기업 순이익(EPS)과 멀티플(PER)의 곱이며, 코스피의 기초 체력은 <span class=\"text-amber-300 font-bold\">실물 수출 개선</span>에 직결됩니다.",
        "내년도 예상 순이익에 기반한 코스피 예상 시가총액은 약 9,365조 원 규모로, 현재 주가 수준은 버블 우려 없이 철저히 저평가 영역에 속합니다.",
        "이익 팽창에 기반한 증시 체급 상승이므로, 일시적인 센티먼트 악화로 주가가 흔들리더라도 펀더멘탈의 훼손은 발생하지 않았습니다."
      ],
      "data_points": [
        "내년 코스피 전체 상장사 예상 순이익 규모: 약 946조 원 (과거 박스피 시절 연간 200조 원 수준 대비 4.7배 증가)",
        "코스피 예상 시가총액 산출값: 약 9,365조 원 수준 (내년 예상 순이익에 2010년 이후 평균 PER 9.9배 적용)"
      ],
      "signal": "bullish",
      "signal_reason": "전체 상장사의 실질 이익이 반도체 수출 호황을 통해 수직 상승하고 있으며, 역사적 평균 멀티플 대입 시 지수 상승 여력이 무궁무진하기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "현재 한국 증시는 이익의 폭발적인 증가 속도를 멀티플(PER)이 쫓아가지 못하고 있는 전형적인 <span class=\"text-amber-300 font-bold\">실적장세 초입</span> 단계입니다. 외부 매크로 요인으로 지수가 조정을 받을 때마다 이익 체력을 지닌 핵심 수출 기업들을 저가 매수하는 것이 주효합니다.",
      "action_point": "코스피 전체 순이익 증가의 70% 이상을 견인하고 있는 반도체 및 HBM 밸류체인 핵심인 <span class=\"text-cyan-300 font-semibold\">삼성전자/SK하이닉스</span>와 실적 개선이 뚜렷한 대표 대형주들을 중장기 바벨 전략으로 모으는 기회로 삼아야 합니다."
    }
  },
  "ai0Id2yBtGM": {
    "primary_topic": "etc",
    "secondary_topics": [],
    "tags": ["도파민", "신경조절물질", "파킨슨병", "동기부여", "이승훈교수"],
    "analysis": {
      "summary": "도파민(Dopamine)은 단순한 쾌락의 신경 물질이 아닌, 미래의 원대한 목표를 추구하고 실행력을 지탱하는 <span class=\"text-amber-300 font-bold\">희망의 메신저</span>입니다. 뇌의 860억 개 신경 세포 중 중뇌에서 뿜어져 나오는 도파민은 뇌의 전체적인 무드(행간의 뉘앙스)를 조정하며, 반복 학습된 운동을 담당하는 선조체와 동기 유발을 이끄는 전두엽에 작용합니다. 예상보다 큰 예측 오차나 새로운 장기 계획을 세울 때 분비되며, 도파민 결핍 시 파킨슨병이나 중증 우울증으로 직결됩니다.",
      "key_claims": [
        "도파민은 0과 1의 전기적 자극을 전달하는 글루탐산/가바와 달리, 향수처럼 뇌 전체에 분사되어 행동을 유도하는 <span class=\"text-amber-300 font-bold\">신경 조절 물질</span>입니다.",
        "중뇌 흑질에서 선조체로 가는 도파민 회로가 노화 등으로 망가지면 자동으로 저장된 운동 조절이 불가능해져 몸이 얼어붙는 <span class=\"text-rose-400 font-medium\">파킨슨병</span>에 걸립니다.",
        "도파민의 본질은 눈앞의 쾌락을 느낄 때보다, 이상적인 가치나 목표를 달성할 수 있다는 '희망'을 품고 행동을 <span class=\"text-amber-300 font-bold\">지속적으로 추구할 때</span> 왕성하게 분비됩니다."
      ],
      "data_points": [
        "인간 대뇌 전체 신경 세포 수: 약 860억 개 수준",
        "신경 세포 간 시냅스 연결 수: 약 100조 개 수준 (하나의 신경 세포가 약 1,000개 이상의 시냅스 담당)"
      ],
      "signal": "na",
      "signal_reason": "도파민의 의학적 성격과 인류의 생리학적/의학적 뇌 과학 원리를 다루는 순수 학술·의학 강연 콘텐츠이기 때문입니다.",
      "key_companies": [],
      "insight": "인간의 동기 부여와 혁신적 실행력은 도파민이라는 생화학적 인센티브 체계(스톡옵션)를 통해 제어됩니다. 낭만이란 이상을 향해 자신을 갈아 넣을 때 분비되는 도파민의 작용이며, 이를 건강하게 활성화하는 루틴 조성이 <span class=\"text-amber-300 font-bold\">생산성 향상</span>의 열쇠입니다.",
      "action_point": "만성 피로나 인지기능 저하(ADHD 등)를 예방하기 위해 약물성 일시적 도파민 쾌락을 멀리하고, <span class=\"text-amber-300 font-bold\">규칙적인 신체 활동</span>과 명확한 장기 목표 수립을 통해 체내 자연 도파민 활성화를 도모해야 합니다."
    }
  }
}

for vid, val in batch_data.items():
    save_and_delete(vid, val["primary_topic"], val["secondary_topics"], val["tags"], val["analysis"])
print("Batch 3 processing completed.")
