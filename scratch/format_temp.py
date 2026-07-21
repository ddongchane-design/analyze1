import re

with open("scratch/temp_batch.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Replace spaces with newlines every 10-15 words, or split by sentence ending
# Let's split by sentence endings like "다.", "요.", "오.", "죠." etc.
formatted = re.sub(r'([다요오죠가나다라마바사아자차카타파하]\. )', r'\1\n', text)
formatted = re.sub(r'(=== FILE:.*)', r'\n\n\1\n', formatted)

with open("scratch/temp_batch_formatted.txt", "w", encoding="utf-8") as f:
    f.write(formatted)

print("Formatted successfully!")
