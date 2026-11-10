"""Téléchargement traçable d'un instantané précis du benchmark Raha Hospital."""
import datetime
import hashlib
import json
import urllib.request
from pathlib import Path

COMMIT = "7be1334b8c7bbdac3f47ef514fb3e1e8c5fc181c"
BASE = f"https://raw.githubusercontent.com/BigDaMa/raha/{COMMIT}"


def main():
    dest = Path(__file__).resolve().parent / "data" / "hospital"
    dest.mkdir(parents=True, exist_ok=True)
    records = []
    for filename in ["dirty.csv", "clean.csv", "LICENSE.md"]:
        relative = "LICENSE.md" if filename == "LICENSE.md" else f"datasets/hospital/{filename}"
        url = f"{BASE}/{relative}"
        with urllib.request.urlopen(url, timeout=60) as response:
            content = response.read()
        (dest / filename).write_bytes(content)
        records.append({"file": filename, "source": url,
                        "sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)})
    meta = {"dataset": "Hospital, benchmark Raha (BigDaMa)", "commit": COMMIT,
            "retrieved_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "license_note": "Le dépôt affiche Apache-2.0 ; aucune licence spécifique au dataset "
                            "n'a été trouvée dans le dossier hospital à cet instantané.",
            "files": records}
    (dest / "source.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print("Hospital téléchargé dans", dest)


if __name__ == "__main__":
    main()
