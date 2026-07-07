from pathlib import Path
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))


def _to_kst_date(pub_str: str) -> str:
    try:
        dt = datetime.fromisoformat(pub_str).astimezone(KST)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return pub_str[:10]


# 토픽별 컬러 팔레트 (kinetic-oracle-hub 스타일)
TOPIC_PALETTE = {
    "robot":        {"color": "cyan",      "hex": "#22d3ee", "emoji": "🤖"},
    "economy":      {"color": "amber",     "hex": "#fbbf24", "emoji": "📊"},
    "tech":         {"color": "indigo",    "hex": "#818cf8", "emoji": "💻"},
    "stock":        {"color": "emerald",   "hex": "#34d399", "emoji": "📈"},
    "energy":       {"color": "orange",    "hex": "#fb923c", "emoji": "⚡"},
    "crypto":       {"color": "fuchsia",   "hex": "#d946ef", "emoji": "🪙"},
    "space":        {"color": "violet",    "hex": "#a78bfa", "emoji": "🚀"},
    "shipbuilding": {"color": "sky",       "hex": "#38bdf8", "emoji": "🚢"},
    "etc":          {"color": "slate",     "hex": "#94a3b8", "emoji": "📰"},
}

SIGNAL_STYLE = {
    "bullish": {"label": "BULLISH", "dot": "#10d98a", "bg": "rgba(16,217,138,0.12)", "border": "rgba(16,217,138,0.35)", "text": "#10d98a"},
    "bearish": {"label": "BEARISH", "dot": "#ff4f72", "bg": "rgba(255,79,114,0.12)", "border": "rgba(255,79,114,0.35)", "text": "#ff4f72"},
    "neutral": {"label": "NEUTRAL", "dot": "#f5c842", "bg": "rgba(245,200,66,0.12)",  "border": "rgba(245,200,66,0.35)",  "text": "#f5c842"},
    "na":      {"label": "N/A",     "dot": "#94a3b8", "bg": "rgba(148,163,184,0.12)", "border": "rgba(148,163,184,0.35)", "text": "#94a3b8"},
}

# ───────────────────────── SHARED HEAD ─────────────────────────

SHARED_HEAD = """
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;800&family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          colors: {
            bg:      "#0b1326",
            surface: "#101931",
            card:    "#16213e",
          }
        }
      }
    }
  </script>
  <style>
    body { font-family: 'Noto Sans KR', sans-serif; }
    .font-manrope { font-family: 'Manrope', sans-serif; }
    .material-symbols-outlined { font-size: inherit; vertical-align: middle; }
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 3px; }
    @media (max-width: 767px) {
      .ch-container-collapsed { display: none !important; }
    }
  </style>
"""

# ───────────────────────── INDEX PAGE ─────────────────────────

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="ko" class="dark">
<head>
  <title>YouTube Insight | Dashboard</title>
  {head}
</head>
<body class="bg-bg text-white min-h-screen relative">

  <!-- Glowing Blobs -->
  <div class="fixed top-[-10%] left-[-10%] w-[40%] h-[40%] bg-purple-500/20 blur-[150px] rounded-full pointer-events-none"></div>
  <div class="fixed bottom-[-10%] right-[-10%] w-[30%] h-[40%] bg-emerald-400/15 blur-[150px] rounded-full pointer-events-none"></div>
  <div class="fixed top-[30%] right-[5%] w-[20%] h-[20%] bg-amber-400/10 blur-[120px] rounded-full pointer-events-none"></div>

  <main class="relative z-10 max-w-[1400px] mx-auto px-8 py-16 flex flex-col items-center">

    <!-- Hero -->
    <div class="text-center mb-16 select-none flex flex-col items-center">
      <div class="flex items-center gap-2 mb-6">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-800/50 border border-slate-700 text-xs font-semibold text-slate-300 tracking-wider">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> SYSTEM ONLINE
        </div>
        <a href="https://kinetic-oracle-main.vercel.app/" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-950/40 border border-purple-800/50 hover:border-purple-500/80 text-xs font-semibold text-purple-300 hover:text-purple-200 transition-all select-none hover:shadow-[0_0_15px_rgba(167,139,250,0.15)]">
          <span class="material-symbols-outlined text-[14px]">home</span> KINETIC ORACLE 홈
        </a>
      </div>
      <h1 class="font-manrope text-5xl md:text-6xl font-extrabold tracking-tighter mb-4 text-transparent bg-clip-text bg-gradient-to-r from-purple-300 via-white to-amber-200 pb-2">
        YouTube Insight
      </h1>
      <p class="text-lg text-slate-400 max-w-xl mx-auto font-light leading-relaxed">
        AI가 유튜브 채널을 실시간 분석해<br>투자 인사이트를 자동으로 추출합니다.
      </p>
    </div>

    {etf_thermometer}

    <!-- Topic Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-5 w-full mb-6">
      {topic_cards}
    </div>

    <p class="text-xs text-slate-600 mt-2">마지막 업데이트: {updated}</p>
  </main>
</body>
</html>"""

INDEX_CARD = """
<a href="{topic_id}.html" class="group relative bg-card/60 backdrop-blur-xl border border-slate-600/40 p-7 rounded-[2rem] flex flex-col transition-all duration-500 hover:-translate-y-2 hover:border-{color}-400/50 hover:shadow-[0_10px_40px_{shadow}]">
  <div class="absolute inset-0 bg-gradient-to-br from-{color}-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-[2rem]"></div>
  <div class="w-14 h-14 rounded-2xl flex items-center justify-center border mb-4 bg-{color}-500/20 text-{color}-400 border-{color}-400/30 shadow-[0_0_15px_{shadow}] text-3xl transition-transform duration-500 group-hover:scale-110">
    <span class="material-symbols-outlined">{icon}</span>
  </div>
  <div class="text-xl font-bold text-slate-100 mb-1 group-hover:text-{color}-300 transition-colors">{emoji} {label}</div>
  <div class="text-slate-400 text-sm font-light flex-grow">{count}개 영상 분석됨</div>
  <div class="mt-5 flex items-center text-sm font-semibold opacity-50 group-hover:opacity-100 transition-all group-hover:translate-x-1 text-{color}-400">
    인사이트 보기 <span class="material-symbols-outlined text-base ml-1">arrow_forward</span>
  </div>
 </a>"""

TOPIC_ICON = {
    "robot": "precision_manufacturing",
    "economy": "query_stats",
    "tech": "memory",
    "stock": "candlestick_chart",
    "energy": "bolt",
    "crypto": "currency_exchange",
    "space": "rocket_launch",
    "shipbuilding": "directions_boat",
    "etc": "newspaper",
}

TOPIC_SHADOW = {
    "robot":        "rgba(34,211,238,0.15)",
    "economy":      "rgba(251,191,36,0.15)",
    "tech":         "rgba(129,140,248,0.15)",
    "stock":        "rgba(52,211,153,0.15)",
    "energy":       "rgba(251,146,60,0.15)",
    "crypto":       "rgba(217,70,239,0.15)",
    "space":        "rgba(167,139,250,0.15)",
    "shipbuilding": "rgba(56,189,248,0.15)",
    "etc":          "rgba(148,163,184,0.15)",
}

# ───────────────────────── TOPIC PAGE ─────────────────────────

TOPIC_TEMPLATE = """<!DOCTYPE html>
<html lang="ko" class="dark">
<head>
  <title>YouTube Insight | {topic_label}</title>
  {head}
</head>
<body class="bg-bg text-white min-h-screen relative">

  <!-- Glowing Blobs -->
  <div class="fixed top-[-10%] left-[-5%] w-[35%] h-[35%] bg-{color}-500/10 blur-[150px] rounded-full pointer-events-none"></div>
  <div class="fixed bottom-[-10%] right-[-5%] w-[25%] h-[35%] bg-purple-500/10 blur-[150px] rounded-full pointer-events-none"></div>

  <!-- Header -->
  <header class="sticky top-0 z-30 bg-bg/80 backdrop-blur-xl border-b border-slate-800/60">
    <div class="max-w-[1400px] mx-auto px-8 py-4 flex items-center justify-between">
      <div class="flex items-center gap-4">
        <a href="index.html" class="flex items-center gap-1 text-sm text-slate-400 hover:text-white transition-colors px-3 py-1.5 rounded-lg border border-slate-700 hover:border-slate-600 bg-slate-800/50">
          <span class="material-symbols-outlined text-base">arrow_back</span> 전체
        </a>
        <div>
          <h1 class="font-manrope text-lg font-bold text-transparent bg-clip-text bg-gradient-to-r from-{color}-300 to-white">
            {emoji} {topic_label}
          </h1>
          <p class="text-xs text-slate-500">AI 분석 인사이트</p>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <a href="https://kinetic-oracle-main.vercel.app/" class="flex items-center gap-1 text-xs text-purple-300 hover:text-purple-200 transition-colors px-3 py-1.5 rounded-lg border border-purple-800/60 hover:border-purple-500 bg-purple-950/40 hover:bg-purple-900/30">
          <span class="material-symbols-outlined text-sm">home</span> KINETIC ORACLE
        </a>
        <span class="text-xs text-slate-600">{updated}</span>
      </div>
    </div>

    <!-- Filter Bar -->
    <div class="max-w-[1400px] mx-auto px-8 pb-3 flex flex-col gap-3">
      <!-- Controls & Signal Filters -->
      <div class="flex items-center justify-between gap-4 flex-wrap w-full">
        <!-- Toggle button on mobile, label on desktop -->
        <div class="flex items-center gap-2">
          <span class="hidden md:inline text-xs text-slate-500 mr-1">채널</span>
          <button id="toggleChBtn" onclick="toggleChannels()" 
            class="md:hidden flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800/40 hover:border-slate-600 text-slate-300 hover:text-white transition-all select-none">
            <span class="material-symbols-outlined text-[16px] leading-none">tune</span>
            <span id="toggleChBtnText">채널 필터 보이기</span>
          </button>
        </div>

        <!-- Right: Signal filters -->
        <div class="flex gap-2">
          <button onclick="filterSig(this,'bullish')" data-sig="bullish"
            class="sig-btn text-[11px] px-3 py-1 rounded-full border border-emerald-500/30 text-emerald-400 hover:bg-emerald-500/15 transition-all">
            ▲ 강세
          </button>
          <button onclick="filterSig(this,'bearish')" data-sig="bearish"
            class="sig-btn text-[11px] px-3 py-1 rounded-full border border-rose-500/30 text-rose-400 hover:bg-rose-500/15 transition-all">
            ▼ 약세
          </button>
          <button onclick="filterSig(this,'neutral')" data-sig="neutral"
            class="sig-btn text-[11px] px-3 py-1 rounded-full border border-amber-500/30 text-amber-400 hover:bg-amber-500/15 transition-all">
            ● 중립
          </button>
          <button onclick="filterSig(this,'na')" data-sig="na"
            class="sig-btn text-[11px] px-3 py-1 rounded-full border border-slate-500/30 text-slate-400 hover:bg-slate-500/15 transition-all">
            ■ N/A
          </button>
        </div>
      </div>

      <!-- Collapsible Channel Filters -->
      <div id="channelContainer" class="ch-container-collapsed flex flex-wrap gap-2 items-center border-t border-slate-800/40 pt-2.5 md:border-none md:pt-0">
        <button onclick="filterCh(this,'all')" data-ch="all"
          class="ch-btn text-xs px-3 py-1 rounded-full border border-{color}-400/50 bg-{color}-500/15 text-{color}-300 font-semibold transition-all">
          전체
        </button>
        {channel_btns}
      </div>
    </div>
  </header>

  <main class="relative z-10 max-w-[1400px] mx-auto px-8 py-10">
    {etf_panel}
    {synthesis}
    <div id="cardGrid" class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-5">
      {cards}
    </div>
    <div id="emptyMsg" class="hidden text-center py-24 text-slate-600">
      <span class="material-symbols-outlined text-5xl mb-3 block opacity-30">inbox</span>
      해당 조건의 영상이 없습니다.
    </div>
  </main>

  <script>
    let activeCh = 'all', activeSig = null;
    function toggleChannels() {{
      const container = document.getElementById('channelContainer');
      const btn = document.getElementById('toggleChBtn');
      const btnText = document.getElementById('toggleChBtnText');
      const isCollapsed = container.classList.contains('ch-container-collapsed');
      
      if (isCollapsed) {{
        container.classList.remove('ch-container-collapsed');
        btn.classList.add('!border-{color}-400/50', '!text-{color}-300', 'bg-{color}-500/15');
        btnText.textContent = '채널 필터 숨기기';
      }} else {{
        container.classList.add('ch-container-collapsed');
        btn.classList.remove('!border-{color}-400/50', '!text-{color}-300', 'bg-{color}-500/15');
        btnText.textContent = '채널 필터 보이기';
      }}
    }}
    function filterCh(btn, ch) {{
      document.querySelectorAll('.ch-btn').forEach(b => b.classList.remove('!bg-{color}-500/15','!border-{color}-400/50','!text-{color}-300','font-semibold'));
      btn.classList.add('font-semibold');
      activeCh = ch; applyFilter();
    }}
    function filterSig(btn, sig) {{
      if (activeSig === sig) {{
        btn.classList.remove('!bg-emerald-500/15','!bg-rose-500/15','!bg-amber-500/15','!bg-slate-500/15');
        activeSig = null;
      }} else {{
        document.querySelectorAll('.sig-btn').forEach(b => b.classList.remove('!bg-emerald-500/15','!bg-rose-500/15','!bg-amber-500/15','!bg-slate-500/15'));
        const map = {{bullish:'!bg-emerald-500/15', bearish:'!bg-rose-500/15', neutral:'!bg-amber-500/15', na:'!bg-slate-500/15'}};
        btn.classList.add(map[sig]);
        activeSig = sig;
      }}
      applyFilter();
    }}
    function applyFilter() {{
      let visible = 0;
      document.querySelectorAll('.insight-card').forEach(c => {{
        const ok = (activeCh==='all'||c.dataset.ch===activeCh) && (!activeSig||c.dataset.sig===activeSig);
        c.style.display = ok ? '' : 'none';
        if (ok) visible++;
      }});
      document.getElementById('emptyMsg').classList.toggle('hidden', visible > 0);
    }}
  </script>
</body>
</html>"""

# ───────────────────────── CARD ─────────────────────────

CARD_TEMPLATE = """
<div class="insight-card group bg-card/60 backdrop-blur-xl border border-slate-700/50 rounded-[1.5rem] p-6 flex flex-col gap-4 transition-all duration-300 hover:-translate-y-1 hover:border-{color}-400/40 hover:shadow-[0_8px_32px_{shadow}] relative overflow-hidden {opacity_class}"
     data-ch="{ch_key}" data-sig="{signal}">
  <div class="absolute inset-0 bg-gradient-to-br from-{color}-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-[1.5rem] pointer-events-none"></div>

  <!-- Top: thumbnail + title + signal -->
  <div class="flex gap-3 items-start">
    <img src="{thumbnail}" class="w-24 h-[60px] rounded-xl object-cover bg-slate-800 flex-shrink-0" onerror="this.style.display='none'">
    <div class="flex-1 min-w-0">
      <h3 class="font-bold text-slate-100 text-[14px] leading-snug line-clamp-2 group-hover:text-{color}-200 transition-colors">{title}</h3>
      <div class="flex items-center gap-2 mt-1.5 flex-wrap">
        <span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-{color}-500/15 text-{color}-300 border border-{color}-400/30">{channel}</span>
        <span class="text-[11px] text-slate-500">{date}</span>
        {etf_badge}
      </div>
    </div>
    <div class="flex-shrink-0">
      <span class="inline-flex items-center gap-1.5 text-[11px] font-bold px-2.5 py-1 rounded-lg border"
        style="background:{sig_bg};color:{sig_text};border-color:{sig_border}">
        <span class="w-1.5 h-1.5 rounded-full" style="background:{sig_dot}"></span>
        {sig_label}
      </span>
    </div>
  </div>

  <!-- Insight -->
  <div class="bg-gradient-to-br from-slate-800/60 to-slate-900/40 border border-slate-700/50 rounded-xl p-4">
    <p class="text-[10px] font-bold tracking-widest text-{color}-400 mb-2 uppercase">Insight</p>
    <p class="text-[13px] text-slate-300 leading-relaxed">{insight}</p>
  </div>

  <!-- Key Claims -->
  <div class="flex flex-col gap-1.5">
    {claims_html}
  </div>

  <!-- Action Point -->
  <div class="bg-amber-400/5 border border-amber-400/20 rounded-xl p-3.5">
    <p class="text-[10px] font-bold tracking-widest text-amber-300 mb-1.5 uppercase">Action Point</p>
    <p class="text-[13px] text-slate-200 leading-relaxed">{action_point}</p>
  </div>

  <!-- Tags + Link -->
  <div class="flex items-center justify-between gap-2 pt-1">
    <div class="flex flex-wrap gap-1.5">{tags_html}</div>
    <a href="{url}" target="_blank"
      class="flex-shrink-0 flex items-center gap-1 text-[12px] font-semibold px-4 py-2 rounded-xl bg-{color}-500/15 hover:bg-{color}-500/25 text-{color}-300 border border-{color}-400/30 hover:border-{color}-400/60 transition-all">
      보기 <span class="material-symbols-outlined text-sm">arrow_forward</span>
    </a>
  </div>
</div>"""

CLAIM_HTML = '<div class="flex items-start gap-2 text-[12px] text-slate-400"><span class="text-slate-600 mt-0.5 flex-shrink-0">▸</span><span>{}</span></div>'
TAG_HTML   = '<span class="px-2 py-0.5 rounded-md text-[10px] bg-slate-800/80 border border-slate-700/60 text-slate-500">{}</span>'


def render_card(video: dict, analysis: dict, classification: dict, etf_flow: list = None) -> str:
    topic_id = classification.get("primary_topic", "tech")
    pal  = TOPIC_PALETTE.get(topic_id, TOPIC_PALETTE["tech"])
    color = pal["color"]
    shadow = TOPIC_SHADOW.get(topic_id, "rgba(129,140,248,0.15)")

    etf_badge = ""
    if etf_flow:
        # Find turnaround or inflow states
        turnaround_etfs = [x for x in etf_flow if x.get("status") == "OK" and x.get("turnaround")]
        inflow_etfs = [x for x in etf_flow if x.get("status") == "OK" and x.get("w1_amount", 0) > 0]
        
        if turnaround_etfs:
            etf_badge = '<span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-amber-500/15 text-amber-300 border border-amber-400/30">🔄 수급 턴어라운드</span>'
        elif inflow_etfs:
            etf_badge = '<span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-500/15 text-emerald-300 border border-emerald-400/30">🟢 자금 유입</span>'
        else:
            etf_badge = '<span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-rose-500/15 text-rose-300 border border-rose-400/30">🔴 자금 유출</span>'

    sig  = analysis.get("signal", "neutral")
    ss   = SIGNAL_STYLE.get(sig, SIGNAL_STYLE["neutral"])

    # signal_confidence 가 low 이면 카드를 흐리게(opacity-60)
    conf = analysis.get("signal_confidence", "high").lower()
    opacity_class = ""
    if conf == "low":
        opacity_class = "opacity-60"
    elif conf == "medium":
        opacity_class = "opacity-85"

    # 시그널 라벨에 신뢰도 표시를 달아줌 (투자 관련이고 신뢰도가 high가 아닐 때 표시해주면 더욱 직관적임)
    sig_label = ss["label"]
    if sig != "na" and conf in ["medium", "low"]:
        conf_kor = "보통" if conf == "medium" else "낮음"
        sig_label = f"{sig_label} ({conf_kor})"

    claims_html = "\n".join(CLAIM_HTML.format(c) for c in analysis.get("key_claims", []))
    tags_html   = "".join(TAG_HTML.format(t)   for t in classification.get("tags", []))

    return CARD_TEMPLATE.format(
        color=color,
        shadow=shadow,
        ch_key=video.get("channel_name", "").replace(" ", "_"),
        signal=sig,
        thumbnail=video.get("thumbnail", ""),
        title=video["title"],
        channel=video["channel_name"],
        date=_to_kst_date(video["published"]),
        url=video["url"],
        sig_bg=ss["bg"], sig_text=ss["text"], sig_border=ss["border"], sig_dot=ss["dot"], sig_label=sig_label,
        insight=analysis.get("insight", ""),
        claims_html=claims_html,
        action_point=analysis.get("action_point", ""),
        tags_html=tags_html,
        opacity_class=opacity_class,
        etf_badge=etf_badge,
    )


CONSENSUS_STYLE = {
    "bullish": {"label": "BULLISH", "color": "#10d98a", "bg": "rgba(16,217,138,0.10)", "border": "rgba(16,217,138,0.30)"},
    "bearish": {"label": "BEARISH", "color": "#ff4f72", "bg": "rgba(255,79,114,0.10)", "border": "rgba(255,79,114,0.30)"},
    "neutral": {"label": "NEUTRAL", "color": "#f5c842", "bg": "rgba(245,200,66,0.10)",  "border": "rgba(245,200,66,0.30)"},
    "na":      {"label": "N/A",     "color": "#94a3b8", "bg": "rgba(148,163,184,0.10)", "border": "rgba(148,163,184,0.30)"},
}

SYNTHESIS_BANNER = """
<div class="mb-8 bg-gradient-to-br from-slate-800/70 to-slate-900/50 border border-{color}-400/25 rounded-2xl p-6">
  <div class="flex items-center gap-3 mb-4 flex-wrap">
    <span class="text-[10px] font-bold tracking-widest text-{color}-400 uppercase">AI 종합 인사이트</span>
    {updated_html}
    <span class="inline-flex items-center gap-1.5 text-[11px] font-bold px-2.5 py-1 rounded-lg border"
      style="background:{cs_bg};color:{cs_color};border-color:{cs_border}">
      <span class="w-1.5 h-1.5 rounded-full" style="background:{cs_color}"></span>
      {cs_label}
    </span>
  </div>
  <p class="text-[13px] text-slate-300 leading-relaxed mb-4">{cross_insight}</p>
  <div class="flex flex-wrap gap-4 text-[12px]">
    <div class="flex-1 min-w-[200px]">
      <p class="text-[10px] font-bold tracking-widest text-slate-500 uppercase mb-2">주요 테마</p>
      <div class="flex flex-wrap gap-1.5">{themes_html}</div>
    </div>
    <div class="flex-1 min-w-[200px]">
      <p class="text-[10px] font-bold tracking-widest text-slate-500 uppercase mb-2">주목 종목/섹터</p>
      <div class="flex flex-wrap gap-1.5">{watchlist_html}</div>
    </div>
  </div>
  {divergence_html}
</div>"""

DIVERGENCE_HTML = '<p class="text-[11px] text-slate-500 mt-3 border-t border-slate-700/50 pt-3">⚡ {divergence}</p>'


def _render_synthesis_banner(synthesis: dict, color: str, updated_at: str = "") -> str:
    if not synthesis:
        return ""
    cs = CONSENSUS_STYLE.get(synthesis.get("consensus", "neutral"), CONSENSUS_STYLE["neutral"])
    themes_html = "".join(
        f'<span class="px-2 py-0.5 rounded-md text-[10px] bg-slate-800/80 border border-slate-700/60 text-slate-400">{t}</span>'
        for t in synthesis.get("key_themes", [])
    )
    watchlist_html = "".join(
        f'<span class="px-2 py-0.5 rounded-md text-[10px] bg-{color}-500/10 border border-{color}-400/30 text-{color}-400">{w}</span>'
        for w in synthesis.get("watch_list", [])
    )
    divergence_html = DIVERGENCE_HTML.format(divergence=synthesis["divergence"]) if synthesis.get("divergence") else ""
    updated_html = f'<span class="text-[10px] text-slate-500 font-light">(업데이트: {updated_at})</span>' if updated_at else ""
    return SYNTHESIS_BANNER.format(
        color=color,
        cs_bg=cs["bg"], cs_color=cs["color"], cs_border=cs["border"], cs_label=cs["label"],
        cross_insight=synthesis.get("cross_insight", ""),
        themes_html=themes_html,
        watchlist_html=watchlist_html,
        divergence_html=divergence_html,
        updated_html=updated_html,
    )


def render_topic_page(topic: dict, cards_html: str, output_dir: Path, channels: list = None, synthesis: dict = None, etf_flow: list = None):
    tid   = topic["id"]
    pal   = TOPIC_PALETTE.get(tid, TOPIC_PALETTE["tech"])
    color = pal["color"]
    emoji = pal["emoji"]

    etf_panel_html = ""
    if etf_flow:
        etf_rows = ""
        for etf in etf_flow:
            if etf.get("status") == "No Data":
                continue
            
            w1 = etf.get("w1_amount", 0)
            flow_acc = etf.get("flow_accel", 0)
            
            w1_formatted = f"+{w1:,.1f}" if w1 > 0 else f"{w1:,.1f}"
            flow_acc_formatted = f"+{flow_acc:,.1f}" if flow_acc > 0 else f"{flow_acc:,.1f}"
            
            flow_acc_color = "text-emerald-400" if flow_acc > 0 else "text-rose-400" if flow_acc < 0 else "text-slate-400"
            w1_color = "text-emerald-400" if w1 > 0 else "text-rose-400" if w1 < 0 else "text-slate-400"
            
            turnaround_badge = ""
            if etf.get("turnaround"):
                turnaround_badge = f'<span class="ml-2 text-[9px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">{etf["turnaround"]}</span>'
                
            aum_change = etf.get("aum_change_rate", 0)
            aum_change_formatted = f"+{aum_change:.2f}%" if aum_change > 0 else f"{aum_change:.2f}%"
            aum_change_color = "text-emerald-400" if aum_change > 0 else "text-rose-400" if aum_change < 0 else "text-slate-400"
            
            etf_rows += f"""
            <div class="flex items-center justify-between py-2 border-b border-slate-700/40 text-xs">
              <div class="flex items-center gap-2">
                <span class="font-bold text-slate-200">{etf['label']}</span>
                <span class="text-slate-500 font-manrope">{etf['ticker']}</span>
                {turnaround_badge}
              </div>
              <div class="flex gap-6 font-manrope">
                <div>AUM: <span class="text-slate-300">{etf['aum']:,.1f}</span> <span class="{aum_change_color} text-[10px]">({aum_change_formatted})</span></div>
                <div>주간 유입: <span class="{w1_color} font-bold">{w1_formatted}</span></div>
                <div>수급 가속도: <span class="{flow_acc_color}">{flow_acc_formatted}</span></div>
              </div>
            </div>
            """
        
        if etf_rows:
            etf_panel_html = f"""
            <div class="mb-6 bg-slate-900/40 border border-slate-700/60 rounded-2xl p-5">
              <div class="flex items-center justify-between mb-3">
                <h4 class="text-xs font-bold tracking-widest text-{color}-400 uppercase flex items-center gap-1.5">
                  <span class="material-symbols-outlined text-[16px]">show_chart</span> 주간 ETF 수급 동향 (Akros 제공)
                </h4>
                <span class="text-[10px] text-slate-500">지표: AUM 및 주간 순유입 변화량</span>
              </div>
              <div class="flex flex-col gap-1">
                {etf_rows}
              </div>
            </div>
            """

    if not cards_html.strip():
        cards_html = ""

    synthesis_path = Path("data/synthesis") / f"{tid}.json"
    updated_at = ""
    if synthesis_path.exists():
        try:
            mtime = synthesis_path.stat().st_mtime
            dt = datetime.fromtimestamp(mtime, KST)
            updated_at = dt.strftime("%Y.%m.%d %H:%M")
        except Exception:
            pass

    synthesis_html = _render_synthesis_banner(synthesis or {}, color, updated_at)

    ch_btns = ""
    if channels:
        for ch in channels:
            key = ch.replace(" ", "_")
            ch_btns += (
                f'<button onclick="filterCh(this,\'{key}\')" data-ch="{key}" '
                f'class="ch-btn text-xs px-3 py-1 rounded-full border border-slate-600 '
                f'text-slate-400 hover:border-{color}-400/50 hover:text-{color}-300 transition-all">'
                f'{ch}</button>\n'
            )

    html = TOPIC_TEMPLATE.format(
        head=SHARED_HEAD,
        topic_label=topic["label"],
        topic_id=tid,
        color=color,
        emoji=emoji,
        etf_panel=etf_panel_html,
        synthesis=synthesis_html,
        cards=cards_html,
        channel_btns=ch_btns,
        updated=datetime.now(KST).strftime("%Y.%m.%d %H:%M"),
    )
    out = output_dir / f"{tid}.html"
    out.write_text(html, encoding="utf-8")
    print(f"  [html] {out}")


def render_index(topics: list, topic_card_counts: dict, topic_last_updates: dict, output_dir: Path, etf_summary: dict = None):
    etf_thermometer = ""
    if etf_summary and etf_summary.get("status") == "OK":
        latest_date = etf_summary.get("latest_date", "")
        prev_date = etf_summary.get("prev_date", "")
        
        # 1. Accelerations
        acc_items = ""
        for idx, item in enumerate(etf_summary.get("top_accelerations", [])):
            acc_items += f"""
            <div class="flex items-center justify-between text-xs py-1.5 border-b border-slate-700/40">
              <span class="text-slate-300 font-semibold">{item['label']}</span>
              <span class="text-emerald-400 font-manrope font-bold">+{item['flow_accel']:,.1f} 가속</span>
            </div>
            """
            
        # 2. Turnarounds
        turn_items = ""
        for idx, item in enumerate(etf_summary.get("turnarounds", [])[:3]):
            color_class = "text-emerald-400" if "Golden" in item['turnaround'] else "text-rose-400"
            symbol = "🔄" if "Golden" in item['turnaround'] else "⚠️"
            turn_items += f"""
            <div class="flex items-center justify-between text-xs py-1.5 border-b border-slate-700/40">
              <span class="text-slate-300 font-semibold">{item['label']}</span>
              <span class="{color_class} font-bold">{symbol} {item['turnaround'].split(' (')[0]}</span>
            </div>
            """
            
        if not acc_items:
            acc_items = '<div class="text-xs text-slate-500 py-4 text-center">가속 테마 없음</div>'
        if not turn_items:
            turn_items = '<div class="text-xs text-slate-500 py-4 text-center">전환 시그널 없음</div>'
            
        date_str = f"({latest_date} vs {prev_date})" if prev_date else f"({latest_date})"
        
        etf_thermometer = f"""
        <!-- ETF Flow Thermometer -->
        <div class="w-full mb-10 bg-gradient-to-br from-slate-900/60 to-slate-950/40 border border-slate-800 rounded-[2rem] p-6 backdrop-blur-xl">
          <div class="flex items-center justify-between mb-4 pb-3 border-b border-slate-800">
            <div class="flex items-center gap-2">
              <span class="material-symbols-outlined text-purple-400">query_stats</span>
              <h2 class="text-base font-bold text-slate-100">주간 글로벌 자금 온도계</h2>
              <span class="text-[10px] text-slate-500 font-manrope">{date_str}</span>
            </div>
            <span class="text-[10px] bg-slate-800 text-slate-400 px-2.5 py-0.5 rounded-full">Akros Flow Engine</span>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- Section 1: Inflow Acceleration -->
            <div>
              <div class="flex items-center gap-1.5 mb-2.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400">수급 모멘텀 가속 (Top 3)</h3>
              </div>
              <div class="flex flex-col">
                {acc_items}
              </div>
            </div>
            
            <!-- Section 2: Trend Turnarounds -->
            <div>
              <div class="flex items-center gap-1.5 mb-2.5">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400">주요 수급 턴어라운드 (Turnarounds)</h3>
              </div>
              <div class="flex flex-col">
                {turn_items}
              </div>
            </div>
          </div>
        </div>
        """
    else:
        msg = etf_summary.get('message', '') if etf_summary else "데이터 준비 중"
        etf_thermometer = f"""
        <!-- ETF Flow Thermometer (Fallback) -->
        <div class="w-full mb-10 bg-slate-900/30 border border-slate-800/80 rounded-[2rem] p-6 text-center">
          <div class="flex items-center justify-center gap-2 text-slate-500 text-xs">
            <span class="material-symbols-outlined text-base animate-pulse">hourglass_empty</span>
            <span>주간 ETF 자금 흐름 데이터 업데이트 대기 중 ({msg})</span>
          </div>
        </div>
        """

    # 가장 최근에 업데이트된 영상 날짜가 있는 순서로 정렬
    sorted_topics = sorted(
        topics,
        key=lambda x: topic_last_updates.get(x["id"], "1970-01-01T00:00:00+00:00"),
        reverse=True
    )

    cards_html = ""
    for t in sorted_topics:
        tid   = t["id"]
        pal   = TOPIC_PALETTE.get(tid, TOPIC_PALETTE["tech"])
        color = pal["color"]
        emoji = pal["emoji"]
        shadow = TOPIC_SHADOW.get(tid, "rgba(129,140,248,0.15)")
        count = topic_card_counts.get(tid, 0)
        cards_html += INDEX_CARD.format(
            topic_id=tid,
            color=color,
            shadow=shadow,
            icon=TOPIC_ICON.get(tid, "circle"),
            emoji=emoji,
            label=t["label"],
            count=count,
        )

    html = INDEX_TEMPLATE.format(
        head=SHARED_HEAD,
        etf_thermometer=etf_thermometer,
        topic_cards=cards_html,
        updated=datetime.now(KST).strftime("%Y.%m.%d %H:%M"),
    )
    out = output_dir / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"  [html] {out}")
