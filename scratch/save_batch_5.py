import json
from pathlib import Path

def save_analysis(video_id, primary_topic, video_data, analysis_data, classification_data):
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
    
    pending_file = Path(f"data/pending/{video_id}.json")
    if pending_file.exists():
        pending_file.unlink()
        print(f"Removed pending: {pending_file}")
        
    synthesis_cache = Path(f"data/synthesis/{primary_topic}.json")
    if synthesis_cache.exists():
        try:
            synthesis_cache.unlink()
            print(f"Invalidated cache: {synthesis_cache}")
        except Exception as e:
            print(f"Error invalidating cache: {e}")

analyses = {
  "lF2WtAUJQWg": {
    "primary": "economy",
    "video": {
      "id": "lF2WtAUJQWg",
      "title": "[김종학의 뉴욕, 지금-6월4일] ‘인플레이션 우려' 연준 페이지북에서 재확인 | 스페이스X, 오는 12일 상장 예정 | 브로드컴, 크라우드 스트라이크, AT&T, 허니웰, 메타",
      "published": "2026-06-04T08:30:00+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=lF2WtAUJQWg",
      "thumbnail": "https://img.youtube.com/vi/lF2WtAUJQWg/hqdefault.jpg"
    },
    "analysis": {
      "summary": "연준 베이지북을 통해 견조한 고용과 완만한 성장 속에서 인플레이션 우려가 재확인되며 시장 금리 상승 및 연말 금리 인상론(74% 확률)이 대두되었습니다. 또한 <span class=\"text-cyan-300 font-semibold\">스페이스X</span>가 주당 135달러(시총 1.8조 달러 규모)로 12일 나스닥 상장을 가시화한 가운데, 장 마감 후 실적을 발표한 <span class=\"text-cyan-300 font-semibold\">브로드컴</span>과 <span class=\"text-cyan-300 font-semibold\">크라우드스트라이크</span>는 높은 기대치(위스퍼 넘버) 미달 및 가이던스 실망으로 시간외 거래에서 급락세를 보이고 있습니다.",
      "key_claims": [
        "연준 베이지북에서 12개 연은 관할 중 10개 지역이 완만히 성장했으나 고금리와 중동 분쟁에 따른 유가/물류비 인플레 경계감이 확인되었다.",
        "스페이스X는 750억 달러 조달을 목표로 상장 절차를 밟고 있으며, 웨드부시는 장기적으로 테슬라와의 합병 가능성(80%)을 높게 평가했다.",
        "앤스로픽이 모건스탠리와 골드만삭스를 주관사로 낙점하고 가을경 최대 1조 달러 밸류의 IPO를 준비 중이다."
      ],
      "data_points": [
        "미국 12월 기준 금리 인상 확률: 74%",
        "5월 ISM 서비스업 PMI: 54.5",
        "4월 공장주문 증가율: 4.8%",
        "스페이스X 희망 공모가: 주당 135달러 (목표 조달액 750억 달러)",
        "스페이스X 평가 가치: 1조 7,700억 ~ 1조 8,000억 달러",
        "스페이스X 나스닥 상장 예정일: 2026년 6월 12일",
        "브로드컴 2분기 매출액: 221억 8,700만 달러 (전년비 +48%)",
        "브로드컴 AI 반도체 매출: 108억 달러 (시장 기대치/위스퍼 110억 달러 소폭 하회)",
        "앤스로픽 기업가치 관측액: 최대 1조 달러"
      ],
      "signal": "bearish",
      "signal_reason": "베이지북의 긴축 연장 시그널과 관세 인상 리스크(한국/일본 등에 12.5% 관세안 제시), 그리고 브로드컴 및 크라우드스트라이크의 실적 발표 후 시간외 폭락이 복합 작용해 기술주 단기 조정 압력을 높입니다.",
      "key_companies": [
        "스페이스X",
        "앤스로픽",
        "브로드컴",
        "크라우드스트라이크",
        "테슬라"
      ],
      "insight": "현재 시장은 고용 강세와 서비스업 확장을 호재가 아닌 '금리 인하 지연 및 인상 위험'이라는 매크로 악재로 해석하는 역방향 장세입니다. 특히 브로드컴의 AI 매출 143% 성장이라는 놀라운 수치마저도 시장의 극단적인 '위스퍼 넘버(Whisper Number)' 기대에 미치지 못해 10% 폭락한 현상은, AI 하드웨어 장기 성장성과 별개로 단기 밸류에이션 피로감이 극에 달했음을 보여줍니다.",
      "action_point": "브로드컴 등 핵심 AI 하드웨어 밸류체인의 실적 미스로 인한 단기 폭락은 실질적 펀더멘탈 훼손이 아닌 높은 기대치 조율 과정이므로, 투매에 동참하기보다 락업 우려가 적은 시점에 분할 매수 기회로 삼는 것이 유리합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["연준베이지북", "스페이스X상장", "앤스로픽IPO", "브로드컴실적", "크라우드스트라이크", "금리인상우려", "관세리스크"]
    }
  },
  "tS-WU2dtgqA": {
    "primary": "economy",
    "video": {
      "id": "tS-WU2dtgqA",
      "title": "[지식뉴스] 주식•부동산? 미 자산 가격 대폭등 시대 \"애초에 미국은 제조업 살릴 생각 없었다\"..트럼프가 AI에 몰빵하는 진짜 이유 (ft.유신익 박사) / 교양이를 부탁해",
      "published": "2026-06-03T10:30:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=tS-WU2dtgqA",
      "thumbnail": "https://img.youtube.com/vi/tS-WU2dtgqA/hqdefault.jpg"
    },
    "analysis": {
      "summary": "글로벌 매크로 관점에서 자산 가치(주식, 고급 부동산) 폭등과 근로 소득의 심각한 양극화 메커니즘을 규명합니다. 미국은 실질 제조업 부활보다는 글로벌 금융 유동성을 미국 내 AI/테크 인프라 자산으로 집중 유치하여 달러 패권 붕괴를 방어하고 자국 자산을 띄우는 금융 패권 수성 전략에 집중하고 있으며, 일론 머스크의 기본 소득(UBI) 구상은 분배 권한과 자산 인프라 독점 한계 측면에서 경제적 모순을 지니고 있습니다.",
      "key_claims": [
        "중앙은행의 돈 풀기는 실물 생산 기계나 노동 가치(정체 상태)보다 경영자와 자본가의 지분 가치(주식 250% 폭등)만 극대화시켰다.",
        "현재 물가 상승의 실체는 생필품이 아니라 부유층의 자산 증식에 의한 고가 주택 및 프리미엄 서비스 가격 폭등(자산 인플레이션)이다.",
        "미국의 패권 수호 전략은 실질 제조업 회복이 아닌 달러 보유국들의 유동성을 자국 AI/테크 자산으로 환류시켜 달러화 신뢰를 방어하는 것이다."
      ],
      "data_points": [
        "글로벌 자산 분배율: 상위 10%가 전체 부의 75% 소유, 하위 50%는 2% 소유",
        "금융위기 이후 글로벌 외환보유고 내 달러화 비중: 60% 하방 경계선 부근 완만히 우하향"
      ],
      "signal": "bearish",
      "signal_reason": "전 세계적인 부의 양극화 극대화와 자산발 인플레이션 고착화는 가계 실질 소비력을 억제하며, 대외 환율 방어로 인한 국내 수입 물가 상승 압박은 한국 중산층 경제에 지속적인 고통을 야기합니다.",
      "key_companies": []
      ,
      "insight": "미국의 대외 정책(IRA, 반도체법 등)의 이면에는 달러 리저브 비중 하락을 방어하기 위해 미국 내 AI 인프라 자산 매력도를 높여 글로벌 유동성을 가두려는 금융공학적 설계가 깔려 있습니다. 이 구조는 노동 소득을 통한 중산층 진입을 차단하고 주식과 지분 중심의 자산 양극화를 고착화시켜 거시적인 사회 구조적 불균형을 심화시키고 있습니다.",
      "action_point": "노동 소득 및 예적금 위주의 자산 포트폴리오를 유지하는 것은 화폐 가치 하락과 자산 양극화에 취약하므로, 미국 내 대체 불가능한 AI 인프라 및 핵심 지분을 소유한 빅테크 지분 중심으로 포트폴리오 체질을 장기적으로 혁신해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["자산인플레이션", "양극화", "달러패권", "유신익", "기본소득모순", "미국금융전략", "화폐가치하락"]
    }
  },
  "3sRr0JbdCaU": {
    "primary": "stock",
    "video": {
      "id": "3sRr0JbdCaU",
      "title": "반도체가 많아도, 주도주가 있어도 혹은 바이오에 울고 있어도 무조건 버티고 지켜볼 것 | 장우진 작가",
      "published": "2026-06-03T09:10:00+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=3sRr0JbdCaU",
      "thumbnail": "https://img.youtube.com/vi/3sRr0JbdCaU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "한국 조선업의 밸류에이션 평가 방식이 과거 수주 잔고 위주의 PBR(0.3~0.4배 수준)에서 실질적 흑자 지속에 따른 PER 기반으로 전환되며 구조적 기업가치 상승 국면에 도달했습니다. 선주사(그리스 선박왕 등)들은 글로벌 해운 운임이 높은 수준을 유지함에 따라 비싼 가격에도 신규 발주를 지속하고 있으며, IMO의 2030년 환경 규제 등급 강화로 노후선 교체가 강제되어 조선사들의 판매자 우위 구도가 장기화될 전망입니다.",
      "key_claims": [
        "조선업은 역사상 처음으로 장기 흑자 구조의 영속성을 입증하며 자산 가치(PBR)가 아닌 수익 가치(PER) 리레이팅을 시도하고 있다.",
        "해운사들이 선가 상승(2020년 대비 70~80% 급증) 부담보다 정시 배달 프리미엄(운임 정상화)을 중요시함에 따라 발주 모멘텀이 유지된다.",
        "글로벌 조선소 구조조정으로 대형선 수용 능력을 갖춘 한국의 과점 조선사들이 글로벌 환경 규제 강화(노후선 교체)의 최대 수혜를 누린다."
      ],
      "data_points": [
        "2020년 대비 개별 선박 가격 상승률: 70% ~ 80%",
        "선가 지수 상승률: 50% ~ 60%"
      ],
      "signal": "bullish",
      "signal_reason": "글로벌 선박 공급 병목 속에서 친환경 규제 교체 주기와 고운임 환경이 결합되어 국내 조선사들의 수주 단가 상승 및 실질 이익 턴어라운드가 향후 2~3년간 지속될 가능성이 높습니다.",
      "key_companies": [
        "HD한국조선해양",
        "삼성중공업",
        "한화오션"
      ],
      "insight": "글로벌 물류 시장은 '저비용 운송'에서 지정학적 갈등(이란 등) 우회를 위한 '정시 공급 보장'으로 패러다임이 이동했습니다. 이는 선주사들이 고선가에도 불구하고 선대 투자를 아끼지 않게 만드는 뇌관이 되었으며, 조선사들이 적자 수주 경쟁에서 완전히 벗어나 고마진 선별 수주를 독식하는 배경이 됩니다.",
      "action_point": "조선주 주가 상승에 따른 밸류에이션 부담 우려로 조기 매도하기보다, 선가 상승분이 본격 영업이익으로 꽂히는 실적 장세 국면까지 보유를 유지하고 조정 시 추가 매수 기회로 삼아야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["energy", "economy"],
      "tags": ["조선업밸류에이션", "PER리레이팅", "선가상승", "친환경선박", "IMO규제", "선주사발주", "해운운임"]
    }
  },
  "eNNcin54184": {
    "primary": "stock",
    "video": {
      "id": "eNNcin54184",
      "title": "지금같은 시장에서 주식 수익률을 높이는 가장 확실한 방법은 \"아무것도 하지 않기\"",
      "published": "2026-06-03T08:30:00+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=eNNcin54184",
      "thumbnail": "https://img.youtube.com/vi/eNNcin54184/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아의 젠슨 황 CEO가 대만 타이베이에서 한국 주요 대기업 총수들(삼성, SK, LG, 네이버, 두산)을 초청해 사상 최초의 만찬(소맥 회동)을 가지고 한국 방문 일정을 조율하는 등 한국 공급망에 대한 강력한 러브콜을 보냈습니다. AI 기술 도입으로 전 세계 3천만 개발자의 생산성이 3배 증가해 $9조 규모의 가치가 창출될 전망인 가운데, 투자자들은 무지성 테마 추종 대신 실질적 수혜주 중심의 선별 투자가 중요함을 역설합니다.",
      "key_claims": [
        "엔비디아는 반도체뿐만 아니라 과학, 로보틱스, AI 팩토리를 아우르는 한국 공급망 파트너십을 미래 핵심 동력으로 재정의했다.",
        "젠슨 황의 방한 일정과 한국 주요 총수들과의 연쇄 회동은 메모리(HBM) 및 온디바이스 AI, 로보틱스 협력을 구체화하기 위한 행보다.",
        "전 세계 개발자 3천만 명의 연봉 합계는 $3조이며, AI 생산성 3배 향상은 연간 $9조의 경제적 파급 효과를 야기한다."
      ],
      "data_points": [
        "전 세계 소프트웨어 개발자 수: 약 3,000만 명",
        "글로벌 개발자 총 연봉 규모: 약 3조 달러",
        "AI 생산성 증대에 따른 개발 가치 스케일: 약 9조 달러"
      ],
      "signal": "bullish",
      "signal_reason": "글로벌 시총 1위 엔비디아가 한국 반도체 및 로봇, IT 인프라 파트너들을 강력한 동맹군(깜부)으로 지정하고 협업을 수직 계열화함에 따라, 국내 대형 IT 및 반도체 섹터의 실적 성장은 확실한 가시성을 얻었습니다.",
      "key_companies": [
        "엔비디아",
        "삼성전자",
        "SK하이닉스",
        "네이버",
        "두산"
      ],
      "insight": "젠슨 황의 '소맥 마케팅'과 한국 기자 샤라웃은 대만 파운드리와 한국 메모리·IT 연합을 조율해 독점적 생태계를 완성하려는 정교한 비즈니스 제스처입니다. 개발자 연봉 $3조 대비 AI 도입 가치 $9조라는 생산성 공식은 빅테크들이 AI 인프라(GPU/HBM) 구매를 멈추지 못하는 명확한 ROI적 근거를 제시합니다.",
      "action_point": "단순 만남 소식에 급등락하는 중소형 테크 테마주에 대한 무지성 투자를 멈추고, 엔비디아의 핵심 밸류체인과 연결되어 실질적 매출 성장을 입증하는 메모리 대장주와 인프라 대형주 지분을 뚝심 있게 지켜야 합니다."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["젠슨황방한", "한국대기업만찬", "HBM동맹", "개발자생산성", "AI팩토리", "선별투자", "이효석"]
    }
  },
  "sLnpiyRT_nM": {
    "primary": "tech",
    "video": {
      "id": "sLnpiyRT_nM",
      "title": "젠슨황 직접 보고 왔습니다… GTC Taipei 키노트 핵심 | AI Agent가 인프라 모든 걸 바꾸다",
      "published": "2026-06-03T06:00:00+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=sLnpiyRT_nM",
      "thumbnail": "https://img.youtube.com/vi/sLnpiyRT_nM/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아 컴퓨텍스(GTC Taipei) 키노트 분석을 통해 AI 컴퓨팅이 단순 비용(Cost Center)에서 24시간 토큰을 찍어내 매출을 내는 디지털 공장인 '매출 센터(Revenue Center)'로 전환되었음을 설명합니다. 전력당 토큰 생산비용을 낮추는 **'전력당 토큰(Tokens per Watt)'**과 **'에이전트 처리량(Agent Throughput)'**이 AI 팩토리의 새로운 지표로 제시되었으며, 엔비디아는 하네스 기반 AI 에이전트와 DSX 플랫폼을 앞세워 인프라 수직 계열화를 공고히 하고 있습니다.",
      "key_claims": [
        "AI 컴퓨팅은 사용자가 서비스를 구동해 추론이 발생할 때마다 매출이 찍히는 '컴퓨트가 곧 매출(Computing is Revenue)' 패러다임으로 안착했다.",
        "AI 팩토리 평가는 단일 칩 속도를 넘어, 한정된 전력 한계 하에 최대 토큰 매출을 내는 전력당 토큰(Tokens per Watt) 설계 경쟁이다.",
        "엔비디아는 AI 팩토리의 효율적 설계를 지원하는 플랫폼 'DSX'와 차세대 베라 루빈(Vera Rubin) 시스템 스택을 통해 표준화를 가속하고 있다."
      ],
      "data_points": [
        "AI 팩토리 핵심 최적화 지표: Tokens per Watt, Agent Throughput",
        "AI 에이전트 정의: LLM (두뇌) + Harness (규칙/제약조건)"
      ],
      "signal": "bullish",
      "signal_reason": "엔비디아가 전력 및 시스템 단위 설계 최적화(DSX)를 독점 제공하며 AI 에이전트 구동에 따른 토큰 매출 극대화 프레임을 완성함에 따라, 엔비디아 풀스택 인프라 플랫폼의 독점력과 단가는 더욱 탄탄해질 전망입니다.",
      "key_companies": [
        "엔비디아"
      ],
      "insight": "엔비디아는 GPU 파는 하드웨어 업체를 넘어 AI 전력과 인프라 효율성을 표준화하는 OS 플랫폼사로 자리 잡았습니다. 'Computing is Revenue' 논리는 고객들이 인프라 투자를 단순 비용이 아닌 실시간 토큰 인쇄기(Token Printer) 구매로 인식하게 만들어, 매크로 둔화 우려 속에서도 빅테크들의 지속 투자를 강제하는 마법의 프레임입니다.",
      "action_point": "엔비디아의 DSX 플랫폼 및 루빈 랙 스케일 아키텍처 도입에 따른 고성능 냉각 솔루션(수냉식 등), 액체 냉각 장비주 및 전력 최적화 관련 반도체 기판(CCL 등) 및 부품 밸류체인의 기술적 주도 기업군을 집중 탐색해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock", "energy"],
      "tags": ["컴퓨텍스", "ComputingIsRevenue", "AI팩토리", "TokensPerWatt", "DSX플랫폼", "베라루빈", "AI에이전트"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["video"], info["analysis"], info["classification"])
