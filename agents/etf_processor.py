import json
import re
import sys
from pathlib import Path
from datetime import datetime

# Configure UTF-8 stdout if needed
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def parse_date_dir(dir_name):
    """
    Parses a directory name like '26.6.16' or '26.07.06' into a datetime object.
    Assumes 2000s for YY.
    """
    match = re.match(r'^(\d+)\.(\d+)\.(\d+)$', dir_name)
    if not match:
        return None
    try:
        year = int(match.group(1)) + 2000
        month = int(match.group(2))
        day = int(match.group(3))
        return datetime(year, month, day)
    except ValueError:
        return None

def load_etf_data_from_dir(dir_path):
    """
    Loads US and KR ETF flow data from a specific date directory.
    Returns a dict mapping Ticker -> ETF data dictionary.
    """
    etfs = {}
    
    # Try both possible naming conventions (spaces/hyphens or underscores)
    kr_files = [dir_path / "aum-flow kr.json", dir_path / "aum_flow_kr.json"]
    kr_file = next((f for f in kr_files if f.exists()), None)
    if kr_file:
        try:
            content = json.loads(kr_file.read_text(encoding="utf-8"))
            for item in content.get("data", []):
                ticker = item.get("Ticker", "").upper().strip()
                if ticker:
                    item["market"] = "kr"
                    etfs[ticker] = item
        except Exception as e:
            print(f"  [warn] Error reading KR AUM file in {dir_path.name}: {e}")
            
    us_files = [dir_path / "aum-flow us.json", dir_path / "aum_flow_us.json"]
    us_file = next((f for f in us_files if f.exists()), None)
    if us_file:
        try:
            content = json.loads(us_file.read_text(encoding="utf-8"))
            for item in content.get("data", []):
                ticker = item.get("Ticker", "").upper().strip()
                if ticker:
                    item["market"] = "us"
                    etfs[ticker] = item
        except Exception as e:
            print(f"  [warn] Error reading US AUM file in {dir_path.name}: {e}")
            
    return etfs

def process_etf_flows():
    """
    Main entry point to scan akros/ directories, calculate changes, and save etf_flows.json.
    """
    akros_path = Path("akros")
    if not akros_path.exists():
        print("  [info] 'akros' directory does not exist. Skipping ETF flow processing.")
        return get_empty_summary("akros 폴더 없음")
        
    # Scan date directories
    date_dirs = []
    for p in akros_path.iterdir():
        if p.is_dir():
            dt = parse_date_dir(p.name)
            if dt:
                date_dirs.append((dt, p))
                
    # Sort chronologically
    date_dirs.sort(key=lambda x: x[0])
    
    if not date_dirs:
        print("  [info] No valid date directories found inside 'akros/'. Skipping ETF flow processing.")
        return get_empty_summary("데이터 준비 중")
        
    latest_dt, latest_dir = date_dirs[-1]
    prev_dt, prev_dir = None, None
    if len(date_dirs) >= 2:
        prev_dt, prev_dir = date_dirs[-2]
        
    print(f"  [etf] Processing latest date: {latest_dir.name} (compared to {prev_dir.name if prev_dir else 'None'})")
    
    latest_data = load_etf_data_from_dir(latest_dir)
    prev_data = load_etf_data_from_dir(prev_dir) if prev_dir else {}
    
    # Load ETF mapping configuration
    mapping_file = Path("config/etf_mapping.json")
    if not mapping_file.exists():
        print("  [warn] 'config/etf_mapping.json' not found. Skipping ETF flow processing.")
        return get_empty_summary("맵핑 설정 파일 없음")
        
    try:
        mapping = json.loads(mapping_file.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  [warn] Failed to parse etf_mapping.json: {e}")
        return get_empty_summary("맵핑 파일 파싱 에러")
        
    etf_flows_by_category = {}
    all_processed_etfs = []
    
    for category, etf_list in mapping.items():
        category_etfs = []
        for etf_info in etf_list:
            ticker = etf_info["ticker"].upper().strip()
            label = etf_info["label"]
            
            # Find item in latest
            item = latest_data.get(ticker)
            if not item:
                # Try prefix match if ticker was mapped slightly differently (e.g. removing KS suffix)
                item = next((v for k, v in latest_data.items() if k.startswith(ticker)), None)
                
            if not item:
                # Graceful degradation if data is missing for a specific ticker
                category_etfs.append({
                    "ticker": ticker,
                    "label": label,
                    "market": etf_info["market"],
                    "status": "No Data"
                })
                continue
                
            aum = item.get("AUM")
            w1_amount = item.get("1W Amount")
            m1_amount = item.get("1M Amount")
            ytd_amount = item.get("YTD Amount")
            
            # Look up in previous data
            prev_item = prev_data.get(ticker)
            if not prev_item:
                prev_item = next((v for k, v in prev_data.items() if k.startswith(ticker)), None)
                
            # Default comparison values
            aum_change = 0
            aum_change_rate = 0
            flow_accel = 0
            turnaround = None
            
            if prev_item:
                prev_aum = prev_item.get("AUM")
                prev_w1 = prev_item.get("1W Amount")
                
                # AUM Change calculations
                if aum is not None and prev_aum is not None:
                    aum_change = aum - prev_aum
                    if prev_aum > 0:
                        aum_change_rate = (aum_change / prev_aum) * 100
                        
                # Flow Acceleration
                if w1_amount is not None and prev_w1 is not None:
                    flow_accel = w1_amount - prev_w1
                    
                    # Turnaround logic (direction change)
                    if prev_w1 <= 0 and w1_amount > 0:
                        turnaround = "Golden Cross (Inflow)"
                    elif prev_w1 >= 0 and w1_amount < 0:
                        turnaround = "Dead Cross (Outflow)"
            
            processed = {
                "ticker": ticker,
                "label": label,
                "market": item.get("market"),
                "status": "OK",
                "aum": aum,
                "w1_amount": w1_amount,
                "m1_amount": m1_amount,
                "ytd_amount": ytd_amount,
                "aum_change": aum_change,
                "aum_change_rate": aum_change_rate,
                "flow_accel": flow_accel,
                "turnaround": turnaround
            }
            category_etfs.append(processed)
            
            # Keep flat list for global calculations
            all_processed_etfs.append({
                "ticker": ticker,
                "label": label,
                "category": category,
                **processed
            })
            
        etf_flows_by_category[category] = category_etfs
        
    # Calculate global indicators: Top 3 Inflow Accelerations
    accelerations = [x for x in all_processed_etfs if x.get("status") == "OK" and x.get("flow_accel", 0) > 0]
    accelerations.sort(key=lambda x: x["flow_accel"], reverse=True)
    top_accel = accelerations[:3]
    
    # Calculate global indicators: Turnarounds (Golden Crosses & Dead Crosses)
    turnarounds = [x for x in all_processed_etfs if x.get("status") == "OK" and x.get("turnaround") is not None]
    
    summary = {
        "status": "OK",
        "latest_date": latest_dir.name,
        "prev_date": prev_dir.name if prev_dir else None,
        "etf_flows_by_category": etf_flows_by_category,
        "top_accelerations": top_accel,
        "turnarounds": turnarounds
    }
    
    # Save cache
    dest_path = Path("data/synthesis/etf_flows.json")
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        dest_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  [etf] Saved ETF flow summary to {dest_path}")
    except Exception as e:
        print(f"  [warn] Failed to save etf_flows.json: {e}")
        
    return summary

def get_empty_summary(message):
    """
    Returns a blank fallback summary structure.
    """
    return {
        "status": "Fallback",
        "message": message,
        "latest_date": "N/A",
        "prev_date": None,
        "etf_flows_by_category": {},
        "top_accelerations": [],
        "turnarounds": []
    }

if __name__ == "__main__":
    process_etf_flows()
