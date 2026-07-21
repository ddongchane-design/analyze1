import pathlib
import json

def verify_json_files():
    data_dir = pathlib.Path("data")
    print(f"Scanning JSON files in {data_dir.resolve()}...")
    
    json_files = list(data_dir.rglob("*.json"))
    print(f"Found {len(json_files)} JSON files.")
    
    corrupted_files = []
    for file_path in json_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as e:
            corrupted_files.append((file_path, e))
            
    if corrupted_files:
        print("\n[!] Found corrupted/invalid JSON files:")
        for path, err in corrupted_files:
            print(f"  - {path}: {err}")
    else:
        print("\n[v] All JSON files are valid! No corruption found.")

if __name__ == "__main__":
    verify_json_files()
