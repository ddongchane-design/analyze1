import json
from pathlib import Path

def save_analysis(video_id, primary_topic, video_data, analysis_data, classification_data):
    # Create analyzed directory
    analyzed_dir = Path(f"data/analyzed/{primary_topic}")
    analyzed_dir.mkdir(parents=True, exist_ok=True)
    
    # Save file
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
    
    # Remove from pending
    pending_file = Path(f"data/pending/{video_id}.json")
    if pending_file.exists():
        pending_file.unlink()
        print(f"Removed pending: {pending_file}")
        
    # Invalidate synthesis cache
    synthesis_cache = Path(f"data/synthesis/{primary_topic}.json")
    if synthesis_cache.exists():
        try:
            synthesis_cache.unlink()
            print(f"Invalidated cache: {synthesis_cache}")
        except Exception as e:
            print(f"Error invalidating cache: {e}")

# Data definitions
analyses = {
  "6jLIhlLokRQ": {
    "primary": "tech",
    "video": {
      "id": "6jLIhlLokRQ",
      "title": "엔비디아가 투자한 최초의 한국 기업",
      "published": "2026-06-03T01:00:00+00:00",
      "channel_name": "Softdragon SOD",
      "url": "https://www.youtube.com/watch?v=6jLIhlLokRQ",
      "thumbnail": "https://img.youtube.com/vi/6jLIhlLokRQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">엔비디아</span>가 한국 팹리스 스타트업에 이례적으로 선제 투자를 단행했으며, 해당 기업의 1.6라비(1.6Tbps) 광통신 제품 상용화를 목전에 두고 있습니다. 이는 기존 스마트폰 통신 속도 대비 1600배 빠른 차세대 속도로, 엔비디아의 차세대 GPU 칩인 <span class=\"text-cyan-300 font-semibold\">베라 루빈</span>(Vera Rubin) 등에 접목될 예정입니다.",
      "key_claims": [
        "엔비디아가 한국 팹리스 스타트업에 최초이자 이례적으로 지분 투자를 단행하며 협력을 강화하고 있다.",
        "상용화 임박한 1.6라비(1.6Tbps) 제품은 스마트폰 속도의 1,600배에 달하는 차세대 고속 통신 규격이다.",
        "엔비디아는 차세대 GPU인 <span class=\"text-cyan-300 font-semibold\">베라 루빈</span>(Vera Rubin) 칩셋에 광학(Optical) 및 튜브 기술을 적용하기 위해 선제적으로 투자했다."
      ],
      "data_points": [
        "통신 속도: 스마트폰의 1,600배",
        "주요 규격: 1.6Tbps (1.6라비)"
      ],
      "signal": "bullish",
      "signal_reason": "엔비디아가 차세대 베라 루빈 칩에 광학 통신 인터커넥트 기술을 탑재하기 위해 한국 팹리스에 선제 투자했다는 점은 광통신 부품 기업 및 관련 생태계에 강력한 성장 신호입니다.",
      "key_companies": [
        "엔비디아",
        "포인트테크놀로지"
      ],
      "insight": "AI 연산 능력이 급증함에 따라 데이터센터 내 칩 간 통신 병목현상이 핵심 과제로 부상했습니다. 엔비디아가 한국의 광학 기술 스타트업에 직접 투자한 것은 차세대 AI 인프라에서 전기 동선 중심의 인터커넥트가 광통신(Optical)으로 급격히 전환될 것임을 시사합니다.",
      "action_point": "차세대 엔비디아 GPU 로드맵(베라 루빈)과 연계된 광통신(Silicon Photonics, CPO) 기술을 보유한 국내 반도체 디자인하우스 및 광부품 밸류체인에 주목해야 합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["엔비디아", "광통신", "팹리스", "베라루빈", "스타트업투자"]
    }
  },
  "ydBdKKLp6Jk": {
    "primary": "etc",
    "video": {
      "id": "ydBdKKLp6Jk",
      "title": "[M-STOCK 이용가이드] 담보대출 투자자정보확인서",
      "published": "2026-06-03T02:00:00+00:00",
      "channel_name": "Smart Money by MiraeAsset",
      "url": "https://www.youtube.com/watch?v=ydBdKKLp6Jk",
      "thumbnail": "https://img.youtube.com/vi/ydBdKKLp6Jk/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">미래에셋증권</span> M-STOCK 앱에서 주식 담보 대출 약정 시 필요한 투자자 정보 확인서 및 신용공여 설문 작성 절차에 대한 가이드입니다. 고객의 투자 성향과 대출 용도를 확인하고 약관 동의를 완료하면 담보 대출을 신청할 수 있습니다.",
      "key_claims": [
        "담보 대출 약정을 위해서는 신용공여 투자자 정보 확인서 작성이 선행되어야 한다.",
        "고객 투자 성향 및 대출 용도 조회를 통해 적절한 여신 한도가 제공된다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "단순한 미래에셋 M-STOCK MTS 사용 가이드 영상으로 시장 지표나 개별 종목에 대한 투자 의견을 포함하지 않는 정보성 콘텐츠입니다.",
      "key_companies": [
        "미래에셋증권"
      ],
      "insight": "증권사의 디지털 담보대출 및 신용공여 가이드는 리테일 투자자들의 레버리지 투자 편의성을 제고하고 증권사의 이자 수익 비즈니스 운영을 지원하는 기초적인 금융 서비스 절차입니다.",
      "action_point": "미래에셋증권 이용 고객은 담보 대출 약정 전 투자성향 확인 및 금리 조건을 꼼꼼히 체크하여 안전한 자금 운용을 도모해야 합니다."
    },
    "classification": {
      "primary_topic": "etc",
      "secondary_topics": [],
      "tags": ["미래에셋증권", "M-STOCK", "담보대출", "이용가이드", "신용공여"]
    }
  },
  "6zsK09d1Wr4": {
    "primary": "economy",
    "video": {
      "id": "6zsK09d1Wr4",
      "title": "환율 1500원, 금리 5%시대? 한국 경제 뒤흔들 3대 시소 게임 #교양이를부탁해",
      "published": "2026-06-03T10:00:31+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=6zsK09d1Wr4",
      "thumbnail": "https://img.youtube.com/vi/6zsK09d1Wr4/hqdefault.jpg"
    },
    "analysis": {
      "summary": "현재 한국 경제가 미국·일본 채권 시장의 충돌, AI 밸류에이션 대 <span class=\"text-rose-400 font-medium\">고금리</span>(5%) 시대의 맞물림, 그리고 1,500원대 <span class=\"text-rose-400 font-medium\">고환율</span>과 <span class=\"text-rose-400 font-medium\">가계부채</span>라는 3대 위기 시소 게임에 직면해 있습니다. 이 시소들의 균형이 깨질 경우 국내 실물 경제와 금융 시장이 큰 충격을 받을 수 있어 정책당국의 정교한 조율이 필요합니다.",
      "key_claims": [
        "미국과 일본의 채권 시장 갈등이 글로벌 유동성과 한국 채권 금리에 심각한 압박을 가하고 있다.",
        "인공지능(AI) 중심의 성장 동력과 5%대 고금리 환경이 충돌하며 옥석 가리기가 촉발되고 있다.",
        "1,500원에 육박하는 고환율과 거대한 가계부채 규모가 맞물려 소비 위축 및 이자 부담 리스크를 증대시키고 있다."
      ],
      "data_points": [
        "환율: 1,500원대",
        "금리 수준: 5%"
      ],
      "signal": "bearish",
      "signal_reason": "고환율, 고금리, 해외 채권 충돌 등 거시경제적 악재가 겹치며 국내 가계부채 뇌관을 자극하고 실물 경기 침체 우려를 가속화시키고 있습니다.",
      "key_companies": [],
      "insight": "한국 경제는 내수 회복을 방해하는 가계부채와 대외 거시 변수(환율·금리)의 틈바구니에 끼어 있습니다. 특히 고금리 장기화는 AI 중심의 자본 투자를 지속해야 하는 빅테크와 중소형 협력사 간의 양극화를 더욱 심화시키는 계기가 될 것입니다.",
      "action_point": "고환율 및 고금리 국면에서 기초 체력이 약한 내수 업종에 대한 노출을 줄이고, 외환 변동성 리스크가 낮고 안정적인 현금 흐름을 창출하는 방어주 및 핵심 수출 대형주 위주로 포트폴리오를 다변화해야 합니다."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock"],
      "tags": ["고환율", "고금리", "채권시장", "가계부채", "한국경제", "AI밸류에이션"]
    }
  },
  "DzeGifTlnHY": {
    "primary": "energy",
    "video": {
      "id": "DzeGifTlnHY",
      "title": "한국 항공유 1위, 지속가능항공유가 흔들 수 있을까?",
      "published": "2026-06-03T04:00:00+00:00",
      "channel_name": "안될과학 Unrealscience",
      "url": "https://www.youtube.com/watch?v=DzeGifTlnHY",
      "thumbnail": "https://img.youtube.com/vi/DzeGifTlnHY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "글로벌 항공유 시장 1위인 한국 정유업계가 친환경 규제 강화에 따른 <span class=\"text-cyan-300 font-semibold\">지속가능항공유</span>(<span class=\"text-cyan-300 font-semibold\">SAF</span>) 도입이라는 중대한 전환점에 직면했습니다. 폐식용유나 도시 쓰레기 등을 재활용한 SAF는 기존 엔진 개조 없이 사용 가능하여 탈탄소 규제의 핵심 대안으로 떠오르고 있습니다.",
      "key_claims": [
        "한국 정유사의 저황 항공유는 뛰어난 품질로 미국 서부 수입량의 70%를 차지하는 등 글로벌 리더십을 갖고 있다.",
        "글로벌 <span class=\"text-amber-300 font-bold\">환경 규제</span> 강화로 기존 화석연료 기반 항공유를 지속가능항공유(SAF)로 의무 대체해야 하는 규제가 확대되고 있다.",
        "SAF는 기존 비행기 엔진을 그대로 쓸 수 있는 '드롭인(Drop-in)' 연료로서 글로벌 생산 설비 투자가 급증하고 있다."
      ],
      "data_points": [
        "미국 서부 수입 항공유 중 한국산 비중: 70%",
        "전 세계 SAF 생산 시설 수: 약 323개"
      ],
      "signal": "neutral",
      "signal_reason": "한국 정유사들에 SAF 전환은 단기적으로 규제 대응 비용 부담을 지우는 위기요인이 될 수 있으나, 선제적 설비 투자를 단행할 경우 친환경 고부가가치 시장의 새로운 기회요인이 될 수 있습니다.",
      "key_companies": [
        "SK이노베이션",
        "S-Oil",
        "GS칼텍스",
        "HD현대오일뱅크"
      ],
      "insight": "글로벌 환경 규제가 선박에 이어 항공 업계로 확대되면서 정유 산업의 생존 공식이 '정제 마진 극대화'에서 '친환경 바이오 연료 확보'로 재편되고 있습니다. 독점적 공급망을 가진 한국 정유사들이 SAF 원료 수급 및 대규모 생산 체제를 선제 구축하느냐가 향후 글로벌 항공유 시장 지배력 유지의 열쇠가 될 것입니다.",
      "action_point": "정유사들의 SAF 설비 투자 현황(바이오원료 확보 동향)을 면밀히 모니터링하고, SAF 제조의 핵심 원료인 폐식용유 및 바이오 원료 수거·정제 밸류체인 보유 기업에 선제 투자 기회를 모색해야 합니다."
    },
    "classification": {
      "primary_topic": "energy",
      "secondary_topics": ["tech"],
      "tags": ["지속가능항공유", "SAF", "정유산업", "친환경에너지", "바이오연료", "환경규제"]
    }
  },
  "byIjCCzkgqQ": {
    "primary": "tech",
    "video": {
      "id": "byIjCCzkgqQ",
      "title": "AI 주식 옥석 가리기 시작! HBM 70% 한국 반도체, 걱정 없는 이유 #교양이를부탁해",
      "published": "2026-06-03T11:00:00+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=byIjCCzkgqQ",
      "thumbnail": "https://img.youtube.com/vi/byIjCCzkgqQ/hqdefault.jpg"
    },
    "analysis": {
      "summary": "고금리 환경 장기화로 AI 업계 내 실적 위주의 <span class=\"text-amber-300 font-bold\">옥석 가리기</span>가 본격화되고 있습니다. 하지만 한국 반도체 기업들은 글로벌 <span class=\"text-cyan-300 font-semibold\">HBM</span> 시장 점유율 70% 이상을 차지하고 있어, <span class=\"text-cyan-300 font-semibold\">엔비디아</span>의 실적 성장과 직접 연동되며 상대적으로 탄탄한 방어력을 보여줄 전망입니다.",
      "key_claims": [
        "고금리로 인해 자금 조달 비용이 증가하여 실체 없는 AI 테마주는 조정을 겪는 '실적 장세'로 진입하고 있다.",
        "엔비디아 실적 발표 이후 시장은 하드웨어 인프라에서 실제 수익이 창출되는 2차 수혜 기업들을 구분하기 시작했다.",
        "한국 반도체 업계는 글로벌 HBM 점유율 70% 이상을 확보하여 엔비디아의 독점적 성장 혜택을 온전히 누리고 있다."
      ],
      "data_points": [
        "글로벌 HBM 점유율 (한국): 70% 이상"
      ],
      "signal": "bullish",
      "signal_reason": "실적 없는 테마주들의 옥석 가리기가 일어나는 환경에서도 엔비디아 공급망 핵심인 HBM 독점적 구조 덕분에 한국 대표 반도체 대형주들은 확실한 실적 성장을 보장받고 있습니다.",
      "key_companies": [
        "엔비디아",
        "삼성전자",
        "SK하이닉스"
      ],
      "insight": "고금리라는 매크로 압박 속에서도 AI 인프라 자본 지출(CAPEX)이 가속화되면서 HBM과 같은 핵심 병목 부품의 지배력이 극대화되고 있습니다. '한국 반도체 점유율 70%'는 금리 부담을 상쇄하는 강력한 가격 결정력을 바탕으로 실적 장세에서 주도주 입지를 굳히는 근거가 됩니다.",
      "action_point": "단순 기대감으로 상승했던 소프트웨어 및 AI 중소형주 비중을 조절하고, 엔비디아 밸류체인 내 확실한 매출 증가를 입증하는 HBM 대장주 및 장비 체인에 집중하는 전략이 유효합니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock", "economy"],
      "tags": ["HBM", "엔비디아", "반도체", "옥석가리기", "고금리", "실적장세"]
    }
  },
  "joqrL33AE1k": {
    "primary": "tech",
    "video": {
      "id": "joqrL33AE1k",
      "title": "GPT보다 30배나 싼 딥시크 V4 Pro",
      "published": "2026-06-03T06:00:00+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=joqrL33AE1k",
      "thumbnail": "https://img.youtube.com/vi/joqrL33AE1k/hqdefault.jpg"
    },
    "analysis": {
      "summary": "중국의 AI 모델 스타트업 <span class=\"text-cyan-300 font-semibold\">딥시크</span>(DeepSeek)가 CSA 및 HCA 압축 기억 구조를 도입한 신형 모델 'V4 Pro'를 출시했습니다. 이 모델은 기존 모델(V3.2) 대비 추론당 연산(FLOPs)을 27% 감축하고, <span class=\"text-cyan-300 font-semibold\">KV 캐시</span> 용량을 단 10% 수준으로 대폭 절감하여 고비용 AI 추론 비용을 극적으로 낮추었습니다.",
      "key_claims": [
        "딥시크 V4 Pro는 메모리 압축 효율화 구조를 통해 대용량 콘텍스트 지원 비용을 대폭 낮췄다.",
        "추론 과정의 FLOPs를 27% 줄이고, 필요한 KV 캐시 메모리 공간을 10% 수준으로 극대화했다.",
        "이번 발표는 물리적 메모리 반도체 사용을 줄이는 것이 아니라 알고리즘 차원의 메모리 대역폭 및 연산 최적화 성과다."
      ],
      "data_points": [
        "추론 FLOPs 감축률: 27%",
        "KV 캐시 요구량: 10% 수준으로 감소 (90% 절감)"
      ],
      "signal": "bullish",
      "signal_reason": "중국 딥시크의 지속적인 극초가성비 AI 모델 고도화는 글로벌 AI 기업들의 추론 단가 인하 경쟁을 부추기고 대중적인 AI 에이전트 서비스 보급을 촉진하는 촉매제가 될 것입니다.",
      "key_companies": [
        "딥시크",
        "오픈AI"
      ],
      "insight": "딥시크의 기술 혁신은 단순히 대형 LLM 학습 경쟁을 넘어, 서비스 운영비의 절대다수를 차지하는 '추론 비용(KV 캐시)'을 얼마나 영리하게 다이어트 시킬 수 있는지를 보여줍니다. 이는 고비용 GPU 사용 효율성을 극대화하여 저비용 AI 에이전트 시장 개화 속도를 앞당길 핵심 경쟁력이 될 것입니다.",
      "action_point": "추론 인프라 비용 절감 솔루션(알고리즘 최적화, 경량화 모델) 경쟁이 격화됨에 따라 이를 주도하는 소프트웨어 강자들과 온디바이스 AI 구동 효율성이 뛰어난 NPU 칩 설계 분야의 투자 매력도가 부각될 수 있습니다."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["딥시크", "DeepSeek", "추론비용", "KV캐시", "경량화", "V4Pro"]
    }
  }
}

for vid, info in analyses.items():
    save_analysis(vid, info["primary"], info["video"], info["analysis"], info["classification"])
