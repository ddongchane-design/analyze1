import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.batch_save import save_batch

batch_7 = [
  {
    "video": {
      "id": "nzbzMi9rlNw",
      "title": "[어바웃 뉴욕] \"팔란티어 실적 93% 급등… 미국 상업 매출 폭발\" | 이나연 특파원",
      "published": "2026-08-12T03:15:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=nzbzMi9rlNw",
      "thumbnail": "https://img.youtube.com/vi/nzbzMi9rlNw/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">팔란티어(PLTR)</span>의 분기 매출이 전년 대비 <span class=\"text-amber-300 font-bold\">93% 급등</span>하며 뉴욕증시에서 폭등세를 기록함. 미국 상업 고객 매출이 149% 폭증함에 따라 단순 정부 군수 계약을 넘어 민간 빅테크 기업들의 AI 거버넌스 필수 인프라로 자리 잡았음이 증명됨.",
      "key_claims": [
        "팔란티어의 미국 상업 매출 149% 증가로 민간 AI 소프트웨어 시장 압도.",
        "AIP 온톨로지 플랫폼 확장에 따른 계약 잔고 폭증 및 마진 대폭 상향."
      ],
      "data_points": [
        "팔란티어 분기 매출 성장률: 93% (미국 상업 매출 149% 증가)"
      ],
      "signal": "bullish",
      "signal_reason": "팔란티어의 미국 상업 시장 폭발적 성장과 실질 AI 소프트웨어 매출 증명.",
      "key_companies": ["팔란티어(PLTR)"],
      "insight": "기업들이 AI 모델을 도입할 때 데이터 통제권과 실질 업무 연결(온톨로지)을 선점한 플랫폼 기업이 엔터프라이즈 AI 시장의 최대 수혜자가 됨.",
      "action_point": "팔란티어 및 실적 성장세가 가시화된 AI 테크 솔루션주 보유."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["팔란티어", "PLTR", "상업매출149%", "AIP", "엔터프라이즈AI"]
    }
  },
  {
    "video": {
      "id": "PAO2QR9l7WM",
      "title": "삼전닉스 물렸다면? 한번에 기대말고 단계적 가격 전략 세우자ㅣ홍선애, 박병창 MP파트너스 대표 [여의도 인사이트]",
      "published": "2026-08-12T09:00:37+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=PAO2QR9l7WM",
      "thumbnail": "https://img.youtube.com/vi/PAO2QR9l7WM/hqdefault.jpg"
    },
    "analysis": {
      "summary": "단기 조정을 받은 삼성전자와 SK하이닉스 등 반도체 투톱에 대한 <span class=\"text-amber-300 font-bold\">단계적 분할 분선 매수 전략</span>을 제시함. HBM 및 레거시 DRAM 수급 불균형과 빅테크 CapEx 실적이 공고하므로 매도 신호가 아닌 <span class=\"text-cyan-300 font-semibold\">분할 가격 전략</span>으로 포트폴리오를 조정할 것을 권고함.",
      "key_claims": [
        "반도체 대장주의 구조적 추세 이탈이 아니며 펀더멘탈은 견고함.",
        "한 번에 올인하기보다 분할 매수를 통한 평단가 관리 및 변동성 대응 강조."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "단기 가격 조정 국면에서 펀더멘탈 기반 단계적 모아남기 전략 권고.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "실적이 뒷받침되는 사이클 대장주는 단기 수급 노이즈로 하락할 때 단계적 대응이 손실 위험을 낮추는 최선책임.",
      "action_point": "삼성전자 및 SK하이닉스의 지정 지지선 이하 분할 매수 전략 실행."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["삼성전자", "SK하이닉스", "단계적분할매수", "반도체전략", "박병창"]
    }
  },
  {
    "video": {
      "id": "phJkTgYnGgY",
      "title": "아직은 추세 이탈 아닌 변동성…삼전닉스 매도 신호는 없었다ㅣ명민준, 박가영, 차영주 [주린이 구조대]",
      "published": "2026-08-12T13:30:31+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=phJkTgYnGgY",
      "thumbnail": "https://img.youtube.com/vi/phJkTgYnGgY/hqdefault.jpg"
    },
    "analysis": {
      "summary": "삼성전자와 SK하이닉스의 기술적 차트 및 기관 매매 수급을 정밀 분석하며 <span class=\"text-cyan-300 font-semibold\">추세 훼손 신호가 없음</span>을 확인점함. 외국인 차익 실현과 단기 미수 정리 과정의 변동성일 뿐이며, 영업이익 가시성과 HBM 독점력이 유지되는 한 <span class=\"text-amber-300 font-bold\">상승 사이클</span>은 이어질 것으로 진단함.",
      "key_claims": [
        "삼전·닉스의 52주 고점 후 조정은 추세 이탈이 아닌 단순 수급 조정.",
        "반도체 턴어라운드 및 HBM 수요 가시성이 유지되어 매도 실익 없음."
      ],
      "data_points": [],
      "signal": "bullish",
      "signal_reason": "기술적 및 기본적 분석상 추세 유지가 확인되며 수급 털어내기 후 재반등 기대.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "실적 피크아웃 신호가 없는 대장주의 단기 조정은 개미 털기 구간이며 기술적 지지선 확인이 중요함.",
      "action_point": "패닉 셀을 지양하고 기술적 이평선 지지 확인 후 홀딩 유지."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy"],
      "tags": ["삼전닉스", "추세유지", "반도체차트", "차영주", "매도신호없음"]
    }
  },
  {
    "video": {
      "id": "pJlDZJHhAPk",
      "title": "물가 지표 공개 앞두고 유가 급등...미국증시 약보합 | 데일리 라이브 | 2026.8.11(화)",
      "published": "2026-08-11T11:13:48+00:00",
      "channel_name": "Smart Money by MiraeAsset ",
      "url": "https://www.youtube.com/watch?v=pJlDZJHhAPk",
      "thumbnail": "https://img.youtube.com/vi/pJlDZJHhAPk/hqdefault.jpg"
    },
    "analysis": {
      "summary": "호르무즈 해협 관련 지정학적 봉쇄 노이즈로 <span class=\"text-violet-300 font-medium\">국제 유가가 5% 급등</span>하며 미국 증시가 약보합을 기록함. 한편 인텔(INTEL)이 피지컬 AI 및 목적 기반 칩 증설 자금을 마련하기 위해 <span class=\"text-rose-400 font-medium\">150억 달러 규모 유상증자</span>를 전격 발표하며 반도체 투심에 충격을 줌.",
      "key_claims": [
        "중동 지정학 불안에 따른 유가 급등이 인플레이션 경계감 유발.",
        "인텔의 150억 달러 유상증자 발표로 주주가치 희석 우려 및 기술주 하방 압력."
      ],
      "data_points": [
        "미국 국채 30년물 금리: 5.28% 기록 (2007년 이후 최고)",
        "인텔 유상증자 발표 규모: 150억 달러",
        "WTI 유가 상승률: 5% 내외 급등"
      ],
      "signal": "bearish",
      "signal_reason": "국제 유가 급등 인플레 압력과 인텔의 대규모 유상증자에 따른 기술주 투심 악화.",
      "key_companies": ["인텔(INTC)", "미래에셋증권"],
      "insight": "경쟁력이 악화된 기술 기업의 대규모 유상증자는 주주 가치를 훼손하며 반도체 업종 내 수급 차별화를 심화시킴.",
      "action_point": "유상증자 리스크가 존재하는 2등주 대신 실적 펀더멘탈이 확실한 1등주로 압축."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["economy", "energy"],
      "tags": ["유가급등", "인텔유상증자", "미국증시약보합", "30년물금리", "지정학리스크"]
    }
  },
  {
    "video": {
      "id": "q2i6fylE_Ek",
      "title": "나스닥, CPI 예상치 부합에 상승…코어위브, 네비우스 등 네오클라우드 급등 [월가 뉴스레터]",
      "published": "2026-08-12T22:03:22+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=q2i6fylE_Ek",
      "thumbnail": "https://img.youtube.com/vi/q2i6fylE_Ek/hqdefault.jpg"
    },
    "analysis": {
      "summary": "7월 미국 CPI가 인플레이션 완화를 가리키며 나스닥 지수가 강세 전환함. 특히 클라우드 매출 폭증을 발표한 <span class=\"text-cyan-300 font-semibold\">네비우스</span>와 <span class=\"text-cyan-300 font-semibold\">코어위브</span> 등 <span class=\"text-amber-300 font-bold\">네오클라우드 AI 가속기 호스팅주</span>가 20% 이상 급등하여 기술주 상승을 주도함.",
      "key_claims": [
        "CPI 안도감 속에서 네오클라우드 기업들의 호실적으로 기술주 랠리 가속.",
        "GPU 호스팅 수요 급증으로 AI 데이터센터 밸류체인 전반의 주가 상승."
      ],
      "data_points": [
        "네비우스, 코어위브 등 네오클라우드 주가 상승률: 15~20% 폭등"
      ],
      "signal": "bullish",
      "signal_reason": "인플레 안도감과 AI 호스팅 인프라 수혜로 기술주 랠리 재개.",
      "key_companies": ["네비우스(NBIS)", "코어위브(CoreWeave)", "엔비디아(NVDA)"],
      "insight": "거시 통화 완화 안도감과 실질 AI 호스팅 수주 호조가 결합할 때 AI 테크주의 상승 폭이 극대화됨.",
      "action_point": "미국 AI 클라우드 인프라주 및 고성능 메모리 밸류체인 포트폴리오 유지."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["나스닥상승", "미국CPI", "네비우스", "코어위브", "네오클라우드"]
    }
  },
  {
    "video": {
      "id": "Q73lxPqfzG0",
      "title": "AI '돈줄'까지 연결됐다? 미·일이 엔화 방어에 나선 이유",
      "published": "2026-08-12T11:15:35+00:00",
      "channel_name": "교양이를 부탁해",
      "url": "https://www.youtube.com/watch?v=Q73lxPqfzG0",
      "thumbnail": "https://img.youtube.com/vi/Q73lxPqfzG0/hqdefault.jpg"
    },
    "analysis": {
      "summary": "미국과 일본 재무 당국이 엔화 급락을 방어하기 위해 <span class=\"text-cyan-300 font-semibold\">공동 외환 개입</span>을 단행한 거시 경제적 배경을 다룸. 엔저 청산(Yen Carry Trade Unwind)에 따른 글로벌 유동성 위축이 빅테크들의 <span class=\"text-rose-400 font-medium\">AI CapEx 자금 조달</span>에 영향을 미치는 것을 막기 위해 미 국채 금리 상방 억제 및 외환 방어에 나선 것으로 해석됨.",
      "key_claims": [
        "미-일 연합 외환 시장 개입으로 엔화 하방 방어 및 글로벌 유동성 경색 차단.",
        "미 국채 30년물 금리 상승 억제를 통한 빅테크 AI 자금 조달 비용 완화."
      ],
      "data_points": [
        "미국 30년물 국채 금리: 5.28% 억제 방어선 설정"
      ],
      "signal": "neutral",
      "signal_reason": "외환 및 국채 금리 안정화 조치에도 불구하고 지정학 및 거시 유동성 관망세 지지.",
      "key_companies": ["엔비디아(NVDA)", "마이크로소프트(MSFT)"],
      "insight": "거시 통화 및 외환 정책이 빅테크의 AI 투자 자금 유동성을 보존하는 핵심 가이드라인으로 작용함.",
      "action_point": "미 국채 금리 추이 및 엔/달러 환율 변동성 모니터링."
    },
    "classification": {
      "primary_topic": "economy",
      "secondary_topics": ["stock", "tech"],
      "tags": ["엔화방어", "미일외환개입", "엔캐리트레이드", "AI자금조달", "국채금리"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_7)
    print(f"Processed batch 7: {n} items saved.")
