import json
from pathlib import Path

analyses = [
    {
        "video": {
            "id": "KdG8DbyyAiw",
            "title": "벤츠, 미국 판매 중단 위기?",
            "published": "2026-08-19T11:00:30+00:00",
            "channel_name": "Softdragon SOD",
            "url": "https://www.youtube.com/watch?v=KdG8DbyyAiw",
            "thumbnail": "https://img.youtube.com/vi/KdG8DbyyAiw/hqdefault.jpg"
        },
        "analysis": {
            "summary": "메르세데스 벤츠(Mercedes-Benz)의 중국계 지분(지리자동차 9.6%, 베이징자동차 약 10%)이 20%에 육박하는 가운데, 미국 하원에서 적대국 지분 15% 초과 기업의 차량 제조 및 판매를 금지하는 <span class=\"text-rose-400 font-medium\">'자동차 현대화 법안'</span>이 발의되어 판매 중단 위기설이 고조되고 있습니다.\n유럽 완성차 업체들이 중국 자본에 깊게 의존하면서 미-중 지정학적 갈등의 직접적인 규제 타깃이 되고 있습니다.\n반면 현대차·기아 등 순수 국내 자본 기반의 글로벌 완성차 기업들은 미국 시장에서 지정학적 반사이익을 얻을 가능성이 커졌습니다.",
            "key_claims": [
                "중국 자본 지분이 15%를 초과하는 완성차 업체의 미국 내 판매를 원천 봉쇄하는 초강력 규제 법안 발의.",
                "벤츠의 중국계 합산 지분이 약 20%에 달해 규제 통과 시 북미 사업에 막대한 타격 불가피."
            ],
            "data_points": [
                "벤츠 주요 중국계 지분율: 지리자동차 9.6% + 베이징자동차 약 10% (합산 약 20%)",
                "미 하원 발의 법안 기준: 중국/러시아 등 적대국 지분 15% 초과 시 제조/판매 금지"
            ],
            "signal": "neutral",
            "signal_reason": "독일 완성차의 대미 수출 리스크는 증대되나 국내 완성차(현대차/기아)에 대한 반사이익 모멘텀이 상존하기 때문임.",
            "key_companies": [
                "메르세데스벤츠",
                "현대자동차(005380)",
                "기아(000270)",
                "지리자동차"
            ],
            "insight": "미국의 대중국 디커플링 정책이 반도체를 넘어 <span class=\"text-cyan-300 font-semibold\">자동차 완성차 지분 구조</span>로 확대되고 있어, 지배구조 리스크가 없는 한국 완성차의 상대적 프리미엄이 부각됩니다.",
            "action_point": "유럽 프리미엄 완성차 비중은 관망하고, 대미 점유율 확대 수혜가 기대되는 현대차 및 기아에 주목할 것."
        },
        "classification": {
            "primary_topic": "etc",
            "secondary_topics": ["stock", "economy"],
            "tags": ["벤츠위기", "자동차현대화법안", "중국자본규제", "현대차기아수혜", "지정학리스크"]
        }
    },
    {
        "video": {
            "id": "LJG-yBkpN_M",
            "title": "AI투자 믿는다? 안 믿는다? | 공강 | #Shorts",
            "published": "2026-08-19T08:30:25+00:00",
            "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=LJG-yBkpN_M",
            "thumbnail": "https://img.youtube.com/vi/LJG-yBkpN_M/hqdefault.jpg"
        },
        "analysis": {
            "summary": "개인 투자자들의 AI 자산 관리 및 투자 알고리즘에 대한 신뢰도와 활용 방식에 대한 다양한 인터뷰를 소개합니다.\n전적인 AI 일임 투자에 대한 경계감과 객관적 데이터 분석 보조 도구로서의 AI 활용 필요성이 공존하고 있습니다.\n투자 판단의 최종 책임은 투자자 본인에게 있으므로 AI를 감정 편향 배제 및 데이터 필터링의 보조 수단으로 활용하는 전략이 추천됩니다.",
            "key_claims": [
                "AI 투자는 인간의 감정 편향을 배제하고 대량의 데이터를 객관적으로 처리하는 강력한 강점을 지님.",
                "완전 자동 일임보다 투자 의사결정을 지원하는 전략적 조력자로서 AI를 활용하는 것이 합리적임."
            ],
            "data_points": [
                "투자자 성향: 자체 분석 신뢰형 vs AI 데이터 기반 보조 수용형"
            ],
            "signal": "na",
            "signal_reason": "AI 투자 도구에 대한 대중 인식 인터뷰 영상으로 투자 시그널에 해당하지 않음.",
            "key_companies": ["미래에셋증권"],
            "insight": "AI 알고리즘은 시장의 변동성을 완전히 제거할 수는 없으나, 인간의 탐욕과 공포에 의한 충동 매매를 방지하는 효과적인 자산 관리 도구가 됩니다.",
            "action_point": "로보어드바이저 및 AI 리밸런싱 기능을 포트폴리오의 보조 수단으로 분산 활용할 것."
        },
        "classification": {
            "primary_topic": "tech",
            "secondary_topics": ["stock", "etc"],
            "tags": ["AI투자", "로보어드바이저", "알고리즘투자", "투자심리", "미래에셋"]
        }
    },
    {
        "video": {
            "id": "mynVdWBBU38",
            "title": "[지식뉴스] \"결국 미 재무부까지 급하게 나섰다\"…국채금리 쇼크에 무너진 반도체, 다시 살아날 반등의 조건들 / 교양이를 부탁해",
            "published": "2026-08-19T12:05:17+00:00",
            "channel_name": "교양이를 부탁해",
            "url": "https://www.youtube.com/watch?v=mynVdWBBU38",
            "thumbnail": "https://img.youtube.com/vi/mynVdWBBU38/hqdefault.jpg"
        },
        "analysis": {
            "summary": "글로벌 장기 국채 금리 급등과 이란 전쟁 장기화 우려로 AI/반도체 섹터의 레버리지 청산이 발생하며 국내 증시가 급락했으나, 미 재무부의 바이백 전격 확대와 유동성 방어막 구축으로 반등의 실마리를 찾고 있습니다.\n아마존 및 네오클라우드(코어위브 등)는 AI 데이터센터 단기 임대 고마진 구조를 통해 <span class=\"text-emerald-400 font-medium\">1~3년 내 CapEx 투자금 회수(ROI)</span>가 가능함을 증명하며 고금리 우려를 상쇄하고 있습니다.\n엔비디아가 월가 6대 금융사(골드만삭스, 블랙록 등)와 손잡고 구축한 5,000억 달러 규모의 GPU 담보 대출 생태계는 오픈AI 등 주요 AI 기업의 자금줄을 터주며 산업 붕괴 위험을 원천 차단하고 있습니다.",
            "key_claims": [
                "미 재무부의 장기 국채 바이백 확대는 금리 상방을 억제하여 AI 기업의 자금 조달 비용을 낮추는 핵심 정책 전환점임.",
                "AI 데이터센터 투자는 3년 내 회수 가능한 고수익 사업 모델을 증명하여 시장의 CapEx 회의론을 불식 중임.",
                "GPU를 기초자산으로 하는 담보부 채권(ABS) 금융 공학 모델이 빅테크와 스타트업의 유동성 방패 역할을 수행함."
            ],
            "data_points": [
                "네오클라우드/아마존 CapEx 회수 기간: 단기 고수익 임대 믹스로 1~3년 내 원금 회수 가능",
                "엔비디아-월가 금융 동맹: 골드만삭스, 블랙록, KKR 등과 5,000억 달러 규모 GPU 담보 대출 및 잔존가치 25% 보증",
                "오픈AI 자금 조달: GPU 담보 기반 약 1,000억 달러 규모 선제 유동성 확보"
            ],
            "signal": "bullish",
            "signal_reason": "미 재무부의 국채 바이백 개입과 엔비디아 중심의 GPU 자산유동화(ABS) 금융 안전판이 확보되어 AI/반도체의 기술적 반등 여건이 조성되었기 때문임.",
            "key_companies": [
                "엔비디아(NVDA)",
                "오픈AI",
                "아마존(AMZN)",
                "삼성전자(005930)",
                "SK하이닉스(000660)",
                "골드만삭스(GS)",
                "블랙록(BLK)"
            ],
            "insight": "AI 버블 붕괴론의 핵심 고리였던 '자금 조달 난항'이 <span class=\"text-cyan-300 font-semibold\">GPU 담보 금융 상품화</span>와 <span class=\"text-rose-400 font-medium\">미 정부의 바이백 개입</span>으로 완벽히 통제권 안에 들어왔습니다.",
            "action_point": "금리 쇼크로 낙폭이 과대했던 삼성전자, SK하이닉스 및 엔비디아 밸류체인을 반등 국면에서 적극 매수 관점으로 대응할 것."
        },
        "classification": {
            "primary_topic": "economy",
            "secondary_topics": ["tech", "stock"],
            "tags": ["국채금리쇼크", "미재무부바이백", "GPU담보대출", "반도체반등조건", "이선엽", "오픈AI자금조달"]
        }
    },
    {
        "video": {
            "id": "nF-9JSMUihU",
            "title": "[3부] 20년간 비슷한 길을 걸어온 빅뱅과 누리호",
            "published": "2026-08-19T11:00:21+00:00",
            "channel_name": "안될과학 Unrealscience",
            "url": "https://www.youtube.com/watch?v=nF-9JSMUihU",
            "thumbnail": "https://img.youtube.com/vi/nF-9JSMUihU/hqdefault.jpg"
        },
        "analysis": {
            "summary": "우주항공청(KASA)과 한국항공우주연구원(KARI)의 관계자가 출연하여 아리랑 위성부터 나로호, 누리호 성공에 이르는 대한민국 20년 우주 개척사와 <span class=\"text-cyan-300 font-semibold\">2030~2032년 달 착륙선 프로젝트</span>를 조명했습니다.\n우주항공청 출범으로 분산되어 있던 연구 개발과 행정 통할, 민간 우주 생태계 지원을 단일 컨트롤 타워 체계로 통합했습니다.\n빅뱅을 최초의 우주항공 홍보대사로 위촉하여 대중적 관심과 우주 과학 인재 유입을 촉진하는 민관 협업 모델을 추진하고 있습니다.",
            "key_claims": [
                "대한민국은 세계 7번째로 자체 발사체와 위성 제작 및 자국 발사 역량을 보유한 우주 강국으로 도약함.",
                "우주항공청(KASA)이 우주 정책 컨트롤 타워 역할을 수행하며 민간 주도의 뉴스페이스(New Space) 시대를 가속화함.",
                "2030년 민관 협력 소형 달 착륙선 및 2032년 달 착륙선 발사 과업을 국가 역량을 결집해 추진 중."
            ],
            "data_points": [
                "아리랑 1호 vs 2호 해상도: 6.6m에서 1.0m로 44배 성능 향상 (빅뱅 도약)",
                "달 탐사 마일스톤: 2030년 민관 소형 달 착륙선 발사 및 2032년 정규 달 착륙선 임무 추진",
                "누리호 4차 발사: 국내 300여 개 우주 민간 기업 참여"
            ],
            "signal": "bullish",
            "signal_reason": "국가 우주항공 컨트롤 타워의 대규모 R&D 예산 집행과 달 착륙선 프로젝트가 가시화되며 우주항공 밸류체인의 구조적 성장이 확정적이기 때문임.",
            "key_companies": [
                "우주항공청(KASA)",
                "한국항공우주연구원(KARI)",
                "한화에어로스페이스(012450)",
                "한국항공우주(047810)",
                "세트렉아이(099320)"
            ],
            "insight": "우주 산업이 국가 주도 연구에서 <span class=\"text-cyan-300 font-semibold\">민간 방산 및 통신·위성 비즈니스</span>로 확장되는 대전환점에 도달했습니다.",
            "action_point": "차세대 발사체 및 달 탐사선 수주 모멘텀을 보유한 한화에어로스페이스, KAI 등 국내 대표 우주항공 방산주를 중장기 보유할 것."
        },
        "classification": {
            "primary_topic": "space",
            "secondary_topics": ["tech", "stock"],
            "tags": ["우주항공청", "KASA", "누리호", "달착륙선", "항공우주연구원", "안될과학", "빅뱅홍보대사"]
        }
    },
    {
        "video": {
            "id": "nxrLHJE5vXU",
            "title": "모더나 암백신 3상 성공 장전 100% 폭등ㅣ美 재무부 장기채 바이백 2배 확대ㅣAI 데이터센터 규제 강화ㅣ코스피 급락에도 원화값 왜 올랐나ㅣ홍혜진의 뉴욕브리핑",
            "published": "2026-08-19T14:28:47+00:00",
            "channel_name": "매경월가월부",
            "url": "https://www.youtube.com/watch?v=nxrLHJE5vXU",
            "thumbnail": "https://img.youtube.com/vi/nxrLHJE5vXU/hqdefault.jpg"
        },
        "analysis": {
            "summary": "모더나(Moderna)가 머크와의 맞춤형 mRNA 암 백신 임상 3상 성공 발표로 장전 주가가 100% 이상 폭등하며 바이오테크 시장의 강력한 주도주로 떠올랐습니다.\n미국 재무부는 장기 국채 금리 급등을 억제하기 위해 국채 바이백 규모를 기존의 2배(최대 40억 달러 이상)로 기습 확대하며 국채 금리를 급락시키고 증시 반등의 불씨를 지폈습니다.\n코스피 급락 속에서도 반도체 수출 호조에 따른 사상 최대 경상수지 흑자와 외환당국 개입으로 원화 환율이 견고한 하방 지지력을 유지했습니다.",
            "key_claims": [
                "모더나-머크의 맞춤형 암 백신 성공은 mRNA 플랫폼의 암 정복 가능성을 입증한 역사적 이정표임.",
                "미 재무부의 장기채 바이백 2배 확대는 채권 시장의 유동성 경색을 해소하는 즉각적 경기 방어 조치임.",
                "환율은 채권 금리차보다 반도체 수출 중심의 경상수지와 외국인 수급에 더 민감하게 반응함."
            ],
            "data_points": [
                "모더나(MRNA) 주가: 개장 전 거래에서 100% 이상 급등 기록",
                "미 재무부 바이백: 10~30년물 장기 국채 대상 매입 한도 2배 확대",
                "국내 외환 시장: 경상수지 흑자 지속으로 원-달러 환율 1,400원대 방어"
            ],
            "signal": "bullish",
            "signal_reason": "미 재무부의 유동성 방어 정책과 바이오 혁신 신약 호재가 결합되어 글로벌 증시의 하방 경직성을 확보했기 때문임.",
            "key_companies": [
                "모더나(MRNA)",
                "머크(MRK)",
                "삼성바이오로직스(207940)",
                "유한양행(000100)",
                "엔비디아(NVDA)"
            ],
            "insight": "빅테크 기술주 조정 국면에서 <span class=\"text-rose-400 font-medium\">바이오 헬스케어</span>가 새로운 주도 섹터로 급부상하고 있으며, 매크로 유동성 개입이 증시 안전판을 제공하고 있습니다.",
            "action_point": "mRNA 및 면역항암제 파이프라인을 보유한 국내외 핵심 바이오주에 대한 신규 분할 매수를 검토할 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["economy", "tech"],
            "tags": ["모더나폭등", "암백신3상", "국채바이백2배", "원달러환율", "홍혜진기자"]
        }
    },
    {
        "video": {
            "id": "p3Xsk7ONGPc",
            "title": "미리 준비하는 중개형ISA 만기",
            "published": "2026-08-19T01:15:06+00:00",
            "channel_name": "Smart Money by MiraeAsset ",
            "url": "https://www.youtube.com/watch?v=p3Xsk7ONGPc",
            "thumbnail": "https://img.youtube.com/vi/p3Xsk7ONGPc/hqdefault.jpg"
        },
        "analysis": {
            "summary": "중개형 ISA 계좌의 의무 가입 기간 만기 도래 시 자금을 현명하게 관리할 수 있는 최적의 세무 및 자산 운용 가이드를 제공합니다.\n비과세 한도를 채운 후 만기일로부터 60일 이내에 연금저축이나 IRP 계좌로 자금을 이전하면 <span class=\"text-emerald-400 font-medium\">이전 금액의 10%(최대 300만 원)를 추가 세액공제</span>받을 수 있습니다.\n자산 증식을 계속 원할 경우 만기를 자유롭게 연장하여 납입 한도(연 2,000만 원, 최대 1억 원)를 유지하며 비과세 복리 혜택을 이어갈 수 있습니다.",
            "key_claims": [
                "ISA 만기 자금을 60일 이내 연금 계좌로 전환 시 최대 300만 원의 파격적인 추가 세액공제 혜택 제공.",
                "장기 투자를 지속하고자 할 때는 해지 대신 만기 연장을 통해 절세 한도를 계속 누릴 수 있음."
            ],
            "data_points": [
                "연금 전환 추가 세액공제: 이전 금액의 10% (최대 300만 원 한도)",
                "신청 기한: ISA 만기일로부터 60일 이내"
            ],
            "signal": "na",
            "signal_reason": "절세 계좌(ISA) 만기 관리 실무 가이드 영상으로 주식 투자 시그널에 해당하지 않음.",
            "key_companies": ["미래에셋증권"],
            "insight": "절세 계좌의 만기 전략을 사전에 수립하여 연금 전환 추가 세액공제를 확보하는 것이 실질 가처분 소득을 극대화하는 팁입니다.",
            "action_point": "ISA 만기 도래 예정자는 60일 이내 연금계좌 전환 신청을 준비하여 연말정산 절세 혜택을 챙길 것."
        },
        "classification": {
            "primary_topic": "stock",
            "secondary_topics": ["etc"],
            "tags": ["중개형ISA만기", "연금전환세액공제", "최대300만원", "절세계좌팁", "미래에셋"]
        }
    }
]

def save_batch(batch_list):
    for item in batch_list:
        vid = item["video"]["id"]
        primary = item["classification"]["primary_topic"]
        target_dir = Path(f"data/analyzed/{primary}")
        target_dir.mkdir(parents=True, exist_ok=True)
        
        target_file = target_dir / f"{vid}.json"
        with open(target_file, "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
        print(f"Saved: {target_file}")
        
        # Remove from pending if exists
        pending_file = Path(f"data/pending/{vid}.json")
        if pending_file.exists():
            pending_file.unlink()
            print(f"Deleted pending: {pending_file}")

save_batch(analyses)
print("Batch 3 completed!")
