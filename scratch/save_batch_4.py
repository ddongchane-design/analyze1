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

# Batch 4 analyses
batch_4 = {
  "_alQSdz53YQ": {
    "primary_topic": "crypto",
    "secondary_topics": ["economy", "tech"],
    "tags": ["이더리움", "이드랩스", "비탈릭부테린", "재단공백", "가치환원", "파이널리티"],
    "analysis": {
      "summary": "이더리움 가격 하락과 재단 공백 논란을 해결하기 위해, 비트마인과 샤프링크 등 주요 지분 보유자들이 공동 펀딩을 통해 가치 환원 응용 조직인 <span class=\"text-cyan-300 font-semibold\">이드랩스(EthLabs)</span>를 설립했습니다. 이더리움 재단이 보안과 순수 기술 연구를 맡는 한편, 이드랩스는 가격 상승과 직접 연결되는 상업적 응용 및 <span class=\"text-amber-300 font-bold\">가치 환원 구조 개선</span>을 집중 지원할 것입니다. L2 활성화로 위축되었던 이더리움 메인넷의 정산 역할 강화와 <span class=\"text-cyan-300 font-semibold\">파이널리티(Finality) 개선</span>이 핵심 과제입니다.",
      "key_claims": [
        "이더리움 재단의 상업성 및 가치 부양 노력 부족에 대한 비판 속에서, 이해관계자들의 자생적 기부로 이드랩스가 빠르게 출범했다.",
        "이드랩스는 이더리움 메인넷으로의 수수료 환원율을 높이고 파이널리티 속도를 크게 단축하는 등 사용성과 가치 극대화를 직접 주도한다.",
        "비탈릭 부테린의 탈중앙화 순수주의와 배치되지 않는 이원화된 분화(대학의 순수과학 vs 응용과학)를 통해 이더리움의 회복 탄력성을 확인했다."
      ],
      "data_points": [
        "이더리움 주요 지분 소유자: 비트마인 및 샤프링크 등 (0.16%~17% 소유 및 1~4% 기부)",
        "이더리움 노드 개수: 현재 약 20,000개 내외"
      ],
      "signal": "bullish",
      "signal_confidence": "medium",
      "signal_reason": "이더리움의 실질적 가치 부양 및 상업적 문제를 전담하는 이드랩스의 출범으로, L2 쏠림에 따른 메인넷 가치 훼손 우려가 극복되고 3분기 대규모 업데이트와 맞물려 강한 반등 시그널로 작용하기 때문입니다.",
      "key_companies": ["이드랩스(EthLabs)", "코인베이스", "비트마인", "샤프링크", "유니스왑"],
      "insight": "그동안 이더리움 생태계는 과도한 탈중앙성과 순수주의 철학에 매몰되어 가격 부양에 소홀하다는 비판을 받았습니다. 그러나 이드랩스라는 상업용 독립 개발 조직이 등장함으로써, 플랫폼 거버넌스의 분열이 아닌 효율적인 역할 분담(L1 개발 고도화 및 최종 정산 기능 강화)을 꾀할 수 있게 되었으며, 이는 제도권 기관 자금의 유입 신뢰도를 한층 높여줄 것입니다.",
      "action_point": "단기 가격 조정에 흔들리지 말고, 3분기 이더리움 <span class=\"text-cyan-300 font-semibold\">메이저 업그레이드</span>와 <span class=\"text-cyan-300 font-semibold\">이드랩스</span>의 상업성 개선 시그널을 관찰하며 포트폴리오 내 이더리움 비중을 분할 매집하는 전략이 유효합니다."
    }
  },
  "_YVCZBxUFM0": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["마이크론", "삼성전자", "SK하이닉스", "반도체실적", "PER밸류에이션", "할인율"],
    "analysis": {
      "summary": "마이크론의 3분기 실적과 4분기 가이던스가 시장 컨센서스를 모두 20% 가까이 상회하며 반도체 <span class=\"text-rose-400 font-medium\">피크아웃 및 AI 버블 우려</span>를 불식시켰습니다. 호실적의 근간은 AI 서버용 HBM 및 고부가가치 메모리 수요의 강력한 지속에 기인합니다. 마이크론의 12개월 선행 PER은 7배 중반 수준으로 매력적이며, 이는 국내 투톱인 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>와 <span class=\"text-cyan-300 font-semibold\">삼성전자</span>에 대한 외국인 매수세 유입과 동반 랠리 기대감을 강력하게 키우고 있습니다.",
      "key_claims": [
        "마이크론의 어닝 서프라이즈와 가이던스 상향은 AI 데이터센터 투자가 일시적인 버블이 아닌 강력한 펀더멘탈에 기반함을 입증한다.",
        "포워드 PER 기준 7배 중반까지 주가 평가가 낮아진 마이크론의 밸류에이션 매력이 글로벌 반도체 전반의 재평가를 유도할 것이다.",
        "과거 마이크론 대비 20~30%에 달했던 한국 반도체 기업들의 할인율이 최근 5~10% 수준으로 크게 좁혀지며 상대적 강세가 부각되고 있다."
      ],
      "data_points": [
        "마이크론 3분기 실적 및 가이던스: 시장 예상치 대비 약 20% 상회",
        "마이크론 4분기 EPS 가이던스: 3.10달러 (이전 분기 2.25달러 대비 대폭 성장)",
        "한국 반도체 기업 할인율: 과거 20~30% 수준 -> 최근 5~10% 이내 축소"
      ],
      "signal": "bullish",
      "signal_confidence": "high",
      "signal_reason": "AI 고점 논란을 완벽히 해소하는 실적 발표와 4분기 가이던스 제시로, 메모리 반도체 사이클이 2027년까지 강력하게 연장될 것임을 시사하기 때문입니다.",
      "key_companies": ["마이크론", "SK하이닉스", "삼성전자"],
      "insight": "단순히 어닝 서프라이즈가 나왔다는 사실을 넘어, HBM 시장과 전반적인 AI 인프라 부품의 병목 현상이 여전함을 보여주고 있습니다. 이는 한국의 하드웨어 제조사들이 공급망의 절대적 열쇠를 쥐고 있음을 재확인시켜 줍니다. 향후 SK하이닉스의 미국 상장 및 삼성전자의 추가 자사주 매입 정책 등이 밸류에이션 할인을 더욱 축소시키는 촉매제가 될 것입니다.",
      "action_point": "공포에 흔들려 포트를 줄이기보다, 확실한 주도주인 <span class=\"text-cyan-300 font-semibold\">SK하이닉스</span>와 밸류에이션 매력이 높은 <span class=\"text-cyan-300 font-semibold\">삼성전자</span> 중심으로 반도체 비중을 50% 이상 유지하며 긴 호흡으로 대응해야 합니다."
    }
  },
  "cwaS1cqEE5E": {
    "primary_topic": "economy",
    "secondary_topics": ["tech", "stock"],
    "tags": ["우발성", "자본비용", "WACC", "AI인프라", "전력과부하", "마이크론실적"],
    "analysis": {
      "summary": "마이크론의 기록적인 호실적 뒤에는 급격히 늘어나는 <span class=\"text-rose-400 font-medium\">자본비용(WACC)</span> 및 AI 구동 방식의 근본적 비효율성이라는 거대한 그림자가 숨어 있습니다. 하이퍼스케일러들은 저렴한 채권 대신 고비용의 주식 발행과 희석(구글의 850억 달러 발행, 오픈AI의 재파이낸싱/IPO 압박 등)을 통해 무한 경쟁을 이어가고 있습니다. 연준의 금리 인상 리스크와 전력망 과부하가 맞물려, 향후 예상치 못한 <span class=\"text-rose-400 font-medium\">우발적 리스크</span>가 발발할 가능성에 대비해야 합니다.",
      "key_claims": [
        "AI 기업들이 높은 요구 수익률을 가진 주주 자본에 과도하게 의존하면서 전체적인 자본비용(WACC) 부담이 가중되고 있다.",
        "현재의 대용량 메모리 기반 실시간 구동 방식은 극심한 전력 과부하를 초래하므로 기술의 파기적 혁신 없이는 인프라가 감당하기 어렵다.",
        "역사적 금융 위기들은 언제나 예상치 못한 우발성에서 출발했으므로, AI 투자 쏠림 속에서 주변부 자산의 이탈과 인프라 지연을 주시해야 한다."
      ],
      "data_points": [
        "구글의 주식 발행 규모: 850억 달러 (포워드 PER 25배 수준)",
        "삼성전자 반도체 부문 마진율: 약 83% 수준 (공급망의 극단적 독식 구조를 시사)"
      ],
      "signal": "bearish",
      "signal_confidence": "medium",
      "signal_reason": "기술 혁신으로 생산성 개선 속도가 비용 상승을 압도하지 못하고 있으며, 자본비용 급등과 전력 부족 등 AI 생태계 내부의 병목 요인들이 누적되어 자산 가격 조정 리스크를 높이고 있기 때문입니다.",
      "key_companies": ["구글", "오픈AI", "애플", "엔비디아", "삼성전자", "SK하이닉스"],
      "insight": "AI 골디락스 네러티브 이면에 있는 고비용 구조를 파헤쳐야 합니다. 특히 애플이 현재의 고비용 메모리 독식 생태계(마진 83%에 달하는 반도체 가격)에 대한 반대 의사를 표명한 것은, 대형 플랫폼사들이 비용 통제를 위해 자체 반도체 개발이나 알고리즘 경량화에 혈안이 될 것임을 예고합니다. 자본비용이 올라가는 중금리 환경에서 단순 테마주는 소외되고, 명확한 현금 흐름을 창출하는 기업 위주로의 자금 쏠림이 한층 심화될 것입니다.",
      "action_point": "성장 테마에 지나치게 편중된 포트폴리오를 조정하여 확실한 <span class=\"text-cyan-300 font-semibold\">하드웨어 공급사</span> 및 <span class=\"text-cyan-300 font-semibold\">전력망 수혜주</span>로 포트를 좁히고, 자산의 20~30%는 <span class=\"text-amber-300 font-bold\">현금 비중</span>으로 보유하여 우발적 변동성에 대비하는 방어적 전략이 적절합니다."
    }
  },
  "e-M-ZEvxLPk": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["마이크론", "어닝서프라이즈", "시간외급등", "퀄컴", "온디바이스AI"],
    "analysis": {
      "summary": "마이크론의 주당순이익(EPS)이 위스퍼링 넘버마저 가볍게 뛰어넘는 25달러(가정 수치 포함 서프라이즈)를 달성하며 시간외 11% 이상 급등했습니다. 이와 동시에 <span class=\"text-cyan-300 font-semibold\">퀄컴</span>의 온디바이스 AI 시장 확대 가이드가 겹쳐 반도체 동반 랠리의 기폭제가 되었습니다. 강달러 기조 용인 하에 미국 국채 금리 안정화($4.3대)와 국제 유가의 60달러대 진입 등 <span class=\"text-amber-300 font-bold\">우호적 매크로 지표</span>들이 겹치며 골디락스 진입 신호가 감지됩니다.",
      "key_claims": [
        "마이크론은 시장의 혹독한 위스퍼링 넘버(22)마저 넘어서는 25를 달성하며 반도체 불확실성을 일거에 소멸시켰다.",
        "온디바이스 AI 성장성에 대한 퀄컴의 긍정적 가이드가 마이크론의 HBM 모멘텀과 시너지를 내며 IT 전반의 수요를 증명했다.",
        "유가가 3개월 만에 60달러선으로 급락하고 국채 금리가 하향 안정화되며 매크로 리스크가 눈에 띄게 완화되었다."
      ],
      "data_points": [
        "마이크론 EPS 예상치: 20.4달러 vs 실제 25달러 발표",
        "미국 10년물 국채 금리: 4.5% 수준 -> 4.3%대로 하락",
        "WTI 유가: 3개월 만에 60달러대(60달러 초반) 진입"
      ],
      "signal": "bullish",
      "signal_confidence": "high",
      "signal_reason": "반도체 어닝 서프라이즈와 매크로 여건 개선(유가 하락, 금리 안정)이 동시에 맞아떨어져 주식 시장의 위험 자산 투자 심리가 강력한 상승 동력을 확보했기 때문입니다.",
      "key_companies": ["마이크론", "퀄컴", "엔비디아", "SK하이닉스"],
      "insight": "최근 3일간의 주가 조정은 마이크론 실적 발표를 앞둔 공포 섞인 대기 장세에 불과했습니다. 이 억눌렸던 불확실성이 해소되자마자 전반적인 하이테크 기업들의 강력한 밸류에이션 매력이 부상하고 있습니다. 강달러의 부작용보다 유가 급락과 금리 인하 기대 등 인플레이션 제어 요인들이 더 강력한 우군으로 작용할 것입니다.",
      "action_point": "불안 심리에 따른 추격 매도를 멈추고, <span class=\"text-cyan-300 font-semibold\">마이크론 및 퀄컴</span> 등 실적으로 증명한 글로벌 핵심 반도체/부품 공급사로 비중을 재조정하여 어닝 시즌의 직접적 수혜를 누려야 합니다."
    }
  },
  "kDZVAHZBB50": {
    "primary_topic": "stock",
    "secondary_topics": ["economy", "tech"],
    "tags": ["조선주", "HD현대중공업", "HD한국조선해양", "발전용엔진", "캐나다군함수주", "LNG운반선"],
    "analysis": {
      "summary": "상선 가격(신조선가) 상승과 압도적인 기술 우위를 통한 LNG 운반선 쇼티지에 힘입어 국내 조선주들의 2027~2028년 실적 상향 추세는 흔들림 없이 우상향하고 있습니다. 특히 <span class=\"text-cyan-300 font-semibold\">HD현대중공업</span>이 데이터센터 발전용 가스 엔진(20MW) 대규모 수주에 성공하며, 조선업이 <span class=\"text-cyan-300 font-semibold\">AI 전력 인프라의 새로운 해결책</span>으로 부각되기 시작했습니다. 캐나다 잠수함 수주 및 미국 비전투함 조달 참여 등 방산 모멘텀도 여전히 잠재되어 있어 투자 매력이 급증하는 시점입니다.",
      "key_claims": [
        "LNG 운반선과 초대형 컨테이너선 등 한국 조선사들이 독점력을 가진 고부가 선종의 수주 잔고가 가득 차 있어 향후 실적이 보장된다.",
        "선박용 엔진 기술을 데이터센터의 자체 전력 발전용 엔진으로 응용 납품(HD현대중공업 가스 엔진 수주)하는 AI 내러티브가 생성되었다.",
        "미국 국방수권법(NDAA)의 비전투함 조달 개방 및 트럼프의 군함 수주 발언 등 해외 방산 시장 개척 기대감이 구체화되고 있다."
      ],
      "data_points": [
        "HD현대중공업 데이터센터 엔진 수주: 가스 발전 엔진 20MW 규모 총 33대 (2028~2030년 분할 인도)",
        "HD현대중공업 연간 엔진 제작 능력: 약 3GW (이번 데이터센터 엔진 비중이 연간 능력의 약 7%에 달함)"
      ],
      "signal": "bullish",
      "signal_confidence": "high",
      "signal_reason": "기존의 선박 제조 사이클에 더해 '데이터센터 자체 전력 공급원(엔진)' 및 '방산 수출 확장'이라는 멀티플 확장 스토리가 결합되면서 강력한 밸류에이션 재평가 국면에 들어섰기 때문입니다.",
      "key_companies": ["HD한국조선해양", "HD현대중공업", "한화오션"],
      "insight": "조선업을 단순히 낡은 굴뚝 산업으로 치부해서는 안 됩니다. 전력 병목에 빠진 글로벌 빅테크 기업들이 전력망 증설을 기다리지 못하고 조선소의 고출력 발전 엔진을 선제적으로 발주하기 시작한 것은 엄청난 패러다임 시프트입니다. HD한국조선해양의 경우 시가총액이 지분 할인을 과도하게 받아 청산 가치보다 낮은 가격에 거래되고 있어 장기적 투자 가치가 매우 높습니다.",
      "action_point": "조정 레벨에 있는 조선주들을 비중 확대 기회로 삼되, 자체 엔진 제작 능력과 강력한 자회사 가치를 지닌 업계 탑픽 <span class=\"text-cyan-300 font-semibold\">HD한국조선해양</span>과 실적 모멘텀이 뚜렷한 <span class=\"text-cyan-300 font-semibold\">HD현대중공업</span>으로 압축 대응하는 것이 정석입니다."
    }
  }
}

for vid, data in batch_4.items():
    save_and_delete(
        video_id=vid,
        primary_topic=data["primary_topic"],
        secondary_topics=data["secondary_topics"],
        tags=data["tags"],
        analysis_data=data["analysis"]
    )
print("Batch 4 completed!")
