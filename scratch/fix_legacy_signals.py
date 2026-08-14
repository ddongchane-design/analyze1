import json
import glob
from pathlib import Path

def fix_signals():
    files = glob.glob("data/analyzed/**/*.json", recursive=True)
    fixed_count = 0
    for fpath in files:
        p = Path(fpath)
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            sig = data.get("analysis", {}).get("signal")
            changed = False
            if sig == "positive":
                data["analysis"]["signal"] = "bullish"
                changed = True
            elif sig == "negative":
                data["analysis"]["signal"] = "bearish"
                changed = True
            
            if changed:
                p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
                fixed_count += 1
        except Exception as e:
            print(f"Error checking {p}: {e}")

    print(f"Fixed {fixed_count} legacy signal values.")

if __name__ == "__main__":
    fix_signals()
