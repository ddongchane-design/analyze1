with open("scratch/temp_batch_formatted.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "=== FILE:" in line:
        print(f"Line {idx+1}: {line.strip()}")
