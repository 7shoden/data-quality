"""Jeu synthétique reproductible. Aucun résultat ne prouve une utilité réelle."""
import csv
import random
from pathlib import Path

from src.data import COLUMNS


def main():
    rng = random.Random(7)
    folder = Path(__file__).resolve().parent / "data" / "demo"
    folder.mkdir(parents=True, exist_ok=True)
    clean = []
    for provider in range(60):
        for visit in range(10):
            state = ["al", "ca", "ny"][provider % 3]
            code = f"measure-{visit}"
            values = [str(10000 + provider), f"hospital {provider}",
                      f"{provider+1} main street", "empty", "empty",
                      ["birmingham", "sacramento", "albany"][provider % 3], state,
                      f"{1000+provider:05d}", f"county {provider%5}",
                      str(2050000000 + provider), "acute care hospitals",
                      "public", "yes", "heart care", code,
                      f"care quality measure {visit}", str(60+visit*3)+"%",
                      str(30+visit)+" patients", f"{state}_{code}"]
            clean.append([str(len(clean)+1)] + values)
    dirty = [row.copy() for row in clean]
    # Exactement 285 cellules changées parmi 600 x 19 = 11 400.
    for flat in rng.sample(range(len(clean)*len(COLUMNS)), 285):
        i, j = divmod(flat, len(COLUMNS))
        old = dirty[i][j+1]
        mode = rng.randrange(4)
        dirty[i][j+1] = ["", old + "???", "x" + old[1:], old * 3][mode]
        if dirty[i][j+1] == old:
            dirty[i][j+1] = old + "x"
    for filename, rows in [("dirty.csv", dirty), ("clean.csv", clean)]:
        with (folder / filename).open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["index"] + COLUMNS)
            writer.writerows(rows)
    with (folder / "toy10.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nom", "age", "code_postal"])
        writer.writerows([["Sara", "22", "01000"], ["Yassine", "vingt", "20000"],
                         ["Imane", "-4", "30000"], ["Omar", "30", "abc"],
                         ["Nadia", "", "40000"], ["Ali", "25", "50000"],
                         ["Hajar", "19", "60000"], ["Amine", "35", "70000"],
                         ["Lina", "28", "80000"], ["Mehdi", "40", "90000"]])
    print("Démo : 600 lignes ; 285 différences. toy10.csv : premier exercice.")


if __name__ == "__main__":
    main()
