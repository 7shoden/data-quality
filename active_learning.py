"""Extension : compare random/uncertainty sur validation, jamais sur test."""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier

from src.data import load_pair
from src.experiment import make_model, verify_bundle
from src.features import CellFeatures
from src.metrics import measures


def probabilities(model, X):
    if 1 not in model.classes_:
        return np.zeros(len(X))
    return model.predict_proba(X)[:, list(model.classes_).index(1)]


def run(folder, artifact_dir):
    verify_bundle(artifact_dir)
    d, _, y, _ = load_pair(folder)
    split = json.loads((Path(artifact_dir) / "splits.json").read_text())
    tr = d.index.get_indexer(split["train"]["record_ids"])
    va = d.index.get_indexer(split["validation"]["record_ids"])
    # Les profils utilisent le pool train non annoté ; aucun label n'y entre.
    feat = CellFeatures(True).fit(d.iloc[tr])
    X, _ = feat.transform(d.iloc[tr])
    V, _ = feat.transform(d.iloc[va])
    target, valid = y[tr].ravel(), y[va].ravel()
    records = []
    for seed in [11, 22, 33, 44, 55]:
        initial = np.random.default_rng(seed).choice(len(X), 10, replace=False).tolist()
        for policy in ["random", "uncertainty"]:
            rng = np.random.default_rng(seed)
            seen = initial.copy()
            while len(seen) <= 100:
                labels = target[seen]
                model = (make_model("logistic", weighted=True) if len(set(labels)) == 2
                         else DummyClassifier(strategy="prior"))
                model.fit(X[seen], labels)
                if len(seen) in [20, 50, 100]:
                    records.append({"seed": seed, "policy": policy, "budget": len(seen),
                                    "found_errors": int(labels.sum()),
                                    **measures(valid, probabilities(model, V))})
                if len(seen) == 100:
                    break
                pool = np.setdiff1d(np.arange(len(X)), np.asarray(seen))
                if policy == "random":
                    query = int(rng.choice(pool))
                else:
                    shuffled = rng.permutation(pool)
                    uncertainty = abs(probabilities(model, X[shuffled]) - .5)
                    query = int(shuffled[np.argmin(uncertainty)])
                seen.append(query)
    path = Path(artifact_dir) / "active_learning_validation.csv"
    pd.DataFrame(records).to_csv(path, index=False)
    print(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/hospital")
    parser.add_argument("--artifacts", default="artifacts/hospital")
    args = parser.parse_args()
    run(args.data, args.artifacts)
