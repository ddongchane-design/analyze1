import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.collector import load_seen, fetch_new_videos
import feedparser

channels = json.loads(Path("config/channels.json").read_text(encoding="utf-8"))["channels"]
seen = load_seen()

print(f"Total seen videos in seen_videos.json: {len(seen)}")

for channel in channels[:5]:
    print(f"\n--- Checking channel: {channel['name']} ({channel['id']}) ---")
    print(f"RSS: {channel['rss']}")
    feed = feedparser.parse(channel["rss"])
    print(f"RSS entries count: {len(feed.entries)}")
    if feed.entries:
        for entry in feed.entries[:3]:
            vid = getattr(entry, 'yt_videoid', getattr(entry, 'id', 'N/A'))
            title = getattr(entry, 'title', '')
            print(f"  Entry: {vid} | Title: {title} | In seen: {vid in seen}")
    else:
        print("  RSS returned 0 entries or failed!")
