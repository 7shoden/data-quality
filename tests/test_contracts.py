"""Tests des invariants qui protègent l'évaluation."""
from pathlib import Path

import numpy as np
import pytest

from src.data import COLUMNS, group_split, load_pair, read_table
from src.features import CellFeatures, missing, mismatch
from src.metrics import measures

ROOT = Path(__file__).resolve().parents[1]


def test_alignment_by_id_not_position(tmp_path):
    dirty, clean, y, groups = load_pair(ROOT / "data/demo")
    raw = (ROOT / "data/demo/dirty.csv").read_bytes()
    (tmp_path / "dirty.csv").write_bytes(raw)
    clean.iloc[::-1].to_csv(tmp_path / "clean.csv")
    d2, c2, y2, _ = load_pair(tmp_path)
    assert np.array_equal(y, y2)
    assert c2.index.tolist() == dirty.index.tolist()


def test_group_split_no_overlap():
    groups = np.repeat(np.arange(45), 3)
    parts = group_split(groups)
    assert [len(set(groups[parts[k]])) for k in ["train", "validation", "test"]] == [27, 9, 9]
    assert set(groups[parts["train"]]).isdisjoint(groups[parts["test"]])


def test_profiles_never_fit_validation():
    dirty, _, _, _ = load_pair(ROOT / "data/demo")
    fit = CellFeatures().fit(dirty.iloc[:10])
    other = dirty.iloc[10:11].copy()
    other.loc[:, "city"] = "ville_jamais_vue"
    X, coords = fit.transform(other)
    i = coords.index[coords.column == "city"][0]
    j = fit.feature_names.index("train_frequency")
    assert X[i, j] == 0
    assert "ville_jamais_vue" not in fit.profiles["city"]["counts"]
    assert np.isfinite(X).all()
    assert len(coords) == len(other)*len(COLUMNS)


def test_string_integrity_and_missing_rules():
    dirty, _, _, _ = load_pair(ROOT / "data/demo")
    assert dirty.iloc[0]["zip"].startswith("0")
    assert missing("empty") and missing("  ")
    assert mismatch("address_2", "empty") == 0
    assert mismatch("phone", "2051234567") == 0
    assert mismatch("score", "105%") == 1


def test_metrics_majority_and_no_support():
    m = measures(np.array([0, 0, 1]), np.zeros(3))
    assert m["recall"] == 0 and m["f1"] == 0 and m["fn"] == 1
    m2 = measures(np.zeros(3), np.zeros(3))
    assert m2["average_precision"] is None and m2["error_support"] == 0


def test_bad_files_fail_clearly():
    for content in [b"", b"index,city\n1,x", b"index,city,city\n1,x,y"]:
        with pytest.raises(ValueError):
            read_table(content)


def test_flat_target_coordinate_alignment():
    d, c, y, _ = load_pair(ROOT / "data/demo")
    fit = CellFeatures(False).fit(d.iloc[:20])
    _, coords = fit.transform(d.iloc[:20])
    flat = y[:20].ravel()
    for i, row in coords.iterrows():
        assert flat[i] == int(d.loc[row.record_id, row.column] != c.loc[row.record_id, row.column])


def test_benchmark_numeric_units():
    from src.features import number
    assert number("97%", "score") == 97
    assert number("33 patients", "sample") == 33
    assert number("3x patients", "sample") is None
    assert mismatch("score", "97%") == 0
    assert mismatch("sample", "33 patients") == 0


def test_end_to_end_without_clean_at_inference(tmp_path):
    from src.experiment import train, evaluate_test
    from src.predict import audit
    artifact_dir = tmp_path / "model"
    train(ROOT / "data/demo", artifact_dir)
    # Inférence à partir d'une copie sale seule, sans référence dans ce dossier.
    path = tmp_path / "fresh.csv"
    path.write_bytes((ROOT / "data/demo/dirty.csv").read_bytes())
    result = audit(read_table(path), artifact_dir)
    assert len(result) == 600*len(COLUMNS)
    assert result.suspicion_score.between(0, 1).all()
    assert result.suspicion_score.is_monotonic_decreasing
    with pytest.raises(ValueError, match="figée"):
        train(ROOT / "data/demo", artifact_dir)
    metrics = evaluate_test(ROOT / "data/demo", artifact_dir)
    assert len(metrics) == 6
    with pytest.raises(ValueError, match="déjà évalué"):
        evaluate_test(ROOT / "data/demo", artifact_dir)


def test_csv_export_formula_and_strings(tmp_path):
    import pandas as pd
    from src.predict import write_review_csv
    path = tmp_path / "review.csv"
    frame = pd.DataFrame({"original_value": ["=1+1", "  @x", "al"], "score": [0.1, 0.2, 0.3]})
    write_review_csv(frame, path)
    result = pd.read_csv(path, keep_default_na=False)
    assert result.original_value.tolist() == ["\'=1+1", "\'  @x", "al"]
    assert frame.original_value.iloc[0] == "=1+1"
