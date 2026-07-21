import json
from pathlib import Path

pending_dir = Path("data/pending")
files = [
    "S0f1kzx6Xo0.json",
    "mB2AVGKMJAw.json",
    "MQX9hVbNbeg.json",
    "aubeiTaOkqw.json",
    "BDvajI4kTqQ.json",
    "vR_73S_rDGk.json",
    "I_NcnH7sjHs.json",
    "q-zONq9JzNA.json",
    "28GFiZhKECI.json",
    "hI1AFp1TJDo.json",
    "E8BMnRLZWsQ.json",
    "8p3Jw-GI1UY.json",
    "tyGE1ML_KPg.json"
]

print(f"{'File':<20} | {'Channel':<15} | {'Date':<20} | {'Title'}")
print("-" * 100)
for fn in files:
    path = pending_dir / fn
    if not path.exists():
        print(f"{fn:<20} | NOT FOUND")
        continue
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        video = data.get("video", {})
        # Transcript might be a list of dicts or a string
        transcript = data.get("transcript", "")
        t_len = len(transcript) if isinstance(transcript, str) else len(json.dumps(transcript))
        print(f"{fn:<20} | {video.get('channel_name', 'N/A'):<15} | {video.get('published', 'N/A'):<20} | {video.get('title')} ({t_len} chars)")
    except Exception as e:
        print(f"{fn:<20} | Error: {e}")
