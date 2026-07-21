import json
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).parent.parent))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from agents.etf_processor import process_etf_flows

def main():
    print("=== Testing ETF Flow Processing ===")
    summary = process_etf_flows()
    
    print("\n--- Summary Metadata ---")
    print(f"Status: {summary.get('status')}")
    print(f"Latest Date Folder: {summary.get('latest_date')}")
    print(f"Previous Date Folder: {summary.get('prev_date')}")
    
    print("\n--- Top Accelerations (Flow Momentum) ---")
    for idx, item in enumerate(summary.get("top_accelerations", [])):
        print(f"  {idx+1}. [{item['category'].upper()}] {item['label']} ({item['ticker']})")
        print(f"     1W Flow: {item['w1_amount']} | Prev 1W: {item['w1_amount'] - item['flow_accel']:.4f} | Acceleration: +{item['flow_accel']:.4f}")
        
    print("\n--- Trend Turnarounds ---")
    for idx, item in enumerate(summary.get("turnarounds", [])):
        print(f"  {idx+1}. [{item['category'].upper()}] {item['label']} ({item['ticker']}) -> {item['turnaround']}")
        print(f"     1W Flow: {item['w1_amount']} | Prev 1W: {item['w1_amount'] - item['flow_accel']:.4f}")
        
    print("\n--- By Category Summary ---")
    for cat, etf_list in summary.get("etf_flows_by_category", {}).items():
        print(f"\nCategory: {cat.upper()}")
        for item in etf_list:
            if item.get("status") == "No Data":
                print(f"  - {item['label']} ({item['ticker']}): [NO DATA]")
            else:
                print(f"  - {item['label']} ({item['ticker']}): AUM: {item['aum']:.2f} | 1W Inflow: {item['w1_amount']} | AUM Change Rate: {item['aum_change_rate']:.2f}% | Turnaround: {item['turnaround']}")

if __name__ == "__main__":
    main()
