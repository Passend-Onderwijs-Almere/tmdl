# Instructies: Maak een mapje aan waar dit python bestand, de markdown tabel als md en TMDL bestand als txt file instaat.
# Verander op regel 10-11 de juiste bestandsnamen
# # Zet python terminal op het juiste pad. Plak in de terminal "cd {path}" (bijvoordbeeld: cd C:\Users\JuliadeSwart\Downloads\Python)
# Als test kan je dir in het terminal zetten en kijken welke bestanden er gevonden worden.
# Zodra alles goed staat moet je in de terminal deze code plakken: python md_to_tmdl_inject.py

import re
from pathlib import Path

MD_FILE = Path("measures.md")                        #Markdown bestand
TMDL_FILE = Path("centrale_dataset_measures.txt")    #TDML script
OUT_FILE = Path("measures_enriched.tmdl")

# ── Stap 1: Markdown parsen ───────────────────────────────
md_map = {}
md_row = re.compile(
    r"\|\s*(.*?)\s*\|"      # 1 Domein
    r"\s*(.*?)\s*\|"        # 2 Naam measure
    r"\s*(.*?)\s*\|"        # 3 Eenheid
    r"\s*(.*?)\s*\|"        # 4 Bron
    r"\s*(.*?)\s*\|"        # 5 Power BI aantekeningen
    r"\s*(.*?)\s*\|"        # 6 Beschrijving
)

with MD_FILE.open(encoding="utf-8") as f:
    for line in f:
        if line.startswith("|") and not line.startswith("|-"):
            m = md_row.match(line)
            if m:
                md_map[m.group(2).strip()] = {
                    "domein": m.group(1).strip(),
                    "beschrijving": m.group(6).strip()
                }

# ── Stap 2: TMDL verrijken ─────────────────────────────────
measure_re = re.compile(r"^(\s*)measure\s+(.+?)\s*=")
out = []

with TMDL_FILE.open(encoding="utf-8") as f:
    for line in f:
        m = measure_re.match(line)
        if m:
            indent = m.group(1)
            name = m.group(2)
            if name in md_map:
                info = md_map[name]
                out.append(f"{indent}/// Domein: {info['domein']}\n")
                out.append(f"{indent}/// Beschrijving:\n")
                for l in info["beschrijving"].splitlines():
                    out.append(f"{indent}/// {l}\n")
        out.append(line)

OUT_FILE.write_text("".join(out), encoding="utf-8")
print("Markdown‑informatie is toegevoegd aan TMDL.")
