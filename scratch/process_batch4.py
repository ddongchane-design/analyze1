import json
from pathlib import Path

# Define the analyzed data for Batch 4
batch_data = {
  "k5c4auK4OK8": {
    "topic": "tech",
    "content": {
      "video": {
        "id": "k5c4auK4OK8",
        "title": "AI에 뒤쳐져 구글과 손잡았다? 애플 AI의 진짜 목적... 시리가 아니라 운영체제였다 | WWDC26 총정리",
        "published": "2026-06-10T11:00:27+00:00",
        "channel_name": "안될공학 - IT 테크 신기술",
        "url": "https://www.youtube.com/watch?v=k5c4auK4OK8",
        "thumbnail": "https://img.youtube.com/vi/k5c4auK4OK8/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 애플은 WWDC26에서 거대 언어 모델의 자체 성능 경쟁보다는 사용자의 화면과 디바이스 맥락을 완벽히 파악하는 <span class=\"text-cyan-300 font-semibold\">OS 기반 AI 에이전트</span>로서의 차별성을 제시했습니다.\n2. 새로워진 시리(Siri)는 캘린더, 사진, 메시지 등 기기 내 개별 앱들을 유기적으로 넘나들며 실제 작업을 직접 실행해 주는 액션형 비서로 진화했습니다.\n3. 생성형 AI가 대중화될수록 단순히 좋은 모델을 가진 기업보다 사용자 일상의 모든 데이터를 통합 관리하는 <span class=\"text-cyan-300 font-semibold\">운영 체제(OS) 장악 기업</span>의 영향력이 극대화될 전망입니다.",
        "key_claims": [
          "애플의 생성형 AI 전략은 고성능 거대 모델과의 경쟁이 아닌, 사용자가 상시 사용하는 OS 환경에 가장 자연스럽고 밀접하게 스며드는 <span class=\"text-cyan-300 font-semibold\">사용자 인터페이스(UI) 최적화</span>입니다.",
          "시리가 화면 내 텍스트와 이미지 컨텍스트를 파악해 실행해 주는 능력은 기존의 웹 기반 챗봇 서비스들의 한계를 넘어서는 <span class=\"text-cyan-300 font-semibold\">진정한 비서 플랫폼</span>의 시초입니다.",
          "애플은 강력한 하드웨어 잠금(Lock-in)과 개인정보 보호를 무기로 AI가 오프라인에서도 작동하도록 설계해 토큰 비용을 획기적으로 낮추고 있습니다."
        ],
        "data_points": [
          "WWDC26(애플 연례 개발자 회의) 개최 및 새로운 Siri 발표",
          "자체 온디바이스 SLM 모델과 웹 기반 LLM(구글 제미나이 등 파트너십) 연동 체계 구축"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "애플의 OS 통합 온디바이스 AI 비전이 마침내 구체화되어, 기기 교체 수요 자극 및 AI 에이전트 소프트웨어 생태계 활성화를 강력히 주도할 시그널을 보냈습니다.",
        "key_companies": [
          "애플(AAPL)",
          "구글(GOOGL)",
          "마이크로소프트(MSFT)"
        ],
        "insight": "생성형 AI의 킬러 앱은 고차원 모델 자체가 아니라 일상 앱을 구동해 주는 OS 기반 에이전트가 될 것입니다. 애플은 <span class=\"text-cyan-300 font-semibold\">독점적 하드웨어-OS 생태계</span>의 지배력을 활용해 AI 유통 경로를 완벽히 통제하고, 모델 개발사들의 강력한 게이트웨이 역할을 할 것입니다.",
        "action_point": "애플의 온디바이스 AI 하드웨어 요구 스펙 증가에 따른 <span class=\"text-cyan-300 font-semibold\">메모리(DRAM, NAND) 고용량화 부품사</span> 및 초고속 인터커넥트 밸류체인 기업들에 주목해야 합니다."
      },
      "classification": {
        "primary_topic": "tech",
        "relevance_score": 9.7
      }
    }
  },
  "LbYdx__750U": {
    "topic": "stock",
    "content": {
      "video": {
        "id": "LbYdx__750U",
        "title": "투자자들 눈물 흘리는 장세... 그래도 팔지 말라는 이유 | 이권희 위즈웨이브 대표 [글로벌 인터뷰]",
        "published": "2026-06-10T23:30:11+00:00",
        "channel_name": "삼프로TV_3ProTV",
        "url": "https://www.youtube.com/watch?v=LbYdx__750U",
        "thumbnail": "https://img.youtube.com/vi/LbYdx__750U/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 미국 근원 CPI 안도감에도 불구하고 이란-미국 간 지정학적 충돌과 옵션 만기일(네 마녀의 날)에 따른 수급 요인으로 기술주 중심의 <span class=\"text-rose-400 font-medium\">단기 투매 현상</span>이 발생했습니다.\n2. 지정학 갈등의 막바지 협상 과정에서는 원래 일시적이고 극심한 교전(전투)이 유도되므로, 최근의 급락도 장기 펀더멘탈 붕괴가 아닌 단기 심리 발작입니다.\n3. 국내 기업들의 영업이익 증가 전망은 견고하며 단지 스페이스X IPO 증거금 준비 등으로 일시적 수급 공백이 있을 뿐이므로 패닉 셀링은 피해야 합니다.",
        "key_claims": [
          "지정학적 갈등은 휴전 및 종결 국면에 가까워질수록 상대방에게 유리한 조건을 얻어내기 위해 <span class=\"text-amber-300 font-bold\">일시적인 군사적 긴장감</span>을 극대화하는 경향을 보입니다.",
          "네 마녀의 날에 연동된 파생상품 헷지 매물과 스페이스X 상장 대기 수급 쏠림이 겹쳐 반도체 기술주의 <span class=\"text-rose-400 font-medium\">단기 하방 변동성</span>을 심화시키고 있습니다.",
          "미국 빅테크의 AI 설비투자 펀더멘탈과 한국 메모리 반도체 공급 계약 구도는 여전히 견고하므로 수급 이슈에 흔들려 투매하지 말아야 합니다."
        ],
        "data_points": [
          "한국 전쟁 휴전 협상 기간 비교 (1951년 시작하여 2년간의 협상 끝에 1953년 체결됨)",
          "WTI 국제 유가 지정학 긴장 재점화로 배럴당 89달러 이상 돌파"
        ],
        "signal": "bullish",
        "signal_confidence": "medium",
        "signal_reason": "전쟁 우려와 수급 교란으로 주가는 급락했으나, 반도체 및 인프라의 기업 이익 펀더멘탈은 변화가 없어 단기 낙폭 과대 구간의 매수 매력도가 높아지고 있습니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)",
          "스페이스X"
        ],
        "insight": "옵션 만기일의 기계적 헷징과 지정학 뉴스에 기반한 단기 차익 실현은 전형적인 소음(Noise)입니다. 빅테크의 이익 창출 능력이 훼손되지 않았다는 점과 <span class=\"text-cyan-300 font-semibold\">역사적 저평가 밸류에이션</span> 수준은 중장기 재상승 모멘텀을 강력히 뒷받침합니다.",
        "action_point": "심리적 패닉에 의한 손절매를 전면 지양하고, 변동성을 활용하여 <span class=\"text-cyan-300 font-semibold\">실적 가시성이 가장 뚜렷한 반도체 대장주</span> 위주로 포트폴리오를 재편하는 기회로 활용해야 합니다."
      },
      "classification": {
        "primary_topic": "stock",
        "relevance_score": 9.3
      }
    }
  },
  "MYLMEY8eDWc": {
    "topic": "etc",
    "content": {
      "video": {
        "id": "MYLMEY8eDWc",
        "title": "외국인이 한국 올 때 변비약 챙기는 이유",
        "published": "2026-06-10T12:00:26+00:00",
        "channel_name": "언더스탠딩_Understanding",
        "url": "https://www.youtube.com/watch?v=MYLMEY8eDWc",
        "thumbnail": "https://img.youtube.com/vi/MYLMEY8eDWc/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 동남아 지역 유학생 등 외국인들이 한국에 정착한 초기 2~3개월 이내에 변비 증상을 호소하는 경우가 빈번합니다.\n2. 이는 쌀의 품종 차이(찰기가 있는 한국 쌀과 소화가 상대적으로 빨리 되는 동남아 쌀) 및 한국 특유의 식단과 소화 적응력의 한계에 기인합니다.\n3. 식단 변화에 따른 신체 및 소화 기능 변화와 일상의 소소한 적응 관련 에피소드를 가볍게 다룬 토크입니다.",
        "key_claims": [
          "쌀 품종(자스민 라이스 대 자포니카 쌀)의 전분 구조와 소화 속도 차이는 초기 외국 거주민들의 <span class=\"text-amber-300 font-bold\">소화계 스트레스</span>의 주요 원인입니다.",
          "식문화 적응 과정에서 발생하는 신체적 부적응 증상은 의외로 다수 해외 유학생들의 일상적 고충으로 자리 잡고 있습니다."
        ],
        "data_points": [
          "외국인 거주 및 유학 초기 약 2~3개월의 위장관 환경 변화 적응 기간 언급"
        ],
        "signal": "na",
        "signal_confidence": "high",
        "signal_reason": "식단 차이에 따른 생리학적 일상 적응 문제를 다룬 가벼운 생활 정보 및 잡담 영상으로, 기업 분석 및 금융 자산 투자와 무관합니다.",
        "key_companies": [],
        "insight": "식문화 차이가 생리 기능에 미치는 소소한 일상적 에피소드로 참고하며, 식품 원자료 가공 및 글로벌 식단 로컬라이징 영역에 미시적인 상식으로 연관 지을 수 있습니다.",
        "action_point": "순수 흥미 위주 시사 잡담용으로 시청하고, 투자 밸류에이션 분석에서는 배제합니다."
      },
      "classification": {
        "primary_topic": "etc",
        "relevance_score": 3.0
      }
    }
  },
  "o8uSfLejqCQ": {
    "topic": "economy",
    "content": {
      "video": {
        "id": "o8uSfLejqCQ",
        "title": "[빈난새의 개장전요것만-6월10일] 수급지옥 기술주, 다음 지지선은 | 오일머니도 스페이스X | 앤스로픽 Fable | 브로드컴 램리서치 슈마컴 POWI 크래커배럴 넷플릭스 카바",
        "published": "2026-06-10T11:00:15+00:00",
        "channel_name": "한경 글로벌마켓",
        "url": "https://www.youtube.com/watch?v=o8uSfLejqCQ",
        "thumbnail": "https://img.youtube.com/vi/o8uSfLejqCQ/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 미국 야간 선물시장은 인플레이션 지표 대기 속에서 이란과의 군사 대립 및 아파치 헬기 피격 보복 공습으로 기술주 매도가 깊어지며 <span class=\"text-rose-400 font-medium\">동반 하락세</span>를 보였습니다.\n2. WTI 유가는 이란 갈등 영향으로 배럴당 89달러 선으로 상승했고, 변동성지수(VIX)는 20선 턱밑인 19.75까지 급등해 경계 심리를 반영했습니다.\n3. 스페이스X의 사우디 오일머니 유치 등 IPO 청약 초과 수급 상황과 앤스로픽의 새 AI 챗봇 모델 'Fable' 발표 소식 등이 개장 전 이슈로 다뤄졌습니다.",
        "key_claims": [
          "트럼프 행정부의 거친 대이란 트루스 소셜 메시지 및 군사 충돌은 원유 공급망 리스크와 함께 <span class=\"text-rose-400 font-medium\">인플레이션 고착화 경계감</span>을 자극하고 있습니다.",
          "미국 증시는 유가 상승에 따라 기술성장주의 밸류에이션 할인을 선반영하며 단기적인 <span class=\"text-rose-400 font-medium\">수급 지옥 조정</span> 국면에 진입했습니다.",
          "중동 국부 펀드가 스페이스X 지분 인수에 적극적으로 참여하는 등 우주 인프라 섹터로의 막대한 자금 이탈 현상이 진행 중입니다."
        ],
        "data_points": [
          "다우 선물 0.5% 하락, S&P 선물 0.5% 하락, 나스닥 선물 약 1.0% 하락",
          "WTI 국제 유가 전장 대비 1% 상승한 배럴당 89달러 기록 (브렌트유 92달러)",
          "VIX(공포지수) 4% 상승한 19.75 기록 (20선 인접)",
          "스페이스X IPO 기관 청약 금액 규모 네 배 이상 초과 접수 집계"
        ],
        "signal": "bearish",
        "signal_confidence": "medium",
        "signal_reason": "트럼프의 대이란 군사적 강경 대치로 유가가 오르는 가운데, 시장 변동성 지표(VIX)가 급등해 단기 뉴욕 증시 기술주 매도 압력을 지지하고 있습니다.",
        "key_companies": [
          "스페이스X",
          "브로드컴(AVGO)",
          "슈퍼마이크로컴퓨터(SMCI)",
          "넷플릭스(NFLX)"
        ],
        "insight": "최근 나스닥 선물 약세와 WTI 유가 반등은 전쟁 위기가 유발한 <span class=\"text-rose-400 font-medium\">지정학 인플레 리스크</span> 때문입니다. 다만 시장은 실제 대규모 중동 전쟁 가능성은 여전히 낮게 보고 있으므로, 현 단계의 하락은 옵션 만기 및 유상증자 희석 공포가 결합된 과도한 기술적 반응에 가깝습니다.",
        "action_point": "유가 민감 성장주의 레버리지 매수를 통제하고, 유가 급등 수혜를 보는 <span class=\"text-cyan-300 font-semibold\">전통 에너지 대장주(셰일오일 관련)</span> 및 배당 방어 성향이 높은 종목으로 변동성 구간을 헷지해야 합니다."
      },
      "classification": {
        "primary_topic": "economy",
        "relevance_score": 9.4
      }
    }
  },
  "OPEkVhRJysE": {
    "topic": "tech",
    "content": {
      "video": {
        "id": "OPEkVhRJysE",
        "title": "젠슨황 \"폭락하면 매수기회다\"..월가의 논리는 이렇습니다.",
        "published": "2026-06-10T10:00:26+00:00",
        "channel_name": "월텍남",
        "url": "https://www.youtube.com/watch?v=OPEkVhRJysE",
        "thumbnail": "https://img.youtube.com/vi/OPEkVhRJysE/hqdefault.jpg"
      },
      "analysis": {
        "summary": "1. 메모리 반도체 산업은 전통적인 컴퓨터 부품 사이클 산업에서 빅테크 인프라 확장을 견인하는 <span class=\"text-cyan-300 font-semibold\">AI 인프라 필수재</span>로 본질적 체질 개선(Re-rating)이 진행되고 있습니다.\n2. 이러한 재평가를 주도하는 핵심 요인은 수요의 구조적 장기화, 물리적 공급 제약, 그리고 가격 변동성을 차단하는 <span class=\"text-cyan-300 font-semibold\">장기 공급 계약(LTA)</span> 체결입니다.\n3. 월가와 국내 증권사들 모두 메모리 산업의 LTA 기반 안정성을 인지하기 시작하여, 최근의 주가 하락은 리스크가 아닌 강력한 '바이더딥(Buy the dip)' 기회로 지목됩니다.",
        "key_claims": [
          "HBM을 위시한 초고대역폭 메모리의 LTA(Long-Term Agreement) 체결은 반도체 메모리를 과거 원자재 Cyclical 업종에서 <span class=\"text-cyan-300 font-semibold\">구조적 빅테크 성장주</span>로 안착시켰습니다.",
          "메모리 제조 3사의 물리적 양산 한계(다이 페널티 등)가 뚜렷하여 수요 폭증 대비 공급 부족 상황이 장기화될 것입니다.",
          "엔비디아 젠슨 황 CEO의 지지처럼, AI 병목현상을 해결할 핵심이 메모리에 있으므로 반도체 가격의 <span class=\"text-cyan-300 font-semibold\">하방 지지 신뢰성</span>은 매우 견고합니다."
        ],
        "data_points": [
          "글로벌 메모리 반도체 3사 (삼성전자, SK하이닉스, 마이크론) 시장 지배력 집중",
          "HBM 및 차세대 서버용 DDR5 메모리 장기 공급 계약(LTA) 체결 비중 대폭 상승"
        ],
        "signal": "bullish",
        "signal_confidence": "high",
        "signal_reason": "전통적 반도체 사이클 성격을 극복하는 장기 계약(LTA) 도입과 AI 병목 필수재로서의 위상 확립으로, 단기 폭락은 매력적인 장기 투자 기회를 제공합니다.",
        "key_companies": [
          "삼성전자(005930)",
          "SK하이닉스(000660)",
          "마이크론(MU)",
          "엔비디아(NVDA)"
        ],
        "insight": "반도체 LTA(장기공급계약) 체결은 실적의 가시성과 예측 가능성을 대폭 제고하여 투자자들에게 사이클 피크아웃 우려를 종식시키는 <span class=\"text-cyan-300 font-semibold\">재평가 정당성</span>을 제공합니다. 이는 시장 조정 국면에서 대장주들의 밸류에이션 멀티플을 높이는 강력한 지지선이 됩니다.",
        "action_point": "단기 기술적 투매로 메모리 및 HBM 부품 관련주가 동반 하락하는 기회를 적극 포착하여, <span class=\"text-cyan-300 font-semibold\">SK하이닉스 및 글로벌 메모리 패키징 소부장 대장주</span>에 대한 비중 확대를 실행해야 합니다."
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
