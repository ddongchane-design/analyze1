import json
from pathlib import Path

batch_11 = [
    "8tUfR9WZtmA.json",
    "CTHMrzXPH1E.json",
    "CVFtZV4WEJM.json",
    "CbcE45MNaoM.json",
    "CrerETT7k2I.json",
    "Cv-gi8-Kn9o.json",
    "IAEJ9qWPjeE.json",
    "Ip4Ia4yblfU.json",
    "LGf6jWKC8oc.json",
    "O-szWnndpBQ.json",
    "Td7U_4SuXC0.json",
    "UQ-Hz9FDEiA.json",
    "ZwxgQIG7S1Q.json",
    "_es2GIlzVmc.json"
]

batch_12 = [
    "_f72XXvVkcU.json",
    "eBt7nHdKFtg.json",
    "fgqjHb7oFGE.json",
    "hxt8OHob-mM.json",
    "j0dz6NlphPs.json",
    "jN5xMaqN6Yk.json",
    "jS_AkPQE33g.json",
    "kQQ2R30DMV0.json",
    "pOcxSKf_PKw.json",
    "sGrU87PLkqQ.json",
    "uZvGP25HCkE.json",
    "webyouAz46w.json"
]

pending_dir = Path("data/pending")

def dump_list(files, out_filename):
    out_lines = []
    for filename in files:
        filepath = pending_dir / filename
        if filepath.exists():
            data = json.loads(filepath.read_text(encoding="utf-8"))
            video = data.get("video", {})
            transcript = data.get("transcript", "")
            out_lines.append("=" * 80)
            out_lines.append(f"FILENAME: {filename}")
            out_lines.append(f"TITLE: {video.get('title')}")
            out_lines.append(f"CHANNEL: {video.get('channel_name')}")
            out_lines.append(f"TRANSCRIPT PREVIEW (6000 chars):")
            out_lines.append(transcript[:6000])
            out_lines.append("=" * 80)
            out_lines.append("\n")
        else:
            out_lines.append(f"File {filename} not found.")
            
    Path(out_filename).write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Dumped to {out_filename}")

dump_list(batch_11, "scratch/batch11_raw.txt")
dump_list(batch_12, "scratch/batch12_raw.txt")
