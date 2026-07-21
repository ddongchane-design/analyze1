import json
from pathlib import Path

def save_and_delete(video_id, primary_topic, secondary_topics, tags, analysis_data):
    pending_path = Path(f"data/pending/{video_id}.json")
    if not pending_path.exists():
        print(f"Error: {pending_path} does not exist.")
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

batch_8 = {
  "JTBk1MUy4Fw": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["코스피8500", "반도체눌림목", "코스닥순환매", "제시리버모어", "이재규"],
    "analysis": {
      "summary": "코스피의 8,500포인트 안착 여부와 함께 하반기 주식 전략을 제시함. 반도체가 밀릴 때마다 매수로 대응하는 **반도체 눌림목 패턴**과 코스닥의 단기 기술적 순환매 반등이 '사람의 반복적 투자 심리'에 기인하여 재차 반복될 가능성이 높다고 분석함. 다만, 반도체 기업들의 이익률이 최고점에 도달했기에 폭발적 속도 조절 가능성도 염두에 둘 것을 조언함.",
      "key_claims": [
        "최근 수개월간 반도체는 조정 시 매수(밀리면 매수) 전략이 100% 수익으로 귀결되는 패턴이 반복되었으며, 이 추세는 여전히 유효함.",
        "코스피 지수는 단기 변동성에도 불구하고 8,500포인트를 돌파/안착할 경우 상방 지지력이 매우 탄탄해지며 우상향 추세를 복귀하게 됨.",
        "인간의 욕망과 공포 심리가 주가를 움직이는 한 주식 시장의 차트 패턴은 반복되며, 개인들의 과도한 포모(FOMO) 심리가 폭발할 때 고점 리스크를 대비해야 함."
      ],
      "data_points": [
        "코스피 복귀 목표 지수: 8,500포인트 이상 마감 시 5일 이동평균선 우상향 전환 및 하방 경직성 확보",
        "국내 환율 뉴노멀 전망: 1,500원 이하로 내려가지 않는 고환율 국면 장기화 가능성 제기"
      ],
      "signal": "bullish",
      "signal_reason": "코스피의 견고한 중장기 우상향 추세(8,500선 안착 대기)가 이어지는 가운데, 조정 시 반도체를 매수하는 눌림목 반복 전략의 신뢰성이 매우 높기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "주식 시장의 기술적 분석은 단순히 숫자의 나열이 아니라 투자 참여자들의 심리적 반복 행위(Repetition)의 산물입니다. 특히 반도체 독주에 지친 개인 수급이 낙폭과대 코스닥 종목이나 2차전지로 순환 매수를 감행하는 단기 소동이 있으나, 이익 가시성이 가장 뚜렷한 <span class=\"text-cyan-300 font-semibold\">메모리 대형주</span>로 자금이 복귀하는 쏠림 현상의 큰 궤적은 변하지 않을 것입니다.",
      "action_point": "코스피 지수 <span class=\"text-cyan-300 font-semibold\">8,500선</span> 부근의 지지력을 확인하며 반도체 대장주들이 조정을 받을 때마다 비중을 늘리는 분할 매수 전략을 유지하고, 코스닥 잡주로의 무분별한 뇌동매매는 극도로 경계해야 합니다."
    }
  },
  "lKxiy3gtR3M": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["테이크오어페이", "반도체담합소송", "LTA장기계약", "번스타인경고", "이효석"],
    "analysis": {
      "summary": "삼성전자와 SK하이닉스의 10개년 장기 대규모 설비 투자를 둘러싼 시장의 공급 과잉 우려(번스타인의 2027년 피크아웃 경고)를 조목조목 반박함. 과거와 달리 현재 메모리 계약은 고객사가 칩을 인수하지 않아도 대금을 전액 지불해야 하는 **테이크 오어 페이(Take-or-Pay)** 장기계약(LTA) 구조로 전환되어 실적 변동성이 크게 상쇄되었으며, HBM 생산에 따른 웨이퍼 손실이 자연스러운 공급 제한 효과를 유도하고 있음을 설명함.",
      "key_claims": [
        "과거에는 빅테크(아마존 등)가 업황 둔화 시 반도체 주문을 일방적으로 취소해 제조사가 재고 손실을 독박 썼으나, 현재는 'Take-or-Pay' LTA 계약 체결로 실적 해자가 구축됨.",
        "미국 소비자들이 메모리 3사를 대상으로 제기한 담합 소송은 HBM 제조 시 발생하는 극심한 웨이퍼 공정 손실률(Yield Loss)로 인한 자연스러운 공급 제한을 오해한 결과에 가깝고 법적 영향력은 제한적임.",
        "JP모건의 '아킬라 셰프(Aquila Chef, 독수리+문어 괴물)' 보고서가 보여주듯 미국 부채 우려에도 글로벌 유동성은 독보적인 생산성을 보유한 미국 시장과 달러 경제로 쏠리고 있음."
      ],
      "data_points": [
        "SK하이닉스/삼성전자 장기 투자 기간: 향후 10년 단위 메가 클러스터 및 용인 단지 투자 가동 계획",
        "번스타인 사이클 전망: 2027년 말 반도체 이익 정점 돌파 후 2028년 하강 예측 (SCA 계약으로 실현 가능성 낮음)"
      ],
      "signal": "bullish",
      "signal_reason": "전략적 장기 공급 계약(SCA/LTA)의 확산과 HBM 생산에 따른 DRAM 자연 감산 효과 덕분에 반도체 대기업들의 이익 지속 기간(Earnings Runway)이 역사적 사이클보다 훨씬 길어질 것이기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "Micron", "NVIDIA"],
      "insight": "반도체 공급 과잉 시나리오를 주장하는 리포트들은 메모리 업계의 근본적인 계약 체질 개선(Take-or-Pay 규정 적용)을 과소평가하고 있습니다. 헬스장 장기 회원권처럼 불이행 시 대금 회수가 보장되는 <span class=\"text-cyan-300 font-semibold\">전략적 장기 계약(SCA)</span>은 반도체 산업을 경기 민감주(Cyclical)에서 구독형 비즈니스 모델(SaaS)에 준하는 안정성으로 체질을 리레이팅하는 핵심 요인입니다.",
      "action_point": "번스타인 등 외국계 증권사의 2027년 조기 꺾임설로 인한 단기 주가 흔들림은 매수 적기입니다. 공급망 주도권을 쥔 <span class=\"text-cyan-300 font-semibold\">SK하이닉스 및 삼성전자</span>의 SCA 비중과 장기 이익 가시성을 기반으로 장기 투자를 이어가야 합니다."
    }
  },
  "lMES84se7wI": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["테슬라급등", "HDD수혜", "나스닥100편입", "금리하락", "드론원자력"],
    "analysis": {
      "summary": "구글 알파벳(다우지수 편입 효과) 및 테슬라(인도량 기대감 8% 급등) 중심의 기술주 반등과 반도체 변동성 지속 원인을 분석함. AI 데이터 저장 수요가 SSD를 넘어 물리적 대용량 하드디스크(HDD)로도 확산되며 시게이트와 웨스턴 디지털이 초강세를 나타냈으며, 미국 10년물 국채 금리가 4.3%대로 하락하며 성장주에 우호적인 환경이 조성되고 있음을 분석함.",
      "key_claims": [
        "알파벳의 다우지수 1일차 편입 효과와 스페이스X의 7월 초 나스닥100 편입 기대 수급이 대형 기술주들의 강력한 수급 방패 역할을 함.",
        "AI 서버 데이터 폭증으로 고대역폭 메모리/SSD에 이어 전통적 대용량 물리 드라이브(HDD) 쇼티지가 심화되며 관련 리더 기업들의 이익이 크게 개선됨.",
        "스페이스X의 스마트폰 위성 직접 연결(Direct-to-Cell) 사업 구체화 및 파트너 발굴(차터 커뮤니케이션)은 기존 지상파 통신주들의 멀티플을 압박하는 요인으로 작용함."
      ],
      "data_points": [
        "주요 종목 등락률: 테슬라 8% 급등, 알파벳 5% 상승, 이온큐(IONQ) 9% 반등",
        "미국 10년물 국채 금리: 4.3% 선 아래로 추가 하락 (유가 하향 안정화 연동)"
      ],
      "signal": "bullish",
      "signal_reason": "미국 10년물 금리의 4.3%대 안정화 및 지수 편입 패시브 수급 유입에 더해, AI 데이터센터용 스토리지 수혜가 SSD에서 HDD 분야로 광범위하게 확산되며 업황 반등 강도가 우수하기 때문입니다.",
      "key_companies": ["Alphabet(GOOGL)", "Tesla(TSLA)", "Seagate", "Western Digital"],
      "insight": "AI 인프라 투자의 흐름이 연산(NVIDIA) -> 메모리(HBM/DRAM) -> 초고속 저장장치(SSD)를 지나, 최종 아카이빙 대용량 원자재인 <span class=\"text-cyan-300 font-semibold\">HDD</span> 영역으로 확장되는 밸류체인 이동 흐름이 확인되었습니다. 또한 금리 안정화 속에 테슬라의 2분기 인도량 반등 모멘텀이 맞물리며 친환경 2차전지 전반으로 온기가 확산될 예고편을 보여주고 있습니다.",
      "action_point": "디램과 낸드 플래시 일변도에서 벗어나 AI 빅데이터의 실질적 저장소 역할을 하는 <span class=\"text-cyan-300 font-semibold\">시게이트(Seagate) 및 웨스턴 디지털(Western Digital)</span> 등 하드디스크 드라이브 관련사 지분을 포트폴리오에 추가 편입하는 전략이 필요합니다."
    }
  },
  "mvdT1R3bMi8": {
    "primary_topic": "economy",
    "secondary_topics": ["energy", "stock"],
    "tags": ["호남800조", "송배전기기", "신재생에너지", "그리드인프라", "지방시대"],
    "analysis": {
      "summary": "호남 지역에 신재생에너지, 그리드 인프라, 전력망 고도화를 중심으로 한 **800조 원 규모의 대규모 국책/민간 연계 투자 사업**의 경제적 실효성과 실질 수혜 기업들을 짚어봄. 태양광·풍력 등 발전원 증설보다 생성된 전력을 소비지로 보내기 위한 송배전망 인프라가 최대 병목임을 분석하고, 전력 기기 대기업들의 구조적 장기 수혜를 전망함.",
      "key_claims": [
        "정부 주도의 호남 800조 프로젝트는 단순히 발전 설비를 늘리는 것을 넘어 호남의 풍부한 무탄소 에너지(CFE)를 수도권 반도체 클러스터로 송전하기 위한 그리드 고도화가 본질임.",
        "국내 전력 그리드의 최대 약점인 '동해안/호남-수도권' 송전선로 부족 문제를 해결하기 위해 초고압직류송전(HVDC) 및 변전 인프라 조기 착공이 강제될 것임.",
        "재생에너지 발전사들은 그리드 연계 지연으로 출력 제한 페널티를 겪고 있으므로, 송전 기기 선도 기업들의 수주 독점이 장기화될 수밖에 없음."
      ],
      "data_points": [
        "호남 메가 프로젝트 총 예산 규모: 정부 및 민간 재원 합산 약 800조 원 규모의 장기 청사진 수립",
        "핵심 공급망 병목: 송배전 전력망 부하율 포화로 인해 신규 발전 설비의 그리드 접속 대기 기간이 수년 이상 지체 중"
      ],
      "signal": "bullish",
      "signal_reason": "조 단위의 대형 전력망 국책 프로젝트가 공식화됨에 따라 초고압 HVDC 및 변압기를 제조하는 국내 전력 기기 핵심 대기업들의 중장기 국내 수주 파이프라인이 확실히 보장되기 때문입니다.",
      "key_companies": ["LS Electric(010120)", "HD현대일렉트릭(267260)", "효성중공업(094820)"],
      "insight": "태양광 패널 등 발전원 투자는 중국의 저가 공세로 경제성이 떨어지지만, 국가 전력 백본망을 구성하는 <span class=\"text-cyan-300 font-semibold\">초고압 변압기 및 배전 솔루션</span>은 고도의 공학적 신뢰성이 필요해 국내 빅3 변압기 제조사들이 독점 구도를 형성하고 있습니다. 호남 800조 투자는 국내 전력 기기 기업들에게 미국 수출 호황에 더해 강력한 '안방 내수 수주 엔진'을 추가로 제공하는 격입니다.",
      "action_point": "미국 데이터센터 발 변압기 쇼티지에 국내 대규모 송배전망 프로젝트 모멘텀이 추가된 만큼, 가격 조정을 겪은 <span class=\"text-cyan-300 font-semibold\">LS Electric 및 HD현대일렉트릭</span>에 대한 비중 확대를 변함없이 최우선 포지션으로 가져가야 합니다."
    }
  },
  "NClzF2H2Aag": {
    "primary_topic": "etc",
    "secondary_topics": [],
    "tags": ["AMOC", "해류순환", "기후변화", "티핑포인트", "안될과학"],
    "analysis": {
      "summary": "지구 기후 조절의 중추 역할을 수행하는 대서양 열염순환(AMOC, 대서양 자오선 역전순환)의 감속 메커니즘과 그에 따른 재앙적 시나리오를 과학적으로 설명함. 그린란드 빙하 융해로 인한 염분 농도 저하가 심해 침강을 막아 해류 순환을 멈추고 있으며, 이 티핑포인트 도달 시 서유럽의 빙하기 회귀 및 글로벌 식량 생산 붕괴가 초래될 수 있음을 경고함.",
      "key_claims": [
        "AMOC는 저지대의 열에너지를 고위도로 수송하는 지구의 거대한 난방 벨트 역할을 수행하며, 북대서양의 고염분 냉수가 가라앉는 침강 운동이 동력원임.",
        "지구 온난화로 그린란드의 담수가 북대서양으로 대량 유입되면서 바닷물의 염분 밀도가 희석되어 아래로 가라앉지 못해 순환 속도가 급격히 둔화되고 있음.",
        "AMOC가 완전히 붕괴될 경우 유럽 평균 기온은 10~15도 급락해 농업이 마비되고, 미국 동부 해안의 해수면이 수십 센티미터 급상승해 주요 도심이 침수되는 국가적 리스크가 발생함."
      ],
      "data_points": [
        "AMOC 순환 속도 변화: 지난 1,000년 역사상 현재 가장 약화된 상태이며 최신 모델은 21세기 내 붕괴 확률이 급증하고 있음을 제시"
      ],
      "signal": "neutral",
      "signal_reason": "대서양 심층 해류의 물리적 감속 기전과 환경적 파급력을 고찰하는 지구 과학 교육 콘텐츠로, 단기 자본 시장 및 주가 등락에는 직접적인 인과 관계가 없기 때문입니다.",
      "key_companies": [],
      "insight": "기후 변화의 '티핑 포인트(Tipping Point)' 중 하나인 <span class=\"text-rose-400 font-medium\">AMOC 둔화</span>는 한 번 멈추면 인간의 기술력으로 되돌릴 수 없는 불가역적인 파멸적 변화입니다. 이는 장기적으로 인구 이동, 글로벌 해운 물류 경로 변화, 농업 비즈니스의 지형 개편을 요구하므로 탄소 배출 규제 준수 및 무탄소 전원(원자력, 신재생)으로의 인프라 전환 속도를 더욱 높이는 강력한 거시적 압력으로 작용할 것입니다.",
      "action_point": "환경 기후 리스크의 장기 심화에 대응하여 저탄소/무탄소 에너지 포트폴리오를 공고히 유지하고, 글로벌 친환경 정책 강화 수혜를 볼 수 있는 핵심 <span class=\"text-cyan-300 font-semibold\">원자력 및 송배전 핵심 망 관련 주식</span>들을 꾸준히 관찰해야 합니다."
    }
  },
  "ntqOoAXHchY": {
    "primary_topic": "economy",
    "secondary_topics": ["stock"],
    "tags": ["반도체독주", "하반기전략", "유동성한계", "종목장세", "박병창"],
    "analysis": {
      "summary": "하반기 국내외 주식 시장의 핵심 동향과 반도체 주도권 지속 여부를 점검함. 빅테크 기업들의 막강한 현금 보유력과 AI 필수 설비인 HBM의 비탄력적 수요로 인해 반도체 섹터의 독주 체제는 연말까지 굳건히 유지될 것이나, 국내 시장 전체의 유동성 부족으로 지수 상승보다 철저한 **개별 수혜 종목 중심의 장세**가 펼쳐질 것임을 전망함.",
      "key_claims": [
        "미국 빅테크의 막대한 캐시플로우가 AI 서버 구축에 재투자되고 있어, 고성능 HBM과 파운드리 칩의 전방 수요 둔화 가능성은 매우 낮음.",
        "국내 증시의 예탁금 및 유동성 총량이 정체되어 있어 시장 전체가 상승하는 대세 상승장보다는, 주도 섹터(반도체) 내 소부장 테마나 개별 바이오 breakout 종목 위주로 매기 쏠림이 유도됨.",
        "미국 대선 및 지정학적 변수에 따른 거시 유가 등락은 단기 노이즈에 불과하며, 실적 성장률이 주가를 압도하는 펀더멘탈 본원 가치에 집중해야 함."
      ],
      "data_points": [
        "빅테크 기업들의 AI 설비 투자 비중: 전체 자유현금흐름(FCF)의 30% 이상을 AI 전용 서버 및 인프라 구축에 우선 배정 중"
      ],
      "signal": "bullish",
      "signal_reason": "빅테크 자금력을 바탕으로 한 반도체 설비 투자 기조가 확고히 유지되고 있으며, 유동성 제한 환경에서 주도 업종인 반도체 소부장 테마로의 쏠림이 가중되기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "지수가 무겁게 정체되는 국면일수록 실적 성장 가시성이 100% 보장된 <span class=\"text-cyan-300 font-semibold\">메모리 공급망 소부장(소재·부품·장비)</span> 강소기업들의 주가 탄력성이 훨씬 도드라집니다. 하반기 증시는 지수 플레이(지수형 ETF)보다는 HBM 수율 개선의 직접적 수혜를 누리는 미세 공정 검사 장비사나 고성능 패키징 특화 기업을 선별해 내는 능력이 초과 수익률(Alpha)의 차이를 만들 것입니다.",
      "action_point": "코스피/코스닥 레버리지 지수 추종 상품의 비중은 축소하되, HBM 검사 및 친환경 패키징 핵심 공정 장비를 독점 공급하는 <span class=\"text-cyan-300 font-semibold\">반도체 강소 소부장 기업</span>들을 발굴해 집중 편입하는 종목 장세 전략을 실행해야 합니다."
    }
  }
}

for vid, data in batch_8.items():
    save_and_delete(
        video_id=vid,
        primary_topic=data["primary_topic"],
        secondary_topics=data["secondary_topics"],
        tags=data["tags"],
        analysis_data=data["analysis"]
    )
print("Batch 8 processing completed!")
