import json
import re
from pathlib import Path

def get_valid_topics(project_root=None):
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent
    else:
        project_root = Path(project_root)
        
    topics_file = project_root / "config" / "topics.json"
    if not topics_file.exists():
        # Fallback to default list if config file doesn't exist
        return {"robot", "economy", "tech", "stock", "energy", "crypto", "space", "shipbuilding", "etc"}
        
    try:
        data = json.loads(topics_file.read_text(encoding="utf-8"))
        return {t["id"] for t in data.get("topics", [])}
    except Exception:
        return {"robot", "economy", "tech", "stock", "energy", "crypto", "space", "shipbuilding", "etc"}

def check_html_tags(text):
    """
    Checks if HTML tags in text are properly balanced and closed.
    Returns a list of errors found.
    """
    if not isinstance(text, str):
        return []
        
    # Extract tags (e.g., <span class="..."> or </span>)
    tags = re.findall(r'</?[a-zA-Z0-9_\-\s="\'\.]+>', text)
    stack = []
    errors = []
    
    for tag in tags:
        if tag.startswith('</'):
            tag_name = tag[2:-1].strip().split()[0].lower()
            if not stack:
                errors.append(f"Unexpected closing HTML tag: '{tag}'")
            else:
                last_open = stack.pop()
                if last_open != tag_name:
                    errors.append(f"Mismatched HTML tags: expected </{last_open}>, found {tag}")
        elif tag.endswith('/>'):
            # Self-closing tag
            pass
        else:
            tag_name = tag[1:-1].strip().split()[0].lower()
            # Ignore standard self-closing tags
            if tag_name not in ('br', 'hr', 'img', 'input', 'meta', 'link'):
                stack.append(tag_name)
                
    while stack:
        errors.append(f"Unclosed HTML tag: <{stack.pop()}>")
        
    return errors

def validate_item(item, project_root=None):
    """
    Validates a single analyzed video item against the schema and safety/rule requirements.
    Returns (is_valid, errors_list)
    """
    errors = []
    
    # 1. Check top-level keys
    required_top_keys = {"video", "analysis", "classification"}
    missing_top_keys = required_top_keys - set(item.keys())
    if missing_top_keys:
        errors.append(f"Missing top-level keys: {list(missing_top_keys)}")
        return False, errors
        
    video = item["video"]
    analysis = item["analysis"]
    classification = item["classification"]
    
    # 2. Validate 'video' structure
    required_video_keys = {"id", "title", "published", "channel_name", "url", "thumbnail"}
    missing_video_keys = required_video_keys - set(video.keys())
    if missing_video_keys:
        errors.append(f"Missing keys in 'video': {list(missing_video_keys)}")
        
    for k, v in video.items():
        if k in required_video_keys and not isinstance(v, str):
            errors.append(f"'video.{k}' must be a string, got {type(v).__name__}")
            
    # 3. Validate 'analysis' structure
    required_analysis_keys = {
        "summary", "key_claims", "data_points", "signal", 
        "signal_reason", "key_companies", "insight", "action_point"
    }
    missing_analysis_keys = required_analysis_keys - set(analysis.keys())
    if missing_analysis_keys:
        errors.append(f"Missing keys in 'analysis': {list(missing_analysis_keys)}")
        
    # Check analysis string fields
    string_fields = {"summary", "signal", "signal_reason", "insight", "action_point"}
    for field in string_fields:
        if field in analysis:
            val = analysis[field]
            if not isinstance(val, str):
                errors.append(f"'analysis.{field}' must be a string, got {type(val).__name__}")
            elif not val.strip() and field != "signal_reason":  # signal_reason might be short, but others shouldn't be empty
                errors.append(f"'analysis.{field}' cannot be empty")
            else:
                # Check HTML tag matching
                html_errors = check_html_tags(val)
                for err in html_errors:
                    errors.append(f"HTML error in 'analysis.{field}': {err}")
                
                # Check for markdown block leakage (like ```json or header marks in content)
                if "```" in val:
                    errors.append(f"Potential markdown block leak in 'analysis.{field}': contains '```'")
                if val.strip().startswith("#"):
                    errors.append(f"Potential markdown heading format leak in 'analysis.{field}'")
                    
    # Check analysis list fields
    list_fields = {"key_claims", "data_points", "key_companies"}
    for field in list_fields:
        if field in analysis:
            val = analysis[field]
            if not isinstance(val, list):
                errors.append(f"'analysis.{field}' must be a list, got {type(val).__name__}")
            else:
                for idx, elem in enumerate(val):
                    if not isinstance(elem, str):
                        errors.append(f"'analysis.{field}[{idx}]' must be a string, got {type(elem).__name__}")
                    elif not elem.strip():
                        errors.append(f"'analysis.{field}[{idx}]' cannot be empty")
                    else:
                        html_errors = check_html_tags(elem)
                        for err in html_errors:
                            errors.append(f"HTML error in 'analysis.{field}[{idx}]': {err}")
                        if "```" in elem:
                            errors.append(f"Potential markdown block leak in 'analysis.{field}[{idx}]'")
                            
    # Validate signal value
    if "signal" in analysis:
        allowed_signals = {"bullish", "bearish", "neutral", "na"}
        if analysis["signal"] not in allowed_signals:
            errors.append(f"Invalid signal value '{analysis['signal']}', must be one of {list(allowed_signals)}")

    # 4. Validate 'classification' structure
    required_class_keys = {"primary_topic", "secondary_topics", "tags"}
    missing_class_keys = required_class_keys - set(classification.keys())
    if missing_class_keys:
        errors.append(f"Missing keys in 'classification': {list(missing_class_keys)}")
        
    valid_topics = get_valid_topics(project_root)
    
    if "primary_topic" in classification:
        primary = classification["primary_topic"]
        if primary not in valid_topics:
            errors.append(f"Invalid primary_topic '{primary}', must be one of {list(valid_topics)}")
            
    if "secondary_topics" in classification:
        secondaries = classification["secondary_topics"]
        if not isinstance(secondaries, list):
            errors.append(f"'classification.secondary_topics' must be a list, got {type(secondaries).__name__}")
        else:
            for idx, sec in enumerate(secondaries):
                if sec not in valid_topics:
                    errors.append(f"Invalid secondary_topic '{sec}' at index {idx}, must be one of {list(valid_topics)}")
                    
    if "tags" in classification:
        tags = classification["tags"]
        if not isinstance(tags, list):
            errors.append(f"'classification.tags' must be a list, got {type(tags).__name__}")
        else:
            for idx, tag in enumerate(tags):
                if not isinstance(tag, str):
                    errors.append(f"'classification.tags[{idx}]' must be a string, got {type(tag).__name__}")
                elif not tag.strip():
                    errors.append(f"'classification.tags[{idx}]' cannot be empty")
                    
    return len(errors) == 0, errors
