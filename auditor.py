"""Lancer depuis la racine : python auditor.py --help."""
import argparse
from pathlib import Path

from src.data import load_pair, read_table
from src.experiment import cross_validate, evaluate_test, train
from src.predict import audit, write_review_csv


def main():
    parser = argparse.ArgumentParser(description="Auditeur de qualité des cellules CSV")
    sub = parser.add_subparsers(dest="command", required=True)
    for cmd in ["inspect", "train", "evaluate", "cv"]:
        p = sub.add_parser(cmd)
        p.add_argument("--data", default="data/hospital")
        if cmd != "inspect":
            p.add_argument("--out", default="artifacts/hospital")
        if cmd == "train":
            p.add_argument("--seed", type=int, default=42)
    p = sub.add_parser("predict")
    p.add_argument("--input", required=True)
    p.add_argument("--artifacts", default="artifacts/hospital")
    p.add_argument("--output", default="reports/triage.csv")
    args = parser.parse_args()
    try:
        if args.command == "inspect":
            d, c, y, g = load_pair(args.data)
            print(f"{len(d)} lignes, {len(d.columns)} colonnes, {len(set(g))} fournisseurs")
            print(f"{int(y.sum())} différences / {y.size} cellules = {y.mean():.4%}")
            print("20 cellules différentes :")
            shown = 0
            for i in range(len(d)):
                for j, col in enumerate(d.columns):
                    if y[i, j] and shown < 20:
                        print(d.index[i], col, repr(d.iat[i, j]), "=>", repr(c.iat[i, j]))
                        shown += 1
        elif args.command == "train":
            result = train(args.data, args.out, args.seed)
            print(result["selected"])
        elif args.command == "evaluate":
            print(evaluate_test(args.data, args.out).to_string(index=False))
        elif args.command == "cv":
            print(cross_validate(args.data, args.out).to_string(index=False))
        else:
            result = audit(read_table(args.input), args.artifacts)
            Path(args.output).parent.mkdir(parents=True, exist_ok=True)
            write_review_csv(result, args.output)
            print(f"{len(result)} cellules ; {int(result.flagged.sum())} à examiner ; {args.output}")
    except (ValueError, FileNotFoundError, UnicodeError) as exc:
        parser.exit(2, f"Erreur : {exc}\n")


if __name__ == "__main__":
    main()
