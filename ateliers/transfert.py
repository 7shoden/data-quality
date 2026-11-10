"""Ateliers synthétiques clients/inventaire : entraînement, test et inférence séparés."""

import argparse
import csv
import hashlib
import json
import random
import re
from collections import Counter
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from src.data import group_split
from src.metrics import choose_threshold, measures
from src.predict import write_review_csv

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = {
    "clients": ["email", "age", "code_postal", "segment", "depense_mad"],
    "inventaire": ["designation", "categorie", "prix_mad", "stock", "entrepot"],
}


def fingerprint(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def schema_mismatch(project, col, value):
    if not value.strip():
        return 1
    if col == "email":
        return int(re.fullmatch(r"[^\s@]+@[^\s@]+\.[A-Za-z]{2,}", value) is None)
    if col == "code_postal":
        return int(re.fullmatch(r"[0-9]{5}", value) is None)
    if col in {"age", "stock", "depense_mad", "prix_mad"}:
        pattern = r"[0-9]+" if col in {"age", "stock"} else r"[0-9]+(?:\.[0-9]+)?"
        if re.fullmatch(pattern, value) is None:
            return 1
        return int(col == "age" and not 18 <= float(value) <= 100)
    vocab = {
        "segment": {"standard", "premium", "pro"},
        "categorie": {"bureau", "informatique", "accessoire"},
        "entrepot": {"casablanca", "rabat", "fes"},
    }
    return int(col in vocab and value not in vocab[col])


def read(project, path):
    columns = ["record_id", "group_id"] + SCHEMAS[project]
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if len(rows) < 2 or len(rows[0]) != len(set(rows[0])):
        raise ValueError("CSV vide ou en-têtes dupliqués")
    if set(rows[0]) != set(columns) or any(len(r) != len(columns) for r in rows[1:]):
        raise ValueError("Schéma de transfert incompatible")
    frame = pd.DataFrame(rows[1:], columns=rows[0]).set_index("record_id")
    if not frame.index.is_unique or any(not s.strip() for s in frame.index):
        raise ValueError("Clé de ligne non unique ou vide")
    return frame[["group_id"] + SCHEMAS[project]]


def profile(project, train):
    return {
        col: {
            "counts": dict(Counter(train[col])),
            "n": len(train),
            "median_length": float(np.median(train[col].str.len())),
        }
        for col in SCHEMAS[project]
    }


def vectors(project, frame, profiles):
    rows, coords = [], []
    cols = SCHEMAS[project]
    for rid, record in frame.iterrows():
        for j, col in enumerate(cols):
            value = record[col]
            pr = profiles[col]
            rows.append(
                [
                    int(not value.strip()),
                    schema_mismatch(project, col, value),
                    len(value),
                    sum(c in "0123456789" for c in value) / max(len(value), 1),
                    pr["counts"].get(value, 0) / pr["n"],
                    abs(len(value) - pr["median_length"]),
                ]
                + [int(k == j) for k in range(len(cols))]
            )
            coords.append({"record_id": rid, "column": col, "original_value": value})
    return np.array(rows, dtype=float), pd.DataFrame(coords)


def generate(project):
    folder = ROOT / "data" / ("transfert_" + project)
    folder.mkdir(parents=True, exist_ok=True)
    rng = random.Random(10 if project == "clients" else 20)
    cols = SCHEMAS[project]

    def rows_for(start, groups):
        records = []
        for g in range(start, start + groups):
            for month in range(6):
                if project == "clients":
                    vals = [
                        f"client{g}@exemple.ma",
                        str(18 + g % 55),
                        f"{1000+g:05d}",
                        ["standard", "premium", "pro"][g % 3],
                        f"{50+g*2+month:.2f}",
                    ]
                else:
                    vals = [
                        f"produit {g}",
                        ["bureau", "informatique", "accessoire"][g % 3],
                        f"{20+g+month/2:.2f}",
                        str(5 + (g + month) % 80),
                        ["casablanca", "rabat", "fes"][month % 3],
                    ]
                records.append([f"R{g:03d}_{month}", f"G{g:03d}"] + vals)
        return records

    clean = rows_for(0, 80)
    dirty = [r.copy() for r in clean]
    malformed = {
        "email": "adresse_sans_arobase",
        "age": "999",
        "code_postal": "35O33",
        "segment": "vip?",
        "depense_mad": "-10",
        "designation": "???",
        "categorie": "inconnue",
        "prix_mad": "prix?",
        "stock": "-3",
        "entrepot": "rbt?",
    }
    for flat in rng.sample(range(len(clean) * len(cols)), 96):
        i, j = divmod(flat, len(cols))
        col = cols[j]
        old = dirty[i][j + 2]
        if rng.random() < 0.7:
            value = malformed[col]
        elif col in {"age", "stock"}:
            value = str(int(old) + 1)
        elif col in {"prix_mad", "depense_mad"}:
            value = f"{float(old)+1:.2f}"
        elif col == "email":
            value = "x" + old
        elif col == "code_postal":
            value = f"{(int(old)+1)%100000:05d}"
        else:
            value = old + "x"
        dirty[i][j + 2] = value
    fresh = rows_for(100, 8)
    fresh[0][2] = "adresse_invalide" if project == "clients" else ""
    for name, values in [
        ("clean.csv", clean),
        ("dirty.csv", dirty),
        ("fresh_dirty.csv", fresh),
    ]:
        with (folder / name).open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["record_id", "group_id"] + cols)
            w.writerows(values)
    meta = {
        "origin": "Données fictives de formation, aucune observation réelle.",
        "groups": 80,
        "rows": 480,
        "business_columns": 5,
        "changed_cells": 96,
        "files": {
            n: fingerprint(folder / n)
            for n in ["dirty.csv", "clean.csv", "fresh_dirty.csv"]
        },
    }
    (folder / "source.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    print(folder)
    return folder


def pair(project):
    folder = ROOT / "data" / ("transfert_" + project)
    d = read(project, folder / "dirty.csv")
    c = read(project, folder / "clean.csv")
    if set(d.index) != set(c.index):
        raise ValueError("Clés dirty/clean différentes")
    c = c.loc[d.index]
    y = d[SCHEMAS[project]].ne(c[SCHEMAS[project]]).to_numpy(dtype=int)
    return folder, d, c, y


def train(project, out):
    out = Path(out)
    if (out / "bundle.joblib").exists():
        raise ValueError("Modèle déjà figé ; nouveau --out requis")
    folder, d, c, y = pair(project)
    split = group_split(c.group_id.to_numpy())
    tr, va = split["train"], split["validation"]
    if len(set(y[tr].ravel())) != 2 or len(set(y[va].ravel())) != 2:
        raise ValueError("Train et validation exigent les deux classes")
    profiles = profile(project, d.iloc[tr])
    Xt, _ = vectors(project, d.iloc[tr], profiles)
    Xv, _ = vectors(project, d.iloc[va], profiles)
    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42),
    )
    model.fit(Xt, y[tr].ravel())
    s = model.predict_proba(Xv)[:, 1]
    threshold = choose_threshold(y[va].ravel(), s)
    out.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        dict(project=project, profiles=profiles, model=model, threshold=threshold),
        out / "bundle.joblib",
    )
    m = {
        "project": project,
        "seed": 42,
        "threshold": threshold,
        "splits": {k: d.index[ix].tolist() for k, ix in split.items()},
        "data_hashes": {n: fingerprint(folder / n) for n in ["dirty.csv", "clean.csv"]},
        "source_sha256": fingerprint(__file__),
        "bundle_sha256": fingerprint(out / "bundle.joblib"),
        "validation": measures(y[va].ravel(), s, threshold),
    }
    (out / "manifest.json").write_text(json.dumps(m, indent=2))
    print("Validation :", m["validation"])
    return m


def check(project, out):
    m = json.loads((Path(out) / "manifest.json").read_text())
    if m["project"] != project or fingerprint(__file__) != m["source_sha256"]:
        raise ValueError("Projet ou code différent du modèle figé")
    if fingerprint(Path(out) / "bundle.joblib") != m["bundle_sha256"]:
        raise ValueError("Modèle modifié après gel")
    return m


def evaluate(project, out):
    out = Path(out)
    if (out / "test_metrics.json").exists():
        raise ValueError("Test déjà évalué ; consultez les résultats")
    m = check(project, out)
    folder, d, _, y = pair(project)
    if any(fingerprint(folder / n) != h for n, h in m["data_hashes"].items()):
        raise ValueError("Dataset modifié après gel")
    b = joblib.load(out / "bundle.joblib")
    ids = m["splits"]["test"]
    ix = d.index.get_indexer(ids)
    X, _ = vectors(project, d.loc[ids], b["profiles"])
    s = b["model"].predict_proba(X)[:, 1]
    rules = np.array(
        [
            schema_mismatch(project, col, row[col])
            for _, row in d.loc[ids].iterrows()
            for col in SCHEMAS[project]
        ]
    )
    result = {
        "model": measures(y[ix].ravel(), s, b["threshold"]),
        "rules": measures(y[ix].ravel(), rules),
        "always_correct": measures(y[ix].ravel(), np.zeros(len(s))),
    }
    (out / "test_metrics.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
    return result


def predict(project, out, input_path, output_path):
    check(project, out)
    b = joblib.load(Path(out) / "bundle.joblib")
    frame = read(project, input_path)
    X, coords = vectors(project, frame, b["profiles"])
    coords["suspicion_score"] = b["model"].predict_proba(X)[:, 1]
    coords["flagged"] = coords.suspicion_score >= b["threshold"]
    coords["human_status"] = "a_revoir"
    coords = coords.sort_values("suspicion_score", ascending=False, kind="stable")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    write_review_csv(coords, output_path)
    print(f"{len(coords)} cellules ; {int(coords.flagged.sum())} alertes")
    return coords


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Ateliers sur données fictives")
    p.add_argument("command", choices=["generer", "entrainer", "evaluer", "predire"])
    p.add_argument("--projet", required=True, choices=list(SCHEMAS))
    p.add_argument("--out")
    p.add_argument("--input")
    p.add_argument("--output")
    args = p.parse_args()
    out = (
        Path(args.out)
        if args.out
        else ROOT / "artifacts" / ("transfert_" + args.projet)
    )
    try:
        if args.command == "generer":
            generate(args.projet)
        elif args.command == "entrainer":
            train(args.projet, out)
        elif args.command == "evaluer":
            evaluate(args.projet, out)
        else:
            if not args.input or not args.output:
                raise ValueError("predire exige --input et --output")
            predict(args.projet, out, args.input, args.output)
    except (ValueError, FileNotFoundError) as exc:
        p.exit(2, f"Erreur : {exc}\n")
