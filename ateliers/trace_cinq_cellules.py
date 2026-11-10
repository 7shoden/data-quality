"""Exemple calculable à la main : coefficients FIXÉS à des fins pédagogiques."""

import csv
import json
import math
import re
from pathlib import Path

TRAIN = {
    "phone": ["2051234567", "2051234567", "3341234567", "2561234567", "2511234567"],
    "emergency_service": ["yes", "yes", "yes", "no", "yes"],
    "city": ["birmingham", "birmingham", "mobile", "dothan", "birmingham"],
}
CELLS = [
    ("A", "phone", "2051234567", "2051234567"),
    ("B", "phone", "205123456x", "2051234567"),
    ("C", "emergency_service", "yxs", "yes"),
    ("D", "city", "sheffield", "sheffield"),
    ("E", "city", "birmingxam", "birmingham"),
]


def features(column, value):
    mismatch = (
        not bool(re.fullmatch(r"[0-9]{10}", value))
        if column == "phone"
        else value not in {"yes", "no"} if column == "emergency_service" else False
    )
    frequency = TRAIN[column].count(value) / len(TRAIN[column])
    return {
        "missing": int(not value.strip()),
        "type_mismatch": int(mismatch),
        "length": len(value),
        "digit_ratio": sum(c in "0123456789" for c in value) / max(len(value), 1),
        "train_frequency": frequency,
        "unseen": int(frequency == 0),
    }


def confusion(targets, predictions):
    tp = sum(y == 1 and p == 1 for y, p in zip(targets, predictions))
    fp = sum(y == 0 and p == 1 for y, p in zip(targets, predictions))
    fn = sum(y == 1 and p == 0 for y, p in zip(targets, predictions))
    tn = sum(y == 0 and p == 0 for y, p in zip(targets, predictions))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * tp / (2 * tp + fp + fn) if 2 * tp + fp + fn else 0.0
    return dict(tp=tp, fp=fp, fn=fn, tn=tn, precision=precision, recall=recall, f1=f1)


def trace():
    rows = []
    for key, column, dirty, clean in CELLS:
        f = features(column, dirty)
        z = -3 + 4 * f["type_mismatch"] + 1.5 * f["unseen"]
        score = 1 / (1 + math.exp(-z))
        rows.append(
            dict(
                cell=key,
                column=column,
                dirty=dirty,
                clean=clean,
                target=int(dirty != clean),
                **f,
                z=z,
                score=score,
                prediction_050=int(score >= 0.5),
                prediction_015=int(score >= 0.15)
            )
        )
    return rows


def main():
    root = Path(__file__).resolve().parents[1]
    folder = root / "reports" / "ateliers"
    folder.mkdir(parents=True, exist_ok=True)
    rows = trace()
    with (folder / "trace_cinq_cellules.csv").open(
        "w", encoding="utf-8", newline=""
    ) as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    metrics = {
        str(t): confusion(
            [r["target"] for r in rows], [int(r["score"] >= t) for r in rows]
        )
        for t in [0.5, 0.15]
    }
    (folder / "trace_metrics.json").write_text(json.dumps(metrics, indent=2))
    for r in rows:
        print(
            r["cell"],
            r["column"],
            repr(r["dirty"]),
            "y=",
            r["target"],
            "z=",
            r["z"],
            "score=",
            round(r["score"], 6),
        )
    print(json.dumps(metrics, indent=2))
    print(
        "Exemple pédagogique : coefficients fixés, aucun apprentissage ni test indépendant."
    )


if __name__ == "__main__":
    main()
