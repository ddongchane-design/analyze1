import json
from pathlib import Path
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pending_files = [
    "SPXhamNPf6Q.json",
    "KdLZthSQ_kA.json",
    "aaDNXBXXOH0.json",
    "EboqEWatLV8.json",
    "pcx-b_l2bQQ.json",
    "QeT-DeK5L2c.json",
    "ujT_gtB4lRA.json",
    "qQi3skDY6ns.json",
    "AxXsOzux7zQ.json",
    "ooyhI2HDUY8.json"
]

for filename in pending_files:
    filepath = Path("data/pending") / filename
    if filepath.exists():
        data = json.loads(filepath.read_text(encoding="utf-8"))
        print(f'"{filename.split(".")[0]}": {json.dumps(data.get("video", {}), ensure_ascii=False)},')
    else:
        print(f'"{filename.split(".")[0]}": NOT FOUND')
