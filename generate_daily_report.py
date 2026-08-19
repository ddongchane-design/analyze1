import os
import json
from pathlib import Path
from datetime import datetime

def main():
    base_dir = Path(__file__).parent.resolve()
    analyzed_dir = base_dir / "data" / "analyzed"
    synthesis_dir = base_dir / "data" / "synthesis"

    today_str = datetime.now().strftime("%Y-%m-%d")
    report_dir = base_dir / "output" / "daily_reports" / today_str
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"{today_str}_executive_summary.html"

    topic_meta = {
        "stock": {"name": "주식 & 증시 매크로", "icon": "📈"},
        "economy": {"name": "거시 경제 & 통화 정책", "icon": "🏛️"},
        "tech": {"name": "테크, AI & 반도체", "icon": "💻"},
        "robot": {"name": "피지컬 AI & 로봇", "icon": "🤖"},
        "space": {"name": "우주 항공 & 위성", "icon": "🚀"},
        "energy": {"name": "에너지 & 전력 인프라", "icon": "⚡"},
        "crypto": {"name": "크립토 & RWA", "icon": "🪙"},
        "etc": {"name": "기타 & 과학 교양", "icon": "🌐"}
    }

    synthesis_data = {}
    for syn_file in synthesis_dir.glob("*.json"):
        if syn_file.name == "etf_flows.json":
            continue
        topic_id = syn_file.stem
        try:
            synthesis_data[topic_id] = json.loads(syn_file.read_text(encoding="utf-8"))
        except Exception:
            pass

    topic_videos = {t: [] for t in topic_meta.keys()}
    all_videos_list = []

    for topic_folder in analyzed_dir.iterdir():
        if topic_folder.is_dir():
            topic_id = topic_folder.name
            if topic_id not in topic_videos:
                topic_videos[topic_id] = []
                
            for v_file in topic_folder.glob("*.json"):
                try:
                    v_data = json.loads(v_file.read_text(encoding="utf-8"))
                    topic_videos[topic_id].append(v_data)
                    all_videos_list.append(v_data)
                except Exception:
                    pass

    # Sort videos by published date descending
    for t in topic_videos:
        topic_videos[t].sort(key=lambda x: x.get("video", {}).get("published", ""), reverse=True)

    total_videos = len(all_videos_list)
    bullish_count = sum(1 for v in all_videos_list if v.get("analysis", {}).get("signal") == "bullish")
    neutral_count = sum(1 for v in all_videos_list if v.get("analysis", {}).get("signal") == "neutral")
    bearish_count = sum(1 for v in all_videos_list if v.get("analysis", {}).get("signal") == "bearish")

    html_content = f"""<!DOCTYPE html>
<html lang="ko" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>일일 브리핑 리포트 ({today_str})</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        heading: ['Outfit', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ background-color: #0b0f17; color: #f1f5f9; font-family: 'Inter', sans-serif; font-size: 16px; line-height: 1.6; }}
        .glass-card {{ background: rgba(21, 29, 42, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); }}
        .glass-nav {{ background: rgba(11, 15, 23, 0.95); backdrop-filter: blur(16px); border-bottom: 1px solid rgba(255, 255, 255, 0.1); }}
        .gradient-text {{ background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
        ::-webkit-scrollbar-track {{ background: #0b0f17; }}
        ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 4px; }}
    </style>
</head>
<body class="min-h-screen text-slate-100">

    <header class="sticky top-0 z-50 glass-nav px-6 py-4">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="flex items-center space-x-3">
                <div class="w-11 h-11 rounded-xl bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center text-white font-bold text-xl shadow-lg shadow-cyan-500/20">
                    YI
                </div>
                <div>
                    <h1 class="text-xl font-bold font-heading text-white flex items-center gap-2">
                        YouTube Insight <span class="gradient-text font-extrabold">통합 브리핑</span>
                    </h1>
                    <p class="text-sm text-slate-400">보고서 생성 일자: <span class="text-cyan-400 font-semibold">{today_str}</span> (가독성 향상 대형 폰트 버전)</p>
                </div>
            </div>

            <nav class="flex items-center space-x-1.5 overflow-x-auto py-1 text-sm font-medium">
                <a href="#overview" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-100 whitespace-nowrap">📊 종합 인사이트</a>
                <a href="#stock" class="px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-emerald-950 hover:text-emerald-300 text-slate-200 whitespace-nowrap">📈 증시/매크로</a>
                <a href="#tech" class="px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-cyan-950 hover:text-cyan-300 text-slate-200 whitespace-nowrap">💻 테크/AI</a>
                <a href="#robot" class="px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-violet-950 hover:text-violet-300 text-slate-200 whitespace-nowrap">🤖 로봇</a>
                <a href="#space" class="px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-amber-950 hover:text-amber-300 text-slate-200 whitespace-nowrap">🚀 우주</a>
                <a href="#energy" class="px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-orange-950 hover:text-orange-300 text-slate-200 whitespace-nowrap">⚡ 에너지</a>
                <a href="#crypto" class="px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-indigo-950 hover:text-indigo-300 text-slate-200 whitespace-nowrap">🪙 크립토</a>
                <a href="#etc" class="px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-200 whitespace-nowrap">🌐 기타</a>
            </nav>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 md:px-8 py-8 space-y-12">

        <!-- Hero Stats Banner -->
        <section id="overview" class="glass-card rounded-2xl p-6 md:p-8 relative overflow-hidden">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                <div class="space-y-2.5 max-w-3xl">
                    <span class="inline-block px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 text-sm font-semibold">
                        ⚡ 가독성 최적화 종합 리포트
                    </span>
                    <h2 class="text-2xl md:text-3xl font-extrabold text-white font-heading tracking-tight">
                        섹터별 동향 & 종합 인사이트 (대형 뷰어)
                    </h2>
                    <p class="text-base text-slate-300 leading-relaxed">
                        한눈에 편안하게 읽으실 수 있도록 **본문 글자 크기, 가독성 색상 대비, 카드 여백을 대폭 확대**하였습니다. 전 섹터 종합 시장 인사이트와 비디오 분석 카드를 편리하게 감상하세요.
                    </p>
                </div>

                <div class="grid grid-cols-4 gap-3 text-center min-w-fit">
                    <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4">
                        <span class="text-xs text-slate-400 font-semibold block mb-1">총 비디오</span>
                        <span class="text-2xl font-black text-white">{total_videos}</span>
                    </div>
                    <div class="bg-emerald-950/50 border border-emerald-800/50 rounded-xl p-4">
                        <span class="text-xs text-emerald-400 font-semibold block mb-1">강세</span>
                        <span class="text-2xl font-black text-emerald-400">{bullish_count}</span>
                    </div>
                    <div class="bg-amber-950/50 border border-amber-800/50 rounded-xl p-4">
                        <span class="text-xs text-amber-400 font-semibold block mb-1">중립</span>
                        <span class="text-2xl font-black text-amber-400">{neutral_count}</span>
                    </div>
                    <div class="bg-rose-950/50 border border-rose-800/50 rounded-xl p-4">
                        <span class="text-xs text-rose-400 font-semibold block mb-1">약세</span>
                        <span class="text-2xl font-black text-rose-400">{bearish_count}</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- PART 1: Synthesis Overview Matrix -->
        <section class="space-y-6">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <h3 class="text-2xl font-extrabold text-white font-heading flex items-center gap-2">
                    <span>🧠</span> 섹터별 종합 인사이트 (Synthesis Summary)
                </h3>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
"""

    for t_id, meta in topic_meta.items():
        syn = synthesis_data.get(t_id, {})
        if not syn:
            continue
        
        consensus = syn.get("consensus", "neutral")
        c_badge = {
            "bullish": '<span class="px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/20 border border-emerald-500/40 text-emerald-300">🟢 강세 (Bullish)</span>',
            "neutral": '<span class="px-3 py-1 rounded-full text-xs font-bold bg-amber-500/20 border border-amber-500/40 text-amber-300">🟡 중립 (Neutral)</span>',
            "bearish": '<span class="px-3 py-1 rounded-full text-xs font-bold bg-rose-500/20 border border-rose-500/40 text-rose-300">🔴 약세 (Bearish)</span>'
        }.get(consensus, '<span class="px-3 py-1 rounded-full text-xs font-bold bg-slate-800 text-slate-300">중립</span>')

        cross_insight = syn.get("cross_insight", "내용 없음")
        divergence = syn.get("divergence", "")
        key_themes = syn.get("key_themes", [])
        watch_list = syn.get("watch_list", [])

        themes_html = "".join([f'<li class="text-sm text-slate-200 flex items-start gap-2"><span class="text-cyan-400 font-bold">•</span><span>{th}</span></li>' for th in key_themes[:3]])
        watch_html = "".join([f'<li class="text-sm text-slate-300 flex items-start gap-2"><span class="text-purple-400 font-bold">🔍</span><span>{w}</span></li>' for w in watch_list[:2]])

        html_content += f"""
                <div class="glass-card rounded-2xl p-6 space-y-4 flex flex-col justify-between hover:border-slate-600 transition-all">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                            <h4 class="text-lg font-bold text-white flex items-center gap-2">
                                <span>{meta["icon"]}</span> {meta["name"]}
                            </h4>
                            {c_badge}
                        </div>

                        <div>
                            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-1.5">💡 종합 인사이트</span>
                            <p class="text-sm text-slate-100 leading-relaxed font-normal bg-slate-900/80 p-3.5 rounded-xl border border-slate-800">
                                {cross_insight}
                            </p>
                        </div>

                        {f'''<div>
                            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1.5">⚖️ 시장 이견 및 시각 차이</span>
                            <p class="text-sm text-slate-200 leading-relaxed italic bg-amber-950/30 p-3 rounded-xl border border-amber-800/30">
                                {divergence}
                            </p>
                        </div>''' if divergence else ''}

                        <div>
                            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1.5">📌 핵심 테마</span>
                            <ul class="space-y-1.5">
                                {themes_html}
                            </ul>
                        </div>
                    </div>

                    <div class="border-t border-slate-800 pt-3 mt-2">
                        <span class="text-xs font-bold text-purple-400 uppercase tracking-wider block mb-1.5">👀 관전 포인트</span>
                        <ul class="space-y-1.5">
                            {watch_html}
                        </ul>
                    </div>
                </div>
"""

    html_content += """
            </div>
        </section>

        <!-- PART 2: Sector-by-Sector Video Analysis Cards -->
        <section class="space-y-12">
            <div class="border-t border-slate-800 pt-8">
                <h3 class="text-2xl font-extrabold text-white font-heading flex items-center gap-2">
                    <span>🎬</span> 섹터별 분석 비디오 카드 (상세보기)
                </h3>
            </div>
"""

    for t_id, meta in topic_meta.items():
        videos = topic_videos.get(t_id, [])
        if not videos:
            continue

        display_videos = videos[:12]

        html_content += f"""
            <div id="{t_id}" class="space-y-6 scroll-mt-24">
                <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                    <h4 class="text-xl font-extrabold text-white flex items-center gap-2.5 font-heading">
                        <span class="text-2xl">{meta["icon"]}</span>
                        <span>{meta["name"]}</span>
                        <span class="text-xs font-semibold text-slate-300 bg-slate-800 px-3 py-1 rounded-full">최근 {len(display_videos)}개 분석</span>
                    </h4>
                    <a href="#overview" class="text-sm text-cyan-400 font-semibold hover:text-cyan-300">Top ▲</a>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
"""

        for v in display_videos:
            v_info = v.get("video", {})
            analysis = v.get("analysis", {})

            title = v_info.get("title", "제목 없음")
            channel = v_info.get("channel_name", "채널 미상")
            pub_date = v_info.get("published", "")[:10]
            url = v_info.get("url", "#")

            signal = analysis.get("signal", "neutral")
            s_badge = {
                "bullish": '<span class="px-2.5 py-1 rounded-lg text-xs font-extrabold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">🟢 Bullish</span>',
                "neutral": '<span class="px-2.5 py-1 rounded-lg text-xs font-extrabold bg-amber-500/20 text-amber-300 border border-amber-500/40">🟡 Neutral</span>',
                "bearish": '<span class="px-2.5 py-1 rounded-lg text-xs font-extrabold bg-rose-500/20 text-rose-300 border border-rose-500/40">🔴 Bearish</span>'
            }.get(signal, '<span class="px-2.5 py-1 rounded-lg text-xs font-extrabold bg-slate-800 text-slate-300">Neutral</span>')

            summary_html = analysis.get("summary", "")
            key_claims = analysis.get("key_claims", [])
            claims_html = "".join([f'<li class="text-sm text-slate-200 leading-relaxed flex items-start gap-2"><span class="text-cyan-400 font-bold">•</span><div>{c}</div></li>' for c in key_claims])
            
            companies = analysis.get("key_companies", [])
            companies_html = "".join([f'<span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-200 border border-slate-700 text-xs font-medium">{c}</span>' for c in companies])

            insight_text = analysis.get("insight", "")
            action_text = analysis.get("action_point", "")

            html_content += f"""
                    <div class="glass-card rounded-2xl p-6 space-y-4 flex flex-col justify-between hover:border-slate-600 transition-all">
                        <div class="space-y-3.5">
                            <div class="flex items-start justify-between gap-3">
                                <div class="space-y-1">
                                    <div class="flex items-center gap-2">
                                        <span class="px-2.5 py-0.5 rounded-full bg-slate-800 text-cyan-400 font-bold text-xs">{channel}</span>
                                        <span class="text-xs text-slate-400">{pub_date}</span>
                                    </div>
                                    <h5 class="text-base font-bold text-white leading-snug hover:text-cyan-300">
                                        <a href="{url}" target="_blank" rel="noopener noreferrer">{title}</a>
                                    </h5>
                                </div>
                                {s_badge}
                            </div>

                            <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800 text-sm text-slate-100 leading-relaxed">
                                {summary_html}
                            </div>

                            <div class="space-y-2">
                                <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block">🔑 핵심 분석 내용</span>
                                <ul class="space-y-2">
                                    {claims_html}
                                </ul>
                            </div>
                        </div>

                        <div class="space-y-3 pt-3 border-t border-slate-800">
                            {f'''<div class="flex flex-wrap items-center gap-1.5">
                                <span class="text-xs text-slate-400 font-semibold mr-1">연관 기업:</span>
                                {companies_html}
                            </div>''' if companies else ''}

                            {f'''<div class="bg-emerald-950/30 border border-emerald-800/40 p-3.5 rounded-xl">
                                <span class="text-xs font-bold text-emerald-400 block mb-1">💡 투자 인사이트 & 전략</span>
                                <p class="text-sm text-emerald-100 leading-relaxed">{action_text or insight_text}</p>
                            </div>''' if action_text or insight_text else ''}
                        </div>
                    </div>
"""

        html_content += """
                </div>
            </div>
"""

    html_content += f"""
        </section>

        <footer class="border-t border-slate-800 pt-8 pb-12 text-center text-sm text-slate-400 space-y-1">
            <p>Generated by Antigravity Agent • Single Page Executive Report (Large Font Edition)</p>
            <p>File Path: {report_file}</p>
        </footer>

    </main>

</body>
</html>
"""

    report_file.write_text(html_content, encoding="utf-8")
    print(f"[SUCCESS] High-readability executive report created:\n{report_file}")

if __name__ == "__main__":
    main()
