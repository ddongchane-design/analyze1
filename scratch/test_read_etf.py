import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def check_file(filepath, search_tickers):
    if not filepath.exists():
        print(f"File not found: {filepath}")
        return
        
    try:
        content = json.loads(filepath.read_text(encoding="utf-8"))
        data_list = content.get("data", [])
        print(f"\n--- Checking {filepath.name} (Total items: {len(data_list)}) ---")
        
        found = []
        for item in data_list:
            ticker = item.get("Ticker", "").upper()
            name = item.get("Name", "")
            # check if ticker or parts of name match our search
            if any(t in ticker for t in search_tickers) or any(t in name.upper() for t in search_tickers):
                found.append(item)
                
        print(f"Found {len(found)} matches:")
        for idx, item in enumerate(found[:25]):
            print(f"  {idx+1:02d}. ID: {item.get('ID')} | Ticker: {item.get('Ticker')} | AUM: {item.get('AUM')} | 1W Amount: {item.get('1W Amount')} | Name: {item.get('Name')}")
            
    except Exception as e:
        print(f"Error reading {filepath.name}: {e}")

def main():
    akros_dir = Path("akros/26.07.06")
    
    # Let's search for interesting words/tickers in Korean file
    kr_search = ["SHIPBUILDING", "조선", "ROBOT", "로봇", "SEMICONDUCTOR", "반도체", "ELECTRICITY", "전력", "DEFENSE", "방산"]
    check_file(akros_dir / "aum-flow kr.json", kr_search)
    
    # Let's search for interesting tickers in US file
    us_search = ["SOXX", "SMH", "IBIT", "FBTC", "GLD", "SPY", "QQQ", "TLT", "XLU", "XLE", "BOTZ", "ARKX", "ITA", "IBB", "XBI"]
    check_file(akros_dir / "aum-flow us.json", us_search)

if __name__ == "__main__":
    main()
