import json
from pathlib import Path

# 21개 비디오 분석 데이터 정의
analyses_db = {
    'iqsZSNt7nEA': {
        'primary_topic': 'robot',
        'secondary_topics': ['tech', 'stock'],
        'tags': ['현대자동차', '보스턴다이나믹스', '휴머노이드', '로봇부품', '일자리대체'],
        'analysis': {
            'summary': '현대자동차가 <span class="text-cyan-300 font-semibold">보스턴 다이나믹스</span>를 인수한 것은 국내 생산직의 강한 노조 리스크를 우회하고 미래 <span class="text-cyan-300 font-semibold">휴머노이드 로봇</span> 시장을 선점하기 위한 장기 포석이다. 이탈리아 및 미국 연구에 따르면 로봇 도입은 단순 해고가 아닌 고임금 관리직 이동의 커리어 사다리를 잠식하는 효과가 있다. 2035년까지 휴머노이드 시장이 380억 달러로 성장하면서 로봇 핵심 부품 기업들의 과실 공유가 기대된다.',
            'key_claims': [
                '보스턴 다이나믹스 인수는 <span class="text-amber-300 font-bold">노조 리스크 우회</span>와 생산성 제고를 노린 장기 시나리오다.',
                '로봇 도입 1%당 반복 노동 강도가 급감하여 노동자의 평생 기대 소득이 감소할 수 있다.',
                '<span class="text-cyan-300 font-semibold">액추에이터, 센서, 배터리</span> 등 하드웨어 부품사들이 시장 성장의 핵심 수혜자가 될 것이다.'
            ],
            'data_points': [
                '로봇 도입 1%포인트당 반복 노동 동작 0.834%포인트 감소',
                '미국 기준 로봇 1대 추가당 평균 커리어 밸류 1.5% 급감 및 3,360달러 평생 소득 감소',
                '2035년까지 휴머노이드 로봇 시장 380억 달러 성장 전망'
            ],
            'signal': 'bullish',
            'signal_reason': '강력한 글로벌 제조 경쟁력을 갖춘 로봇 플랫폼과 부품 생태계의 중장기 동반 성장이 확실시된다.',
            'key_companies': ['현대자동차', 'Boston Dynamics', '레인보우로보틱스', 'Tesla'],
            'insight': '기술 혁신의 흐름은 거역할 수 없으며, 노조 리스크가 없는 해외 신공장에서부터 로봇 기반의 무인 공정이 먼저 확산되어 전통 고용 구조를 완전히 바꿀 것이다.',
            'action_point': '로봇에 필수로 들어가는 핵심 하드웨어(특히 <span class="text-cyan-300 font-semibold">전고체 배터리</span> 및 구동용 모터/액추에이터) 대장주에 장기 투자하라.'
        }
    },
    'JqBXk897YTs': {
        'primary_topic': 'tech',
        'secondary_topics': ['stock'],
        'tags': ['광네트워크', 'AI병목현상', '광트랜시버', '데이터센터', '칩간통신'],
        'analysis': {
            'summary': 'AI 서비스가 멀티모달(동영상, 오감) 시대로 진화함에 따라 데이터센터 내 전송 지연을 막는 <span class="text-cyan-300 font-semibold">광 네트워크(Optical Network)</span>가 차세대 AI 인프라의 핵심으로 급부상했다. 기존 구리선 기반 통신은 대역폭 한계와 발열로 인해 수만 장의 GPU 병렬 연결을 효율적으로 지원할 수 없다. 칩 간 통신(스케일업)까지 광 통신이 확장되며 데이터센터 예산 중 네트워크 비중이 크게 늘어날 전망이다.',
            'key_claims': [
                '멀티모달 AI와 휴머노이드의 정교한 데이터 전송을 위해 네트워크 병목 해결이 절실하다.',
                '데이터센터 인프라 내 <span class="text-cyan-300 font-semibold">네트워크 할당 비중</span>이 10% 초반에서 향후 20%로 급증할 것이다.',
                '광 네트워크 전환은 부품 및 설계의 총체적 변화가 필요해, 단기적으로는 구리 하이브리드 기술도 함께 공존한다.'
            ],
            'data_points': [
                '데이터센터 예산 내 네트워크 비중 기존 10% 초반에서 15%로 증가, 향후 20%까지 전망',
                'AI 서버 내 메모리 원가 비중 기존 27%에서 40% 이상으로 증가'
            ],
            'signal': 'bullish',
            'signal_reason': '빅테크들의 초거대 CapEx 투자가 물리적 하드웨어 한계를 극복하기 위해 <span class="text-cyan-300 font-semibold">광트랜시버 및 스위치</span> 업종으로 집중될 수밖에 없다.',
            'key_companies': ['Ciena', 'Lumentum', 'Coherent', 'Nokia', '크리오테크'],
            'insight': 'GPU의 계산 능력이 극대화되더라도 이를 연결하는 통신 채널이 느리면 전체 시스템 성능이 저하되는 병목 현상이 발생하여, 네트워크 고도화가 반도체만큼 중요해졌다.',
            'action_point': '글로벌 독점적 기술력을 지닌 해외 <span class="text-cyan-300 font-semibold">광트랜시버 설계 기업</span> 및 광학 솔루션 소부장 종목의 조정을 기회로 매수하라.'
        }
    },
    'Jts7vHxRtHQ': {
        'primary_topic': 'tech',
        'secondary_topics': ['etc'],
        'tags': ['제프베이조스', 'AI일자리', '생산성향상', '자동화혁신', '노동력부족'],
        'analysis': {
            'summary': '제프 베이조스는 AI 혁신으로 인한 일자리 감소에 낙관적 시각을 제시하며, 오히려 장기적으로 <span class="text-amber-300 font-bold">노동력 부족 현상</span>이 발생할 것이라 전망했다. 생산성이 증가하면 물가가 안정되고 소비가 증진되어 전체 경제 규모가 확장되며, 이는 새로운 도구와 신산업의 발명으로 이어진다. 공장의 단순 노동자는 줄어들더라도 제품 기획과 엔지니어링 등 고부가 가치 직군의 신규 채용은 폭발적으로 증가할 것이다.',
            'key_claims': [
                '기술 발명과 <span class="text-amber-300 font-bold">생산성 증대</span>가 일자리 자체를 완전히 없애기보다는 경제 전반의 삶의 질을 제고한다.',
                '아이폰이나 페니실린처럼 획기적 발명품은 고용의 형태를 완전히 바꾸어 새로운 기회를 만들어낸다.',
                '생산 공장이 자동화되더라도 향후 기획 및 연구 개발에 필요한 <span class="text-cyan-300 font-semibold">엔지니어 고용</span>은 더 늘어날 것이다.'
            ],
            'data_points': [
                '아마존 공장의 자동화 수준 지속 상승',
                '신규 엔지니어링 및 개발자 부문 채용 비중 대폭 상향 계획'
            ],
            'signal': 'bullish',
            'signal_reason': '생산성 제고와 신생 산업의 태동으로 빅테크 플랫폼과 엔지니어링 시장의 장기적 펀더멘탈이 견고해진다.',
            'key_companies': ['Amazon', 'Microsoft', 'Apple'],
            'insight': '단기적인 노동 시장의 변화와 혼란은 존재할 수 있으나, 역사적으로 발명과 혁신은 언제나 경제를 성장시키고 인간의 삶을 더 윤택하게 만들어왔다.',
            'action_point': '실업 비관론으로 인한 단기 주가 출렁임에 휘둘리지 말고, <span class="text-cyan-300 font-semibold">AI를 이용해 자체 생산성을 비약적으로 높이는</span> 빅테크 리더들을 포트폴리오에 유지하라.'
        }
    },
    'ktNAkVbVRvc': {
        'primary_topic': 'economy',
        'secondary_topics': ['stock', 'tech'],
        'tags': ['미국이란종전', '국제유가하락', 'FOMC금리동결', '반도체성장률', '변동성장세'],
        'analysis': {
            'summary': '미국과 이란의 <span class="text-violet-300 font-medium">전격 종전 합의 기대감</span>과 스페이스X의 상장 성공으로 미국 3대 지수가 일제히 랠리를 펼쳤다. 국제 유가가 배럴당 90달러 이하로 급락하여 글로벌 인플레이션 압력이 크게 낮아졌고, 이는 FOMC의 긴축 완화 기대를 지지했다. 글로벌 반도체 시장이 메모리 중심 80% 이상 고성장에 힘입어 3분기 연속 강한 모멘텀을 유지하고 있으나, 국내 코스피는 외국인 수급 변동성으로 급등락하는 흐름을 보인다.',
            'key_claims': [
                '<span class="text-violet-300 font-medium">지정학적 리스크 완화</span>로 WTI 유가가 90달러를 깨고 내려와 소비자 심리지수가 큰 폭 개선됐다.',
                '반도체 매출이 4분기 급증하여 2002년 이후 최고 성장세를 달성, 메모리 반도체가 성장을 견인했다.',
                '국내 증시는 개인들의 B2투자 확대로 <span class="text-rose-400 font-medium">반대매매 리스크</span>가 커져 철저한 리스크 관리가 필요하다.'
            ],
            'data_points': [
                '미국 6월 소비자심리지수 예비치 48.9로 개선',
                '반도체 시장 4분기 매출 전분기 대비 27% 증가한 3,190억 달러 기록',
                '메모리 반도체 매출 80% 이상 급증',
                '외국인 국내 주식 시장 24거래일 연속 순매도 기록 후 첫 매수 전환'
            ],
            'signal': 'bullish',
            'signal_reason': '지정학적 악재 완화에 따른 유가 하향 안정화와 반도체 하드웨어의 초고속 성장이 연말 랠리의 단단한 지지대 역할을 한다.',
            'key_companies': ['Tesla', 'SpaceX', 'ARM', 'Adobe', 'Albemarle'],
            'insight': '시장의 가장 큰 걸림돌이었던 고유가와 지정학적 충돌이 소멸 단계에 접어듦에 따라, 펀더멘탈이 튼튼한 IT 및 리튬 배터리 소부장 업종의 수급 회복이 예상된다.',
            'action_point': '단기 고점 부담이 있는 유가 민감주 비중을 줄이고, 지정학적 리스크 소멸의 최대 수혜를 입을 <span class="text-cyan-300 font-semibold">메모리 반도체 및 빅테크 성장주</span>로 포트폴리오를 압축하라.'
        }
    },
    'm63iZ4X3OxU': {
        'primary_topic': 'stock',
        'secondary_topics': ['tech'],
        'tags': ['삼성전자', 'SK하이닉스', 'IT부품', '수급복귀', '반도체밸류체인'],
        'analysis': {
            'summary': '최근 글로벌 증시의 변동성 완화와 유동성 회복에 힘입어 <span class="text-cyan-300 font-semibold">삼성전자와 SK하이닉스</span>로의 기관/외국인 메이저 수급이 급격히 복귀하고 있다. 인공지능 서버 수요 강세와 함께 삼성전기 및 LG이노텍의 2분기 가이던스 상향 리포트가 잇따르며 반도체/IT 전반의 온기가 확산 중이다. 주말을 거치며 투자 심리가 턴어라운드된 만큼, 급락 장세를 거쳐 견고한 V자 반등이 나타날 가능성이 높아졌다.',
            'key_claims': [
                '최근 시장 급등락으로 단기 변동성이 극에 달했으나 수급적으로 글로벌 유동성이 대형 반도체주로 유입되고 있다.',
                '삼성전기, LG이노텍의 2분기 실적 가이던스 상향으로 반도체 밸류체인 전반의 <span class="text-cyan-300 font-semibold">IT 부품/소재 동반 랠리</span>가 시작되었다.',
                '매크로 지표 안정에 따라 시장 복귀를 적극 검토해야 할 시점이다.'
            ],
            'data_points': [
                '삼성전기 및 LG이노텍 2분기 실적 컨센서스 상향 리포트 대폭 집계',
                '미국 선물 시장 및 원화 자산 강세 흐름 동시 포착'
            ],
            'signal': 'bullish',
            'signal_reason': '대형 반도체주에 더해 IT 하드웨어 전반으로 가이던스 상향 및 <span class="text-cyan-300 font-semibold">외국인 수급 복귀</span>가 강하게 이어지고 있다.',
            'key_companies': ['삼성전자', 'SK하이닉스', '삼성전기', 'LG이노텍'],
            'insight': 'IT 대장주들의 랠리가 밸류체인 하단에 위치한 기판, 수동부품(MLCC) 등으로 낙수효과를 내고 있어 업황 턴어라운드의 신뢰도가 매우 높다.',
            'action_point': '이미 오른 반도체 외에, 가이던스가 급격히 상향되고 있는 <span class="text-cyan-300 font-semibold">MLCC 및 패키지 기판 선도사</span>들의 비중을 서서히 확대하라.'
        }
    },
    'maciNZEJzrc': {
        'primary_topic': 'economy',
        'secondary_topics': ['stock'],
        'tags': ['트럼프생일', '미국이란평화협정', '코스피사이드카', '유가폭락', '수급쏠림'],
        'analysis': {
            'summary': '도널드 트럼프 전 대통령의 생일 전후로 미국과 이란의 <span class="text-violet-300 font-medium">평화 협정 타결 소식</span>이 오피셜로 발표되며 코스피가 폭등, 매수 사이드카가 발동했다. 국제 유가는 배럴당 80달러 초반으로 크게 하락하며 글로벌 시장에 강력한 안도감을 주었다. 외국인이 코스피 대형주 위주로 1.5조 원 이상의 강력한 매수세를 보여주는 반면 코스닥은 수급이 일부 소외되며 상대적으로 약세를 보였다.',
            'key_claims': [
                '미국-이란 간 양해 각서 서명으로 지정학적 긴장이 크게 소멸하며 코스피가 5% 가까이 폭등했다.',
                '국제 유가의 안정과 원달러 환율 하락(1,510원대 진입)이 한국 증시의 <span class="text-cyan-300 font-semibold">외국인 강매수 유입</span>을 자극했다.',
                '유가 하락 수혜로 항공/해운 및 경기 민감주의 단기 반등 모멘텀이 강화될 것이다.'
            ],
            'data_points': [
                '코스피 당일 4.95% 상승한 8,525선 마감 (장중 8,600 돌파)',
                '외국인 코스피 하루 1조 5,000억 원 순매수 기록',
                '환율 1,510원대로 급락 및 WTI 유가 80달러대 진입',
                '코스피 시장 매수 사이드카 긴급 발동'
            ],
            'signal': 'bullish',
            'signal_reason': '중동 리스크라는 거대한 유가 인플레 압박이 제거되어 한국 증시 전반에 강력한 <span class="text-amber-300 font-bold">수급 리레이팅</span>이 진행되고 있다.',
            'key_companies': ['대한항공', '두산', '삼성전자', 'SK하이닉스'],
            'insight': '트럼프의 정치적 목적과 미국의 조기 휴전 압박이 맞아떨어져 유가 하향 안정화가 빠르게 실현되었으며, 이는 연준의 금리 압박 완화로 연결될 것이다.',
            'action_point': '지정학적 완화 수혜를 직접 입는 <span class="text-cyan-300 font-semibold">항공 및 운송 대형주</span>와 고유가 하락 수혜를 받는 대형 반도체 중심 포트폴리오를 유지하라.'
        }
    },
    'mSUEr1_0ZwE': {
        'primary_topic': 'etc',
        'secondary_topics': ['etc'],
        'tags': ['미래에셋숏폼', '지금부터미래', '에피소드', '마케팅컨텐츠'],
        'analysis': {
            'summary': "해당 비디오는 미래에셋증권에서 기획/제작한 '지금부터, 미래' 숏드라마의 일부이다. 등장인물 도윤이 오해로 인해 서툴게 사과하는 내용으로 이루어져 있으며, 공대 전설 및 특정 인물 간의 관계에 관한 해프닝을 다룬다.",
            'key_claims': [
                '등장인물 간의 개인적인 오해를 풀기 위한 진심 어린 사과를 담은 일상 에피소드이다.',
                '젊은 층을 타겟으로 제작된 증권사 브랜드 마케팅용 숏폼 드라마이다.'
            ],
            'data_points': [
                '미래에셋 공식 유튜브 채널 게재 숏드라마 시리즈물'
            ],
            'signal': 'neutral',
            'signal_reason': '순수 투자 시그널을 담고 있지 않은 대고객 마케팅 및 커뮤니케이션성 엔터테인먼트 콘텐츠이다.',
            'key_companies': ['미래에셋증권'],
            'insight': '증권사가 단순 리서치 정보를 넘어 캐릭터와 스토리가 있는 숏폼 콘텐츠를 통해 잠재 고객층과 친밀한 소통을 시도하고 있다.',
            'action_point': '투자 행동 요령 없음. 브랜드 호감도 측면에서만 가볍게 시청할 수준이다.'
        }
    },
    'nezzlzj9olM': {
        'primary_topic': 'stock',
        'secondary_topics': ['economy'],
        'tags': ['리밸런싱', '옵션만기일', '필라델피아반도체지수', '변동성', '스페이스X수급'],
        'analysis': {
            'summary': '미국-이란 종전 타결 속보로 글로벌 증시가 급반등한 가운데, 향후 시장의 핵심 변수로 <span class="text-rose-400 font-medium">스페이스X 관련 수급 변동</span>과 연준 금리 결정 전후의 \'리밸런싱\'이 제시되었다. 필라델피아 반도체 지수의 극심한 주간 변동성(고가와 저가의 격차가 13%)은 수급적 포지션 청산과 재구축 과정을 투영한다. 단기 급등 시 추격 매수보다는 80달러 전후의 유가 흐름과 금리 추이를 확인하며 변동성에 대응해야 한다.',
            'key_claims': [
                '중동 종전 속보로 인플레이션 우려가 경감되었으나 연준 FOMC를 전후한 <span class="text-rose-400 font-medium">수급 변동성</span>은 여전히 크다.',
                '필라델피아 반도체 지수의 주간 13% 변동폭이 보여주듯 수급 재구축이 극심하게 진행 중이다.',
                '급반등 장세에서 지나친 레버리지 베팅은 <span class="text-rose-400 font-medium">청산 압력</span>을 가중시켜 불리할 수 있으므로 주의해야 한다.'
            ],
            'data_points': [
                '나스닥 지수 6월 첫째 주 4.6% 급락 후 주 후반 극적 반등',
                '필라델피아 반도체 지수 주간 변동폭 고점 대비 저점 차이 13% (종가 9.4% 상승, 주간 저점 -3.5% 기록)',
                '국제 유가 80~81달러 안착 흐름 및 미국 2년물 국채 수익률 횡보'
            ],
            'signal': 'neutral',
            'signal_reason': '지정학적 악재 해소라는 호재와 연준 FOMC 경계감 및 선물옵션 동시 만기 리밸런싱이라는 수급 노이즈가 혼재되어 있어 단기 변동성이 지속될 수 있다.',
            'key_companies': ['SpaceX', 'NVIDIA'],
            'insight': "시장들이 호재에 맞춰 급반등하지만, 기관들이 대규모 선물옵션 만기 및 대형 테크주 편출입을 통해 포트폴리오를 조정하는 '리밸런싱' 시즌에는 가격 왜곡이 발생하기 쉽다.",
            'action_point': '반등 시 급하게 비중을 채우기보다 변동성을 이겨낼 수 있는 현금 비중을 유지하고, 분기말 <span class="text-rose-400 font-medium">기관 리밸런싱 매물</span> 출회 시 안정적인 실적주 위주로 저가 매수하라.'
        }
    },
    'NTk-M2cLOi8': {
        'primary_topic': 'stock',
        'secondary_topics': ['tech', 'economy'],
        'tags': ['전쟁종식재건', 'IT주도주', '반도체선호', '유동성쏠림', '지수전망'],
        'analysis': {
            'summary': '중동 종전 합의 이후 시장의 기대와 달리 단순 재건 테마주(건설, 기계)는 주도권을 쥐지 못하고 있으며, 여전히 <span class="text-cyan-300 font-semibold">IT/반도체 중심의 주도주</span>가 가장 강력한 흐름을 지속하고 있다. 유가 하락에 따른 비용 절감과 유동성 환경 개선은 결국 실적 가시성이 가장 돋보이는 테크 섹터로 자금이 재유입되는 동력으로 작용한다. 주가지수 9,000선 돌파 시도가 이어지는 상황에서 수급 쏠림이 유효하다.',
            'key_claims': [
                '지정학적 리스크 소멸 국면에서 재건 수혜 테마보다 펀더멘탈이 검증된 <span class="text-cyan-300 font-semibold">IT 반도체 업종</span>의 지배력이 더 확고하다.',
                '유가 하락으로 확보된 인프라 예산과 투자 여력은 결국 인공지능(AI)과 디지털 전환 설비로 집중된다.',
                '국장 및 미증시 모두 단기 테마성 자금 순환매보다 실적 지표가 찍히는 대형주 위주로 대응하는 것이 효율적이다.'
            ],
            'data_points': [
                '원-달러 환율 1,510원대로 하향 및 유가 안정',
                '미국 나스닥 선물 및 주요 IT 지수 주말 내 1.5%대 랠리',
                '지수 단기 7,000선 돌파 후 8,000 돌파 및 9,000선 트라이 전망'
            ],
            'signal': 'bullish',
            'signal_reason': '일시적인 테마 장세로의 유출 없이 <span class="text-cyan-300 font-semibold">반도체 및 인프라 주도군</span>으로 유동성 쏠림이 더욱 단단해지고 있다.',
            'key_companies': ['삼성전자', 'SK하이닉스', 'NVIDIA'],
            'insight': '전쟁 종식은 비용 요인 하락을 통해 실질 구매력을 늘리며, 이는 단순 건설 재건보다 부가가치가 가장 높은 미래 혁신 IT 자산으로의 교체 투자를 촉진한다.',
            'action_point': '모멘텀이 약한 재건 테마주의 단기 낙폭과대 반등에 현혹되지 말고, 여전히 시장을 지배하는 <span class="text-cyan-300 font-semibold">인공지능 하드웨어 선도 기업</span>에 핵심 비중을 집중하라.'
        }
    },
    'nWlYph4WrlQ': {
        'primary_topic': 'economy',
        'secondary_topics': ['stock'],
        'tags': ['유동성스톰', 'FMC금리결정', 'B2U반대매매', '외국인옵션풋콜', '국민연금수급'],
        'analysis': {
            'summary': '미국과 이란의 평화 협정 체결로 WTI 국제 유가가 배럴당 80달러 초반으로 가파르게 안정화되며 인플레이션 해소 환희가 증시를 덮쳤다. 하지만 수급적으로 외국인의 코스피 매도 규모가 역대 최장이었던 점과 국내 투자자의 고위험 포모(FOMO) 트레이딩은 잠재적 위험 요인이다. 특히 6월 통화정책(FOMC, BOJ) 회의가 집중된 슈퍼 위크를 앞두고 있어 통화 유동성의 일시적 쏠림 및 변동성 급증에 대비해야 한다.',
            'key_claims': [
                '중동 리스크 종식과 함께 유가 하락이 소비자 심리를 이끌며 미국 선물이 1~2% 급등 랠리를 펼치고 있다.',
                '역대급 코스피 변동성 지수와 <span class="text-rose-400 font-medium">B2U 반대매매 폭증</span>(3거래일 연속 1천억 이상)은 국내 증시의 취약한 기초체력을 보여준다.',
                '외국인들이 수급 리스크 해지를 위해 선물옵션 시장에서 역대급으로 <span class="text-rose-400 font-medium">하방(풋옵션) 베팅</span>을 늘려 놓은 점을 예의주시해야 한다.'
            ],
            'data_points': [
                '외국인 5월 7일 ~ 6월 11일까지 24거래일 연속 최장 코스피 매도 랠리 기록',
                '유가 80달러 중후반에서 80달러 초반으로의 급락 흐름 포착',
                '미국 옵션 시장 내 MSCI 한국 ETF(EWY)의 풋옵션 배팅 비중 급증',
                '국민연금 국내 주식 보유 한도 상향 조치 (최소 25.8%까지 수급 버퍼 마련)'
            ],
            'signal': 'neutral',
            'signal_reason': '지정학적 완화로 급등 출발하지만, 외국인의 풋 베팅과 만기일 및 주요국 금리 결정 등 매크로 유동성 변동성이 고조되는 구간이다.',
            'key_companies': ['삼성전자', 'SK하이닉스'],
            'insight': '시장들이 호재에 환호할 때 수급의 이면을 살펴보면 파생 시장에서의 해지 배팅이 급증하고 있어, 추세적 상승보다 큰 폭의 변동성 내 옥석 가리기가 진행될 가능성이 높다.',
            'action_point': '지나친 상방 쫓아가기식 매수를 자제하고, 변동성이 완화되어 <span class="text-rose-400 font-medium">환율이 안정되는 국면</span>을 확인하며 철저히 실적 분산 투자를 집행하라.'
        }
    },
    'Oj5Mf1eg-cw': {
        'primary_topic': 'stock',
        'secondary_topics': ['tech'],
        'tags': ['레버리지ETF', '단일종목ETF', '장마감리밸런싱', '주가왜곡', '수급병목'],
        'analysis': {
            'summary': '자산운용사들의 단일 종목 레버리지 ETF 출시가 늘어나면서 <span class="text-rose-400 font-medium">삼성전자 및 SK하이닉스의 변동성</span>을 비정상적으로 키우는 요인으로 지적되고 있다. 단일 종목 레버리지 ETF는 일일 2배 수익률 약정을 위해 매일 장 마감 직전 선물/현물 매매를 통해 배율을 맞추는 리밸런싱을 강제한다. 주가가 오르는 날에는 장 마감 직전 매수 수요를 폭증시켜 상승을 가속하고, 내리는 날에는 투매를 자극해 급락을 심화시키는 이른바 \'꼬리가 몸통을 흔드는\' 왜곡 현상이 고착화되고 있다.',
            'key_claims': [
                '단일 종목 레버리지 ETF는 일일 배율을 추종하기 위해 장 마감 직전 기계적인 매매(리밸런싱)를 집행한다.',
                '주가 상승 시 리밸런싱을 위해 추가 매수가 유입되어 상승폭이 증폭되며, 하락 시에는 강제 매도로 하락폭이 깊어진다.',
                '단일 종목 ETF의 폭발적 성장이 오히려 대형 주도주의 <span class="text-rose-400 font-medium">일일 변동성 왜곡 현상</span>을 극대화하고 있다.'
            ],
            'data_points': [
                '국내 ETF 전체 시가 총액 최초 500조 원 돌파',
                '단일 종목 레버리지 ETF 도입 이후 특정 거래일 하이닉스 주가 7.7% 하락 시 관련 ETF의 기계적 왜곡에 따른 변동폭 확대'
            ],
            'signal': 'neutral',
            'signal_reason': '주가의 장기 펀더멘탈을 훼손하지는 않으나, 기계적 수급으로 인해 단기 일중 변동성이 상하방 모두 과도하게 발생할 수 있음을 경고한다.',
            'key_companies': ['삼성전자', 'SK하이닉스'],
            'insight': '금융 상품의 혁신이 실물 주식의 수급을 왜곡하는 현상이 잦아지고 있으므로, 투자자들은 장 마감 30분 전의 변동성이 펀더멘탈의 변화가 아닌 기계적 리밸런싱의 결과일 수 있음을 인지해야 한다.',
            'action_point': '단일 종목 레버리지 ETF 수급으로 인해 장 마감 직전 <span class="text-rose-400 font-medium">과도하게 왜곡된 급락 시점</span>을 오히려 현물 장기 매수의 기회로 활용하라.'
        }
    },
    'Qc7KGoDj5m8': {
        'primary_topic': 'tech',
        'secondary_topics': ['etc'],
        'tags': ['앤트로픽', '세이프가드', 'AI투명성', '답변왜곡', '보이지않는개입'],
        'analysis': {
            'summary': '앤트로픽(Anthropic)이 차세대 모델 \'Opus 4.8\' 등의 출시 과정에서 사용자에게 고지하지 않고 안전장치를 가동한 \'보이지 않는 개입\'이 밝혀지며 논란이 일었다. 시스템 카드에 명시된 <span class="text-rose-400 font-medium">프롬프트 모디피케이션(질문 조작), 스티어링 벡터(사고 강제 전환), 패프트(일부 재교육)</span>를 통해 AI의 결과물을 인위적으로 흐리게 만든 것이다. 사용자들의 격렬한 반발로 앤트로픽은 이틀 만에 공식 사과하고 오프스 4.8 폴백 방식으로 투명하게 전환하겠다고 발표했다.',
            'key_claims': [
                '앤트로픽은 사용자가 모르게 답변을 순화하거나 사고 흐름을 비트는 세이프가드를 가동했다.',
                '답변 거부가 아닌, 인위적으로 왜곡된 답변을 제공함으로써 모델 신뢰성에 심각한 타격을 입혔다.',
                '안전 규제와 인공지능 성능 간의 균형 설정 실패로 인해 기업용 <span class="text-rose-400 font-medium">AI 신뢰도 및 투명성 검증</span> 이슈가 수면 위로 떠올랐다.'
            ],
            'data_points': [
                '앤트로픽 출시 단 2일 만에 세이프가드 시스템 강제 개입 논란 발생',
                'Opus 4.8 폴백 방식으로의 전면 복귀 결정'
            ],
            'signal': 'neutral',
            'signal_reason': '앤트로픽의 투명성 논란은 단기 노이즈에 가깝지만, AI 규제 시스템의 신뢰성에 관한 근본적인 물음을 제기한다.',
            'key_companies': ['Anthropic', 'OpenAI'],
            'insight': 'AI 모델의 세이프가드 개입이 투명하게 공유되지 않는다면 기업들은 인공지능이 제공한 원시 정보와 조작된 정보 간의 차이를 구분하지 못해 비즈니스 의사결정의 리스크가 될 수 있다.',
            'action_point': '기술 투명성 및 개방성이 확보된 <span class="text-cyan-300 font-semibold">오픈소스 LLM 툴체인</span>과 개발 주도권을 쥔 플랫폼사들의 솔루션에 집중할 필요가 있다.'
        }
    },
    'QJtL1fYQ_yQ': {
        'primary_topic': 'economy',
        'secondary_topics': ['stock', 'energy'],
        'tags': ['호르무즈개방', '미국이란합의', '국제유가안정', '중소형주반등', '지정학완화'],
        'analysis': {
            'summary': '트럼프 대통령이 이란과의 최종 합의를 공식화하며 <span class="text-violet-300 font-medium">호르무즈 해협의 전면 개방</span>과 해군 봉쇄 즉각 철수를 승인했다. 이란 역시 오늘 밤부터 전선에서의 연구적 군사 작전 종료를 발표하며 공식적인 종전을 선언했다. 이에 선물 시장에서 국제 유가는 배럴당 80달러 초반으로 급락했고, 증시는 테크주와 중소형주 위주로 강력한 반등 모멘텀을 형성하고 있다.',
            'key_claims': [
                '미국과 이란이 동시에 사실상 승리 선언을 하며 60일간의 최종 협상 양해 각서 문안 공개가 임박했다.',
                '유가 하락(80달러대 진입)으로 물가 압력이 완화되어 <span class="text-cyan-300 font-semibold">러셀 2000 중소형 지수</span> 및 테크 지수가 1.5% 이상 상승 랠리를 펼치고 있다.',
                '다만 제네바 본협정 서명식(19일) 이전까지 이스라엘의 산발적 도발이나 돌발 공습은 최종 조율의 변수가 될 수 있다.'
            ],
            'data_points': [
                '국제유가 WTI 기준 80달러 초반으로 급락',
                '미국 증시 테크 선물 +1.40%, 중소형 러셀2000 선물 +1.69% 급등',
                '양국 최종 본합의 서명 예정일 6월 19일 지정'
            ],
            'signal': 'bullish',
            'signal_reason': '최악의 중동 전면전 우려가 종식되면서 유가 폭락과 환율 안정, 그리고 그간 눌려 있던 IT 성장주와 중소형주로의 강력한 수급 확산이 기대된다.',
            'key_companies': ['Tesla', 'NVIDIA'],
            'insight': '매크로 환경에서 유가 안정은 금리 인하 경로를 단축하는 효과를 내며, 이는 소외되었던 중소형 혁신주들에 강한 성장 활력을 줄 것이다.',
            'action_point': '단기 고유가 테마주(정유, 해운)에서 즉각 엑시트하고, 유가 완화 국면에서 금리 수혜가 클 <span class="text-cyan-300 font-semibold">중소형 테크주 및 하드웨어 가치주</span>로 자금을 신속히 재배치하라.'
        }
    },
    'qZqCE7xfl0g': {
        'primary_topic': 'economy',
        'secondary_topics': ['stock'],
        'tags': ['오건영부의갈림길', '고유가구조화', '연준의장교체', 'AI혁명', '미국일극주의'],
        'analysis': {
            'summary': '오건영 단장은 중동 전쟁이 종식되어도 지정학적 리스크의 상흔과 정유/가스 파괴 시설의 재건 문제로 유가가 급격히 전쟁 이전 레벨(60달러대)로 돌아가긴 어렵다고 분석했다. 배들의 용선료, 위험 지역 인건비, 보험료 급증 등 <span class="text-rose-400 font-medium">운송 비용의 구조적 상승</span>이 지속되기 때문이다. 향후 자산 시장은 트럼프의 관세 정책, 연준의 친트럼프 수장(케빈 워시) 교체 변수, 그리고 AI 혁명의 성공 여부라는 다차원적 \'부의 갈림길\'에 직면하고 있다.',
            'key_claims': [
                '중동 에너지 재건 지연 및 호르무즈 해협 용선료/보험료 폭증으로 <span class="text-rose-400 font-medium">구조적 고유가(80달러 내외)</span>가 장기화될 수 있다.',
                '연준 의장이 케빈 워시로 교체되면서 연준의 독립성 약화 우려와 인플레이션 통제 리스크가 자극될 가능성이 있다.',
                '향후 5년의 장기 투자를 가정하면 매크로 충격을 극복하고 살아남을 고부가가치 <span class="text-cyan-300 font-semibold">AI 포트폴리오</span>의 완성도가 가장 중요하다.'
            ],
            'data_points': [
                '전쟁 이전 국제 유가 배럴당 60달러대에서 전쟁 중 120달러 급등 후 현재 80달러 후반대 안착',
                '일본 니케이 지수 금융위기 당시 8,000선에서 현재 65,000선 돌파 (약 8배 상승)',
                '연준 6월 FMC 금리 가이드라인 및 캐빈워시 임명 절차 진행'
            ],
            'signal': 'neutral',
            'signal_reason': '전쟁 종식이라는 환희 이면에 높은 구조적 물가와 연준 독립성 훼손 리스크가 도사리고 있어 장기적 분산 포트폴리오 유지가 필수적이다.',
            'key_companies': ['신한은행'],
            'insight': '시장들의 적응력은 대단하여 지정학이나 관세 악재에 익숙해지지만, 그 과정에서 나타나는 비용 증가(인플레이션) 체질은 쉽게 변하지 않으므로 자산 배분의 기조를 흐트러뜨려선 안 된다.',
            'action_point': '유가 급락에 따른 일시적 안도감에 취해 가치주 비중을 과도하게 낮추지 말고, <span class="text-cyan-300 font-semibold">에너지 다변화 수혜주</span> 및 확실한 독점력을 지닌 AI 인프라주를 고르게 분산 배치하라.'
        }
    },
    'RBrP44mxPuE': {
        'primary_topic': 'stock',
        'secondary_topics': ['tech'],
        'tags': ['반도체조정기', '역기저효과', '수출증가율', 'CapEx투자', '매수타이밍'],
        'analysis': {
            'summary': '이형수 대표는 반도체 업황의 전년 대비 역기저 효과와 5월 일평균 수출 증가율의 둔화가 시장에 <span class="text-rose-400 font-medium">3분기 가격 조정 압력</span>을 가할 수 있다고 조언했다. 하지만 과거 B2C 중심 사이클과 달리 이번 사이클은 빅테크 간 경쟁에 기반한 대규모 \'인프라 투자(CapEx)\' 성격이 짙어 설비 투자 속도를 늦추기 어렵다. 따라서 3분기의 흔들림과 변동성을 겪고 나면 올 연말부터 내년까지 반도체 주가가 역사적 고점을 다시 경신하는 최적의 매수 기회가 될 것이다.',
            'key_claims': [
                '작년 하반기 메모리 급등에 따른 역기저 효과로 인해 <span class="text-rose-400 font-medium">3분기 메모리 수출 지표</span>의 일시적 둔화가 예상된다.',
                '이번 인공지능 인프라 투자는 경쟁 압박 때문에 빅테크의 CapEx를 중단할 수 없어 장기 수요의 골격이 유지된다.',
                '현금 비중을 유지하며 3분기 조정기를 견뎌내면, 연말 강력한 <span class="text-cyan-300 font-semibold">반도체 소부장 랠리</span>를 누릴 수 있다.'
            ],
            'data_points': [
                '5월 전체 메모리 일평균 수출 증가율 270%대에서 100%대로 연말 둔화 가능성',
                '메모리 법령 가격 급등 역기저 반영 시점 8월 말 이후 집중'
            ],
            'signal': 'bullish',
            'signal_reason': '3분기의 일시적 수급 및 기저 효과 조정을 거쳐 대규모 인프라 발 반도체 메가 사이클의 2차 랠리가 시작될 가능성이 높다.',
            'key_companies': ['삼성전자', 'SK하이닉스'],
            'insight': '사이클의 피크 아웃 논란이 일 때 지표의 절대적 수치보다 빅테크들의 자본 지출 경쟁(FOMO) 구조가 멈췄는지를 봐야 하며, 경쟁이 지속되는 한 반도체 장비 수요는 계속 우상향한다.',
            'action_point': '3분기 가격 지표 둔화 리포트로 인해 반도체 대형주 및 장비 소부장이 흔들릴 때 <span class="text-cyan-300 font-semibold">현금을 분할 투입하여 비중을 확충</span>하는 기회로 활용하라.'
        }
    },
    'RjvFCXUJ3kA': {
        'primary_topic': 'etc',
        'secondary_topics': ['etc'],
        'tags': ['안될과학', '아티스트해윤', '사이언스나이트라이브', '과학대중화', '토크쇼'],
        'analysis': {
            'summary': "과학 대중화 채널 안될과학에 글로벌 팝 그룹 '나우 유나이티드' 출신 아티스트 해윤이 출연하여, 해외 활동 경험과 솔로 데뷔 에피소드 및 일상 속 뜨개질 취미를 소개했다. 진행자 궤도는 대중이 과학을 즐길 수 있도록 클럽을 대여하여 개최한 '사이언스 나이트 라이브(Science Night Live)' 수학/과학 댄스 이벤트를 공유하며 흥미를 유발했다.",
            'key_claims': [
                '다국적 그룹에서 솔로 아티스트로 변신한 해윤의 글로벌 소통 경험과 도전 정신을 다룬 토크 콘서트이다.',
                '클럽에서 수학 수식 야광봉을 흔드는 <span class="text-cyan-300 font-semibold">사이언스 나이트 라이브</span> 이벤트를 통해 대중과 과학의 융합을 추진했다.'
            ],
            'data_points': [
                '아티스트 뮤직비디오 조회수 1억 뷰 이상 달성 기록',
                '사이언스 나이트 라이브 행사 틱톡/유튜브 공유 수천 건 바이럴 기록'
            ],
            'signal': 'neutral',
            'signal_reason': '순수 투자 정보가 아닌 아티스트 인터뷰 및 대중 과학 문화 소통을 위한 예능형 교양 콘텐츠이다.',
            'key_companies': ['안될과학'],
            'insight': '지루하고 딱딱하게 느껴지는 과학/수학 공식을 클럽 댄스파티 형식의 서브컬처와 결합하여 대중의 진입장벽을 획기적으로 낮추는 시도가 돋보인다.',
            'action_point': '투자 행동 요령 없음. 힐링 및 교양 엔터테인먼트로 시청하기에 적합하다.'
        }
    },
    'tk-LXS-w0y8': {
        'primary_topic': 'tech',
        'secondary_topics': ['stock'],
        'tags': ['젠슨황', '에이전틱AI', '소프트웨어생존', '엔비디아', 'AI도구'],
        'analysis': {
            'summary': '젠슨 황 엔비디아 CEO는 <span class="text-cyan-300 font-semibold">에이전트형 AI(Agentic AI)</span>의 등장으로 모든 소프트웨어 회사들이 문을 닫을 것이라는 우려에 정면 반박했다. 에이전트가 범용화될수록 인간 노동력의 수적 한계를 뛰어넘어 기존보다 기하급수적으로 많은 전용 도구(소프트웨어)를 소비하게 된다. 따라서 현시점은 소프트웨어 기업들에 전례 없는 큰 시장 확장의 기회이며, 다만 모든 소프트웨어는 AI 에이전트가 쉽게 파싱하고 활용할 수 있는 형태로 재설계되어야 한다.',
            'key_claims': [
                'AI 에이전트의 대량 도입은 생산 노동의 병목을 해결하고 소프트웨어 수요를 <span class="text-cyan-300 font-semibold">수십 배 이상 폭증</span>시킬 것이다.',
                '에이전트 중심의 생태계로 재구성하지 못하는 레거시 소프트웨어 기업들은 <span class="text-rose-400 font-medium">도태 위험</span>이 크다.',
                '미래 소프트웨어의 가치는 사람뿐 아니라 AI 에이전트에게 얼마나 가치 있는 도구로 제시되는가에 달려 있다.'
            ],
            'data_points': [
                '글로벌 B2B 엔터프라이즈 에이전트 도입률 급증 추세',
                '소프트웨어 API 연동 지연 수준 및 전송 대역폭 가이드 제시'
            ],
            'signal': 'bullish',
            'signal_reason': 'AI 에이전트 생태계의 도래로 소프트웨어 소모량이 기하급수적으로 폭증하며 새로운 <span class="text-cyan-300 font-semibold">B2B AI 소프트웨어</span> 전성시대가 열린다.',
            'key_companies': ['NVIDIA', 'Microsoft'],
            'insight': 'AI가 인간을 대신해 코딩하고 프로그램을 실행하는 시대에는 소프트웨어의 사용 주체가 인간에서 에이전트로 이동하므로, API 친화적이고 에이전트 지향적인 혁신 소프트웨어 기업의 몸값이 치솟을 것이다.',
            'action_point': '단순 UI 위주의 레거시 소프트웨어사에서 벗어나, 에이전트 AI가 호출하여 복잡한 태스크를 해결하는 데 필수적인 <span class="text-cyan-300 font-semibold">엔터프라이즈 API/DB 솔루션</span> 기업을 매수하라.'
        }
    },
    'UtUyfRostjY': {
        'primary_topic': 'robot',
        'secondary_topics': ['tech'],
        'tags': ['중국로봇', '뉴비트리U1', '원가경쟁력', '중국로보틱스', '휴머노이드양산'],
        'analysis': {
            'summary': '중국의 로보틱스 선도 기업 뉴비트리(Newvitry)가 인간의 외모와 표정을 완벽하게 재현한 실리콘 피부 기반 <span class="text-cyan-300 font-semibold">휴머노이드 로봇 \'U1\'</span>을 출시했다. 서구권 기업들이 로봇과 인간의 구분을 명확히 하는 철학을 갖는 반면, 중국 기업들은 정서적 교감을 위해 인간과 99% 유사한 디자인을 추구하고 있다. 베이징 로봇 마라톤에서 하프 마라톤을 50분대에 완주하는 신체 협응력 향상과 함께, 1천만 원대 초반의 미친 원가 경쟁력을 바탕으로 전 세계 시장 대량 양산을 노리고 있다.',
            'key_claims': [
                '중국의 휴머노이드 로봇 U1은 실리콘 피부와 근육 매핑 기술로 <span class="text-cyan-300 font-semibold">극사실적 인간 모사</span>를 구현했다.',
                '중국 로봇 생태계는 수만 개의 스타트업 경쟁을 바탕으로 <span class="text-cyan-300 font-semibold">2만 달러 이하의 압도적 저가격</span> 양산 체제를 구축했다.',
                '미국의 실용주의(물류/작업 특화)와 달리 중국은 정서적 교감 및 극사실적 형태 선점에 역량을 집중하고 있다.'
            ],
            'data_points': [
                '뉴비트리 U1 모델 키 183cm, 몸무게 42kg (여성형 키 168cm, 몸무게 35kg)',
                '중국 아너 휴머노이드 하프 마라톤 완주 기록 50분 26초 (인간 세계 기록 57분보다 단축)',
                '유니트리 G1 로봇 시판가 2만 달러 및 원가 약 8,900달러(약 1,200만 원)'
            ],
            'signal': 'bullish',
            'signal_reason': '중국발 초저가 휴머노이드 보급으로 로봇 상용화 타임라인이 비약적으로 단축되고 있으며, 관련 핵심 부품 단가 하락이 생태계 성장을 촉진한다.',
            'key_companies': ['뉴비트리(Newvitry)', '유니트리(Unitree)', 'Figure AI'],
            'insight': '중국은 스마트폰, 배터리에서 보여준 압도적인 원가 절감 제조 파워를 로봇 산업에도 그대로 투영하고 있어, 로봇 하드웨어의 범용화(Commoditization) 속도가 예상보다 빠를 것이다.',
            'action_point': '중국 로봇 플랫폼 기업의 글로벌 확장에 따른 하드웨어 부품(<span class="text-cyan-300 font-semibold">액추에이터, 고성능 모터, 센서</span>) 공급망을 확보한 한중일 강소기업들에 주목하라.'
        }
    },
    'V0IfOF0eE24': {
        'primary_topic': 'crypto',
        'secondary_topics': ['economy'],
        'tags': ['해외가상자산신고', '세무법인리치', '비수탁형지갑', '국세청세무조사', 'CARF'],
        'analysis': {
            'summary': '국세청이 가상자산 과세 시스템 본격 가동을 위해 해외 금융계좌 모니터링 및 국가 간 <span class="text-rose-400 font-medium">가상자산 이전 정보 교환망(CARF)</span> 구축을 추진 중이다. 해외 가상자산 거래소(바이낸스 등)에 잔액 합계 5억 원 이상 보유 시 매월 말일 기준으로 신고할 의무가 부과되며, 미신고 시 상당한 과태료가 발생한다. 다만 메타마스크 등 개인이 직접 지갑 키를 통제하는 비수탁형(Non-Custodial) 탈중앙화 지갑은 현재 신고 대상에서 제외되어 있어 법령 해석에 주의가 요구된다.',
            'key_claims': [
                '국세청은 2027년 본격 과세를 앞두고 해외 가상자산 데이터베이스와 <span class="text-rose-400 font-medium">자금 추적 시스템</span>을 고도화하고 있다.',
                '해외 금융자산(코인 포함) 합산 5억 초과 시 신고 대상이며, 세무 조사 기준은 실무상 20억 수준에서 점차 확대될 전망이다.',
                '비수탁형 개인 지갑은 규제망의 사각지대에 있으나 향후 CARF 시스템 안착 시 감시망이 촘촘해질 것이다.'
            ],
            'data_points': [
                '국내 가상자산 KYC 계좌수 177만 개에서 1,113만 개로 급증',
                '코인 자산가 중 80% 이상은 소액 투자자로 기본 공제 한도(250만 원) 미만 과세 제외군 해당',
                '해외 금융계좌 총합 5억 원 초과 시 신고 대상 편입 및 20억 초과 고액 지갑 표적 모니터링 가동'
            ],
            'signal': 'bearish',
            'signal_reason': '가상자산의 익명성과 탈중앙화 성격이 세무 당국의 <span class="text-rose-400 font-medium">글로벌 공조 규제망</span>에 갇히며 자금 유입 위축 등 시장 유동성 저해 요인으로 작용한다.',
            'key_companies': ['세무법인 리치', 'Binance'],
            'insight': '규제 당국은 탈세 방지와 세수 확보를 위해 가상자산을 완전히 기존 제도권 금융 시스템의 과세 모델 안으로 포섭하려 하며, 이는 고액 자산가들의 가상자산 보유 방식을 크게 변화시킬 것이다.',
            'action_point': '해외 거래소 및 개인 지갑 간의 빈번한 자금 이동은 가이드라인 위반 과태료를 유발할 수 있으므로, 전문가의 자문을 얻어 <span class="text-rose-400 font-medium">가상자산 납세 포지션</span>을 미리 정비하라.'
        }
    },
    'wKrKPWYUDho': {
        'primary_topic': 'stock',
        'secondary_topics': ['economy'],
        'tags': ['코스닥변곡점', '동전주상장폐지', '코스닥승강제', '영업이익우량주', '연기금수급'],
        'analysis': {
            'summary': '이란 종전 합의와 유가 급락으로 매크로 악재가 해소된 국면에서 코스닥 시장의 변곡점이 임박했다는 진단이 제기되었다. 특히 7월 1일부터 집행되는 <span class="text-rose-400 font-medium">동전주 및 시총 미달 기업 상장폐지</span> 조치와 코스닥 승강제 도입(프라임 지수 구축)은 코스닥 수급 생태계를 전면 재편할 것이다. 연기금이 코스닥에 복귀할 때 단순 고평가된 테마주보다는 실제 실적과 성장률이 뒷받침되는 영업이익 상위 소부장 종목으로 자금이 압축 집중될 전망이다.',
            'key_claims': [
                'WTI 유가의 80달러 이하 하락이 확산 랠리의 트리거가 되어 금리 인하 기대와 함께 코스닥 반등을 이끌 것이다.',
                '7월부터 상장폐지 조건이 대폭 강화되어 좀비 기업들이 정리되며 시장 전반의 <span class="text-cyan-300 font-semibold">건전성 제고 효과</span>가 기대된다.',
                '코스닥 승강제 도입으로 연기금 수급은 밸류에이션 부담이 큰 바이오보다는 실제 이익을 내는 <span class="text-cyan-300 font-semibold">반도체 소부장 대장주</span>로 쏠릴 것이다.'
            ],
            'data_points': [
                '7월 1일부터 동전주 및 시가총액 미달 퇴출 가이드라인 가동',
                '코스닥 프라임 지수 설계 및 연기금 신규 편입 가이드 검토',
                'WTI 국제유가 80달러 전후 지지 흐름에서 80달러 하회 트라이 가능성'
            ],
            'signal': 'bullish',
            'signal_reason': '좀비 기업 정리와 정부 주도의 제도적 수급 개선(승강제, 연기금 복귀)이 우량 코스닥 종목의 강력한 멀티플 재평가를 견인할 것이다.',
            'key_companies': ['에코프로BM'],
            'insight': '코스닥 지수의 단순 밸류에이션 평균은 착시를 유발하므로, 시장의 정화 과정(상폐)과 제도적 수급(프라임 지수)이 겹치는 우량 강소기업으로만 포트폴리오를 슬림화해야 한다.',
            'action_point': '영업이익 퀄리티가 우수하고 이익 성장률이 뚜렷하여 연기금이 매수할 수 있는 <span class="text-cyan-300 font-semibold">우량 코스닥 소부장 탑픽(Top Picks)</span> 위주로 포트폴리오를 집중 재편하라.'
        }
    },
    'xd60MxaPcTg': {
        'primary_topic': 'stock',
        'secondary_topics': ['tech'],
        'tags': ['삼성전자', 'SK하이닉스', '환율하락', '외국인매수폭발', '코스피랠리'],
        'analysis': {
            'summary': '미국과 이란의 평화 협정 타결 소식에 힘입어 원달러 환율이 급격히 내려앉고, 코스피는 대형 반도체주 중심의 외국인 폭발적 수급(1.5조 원 순매수) 유입으로 5% 가까이 앙등했다. 반면 코스닥은 대형 바이오주와 차별화된 흐름을 보이며 0.3% 상승에 그쳤다. 전문가들은 단기 유가 급락에 따른 수혜가 대형 수출주에 먼저 작용하므로 삼성전자와 SK하이닉스의 비중을 굳건히 유지할 것을 당부했다.',
            'key_claims': [
                '중동 지정학적 리스크 소멸로 환율 안정(1,510원대)과 코스피 대장주의 <span class="text-cyan-300 font-semibold">외국인 수급 독식</span> 현상이 심화되고 있다.',
                '코스피는 장중 8,600선을 터치하는 등 초강세이나 코스닥은 수급 분산 부족으로 상대적으로 상승률이 저조하다.',
                '지정학 리스크가 사라져 유가가 안정된 만큼, 비용 하락 수혜와 이익 신뢰도가 가장 큰 <span class="text-cyan-300 font-semibold">삼전/닉스 중심의 대응</span>이 유리하다.'
            ],
            'data_points': [
                '코스피 4.95% 상승 마감, 코스닥 0.35% 마감 (장외 외국인 매수 1.5조 대폭 집중)',
                '상승 종목수 코스피 658개, 코스닥 975개로 확산 분위기 형성',
                '환율 1,510원 수준으로의 하향 안정화 가속'
            ],
            'signal': 'bullish',
            'signal_reason': '대외 거시 악재의 급격한 해소로 환율 하락과 함께 대형 반도체 업종의 이익 추정치가 추가 상향되며 안정적인 랠리가 예상된다.',
            'key_companies': ['삼성전자', 'SK하이닉스', '대한항공', '두산'],
            'insight': '한국 증시의 특성상 해외 유가/환율 매크로 호재가 발생하면 외국인 패시브 자금은 국내 코스닥 중소형주가 아닌 초대형 IT 지수주(삼성전자, SK하이닉스)를 가장 먼저 대량 매수한다.',
            'action_point': '코스닥 소형주의 무리한 단기 물타기 대신 환율 하락의 직접적 수혜를 입고 외국인 패시브 자금이 집중되는 <span class="text-cyan-300 font-semibold">삼성전자 및 SK하이닉스</span> 비중을 안정적으로 유지하라.'
        }
    }
}

def run_process():
    pending_dir = Path("data/pending")
    analyzed_dir = Path("data/analyzed")
    synthesis_dir = Path("data/synthesis")
    
    success_count = 0
    
    for video_id, info in analyses_db.items():
        pending_file = pending_dir / f"{video_id}.json"
        if not pending_file.exists():
            print(f"Skipping: {video_id}.json not found in pending (might have been processed)")
            continue
            
        try:
            # 원본 데이터 로드
            raw_data = json.loads(pending_file.read_text(encoding="utf-8"))
            
            # 새 구조 구성
            analyzed_data = {
                "video": raw_data.get("video", {}),
                "analysis": info["analysis"],
                "classification": {
                    "primary_topic": info["primary_topic"],
                    "secondary_topics": info["secondary_topics"],
                    "tags": info["tags"]
                }
            }
            
            # 대상 폴더 생성 및 저장
            dest_folder = analyzed_dir / info["primary_topic"]
            dest_folder.mkdir(parents=True, exist_ok=True)
            dest_file = dest_folder / f"{video_id}.json"
            dest_file.write_text(json.dumps(analyzed_data, ensure_ascii=False, indent=2), encoding="utf-8")
            
            # pending 파일 삭제
            pending_file.unlink()
            print(f"Processed and deleted: {video_id}.json")
            
            # 관련 synthesis 캐시 파일 삭제
            synth_cache = synthesis_dir / f"{info['primary_topic']}.json"
            if synth_cache.exists():
                synth_cache.unlink()
                print(f"Cleared synthesis cache: {synth_cache.name}")
                
            success_count += 1
        except Exception as e:
            print(f"Error processing {video_id}: {e}")
            
    print(f"Batch execution finished. Successfully processed {success_count} files.")

if __name__ == "__main__":
    run_process()
