import glob
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def show(start, end):
    files = sorted(glob.glob("scratch/pending_details/*.txt"))
    for f in files[start:end]:
        print("="*60)
        content = Path(f).read_text(encoding="utf-8")
        print(content[:1500])

if __name__ == "__main__":
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    e = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    show(s, e)
