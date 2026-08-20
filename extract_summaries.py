import os
import json
import re
from pathlib import Path

def clean_transcript(text):
    # Remove caption markings like >> or [laughter]
    text = re.sub(r'>>|\[[^\]]+\]', ' ', text)
    # Normalize spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_key_sentences(text, keywords, max_chars=3000):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    selected = []
    current_len = 0
    
    # Always include first few sentences
    for s in sentences[:3]:
        s_clean = s.strip()
        if s_clean and s_clean not in selected:
            selected.append(s_clean)
            current_len += len(s_clean)
            
    # Include sentences with keywords
    for s in sentences[3:-3]:
        s_clean = s.strip()
        if not s_clean:
            continue
        # Check if any keyword matches
        if any(kw in s_clean for kw in keywords):
            if current_len + len(s_clean) < max_chars:
                selected.append(s_clean)
                current_len += len(s_clean)
            else:
                break
                
    # Include last few sentences
    for s in sentences[-3:]:
        s_clean = s.strip()
        if s_clean and s_clean not in selected:
            if current_len + len(s_clean) < max_chars:
                selected.append(s_clean)
                current_len += len(s_clean)
                
    return " ... ".join(selected)

def main():
    pending_dir = Path("data/pending")
    pending_files = list(pending_dir.glob("*.json"))
    
    if not pending_files:
        print("No pending files.")
        return

    # Load keywords
    topics = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))["topics"]
    all_keywords = []
    for t in topics:
        all_keywords.extend(t.get("keywords", []))
    all_keywords = list(set(all_keywords))
    
    condensed = []
    
    for f in pending_files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            video = data["video"]
            transcript = clean_transcript(data["transcript"])
            
            # Extract key parts
            condensed_text = extract_key_sentences(transcript, all_keywords)
            
            condensed.append({
                "id": video["id"],
                "title": video["title"],
                "channel_name": video["channel_name"],
                "published": video["published"],
                "condensed_transcript": condensed_text
            })
        except Exception as e:
            print(f"Error processing {f.name}: {e}")
            
    scratch_dir = Path("scratch")
    scratch_dir.mkdir(exist_ok=True)
    out_path = scratch_dir / "condensed_transcripts.json"
    out_path.write_text(json.dumps(condensed, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Successfully wrote {len(condensed)} condensed transcripts to {out_path}")

if __name__ == "__main__":
    main()
