"""Contrats des nouveaux ateliers et de leurs projets de transfert."""

import numpy as np
import pytest
from ateliers.trace_cinq_cellules import trace, confusion
from ateliers.solutions_exercices import aligned_labels
from ateliers.verifier_exercices import verify
from ateliers import solutions_exercices
from ateliers.transfert import (
    SCHEMAS,
    pair,
    profile,
    vectors,
    schema_mismatch,
    train,
    evaluate,
    predict,
    ROOT,
)


def test_five_cell_trace_and_metrics():
    rows = trace()
    assert [r["target"] for r in rows] == [0, 1, 1, 0, 1]
    assert rows[1]["score"] == rows[2]["score"] and rows[3]["score"] == rows[4]["score"]
    m = confusion([r["target"] for r in rows], [r["prediction_050"] for r in rows])
    assert (m["tp"], m["fp"], m["fn"], m["tn"]) == (2, 0, 1, 2) and m["f1"] == 0.8


def test_solutions_and_key_alignment():
    assert verify(solutions_exercices) == (6, 6)
    assert aligned_labels({"A": "x", "B": "y"}, {"B": "y", "A": "z"}) == {
        "A": 1,
        "B": 0,
    }
    with pytest.raises(ValueError):
        aligned_labels({"A": "x"}, {"B": "x"})


@pytest.mark.parametrize("project", ["clients", "inventaire"])
def test_transfer_coordinates_and_train_profiles(project):
    _, d, c, y = pair(project)
    assert y.sum() == 96 and y.shape == (480, 5)
    pr = profile(project, d.iloc[:12])
    unseen = d.iloc[12:13].copy()
    col = SCHEMAS[project][0]
    unseen.loc[:, col] = "jamais_vue"
    X, coords = vectors(project, unseen, pr)
    assert X[0, 4] == 0 and np.isfinite(X).all()
    assert len(coords) == 5 and "group_id" not in coords.column.tolist()


def test_transfer_end_to_end(tmp_path):
    out = tmp_path / "model"
    m = train("clients", out)
    _, d, c, _ = pair("clients")
    gs = [set(c.loc[ids].group_id) for ids in m["splits"].values()]
    assert all(gs[i].isdisjoint(gs[j]) for i in range(3) for j in range(i))
    result = predict(
        "clients",
        out,
        ROOT / "data/transfert_clients/fresh_dirty.csv",
        tmp_path / "review.csv",
    )
    assert len(result) == 48 * 5
    assert evaluate("clients", out)["model"]["cells"] == 480
    with pytest.raises(ValueError, match="déjà évalué"):
        evaluate("clients", out)
    assert schema_mismatch("clients", "age", "17") == 1
    assert schema_mismatch("inventaire", "stock", "-1") == 1
