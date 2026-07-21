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

batch_3 = {
  "nSF8_BlFix8": {
    "primary_topic": "tech",
    "secondary_topics": ["stock"],
    "tags": ["GLP1저혈당안전성", "인슐린터보차저", "비만약대중화", "바이오메가트렌드", "노보노디스크"],
    "analysis": {
      "summary": "GLP-1 비만 치료제(위고비 등)는 혈당이 상승했을 때만 인슐린 분비를 폭증시키는 '터보 차저' 메커니즘으로 작동하므로, 당뇨가 없는 정상인이 살 빼는 용도로 복용하더라도 저혈당 쇼크에 빠지지 않는 독보적 생리적 안전성을 입증했습니다. 이러한 메커니즘 덕분에 글로벌 대중화 및 적응증 확장이 가속화되고 있습니다.",
      "key_claims": [
        "GLP-1 제제는 췌장의 베타 세포가 혈당을 인지해 켜진 상태에서만 인슐린 분비를 증폭시키는 터보 차저 역할을 수행한다.",
        "정상인이 복용하더라도 스위치가 켜지지 않아 저혈당을 유발하지 않으므로 기존 당뇨약과 차별화되는 대중적 안전성을 보장한다."
      ],
      "data_points": [],
      "signal": "positive",
      "signal_reason": "저혈당 부작용이 없는 기전적 안전성이 확인되어 비만 치료제의 일반인 타깃 대중화 및 글로벌 바이오 시장 파이 확장이 보장되기 때문입니다.",
      "key_companies": ["노보노디스크(NVO)", "일라이릴리(LLY)"],
      "insight": "저혈당 위험이 없다는 것은 일반 소비자 대상 대중 의약품으로서의 침투율 한계가 없음을 뜻합니다. GLP-1 밸류체인의 성장성은 확고합니다.",
      "action_point": "GLP-1 생산 CDMO 및 펩타이드 원료 공급사에 대한 장기 매수 관점을 지속 유지해야 합니다."
    }
  },
  "68jlpTtNrf0": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["옵션만기웩더독", "외국인저가매집", "프로그램매도유도", "레버리지이동", "악재소멸패턴"],
    "analysis": {
      "summary": "오로라투자자문 이지환 대표는 미 옵션 만기(매달 3번째 금요일) 전후로 풋 프리미엄을 노린 노이즈(DeepSeek, Kimi K3 등)가 부풀려진 뒤 만기가 지나면 악재가 자취를 감추는 '웩더독(Whip the dog)' 패턴을 분석했습니다. 외국인은 선물을 통해 국내 기관의 프로그램 매도를 유발한 뒤 밑에서 삼성전자·하이닉스를 싹쓸이 저가 매집 중이며, 개인 레버리지 물량이 미국 ADR로 이동하며 국내 수급 체질이 개선되고 있습니다.",
      "key_claims": [
        "미국 옵션 만기 1~2주 전마다 악재(Kimi K3, 데이터센터 지연 등)를 부풀려 풋 프리미엄을 취한 뒤, 만기가 지나면 호재로 급반전되는 수급 왜곡이 되풀이되고 있다.",
        "외국인은 선물 투매로 국내 금융투자의 프로그램 매도를 유발한 후 밑에서 반도체 현물을 저가 매집하는 전형적인 매집 기법을 가동하고 있다.",
        "국내 단일 종목 2배 레버리지 ETF에 갇혀있던 수급이 해소되고 외국인 액티브 자금이 유입되며 반도체 바닥이 확고해졌다."
      ],
      "data_points": [
        "외국인 수급 변화: 프로그램 매도 유도 후 반도체 현물 순매수로 전환",
        "지수 조정폭: 코스닥 ~40%, 코스피 ~30% 조정 후 바닥 잡기 국면 진입"
      ],
      "signal": "positive",
      "signal_reason": "옵션 만기 수급 노이즈가 해소되고 외국인의 프로그램 저가 매집 전환이 확인되어 반도체 주도의 펀더멘탈 반등이 재개되고 있기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "삼성전자(005930)"],
      "insight": "옵션 만기 직전 쏟아지는 악재 뉴스에 공포 투매를 하면 안 됩니다. 외국인은 공포를 유발해 기관의 프로그램 매도를 끌어낸 뒤 최저점에서 주식을 담고 있습니다.",
      "action_point": "수급 왜곡으로 과조정받은 반도체 대형주를 털리지 말고 고수하며, 옵션 만기 직후 반등 파동에 적극적으로 탑승해야 합니다."
    }
  },
  "UytqcG_sekI": {
    "primary_topic": "robot",
    "secondary_topics": ["stock", "tech"],
    "tags": ["정부로봇구매", "군용로봇1000대", "현대차로봇", "삼성전자레인보우", "쿠팡로봇자동화"],
    "analysis": {
      "summary": "대한민국 정부가 정찰·폭발물 처리 및 경계 작전을 위해 군용 로봇 1,000대 규모의 공공 구매를 시동 걸었습니다. 현대차, 삼성전자, LG전자 및 레인보우로보틱스 등 국내 대표 기업들이 B2B/B2G 로봇 조달 사업에 본격 참여하고 있으며, 쿠팡의 24시간 물류 로봇 가동과 맞물려 산업 및 군사 로봇 상용화가 급물살을 타고 있습니다.",
      "key_claims": [
        "정부가 군용 및 공공 부문용 로봇 1,000대 구매 사업을 확정하여 공공 조달 시장의 로봇 생태계 확장을 자극하고 있다.",
        "삼성전자의 레인보우로보틱스 지분 활용 및 현대차 보스턴다이내믹스 기술 결합으로 B2B 무인화 솔루션 계약이 구체화되고 있다.",
        "쿠팡 등 물류 대기업들이 수백 대의 자율 이동 로봇(AMR)을 24시간 풀 가동하며 물류 자동화의 생산성을 실증했다."
      ],
      "data_points": [
        "정부 군용 로봇 조달 사업 규모: 1,000대 확정"
      ],
      "signal": "positive",
      "signal_reason": "정부 주도의 1,000대 군용 로봇 대규모 조달로 로봇 기업들의 실질 매출 발생(B2G)과 산업용 로봇 생태계 확장이 명확해졌기 때문입니다.",
      "key_companies": ["레인보우로보틱스(277810)", "현대차(005380)", "삼성전자(005930)", "두산로보틱스(454910)"],
      "insight": "로봇 산업이 연구실 시연을 넘어 정부 공공 조달(B2G)과 대기업 물류 현장(B2B)의 실질 수주 단계로 진입했습니다. 매출 실현 속도가 빠른 협동/군용 로봇 부품사가 수혜를 입습니다.",
      "action_point": "정부 조달 수혜를 직접 입는 레인보우로보틱스 및 로봇 핵심 부품(감속기, 액추에이터) 공급사들의 비중 확대를 추천합니다."
    }
  },
  "F_LsF359tVo": {
    "primary_topic": "stock",
    "secondary_topics": ["tech"],
    "tags": ["상승랠리본격화", "외국인순매수", "반도체조선방산", "실적시즌모멘텀", "수급개선"],
    "analysis": {
      "summary": "주린이 구조대 브리핑은 펀더멘탈 훼손 없는 투매 조정이 마무리되고, 외국인의 반도체·조선·방산 섹터 순매수 유입에 힘입어 본격적인 랠리 복귀 국면이 개화했다고 분석했습니다. 7월 말부터 전개될 국내외 빅테크 및 주력 기업들의 호실적 발표가 증시의 추세적 상승을 견인할 것으로 전망됩니다.",
      "key_claims": [
        "단기 수급 꼬임에 따른 과매도 구간이 끝남에 따라 반도체, 방산, 조선 등 주도주의 상승 랠리가 복귀하고 있다.",
        "외국인의 현선물 저가 매수가 다시 유입되기 시작하여 8월 랠리의 기틀을 마련했다."
      ],
      "data_points": [],
      "signal": "positive",
      "signal_reason": "수급 악재 소멸과 주력 3대 섹터(반도체, 조선, 방산)로의 외국인 매수세 재유입이 확인되었기 때문입니다.",
      "key_companies": ["SK하이닉스(000660)", "한화오션(042660)", "LIG넥스원(079550)"],
      "insight": "하락장에서 털리지 않은 우량 주도주(반도체/조선/방산)가 랠리 재개 시 가장 가파른 반등 탄력을 보입니다.",
      "action_point": "반도체와 방산 주도주 포트폴리오를 유지하고, 호실적이 예상되는 대형 조선주의 비중 확대를 권장합니다."
    }
  },
  "h_sI7zIdZLI": {
    "primary_topic": "stock",
    "secondary_topics": ["economy"],
    "tags": ["켈리공식", "섀넌의마귀", "포트폴리오재분배", "현금비중관리", "산술평균vs기하평균"],
    "analysis": {
      "summary": "신영증권 박소연 이사는 켈리 공식(Kelly Criterion)과 섀넌의 마귀(Shannon's Demon) 등 수학적 포트폴리오 이론을 바탕으로, 시장 변동성 극복을 위해서는 100% 주식 올인보다 항상 적정 현금 비중을 유지하고 주기적 리밸런싱을 단행해야 자산의 기하평균(복리) 수익률을 극대화할 수 있음을 증명했습니다.",
      "key_claims": [
        "자산의 장기 복리 성장은 단순 산술평균이 아닌 기하평균으로 결정되며, 변동성이 클수록 100% 주식 보유는 파산 위험(Ruin Risk)을 높인다.",
        "켈리 공식과 섀넌의 마귀 원리에 따라 현금 비중(예: 30~50%)을 유지하고 정기적 리밸런싱을 시행하면 변동성 자체가 수익으로 전환된다."
      ],
      "data_points": [],
      "signal": "neutral",
      "signal_reason": "개별 종목의 호재/악재가 아닌 포트폴리오 리밸런싱과 현금 관리의 중요성을 강조하는 수학적 투자 원론 분석이기 때문입니다.",
      "key_companies": [],
      "insight": "상승장과 하락장 모두에서 생존하는 비결은 적정 현금을 항시 보유하고 리밸런싱을 기계적으로 단행해 변동성을 복리 수익으로 바꾸는 것입니다.",
      "action_point": "포트폴리오 내 20~30% 수준의 안정적인 현금/채권 비중을 상시 확보하여 변동성 장세에서의 저가 매수 여력을 유지해야 합니다."
    }
  }
}

for vid, data in batch_3.items():
    save_and_delete(vid, data["primary_topic"], data["secondary_topics"], data["tags"], data["analysis"])
print("Batch 3 completed!")
