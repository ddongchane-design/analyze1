import json
from pathlib import Path

def main():
    dest_dir = Path("data/synthesis")
    dest_dir.mkdir(parents=True, exist_ok=True)

    synthesis_data = {
        "robot": {
            "consensus": "bullish",
            "cross_insight": "<span class=\"text-cyan-300 font-semibold\">삼성전자</span>가 RX 부문 R&D 캠퍼스에서 휴머노이드 로봇 시연을 전격 진행하며 엔비디아 주도의 <span class=\"text-amber-300 font-bold\">피지컬 AI(Physical AI)</span> 상용화 경쟁에 가세했습니다. 초소형 모듈형 <span class=\"text-cyan-300 font-semibold\">액추에이터</span>와 실시간 카메라 비전 센싱 기술이 핵심 차별화 요소로 부각되고 있으며, 구인난에 시달리는 건설·산업 현장의 모듈형 로봇과 자율 중장비 도입이 대기업 부품 생태계의 성장을 견인하고 있습니다.",
            "divergence": "범용 휴머노이드의 대량 양산 및 가격 다운에는 시간이 걸릴 것이라는 신중론과, 대기업의 핵심 부품 내재화 및 특정 산업용 틈새 로봇의 빠른 실적 가시성이 투심을 이끌 것이라는 낙관론이 대립합니다.",
            "key_themes": [
                "삼성전자 및 대기업 주도의 휴머노이드 로봇 시연과 피지컬 AI 상용화 가속",
                "핵심 모션 기술인 모듈형 액추에이터 및 정밀 카메라 센서 밸류체인 진입 경쟁",
                "산업 및 건설 현장 구인난 해소를 위한 무인 원격 자율 로봇 솔루션 확산"
            ],
            "watch_list": [
                "삼성전자의 휴머노이드 공식 공개 일정 및 핵심 액추에이터 공급사 공시",
                "엔비디아 피지컬 AI 플랫폼과 국내 로봇 스타트업 간의 기술 협력 프로젝트",
                "유니트리(Unitree) 등 글로벌 휴머노이드 기업들의 상장(IPO) 모멘텀"
            ]
        },
        "economy": {
            "consensus": "neutral",
            "cross_insight": "미국 7월 소비자물가지수(CPI 3.4%, 근원 2.5%)가 시장 예상치에 완벽히 부합하며 <span class=\"text-amber-300 font-bold\">인플레이션 완화 안도감</span>을 선사했으나, 중동 지정학 불안에 따른 유가 변동성이 거시 시장의 관망세를 유지시키고 있습니다. 미·일 재무 당국이 30년물 국채 금리(5.28%) 억제와 엔화 하방 방어를 위해 <span class=\"text-violet-300 font-medium\">공동 외환 개입</span>을 단행하면서, 빅테크의 40조 달러 부채 국면 속 AI CapEx 투자 자금 파이프라인을 보존하려는 움직임이 뚜렷해졌습니다.",
            "divergence": "7월 CPI 부합과 미·일 유동성 방어로 연준의 금리 인하 및 생산성 개선 랠리가 이어질 것이라는 낙관론과, 지정학 유가 상승과 고금리 장기화에 따른 한계 기업의 조달 비용 경색을 경계하는 신중론이 교차합니다.",
            "key_themes": [
                "미국 7월 CPI 부합에 따른 물가 상방 압력 완화와 증시 안도감 형성",
                "미·일 외환 시장 공동 개입 및 미 30년물 국채 금리 억제를 통한 유동성 보존",
                "40조 달러 국가 부채 상쇄를 위한 AI 생산성 혁명론의 재부각"
            ],
            "watch_list": [
                "미 10년물 및 30년물 국채 금리의 5.0%선 안착 여부 및 FOMC 금리 발언",
                "호르무즈 해협 지정학 노이즈와 국제 유가(WTI) 배럴당 80달러선 지지력",
                "미국 중간선거 국면에서의 관세 정책 및 입법 불확실성 전개 추이"
            ]
        },
        "tech": {
            "consensus": "bullish",
            "cross_insight": "생성형 AI 생태계가 단순 알고리즘 모델 개발을 넘어 실질 매출(ROI)을 창출하는 <span class=\"text-cyan-300 font-semibold\">엔터프라이즈 AI 통제권(팔란티어)</span>과 <span class=\"text-cyan-300 font-semibold\">네오클라우드 호스팅(네비우스, 코어위브)</span> 시장으로 급속히 재편되고 있습니다. 애플의 차세대 AFM3 파운데이션 모델이 DRAM 단가 상승에 대응해 <span class=\"text-amber-300 font-bold\">NAND 오프로딩 기술</span>을 도입함에 따라 고용량 낸드 수요가 부각되는 한편, AI 사이버 보안(팔로알토)과 맞춤형 ASIC(마벨) 칩 생태계가 테크 상동력을 이끌고 있습니다.",
            "divergence": "OpenAI 등 대표 AI 스타트업들의 데이터센터 임대료 부담과 자금 경색 리스크를 경고하는 의견과, 팔란티어(93% 성장) 및 네비우스(500% 성장)의 실적 폭발이 증명하듯 기업들의 AI 지출 락인 효과가 굳건하다는 시각이 팽팽합니다.",
            "key_themes": [
                "팔란티어 AIP 등 기업 데이터 및 AI 거버넌스 통제 플랫폼의 폭발적 매출 성장",
                "네비우스·코어위브 등 네오클라우드 AI 가속기 호스팅 기업들의 실적 어닝 서프라이즈",
                "애플 AFM3의 NAND 오프로딩 아키텍처 도입 및 온디바이스 AI 메모리 지형 변화"
            ],
            "watch_list": [
                "팔란티어 및 네오클라우드 호스팅 기업들의 분기 계약 잔고 확충 속도",
                "애플 아이폰 신제품 온디바이스 AI 탑재 및 고용량 NAND 채택 비율",
                "OpenAI 및 Anthropic의 IPO 타임라인과 데이터센터 자금 조달 구조"
            ]
        },
        "stock": {
            "consensus": "bullish",
            "cross_insight": "<span class=\"text-cyan-300 font-semibold\">SK하이닉스(000660)</span>가 코스피 보통주 시가총액 1위에 등극하며 역사적인 반도체 주도주 패러다임 전환이 성사되었으며, 대장주 밸류 부담 완화로 자금이 코스닥 <span class=\"text-cyan-300 font-semibold\">전공정 장비 및 소부장주</span>로 확산되는 순환매 랠리가 지속되고 있습니다. 빅테크들의 CapEx 가이던스 상향과 마이크론·삼성전자 등 메모리 공급사들의 HBM 쏠림으로 인한 범용 DRAM 판가 강세가 국내 반도체 밸류체인의 <span class=\"text-amber-300 font-bold\">실적 피난처</span> 역할을 강화하고 있습니다.",
            "divergence": "코스피 내 반도체 비중 과밀에 따른 단기 수급 조정 가능성과 현금/국채 비중 확보를 조언하는 자산배분론과, 잉여현금흐름(FCF)이 튼튼한 메모리 대장주와 코스닥 소부장 순환매 랠리가 주가를 추가 레벨업시킬 것이라는 낙관론이 갈립니다.",
            "key_themes": [
                "SK하이닉스 시총 1위 역전 및 HBM 독점력 기반 반도체 주도주 장세 안착",
                "코스피 대장주에서 코스닥 전공정 소부장(원익IPS, 유진테크 등)으로의 순환매 확산",
                "미국 빅테크 M7 호실적 가이던스와 메모리 제조업체 FCF 펀더멘탈 우위"
            ],
            "watch_list": [
                "삼성전자의 엔비디아 HBM3E/HBM4 최종 퀄테스트 통과 및 수율 공시",
                "코스닥 전공정/후공정 소부장사들의 분기 수주 잔고 및 영업이익률",
                "미국 빅테크 M7의 3분기 CapEx 집행률 및 반도체 수주 지속성"
            ]
        },
        "space": {
            "consensus": "bullish",
            "cross_insight": "<span class=\"text-cyan-300 font-semibold\">스페이스X(SpaceX)</span>의 상장(IPO) 모멘텀과 목표 시가총액 상승이 테슬라와 민간 우주 경제 밸류체인 전반의 멀티플을 재평가시키고 있습니다. 지상 AI 데이터센터와 <span class=\"text-cyan-300 font-semibold\">스타링크 저궤도 위성망</span>의 결합, 그리고 우주 제조물 대기권 회수를 위한 스타폴(Starfall) 프로젝트가 가시화되는 가운데, 중국 역시 재사용 로켓 '창정 10B'의 <span class=\"text-amber-300 font-bold\">그물 포획(Net Capture) 기술</span>을 시험하며 글로벌 우주 패권 경쟁을 가속화하고 있습니다.",
            "divergence": "스페이스X의 스타링크 현금 흐름 창출과 상장 시너지가 우주 항공 붐을 지속시킬 것이라는 낙관론과, 로켓 회수 기술 난이도 및 상장 초기 주가 변동성 리스크를 주의해야 한다는 신중론이 존재합니다.",
            "key_themes": [
                "스페이스X 상장 모멘텀 및 테슬라 자율주행 AI와 스타링크 위성망 시너지",
                "우주 의약품 및 반도체 소재 '우주 제조(In-Space Manufacturing)' 캡슐 회수 성사",
                "중국 창정 10B 그물 포획 방식 시험에 따른 글로벌 재사용 발사체 기술 다변화"
            ],
            "watch_list": [
                "스페이스X의 공식 IPO 신청 타임라인 및 스타링크 월간 구독자 증가세",
                "스페이스X 스타폴 회수 캡슐의 궤도 재진입 시험 성공 데이터",
                "국내 우주항공 부품/위성 통신 기업들의 글로벌 발사체 공급망 진출 성과"
            ]
        },
        "energy": {
            "consensus": "neutral",
            "cross_insight": "글로벌 AI 데이터센터 증설의 50% 이상이 지역 주민의 소음 민원과 <span class=\"text-rose-400 font-medium\">전력망 인허가 병목</span>으로 지연되면서, 에너지가 AI 생태계의 최우선 제한 요인으로 떠올랐습니다. 차세대 AI 데이터센터 유치를 둘러싸고 독립 전력망을 갖춘 지역으로 수급이 쏠리는 한편, <span class=\"text-cyan-300 font-semibold\">초고압 변압기 및 송배전 기기</span> 숏티지와 <span class=\"text-amber-300 font-bold\">SMR(소형모듈원전)</span> 지원책이 국가 차원의 에너지 안보 자산으로 대두되고 있습니다.",
            "divergence": "전력 쇼티지 및 변압기 부족으로 데이터센터 가동이 지연될 것이라는 병목 경고론과, SMR 및 가상발전소(VPP) 인프라 투자가 가속화되어 에너지 소부장 기업들의 사상 최대 이익이 장기화될 것이라는 낙관론이 대립합니다.",
            "key_themes": [
                "데이터센터 50% 공사 지연과 전력망 인허가/소음 NIMBY 병목 부각",
                "초고압 변압기 리드타임 3~4년 고착화에 따른 송배전 기기 수주 폭증",
                "정부의 7대 미래성장동력 지정에 따른 SMR 및 원자력 R&D 예산 집중"
            ],
            "watch_list": [
                "HD현대일렉트릭 등 국내 전력 송배전 기기사들의 북미 수주잔고 및 마진",
                "미국 주요 주의 데이터센터 독립 전력망 인허가 통과 비율",
                "정부의 SMR 인허가 및 체코 원전 본계약 체결 일정"
            ]
        },
        "crypto": {
            "consensus": "bullish",
            "cross_insight": "비트코인 가격이 온체인 바닥 신호를 확인한 가운데, 블랙록 등 월가 기관 자금의 <span class=\"text-cyan-300 font-semibold\">현물 ETF 지속 유입</span>과 MSTR 등 기업용 트레저리의 대기 매수세가 탄탄한 하방 지지력을 제공하고 있습니다. 스마트 컨트랙트 기반 자동 자산 운용 도구인 <span class=\"text-amber-300 font-bold\">디파이 볼트(Vault)</span>에 실물자산 토큰화(<span class=\"text-cyan-300 font-semibold\">RWA</span>) 자금이 유입되며 크립토 자산이 제도권 자산운용업과 결합되고 있습니다.",
            "divergence": "월가 기관 및 법인 자금 유입으로 비트코인이 글로벌 대체 안전 자산으로 안착할 것이라는 낙관론과, 온체인 레버리지 해킹 및 통화 긴축 기조 장기화 시 단기 박스권 횡보를 경고하는 신중론이 존재합니다.",
            "key_themes": [
                "기관 자금 및 비트코인 현물 ETF의 지속적 순유입을 통한 바닥 확인",
                "디파이 볼트(Vault)와 실물자산 토큰화(RWA)의 결합을 통한 온체인 자산 운용 확대",
                "MicroStrategy 등 대형 기업용 트레저리의 비트코인 락인 효과 강화"
            ],
            "watch_list": [
                "비트코인 현물 ETF 및 이더리움 ETF의 일간 순자금 유입액 변화",
                "월가 대형 사모펀드들의 RWA 온체인 파이프라인(Vault) TVL 증감",
                "MSTR의 추가 주식 발행 및 주당 비트코인 가치(BPS) 상승 추이"
            ]
        },
        "etc": {
            "consensus": "neutral",
            "cross_insight": "경영학적 관점에서 조직의 사상 최대 실패를 파헤친 《실패의 본질》을 통해, 힘센 경쟁자가 존재하는 시장에서 리더십이 <span class=\"text-amber-300 font-bold\">목표의 명확화</span>와 사전 <span class=\"text-rose-400 font-medium\">손절매 라인(플랜 B)</span>을 구축하는 것의 중요성을 강조함. 사회 및 정책적으로는 미국 중간선거를 앞둔 정치적 양극화와 미국 내 식품 안전 유통망(샐러드 기생충 리콜) 노이즈가 기업 브랜드 및 수급 생태계의 주요 변수로 다루어짐.",
            "divergence": "과거 승리의 자만에 빠지지 않고 리스크 시나리오를 선제 수립하는 기업이 살아남을 것이라는 낙관론과, 지정학 및 정치적 불확실성이 지속되어 기업 투자 심리가 위축될 수 있다는 회의론이 존재합니다.",
            "key_themes": [
                "조직 관리 및 리더십에서 1순위 목적 설정과 컨틴전시 플랜(손절 라인) 수립 필수화",
                "미국 중간선거 국면의 양극화 정치 노이즈와 관세/정책 불확실성",
                "식품 안전 리콜 이슈 및 헬시 패스트 캐주얼 외학 업계 공급망 차별화"
            ],
            "watch_list": [
                "기업들의 신규 프로젝트 및 투자 시 손절매 플랜 B 구축 유무",
                "미국 중간선거 관련 여론조사 추이 및 관세 정책 발표",
                "여름철 재난 방재 및 식품 공급망 안전 규제 가이드라인"
            ]
        }
    }

    for topic_id, data in synthesis_data.items():
        file_path = dest_dir / f"{topic_id}.json"
        file_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Generated and updated synthesis: {file_path}")

if __name__ == "__main__":
    main()
