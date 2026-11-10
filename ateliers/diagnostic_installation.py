"""Contrôle pratique de l'installation : ne réentraîne et ne réévalue aucun modèle."""

import importlib
import platform
import sys
from pathlib import Path


def main():
    print("Python :", platform.python_version())
    print("Interpréteur :", sys.executable)
    for name in ["numpy", "pandas", "sklearn", "joblib", "streamlit", "pytest"]:
        module = importlib.import_module(name)
        print(name, getattr(module, "__version__", "import OK"))
    root = Path(__file__).resolve().parents[1]
    from src.data import load_pair
    from src.experiment import verify_bundle
    from src.predict import audit

    dirty, _, y, groups = load_pair(root / "data/hospital")
    assert dirty.shape == (1000, 19) and y.sum() == 509
    verify_bundle(root / "artifacts/hospital")
    result = audit(dirty.iloc[:2], root / "artifacts/hospital")
    assert len(result) == 38 and result.suspicion_score.between(0, 1).all()
    print("Hospital : 1000 lignes, 19 champs, 45 fournisseurs, 509 différences")
    print("Inférence : 2 lignes -> 38 cellules, sans clean transmis à audit")
    print("INSTALLATION OK")


if __name__ == "__main__":
    main()
