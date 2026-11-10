"""Relier cinq cellules de VALIDATION au vrai modèle Hospital, sans nouvel apprentissage."""

import json
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from src.data import load_pair
from src.experiment import verify_bundle


def main():
    root = Path(__file__).resolve().parents[1]
    folder = root / "artifacts/hospital"
    verify_bundle(folder)
    d, c, y, _ = load_pair(root / "data/hospital")
    split = json.loads((folder / "splits.json").read_text())
    ids = split["validation"]["record_ids"]
    target = y[d.index.get_indexer(ids)].ravel()
    best = joblib.load(folder / "bundle.joblib")["best"]
    X, coords = best["features"].transform(d.loc[ids])
    scores = best["model"].predict_proba(X)[:, 1]
    pred = scores >= best["config"]["threshold"]
    cases = list(np.flatnonzero((target == 0) & pred)[:2])
    cases += list(np.flatnonzero((target == 1) & ~pred)[:2])
    cases += list(np.flatnonzero(target == pred)[: 5 - len(cases)])
    records = []
    for k in cases:
        rec = coords.iloc[k].to_dict()
        rec.update(
            target=int(target[k]),
            clean=c.loc[rec["record_id"], rec["column"]],
            score=float(scores[k]),
            prediction=int(pred[k]),
            features=dict(zip(best["features"].feature_names, X[k].tolist())),
        )
        scaled = best["model"][0].transform(X[[k]])[0]
        classifier = best["model"][1]
        contributions = scaled * classifier.coef_[0]
        rec["intercept"] = float(classifier.intercept_[0])
        rec["linear_contributions"] = dict(
            zip(best["features"].feature_names, contributions.tolist())
        )
        rec["z"] = rec["intercept"] + float(contributions.sum())
        reconstructed = 1 / (1 + np.exp(-rec["z"]))
        assert abs(reconstructed - rec["score"]) < 1e-10
        records.append(rec)
        print(
            rec["record_id"],
            rec["column"],
            "y=",
            rec["target"],
            "score=",
            round(rec["score"], 6),
            "decision=",
            rec["prediction"],
        )
    dest = root / "reports/ateliers/diagnostic_validation.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(records, indent=2, ensure_ascii=False))
    print("30 caractéristiques par cellule ; détail dans", dest)


if __name__ == "__main__":
    main()
