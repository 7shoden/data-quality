"""Feedback progressif : python -m ateliers.verifier_exercices [--corrige]."""

import argparse
import importlib


def verify(module):
    def labels_reject():
        try:
            module.aligned_labels({"A": "x"}, {"B": "x"})
        except ValueError:
            return True
        return False

    records = [{"id": "A", "score": 0.2}, {"id": "B", "score": 0.9}]
    checks = [
        (
            "N1 manque",
            lambda: module.is_missing("  ")
            and module.is_missing("empty")
            and not module.is_missing("EMPTY")
            and not module.is_missing("0"),
        ),
        (
            "N2 ratios",
            lambda: module.digit_ratio("ab12") == 0.5 and module.digit_ratio("") == 0,
        ),
        (
            "N3 profil",
            lambda: module.column_frequency(["al", "al", "ca"], "al") == 2 / 3
            and module.column_frequency(["al"], "xx") == 0
            and module.column_frequency([], "x") == 0,
        ),
        (
            "N4 alignement",
            lambda: module.aligned_labels({"A": "x", "B": "y"}, {"B": "z", "A": "x"})
            == {"A": 0, "B": 1}
            and labels_reject(),
        ),
        (
            "N5 métrique",
            lambda: abs(module.f1_from_counts(8, 4, 2) - 16 / 22) < 1e-12
            and module.f1_from_counts(0, 0, 0) == 0,
        ),
        (
            "N6 classement",
            lambda: module.top_k(records, 1)[0]["id"] == "B"
            and records[0]["id"] == "A"
            and module.top_k(records, 0) == [],
        ),
    ]
    passed = 0
    for name, check in checks:
        try:
            ok = check()
            print(name, ": OK" if ok else ": à corriger")
            passed += int(bool(ok))
        except NotImplementedError:
            print(name, ": à compléter")
        except Exception as exc:
            print(name, ":", type(exc).__name__, str(exc))
    return passed, len(checks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--corrige", action="store_true")
    args = parser.parse_args()
    name = "solutions_exercices" if args.corrige else "exercices_a_completer"
    passed, total = verify(importlib.import_module("ateliers." + name))
    print(
        f"Résultat : {passed}/{total}. Le fichier à compléter commence volontairement à 0/6."
    )
