# Édition maîtrise : commencer ici

Le PDF révisé accompagne ce dossier complet. Utiliser cette édition du ZIP pour les
nouveaux ateliers ; le projet Hospital d'origine et ses résultats restent conservés.

## Installation sous Python 3.12

Depuis ce dossier, sous Linux/macOS :

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python -m ateliers.diagnostic_installation
python -m pytest -q
```

Sous Windows PowerShell, sans activation :

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.venv\Scripts\python.exe -m ateliers.diagnostic_installation
.venv\Scripts\python.exe -m pytest -q
```

Résultats attendus : `INSTALLATION OK`, puis `17 passed`.
Utiliser ce même exécutable Windows à la place de `python` dans les commandes suivantes.

## Parcours

1. Lire les leçons 01 à 10 et lancer les scripts lessons/.
2. Étudier les données et les profils ; conserver les chaînes brutes.
3. Exécuter la trace manuelle : `python -m ateliers.trace_cinq_cellules`.
4. Compléter ateliers/exercices_a_completer.py, puis lancer
   `python -m ateliers.verifier_exercices`.
5. Consulter les solutions après tentative : `python -m ateliers.verifier_exercices --corrige`.
6. Relier le vrai modèle à ses cellules : `python -m ateliers.diagnostic_hospital`.
7. Suivre README.md pour le pipeline Hospital et l'interface Streamlit.
8. Reproduire les projets clients et inventaire, puis construire un exemple personnel.

Les six fonctions d'exercice commencent volontairement à 0/6 avec NotImplementedError.
Le vérificateur les présente comme « à compléter » ; les tests de livraison doivent
passer indépendamment de votre travail dans ce fichier.

## Trace manuelle : résultats attendus

Commande : `python -m ateliers.trace_cinq_cellules`.
Scores A/B/C/D/E : 0.047426, 0.924142, 0.924142, 0.182426, 0.182426.
Seuil .50 : TP=2, FP=0, FN=1, TN=2, F1=.8.
Seuil .15 : TP=3, FP=1, FN=0, TN=1, F1=6/7.
Ces coefficients sont fixés pour l'apprentissage du calcul, pas appris du benchmark.

## Projets de transfert : données fictives incluses

Les deux datasets possèdent 480 lignes, 80 groupes, 5 colonnes métier et 96 cellules
modifiées sur 2400. record_id et group_id restent hors des caractéristiques.
Les projets ne représentent aucun client ni produit réel.

Pour les clients :

```bash
python -m ateliers.transfert entrainer --projet clients --out artifacts/mes_clients
python -m ateliers.transfert evaluer --projet clients --out artifacts/mes_clients
python -m ateliers.transfert predire --projet clients --out artifacts/mes_clients --input data/transfert_clients/fresh_dirty.csv --output reports/ma_revue_clients.csv
```

Pour l'inventaire :

```bash
python -m ateliers.transfert entrainer --projet inventaire --out artifacts/mon_inventaire
python -m ateliers.transfert evaluer --projet inventaire --out artifacts/mon_inventaire
python -m ateliers.transfert predire --projet inventaire --out artifacts/mon_inventaire --input data/transfert_inventaire/fresh_dirty.csv --output reports/ma_revue_inventaire.csv
```

Les commandes longues se collent chacune sur une ligne.
Les modèles de référence sont déjà dans artifacts/transfert_clients et
artifacts/transfert_inventaire. Pour une démonstration immédiate, utiliser ces chemins
avec predire ; ne pas relancer leur évaluation, leurs résultats sont déjà enregistrés.
Pour refaire l'entraînement, conserver les nouveaux dossiers proposés ci-dessus.

Résultats test de référence (données synthétiques uniquement) :
- Clients : modèle F1=0.952381 ; règles F1=0.952381 ; 22 erreurs sur 480 cellules test.
- Inventaire : modèle F1=0.913043 ; règles F1=0.809524 ; 25 erreurs sur 480 cellules test.

Le fichier fresh de chaque projet contient 48 lignes, 240 cellules et de nouveaux groupes.
L'inférence y signale 48 cellules. Ce nombre n'est ni une précision ni un rappel : aucune
référence clean de fresh n'est fournie, et des identités nouvelles peuvent être signalées.

## Ce qui est conservé et vérifié

Le modèle Hospital choisi sur validation est inchangé : 64 TP, 24 FP, 42 FN, 3309 TN
sur 3439 cellules test. L'édition pédagogique ne réoptimise pas ce résultat.
Un environnement virtuel neuf a été créé et installé avec requirements-lock.txt.
Les 17 tests, le diagnostic, les corrigés et les ateliers ont été exécutés.
L'interface est vérifiée avec l'outil de test Streamlit et des uploads simulés.
Les vérifications de labels par un humain restent à effectuer dans
reports/label_spotchecks_a_completer.csv. Aucune étude pédagogique auprès d'un vrai
lecteur débutant n'est revendiquée.

Le HTML éditable du livre est livré sous docs/, avec ses graphiques locaux.
Il sert à la lecture et à l'annotation ; les outils de fabrication PDF ne sont pas
nécessaires pour exécuter le projet.

Pour les détails complets du backend Hospital, voir docs/README_HOSPITAL.md.
