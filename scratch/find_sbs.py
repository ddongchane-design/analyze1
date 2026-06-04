import re

with open(r'C:\Users\ddong\.gemini\antigravity-ide\brain\f9b0a817-ffc7-4599-914f-9f294b90d74c\.system_generated\steps\284\content.md', encoding='utf-8') as f:
    text = f.read()

# 1. Canonical URL
canon = re.findall(r'canonical.*?channel/([^"\']+)', text)
print("Canonical ID:", canon)

# 2. External ID
external = re.findall(r'externalId["\']\s*:\s*["\']([^"\']+)', text)
print("External ID:", external)

# 3. Browse ID
browse = re.findall(r'browseId["\']\s*:\s*["\'](UC[^"\']+)', text)
print("Browse ID:", set(browse))

# 4. Search for UC followed by 22 chars near the word "sbs" or "explained"
for m in re.finditer(r'UC[a-zA-Z0-9_-]{22}', text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 50)
    context = text[start:end].replace('\n', ' ')
    if 'sbs' in context.lower() or 'explained' in context.lower():
        print(f"Match context for {m.group()}: ... {context} ...")
