"""Interface facultative : streamlit run app.py."""
import io
from pathlib import Path

import streamlit as st

from src.data import read_table
from src.predict import audit, write_review_csv

st.set_page_config(page_title="Auditeur de données", layout="wide")
st.title("Auditeur de qualité des données")
st.caption("Classez les cellules à vérifier. Une alerte demande une vérification humaine.")
folder = st.selectbox("Modèle préparé", ["artifacts/hospital", "artifacts/demo"])
uploaded = st.file_uploader("Importer un CSV du même schéma Hospital", type=["csv"])
if uploaded is not None:
    try:
        if len(uploaded.getvalue()) > 5_000_000:
            raise ValueError("Fichier trop volumineux : maximum 5 Mo pour cette démo.")
        frame = read_table(uploaded.getvalue())
        if len(frame) > 5000:
            raise ValueError("Maximum 5 000 lignes pour cette démo.")
        st.subheader("Aperçu des données")
        st.dataframe(frame.head(20))
        if not (Path(folder) / "manifest.json").exists():
            st.info("Préparez ce modèle avec la commande train du README.")
        else:
            result = audit(frame, folder)
            st.metric("Cellules signalées", int(result.flagged.sum()))
            only_flags = st.checkbox("Afficher uniquement les alertes", value=True)
            view = result[result.flagged] if only_flags else result
            st.dataframe(view.head(1000), use_container_width=True)
            buffer = io.StringIO()
            write_review_csv(result, buffer)
            st.download_button("Télécharger le tableau de revue", buffer.getvalue(),
                               file_name="triage.csv", mime="text/csv")
    except (ValueError, FileNotFoundError, UnicodeError) as exc:
        st.error(str(exc))
