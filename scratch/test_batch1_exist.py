from pathlib import Path
video_ids = ["-ADB_o6C2ig", "-LUnTYx_xAA", "08Lrl4ijgS4", "1Q2XkHeNrIk", "95_M8-DYUA8", "9fRankiszG4", "AbBJl3_G_s4"]
for vid in video_ids:
    p = Path(f"data/pending/{vid}.json")
    print(f"{vid}: exists={p.exists()}, size={p.stat().st_size if p.exists() else 0}")
