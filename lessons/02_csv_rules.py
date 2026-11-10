"""Mini-auditeur sans ML : bibliothèque standard uniquement."""
import csv
import re
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data/demo/toy10.csv"
with path.open(encoding="utf-8", newline="") as f:
    for line, row in enumerate(csv.DictReader(f), start=2):
        reasons = []
        try:
            age = int(row["age"])
            if not 0 <= age <= 120:
                reasons.append("âge hors limites")
        except ValueError:
            reasons.append("âge manquant ou non entier")
        if not re.fullmatch(r"[0-9]{5}", row["code_postal"]):
            reasons.append("code postal invalide")
        if reasons:
            print(line, row["nom"], "; ".join(reasons))
