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
  "-ADB_o6C2ig": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["SK하이닉스", "삼성전자", "시총역전", "미국ADR", "코스피상단"],
    "analysis": {
      "summary": "SK하이닉스가 삼성전자 시가총액을 추월하면 <span class=\"text-rose-400 font-medium\">반도체 과열 및 강세장 고점 시그널</span>로 해석될 수 있으나, 현재 순이익 기초 체력은 삼성전자가 여전히 압도적입니다. 하이퍼스케일러들의 투자 정점 우려는 과도하며 반도체 중심의 주도권은 올해 말까지 안정적으로 이어질 전망입니다. SK하이닉스의 미국 <span class=\"text-cyan-300 font-semibold\">ADR 상장</span>은 마이크론 수준의 멀티플(8~9배)로 리레이팅되는 호재이나 순환 참조로 인한 단기 변동성은 유의해야 합니다.",
      "key_claims": [
        "SK하이닉스의 시총 역전은 이익 체력(삼성전자 순이익의 70~75% 수준) 대비 과도한 <span class=\"text-rose-400 font-medium\">반도체 쏠림 과열</span>을 나타내는 지표입니다.",
        "하이퍼스케일러의 투자 회수 우려는 시기상조이며, 매출 대비 투자 증가율 크로스오버는 내년 3분기로 예상되어 반도체 실적 가시성은 굳건합니다.",
        "장단기 금리차 상승은 성장주에 우호적이며 내년 순이익 946조 원 달성 시 코스피 지수는 이론적으로 <span class=\"text-amber-300 font-bold\">11,450포인트 상단</span>까지 도달 가능합니다."
      ],
      "data_points": [
        "SK하이닉스의 순이익 수준: 삼성전자 대비 약 70% ~ 75% 수준",
        "삼성전자 및 SK하이닉스의 코스피 내 시가총액 비중: 약 50% 수준",
        "두 기업의 코스피 전체 순이익 비중: 약 70% ~ 75% 수준",
        "하이퍼스케일러 투자 증가율이 매출 증가율 밑으로 하회하는 정점 전망 시기: 2027년 3분기",
        "내년 코스피 전체 순이익 전망치: 약 946조 원 (과거 평균 PER 9.9배 적용 시 지수 상단 11,450포인트 산출)",
        "현재 SK하이닉스 PER 멀티플: 5배 ~ 6배 수준 (미국 마이크론은 8배 ~ 9배 수준)"
      ],
      "signal": "neutral",
      "signal_reason": "실적과 이익 증가율 측면에서 반도체의 주도권은 굳건하나, 시총 역전 우려와 글로벌 자금 흐름의 단기 변동성이 공존하기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)", "마이크론(MU)", "TSMC"],
      "insight": "반도체 쏠림은 실물 이익 비중(70% 이상)에 기반한 합리적 강세장이며, <span class=\"text-cyan-300 font-semibold\">ADR 상장</span>을 통한 글로벌 멀티플 갭 메우기가 진행 중입니다. 다만 타 업종의 이익 쫓아오기(이익 증가율 18% 수준)가 약해 반도체 외 업종으로의 급격한 순환매는 제한적입니다.",
      "action_point": "삼성전자와 SK하이닉스의 호실적 발표 후 일시적 주가 조정은 비중을 확대하는 <span class=\"text-amber-300 font-bold\">좋은 매수 타이밍</span>으로 활용하고, 무리한 낙수 효과 기대로 비(非)주도주를 추격 매수하는 것은 지양해야 합니다."
    }
  },
  "-LUnTYx_xAA": {
    "primary_topic": "etc",
    "secondary_topics": ["tech"],
    "tags": ["위고비", "마운자로", "GLP-1", "비만치료제", "지방간염"],
    "analysis": {
      "summary": "비만은 의지의 영역이 아닌 만성 염증 질환으로 분류되며, 최근 <span class=\"text-cyan-300 font-semibold\">위고비(GLP-1)</span> 등 혁신 치료제의 도입으로 지방간염 치료와 대규모 체중 감량이 입증되고 있습니다. GLP-1 유사체는 뇌 시상하부에 작용하여 항상성 식욕과 도파민 갈망을 억제하며 혈당 변동폭을 안정시킵니다. 마운자로는 GIP와 GLP-1의 이중 작용을 통해 더 강력한 감량 효과를 보여주며 환자 상태에 따른 정밀 처방이 중요합니다.",
      "key_claims": [
        "비만은 단순한 식사량 문제를 넘어 <span class=\"text-rose-400 font-medium\">지방세포의 염증성 반응</span>과 부종이 수면장애 및 폭식을 유발하는 악순환의 질병입니다.",
        "GLP-1 약물은 부교감 신경과 뇌 시상하부에 다중으로 작용하여 강박적 폭식(음식 소음)을 억제하고 혈당 스파이크를 제어합니다.",
        "치료제 중단 이후에도 체내 GLP-1 분비를 유도하려면 <span class=\"text-amber-300 font-bold\">단백질과 식이섬유 중심 식단</span>을 소장 하부(L-세포)까지 도달하도록 섭취해야 합니다."
      ],
      "data_points": [
        "안될과학 항성 감량 사례: 지방간염 치료 목적 복용으로 체중 약 90kg에서 67kg까지 감소",
        "약물 반감기: 체내 반감기 약 1주일 (지속 주사 시 중첩 효과로 인한 용량 주의 필요)",
        "음식 소음 감소 효과: 약물 복용 시 음식에 대한 강박적 생각(음식 소음)이 약 80% 감소"
      ],
      "signal": "na",
      "signal_reason": "비만 치료제의 생물학적 기전과 건강 영향에 초점을 맞춘 순수 과학/의학 해설 영상으로 직접적인 투자 방향성을 제시하지 않습니다.",
      "key_companies": ["노보노디스크(NVO)", "일라이릴리(LLY)"],
      "insight": "GLP-1 계열 치료제는 단순 미용 목적을 넘어 심근경색 예방 및 <span class=\"text-cyan-300 font-semibold\">혈관 내피 염증 개선</span> 등 대사 질환 인프라의 게임 체인저로 안착하고 있습니다. GIP 복합제인 <span class=\"text-cyan-300 font-semibold\">마운자로</span>의 가세로 제약 바이오 시장 판도 변화가 가속화되고 있습니다.",
      "action_point": "글로벌 비만 치료제 시장의 독점권을 쥐고 있는 <span class=\"text-cyan-300 font-semibold\">노보노디스크</span> 및 <span class=\"text-cyan-300 font-semibold\">일라이릴리</span>의 Capex 및 공급망 확대 수혜주 위주로 장기적 밸류에이션 추이를 모니터링할 필요가 있습니다."
    }
  },
  "08Lrl4ijgS4": {
    "primary_topic": "etc",
    "secondary_topics": ["economy"],
    "tags": ["중국기업", "노동문화", "고속성장", "지속가능성", "세대교체"],
    "analysis": {
      "summary": "중국 기업들이 평균 20대 중후반의 매우 젊은 인력 구조와 극단적인 노동 강도를 바탕으로 고속 성장을 이룩한 비밀을 밝힙니다. 단기적인 속도전과 시장 장악 측면에서는 높은 효율을 보여주었으나, 40대 이후의 경력 단절 및 고령화 리스크로 인해 장기 지속 가능성에 대한 의문이 제기됩니다. 젊은 세대가 겪는 압도적인 업무 스트레스와 생존 압박은 <span class=\"text-rose-400 font-medium\">중국 경제의 또 다른 한계점</span>으로 작용할 수 있습니다.",
      "key_claims": [
        "중국 빅테크 및 제조업 기업들은 직원 평균 연령을 20대로 유지하며 <span class=\"text-violet-300 font-medium\">빠른 의사결정과 실행 속도</span>를 핵심 무기로 삼고 있습니다.",
        "나이가 들면 임원 승진에 실패할 경우 자연스럽게 도태되는 구조로, 고숙련 인재의 숙련도 축적을 저해하는 요인입니다.",
        "주 52시간 제약을 뛰어넘는 과도한 연장 근무와 무한 경쟁 시스템은 단기적인 성과 창출에만 집중하는 딜레마를 내포합니다."
      ],
      "data_points": [
        "조사 대상 중국 기업 직원 평균 나이: 약 25세 ~ 29세 수준"
      ],
      "signal": "neutral",
      "signal_reason": "중국 특유의 고속 성장 공식의 장단점을 다루고 있으며, 단기 성장 탄력성과 장기 시스템 리스크가 상충하는 중립적인 거시 변화이기 때문입니다.",
      "key_companies": [],
      "insight": "중국 기업의 초고속 성장 공식은 대규모 인적 인프라의 <span class=\"text-rose-400 font-medium\">한계 노동 투입</span>에 의존해 왔습니다. 그러나 인구 절벽과 청년 세대의 번아웃이 심화됨에 따라 질적 성장을 위한 조직 문화 혁신 없이는 생태계 붕괴를 맞이할 수 있습니다.",
      "action_point": "중국 내 비즈니스 모델을 가진 기업 투자 시, 극단적인 세대교체와 규제에 따른 인적 자원 이탈 가능성 및 지속 가능 여부를 핵심 평가 요소로 반영해야 합니다."
    }
  },
  "1Q2XkHeNrIk": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["투자의그릇", "멘탈관리", "변동성제어", "자산분배", "삼성전자"],
    "analysis": {
      "summary": "주식 시장의 폭락이나 급락 자체보다 투자자 본인의 <span class=\"text-rose-400 font-medium\">감당 가능한 자산 그릇</span>을 넘는 투자가 계좌를 망가뜨리는 근본 원인입니다. 반도체 쏠림과 극심한 주가 변동성 속에서 감정적 뇌동매매와 패닉셀을 방지하기 위해서는 책임 의식을 가진 훈련이 수반되어야 합니다. 돈의 그릇을 키우는 책임감과 냉정한 분산 투자를 통해 변동성을 이겨내야 장기적인 생존이 가능합니다.",
      "key_claims": [
        "투자금이 본인의 소득과 멘탈 그릇을 초과할 때 변동성(20% 수준)에 의해 연봉급 손실이 발생하면 합리적 판단을 잃고 <span class=\"text-rose-400 font-medium\">뇌동매매와 패닉 매도</span>를 저지릅니다.",
        "성공적인 투자 성과는 권한을 누리는 만큼 리스크와 실패에 대한 <span class=\"text-amber-300 font-bold\">철저한 자기 책임</span>을 받아들이는 훈련에서 출발합니다.",
        "주가 흔들림에 흔들리지 않기 위해 비중 조절과 포트폴리오 다각화 등 변동성을 견딜 수 있는 체계적 관리가 필수적입니다."
      ],
      "data_points": [
        "가정된 하이닉스 조정 폭: 약 20% 변동 발생 시, 1천만 원 투자자는 200만 원, 10억 원 투자자는 2억 원의 심리적 충격 발생"
      ],
      "signal": "neutral",
      "signal_reason": "시장 전체의 방향성보다는 투자자 개인의 심리 통제 및 자산 관리 역량을 다루는 콘텐츠이기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "시장의 단기 변동성은 피할 수 없는 법칙이며, 투자자의 그릇이 준비되지 않은 채로 레버리지나 물타기로 승부를 보려 하면 <span class=\"text-rose-400 font-medium\">계좌 영구 손실</span>로 연결됩니다. 변동성을 견디고 이겨낼 수 있도록 분산 투자와 비중 관리를 내재화해야 합니다.",
      "action_point": "삼성전자, 하이닉스 등 주도주 급등락 시 군중 심리에 휩쓸리지 않도록 본인의 투자 그릇 크기에 맞춰 <span class=\"text-amber-300 font-bold\">포트폴리오 비중을 상시 조절</span>하고, 확실한 현금 흐름 범위 내에서 장기 분할 투자 원칙을 준수해야 합니다."
    }
  },
  "95_M8-DYUA8": {
    "primary_topic": "crypto",
    "secondary_topics": ["economy"],
    "tags": ["스테이블코인", "USDT", "미국국채", "디지털달러", "지니어스법"],
    "analysis": {
      "summary": "지정학적 리스크나 긴급 사태(개엄 등) 발생 시, 은행 등 전통 금융 인프라가 닫힌 상황에서 투자자들은 <span class=\"text-cyan-300 font-semibold\">스테이블 코인(테더 USDT)</span>을 통해 자산을 달러로 신속히 환전 및 대피시키는 행동을 보여주었습니다. 미국은 CBDC 대신 민간 스테이블 코인을 지니어스법(Genius Act) 및 클레리티법(Clarity Act)을 통해 제도권으로 편입시키려 합니다. 이를 통해 글로벌 투자자들이 무의식적으로 <span class=\"text-amber-300 font-bold\">미국 국채를 구매</span>하게 만드는 거대한 디지털 금융 패권 인프라가 작동하고 있습니다.",
      "key_claims": [
        "과거 위기 시에는 실물 금이나 달러 현찰을 모았으나, 디지털 시대에는 24시간 블록체인 거래망을 통해 <span class=\"text-cyan-300 font-semibold\">디지털 피난처인 스테이블 코인</span>으로 자금이 빠르게 도피합니다.",
        "미국은 민간 주도의 스테이블 코인을 미국 금융 질서 안으로 편입하여 준비금 자산의 대부분을 <span class=\"text-cyan-300 font-semibold\">미국 단기 국채</span>로 채우도록 법제화(지니어스법 등)하고 있습니다.",
        "글로벌 사용자들이 스테이블 코인을 구매하고 거래하는 행위 자체가 미국 국채의 수요를 무한히 증가시켜 미국의 국가 부채 부담을 덜어주는 요인으로 작용합니다."
      ],
      "data_points": [
        "스테이블 코인 준비금 연동: 민간 발행 스테이블 코인 준비금의 압도적인 비중이 미국 국채로 운용됨"
      ],
      "signal": "bullish",
      "signal_reason": "디지털 달러(스테이블 코인)의 글로벌 인프라 및 법적 안착이 가속화되면서 미국 단기 국채에 대한 강력한 신규 수요가 구조적으로 확장되고 있기 때문입니다.",
      "key_companies": ["Tether", "Circle"],
      "insight": "미국은 막대한 무역 적자와 국채 발행 문제를 민간 스테이블 코인의 글로벌 보급을 통해 우회적으로 해결하고 있습니다. 스테이블 코인 규제 제정은 디지털 달러의 패권을 공고히 하고 전 세계 자본이 스스로 <span class=\"text-cyan-300 font-semibold\">미국 국채</span>를 매수하게 만드는 지경학적 승부수입니다.",
      "action_point": "스테이블 코인 관련 제도화 법안인 <span class=\"text-cyan-300 font-semibold\">지니어스법과 클레리티법</span>의 의회 통과 흐름을 주시하며, 실물자산 토큰화(RWA) 및 디지털 자산 금융 인프라를 확장하는 선두 금융 기업들에 대한 투자를 긍정적으로 고려해야 합니다."
    }
  },
  "9fRankiszG4": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["약세장진입", "현금비중확대", "금리장기화", "트럼프불확실성", "사이드카"],
    "analysis": {
      "summary": "최근 코스피/코스닥의 동시 매수 사이드카 발동 등 심각한 주가 롤러코스터 장세는 시장 전반의 <span class=\"text-rose-400 font-medium\">유동성 이탈 and 약세장 진입</span>의 전조로 분석됩니다. 글로벌 고금리 장기화의 중력과 트럼프 당선에 따른 정책 불확실성 증대로 인해 단기 낙폭 과대에 따른 기술적 반등에 안주하기 어렵습니다. 불확실성 국면에서는 잃지 않는 투자를 최우선으로 삼아 반등 시 주식 비중을 줄이고 현금을 확보해야 합니다.",
      "key_claims": [
        "특별한 외부 이벤트 없이 유동성 축소만으로 지수가 고점 대비 20~30% 급락한 현 상황은 이미 <span class=\"text-rose-400 font-medium\">약세장의 정의에 부합</span>합니다.",
        "원화 약세가 엔화 동조화가 아닌 달러 강세에 의해 주도되는 국면은 시중 유동성이 달러로 유출되고 있음을 나타내는 경고음입니다.",
        "AI 케펙스(CapEx) 투자 회수 기간 및 ROI(투자회수율)에 대한 빅테크의 노이즈는 주가 변동성을 계속 극대화할 것입니다."
      ],
      "data_points": [
        "녹화 기준일: 2026년 7월 10일 금요일 (코스피/코스닥 매수 사이드카 동시 발동일)",
        "지수 낙폭 수준: 주요 지수 고점 대비 약 20% ~ 30% 수준의 하락 이력 존재"
      ],
      "signal": "bearish",
      "signal_reason": "원화 약세를 동반한 강달러 지속, 고금리 유지 장기화, 주요 기술적 지지선(80일선 등) 붕괴 및 정치적 불확실성이 복합적으로 증시 하방 압력을 키우고 있기 때문입니다.",
      "key_companies": ["삼성전자(005930)", "SK하이닉스(000660)"],
      "insight": "현재 시장은 과열된 상반기 랠리 이후 <span class=\"text-rose-400 font-medium\">글로벌 긴축과 달러 진공흡입</span> 여파로 자금이 메마르고 있는 조정 단계입니다. 단기 낙폭 과대로 인해 세게 오르는 기술적 반등이 나오더라도, 추세 전환이 증명되기 전까지는 보수적 현금 관리가 필수적입니다.",
      "action_point": "매수 사이드카 등 단기 급등 반등 발생 시 추가 추격 매수보다는 기존 보유 주식을 분할 매도하여 <span class=\"text-amber-300 font-bold\">현금 비중을 30~50% 이상으로 확대</span>하는 보수적 방어 전략을 실행해야 합니다."
    }
  },
  "AbBJl3_G_s4": {
    "primary_topic": "economy",
    "secondary_topics": ["crypto"],
    "tags": ["트리핀딜레마", "마이런리포트", "플라자합의", "달러패권", "스테이블코인"],
    "analysis": {
      "summary": "기축통화 발행국인 미국이 겪는 경상수지 적자 누적과 강달러에 따른 수출 경쟁력 약화 및 제조 기반 붕괴의 딜레마(<span class=\"text-amber-300 font-bold\">트리핀 딜레마</span>)를 해설합니다. 트럼프 행정부의 정책적 기반이 되는 마이런 리포트(Miron Report)는 관세와 방위비 증액, 그리고 국채 만기를 초장기체로 전환하는 마라라고 통화 절상 합의(플라자 합의 변형)를 구상해 왔습니다. 하지만 최근 급격하게 확장된 <span class=\"text-cyan-300 font-semibold\">스테이블 코인</span> 인프라가 글로벌 달러 수요를 국채로 중개하며 플라자 합의 없이도 딜레마를 해소할 디지털 대안으로 부각됩니다.",
      "key_claims": [
        "기축통화인 달러는 글로벌 유동성 공급 의무와 미국 경상적자 심화 및 신뢰성 훼손이라는 <span class=\"text-amber-300 font-bold\">구조적 트리핀 딜레마</span>에 갇혀 있습니다.",
        "마이런 리포트는 타국의 무임승차를 방지하기 위해 강제적 관세 장벽과 보유 미 국채 만기 연장 등 극단적인 마라라고 합의를 대안으로 제시했습니다.",
        "민간 스테이블 코인의 글로벌 확산은 전통 국가 간의 억지 협정 없이도 전 세계 리테일 자금이 <span class=\"text-cyan-300 font-semibold\">미국 국채를 구매 및 파킹</span>하게 만드는 신개념 금융 인프라 역할을 수행합니다."
      ],
      "data_points": [
        "마론 리포트(글로벌 통상 시스템 재구조화 가이드): 트럼프 당선 직전 스티브 마이런에 의해 작성되었으며, 타국 무임승차 배격과 미국 내 공장 유치 및 상호 관세를 주장"
      ],
      "signal": "neutral",
      "signal_reason": "달러 기축통화 체제의 구조적 한계와 이를 돌파하기 위한 디지털 달러(스테이블 코인) 지경학적 영향력을 거시적으로 다루고 있기 때문입니다.",
      "key_companies": ["Tether", "Circle"],
      "insight": "미국은 민간 스테이블 코인을 제도권(지니어스/클레리티법)으로 가두면서 달러 유통망을 블록체인 위에 고속도로처럼 깔아두었습니다. 이는 동맹국에 대한 정치적 리스크 없이 <span class=\"text-cyan-300 font-semibold\">미국 국채의 안정적 매수자</span>를 무한 확장하려는 국가적 패권 유지 기전입니다.",
      "action_point": "미국 규제망 안으로 수용되는 <span class=\"text-cyan-300 font-semibold\">디지털 달러 및 RWA(실물자산 토큰화) 밸류체인</span>을 확보한 결제/핀테크 플랫폼 및 블록체인 수혜 기업들을 포트폴리오의 장기 헷지 수단으로 검토해야 합니다."
    }
  }
}

for vid, val in batch_data.items():
    save_and_delete(vid, val["primary_topic"], val["secondary_topics"], val["tags"], val["analysis"])
print("Batch 1 processing completed.")
