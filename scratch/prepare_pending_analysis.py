import json
import glob
import os

files = sorted(glob.glob('data/pending/*.json'))
print(f"Total pending: {len(files)}")

batch_size = 6
batches = [files[i:i + batch_size] for i in range(0, len(files), batch_size)]

os.makedirs('scratch/batches', exist_ok=True)

for b_idx, batch in enumerate(batches, 1):
    batch_data = []
    for f in batch:
        vid = os.path.splitext(os.path.basename(f))[0]
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        
        video = d.get('video', {})
        transcript = d.get('transcript', '')
        # 자막이 너무 긴 라이브 방송의 경우 핵심 앞/뒤 및 중요 요약 발췌 (최대 15000자)
        if len(transcript) > 15000:
            condensed = transcript[:8000] + "\n\n[...중략...]\n\n" + transcript[-7000:]
        else:
            condensed = transcript
            
        batch_data.append({
            "id": vid,
            "title": video.get("title", ""),
            "channel_name": video.get("channel_name", ""),
            "published": video.get("published", ""),
            "url": video.get("url", f"https://www.youtube.com/watch?v={vid}"),
            "thumbnail": video.get("thumbnail", f"https://img.youtube.com/vi/{vid}/hqdefault.jpg"),
            "transcript_summary_len": len(transcript),
            "transcript": condensed
        })
    
    out_path = f'scratch/batches/batch_{b_idx}.json'
    with open(out_path, 'w', encoding='utf-8') as fp:
        json.dump(batch_data, fp, ensure_ascii=False, indent=2)
    print(f"Batch {b_idx} created with {len(batch_data)} videos -> {out_path}")
