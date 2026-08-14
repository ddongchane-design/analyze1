import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.batch_save import save_batch

batch_4 = [
  {
    "video": {
      "id": "g4TcRlCrA-w",
      "title": "[어바웃 뉴욕] 코어위브 시간외 폭등 이유… \"AI 데이터센터 임대 수주 대폭 증가\" | 이나연 특파원",
      "published": "2026-08-11T03:00:00+00:00",
      "channel_name": "매경월가월부",
      "url": "https://www.youtube.com/watch?v=g4TcRlCrA-w",
      "thumbnail": "https://img.youtube.com/vi/g4TcRlCrA-w/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">코어위브(CoreWeave)</span>가 시간외 거래에서 급등함. 빅테크 및 AI 스타트업들의 GPU 가속기 클러스터 임대 수주 장고가 폭발적으로 급증하면서 네오클라우드(NeoCloud)의 <span class=\"text-amber-300 font-bold\">실질 수익성 및 캐시카우</span> 창출력이 증명되었기 때문임.",
      "key_claims": [
        "코어위브의 데이터센터 임대 수주잔고 폭증으로 고성능 AI 인프라 수요 견고함 입증.",
        "엔비디아 특화 호스팅 기업들의 실적 호조가 기술주 투심 전반을 인양."
      ],
      "data_points": [
        "코어위브 시간외 주가 상승률: 15% 이상 폭등 기록"
      ],
      "signal": "bullish",
      "signal_reason": "네오클라우드 호스팅 수주 폭증으로 AI 데이터센터 실적 가시성 대폭 상향.",
      "key_companies": ["코어위브(CoreWeave)", "엔비디아(NVDA)", "네비우스(NBIS)"],
      "insight": "AI 클라우드 임대(NeoCloud) 시장의 고성장은 GPU 서버 및 고성능 메모리 수급의 강력한 실수요를 증명하는 핵심 지표임.",
      "action_point": "코어위브 및 네오클라우드 관련 밸류체인과 엔비디아 서버 공급망 부품사 비중 유지."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["코어위브", "NeoCloud", "AI데이터센터", "GPU클러스터", "임대수주폭증"]
    }
  },
  {
    "video": {
      "id": "GaYvvP7H1bc",
      "title": "(미공개 영상) 젠슨황이 한국에 오는 이유",
      "published": "2026-08-11T09:00:00+00:00",
      "channel_name": "Softdragon SOD",
      "url": "https://www.youtube.com/watch?v=GaYvvP7H1bc",
      "thumbnail": "https://img.youtube.com/vi/GaYvvP7H1bc/hqdefault.jpg"
    },
    "analysis": {
      "summary": "엔비디아 CEO 젠슨 황의 방한 목적과 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>, <span class=\"text-cyan-300 font-semibold\">삼성전자</span>와의 차세대 HBM4 및 맞춤형 파운드리 공정 협력 강화 배경을 다룸. 엔비디아 가속기의 숏티지를 해결하기 위해 한국 메모리 2사와의 <span class=\"text-amber-300 font-bold\">동맹 및 공급량 확보</span>가 최우선 과제로 부상함.",
      "key_claims": [
        "젠슨 황 방한을 통한 HBM4 및 3D 패키징 공급망 협의 가속화.",
        "SK하이닉스와 삼성전자 간의 엔비디아 차세대 AI 칩 공급 주도권 경쟁."
      ],
      "data_points": [
        "엔비디아 차세대 블랙웰/루빈 가속기용 HBM4 물량 협의 진행"
      ],
      "signal": "bullish",
      "signal_reason": "젠슨 황 방한 및 엔비디아와 한국 메모리 2사 간의 차세대 HBM 공급 동맹 공고화.",
      "key_companies": ["엔비디아(NVDA)", "SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "엔비디아의 독주 체제 속에서 HBM4 규격 표준화와 턴키 공급 능력을 지닌 국내 반도체 기업들의 입지는 더욱 굳건해짐.",
      "action_point": "젠슨 황 방한 동선 및 HBM4 수주 계약 관련 공식 공시 추적."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["젠슨황방한", "엔비디아동맹", "HBM4", "SK하이닉스", "삼성전자"]
    }
  },
  {
    "video": {
      "id": "Gsf2oX0U-uo",
      "title": "“저커버그·젠슨 황이 오들오들 떨며 초긴장한 이유” 중국이 AI 전쟁에서 꺼낸 진짜 무기는 기술이 아니었다 [Z1뉴스 - 2부]",
      "published": "2026-08-11T21:00:06+00:00",
      "channel_name": "이효석아카데미",
      "url": "https://www.youtube.com/watch?v=Gsf2oX0U-uo",
      "thumbnail": "https://img.youtube.com/vi/Gsf2oX0U-uo/hqdefault.jpg"
    },
    "analysis": {
      "summary": "메타(Meta) 마크 저커버그가 <span class=\"text-cyan-300 font-semibold\">오픈소스 AI(Llama)</span> 전략의 중요성을 재차 강조한 배경에는 중국의 저비용 모델 호스팅과 디플레이션성 단가 공격이 존재함. 미국의 폐쇄형 프런티어 모델(OpenAI/Anthropic)에 맞서 메타가 오픈소스 진영을 결집하고 유통 주도권을 확보하려는 <span class=\"text-amber-300 font-bold\">AI 주도권 출혈 경쟁</span>을 진단함.",
      "key_claims": [
        "메타의 오픈소스 모델(MusicGlimmer 등) 공개 강화를 통한 생태계 우위 점유.",
        "중국 기업들의 저비용 파인튜닝 모델 무료 공개가 빅테크의 API 단가 하락 유도."
      ],
      "data_points": [
        "저커버그 성명서 내 '오픈소스' 언급 횟수: 총 16회 기록"
      ],
      "signal": "neutral",
      "signal_reason": "오픈소스 대 클로즈드소스 간 주도권 경쟁 격화 및 단가 하락 압력 양존.",
      "key_companies": ["메타(META)", "엔비디아(NVDA)", "OpenAI", "Anthropic"],
      "insight": "AI 알고리즘 모델의 단가 폭락 속에서 단일 모델 제공업체보다 플랫폼 락인(Lock-in) 및 하드웨어 밸류체인을 쥔 주체가 거대 가치를 점유함.",
      "action_point": "빅테크 간 오픈소스 생태계 팽창 속도와 인프라 솔루션 기업 중심 포트폴리오 유지."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock", "economy"],
      "tags": ["저커버그", "메타오픈소스", "AI단가경쟁", "중국AI도전", "Llama"]
    }
  },
  {
    "video": {
      "id": "heIhmgp4ywU",
      "title": "AI 때문에 아이폰 용량 더 커진다? 애플, DRAM 아닌 NAND를 활용한 접근 분석 | AFM3가 바꾸는 스마트폰 메모리 | HBF와 zNAND-O",
      "published": "2026-08-11T10:30:04+00:00",
      "channel_name": "안될공학 - IT 테크 신기술",
      "url": "https://www.youtube.com/watch?v=heIhmgp4ywU",
      "thumbnail": "https://img.youtube.com/vi/heIhmgp4ywU/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">애플(AAPL)</span>이 차세대 파운데이션 모델 AFM3에서 모바일 DRAM 단가 급등을 회피하기 위해 <span class=\"text-cyan-300 font-semibold\">NAND 플래시 오프로딩(Offloading)</span> 오프쇼어링 아키텍처를 전격 도입함. 200억 파라미터 대형 모델을 NAND에 상주시키고 필요 활성 파라미터만 DRAM으로 전송하는 구조로, 고용량 NAND 플래시 수혜가 예상됨.",
      "key_claims": [
        "애플의 AFM3 모델 아키텍처 혁신으로 아이폰 내 대용량 NAND 수요 급증.",
        "LPDDR5X 가격 급등 대응을 위해 NAND 오프로딩 기술 도입으로 모바일 메모리 지형 변화.",
        "중국 CXMT 등 D램 공급망 다변화 타진 및 온디바이스 AI 기기용 낸드 재평가."
      ],
      "data_points": [
        "모바일 LPDDR5X D램 가격 상승률: 전분기 대비 78%~83% 폭등",
        "애플 AFM3 온디바이스 모델 파라미터: 200억 개 (필요시 10억~40억 개 활성화)",
        "CXMT 세계 D램 점유율: 2025년 기준 약 7.7% 기록"
      ],
      "signal": "bullish",
      "signal_reason": "애플의 차세대 온디바이스 AI 아키텍처 변경으로 고용량 낸드 플래시 수요 폭증 기대.",
      "key_companies": ["애플(AAPL)", "SK하이닉스(000660)", "삼성전자(005930)", "CXMT"],
      "insight": "온디바이스 AI의 메모리 병목 극복 과정에서 낸드 플래시의 위상이 데이터 보관을 넘어 실시간 가중치 오프로딩 매개체로 재해석됨.",
      "action_point": "고용량 낸드 플래시 생산 비중이 높은 국내 메모리 제조사 및 낸드 컨트롤러 소부장주 주시."
    },
    "classification": {
      "primary_topic": "tech",
      "secondary_topics": ["stock"],
      "tags": ["애플AFM3", "NAND오프로딩", "온디바이스AI", "아이폰용량", "메모리병목"]
    }
  },
  {
    "video": {
      "id": "HLbCi52epWw",
      "title": "[박신영의 개장전요것만-8월11일] AI 연이은 해킹 사고에 팔로알토 주목 | MS 자체 AI칩에 마벨 수혜",
      "published": "2026-08-11T14:00:55+00:00",
      "channel_name": "한경 글로벌마켓",
      "url": "https://www.youtube.com/watch?v=HLbCi52epWw",
      "thumbnail": "https://img.youtube.com/vi/HLbCi52epWw/hqdefault.jpg"
    },
    "analysis": {
      "summary": "프런티어 AI 모델의 취약점과 보안 젤브레이크(Jailbreak) 해킹 사고가 빈번해짐에 따라 <span class=\"text-cyan-300 font-semibold\">팔로알토 네트워크(PANW)</span> 등 AI 보안 기업들의 주가가 급등함. 동시에 마이크로소프트의 자체 AI 가속기(Maia) 탈엔비디아 내재화로 맞춤형 주문형 반도체(<span class=\"text-cyan-300 font-semibold\">ASIC</span>) 제조사인 마벨 테크놀로지(MRVL)가 수혜주로 부상함.",
      "key_claims": [
        "AI 탈옥 및 보안 사고 증가로 기업들의 AI 프런티어 보안 구축 지출 폭증.",
        "마이크로소프트 자체 AI 칩 증설에 따른 마벨(Marvell)의 ASIC 설계 수주 확대."
      ],
      "data_points": [
        "팔로알토 네트워크 주가 상승세 및 AI 사이버 보안 수주 호조"
      ],
      "signal": "bullish",
      "signal_reason": "AI 보안 필수화 및 빅테크 자체 ASIC AI 칩 생태계 확장 모멘텀.",
      "key_companies": ["팔로알토 네트워크(PANW)", "마이크로소프트(MSFT)", "마벨 테크놀로지(MRVL)"],
      "insight": "AI 인프라 확장의 차세대 축은 AI 모델의 탈옥 방지 및 보안 거버넌스와 칩 내재화를 위한 맞춤형 ASIC 생태계임.",
      "action_point": "AI 보안 수혜주(PANW) 및 빅테크 자체 칩 파트너사(MRVL) 비중 확대."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech"],
      "tags": ["팔로알토", "AI보안", "마벨테크놀로지", "ASIC", "자체AI칩"]
    }
  },
  {
    "video": {
      "id": "iGVJJuQt77Y",
      "title": "시가총액 1위 SK하이닉스의 의미 | 삼프로TV 오늘 주식",
      "published": "2026-08-11T11:00:00+00:00",
      "channel_name": "삼프로TV_3ProTV",
      "url": "https://www.youtube.com/watch?v=iGVJJuQt77Y",
      "thumbnail": "https://img.youtube.com/vi/iGVJJuQt77Y/hqdefault.jpg"
    },
    "analysis": {
      "summary": "<span class=\"text-cyan-300 font-semibold\">SK하이닉스(000660)</span>가 코스피 보통주 시가총액 1위로 역전 등극하는 역사적 장세가 전개됨. HBM 시장 독점력과 압도적 영업이익률이 만든 거대한 <span class=\"text-amber-300 font-bold\">반도체 주도권 재편</span>이며, 자금이 코스닥의 저평가된 전공정 장비주로 확산되는 대세 상승장의 신호탄으로 평가됨.",
      "key_claims": [
        "SK하이닉스의 시가총액 보통주 1위 등극으로 국내 반도체 패러다임 재편 증명.",
        "HBM 독점력에 따른 실적 가시성이 코스닥 전공정 소부장으로의 순환매 자극."
      ],
      "data_points": [
        "SK하이닉스 코스피 시가총액 보통주 기준 1위 등극",
        "반도체 업종이 코스피 전체 시가총액에서 차지하는 비중: 약 57%"
      ],
      "signal": "bullish",
      "signal_reason": "SK하이닉스의 역사적 시총 1위 등극과 반도체 밸류체인 실적 장세 선도.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "단순 종합가전/메모리 레거시 중심 기업보다 세계 최고 성능의 HBM 첨단 패키징 기술을 독점한 기업이 시장의 1등 가치를 점유함.",
      "action_point": "SK하이닉스 핵심 밸류체인 소부장주 및 HBM 연관 후공정/전공정주 중심 포트폴리오 유지."
    },
    "classification": {
      "primary_topic": "stock",
      "secondary_topics": ["tech", "economy"],
      "tags": ["SK하이닉스", "시총1위", "HBM독점", "반도체주도주", "코스피재편"]
    }
  }
]

if __name__ == "__main__":
    n = save_batch(batch_4)
    print(f"Processed batch 4: {n} items saved.")
