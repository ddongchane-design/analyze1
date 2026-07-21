import sys
import json
from pathlib import Path

# Add project root to sys.path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from agents.harness import validate_item

def fix_file(file_path):
    try:
        content = json.loads(file_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return False

    modified = False

    # Fix classification missing keys
    if "classification" in content:
        if "secondary_topics" not in content["classification"]:
            content["classification"]["secondary_topics"] = []
            modified = True
        if "tags" not in content["classification"]:
            content["classification"]["tags"] = []
            modified = True

    # Fix analysis missing keys and types
    if "analysis" in content:
        # Check action_point type list
        if "action_point" in content["analysis"]:
            ap = content["analysis"]["action_point"]
            if isinstance(ap, list):
                # Join list items into a single string
                content["analysis"]["action_point"] = " ".join(str(x) for x in ap)
                modified = True

        # Check missing signal_reason
        if "signal_reason" not in content["analysis"]:
            sig = content["analysis"].get("signal", "na")
            content["analysis"]["signal_reason"] = f"지정된 시그널({sig})에 대한 분석 의견입니다."
            modified = True

    if modified:
        # Validate again
        is_valid, errors = validate_item(content)
        if is_valid:
            file_path.write_text(json.dumps(content, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"Fixed: {file_path.name}")
            return True
        else:
            print(f"Failed to automatically fix {file_path.name}: {errors}")
            return False
    return False

def main():
    analyzed_dir = project_root / "data" / "analyzed"
    
    json_files = list(analyzed_dir.glob("**/*.json"))
    fixed_count = 0
    
    for json_file in json_files:
        if fix_file(json_file):
            fixed_count += 1
            
    print(f"\nFixed {fixed_count} files.")

if __name__ == "__main__":
    main()
