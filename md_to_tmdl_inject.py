import re
from pathlib import Path

MD_FILE = Path("measures.md")
TMDL_FILE = Path("centrale_dataset_measures.txt")
OUT_FILE = Path("measures_enriched.tmdl")

# ── Stap 1: Markdown parsen ───────────────────────────────
md_map = {}
md_row = re.compile(r"\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|")

with MD_FILE.open(encoding="utf-8") as f:
    for line in f:
        if line.startswith("|") and not line.startswith("|-"):
            m = md_row.match(line)
            if m:
                domein, naam, beschrijving = m.groups()
                md_map[naam.strip()] = {
                    "domein": domein.strip(),
                    "beschrijving": beschrijving.strip()
                }

# ── Stap 2: TMDL verrijken ─────────────────────────────────
measure_re = re.compile(r"^\s*measure\s+(.+?)\s*=")
out = []

with TMDL_FILE.open(encoding="utf-8") as f:
    for line in f:
        m = measure_re.match(line)
        if m:
            name = m.group(1)
            if name in md_map:
                info = md_map[name]
                out.append(f"/// Domein: {info['domein']}\n")
                out.append("/// Beschrijving:\n")
                for l in info["beschrijving"].splitlines():
                    out.append(f"/// {l}\n")
        out.append(line)

OUT_FILE.write_text("".join(out), encoding="utf-8")
print("✅ Markdown‑informatie is toegevoegd aan TMDL.")
