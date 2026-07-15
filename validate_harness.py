import sys
import json
from pathlib import Path
from agents.harness import validate_item

# Set stdout to UTF-8 to avoid encoding errors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    project_root = Path(__file__).resolve().parent
    analyzed_dir = project_root / "data" / "analyzed"
    
    if not analyzed_dir.exists():
        print(f"Error: Analyzed directory {analyzed_dir} does not exist.")
        sys.exit(1)
        
    print(f"Scanning for analyzed JSON files in {analyzed_dir}...\n")
    
    json_files = list(analyzed_dir.glob("**/*.json"))
    total_files = len(json_files)
    valid_count = 0
    invalid_count = 0
    errors_by_file = {}
    
    for json_file in json_files:
        relative_path = json_file.relative_to(project_root)
        try:
            content = json.loads(json_file.read_text(encoding="utf-8"))
            is_valid, errors = validate_item(content, project_root)
            if is_valid:
                valid_count += 1
            else:
                invalid_count += 1
                errors_by_file[str(relative_path)] = errors
        except Exception as e:
            invalid_count += 1
            errors_by_file[str(relative_path)] = [f"Failed to load or parse JSON: {e}"]
            
    print(f"=== Validation Summary ===")
    print(f"Total files checked: {total_files}")
    print(f"Valid files:        {valid_count}")
    print(f"Invalid files:      {invalid_count}")
    print(f"==========================\n")
    
    if invalid_count > 0:
        print("!!! Validation Errors Found !!!")
        for file_path, errors in errors_by_file.items():
            print(f"\n[FAIL] {file_path}")
            for err in errors:
                print(f"  - {err}")
        sys.exit(1)
    else:
        print("[SUCCESS] All analyzed files conform to the constraints and rules!")
        sys.exit(0)

if __name__ == "__main__":
    main()
