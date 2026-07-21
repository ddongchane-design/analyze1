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
    if synthesis_cache.exists():
        synthesis_cache.unlink()
        print(f"Invalidated cache: {synthesis_cache}")

# Batch 5 analyses
batch_5 = {
  "oMrP_-w580U": {
    "primary_topic": "space",
    "secondary_topics": ["tech", "stock"],
    "tags": ["스페이스X", "AST스페이스모바일", "위성인터넷", "나스닥상장", "스타링크", "직접연결"],
    "analysis": {
      "summary": "스페이스X가 시가총액 2조 달러를 돌파하며 상장했으며, 우주와 AI(xAI 그록, 콜로서스 등)를 결합한 거대한 생태계를 구축하고 있습니다. 한편 <span class=\"text-cyan-300 font-semibold\">AST 스페이스모바일(ASTS)</span>은 스마트폰을 위성에 직접 연결하는(Direct-to-Cell) 고유한 틈새 시장을 공략하며 AT&T, 버라이즌 등 통신사 연합의 강력한 지지를 받고 있습니다. 다만 ASTS는 위성 발사 비용 조달에 따른 <span class=\"text-rose-400 font-medium\">지분 희석 리스크</span>가 상존합니다.",
      "key_claims": [
        "스페이스X는 단순 로켓 회사를 넘어 AI(xAI) 및 소셜망(X)을 융합한 2조 달러 규모의 종합 기술 복합 기업으로 도약했다.",
        "AST 스페이스모바일은 일반 스마트폰을 우주 위성에 직접 연결하는 틈새 영역에서 스타링크보다 기술적으로 약 2년 앞선 우위를 보인다.",
        "ASTS는 통신사 공동 플랫폼 구축 등 우호적 환경을 만났으나, 본격적인 이익 창출 전까지 위성 발사를 위한 추가 자금 수급(희석 위험)을 경계해야 한다."
      ],
      "data_points": [
        "스페이스X 나스닥 상장 조달액: 약 857억 달러",
        "스페이스X 시가총액: 2조 달러 돌파",
        "스페이스X 스타링크 통신 부문 매출 비중 (2025): 약 114억 달러 (전체 61% 차지)"
      ],
      "signal": "neutral",
      "signal_confidence": "high",
      "signal_reason": "스페이스X와 ASTS 모두 우주 연결 테마의 핵심 성장주이나, 극단적인 고평가(매출 대비 90배 멀티플)와 본격적 이익 부재에 따른 추가 희석 리스크가 상존하여 방어적 균형 감각이 필요한 구간이기 때문입니다.",
      "key_companies": ["스페이스X", "AST스페이스모바일(ASTS)", "AT&T", "버라이즌"],
      "insight": "우주 산업이 점차 고도화되면서 수직 계열화된 거인(스페이스X)과 전문적인 틈새 레이어(AST 스페이스모바일)로 시장이 분화되고 있습니다. 특히 ASTS는 통신사 가입자를 그대로 흡수하는 구조로 마케팅 비용이 들지 않는 강력한 비즈니스 모델을 가졌으나, 천문학적인 위성 발사 비용 조달에 따른 주주 가치 희석 리스크가 상존하므로, 거품 낀 멀티플을 추격하기보다 냉정한 자금 조달 스케줄과 스타링크의 기술 추격을 검증해야 합니다.",
      "action_point": "스페이스X와 ASTS는 전혀 다른 리스크 프로필을 지닌 자산입니다. AI 시너지를 믿는다면 <span class=\"text-cyan-300 font-semibold\">스페이스X(합병 형태)</span>를, 위성 통신 직접 연결 틈새의 독점을 노린다면 <span class=\"text-cyan-300 font-semibold\">ASTS</span>에 배팅하되, ASTS의 경우 위성 발사 일정에 맞춘 <span class=\"text-rose-400 font-medium\">지분 희석 리스크</span>를 고려해 포트폴리오 비중을 조절해야 합니다."
    }
  },
  "q8K1kbL3T4Y": {
    "primary_topic": "etc",
    "secondary_topics": ["stock"],
    "tags": ["미래에셋증권", "담보대출", "이용가이드", "M-STOCK"],
    "analysis": {
      "summary": "미래에셋증권 모바일 앱 M-STOCK을 통해 보유 주식을 담보로 활용하여 일반 대출 및 매도 대출 약정을 맺는 실무 프로세스 가이드입니다. 약정 과정에서 투자 성향 및 신용공여 정보 확인서를 제출하고, 5천만 원 초과 시에는 인지세가 차등 부과되며 <span class=\"text-amber-300 font-bold\">5천만 원 이하 시 인지세가 면제</span>됩니다. 대출 시 추가 담보 납부(마진콜) 및 만기 안내 등 알림 설정이 가능합니다.",
      "key_claims": [
        "보유 중인 주식을 담보로 대출받는 일반 담보대출과 매도 완료 후 즉시 인출 가능한 매도 담보대출을 모바일 앱에서 간편히 약정할 수 있다.",
        "대출 금액 합산 기준 5천만 원 이하의 소액 대출 건에 대해서는 인지세가 전액 발생하지 않는다.",
        "해외 주식을 담보로 포함할 수 있으나, 담보 비율 하락에 따른 추가 담보 미납 시 반대매매가 진행될 수 있으므로 유의해야 한다."
      ],
      "data_points": [
        "인지세 면제 기준: 대출 약정 총합산 금액 5,000만 원 이하"
      ],
      "signal": "neutral",
      "signal_confidence": "high",
      "signal_reason": "증권사의 신용 담보대출 가이드로서 시장 전반의 호재나 악재 시그널보다는, 투자자 본인의 담보 자금 관리와 레버리지 위험 통제 영역을 다룬 실무적인 내용이기 때문입니다.",
      "key_companies": ["미래에셋증권"],
      "insight": "개인 투자자들이 주식 담보대출 기능을 활용할 때의 복잡한 절차와 인지세 면제 기준(5천만 원 이하)을 설명하는 실무적인 가이드입니다. 증권사 입장에서는 이와 같은 담보대출 서비스 활성화를 통해 안정적인 이자 마진(신용공여 수익)을 추가로 확보하는 비즈니스 구조를 구축하고 있습니다.",
      "action_point": "대출 금액 합산 5천만 원 이하에서 <span class=\"text-amber-300 font-bold\">인지세 면제 혜택</span>을 활용하고, 담보 비율 하락에 따른 추가 담보 납부 통보 등 <span class=\"text-rose-400 font-medium\">반대매매 리스크</span>에 상시 대비하는 약정 통보 서비스를 반드시 신청해야 합니다."
    }
  },
  "qmXbuBN1sOg": {
    "primary_topic": "space",
    "secondary_topics": ["tech"],
    "tags": ["우주공장", "무중력제조", "단백질결정", "항암제키트루다", "지블란광섬유"],
    "analysis": {
      "summary": "우주 정거장의 무중력(마이크로 중력) 환경을 활용해 고순도 의약품 및 정밀 신소재를 생산하는 <span class=\"text-cyan-300 font-semibold\">우주 제조(Space Manufacturing)</span> 기술을 조명합니다. 머크는 중력 영향이 배제된 우주 정거장에서 항암제 키트루다의 단백질 입자를 39마이크로미터로 극도로 고르게 결정화했습니다. 신호 결함이 없는 <span class=\"text-cyan-300 font-semibold\">지블란(ZBLAN) 광섬유</span> 등 중력 제약이 없는 신소재 혁신이 가시화되고 있습니다.",
      "key_claims": [
        "우주 무중력 공간에서는 중력에 의한 대류나 물질 가라앉음이 없어 단백질 결정 등을 지상보다 균일하게 합성할 수 있어 제약 회사들의 러시가 이어지고 있다.",
        "항암제 키트루다 등의 고성능 약품 성분을 무중력에서 결정화할 경우 고른 균일성 덕분에 인체 투여 효율이 비약적으로 향상된다.",
        "이론상 최강의 광섬유 소재인 지블란은 지구 중력 하에서 생기는 미세 균열(결함)을 극복하고 무중력에서 완벽한 신호 전달체로 양산이 가능하다."
      ],
      "data_points": [
        "지상 키트루다 입자 분산: 13~102마이크로미터 (불균일)",
        "우주정거장 키트루다 입자 크기: 39마이크로미터 (고도의 균일 결정 생성)"
      ],
      "signal": "bullish",
      "signal_confidence": "high",
      "signal_reason": "무중력 우주 환경을 이용한 바이오 및 정보통신 신소재 제조 기술이 지상의 물리적 한계를 극복하는 실체적 결과물(어닝서프라이즈 및 성능 개선)로 확인되며 장기 성장 동력으로 입증되었기 때문입니다.",
      "key_companies": ["머크"],
      "insight": "우주 산업이 단순 탐사와 통신을 넘어 고부가가치 의약품 및 정밀 하드웨어를 생산하는 '무중력 제조(Space Manufacturing)' 기지로 확장되고 있습니다. 이는 지상에서 중력의 한계로 불가능했던 초고순도 단백질 결정이나 무결함 광소재의 상업화를 가속화할 것입니다.",
      "action_point": "우주 공간에서의 생산 비용 절감 및 무중력 제조 기술을 선점하는 글로벌 <span class=\"text-cyan-300 font-semibold\">제약사(머크 등)</span>와 <span class=\"text-cyan-300 font-semibold\">초정밀 신소재 개발 기업</span>의 우주 프로젝트 진척도를 주목해야 합니다."
    }
  },
  "sywYGB6JHTo": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["V코스피", "코스피변동성", "마이크론실적", "풋콜레이시오", "레버리지ETF"],
    "analysis": {
      "summary": "코스피의 변동성 지수인 <span class=\"text-rose-400 font-medium\">V코스피</span>가 과거 글로벌 금융위기 수준(89선 부근)에 근접하게 폭증하며 글로벌 시장 대비 유별난 변동성을 보였습니다. 이례적인 것은 주가 폭락이 아니라 반도체 중심의 사상 최대 이익(컨센서스 과열)과 5월 이후 대형 <span class=\"text-rose-400 font-medium\">레버리지 ETF 수급 노이즈</span>가 겹쳐 발생했다는 점입니다. 마이크론 실적 직전 옵션 시장에서는 풋 옵션 비중이 2배 이상 몰리며 하방 공포가 극대화되었습니다.",
      "key_claims": [
        "V코스피가 역대급 변동성을 나타냈으나, 이는 금융위기처럼 펀더멘탈 붕괴가 아닌 레버리지 파생 수급이 부추긴 단기적 바람(노이즈)에 불깝하다.",
        "현재 코스피는 기업 이익 컨센서스가 전례 없는 수치로 폭증하는 이례적인 '이익 과열' 및 펀더멘탈 강세 상태를 보이고 있다.",
        "옵션 시장 내 마이크론의 풋콜 비율(풋옵션이 콜옵션의 2배)이 극대화되면서 실적 발표 직전까지 공포성 눈치싸움 매물이 출하되었다."
      ],
      "data_points": [
        "V코스피 변동성 지수: 금융위기 수준 근접 급증",
        "마이크론 실적 전 옵션 풋콜 비중: 풋옵션 비중이 콜옵션 대비 약 2배 우세"
      ],
      "signal": "neutral",
      "signal_confidence": "medium",
      "signal_reason": "V코스피 수치만 보면 공포 시그널이나, 기업 이익(펀더멘탈) 성장세는 사상 최대 수준을 지속하고 있고 파생상품 발 수급 왜곡이 원인이므로 변동성이 지속되되 추세 붕괴로 이어지지 않기 때문입니다.",
      "key_companies": ["마이크론", "삼성전자", "SK하이닉스"],
      "insight": "역사적으로 변동성 지수의 폭증은 항상 실적 급감과 주가 폭락을 동반했으나, 현재 코스피는 사상 최대의 기업 실적(반도체 중심)을 배경으로 변동성이 치솟는 이례적인 '펀더멘탈 과열' 상태입니다. 레버리지 수급 요인으로 등락 폭이 극대화된 상태이므로 주가의 일시적 등락에 투매하거나 추격하기보다는, 기업 이익의 훼손 여부를 냉정히 체크해야 합니다.",
      "action_point": "수급 노이즈로 빚어진 변동성을 역이용하여 투매에 동참하기보다, <span class=\"text-cyan-300 font-semibold\">반도체 투톱(삼성전자, SK하이닉스)</span>의 <span class=\"text-amber-300 font-bold\">실적 턴어라운드 흐름</span>을 믿고 변동성을 버텨내거나 조정 시 분할 매수 기회로 활용해야 합니다."
    }
  },
  "vxRs-slyCRY": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["반도체", "추격매수금지", "삼성전자", "SK하이닉스", "ADR상장", "수남매"],
    "analysis": {
      "summary": "마이크론 실적 서프라이즈로 인해 삼성전자와 SK하이닉스 등 국내 대표 반도체 기업들이 5~11% 급등하며 강세를 보이고 있습니다. <span class=\"text-cyan-300 font-semibold\">SK하이닉스의 7월 나스닥 ADR 상장</span> 일정 확정 소식이 강력한 외인 수급 촉매제로 작용하고 있습니다. 다만 주도주 쏠림이 극대화되고 있으며 바이오 등 타 섹터로의 순환매는 지체되는 내로우(Narrow) 장세이므로, 섣부른 <span class=\"text-rose-400 font-medium\">추격매수는 절대 금물</span>입니다.",
      "key_claims": [
        "마이크론의 강력한 가이드가 IT 전반의 자신감을 충전하며 삼성전자 및 SK하이닉스가 일제히 상승 양봉을 그렸다.",
        "SK하이닉스가 7월 10일경 나스닥에 ADR을 상장하기로 확정하면서 해외 주식 담보 및 추가 외국인 자금 조달 창구가 열렸다.",
        "시장 전체가 강하게 올라가는 듯 보이나 실상 반도체 대장주 외의 바이오, 중소형주 등은 철저히 소외되는 내로우 장세가 계속되고 있다."
      ],
      "data_points": [
        "SK하이닉스 나스닥 ADR 상장 목표 일정: 2026년 7월 10일경",
        "삼성전자/SK하이닉스 실적 발표일 상승률: 삼성전자 5~6%, SK하이닉스 9~11%대 급등"
      ],
      "signal": "bullish",
      "signal_confidence": "high",
      "signal_reason": "AI 반도체 공급 부족 수혜와 Hynix의 나스닥 ADR 상장이라는 확실한 글로벌 밸류업 모멘텀이 추가 유입되어 주도주의 상승 탄력이 강화되었기 때문입니다.",
      "key_companies": ["삼성전자", "SK하이닉스", "SK스퀘어", "삼성전기"],
      "insight": "글로벌 공급망 병목 해소와 ADR 상장 모멘텀을 지닌 SK하이닉스 등 주도주 위주의 자금 쏠림이 장기화되고 있습니다. 순환매가 넓고 강하게 도는 시장이 아니기 때문에, 낙폭과대라는 이유만으로 바이오나 중소형주를 조급하게 매수하는 것은 소외 기간을 늘릴 뿐입니다.",
      "action_point": "시장의 주인공인 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>와 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>, 그리고 지주사인 <span class=\"text-cyan-300 font-semibold\">SK스퀘어</span>에 포트폴리오를 집중하고, 타 섹터의 섣부른 <span class=\"text-rose-400 font-medium\">추격 매수는 지양</span>해야 합니다."
    }
  }
}

for vid, data in batch_5.items():
    save_and_delete(
        video_id=vid,
        primary_topic=data["primary_topic"],
        secondary_topics=data["secondary_topics"],
        tags=data["tags"],
        analysis_data=data["analysis"]
    )
print("Batch 5 completed!")
