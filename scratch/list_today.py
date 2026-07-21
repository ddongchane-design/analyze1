import json
import os

vids = [
    '36JHK2Vgf_w', '7Uz31gVk2l4', 'AAai38w84vc', 'b06GM7Ok1io', 'fphU6tzjVMM',
    'JMAjoOff_TY', 'jNK_51QDdDU', 'l5oQymvTPlo', 'LAmPHgjxtbE', 'mcncFNbnRAU',
    'S79MSyBVamY', 'xk35tWdAH0U', 'YnNDYCyBmiA', '_WNu3oWA--M'
]

topics = ['economy', 'tech', 'stock', 'etc', 'robot']

with open("scratch/list_today.md", "w", encoding="utf-8") as out:
    out.write("# 6월 7일 분석한 유튜브 영상 리스트 (총 14개)\n\n")
    out.write("| 발행일 | 채널 | 제목 |\n")
    out.write("|---|---|---|\n")
    for vid in vids:
        for topic in topics:
            p = f"data/analyzed/{topic}/{vid}.json"
            if os.path.exists(p):
                with open(p, encoding='utf-8') as f:
                    data = json.load(f)
                    video = data['video']
                    out.write(f"| {video['published'][:10]} | {video['channel_name']} | {video['title']} |\n")
                break
