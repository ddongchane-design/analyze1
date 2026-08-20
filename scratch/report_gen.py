import json, glob, sys
from pathlib import Path

files = glob.glob('data/analyzed/**/*.json', recursive=True)
output = []
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if '자동분석' in data.get('classification', {}).get('tags', []):
                title = data.get('video', {}).get('title', 'No Title')
                topic = data.get('classification', {}).get('primary_topic', 'etc')
                url = data.get('video', {}).get('url', '')
                channel = data.get('video', {}).get('channel_name', 'Unknown')
                summary = data.get('analysis', {}).get('summary', '')
                output.append({
                    'title': title,
                    'topic': topic,
                    'url': url,
                    'channel': channel,
                    'summary': summary
                })
    except Exception as e:
        pass

grouped = {}
for item in output:
    grouped.setdefault(item['topic'], []).append(item)

report_lines = ['# 🚀 8월 17일 신규 수집 및 분석 완료 영상 리포트\n']
report_lines.append('로컬 에이전트 분석(`자동분석`)을 거쳐 각 주제별로 렌더링된 신규 영상 23건의 리스트입니다.\n')

for topic, items in grouped.items():
    report_lines.append(f'## 📌 {topic.upper()} 카테고리 ({len(items)}건)\n')
    for item in items:
        report_lines.append(f'- **[{item["channel"]}]** [{item["title"]}]({item["url"]})')
        report_lines.append(f'  - 요약: {item["summary"]}')
    report_lines.append('\n')

report_content = '\n'.join(report_lines)

# Write to artifact
import os
os.makedirs('C:/Users/yoyo_/.gemini/antigravity-ide/brain/90a5fc5f-94b5-48c0-ad6f-77f8652d2031', exist_ok=True)
with open('C:/Users/yoyo_/.gemini/antigravity-ide/brain/90a5fc5f-94b5-48c0-ad6f-77f8652d2031/analyzed_videos_report.md', 'w', encoding='utf-8') as f:
    f.write(report_content)
    
print("Report generated successfully.")
