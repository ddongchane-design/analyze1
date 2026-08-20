import json
import os
from pathlib import Path

batch1 = [
    {
        "video": {
            "id": "-4hOsrJbflA",
            "title": "[일본경제상황] \"하이닉스, 키옥시아 목숨줄 잡고 있다\"...40년 만에 다시 '금융대국'으로 부활한 일본, 시가총액 순위에 숨겨진 비밀 / 교양이를 부탁해",
            "published": "2026-08-02T13:00:08+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=-4hOsrJbflA",
            "thumbnail": "https://img.youtube.com/vi/-4hOsrJbflA/hqdefault.jpg"
        },
        "analysis": {
            "summary": "일본 주식시장의 총가치가 급증하며 40년 만에 <span class=\"text-amber-300 font-bold\">금융대국</span>으로 재부상하는 과정에서, 메모리 반도체 기업 키옥시아(Kioxia)와 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>의 지분 연관성 및 사업 협력이 핵심 변수로 부각됨. 엔화 약세 기반의 외국인 자금 유입과 일본 상장사들의 주주환원 확대가 도쿄 증시 상승을 견인하고 있으나, 낸드 파운드리 시장 경쟁 심화로 인한 지배구조 재편 압력이 커지고 있음.",
            "key_claims": [
                "<span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>가 펀드를 통해 키옥시아 지분을 우회 보유하고 있어 키옥시아의 상장 및 경영 향방에 결정적 영향을 미침.",
                "일본 증시의 부활은 디플레이션 탈출과 기업 지배구조 개선(주주환원 강요)이 맞물린 결과임."
            ],
            "data_points": [
                "일본 상장사 도쿄 증시 시가총액: 약 5,500조 달러/엔 규모 기록",
                "키옥시아 지분 구조 내 SK하이닉스 간접 지율: 약 15% 수준"
            ],
            "signal": "bullish",
            "signal_reason": "일본 자본시장의 재평가와 글로벌 낸드 플래시 공급망 조정을 통한 한국 메모리 반도체 기업들의 지배력 제고 기대감이 큼.",
            "key_companies": ["SK하이닉스(000660)", "키옥시아", "소프트뱅크"],
            "insight": "일본 도쿄 증시의 재평가는 단순한 엔저 효과를 넘어 기업 지배구조 혁신과 반도체 공급망 재편(키옥시아-SK하이닉스 연동)이 이끄는 구조적 변화임.",
            "action_point": "키옥시아 상장 추진 경과에 따른 낸드 수급 변화 및 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>의 지분가치 재평가 모멘텀에 주목할 필요가 있음."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy", "tech"],
            "tags": ["SK하이닉스", "키옥시아", "일본증시", "금융대국", "낸드플래시"]
        }
    },
    {
        "video": {
            "id": "-DJwaPYOCdw",
            "title": "이란은 때릴수록 더 강해집니다 (※2026년 7월 27일 방송입니다)",
            "published": "2026-07-27T00:00:00+00:00",
            "channel_name": "언더스탠딩_Understanding",
            "url": "https://www.youtube.com/watch?v=-DJwaPYOCdw",
            "thumbnail": "https://img.youtube.com/vi/-DJwaPYOCdw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "중동 지정학적 충돌 상황에서 <span class=\"text-violet-300 font-medium\">이란에 대한 외부 압박</span>과 군사적 제재가 오히려 이란 내부의 정권 결속력과 대항력을 강화하는 역설을 설명함. 미국 및 서방 국가들의 제재 장기화가 원유 공급망 및 국제 유가 변동성에 지속적인 잠재 리스크로 작용하고 있음.",
            "key_claims": [
                "외부 군사적·경제적 타격이 이란 내부의 정치적 통제력 강화를 초래함.",
                "중동 정세 안정을 위한 외교적 협상(JCPOA 등)의 재가동 가능성이 불확실함."
            ],
            "data_points": [
                "2015년 JCPOA 합의 및 2026년 현재 재제재 국면 비판"
            ],
            "signal": "neutral",
            "signal_reason": "지정학적 리스크 장기화가 유가 하단을 지지하나, 즉각적인 전면전 확대 가능성은 제한적임.",
            "key_companies": [],
            "insight": "중동 제재는 단순한 원유 차단을 넘어 지정학적 블록화 및 에너지 가격의 상방 위험을 상시 유지시키는 구조적 원인임.",
            "action_point": "국제 유가 변동성과 에너지 관련 종목의 지정학적 헤지 역할을 주시할 필요가 있음."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["energy"],
            "tags": ["이란", "지정학리스크", "중동정세", "국제유가"]
        }
    },
    {
        "video": {
            "id": "1M0yerS-NNI",
            "title": "강남 대장 아파트 값이라는 엔비디아 신제품 ㄷㄷ",
            "published": "2026-08-02T11:00:13+00:00",
            "channel_name": "Softdragon SOD",
            "url": "https://www.youtube.com/watch?v=1M0yerS-NNI",
            "thumbnail": "https://img.youtube.com/vi/1M0yerS-NNI/hqdefault.jpg"
        },
        "analysis": {
            "summary": "<span class=\"text-cyan-300 font-semibold\">엔비디아</span>의 최신 차세대 AI 가속기 Rack(NVL72 / NVL144 등) 신제품 단가가 강남 아파트 가격에 육박하는 초고가 랙 수준으로 형성되어 있음을 조명함. 수냉식 냉각 시스템과 전력 소비 효율이 AI 데이터센터 구축의 핵심 경쟁력으로 떠오르고 있음.",
            "key_claims": [
                "엔비디아의 초고가 랙 스케일 AI 가속기는 개별 칩 단가를 넘어 랙 단위 시스템 파워로 과금됨.",
                "대규모 AI 팩토리 구축을 위해서는 수냉식 쿨링 및 전력 인프라 확충이 필수적임."
            ],
            "data_points": [
                "엔비디아 NVL72/144 랙 스케일 가격: 시스템 랙당 200만~300만 달러(한화 약 30억~40억 원) 육박",
                "소비 전력 요구치: 랙당 600kW~1000kW 수준"
            ],
            "signal": "bullish",
            "signal_reason": "AI 하드웨어의 초고가 단가 유지와 초고성능 랙 스케일 시스템 수요가 하이퍼스케일러 투자 유인을 지속시키고 있음.",
            "key_companies": ["엔비디아(NVDA)"],
            "insight": "AI 반도체는 개별 GPU 칩 판매에서 랙 스케일 수냉 솔루션 전체를 아우르는 초고가 'AI 팩토리' 시스템 사업으로 전환함.",
            "action_point": "엔비디아 NVL 랙 스케일 출하량 증가에 따른 수냉 쿨링 장비 및 초고용량 메모리 공급망을 점검해야 함."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock"],
            "tags": ["엔비디아", "NVL72", "AI팩토리", "수냉식쿨링", "B200"]
        }
    },
    {
        "video": {
            "id": "1Tak5t_eHT4",
            "title": "롯데타워도 작아 보인다?! 세계 최고층 빌딩의 진짜 순위",
            "published": "2026-08-01T11:00:31+00:00",
            "channel_name": "안될과학 Unrealscience",
            "url": "https://www.youtube.com/watch?v=1Tak5t_eHT4",
            "thumbnail": "https://img.youtube.com/vi/1Tak5t_eHT4/hqdefault.jpg"
        },
        "analysis": {
            "summary": "세계 최고층 빌딩들의 높이 측정 기준과 공학적 덤프 기술(첨탑 vs 거주가능 층) 및 지진·강풍을 견디는 최첨단 <span class=\"text-cyan-300 font-semibold\">초고층 건축 공학</span>을 해설함. 롯데월드타워, 부르즈 할리파, 제다 타워 등 세계적 마천루들의 공학적 설계 특성을 비교 분석함.",
            "key_claims": [
                "빌딩의 순위는 안테나/첨탑 포함 여부와 실제 사용 가능 층고에 따라 다르게 산정됨.",
                "바람 하중을 줄이기 위한 유선형 외관 디자인과 질량 감쇄 장치(Tuned Mass Damper)가 필수적임."
            ],
            "data_points": [
                "부르즈 할리파 높이: 828m",
                "롯데월드타워 높이: 555m (세계 6위 수준)"
            ],
            "signal": "na",
            "signal_reason": "순수 과학 및 초고층 건축 공학 지식을 전달하는 교양 교양 콘텐츠임.",
            "key_companies": ["삼성물산"],
            "insight": "초고층 마천루는 국가적 랜드마크이자 풍하중 제어와 신소재 콘크리트 공법 등 최고 난도 토목 공학의 집약체임.",
            "action_point": "초고층 건축 공학 관련 기술력을 보유한 글로벌 건설 엔지니어링 기업들의 기술 모멘텀을 상식 수준에서 파악할 수 있음."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["초고층빌딩", "부르즈할리파", "롯데월드타워", "건축공학"]
        }
    },
    {
        "video": {
            "id": "2GLiNyGcl7c",
            "title": "게을러서 살찌는 게 아니다? 전문가가 지목한 뜻밖의 범인 #교양이를부탁해 #비만 #다이어트 #체중감량",
            "published": "2026-08-02T11:00:20+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=2GLiNyGcl7c",
            "thumbnail": "https://img.youtube.com/vi/2GLiNyGcl7c/hqdefault.jpg"
        },
        "analysis": {
            "summary": "비만이 단순한 의지력 부족이나 게으름이 아니라, 현대인의 <span class=\"text-amber-300 font-bold\">대사 불균형</span>과 자율신경계 및 호르몬 조절 장애에서 비롯되는 건강 질환임을 밝힘. 초가공식품 섭취 축소와 호르몬 반응 개선 중심의 대사 건강 관리가 필수적임.",
            "key_claims": [
                "체중 증가의 주요 원인은 칼로리 과다 섭취 자체보다 인슐린 및 식욕 조절 호르몬 이상임.",
                "의지력에 의존한 극단적 섭취 제한은 요요 현상을 유발할 위험이 큼."
            ],
            "data_points": [],
            "signal": "na",
            "signal_reason": "건강 및 의학 숏폼 지식 콘텐츠로 직접적인 주식 투자와 무관함.",
            "key_companies": [],
            "insight": "비만 치료 패러다임이 의지력 조절에서 호르몬 치료 및 대사 기능 정상화(GLP-1 등)로 전환되는 사회적 현상과 일치함.",
            "action_point": "비만 관련 바이오/제약 대사 치료제 시장의 사회적 관심도를 가늠할 수 있음."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": [],
            "tags": ["비만", "대사질환", "인슐린", "건강관리"]
        }
    },
    {
        "video": {
            "id": "5NZ0BgpeenY",
            "title": "7월 반도체 폭락과 급등의 숨겨진 비밀",
            "published": "2026-08-01T05:22:47+00:00",
            "channel_name": "이효석아카데미",
            "url": "https://www.youtube.com/watch?v=5NZ0BgpeenY",
            "thumbnail": "https://img.youtube.com/vi/5NZ0BgpeenY/hqdefault.jpg"
        },
        "analysis": {
            "summary": "7월 진행된 글로벌 <span class=\"text-cyan-300 font-semibold\">반도체 주가 변동성</span>(급락 후 반등)의 근본 원인을 하이퍼스케일러의 CapEx 이익 회수 우려, 분기말 리밸런싱 수급, 그리고 메모리 가격(ASP) 구조를 통해 정밀하게 파헤침. 단기 변동성에도 불구하고 AI 가속기용 <span class=\"text-cyan-300 font-semibold\">HBM</span> 수요 극대화와 공급 제약으로 인해 한국 메모리 기업들의 실적 우상향 기조는 유효함을 역설함.",
            "key_claims": [
                "7월 반도체 급락은 펀더멘털 훼손이 아닌 분기말 수급 청산 및 차익 실현 기회였음.",
                "HBM3E 공급 둔화 우려는 헛소문이며 SK하이닉스와 삼성전자의 이익 체력은 사상 최고 수준임.",
                "변동성 장세에서는 단순 센티먼트보다 실제 이익 수정치(EPS 상향)를 추적해야 함."
            ],
            "data_points": [
                "2026년 7월 코스피 반도체 변동폭: 고점 대비 10% 내외 조정 후 반등",
                "HBM3E 공급 가격 및 이익률: 역사적 고점 경신 중"
            ],
            "signal": "bullish",
            "signal_reason": "AI 반도체 펀더멘털(HBM 공급 부족 및 실적 상향)이 견고하며 주가 조정을 매수 기회로 활용할 수 있는 구간임.",
            "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)", "엔비디아(NVDA)", "마이크론(MU)"],
            "insight": "반도체 주가의 7월 조정은 수급 쏠림과 리밸런싱에 의한 일시적 소용돌이였으며, 이익 추정치가 지속 상향되는 한 반도체 주도주 장세는 멈추지 않음.",
            "action_point": "주가 조정 시 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span> 및 <span class=\"text-cyan-300 font-semibold\">삼성전자</span> 등 메모리 핵심 대장주에 대한 분할 매수 전략이 유효함."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["tech", "economy"],
            "tags": ["반도체폭락", "HBM", "SK하이닉스", "삼성전자", "이효석"]
        }
    }
]

def save_batch(batch):
    for item in batch:
        primary = item["classification"]["primary_topic"]
        vid = item["video"]["id"]
        out_dir = Path(f"data/analyzed/{primary}")
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{vid}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
        print(f"[저장 완료] {out_file}")
        
        pending_file = Path(f"data/pending/{vid}.json")
        if pending_file.exists():
            pending_file.unlink()
            print(f"[삭제 완료] {pending_file}")

if __name__ == "__main__":
    save_batch(batch1)
