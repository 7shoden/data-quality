# De Python zéro à un projet IA maîtrisé

Français et darija ; corrigés séparés. Voir le PDF et README.md pour le parcours complet.

## 01. Ce que vous allez construire

Une cellule est l’intersection d’une ligne et d’une colonne. Dans une table d’hôpitaux, une ligne décrit une mesure pour un établissement ; le même établissement apparaît plusieurs fois. Une cellule peut contenir une faute de frappe, un numéro au mauvais format ou une valeur plausible mais incorrecte. Le but est de classer les cellules à vérifier par un humain, pas de réécrire les données automatiquement.
Le système reçoit un CSV conforme au schéma Hospital. Pour chaque cellule, il calcule des nombres décrivant sa forme et son contexte, puis produit un score de suspicion entre 0 et 1. Un seuil convertit ce score en alerte. La sortie conserve la clé de ligne, la colonne, la valeur originale et un statut humain. Un score élevé ne constitue pas une preuve d’erreur.
À la fin, vous saurez programmer, explorer un tableau, créer une cible, séparer les données, comparer des règles et deux modèles, mesurer leurs erreurs, sauvegarder un modèle et proposer une interface. Ces compétences se transfèrent aux autres projets de classification tabulaire, à condition de redéfinir la cible, le schéma et le protocole d’évaluation.
Le cours suit votre feuille de route, avec deux adaptations explicites : une préparation Python plus progressive et une extension d’apprentissage actif évaluée sur validation pendant le développement. Le test final reste réservé à une évaluation après gel.

**Darija (latin)** : Bghina n3erfo achmen khana f tableau khassha l-moraja3a. Ila l-programme 3ta score kbir, ma kay3nich belli l-qima ghalta b-yaqin. Nta katcheckiha. Ghadi nbniw kolchi b chwiya : Python, data, règles, modèles, évaluation, w interface.

**بالدارجة** : الفكرة هي نرتبو الخانات اللي خاصها المراجعة. السكور العالي ماشي دليل قاطع على الخطأ، والبرنامج ما كيبدل حتى قيمة بوحدو.

```text
CSV sale -> caractéristiques X -> modèle -> score -> revue humaine
CSV propre + CSV sale -> étiquettes y (pendant l'apprentissage)
À l'utilisation : aucun CSV propre n'est nécessaire.
```

X représente les informations disponibles au moment de l’audit. y représente la réponse connue pour apprendre. La référence propre sert à fabriquer y et à évaluer ; elle ne devient jamais une caractéristique.

**Exercice** : Écrivez une phrase décrivant l’entrée, une décrivant la sortie et une décrivant une limite du système.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous distinguez détection, classement et correction ; vous savez expliquer X et y.

## 02. Organiser son apprentissage

Si vous débutez en programmation, réservez d’abord deux à quatre semaines aux bases. Le planning de huit semaines du document source suppose une progression collective rapide ; ajoutez ce temps de préparation si nécessaire. Comptez environ 80 à 120 heures de pratique personnelle pour ce parcours, selon votre point de départ. Ce nombre est une estimation pédagogique, pas une garantie de vitesse.
Travaillez par séances de 60 à 90 minutes : lire une notion, recopier un exemple court, modifier une entrée, provoquer une erreur, expliquer le résultat sans regarder. Gardez un carnet avec trois lignes : ce que j’ai compris, le bug rencontré, le test qui prouve la correction. Reprendre une erreur comprise développe davantage l’autonomie que lancer dix fois un script sans le lire.
Le pack contient un cours, des scripts complets, un mini-tableau de dix lignes, un dataset synthétique de 600 lignes et Hospital. Les scripts lessons/ servent de pont entre les exemples et le vrai projet. Les modules src/ constituent la version finale. Ne commencez pas par mémoriser src/experiment.py : revenez-y après les fonctions, Pandas et les métriques.
À trois, alternez les rôles : écrire, relire et expliquer. Chacun doit pouvoir exécuter le pipeline entier. Une division où une seule personne comprend le modèle crée un risque pour la soutenance et pour la maintenance.

**Darija (latin)** : Ma t7fedch l-code bla fahm. Qra, jarrab, bdel chi valeur, w chof 3lach tbedel résultat. Ila tla3 bug, kteb sabab dyalo. Kol wa7ed f groupe khasso yqder ychra7 projet kamel, machi ghir fichier dyalo.

**بالدارجة** : قرا الفكرة، جرب المثال، بدل شي قيمة، ومن بعد شرح النتيجة بكلامك. التقدم كيبان فشنو تقدر تدير بوحدك، ماشي غير شحال قريتي.

```text
Préparation : leçons 03 à 11
Données : leçons 12 à 18
ML et évaluation : leçons 19 à 30
Application et autonomie : leçons 31 à 40
```

Les jalons du cours vérifient une compétence observable. Si vous ne pouvez pas expliquer un exemple avec vos propres mots, refaites-le sur une autre petite table.

**Exercice** : Planifiez quatre séances cette semaine et donnez à chacune un résultat vérifiable.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous avez un environnement de travail et un carnet de progression.

## 03. Terminal, Python et environnement virtuel

Un terminal exécute des commandes dans un dossier courant. pwd affiche ce dossier sous Linux/macOS ; cd le change ; ls liste son contenu. Sous Windows PowerShell, Get-Location et Get-ChildItem remplissent les mêmes rôles. Un chemin relatif part du dossier courant. Lancez toutes les commandes du projet depuis le dossier contenant auditor.py.
Python lit un fichier .py de haut en bas. L’éditeur sert à écrire le fichier ; le terminal sert à lancer python fichier.py. L’invite >>> correspond au mode interactif Python : on n’y colle pas les commandes de terminal. Pour quitter ce mode, tapez exit().
Une bibliothèque est du code réutilisable. pip installe ces bibliothèques. Un environnement virtuel isole celles du projet. Le pack est prévu pour Python 3.11 ou 3.12 ; les dépendances directes sont fixées dans requirements.txt. La version complète réellement utilisée lors de la vérification est enregistrée dans requirements-lock.txt. Utilisez Python 3.12 pour reproduire cet environnement, plutôt qu’une version différente choisie au hasard.
Décompressez d’abord le pack, ouvrez un terminal dans projet_auditeur, créez .venv puis activez-le. Le préfixe (.venv) vous aide à repérer l’environnement actif. La commande python -m pip garantit que l’installation correspond au Python utilisé.

**Darija (latin)** : Terminal b7al bab fin kat3ti les commandes. Dossier courant howa fin nta daba. .venv katkhlli bibliothèques dyal had projet bo7dhom, bach ma ytkheltouch m3a projet akhor. Ila commande ma khdematch, chof wach nta f dossier s7i7.

**بالدارجة** : الطرفية هي البلاصة ديال الأوامر، والمحرر هو فين كتكتب الملفات. البيئة الافتراضية كتخلي مكتبات هاد المشروع بوحدهم باش ما يتخلطوش مع مشاريع أخرى.

```text
# Linux / macOS, dans projet_auditeur
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python lessons/01_python.py

# Windows PowerShell (activation facultative)
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe lessons/01_python.py
```

Sous Windows, vous pouvez utiliser directement .venv\Scripts\python.exe dans les commandes suivantes. Vous n’avez pas besoin de modifier la politique PowerShell pour activer le dossier.

**Exercice** : Créez bonjour.py contenant print("Salam Python") et exécutez-le. Puis affichez la version de Python et l’emplacement de l’exécutable.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous savez différencier terminal, éditeur, interpréteur et dossier courant.

## 04. Variables, types et calculs

Une variable associe un nom à un objet. Dans age = 22, = effectue une affectation ; == compare deux valeurs. Python distingue int pour les entiers, float pour les nombres décimaux, str pour le texte et bool pour True ou False. None représente l’absence d’un objet, mais n’est pas la même chose que la chaîne vide "".
Le type exprime une signification, pas seulement une apparence. Un code postal est une chaîne : "01000" doit garder son zéro initial. Un identifiant de fournisseur se compare comme un identifiant, même s’il n’utilise que des chiffres. Un score numérique pourra être converti en float après avoir contrôlé sa validité.
Les opérateurs +, -, *, / réalisent les calculs courants. // calcule une division entière et % un reste. Diviser par zéro déclenche une exception. Pour une proportion de chiffres dans une chaîne vide, utiliser max(longueur, 1) empêche cette erreur et donne une proportion nulle.
Nommez les variables selon leur rôle : value, length, score, target. Un nom comme x est acceptable dans une formule courte ; dans une fonction métier, un nom précis facilite la relecture. Les commentaires expliquent une intention utile, pas chaque évidence syntaxique.

**Darija (latin)** : Variable hiya smiya katched valeur. "01000" texte, machi nombre li ghadi n7sbo bih. Ila 7weltiha l entier, zéro lwel kaydi3. Type kayt7edded 3la 7sab ma3na dyal colonne, machi ghir chkl dyalha.

**بالدارجة** : اختار النوع على حساب المعنى. الكود البريدي ورقم الهاتف نصوص، حيت الصفر اللي فاللول مهم وما بغيناش يضيع.

```text
code_postal = "01000"
longueur = len(code_postal)
nombre_chiffres = 5
ratio = nombre_chiffres / max(longueur, 1)
est_vide = longueur == 0
print(type(code_postal).__name__, longueur, ratio, est_vide)
# str 5 1.0 False
print(int(code_postal))  # 1000 : information perdue
```

len renvoie 5. Le ratio est un float. La comparaison produit un booléen. int crée une nouvelle représentation numérique ; elle ne conserve pas la mise en forme du texte.

**Exercice** : Prédisez les types de 3, 3.0, "3", True et None. Pourquoi ne pas convertir un numéro de téléphone en nombre ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous choisissez un type selon le sens de la donnée.

## 05. Chaînes, espaces et expressions régulières

Une chaîne est une séquence de caractères. len compte ses caractères ; s[0] lit le premier ; s[:2] lit les deux premiers. Attention : accéder à s[0] échoue si s est vide. Les chaînes sont immuables : strip et lower renvoient de nouvelles chaînes.
strip supprime les espaces aux extrémités ; lower convertit les lettres en minuscules. Ces opérations peuvent servir à reconnaître une valeur vide, mais les appliquer aux données avant de fabriquer les étiquettes change la définition d’une erreur. Dans notre benchmark, "al" et "al " sont différents. On conserve donc le texte original pour la comparaison exacte.
Une expression régulière décrit une forme autorisée. [0-9]{5} exige cinq chiffres ASCII. re.fullmatch vérifie toute la chaîne ; re.search cherche seulement un fragment. Pour un téléphone de dix chiffres, fullmatch rejette "2051234567x". Cela détecte une incompatibilité de format, pas un mauvais numéro parfaitement formé.
Dans le dataset, le texte "empty" joue le rôle d’un marqueur de manque. C’est un choix de ce benchmark, pas une convention universelle. Certains champs autorisent ce marqueur. Une adresse secondaire vide n’est donc pas automatiquement une erreur.

**Darija (latin)** : "al" w "al " kaybano qrab, walakin comparaison exacte kat7seb espace. Ma tnqich data qbel ma tfhem règle dyal labels. Regex katchecki chkl ; téléphone b 10 chiffres yqder ybqa ghalet ila howa dyal chi wa7ed akhor.

**بالدارجة** : التحقق من الشكل ماشي هو التأكد من الحقيقة. رقم فيه عشرة أرقام يقدر يبقى غالط، والمسافة الزايدة كتبدل المقارنة الحرفية.

```text
import re
s = " 01000 "
print(repr(s), repr(s.strip()))
print(bool(re.fullmatch(r"[0-9]{5}", s)))
print(bool(re.fullmatch(r"[0-9]{5}", s.strip())))
print("al" == "al ")
# False, True, False pour les trois comparaisons
```

Le préfixe r crée une chaîne brute pratique pour les motifs. bool convertit le résultat de fullmatch en True ou False. repr rend visibles les espaces dans les affichages de diagnostic.

**Exercice** : Validez "01000", "1000", "12a45" et "123456" avec le motif de cinq chiffres. Quelle valeur doit passer ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous distinguez forme valide, valeur correcte et normalisation.

## 06. Conditions et logique booléenne

if exécute un bloc quand une condition est vraie ; elif essaie une autre condition ; else couvre les cas restants. Python utilise l’indentation pour délimiter les blocs. Choisissez quatre espaces et ne mélangez pas tabulations et espaces. Une erreur d’indentation change la structure du programme.
and exige deux conditions vraies ; or en exige au moins une ; not inverse le résultat. Les comparaisons peuvent s’enchaîner : 0 <= age <= 120. Cette règle est un exemple pédagogique d’intervalle autorisé. Un projet réel doit documenter ses contraintes métier et ses exceptions.
L’ordre des contrôles protège le programme. Vérifier d’abord si la valeur est vide évite de convertir "" en entier. Vérifier une forme numérique ne garantit pas que la valeur est dans le domaine. Une valeur négative peut être syntaxiquement un nombre et rester invalide pour un âge.
Une règle déterministe renvoie toujours le même résultat pour les mêmes entrées. Elle offre un point de comparaison transparent pour le ML. Écrire ces règles avant les modèles permet d’obtenir une première solution utile et de vérifier si la complexité supplémentaire apporte un gain.

**Darija (latin)** : if b7al "ila" ; else b7al "ila ma kanch". Tertib dyal conditions mohim : lwel chof wach valeur khawya, mn be3d conversion, mn be3d limites. Règles sahl tchra7hom, w ghadi nqarnouhom m3a ML.

**بالدارجة** : كتب القاعدة بكلام واضح قبل الكود. تأكد واش القيمة خاوية، من بعد جرب التحويل، ومن بعد الحدود المسموح بها.

```text
age_texte = "-4"
if age_texte.strip() == "":
    raison = "manquant"
else:
    age = int(age_texte)
    if 0 <= age <= 120:
        raison = "forme acceptable"
    else:
        raison = "hors limites"
print(raison)  # hors limites
```

Cet exemple suppose une conversion possible. La leçon sur les exceptions ajoutera le cas "vingt". La formulation "forme acceptable" évite de déclarer une valeur vraie sur sa seule apparence.

**Exercice** : Ajoutez une règle pour un score compris entre 0 et 100. Le score "empty" est autorisé comme manque.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous écrivez une règle en langage naturel avant de la coder.

## 07. Listes, dictionnaires, ensembles et boucles

Une liste conserve une séquence ordonnée : valeurs = ["al", "ca", "al"]. Ses positions commencent à zéro. Un dictionnaire associe des clés à des valeurs : compte["al"] = 2. Un ensemble conserve des éléments uniques et permet de vérifier des intersections. Un tuple sert souvent à regrouper plusieurs résultats.
Une boucle for parcourt une collection. enumerate fournit à la fois la position et la valeur. range(3) produit les positions 0, 1, 2. On utilise les boucles pour comprendre le traitement cellule par cellule ; plus tard, NumPy et Pandas permettront aussi des opérations vectorisées.
Compter les occurrences prépare la caractéristique de fréquence. Pour chaque valeur, on augmente son compteur. get(valeur, 0) renvoie zéro si la clé n’existe pas encore. La fréquence relative vaut compteur / nombre de valeurs. Une valeur inconnue dans un nouveau fichier reçoit une fréquence nulle dans le profil appris.
Les ensembles protègent le découpage : si train_groups & test_groups n’est pas vide, un établissement apparaît dans les deux ensembles. C’est une erreur de protocole, même si les lignes exactes sont différentes. Les structures Python servent donc directement à la rigueur scientifique.

**Darija (latin)** : Liste kat7fed l-ordre. Dictionnaire kayrbet clé b valeur. Set kay7yed doublons. Bash n7sbo ch7al men merra jat "al", kandouro b boucle w nzido compteur. Bash n7miw split, kanchoufo wach groupes kaytlaqaw.

**بالدارجة** : اللائحة كتحافظ على الترتيب، والقاموس كيربط المفتاح بالقيمة، والمجموعة كتعاوننا نكشفو التداخل بين المستشفيات.

```text
values = ["al", "ca", "al", "ny"]
counts = {}
for position, value in enumerate(values):
    counts[value] = counts.get(value, 0) + 1
print(counts)                  # {'al': 2, 'ca': 1, 'ny': 1}
print(counts.get("xx", 0) / len(values))  # 0.0
train_groups = {"H1", "H2"}
test_groups = {"H3"}
assert not (train_groups & test_groups)
```

assert provoque un échec si l’invariant est faux. Dans les modules, ces contrôles rendent visibles des erreurs qui donneraient autrement des scores trompeurs.

**Exercice** : Calculez les fréquences de ["a", "b", "a", "a"]. Puis ajoutez "H2" au test et expliquez l’échec de l’assertion.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous construisez un compteur et vérifiez une intersection sans bibliothèque ML.

## 08. Fonctions, modules et petits objets

Une fonction rassemble une opération sous un nom. def définit la fonction, les paramètres reçoivent ses entrées et return renvoie son résultat. print affiche seulement une information. Une fonction qui affiche True sans le retourner n’offre pas un résultat exploitable par une autre fonction.
Choisissez une responsabilité claire : lire un CSV, valider une cellule, calculer une métrique. Les annotations de types documentent les intentions mais n’effectuent pas automatiquement une validation à l’exécution. Écrivez des messages d’erreur utiles pour les contrats qui comptent.
Un module est un fichier Python importable. Un package est un dossier organisé de modules ; src/__init__.py l’identifie explicitement ici. Le bloc if __name__ == "__main__" permet d’exécuter une commande lorsque le fichier est lancé directement, sans la relancer lors d’un import.
Une classe regroupe un état et des opérations. Notre CellFeatures conserve les profils appris dans self.profiles. fit apprend cet état sur train, puis transform le réutilise sur validation, test ou nouveaux fichiers. Vous n’avez pas besoin d’héritage avancé : comprenez d’abord l’instance, ses attributs et ses méthodes.

**Darija (latin)** : Fonction katakhod entrées w katrje3 résultat. print ghir kaybayan ; return kay3ti résultat l-code li 3ayet. Classe CellFeatures kat7fed profils dyal train, w transform katsta3melhom bla ma t3awed t3ellem men validation.

**بالدارجة** : الدالة كتشد مدخلات وكترد نتيجة. الطباعة غير كتبين النتيجة، أما الإرجاع كيخلي دالة أخرى تستعملها. الكائن يقدر يحتافظ بإحصائيات التعلم.

```text
def digit_ratio(value: str) -> float:
    n = len(value)
    count = sum(c in "0123456789" for c in value)
    return count / max(n, 1)

print(digit_ratio("ab12"))  # 0.5
print(digit_ratio(""))      # 0.0

class CounterExample:
    def __init__(self):
        self.total = 0
    def add(self):
        self.total += 1
```

sum additionne ici les booléens, car True se comporte comme 1 et False comme 0. self désigne l’instance en cours ; chaque instance peut garder un état différent.

**Exercice** : Écrivez une fonction is_missing qui reconnaît une chaîne vide, des espaces ou le texte "empty".

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous pouvez importer une fonction et expliquer ce que fit mémorise.

## 09. Fichiers, CSV, JSON et exceptions

Un CSV est un texte tabulaire. Les virgules séparent les champs, mais une valeur entre guillemets peut elle-même contenir une virgule. N’utilisez pas split(",") pour le lire. csv.DictReader gère les règles du format et fournit un dictionnaire par ligne.
with ouvre puis ferme correctement un fichier, même en cas d’erreur. encoding="utf-8" précise le décodage ; utf-8-sig accepte aussi un éventuel marqueur BOM initial. newline="" est recommandé avec le module csv pour éviter des lignes vides supplémentaires selon le système.
JSON conserve des structures simples : dictionnaires, listes, nombres, chaînes et booléens. Nous l’utilisons pour les métadonnées, le schéma et les partitions. joblib conserve les objets de modèles ; on ne charge que des artefacts de confiance, car leur désérialisation peut exécuter du code.
Une exception signale un problème. try/except ValueError permet de traiter une conversion impossible. Évitez except: pass : cela masque la cause et peut produire un résultat faux sans avertissement. Le projet rejette explicitement les fichiers vides, colonnes absentes, clés dupliquées et lignes mal formées.

**Darija (latin)** : CSV machi ghir texte n9smo b virgule ; chi valeur yqder tkoun fiha virgule bin guillemets. Sta3mel csv ou pandas. Ila float("abc") 3ta erreur, chdo b except ValueError w 3ti message mafhoum, ma tkhbbich bug.

**بالدارجة** : استعمل قارئ الملفات الجدولية باش الفواصل داخل القيم ما يفسدوش القراءة. إلا فشل تحويل رقم، عطينا سبب واضح وما تخبيش الخطأ.

```text
import csv
from pathlib import Path

path = Path("data/demo/toy10.csv")
with path.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
for row in rows:
    try:
        age = int(row["age"])
        print(row["nom"], 0 <= age <= 120)
    except ValueError:
        print(row["nom"], "âge non exploitable")
```

Le CSV de dix lignes est un exercice distinct : il n’a pas le schéma Hospital exigé par auditor.py. Utilisez lessons/02_csv_rules.py pour ce fichier.

**Exercice** : Combien de personnes ont un âge non convertible dans toy10.csv ? Et combien ont un âge numérique hors limites ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous lisez un CSV et traitez une conversion impossible sans arrêter tout le script.

## 10. Déboguer, tester et utiliser Git

Un traceback se lit d’abord à la dernière ligne : elle indique le type d’erreur et son message. Remontez vers votre fichier et sa ligne. FileNotFoundError suggère un chemin incorrect ; KeyError une colonne absente ; ValueError une valeur ou une forme non acceptée ; ModuleNotFoundError un environnement incomplet.
Réduisez un bug à un exemple de deux ou trois lignes. Affichez repr(value), le type et les dimensions avant l’opération fautive. Un test utile protège une propriété : alignement par clé, absence de chevauchement des groupes, fréquence inconnue nulle, correspondance entre cible aplatie et coordonnées. Tester uniquement qu’une fonction renvoie ce que son code dit déjà apporte moins d’assurance.
Git enregistre des versions du code. git status montre les modifications ; git add sélectionne des fichiers ; git commit crée un instantané. Une branche isole un changement ; une revue relie ce changement à une intention et à une vérification. Ne placez pas .venv dans Git.
Les partitions et métadonnées d’expérience doivent être conservées. Les fichiers lourds de modèles peuvent rester hors Git si vous utilisez un stockage d’artefacts identifié. Une graine aléatoire ne remplace pas les fichiers de données, versions de bibliothèques et paramètres.

**Darija (latin)** : Ila programme ta7, qra dernier message, mn be3d line dyal fichier dyalek. Sghgher exemple bach t3ref sabab. Git b7al historique mratab : kol commit fih changement mafhoum w test kaybayan belli khdam.

**بالدارجة** : قرا آخر سطر فالخطأ ورجع للسطر اللي فيه السبب. الاختبار خاصو يحمي قاعدة مهمة بحال تطابق المفاتيح وعدم خلط المجموعات.

```text
python -m pytest -q

git init
git switch -c feature/lecture-csv
git status
git add src/data.py tests/test_contracts.py
git commit -m "Lecture CSV et vérification des clés"
```

La configuration de nom et d’adresse Git peut être nécessaire lors du premier commit. N’exécutez pas git add . sans regarder les fichiers inclus, notamment les données personnelles dans de futurs projets.

**Exercice** : Inventez un test qui échoue si on remplace l’alignement par clés par un simple alignement par positions.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous expliquez ce qu’un test garantit et ce qu’il ne garantit pas.

## 11. NumPy, vecteurs et tableaux

Un vecteur est une liste ordonnée de nombres décrivant un exemple. Pour une cellule, on peut utiliser [manque, format_invalide, longueur, ratio_chiffres]. Une matrice X empile ces vecteurs. Une cible y contient un nombre par exemple, ici 0 pour cellule conforme à la référence et 1 pour différence.
NumPy représente efficacement les tableaux numériques. X.shape indique nombre d’exemples et nombre de caractéristiques. X[i, j] désigne la caractéristique j de l’exemple i. Les opérations sur des tableaux sont souvent effectuées élément par élément. np.isfinite détecte les NaN et infinis qui empêcheraient l’apprentissage.
Notre unité d’exemple est la cellule : 1 000 lignes et 19 colonnes métier donnent 19 000 exemples. Les cellules d’une même ligne ou d’un même hôpital restent dépendantes. Leur nombre ne justifie donc pas de prétendre disposer de 19 000 observations indépendantes.
Le parcours est fixé ligne par ligne, puis colonne par colonne. y.ravel() doit utiliser cet ordre. Aplatir dans un ordre différent apprendrait des réponses associées aux mauvaises cellules. Un test compare directement chaque coordonnée à dirty et clean.

**Darija (latin)** : X b7al tableau dyal chiffres li modèle kayfhem. Kol ligne f X katmattel khana wa7da men CSV, machi hôpital kamel. L-ordre mohim : ila labels trettbo b tariqa okhra, modèle ghadi yt3ellem réponses ghalta.

**بالدارجة** : كل خانة كتولي مثال عددي للموديل. خاص الترتيب ديال الميزات والترتيب ديال الأجوبة يبقاو مطابقين من أول العملية لآخرها.

```text
import numpy as np
X = np.array([[0, 0, 5, 1.0], [1, 1, 0, 0.0]])
y = np.array([0, 1])
print(X.shape, y.shape)  # (2, 4) (2,)
assert len(X) == len(y)
assert np.isfinite(X).all()
labels_table = np.array([[0, 1], [1, 0]])
print(labels_table.ravel())  # [0 1 1 0]
```

Les quatre caractéristiques ont un ordre déclaré. Changer cet ordre entre l’entraînement et l’inférence change le sens des coefficients du modèle.

**Exercice** : Une table de 600 lignes et 19 colonnes donne quelle forme de y aplati ? Combien de lignes dans X ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous reliez une cellule originale à une ligne de X et un élément de y.

## 12. Pandas : lire, sélectionner et résumer

Un DataFrame est une table nommée. Chaque colonne est une Series. head affiche les premières lignes ; shape donne les dimensions ; df["city"] choisit une colonne. loc sélectionne par étiquette et iloc par position. Un index n’est pas nécessairement un simple compteur : ici, c’est une clé de ligne provenant du fichier.
Pour éviter de perdre les zéros initiaux, chargez les CSV comme chaînes. keep_default_na=False empêche que certaines chaînes deviennent automatiquement des valeurs manquantes. Le lecteur final utilise aussi csv pour vérifier les champs du fichier avant de construire le DataFrame.
Un masque booléen permet de filtrer. pd.to_numeric(..., errors="coerce") sert à explorer une version numérique temporaire : les conversions impossibles deviennent NaN dans cette copie. Ne remplacez pas la colonne brute par cette copie avant d’avoir créé les étiquettes exactes.
Résumez toujours les dimensions, valeurs distinctes, marqueurs de manque et exemples. df.isna() ne détecte pas le texte "empty" ni forcément les chaînes vides conservées comme texte. Il faut une définition explicite du manque adaptée au dataset.

**Darija (latin)** : Pandas kay3tik tableau b smiyat colonnes. loc kayqelleb b clé, iloc b position. "empty" texte ma howach NaN. Ila bghiti t7seb manque, khass règle kat3ref les tokens dyal dataset.

**بالدارجة** : حافظ على النص الأصلي، ودير التحويلات فالنسخ اللي كتستعملها للتحليل. كلمة كتدل على الفراغ ما كتوليش تلقائياً قيمة مفقودة عند المكتبة.

```text
import pandas as pd
df = pd.read_csv("data/demo/toy10.csv",
                 dtype=str, keep_default_na=False)
print(df.shape)
print(df["code_postal"].head())
age_num = pd.to_numeric(df["age"], errors="coerce")
mask = age_num.isna() | ~age_num.between(0, 120)
print(df.loc[mask, ["nom", "age"]])
print((df["age"].str.strip() == "").sum())
```

| est le ou élément par élément dans Pandas. Les expressions doivent souvent être entourées de parenthèses. and attend un seul booléen et ne remplace pas | pour des Series.

**Exercice** : Sélectionnez les codes postaux qui ne correspondent pas à cinq chiffres, sans modifier le tableau original.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous savez explorer un tableau en conservant ses chaînes brutes.

## 13. Trois datasets pour progresser

Le fichier toy10.csv possède dix lignes et trois colonnes : nom, age, code_postal. Il sert à apprendre les boucles, conversions et règles. Son format n’est pas celui de l’auditeur final. Le script lessons/02_csv_rules.py y détecte quatre lignes à vérifier.
Le dataset demo utilise le schéma Hospital, avec 60 fournisseurs synthétiques, 600 lignes et 19 colonnes métier. Le générateur fixe la graine à 7 et modifie exactement 285 cellules sur 11 400, soit 2,5 %. Les paires dirty.csv et clean.csv permettent de tester tout le pipeline hors ligne. Les erreurs y sont artificielles et plus simples que celles d’un vrai système.
Hospital vient du dossier datasets/hospital du dépôt BigDaMa/raha. L’instantané téléchargé est identifié par un commit, des URL et des empreintes SHA-256 dans source.json. Les dimensions et différences sont recalculées dans le pack ; elles ne sont pas supposées vraies seulement parce que la feuille de route les annonce.
Le dépôt affiche une licence Apache-2.0. Le pack conserve le fichier de licence et signale qu’aucune licence particulière au dataset n’est présente dans ce dossier de l’instantané. Conservez la provenance lorsque vous réutilisez les données. Il s’agit de tables d’établissements et de mesures, pas d’un dataset clinique de patients utilisé pour diagnostiquer des personnes.

**Darija (latin)** : Ghadi nbda b 10 lignes bach nfhem. Mn be3d demo kbira b erreurs msnou3in. Mn be3d Hospital li jay men Raha. Résultats dyal demo ma n9drouch n3emmohom 3la data réelle. Khassna n7efdo source w version.

**بالدارجة** : بدا بالجدول الصغير، دوز للبيانات المصنوعة، ومن بعد المعيار الحقيقي. النتائج ديال بيانات سهلة ومصنوعة ما كتضمنش الأداء فالواقع.

```text
python make_demo.py
python auditor.py inspect --data data/demo
python download_data.py
python auditor.py inspect --data data/hospital
# Les CSV sont déjà inclus dans le pack.
# Le téléchargement sert à retrouver le même instantané.
```

inspect charge dirty et clean, aligne leurs clés et affiche vingt différences. Ces exemples sont un contrôle du benchmark ; les diagnostics utilisés pour améliorer le modèle viennent ensuite de validation.

**Exercice** : Quelle propriété du dataset synthétique risque de faciliter artificiellement la détection ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous savez à quel dataset correspondent vos résultats.

## 14. Dictionnaire de données et schéma

Un schéma décrit les colonnes attendues et leur sens. Le projet exige index plus dix-neuf colonnes métier. index est une clé de ligne : elle sert à aligner et retrouver les cellules, jamais à entraîner le modèle. provider_number identifie l’établissement ; plusieurs lignes partagent cette valeur.
name, address_1, address_2, address_3, city, state, zip, county et phone décrivent l’établissement. type et owner décrivent son statut ; emergency_service indique yes ou no. condition, measure_code et measure_name décrivent la mesure ; score et sample représentent des valeurs numériques quand elles sont présentes ; state_average est un libellé composite.
Le CSV propre utilise des en-têtes différents : ProviderNumber devient provider_number, HospitalName devient name, ZipCode devient zip et Stateavg devient state_average. Le dictionnaire HEADER_MAP explicite les dix-neuf correspondances. Une conversion automatique de casse ne suffirait pas pour HospitalName et name.
Nos règles sont des hypothèses de benchmark : state attend deux lettres minuscules ; phone dix chiffres ; zip quatre ou cinq chiffres ; score un pourcentage écrit comme « 97% » de 0 à 100 ; sample un effectif écrit comme « 33 patients ». address_2, address_3, score et sample peuvent manquer. Une adaptation à un autre pays ou à un autre flux exige de revoir ces règles et leur coût en fausses alertes.

**Darija (latin)** : Schéma howa contrat dyal tableau : achmen colonnes, ma3na dyalhom, w chno format maqboul. ZipCode w zip nafs colonne b smiyat mkhtalfin. Ma n3tamdouch 3la l-position, kanst3mlo mapping wad7.

**بالدارجة** : المخطط هو عقد: أسماء الأعمدة، المعنى ديالها، والشكل المقبول. إلا تبدل المجال خاصنا نراجعو القواعد، ماشي غير نبدلو اسم الملف.

```text
from src.data import HEADER_MAP, COLUMNS
print(HEADER_MAP["HospitalName"])  # name
print(len(COLUMNS))               # 19

# Exemple de règles déclarées
# state : [a-z]{2}
# zip : [0-9]{4,5} (convention héritée du benchmark)
# phone : [0-9]{10}
# index : clé unique, conservée hors de X
```

Le lecteur accepte les en-têtes propres ou sales après mapping et réordonne les colonnes selon COLUMNS. Il rejette les colonnes inattendues plutôt que d’auditer silencieusement un autre schéma.

**Exercice** : Pourquoi une colonne zip entièrement numérique n’implique-t-elle pas une déviation numérique dans X ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous pouvez expliquer le rôle de chacune des dix-neuf colonnes.

## 15. Aligner les tables et fabriquer la cible

La cible vaut y(i,j)=1 si dirty(i,j) est différent de clean(i,j), sinon 0. Cette définition mesure un désaccord avec la référence. Elle suppose que la référence est fiable ; elle ne prouve pas que toute différence est une erreur métier. Un contrôle manuel vérifie notamment les différences de casse, d’espace et les conventions de manque.
Avant de comparer, normalisez uniquement les noms d’en-têtes grâce au mapping déclaré. Vérifiez que les clés index sont uniques et non vides, puis que leurs ensembles sont égaux. Réordonnez le propre selon les clés du sale, enfin selon les colonnes métier. Une jointure implicite par positions peut fabriquer des milliers de fausses erreurs.
On conserve la comparaison exacte du texte, espaces compris. Choisir une comparaison après strip serait possible pour un autre benchmark, mais changerait la cible ; il faudrait l’annoncer et recalculer toutes les statistiques. N’appliquez pas une normalisation opportuniste pour obtenir un meilleur score.
Pour les groupes, on utilise ici provider_number de la référence : certains identifiants sales peuvent être corrompus et diviseraient artificiellement un même hôpital. Cette information sert exclusivement à définir le protocole hors ligne, pas à construire X ni à prédire. En déploiement, un identifiant maître fiable est une autre manière d’assurer ce regroupement.

**Darija (latin)** : Qbel comparaison, rbet lignes b index s7i7. Ila tableau propre meqloub f l-ordre, labels khasshom ybqaw nafs-hom. Référence kat3tina réponse bach nt3ellmo, walakin ma katdkholch f features. Groupe men référence ghir bach split ykoun n9i.

**بالدارجة** : ربط الجدول النقي والوسخ بالمفاتيح، ماشي بترتيب السطور. الجواب الحقيقي كيتصاوب بالمقارنة، ولكن ما كيدخلش وسط الميزات.

```text
from src.data import load_pair
dirty, clean, y, groups = load_pair("data/hospital")
assert dirty.index.equals(clean.index)
assert dirty.columns.equals(clean.columns)
print(y.shape, int(y.sum()))
# y est une matrice de 0/1 ; on l'aplatira après le split.
# La clé index n'apparaît pas parmi les caractéristiques.
```

Conservez vingt différences et vingt égalités dans une feuille de contrôle. Pour chacune, notez la clé, la colonne, les deux valeurs, votre interprétation et le nom du vérificateur.

**Exercice** : Le CSV propre est trié à l’envers. Faut-il trier le sale au hasard pour compenser ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous reconstruisez y et démontrez sa correspondance avec les coordonnées.

## 16. Exploration et déséquilibre des classes

L’exploration décrit la difficulté avant de modéliser. Mesurez le nombre de lignes, colonnes et fournisseurs ; le taux de différences global ; les erreurs par colonne ; le taux de marqueurs manquants ; les valeurs fréquentes et les longueurs inhabituelles. Chaque chiffre doit préciser son dénominateur.
Si 509 cellules sur 19 000 diffèrent, la prévalence vaut 509/19000=2,679 %. Le modèle qui répond toujours « correct » obtient alors 97,321 % d’accuracy. Pourtant il ne trouve aucune erreur : son rappel sur la classe 1 est nul. Cette baseline doit apparaître dans le rapport pour déjouer la séduction d’un grand pourcentage.
Un histogramme de longueurs ne révèle pas directement des erreurs. Les noms de mesures sont naturellement longs et les codes d’état courts. La comparaison utile se fait souvent à l’intérieur d’une colonne et avec une compréhension de sa sémantique. Une valeur rare peut être parfaitement correcte.
L’exploration globale permet de contrôler le fichier et sa référence. Après le gel du split, les analyses guidant les caractéristiques et réglages se font sur train et validation. Ne regardez pas les faux négatifs du test pour modifier le pipeline puis prétendre avoir conservé un test indépendant.

**Darija (latin)** : Ila erreurs qlalin, "kolchi s7i7" yqder y3ti accuracy kbira. Walakin ma lqa ta erreur. Donc khasna métriques dyal classe erreur, w ch7al men erreur kayna f kol colonne. Rareté bo7dha ma kat3nich ghalat.

**بالدارجة** : إلا الأخطاء قليلة، برنامج كيقول كلشي صحيح يقدر يبان ناجح بنسبة كبيرة. خاصنا نشوفو شحال من خطأ لقا وشحال عطى من إنذار كاذب.

```text
import pandas as pd
from src.data import load_pair
d, c, y, groups = load_pair("data/hospital")
errors = pd.Series(y.sum(axis=0), index=d.columns)
print(errors.sort_values(ascending=False))
prevalence = y.mean()
print("Taux d'erreurs :", prevalence)
print("Accuracy toujours correct :", 1-prevalence)
```

Le graphique du cours affiche les différences exactes par colonne sur le benchmark. Les résultats de modèles utilisent ensuite les partitions enregistrées.

**Exercice** : Sur 1000 cellules avec 25 erreurs, un système qui ne signale rien obtient quelle accuracy et quel rappel ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous pouvez expliquer pourquoi l’accuracy est insuffisante.

## 17. Train, validation et test par groupes

Train sert à apprendre les profils, le scaler et les coefficients du modèle. Validation sert à choisir les hyperparamètres, la famille de modèle et le seuil. Test sert à estimer une fois la performance du système figé. Modifier un choix après avoir vu le test transforme ce test en nouvelle validation.
Le même fournisseur apparaît dans plusieurs lignes. Un split aléatoire des cellules peut mettre des noms et adresses presque identiques dans train et test. Le modèle reconnaîtrait alors des établissements déjà vus. La séparation par fournisseur évalue sa capacité à auditer des établissements absents du train.
On réserve 20 % des groupes au test, puis 25 % des groupes restants à validation. Cela donne environ 60/20/20 des groupes, pas nécessairement des lignes ni des erreurs. Pour 45 fournisseurs, le split donne 27, 9 et 9 groupes. Leurs tailles en lignes peuvent varier.
La graine 42 rend le tirage reproductible pour cet environnement. On sauvegarde aussi les clés et groupes dans splits.json. Vérifiez les intersections nulles et la présence des deux classes dans train et validation. Si une partition ne contient aucune erreur, rapportez cette difficulté ; ne cherchez pas silencieusement une graine donnant un meilleur score.

**Darija (latin)** : Train b7al waqt l-qraya, validation b7al exercices bach nkhtaro méthode, test b7al examen l-akher. Ma ndkhlouch nafs hôpital f jouj côtés. 60/20/20 dyal groupes, machi darori dyal lignes.

**بالدارجة** : خلي كل مستشفى فجهة وحدة. التعلم باش نتعلمو، التحقق باش نختارو، والاختبار الأخير باش نقيسو الاختيار اللي تجمد.

```text
from src.data import group_split, load_pair
d, c, y, groups = load_pair("data/hospital")
parts = group_split(groups, seed=42)
for name, ix in parts.items():
    print(name, len(ix), len(set(groups[ix])), y[ix].sum())
a = set(groups[parts["train"]])
b = set(groups[parts["test"]])
assert a.isdisjoint(b)
```

Ce split mesure un scénario précis : nouveaux fournisseurs, schéma inchangé. Auditer de nouvelles mesures chez les mêmes fournisseurs ou des fichiers futurs demanderait éventuellement un autre protocole, notamment temporel.

**Exercice** : Pourquoi ne pas utiliser directement train_test_split sur les 19 000 cellules ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous savez justifier l’unité de regroupement de votre futur projet.

## 18. Baselines déterministes

Une baseline fournit un résultat de référence à faible complexité. La première répond toujours « correct ». Son F1 et son rappel de la classe erreur sont nuls lorsqu’il existe des erreurs. La seconde applique les règles de schéma : format, manque obligatoire et limites numériques.
Notre règle renvoie 1 si une cellule manque dans un champ obligatoire, viole une expression régulière ou dépasse un intervalle numérique. Sinon elle renvoie 0. Pour address_2, address_3, score et sample, un manque autorisé ne déclenche pas l’alerte. La baseline n’apprend aucune fréquence et ne reçoit pas la référence propre lors de l’inférence.
Les erreurs au format valide restent difficiles : une mauvaise ville composée de lettres ressemble à une bonne ville. Les règles ne détectent pas non plus toutes les contradictions entre colonnes. À l’inverse, une règle trop stricte sur les codes postaux peut signaler une valeur de référence correcte dans un benchmark hérité.
Évaluez toutes les méthodes sur les mêmes cellules et avec la même cible. La baseline règle produit un score binaire, contrairement aux modèles qui classent plus finement les cellules. Ne comparez pas les méthodes sur des sous-ensembles différents en leur attribuant ensuite un unique classement global.

**Darija (latin)** : Baseline hiya départ bach n3erfo wach ML zad chi faida. Règle katched téléphone li fih lettres, walakin ville ghalta b lettres s7a7 yqder tfoutha. Ila règles reb7o modèle, had résultat 3ilmi ma fih ta mochkil.

**بالدارجة** : القواعد بداية ضرورية للمقارنة. كتشد الأخطاء المعروفة فالشكل، ولكن قيمة معقولة فالشكل تقدر تكون غالطة فالمعنى.

```text
from src.features import mismatch
print(mismatch("phone", "2051234567"))  # 0
print(mismatch("phone", "205123456x"))  # 1
print(mismatch("address_2", "empty"))   # 0
print(mismatch("score", "150%"))         # 1
print(mismatch("city", "wrongcity"))    # 0
```

La dernière réponse montre une limite concrète : les règles de cette baseline ne comprennent pas la vérité géographique. Le contexte statistique peut aider, mais ne garantit pas de corriger cette limite.

**Exercice** : Ajoutez mentalement une règle « toute valeur inconnue est fausse ». Quel défaut majeur crée-t-elle ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous pouvez défendre une baseline et donner un échec précis.

## 19. Décrire une cellule sans son contexte

Les caractéristiques locales décrivent la cellule seule, sous les contraintes de sa colonne. Le projet utilise manque, incompatibilité de type, longueur, proportion de chiffres, de lettres, d’espaces et de caractères spéciaux. On ajoute un codage indicateur de la colonne pour que le modèle distingue un téléphone d’un nom.
Pour "ab12", la longueur vaut 4, le ratio de chiffres 2/4 et le ratio de lettres 2/4. Pour une chaîne vide, chaque ratio vaut 0 grâce au dénominateur max(n,1). L’indicateur de manque conserve l’information que cette longueur nulle représente une absence.
Le codage de colonne est fixe : dix-neuf positions, dont une seule vaut 1. Il est présent dans les variantes avec et sans contexte. On ne donne au modèle ni la clé index, ni la valeur brute du fournisseur, ni la valeur propre, ni la cible. Le codage de colonne exprime le schéma connu, pas l’identité de l’hôpital.
Le schéma sans contexte compte sept caractéristiques de base plus dix-neuf indicateurs, donc 26 caractéristiques. Le modèle avec contexte en compte quatre de plus. Sauvegarder leur ordre est aussi important que sauvegarder leurs noms : un modèle interprète des positions, pas vos intentions.

**Darija (latin)** : Modèle ma kayqrach texte kif bnadem. Kan7wlo khana l chiffres : longueur, ratios, manque... W kan3tiwh achmen colonne hiya. Ma kan3tiwhch l-jawab propre ou identifiant dyal ligne.

**بالدارجة** : حوّل الخانة لأوصاف رقمية بحال الطول ونسبة الأرقام والشكل. ما تعطيناش للموديل الجواب النقي ولا رقم السطر باش يحفظو.

```text
value = "ab12"
n = len(value)
digits = sum(c in "0123456789" for c in value)
letters = sum(c.isalpha() for c in value)
vector = [0, 0, n, digits/max(n, 1), letters/max(n, 1)]
print(vector)  # [0, 0, 4, 0.5, 0.5]
# Les autres ratios et indicateurs de colonne s'ajoutent.
# Aucun accès à clean n'est nécessaire.
```

Le deuxième zéro suppose que le texte est acceptable pour sa colonne. Dans phone, la même valeur provoquerait type_mismatch=1. Une caractéristique locale peut donc utiliser les contraintes déclarées du schéma.

**Exercice** : Calculez longueur, ratio chiffres et ratio espaces pour "12 3" et pour "".

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous vérifiez cinq vecteurs à la main et retrouvez le même résultat à 10^-4 près.

## 20. Apprendre le contexte sur train uniquement

Le contexte compare une cellule à la distribution de sa colonne. La fréquence vaut nombre d’occurrences de sa valeur dans la colonne train divisé par nombre de lignes train. La déviation de longueur vaut |longueur - médiane_train| / max(écart_type_longueurs_train,1).
Pour score et sample, on calcule aussi une distance numérique absolue à la moyenne train, divisée par max(écart_type_train,1). L’indicateur numeric_applicable précise si cette distance a un sens. Les identifiants, codes postaux et téléphones n’utilisent pas ce calcul numérique. Les valeurs non convertibles n’y entrent pas et reçoivent une déviation nulle avec indicateur 0.
Le profil est appris sur le CSV sale de train. Il peut donc lui-même contenir des erreurs ; on ne prétend pas disposer d’une distribution parfaite. La médiane de longueur et les conventions de plancher limitent certains problèmes mais ne garantissent pas une robustesse universelle.
fit mémorise fréquences et statistiques. transform ne les modifie pas et donne zéro à la fréquence d’une valeur inconnue. Calculer les fréquences sur le fichier complet avant le split exposerait validation et test à l’apprentissage. Recalculer un profil sur un nouvel upload changerait aussi le système évalué.

**Darija (latin)** : Contexte howa nqaren khana m3a colonne dyal train. Ila valeur jdida, fréquence zéro, walakin ma darorich ghalta. Profil ma khassoch ytbeddel mlli n3tiw validation ou upload jdid. fit kayt3ellem, transform kaytbeq.

**بالدارجة** : الإحصائيات خاصها تتعلم غير من جزء التعلم. فملف جديد كنستعملو نفس الإحصائيات، وما كنعاودوش نحسبوها عليه.

```text
from src.data import load_pair, group_split
from src.features import CellFeatures
d, _, y, g = load_pair("data/hospital")
parts = group_split(g)
features = CellFeatures(context=True).fit(d.iloc[parts["train"]])
X_train, coords_train = features.transform(d.iloc[parts["train"]])
X_val, coords_val = features.transform(d.iloc[parts["validation"]])
print(X_train.shape[1])  # 30
```

Une colonne de longueur constante a une échelle de 1, donc aucune division par zéro. Une déviation positive est un indice descriptif, pas un verdict d’erreur.

**Exercice** : Le train contient ["al", "al", "ca", "ny"]. Calculez les fréquences de "al" et de "xx". Que se passe-t-il si vous ajoutez les valeurs de validation au compteur ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous identifiez au moins quatre endroits où une fuite peut se produire.

## 21. Contrats, coordonnées et fuite de données

Une caractéristique est admissible si elle est disponible au moment réel de la prédiction. La référence propre, un statut humain futur ou la différence dirty-clean sont des réponses, pas des entrées. Une colonne appelée « corrigé » serait une fuite de cible si elle n’existe qu’après vérification.
Un autre piège est la fuite de prétraitement : scaler, fréquences, médianes ou sélection de caractéristiques calculés sur toutes les partitions. Une Pipeline protège le scaler en l’ajustant lors de fit du modèle. Nos profils externes restent à surveiller séparément : ils sont ajustés uniquement sur les lignes train et recalculés dans chaque pli de CV.
Pour chaque vecteur, gardez un tableau de coordonnées contenant record_id, row_position, column et original_value. row_position sert au diagnostic, pas au modèle. L’ordre est ligne puis colonne ; la cible s’aplatit dans le même ordre. La revue humaine peut ainsi revenir exactement à la cellule concernée.
Les contrôles automatiques du pack vérifient notamment les en-têtes, l’unicité des clés, l’absence de groupes partagés, l’alignement des labels et la finitude de X. Ils ne prouvent pas la vérité métier de la référence ni l’absence de tout biais statistique.

**Darija (latin)** : Souel rassek : wach had information ghadi tkoun 3ndi mlli n-auditi fichier jdid ? Ila la, ma tdkhelhach f X. Coordonnées bach nrj3o l-khana ; machi bach modèle y7fed numéro dyal ligne.

**بالدارجة** : سول راسك: واش هاد المعلومة غادي تكون متوفرة وقت الاستعمال؟ إلا ما كانتش، ما تدخلهاش فميزات الموديل.

```text
assert len(X_train) == len(coords_train)
assert len(X_train) == y[parts["train"]].size
assert "record_id" not in features.feature_names
assert "target" not in features.feature_names
# Le test du pack compare aussi chaque coordonnée
# à la cellule dirty/clean dont elle provient.
```

La disponibilité doit aussi être temporelle : une information calculée après l’événement à prédire n’est pas licite seulement parce qu’elle se trouve maintenant dans le même CSV.

**Exercice** : Pour prédire un remboursement en retard, peut-on utiliser le commentaire « dette réglée après relance » écrit trois mois plus tard ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous faites un audit de disponibilité de chaque entrée d’un nouveau projet.

## 22. Les mathématiques utiles, sans détour

Une moyenne additionne les valeurs puis divise par leur nombre. La médiane partage les valeurs triées en deux moitiés : pour [2,2,3,100], elle vaut 2,5 tandis que la moyenne vaut 26,75. Une valeur extrême modifie donc fortement la moyenne. Le profil utilise la médiane pour la longueur et une moyenne pour les valeurs numériques décodées.
La variance mesure une dispersion moyenne au carré ; l’écart-type est sa racine carrée. Notre calcul NumPy utilise la convention de population ddof=0. Une standardisation transforme x en (x-moyenne_train)/écart_type_train. StandardScaler gère les caractéristiques constantes ; notre propre déviation utilise un plancher de 1 pour l’échelle.
Une probabilité est comprise entre 0 et 1. Un modèle peut renvoyer un score interprété comme une probabilité de classe, mais cette interprétation doit être vérifiée par calibration. Un score de 0,8 ne garantit pas que huit cellules sur dix ayant ce score sont réellement fausses, surtout après pondération des classes.
Un produit scalaire additionne des produits : w1*x1 + w2*x2 + ... + b. C’est le calcul central d’un classifieur linéaire. Vous pouvez commencer par comprendre le sens des poids et la séparation des données sans dériver à la main toute l’optimisation numérique.

**Darija (latin)** : Moyenne katjme3 w katqsem ; médiane hiya l-wast men be3d tri. Valeur kbira bzzaf katjerr moyenne. Score 0.8 ma howach wa3d belli 80% dyal had cas ghalat ; modèle khasso évaluation w calibration ila bghina had l-ma3na.

**بالدارجة** : المتوسط كيتأثر بالقيم الكبيرة، والوسيط أقل تأثراً بها. إلا كان التشتت صفر، خاص قاعدة واضحة باش ما نقسموش على الصفر.

```text
import numpy as np
values = np.array([2, 2, 3, 100], dtype=float)
print(values.mean())       # 26.75
print(np.median(values))   # 2.5
length = 8
median_train = 5
scale_train = 2
print(abs(length-median_train)/max(scale_train, 1))  # 1.5
```

La valeur absolue rend notre déviation positive. Elle perd le sens « trop court » ou « trop long ». Une amélioration future pourrait ajouter une déviation signée, mais elle doit être évaluée comme une modification distincte.

**Exercice** : Calculez la moyenne et la médiane de [4,4,4]. Quelle division pose problème sans convention de secours ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous calculez fréquence, médiane et déviation normalisée sur un petit exemple.

## 23. Apprentissage supervisé : fit, predict et score

Un apprentissage supervisé cherche une relation entre X et y à partir d’exemples étiquetés. Ici, X décrit une cellule et y indique son désaccord avec la référence. Le modèle ajuste des paramètres pour mieux distinguer les deux classes sur train. Il n’apprend pas une notion universelle de vérité des données.
fit réalise l’apprentissage. predict produit une décision de classe selon la règle du modèle. predict_proba produit des scores de classes. Dans nos modèles entraînés avec les deux classes 0 et 1, la colonne [:,1] correspond à la classe erreur. L’extension d’apprentissage actif gère explicitement le cas initial où une seule classe a été observée.
Le surapprentissage apparaît quand un modèle se spécialise trop sur les exemples de train. Un excellent F1 train avec un F1 validation faible est un signal d’alerte. Un modèle trop simple peut échouer sur les deux ensembles ; c’est une forme de sous-apprentissage. Plus de profondeur ou plus de variables n’améliorent pas automatiquement la généralisation.
La pondération balanced augmente le poids relatif de la classe rare dans l’apprentissage. Elle ne crée pas d’erreurs supplémentaires et ne remplace pas une évaluation. Elle peut augmenter le rappel et dégrader la précision ; son intérêt doit être mesuré sur validation.

**Darija (latin)** : Supervisé kay3ni 3ndna exemples m3a réponses. fit kayt3ellem men train. predict_proba kay3ti scores. Ila résultat dyal train zwin bzzaf w validation d3if, yqder modèle 7fed détails bla ma y3emmem.

**بالدارجة** : الموديل كيتعلم من أمثلة مع الأجوبة. نتيجة ممتازة فالتعلم وضعيفة فالتحقق تقدر تعني أنه حفظ التفاصيل وما تعلمش يعمم.

```text
from sklearn.tree import DecisionTreeClassifier
X = [[0, 0], [0, 1], [1, 8], [1, 9]]
y = [0, 0, 1, 1]
model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)
print(model.classes_)  # [0 1]
print(model.predict_proba([[1, 7]]))
# Exemple minuscule pour comprendre l'API, pas un benchmark.
```

Un score parfait sur quatre exemples ne permet aucune conclusion sur un nouveau fichier. L’exemple isole l’usage de l’API ; la vraie conclusion vient du protocole groupé.

**Exercice** : Que change balanced : la proportion réelle d’erreurs dans le test ou le coût des classes pendant fit ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous distinguez paramètres appris, hyperparamètres choisis et seuil de décision.

## 24. Régression logistique : un premier modèle

Malgré son nom, la régression logistique sert ici à une classification binaire. Elle calcule z=b+somme(wj*xj), puis applique la fonction sigmoïde p=1/(1+exp(-z)). Un poids positif augmente le score quand sa caractéristique augmente, toutes les autres entrées restant fixes.
Les échelles comptent : une longueur de 180 et un ratio de 0,2 ne jouent pas sur les mêmes amplitudes. StandardScaler centre et réduit les caractéristiques à partir de train. La Pipeline enchaîne scaler et modèle ; lorsque vous appelez fit, les deux apprennent uniquement sur les exemples transmis.
La régularisation limite les poids trop extrêmes. Le pack garde C à sa valeur par défaut et fixe max_iter=2000 pour laisser l’optimiseur converger. Il compare le modèle sans pondération et avec class_weight="balanced". Le nombre d’essais reste limité et annoncé pour réduire la tentation de chercher indéfiniment un bon résultat de validation.
Les coefficients standardisés aident à interpréter le modèle, mais ne prouvent pas une relation causale. Deux caractéristiques corrélées peuvent se partager un effet. Le score exprime une combinaison des entrées ; les indicateurs affichés dans l’interface sont des observations de règles et de profils, pas une explication causale exacte de chaque score.

**Darija (latin)** : Régression logistique katjme3 features b poids w kat7wel résultat l score bin 0 w 1. StandardScaler kayqerreb échelles. Poids positif kaytelle3 score ila feature zadet, walakin ma kay3nich sabab 7aqiqi dyal erreur.

**بالدارجة** : الموديل الخطي كيحسب مجموع الميزات بالأوزان، ومن بعد كيحوّلو لسكور. الأوزان كتشرح الحساب، وما كتثبتش السبب الحقيقي ديال الخطأ.

```text
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=2000, random_state=42)
)
# X_train et y_train viennent uniquement de train.
model.fit(X_train, y_train)
scores_val = model.predict_proba(X_val)[:, 1]
```

Dans cet extrait, y_train désigne y[parts["train"]].ravel(). Les variables X proviennent de la leçon 20. Pour un script autonome complet, utilisez auditor.py et src/experiment.py dans l’annexe.

**Exercice** : Pour z=0, calculez la sigmoïde. Si le seuil vaut 0,6, cette cellule est-elle signalée ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous expliquez pourquoi scaler.fit ne doit pas recevoir validation ni test.

## 25. Arbre de décision : des questions successives

Un arbre choisit des questions sur les caractéristiques : type_mismatch <= 0,5 ? longueur <= 12,5 ? fréquence <= 0,01 ? Chaque branche dirige les exemples vers une feuille contenant une estimation de leur répartition entre classes. Un arbre représente facilement certaines interactions non linéaires.
Le critère de Gini mesure l’impureté : 1-somme(pk²). Une feuille entièrement composée d’une seule classe a une impureté nulle. L’algorithme cherche des divisions réduisant l’impureté. Il ne sait pas si une règle correspond à une vérité métier ; il exploite les exemples reçus.
La profondeur maximale limite le nombre de questions successives. Le pack compare 2, 4, 6 et 8. min_samples_leaf=10 interdit les feuilles trop petites. Un arbre très profond peut mémoriser des particularités du train. Une normalisation n’est généralement pas nécessaire pour ces divisions par seuil.
L’importance d’une caractéristique calculée par l’arbre est descriptive et peut favoriser certaines variables. Inspectez les premiers nœuds, les métriques de validation et des exemples d’échecs. Un arbre interprétable n’est pas automatiquement un arbre juste ni stable sur de nouveaux fournisseurs.

**Darija (latin)** : Arbre kaysouel soualat b7al "format ghalet ?" w "longueur kbira ?". Profondeur kbira kat3tih détails bzzaf w yqder y7fed train. Khassna n9arno depths 2,4,6,8 3la validation, machi nkhtaro l-akbar direct.

**بالدارجة** : الشجرة كتسول أسئلة متتابعة. إلا عطيناها عمق كبير بزاف، تقدر تحفظ تفاصيل التعلم، لذلك كنختارو الحجم باستعمال التحقق.

```text
from sklearn.tree import DecisionTreeClassifier, export_text
model = DecisionTreeClassifier(
    max_depth=4, min_samples_leaf=10,
    class_weight="balanced", random_state=42
)
model.fit(X_train, y_train)
print(export_text(model, feature_names=features.feature_names,
                  max_depth=2))
```

L’affichage tronqué aux premiers niveaux aide à expliquer le fonctionnement. Les seuils s’appliquent aux caractéristiques originales de l’arbre, contrairement aux entrées standardisées de la régression logistique.

**Exercice** : Calculez Gini pour une feuille de 10 cellules contenant 5 erreurs et 5 cellules correctes, puis pour 10 cellules correctes.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous reliez profondeur, complexité et écart train/validation.

## 26. Précision, rappel, F1 et matrice de confusion

La classe positive est l’erreur. TP : erreur signalée. FP : cellule correcte signalée. FN : erreur manquée. TN : cellule correcte non signalée. Une matrice avec lignes [vrai correct, vraie erreur] et colonnes [prédit correct, prédit erreur] contient [[TN,FP],[FN,TP]]. Déclarez cet ordre pour éviter les inversions.
Précision=TP/(TP+FP) répond : parmi mes alertes, quelle part est une vraie erreur ? Rappel=TP/(TP+FN) répond : parmi les erreurs présentes, quelle part ai-je trouvée ? F1=2*précision*rappel/(précision+rappel), ou 2TP/(2TP+FP+FN), équilibre les deux sans tenir compte des TN.
Exemple : sur 1000 cellules, 25 sont fausses. Le système produit 30 alertes dont 20 exactes : TP=20, FP=10, FN=5, TN=965. La précision vaut 66,67 %, le rappel 80 % et F1 vaut 72,73 %. Le coût dépend aussi du temps nécessaire pour vérifier les dix fausses alertes.
Quand une colonne ne contient aucune erreur, le rappel n’a pas d’interprétation empirique. Le code adopte zero_division=0 pour rester calculable et affiche error_support=0. Ne présentez pas ce zéro comme une preuve d’échec ou de réussite. Average precision résume le classement des scores ; ce n’est ni l’accuracy ni exactement l’aire trapézoïdale d’une courbe précision-rappel.

**Darija (latin)** : Précision : men alertes li 3titi, ch7al s7a7 ? Rappel : men erreurs li kaynin, ch7al lqiti ? FP kaydiye3 waqt l-moraja3a. FN howa erreur li fatet. Khassna njm3o métriques m3a effectifs, machi pourcentage bo7do.

**بالدارجة** : الدقة كتجاوب شحال من إنذار كان صحيح. الاسترجاع كيجاوب شحال من خطأ موجود لقيناه. خاص الأعداد مع النسب باش نفهمو النتيجة.

```text
from src.metrics import measures
import numpy as np
y = np.array([1, 1, 1, 0, 0, 0])
scores = np.array([.9, .8, .2, .7, .1, .05])
print(measures(y, scores, threshold=.5))
# TP=2, FP=1, FN=1, TN=2
# précision=rappel=F1=2/3
```

Le rapport final affiche des nombres et non seulement une courbe. Les cellules sont corrélées par fournisseur : une incertitude statistique exige un traitement par groupes, pas un rééchantillonnage naïf de cellules indépendantes.

**Exercice** : Un système annonce 90 % de précision mais seulement 10 % de rappel. Que vit l’utilisateur ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous reconstruisez TP, FP, FN et TN à partir d’une liste de six cellules.

## 27. Choisir un seuil et un budget de revue

Un modèle produit un classement ; le seuil transforme le classement en action. Baisser le seuil augmente ou conserve le nombre de cellules signalées. Le rappel ne diminue donc pas pour un ensemble fixe, mais la précision peut varier de façon non monotone. Le bon seuil dépend du compromis entre erreurs manquées et coût de vérification.
Le pack pré-déclare une grille de 0,05 à 0,95 par pas de 0,05. Pour chaque candidat, il retient le seuil au meilleur F1 de validation. En cas d’égalité entre seuils, il privilégie la précision puis le seuil le plus élevé. Le modèle global retenu est ensuite le premier candidat au F1 maximal, dans l’ordre fixé des essais.
Ce réglage optimise F1, pas une calibration probabiliste ni un coût économique explicite. Une variante métier peut fixer un rappel minimal ou limiter les alertes à K cellules. Precision@K mesure les erreurs trouvées parmi ces K cellules ; Recall@K les rapporte à toutes les erreurs du jeu étiqueté.
Avec un seuil choisi sur validation, les métriques de validation sont optimistes pour ce choix. Le test final apporte une estimation séparée. Pour estimer sans biais une procédure complète de recherche d’hyperparamètres, il faudrait une validation imbriquée par groupes, plus coûteuse.

**Darija (latin)** : Seuil howa niveau li mnno katbda alerte. Ila n9es, alertes kayketro w rappel ma kayn9esch 3la nafs fichier. Ila 3ndek waqt treje3 50 cellules, top-50 yqder ykoun règle d’action a7sen men seuil tabit.

**بالدارجة** : العتبة كتحدد منين كتبدا المراجعة. نختاروها على التحقق وحسب تكلفة العمل، وما نبدلوهاش بعدما نشوفو الاختبار النهائي.

```text
from src.metrics import choose_threshold, measures
threshold = choose_threshold(y_val, scores_val)
validation_result = measures(y_val, scores_val, threshold)
print(threshold, validation_result)
# À partir du gel : ne plus modifier ce seuil après le test.
# y_val = y[parts["validation"]].ravel()
```

Le pack ne réentraîne pas le modèle sur train+validation après ce choix. Il conserve le modèle appris sur train, ce qui évite de modifier la distribution des scores après le réglage du seuil.

**Exercice** : Vous changez le seuil de 0,6 à 0,2 après avoir vu le rappel test. Pouvez-vous encore appeler le résultat une évaluation finale indépendante ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous justifiez le seuil par un objectif annoncé et une partition appropriée.

## 28. Comparaison contrôlée et ablation

Une ablation retire ou ajoute un groupe de caractéristiques pour mesurer son apport. Ici, les variantes sans contexte utilisent les sept caractéristiques locales et dix-neuf indicateurs de colonne. Les variantes avec contexte ajoutent fréquence, déviation de longueur, déviation numérique et applicabilité numérique.
Gardez les mêmes données, labels, partitions et règles de mesure. Pour chaque famille et chaque variante, le pack applique la même procédure de recherche : pondération absente ou balanced ; pour les arbres, profondeurs 2,4,6,8 ; seuil choisi sur la même grille de validation. Il y a vingt candidats ML et deux baselines.
Comparer les meilleures variantes de chaque côté mesure l’effet de l’ajout de contexte accompagné de la même procédure de sélection. Ce n’est pas une expérience à hyperparamètres strictement constants. Le journal permet aussi une comparaison à famille, profondeur, pondération et seuil identiques pour isoler davantage l’effet des caractéristiques.
Un écart observé sur neuf fournisseurs test ne prouve pas une différence statistiquement significative. Rapportez la taille de l’écart et sa fragilité. Pour une estimation d’incertitude, une extension peut rééchantillonner les fournisseurs test avec remise, en conservant leurs cellules ensemble et sans retoucher les modèles.

**Darija (latin)** : Ablation katjaweb : wach contexte zad chi 7aja ? Khass nafs split w nafs procédure. Ila bdelti features w profondeur w dataset f nafs waqt, ma tqderch tgol sabab men features bo7dhom. Farq sghir ma howach preuve dyal significativité.

**بالدارجة** : باش نقارنو بإنصاف، خلي نفس البيانات والتقسيم والمقياس. وضح واش بدلت غير الميزات أو حتى طريقة اختيار الإعدادات.

```text
import pandas as pd
runs = pd.read_csv("artifacts/hospital/validation_experiments.csv")
ml = runs[runs["family"].notna()]
comparison = ml.groupby(["family", "context"])["f1"].max()
print(comparison)
# Comparaison à réglage constant : filtrer aussi depth,
# weighted et threshold avant de calculer les écarts.
```

Une amélioration de F1 peut cacher une perte de rappel sur une colonne précise. Examinez les métriques par colonne et des erreurs concrètes avant de conclure à un gain utile.

**Exercice** : Vous ajoutez le contexte et changez simultanément le seuil. Quel résultat l’expérience permet-elle d’attribuer ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous annoncez exactement ce qui varie et ce qui reste contrôlé dans une expérience.

## 29. Validation croisée et analyse des erreurs

Une validation croisée par groupes divise les fournisseurs train en plusieurs plis. À chaque tour, on apprend sur certains groupes et on évalue sur les autres. Chaque pli doit réapprendre ses profils de colonnes et son scaler. Pré-calculer une seule matrice contextuelle sur tout train avant les plis ferait fuiter la distribution des groupes de validation internes.
La commande cv du pack effectue trois plis sur les fournisseurs du train seulement. Elle utilise la configuration choisie sur la validation externe et un seuil fixe de 0,5. C’est un diagnostic de sensibilité aux groupes, pas une estimation imbriquée et indépendante de toute sélection. Le F1 ne se compare donc pas directement au F1 au seuil optimisé du rapport final.
Analysez aussi les FP et FN sur validation. Un nom correct et rare peut recevoir une faible fréquence. Une faute qui conserve longueur et forme peut rester invisible. Un identifiant corrompu peut violer un format tandis qu’un téléphone incorrect de dix chiffres ne le viole pas.
Le pack extrait jusqu’à dix exemples de chaque type ; s’il en existe moins, il conserve ceux disponibles. Notez pour chaque erreur la colonne, le profil, les caractéristiques, le score, la décision et une hypothèse. Une hypothèse n’est pas une preuve : ne multipliez pas les ajustements sans nouvelle comparaison contrôlée.

**Darija (latin)** : CV b groupes katbdel achmen hôpitaux ntmerrno 3lihom w achmen nqeymo 3lihom. F kol pli, profils khasshom yt3awdo men partie train dyalo. Chof FP w FN bach tfhem chno modèle kayfout, machi ghir bach ttelle3 score.

**بالدارجة** : فكل طية ديال التحقق خاص الإحصائيات تتعلم من الجزء ديال التعلم ديالها. راجع الإنذارات الكاذبة والأخطاء اللي فاتت باش تفهم الحدود.

```text
python auditor.py cv --data data/hospital --out artifacts/hospital
# Produit train_group_cv.csv
# Ouvrir aussi :
# validation_errors.csv
# validation_per_column.csv
```

Si vous utilisez les résultats CV pour modifier le système, faites ces choix avant le gel scientifique final et gardez le journal. Le pack fige automatiquement l’expérience entraînée ; créez un nouveau dossier pour une étude de développement distincte.

**Exercice** : Pourquoi les profils doivent-ils être recalculés dans chaque pli même s’ils n’utilisent pas y ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous expliquez une fausse alerte, une erreur manquée et une limite de votre CV.

## 30. Comprendre le lancement de bout en bout

Le point d’entrée auditor.py organise les commandes ; il n’est pas le lieu où toute la logique est mélangée. src/data.py lit et aligne. src/features.py construit X. src/metrics.py mesure les résultats. src/experiment.py entraîne, sélectionne et évalue. src/predict.py produit le tableau de revue.
train charge les deux CSV, crée les groupes et le split, apprend les profils sur train, entraîne vingt candidats, choisit leurs seuils sur validation, écrit les diagnostics puis fige le bundle. Aucun résultat test n’est utilisé pour ce choix. Le modèle retenu reste entraîné sur train uniquement.
evaluate vérifie les empreintes des données et artefacts, reprend les clés test enregistrées et évalue les deux baselines ainsi que les variantes retenues de chaque famille et ablation. Le meilleur modèle global a déjà été choisi sur validation ; on ne le remplace pas par le gagnant apparent du test.
Les artefacts d’exemple sont livrés avec leurs résultats. Pour reconstruire le pipeline, utilisez un nouveau dossier comme artifacts/mon_hospital. Une expérience déjà figée n’est pas écrasée. La commande evaluate refuse une deuxième évaluation si test_metrics.csv existe : c’est un garde-fou pédagogique, pas une protection contre toute manipulation volontaire.

**Darija (latin)** : Ma khasskch tlesseq kol code f fichier wa7ed. Kol module 3ndo rôle. train kaykhtar b validation, evaluate kayqis test mlli kolchi wajed. Ila bghiti t3awed tajriba, dir dossier jdid w sejjel 3lach, ma tqellebch 3la seed li kay3ejbek.

**بالدارجة** : البرنامج النهائي مراحل مربوطة، وكل ملف عندو دور. خاصك تقدر تتبع الخانة من القراءة حتى لائحة المراجعة بلا ما تضيع.

```text
python -m pytest -q
python auditor.py inspect --data data/hospital
python auditor.py train --data data/hospital --out artifacts/mon_hospital
python auditor.py cv --data data/hospital --out artifacts/mon_hospital
# Quand les choix sont figés :
python auditor.py evaluate --data data/hospital --out artifacts/mon_hospital
python auditor.py predict --input data/hospital/dirty.csv   --artifacts artifacts/mon_hospital --output reports/mon_triage.csv
```

Les longues commandes peuvent être écrites sur une seule ligne. Le caractère de continuation \ convient à Bash ; sous PowerShell, collez la commande complète sur une ligne.

**Exercice** : Quelle commande doit fonctionner sans clean.csv ? Et laquelle exige une référence propre ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous exécutez les quatre commandes et retrouvez les fichiers de sortie.

## 31. Lire les résultats sans les survendre

Le chapitre de résultats mesurés qui suit les leçons est produit à partir des fichiers CSV réellement générés par le pack. Les nombres ne sont pas des objectifs de performance. Ils correspondent à un instantané précis du dataset, à la graine 42, à un split par fournisseur et aux hypothèses de caractéristiques décrites ici.
Le journal validation_experiments.csv contient les configurations, seuils, F1 train et métriques de validation. test_metrics.csv contient les baselines et les variantes choisies avant le test. test_per_column.csv décrit le modèle retenu globalement sur validation. Un autre modèle peut afficher un meilleur F1 test par hasard ; cela ne justifie pas un changement de sélection après coup.
Le dénominateur correct exclut index : Hospital contient 1 000 lignes, 19 colonnes métier et 509 différences, soit environ 2,679 % d’erreurs sur 19 000 cellules. La feuille de route compte vingt colonnes en incluant l’index ; l’utiliser comme dénominateur des cellules auditées sous-estimerait légèrement la prévalence. Le cours explicite cette correction de lecture.
Les performances sont limitées par la petite quantité de fournisseurs, la référence disponible, les corruptions présentes et les règles de parsing. Le projet ne démontre pas une capacité à auditer n’importe quel CSV, ni à corriger toutes les fautes, ni à garantir 95 % de performance. Un modèle inférieur aux règles reste un résultat exploitable si l’analyse est honnête.

**Darija (latin)** : Nombres li f rapport jayyin men exécution, machi exemples mtkheylin. Ma ngoulouch modèle kaykhdem f ay CSV. Kaykhdem f had schéma w had protocole. Ila modèle ma zadch, kanketbo résultat b sara7a w kanfessro limites.

**بالدارجة** : نشر الأرقام كاملة هو جزء من العمل العلمي. النتيجة كتخص هاد البيانات وهاد التقسيم، وماشي وعد بأن الموديل غادي يخدم فنفس المستوى دائماً.

```text
import json
import pandas as pd
from pathlib import Path
folder = Path("artifacts/hospital")
manifest = json.loads((folder/"manifest.json").read_text())
print("Choix sur validation :", manifest["selected"])
print(pd.read_csv(folder/"test_metrics.csv")[
    ["name", "precision", "recall", "f1", "error_support"]])
```

Le score au seuil choisi et la qualité de classement ne sont pas identiques. Rapportez aussi la charge de revue : nombre d’alertes = TP+FP. Pour un usage humain, cela rend le résultat plus concret qu’un F1 isolé.

**Exercice** : Une méthode a F1=0,80 sur validation et 0,63 sur test. Peut-on conserver seulement le premier nombre dans la conclusion ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous rédigez trois phrases de conclusion comprenant résultat, protocole et limite.

## 32. Sauvegarder et prédire sans référence

Un modèle utilisable comprend plus que ses coefficients. Le bundle conserve les profils de colonnes, les transformations, le modèle, les noms de caractéristiques et le seuil. Les fichiers JSON décrivent schéma, sélection, versions et empreintes. Oublier les profils rendrait l’inférence incohérente avec l’apprentissage.
Lors de predict, on lit le CSV sale, vérifie son schéma, reconstruit X avec les profils sauvegardés, calcule les scores puis trie les cellules. Le fichier propre n’est pas consulté. Une nouvelle valeur reçoit une fréquence nulle dans le profil ; elle n’est pas ajoutée au dictionnaire pendant l’audit.
Le tableau contient record_id, row_position, column, original_value, suspicion_score, flagged, review_indicators, human_status, human_comment et human_label. Les indicateurs décrivent manque, format et nouveauté observés. Ils ne constituent pas une décomposition fidèle du calcul du modèle.
L’export protège les cellules commençant par un préfixe de formule de tableur en ajoutant une apostrophe. La représentation exportée peut donc contenir cette apostrophe ; le CSV source reste intact. Chargez uniquement des bundles joblib de confiance. Pour une application publique, un format de sérialisation restreint et une politique d’accès seraient des travaux supplémentaires.

**Darija (latin)** : Bach modèle ybqa kaykhdem, khass sauvegarde dyal profils w seuil, machi coefficients bo7dhom. Predict ma kay7tajch clean. Tableau dyal revue kaykhelli l-valeur l-asliya bach bnadem yqder yraje3 w ykteb décision.

**بالدارجة** : حفظ الموديل بوحدو ما كافيش: خاص الإحصائيات وترتيب الميزات والعتبة. فالتنبؤ كنحتاجو الملف الوسخ والموديل، وما كنحتاجوش الملف النقي.

```text
python auditor.py predict --input data/hospital/dirty.csv   --artifacts artifacts/hospital --output reports/triage.csv

# En Python :
from src.data import read_table
from src.predict import audit
frame = read_table("data/hospital/dirty.csv")
review = audit(frame, "artifacts/hospital")
print(review.head(5))
```

Le tableau est classé sur le fichier entier pour illustrer l’outil. Il contient des lignes ayant servi à l’apprentissage : on n’en déduit aucune nouvelle métrique de généralisation. Les métriques indépendantes viennent du sous-ensemble test enregistré.

**Exercice** : Pourquoi recalculer les fréquences sur le fichier uploadé changerait-il le comportement du système ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous pouvez retirer clean.csv d’un dossier d’inférence sans empêcher predict.

## 33. Interface Streamlit et revue humaine

Streamlit transforme un script Python en interface locale. L’application propose un upload CSV, un aperçu de vingt lignes, un compteur d’alertes, un tableau trié et le téléchargement de la revue. Elle utilise le même backend que la CLI, ce qui réduit le risque d’avoir deux implémentations divergentes.
Le choix du modèle pointe sur artifacts/hospital ou artifacts/demo. Pour afficher votre propre expérience, remplacez ou étendez cette liste explicitement dans app.py avant de lancer l’application. L’interface indique si le modèle n’a pas encore été préparé. Le seuil provient du bundle figé et n’est pas réglé librement sur le test.
L’application limite cette démo à 5 Mo et 5 000 lignes, contrôle le contenu et présente les erreurs de schéma. Elle affiche au plus 1 000 lignes de revue mais exporte la liste complète. L’extension .csv du fichier ne garantit pas sa validité : le lecteur doit encore vérifier les en-têtes et les lignes.
La revue humaine reste un workflow simple : télécharger le tableau, renseigner human_status avec confirme_erreur, correct ou incertain, puis ajouter un commentaire et éventuellement une étiquette 0/1. Le pack ne réentraîne pas automatiquement un modèle à partir de ces colonnes. Une extension devra valider les clés, dater les décisions et séparer les données de développement.

**Darija (latin)** : Interface katsehel upload w lecture dyal alertes. Nefs code dyal CLI howa li kay7seb scores. Human_status ma howach réponse automatique : nta li katraje3. Ila bghiti t3ellem men revue, khass protocole jdid bach ma ydkholch test f train.

**بالدارجة** : الواجهة كتسهل الاستعمال، ولكن نفس الحساب خاصو يبقى فالخلفية. الإنسان كيراجع الإنذار وكيكتب القرار؛ إعادة التعلم ماشي تلقائية.

```text
python -m streamlit run app.py
# Ouvrir l'adresse locale affichée dans le terminal.
# Importer data/hospital/dirty.csv.
# Filtrer les alertes puis télécharger triage.csv.
# Arrêter le serveur avec Ctrl+C.
```

Le pack a vérifié le scénario upload et téléchargement avec les outils de test Streamlit. Cela ne constitue pas un déploiement public sécurisé ni un service multiutilisateur.

**Exercice** : Un utilisateur importe un CSV clients avec email et revenu. L’interface doit-elle tenter de l’auditer avec le modèle Hospital ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous démontrez l’application avec un bon fichier et un fichier invalide.

## 34. Dépannage : comprendre les échecs fréquents

« No module named pandas » signifie que le Python courant ne voit pas la bibliothèque. Vérifiez sys.executable et utilisez python -m pip dans le même environnement. Si Python est trop récent pour les versions fixées, créez l’environnement avec Python 3.12. Le projet n’exige pas de GPU.
« Schéma incorrect » indique des colonnes absentes ou inattendues. Comparez les en-têtes à COLUMNS et index ; ne renommez pas au hasard des champs métier différents. « Clé index doit être unique » révèle des doublons qui empêchent un alignement univoque. Définissez une vraie clé de ligne en amont plutôt que supprimer silencieusement des observations.
« Expérience déjà figée » vous invite à utiliser un autre dossier pour un nouveau développement. « Artefact modifié » signifie que les empreintes ne correspondent plus. Reconstituez une expérience cohérente depuis les mêmes données et le code voulu. Ne désactivez pas une vérification pour faire disparaître le message.
Un mauvais score n’est pas un bug à lui seul. Vérifiez la cible, les supports, la correspondance des coordonnées, les unités de score/sample et l’absence de fuite. Ensuite examinez les faux positifs et négatifs. Ajouter une bibliothèque plus complexe avant ce diagnostic masque souvent le vrai problème.

**Darija (latin)** : Message dyal erreur kay3ti piste. Ma tmse7ch contrôle bach code ydouz. Chof environnement, chemin, schéma, unités, w labels. F1 d3if yqder ykoun résultat réel, machi darori faute f code.

**بالدارجة** : ما تمسحش التحقق باش رسالة الخطأ تختفي. راجع البيئة والمسار والمخطط والوحدات. نتيجة ضعيفة تقدر تكون حد حقيقي، ماشي عطب فالبرنامج.

```text
python --version
python -c "import sys; print(sys.executable)"
python -m pip show pandas scikit-learn
python -m pytest -q
python auditor.py --help
python auditor.py predict --help
```

Si une installation échoue sans connexion, les CSV et scripts restent disponibles mais les bibliothèques doivent être installées depuis un cache ou une connexion ultérieure. Le ZIP ne contient pas l’environnement Python ni toutes ses roues binaires.

**Exercice** : Après un changement de dossier, predict ne trouve plus artifacts/hospital. Quel est le premier contrôle ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous diagnostiquez un échec sans effacer les données ni contourner les contrats.

## 35. Extension : apprentissage actif et budget

L’apprentissage actif cherche quelles cellules faire annoter avec un budget limité. Ce n’est pas la même question que choisir les cellules les plus probablement fausses. L’incertitude choisit des exemples proches de la frontière pour apprendre ; le classement de suspicion vise des erreurs probables pour les trouver rapidement.
Le script active_learning.py compare uncertainty et random, sur un pool composé uniquement des fournisseurs train. Chaque politique part des mêmes dix cellules pour une graine donnée. Chaque cellule inspectée compte dans le budget total, y compris celles de départ. Les mesures sont enregistrées aux budgets 20,50,100, sur cinq graines fixées.
À chaque étape, on révèle le label de la cellule choisie et on réentraîne. Si les labels initiaux ne contiennent qu’une classe, un DummyClassifier permet de continuer sans regarder en secret des labels pour équilibrer le départ. Les égalités d’incertitude sont départagées par une permutation reproductible.
Les profils utilisent le pool train non annoté ; les labels ne servent pas à les ajuster. Les courbes de performance pendant le développement portent sur validation, jamais sur test. Cela corrige une ambiguïté de la feuille de route qui suggérait des courbes test à chaque budget tout en demandant un test scellé. Choisissez d’abord politique et budget ; une comparaison finale pré-déclarée peut ensuite être évaluée une fois sur un test indépendant.

**Darija (latin)** : Active learning kayqelleb 3la cellules li yqedro y3ellmo modèle, machi darori li score dyal erreur dyalhom kbir. Budget kay7seb ga3 cellules li trej3at, 7ta 10 lwelin. Test ma nlemsouch f kol étape.

**بالدارجة** : التعلم النشط كيختار أمثلة باش يتعلم منها. كل مراجعة كتتحسب فالميزانية، حتى الأمثلة الأولى، والاختبار النهائي كيبقى خارج التجارب.

```text
python active_learning.py --data data/hospital   --artifacts artifacts/hospital
# Sortie : active_learning_validation.csv
# Comparer par budget : moyenne et dispersion sur 5 graines.
# Ne pas interpréter un seul tirage favorable comme preuve.
```

La simulation révèle la référence comme si un humain répondait sans erreur. Un vrai annotateur coûte du temps et peut se tromper ; cet écart fait partie des limites à annoncer. Les résultats de cette extension sont séparés du benchmark du modèle entraîné avec tous les labels train.

**Exercice** : Si les dix cellules initiales ne contiennent aucune erreur, est-il acceptable d’explorer les labels cachés gratuitement jusqu’à en trouver une ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous distinguez acquisition pour apprendre et triage pour découvrir des erreurs.

## 36. Rapport académique et soutenance

Le rapport doit permettre à un autre groupe de reconstruire l’expérience. Présentez le problème, l’utilisateur visé, le schéma, la provenance du dataset, la définition exacte de l’erreur, les contrôles de labels et le regroupement des fournisseurs. Décrivez ensuite les caractéristiques, baselines, modèles, paramètres et procédure de choix de seuil.
Dans les résultats, distinguez validation et test. Fournissez des effectifs, précision, rappel, F1, average precision lorsque définie et charge de revue. Ajoutez une ablation explicite et deux analyses de cas : une fausse alerte et une erreur manquée. Faites suivre les limites et les commandes de reproduction.
Pour dix minutes de présentation à trois, consacrez environ deux minutes au problème et aux données, une minute au split et à y, deux minutes aux caractéristiques et modèles, deux minutes aux résultats, puis trois minutes à la démonstration et aux questions. Chaque membre doit pouvoir répondre sur l’ensemble du pipeline.
La contribution du projet peut être une comparaison empirique rigoureuse et un outil reproductible ; elle n’exige pas d’inventer un nouvel algorithme si cela correspond aux critères du cours. Faites confirmer ces critères par l’enseignant. Ne présentez pas la régression logistique ou l’arbre comme vos propres inventions.

**Darija (latin)** : F soutenance, chra7 problème, labels, split, features, résultats, w limites. Ila sowlouk 3lach ML, jawb b comparaison réelle m3a règles. Ila règles 7sen, golha b sara7a. Contribution yqder tkoun méthodologie w outil mratab.

**بالدارجة** : فالعرض شرح المشكلة والبيانات والتقسيم والنتائج والحدود. كل عضو خاصو يفهم المشروع كامل، والنتيجة الصادقة أهم من المبالغة.

```text
Structure conseillée de reports/final_report.md :
1. Problème et périmètre
2. Données, provenance et labels
3. Protocole et prévention des fuites
4. Baselines, caractéristiques et modèles
5. Résultats, ablation et cas d'erreur
6. Limites et pistes
7. Reproduction et répartition du travail
```

Le pack fournit un rapport d’exécution avec les vrais résultats. Complétez l’analyse métier, la revue humaine et les responsabilités personnelles ; n’inventez pas des observations de terrain non effectuées.

**Exercice** : Préparez une réponse de trente secondes à « Pourquoi pas uniquement des règles ? »

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous pouvez défendre une hypothèse, une mesure et une limite sans lire vos diapositives.

## 37. Planning réaliste et jalons

Avant les huit semaines du projet, terminez les bases jusqu’au mini-auditeur sans ML. Cette préparation est réussie quand vous pouvez lire un CSV, écrire une fonction de validation et expliquer une exception. Le temps supplémentaire dépend de votre expérience ; ne sacrifiez pas les bases pour respecter artificiellement une date.
Semaine 1 : environnement, Git, lecture CSV et règles. Semaine 2 : schéma, alignement, labels, contrôle manuel et split sauvegardé. Semaine 3 : caractéristiques locales, profils train et tests de coordonnées. Semaine 4 : régression logistique et arbre, premier journal de validation.
Semaine 5 : matrice de confusion, ablation, seuil et analyse d’erreurs. Semaine 6 : CV par fournisseurs, une amélioration contrôlée et gel du pipeline. Semaine 7 : interface, export et tests de fichiers invalides. Semaine 8 : test final, rapport et répétition de soutenance. L’apprentissage actif vient seulement si le cœur fonctionne et s’il reste du temps.
À trois, chaque semaine comporte une petite tâche d’intégration commune. Définissez « terminé » par un résultat exécutable, un test pertinent, une relecture et une explication orale. Si vous travaillez seul, utilisez les trois rôles à des moments différents : auteur, testeur et critique.

**Darija (latin)** : Planning ma howach ghir dates. Kol semaine khass résultat kaykhdem w nta katfhemo. Ila projet mazal ma kaydourch men début l fin, ma tzidch active learning ou fonctionnalités jdadin. Sali l-core lwel.

**بالدارجة** : كل أسبوع خاص نتيجة كتخدم وتقدر تشرحها. إلا الأساس باقي ما خدامش من الأول للآخر، كملو قبل الإضافات الاختيارية.

```text
Séance type de 90 minutes :
15 min : rappeler le concept sans notes
45 min : coder une seule étape
20 min : vérifier sur un exemple contrôlé
10 min : noter résultat, bug et prochaine action

Jalon final : une autre personne lance le README sans aide.
```

Un retard sur les profils ou les labels doit déplacer les tâches avancées. Un joli écran ne compense pas un protocole qui mélange les fournisseurs entre train et test.

**Exercice** : Il reste deux jours et l’interface fonctionne, mais les labels sont alignés par position. Quelle priorité ?

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Chaque tâche possède une preuve de fin et une personne capable de l’expliquer.

## 38. Adapter la méthode à un autre projet

Pour un nouveau projet tabulaire, commencez par la décision à soutenir. Une fraude se prédit souvent par transaction ; un défaut par pièce ; une erreur de données par cellule. L’unité d’exemple détermine X, y, les coordonnées et les métriques. Ne copiez pas l’aplatissement des cellules pour un problème qui exige une cible par ligne.
Définissez ensuite la référence et sa disponibilité. Qui annote ? Avec quelle fiabilité ? Quand les entrées sont-elles connues ? Quelle entité partage des observations : client, machine, établissement, utilisateur ? Un split groupé ou temporel doit reproduire le scénario d’usage réel.
Créez une baseline simple et des caractéristiques compréhensibles. Conservez le principe fit sur train, transform ailleurs. Choisissez la métrique selon le coût des erreurs. Un problème de régression demande d’autres modèles et métriques, comme une erreur absolue moyenne ; un problème sans labels ne peut pas être évalué comme notre classification supervisée.
Avant le déploiement, contrôlez la dérive : schéma, taux de manque, fréquences inconnues, volume d’alertes et échantillon revu humainement. Une dérive ne justifie pas un réentraînement automatique sans labels fiables et protocole. Versionnez les données, décisions et modèles.

**Darija (latin)** : B had cours tqder tbni projets qrab, walakin machi tnsekh code bla ma tbeddel problème. Souel : chno exemple ? chno cible ? chno groupe ? chno information motaha f waqt prédiction ? Mn be3d modèles kayjiw.

**بالدارجة** : فمشروع جديد، عرف المثال والهدف والمجموعات والمعلومات المتوفرة وقت التنبؤ. نفس المنهجية كتنتقل، ولكن القواعد والمقاييس كتتبدل.

```text
Fiche de transfert :
Décision : quelles actions après une prédiction ?
Exemple : cellule, ligne, document, événement ?
Cible : qui sait la vraie réponse et quand ?
Split : client / machine / temps / fournisseur ?
Baseline : règle ou prédiction constante ?
Mesure : coût FP, coût FN, budget humain ?
Livraison : interface, artefacts et surveillance ?
```

Le template de nouveau projet inclus dans reports/ oblige à remplir ces choix avant d’entraîner un modèle. C’est cette démarche, plus que le choix d’un algorithme, qui rend la méthode transférable.

**Exercice** : Pour détecter des défauts de capteurs sur des machines déjà connues, proposez un split si la prédiction concerne le mois prochain.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous savez modifier le protocole au lieu de réutiliser mécaniquement celui d’Hospital.

## 39. Examen corrigé : vérifier sa compréhension

Essayez les dix questions sans consulter les corrections. 1. Pourquoi lire un téléphone en chaîne ? 2. Que représente y=1 ? 3. Pourquoi une clé unique ? 4. Pourquoi séparer par fournisseur ? 5. Où apprendre les fréquences ? 6. Pourquoi accuracy trompe-t-elle ici ? 7. Que mesure le rappel ? 8. À quoi sert validation ? 9. Predict a-t-il besoin de clean ? 10. Un score de 0,9 prouve-t-il une erreur ?
Pour chaque réponse, donnez un exemple concret du projet. Une définition récitée sans exemple ne vérifie pas la compréhension. Dessinez aussi le chemin d’une cellule depuis le CSV sale jusqu’à la ligne de revue : clé, valeur, caractéristiques, score, seuil, alerte et décision humaine.
Ajoutez trois questions de méthode : que faire si les règles battent ML ? que peut-on conclure d’un gain sur un seul split ? comment réutiliser des annotations humaines sans contaminer le test ? Ces questions distinguent un pipeline qui s’exécute d’un projet que vous pouvez défendre.
Enfin, expliquez la différence entre erreur de parsing, erreur de données et erreur de modèle. Une chaîne « 97% » rejetée par float brut est un problème de parsing de notre code ; un « 9x% » peut être une corruption ; une valeur correctement parsée mais mal classée est une erreur de prédiction.

**Darija (latin)** : Jerreb tjawb bla ma tchof correction. Ila qderti tfesser b exemple w tersem pipeline, rah fahm. Ila ghir katreded mots b7al leakage w F1 bla ma t7sebhom, rje3 l-exemples sghar.

**بالدارجة** : جاوب بلا ما تشوف التصحيح، وحسب بيدك. إلا قدرت تفسر كل جواب بمثال وتلقى خطأ فحساب آخر، راه الفهم ولى عملي.

```text
Mini-calcul :
100 cellules, 10 erreurs ; 12 alertes, dont 8 vraies erreurs.
TP = ? ; FP = ? ; FN = ? ; TN = ?
Précision = ? ; Rappel = ? ; F1 = ?

Mini-protocole :
Une ville nouvelle a une fréquence train de zéro.
Peut-on déclarer automatiquement cette ville fausse ?
```

Faites les calculs avant de comparer. La connaissance des métriques doit vous permettre de détecter une incohérence dans un rapport ou une présentation.

**Exercice** : Répondez aux dix questions et au mini-calcul. Pour chaque notion mal maîtrisée, indiquez la leçon à refaire.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous répondez correctement et pouvez justifier les réponses avec le code.

## 40. Projet autonome : reconstruire sans copier

Créez un nouveau dossier et reconstruisez d’abord un auditeur de trois colonnes : nom, age, code_postal. Écrivez votre propre schéma, un CSV propre et une copie sale. Introduisez des erreurs de formats et quelques erreurs plausibles. Ajoutez plusieurs lignes par personne ou foyer si votre scénario comporte cette dépendance, puis choisissez un split cohérent.
Commencez par les règles et leur matrice de confusion. Implémentez ensuite les caractéristiques locales, les profils train et un modèle simple. Conservez la comparaison exacte et les coordonnées. Choisissez un seuil sur validation. Une fois les choix figés, évaluez le test et rédigez une page expliquant ce qui est détecté et ce qui échappe.
Votre réussite se mesure à l’autonomie : un autre lecteur doit pouvoir comprendre les hypothèses et lancer votre projet. Le nombre de bibliothèques n’est pas un critère. Une solution courte, contrôlée et honnêtement mesurée vaut mieux qu’un modèle sophistiqué dont vous ne pouvez pas expliquer les entrées.
Après cet exercice, revenez au projet Hospital. Expliquez chaque module, supprimez mentalement une protection et prédisez le risque : index dans X, profil sur tout le fichier, clean mal aligné, seuil choisi sur test ou parsing d’unités absent. Si vous pouvez détecter ces erreurs sans aide, vous avez acquis une base solide pour les projets comparables.

**Darija (latin)** : Daba jerreb tbni version dyalek men zéro. Machi darori tkoun kbira. L-mohim tfhem choix, tkhteberhom, w tkteb limites. Ila qderti tbeddel dataset w tsawweb protocole bla ma t7taj nsekh kolchi, rah wselti l-hadaf.

**بالدارجة** : آخر تحدي هو تبني نسخة صغيرة ببيانات أخرى وتشرح كل اختيار. الاستقلالية هي تعرف تبدل المثال وتبقى الطريقة صحيحة.

```text
Livrables personnels :
- README avec installation et commandes
- données et fiche de provenance
- schéma et définition de y
- partitions conservées et tests des contrats
- baseline + modèle + métriques de validation/test
- tableau de revue sur un nouveau fichier
- une page de résultats et limites
```

Le schéma Hospital du pack n’accepte pas directement ce mini-projet : adaptez les constantes, règles, profils et tests dans votre copie. Cette adaptation est précisément l’exercice d’autonomie.

**Exercice** : Expliquez à un camarade, en cinq minutes, comment construire le projet sans lui montrer votre code.

**Corrigé** : consulter la section finale.

**Preuve de maîtrise** : Vous pouvez construire et défendre un nouveau petit projet tabulaire comparable.

# Six TP progressifs

## TP1. Des chaînes vers des règles fiables

Écrire des fonctions réutilisables sans détruire les valeurs brutes.

### Guidé
Exécutez lessons/02_csv_rules.py. Pour chaque ligne signalée, relevez la règle déclenchée. Modifiez uniquement une copie de toy10.csv : remplacez l’âge texte de Yassine par 22, puis vérifiez que son alerte disparaît et que les trois autres restent.

### À compléter
Complétez N1 is_missing et N2 digit_ratio dans ateliers/exercices_a_completer.py. Énoncez le résultat attendu pour "", "  ", "empty", "EMPTY", "ab12" et "01000" avant de lancer le vérificateur.

### Autonome
Écrivez votre propre validateur de code postal de cinq chiffres ASCII. Distinguez les catégories manquant et format invalide. Faites cinq exemples, dont un code qui commence par zéro.

### Preuve
N1 et N2 sont OK ; le tableau original conserve "01000" ; aucune exception sur une chaîne vide.

## TP2. Construire des labels qui ne dépendent pas de l’ordre

Protéger le lien entre chaque réponse et sa cellule.

### Guidé
Créez dirty={"A":"al", "B":"ca"} et clean={"B":"ny", "A":"al"}. Calculez les labels par clé. Inversez l’ordre du dictionnaire clean et expliquez pourquoi le résultat doit rester identique.

### À compléter
Complétez N4 aligned_labels. Refusez une clé absente, une clé supplémentaire et une différence d’ensemble de clés. Le fichier corrigé traite les dictionnaires ; le lecteur Hospital protège aussi les doublons dans le CSV.

### Autonome
Prenez six établissements avec deux lignes chacun. Construisez à la main une partition de trois groupes train, un validation et deux test. Vérifiez les intersections et expliquez pourquoi ces proportions ne doivent pas forcément être 60/20/20 dans cet exercice minuscule.

### Preuve
Labels attendus : A=0, B=1. Modifier l’ordre ne change rien. Une clé différente déclenche ValueError. Aucun groupe n’appartient à deux partitions.

## TP3. Apprendre un profil et tester une valeur inconnue

Appliquer fit sur train et transform ailleurs avec un exemple calculable.

### Guidé
Avec train=["al","al","ca","ny"], calculez fréquence("al") et fréquence("xx"). Ajoutez ensuite dix "xx" dans un tableau de validation séparé. Le profil train doit rester inchangé.

### À compléter
Complétez N3 column_frequency. Traitez aussi train=[] en renvoyant zéro, uniquement pour rendre cette fonction d’exercice définie. Dans un vrai entraînement, un train vide doit être rejeté.

### Autonome
Faites deux listes de longueurs : [2,2,2] puis [2,2,100]. Comparez moyenne et médiane. Proposez une règle pour éviter une division par zéro et expliquez ce qu’elle change à l’interprétation de la déviation.

### Preuve
Fréquences 0,5 et 0 ; aucune mutation du profil après validation ; déviation finie même si les longueurs du train sont constantes.

## TP4. Scores, décisions et charge de revue

Lire une matrice de confusion et choisir un seuil sur validation.

### Guidé
Exécutez python -m ateliers.trace_cinq_cellules. Reconstituez les cinq labels, les scores et la matrice au seuil 0,50. Vérifiez ensuite ce qui change au seuil 0,15.

### À compléter
Complétez N5 f1_from_counts. Vérifiez TP=8, FP=4, FN=2 puis TP=FP=FN=0. Ajoutez vous-même une fonction precision_from_counts qui protège les divisions nulles.

### Autonome
Imaginez un budget de deux revues : choisissez les deux plus hauts scores des cinq cellules. Distinguez le nombre d’erreurs découvertes du nombre d’erreurs présentes. Expliquez pourquoi choisir la meilleure politique sur un test déjà consulté serait un problème.

### Preuve
Au seuil 0,50 : TP=2, FP=0, FN=1, TN=2, F1=0,8. Au seuil 0,15 : TP=3, FP=1, FN=0, TN=1. Vous savez expliquer le faux positif ajouté.

## TP5. Lire un vrai diagnostic du modèle Hospital

Relier le code, les artefacts et des cellules concrètes de validation.

### Guidé
Exécutez python -m ateliers.diagnostic_hospital. Ouvrez reports/ateliers/diagnostic_validation.json. Pour la cellule 451/state, notez la valeur brute, la cible, le score, le seuil et le résultat de la comparaison.

### À compléter
Complétez N6 top_k : trier une liste de dictionnaires par score décroissant sans modifier l’original. Vérifiez aussi k=0 et une liste vide.

### Autonome
Exécutez predict sur une copie sale placée dans un dossier sans clean.csv. Puis importez un CSV au mauvais schéma dans Streamlit. Documentez une sortie correcte et un message de rejet, sans modifier les protections.

### Preuve
La prédiction n’exige aucune référence propre. Le mauvais schéma est rejeté clairement. Le diagnostic utilise la validation et ne réentraîne rien.

## TP6. Transférer la démarche et défendre ses choix

Reconstruire une comparaison et rédiger une conclusion vérifiable.

### Guidé
Lisez le projet clients du chapitre de transfert et reproduisez son entraînement dans artifacts/mes_clients. Comparez les règles et le modèle sur les résultats fournis avant d’interpréter le nombre de revues du fichier fresh.

### À compléter
Dans une copie de SCHEMAS et schema_mismatch, ajoutez un champ métier que vous savez définir et annoter. Modifiez aussi le générateur et les tests. Cette modification impose une nouvelle expérience et ne doit pas charger un ancien modèle.

### Autonome
Construisez un petit jeu d’inventaire différent du générateur : cinq colonnes, plusieurs lignes par produit, un schéma, une référence vérifiée et une baseline. Expliquez le scénario de généralisation, puis faites une démonstration de cinq minutes.

### Preuve
Vous annoncez unité d’exemple, cible, groupes, disponibilité des features, métrique, seuil, limites et commandes. Un autre lecteur peut reproduire votre travail.

# Corrigés des leçons

## 01. Ce que vous allez construire

Entrée : CSV Hospital sale. Sortie : liste de cellules classées par suspicion. Limite : une faute au format parfaitement plausible peut passer inaperçue.

## 02. Organiser son apprentissage

Exemple : séance 1, lancer un .py ; séance 2, valider quatre chaînes ; séance 3, lire toy10.csv ; séance 4, expliquer et corriger deux erreurs.

## 03. Terminal, Python et environnement virtuel

python --version ; dans un fichier : import sys puis print(sys.executable). Le chemin doit pointer vers l’environnement du projet.

## 04. Variables, types et calculs

int, float, str, bool, NoneType. Un téléphone n’est pas une quantité à additionner ; ses préfixes et zéros doivent être conservés.

## 05. Chaînes, espaces et expressions régulières

Seule "01000" passe. Notre schéma Hospital tolère toutefois quatre ou cinq chiffres, pour tenir compte des représentations héritées du benchmark ; ce choix doit être déclaré.

## 06. Conditions et logique booléenne

Si valeur == "empty", ne signalez pas le manque. Sinon convertissez en nombre puis signalez les valeurs hors de [0,100]. Traitez les conversions impossibles avec try/except.

## 07. Listes, dictionnaires, ensembles et boucles

a : 3/4 ; b : 1/4. H2 appartient alors au train et au test : la séparation par établissement n’est plus respectée.

## 08. Fonctions, modules et petits objets

def is_missing(value): return value.strip() in {"", "empty"}. Elle ne doit pas transformer la valeur originale enregistrée dans le tableau de revue.

## 09. Fichiers, CSV, JSON et exceptions

Deux conversions échouent : Yassine et Nadia. Imane possède un âge numérique négatif. Omar a un code postal invalide mais un âge acceptable.

## 10. Déboguer, tester et utiliser Git

Inversez l’ordre du CSV propre en conservant ses clés. Les étiquettes attendues doivent rester identiques. C’est le rôle de test_alignment_by_id_not_position.

## 11. NumPy, vecteurs et tableaux

y a la forme (11400,). X possède 11400 lignes et une colonne par caractéristique. Le projet utilise 26 caractéristiques sans contexte et 30 avec contexte.

## 12. Pandas : lire, sélectionner et résumer

mask = ~df["code_postal"].str.fullmatch(r"[0-9]{5}") ; df.loc[mask]. La ligne d’Omar doit être retenue.

## 13. Trois datasets pour progresser

Les suffixes ??? et les répétitions de texte sont des corruptions très visibles ; un modèle peut les repérer sans comprendre le domaine. Une substitution plausible serait plus difficile.

## 14. Dictionnaire de données et schéma

Un code postal est un identifiant catégoriel, pas une grandeur où une distance arithmétique exprime une anomalie. Le profil numérique est limité à score et sample.

## 15. Aligner les tables et fabriquer la cible

Non. clean = clean.loc[dirty.index, COLUMNS] impose explicitement le même ordre par clés. Le résultat ne dépend plus des positions initiales.

## 16. Exploration et déséquilibre des classes

Accuracy = 975/1000 = 97,5 %. Rappel = 0/25 = 0. Sa bonne accuracy ne traduit aucune capacité de détection.

## 17. Train, validation et test par groupes

Cela mélange des cellules dépendantes et peut exposer les mêmes fournisseurs dans chaque partition. Les résultats seraient trop favorables au scénario de nouveaux hôpitaux.

## 18. Baselines déterministes

Elle signale les nouveaux noms et adresses corrects, précisément fréquents chez les fournisseurs inconnus du test. Inconnu ne signifie pas incorrect.

## 19. Décrire une cellule sans son contexte

"12 3" : longueur 4, ratio chiffres 3/4, ratio espaces 1/4. Chaîne vide : longueur 0 et tous les ratios 0, avec manque=1.

## 20. Apprendre le contexte sur train uniquement

Fréquences : 0,5 et 0. Ajouter validation modifie les caractéristiques grâce à des données tenues à l’écart : c’est une fuite de distribution.

## 21. Contrats, coordonnées et fuite de données

Non pour une prédiction effectuée avant la relance. Cette information postérieure contient une partie de la réponse et ne sera pas disponible au moment prévu.

## 22. Les mathématiques utiles, sans détour

Les deux valent 4. L’écart-type vaut zéro : une division par cet écart-type serait impossible. On fixe ici un plancher documenté.

## 23. Apprentissage supervisé : fit, predict et score

Le coût des classes pendant fit. Le test conserve sa distribution naturelle et ses vrais effectifs.

## 24. Régression logistique : un premier modèle

La sigmoïde vaut 0,5. Avec la règle score >= 0,6, la cellule n’est pas signalée.

## 25. Arbre de décision : des questions successives

Premier cas : 1-(0,5²+0,5²)=0,5. Second cas : 1-(1²+0²)=0. Une feuille pure peut pourtant provenir d’un surapprentissage si elle généralise mal.

## 26. Précision, rappel, F1 et matrice de confusion

La plupart des alertes sont utiles, mais neuf erreurs sur dix restent invisibles. Ce réglage peut convenir à un très petit budget de revue, mais ne couvre pas un objectif de détection exhaustive.

## 27. Choisir un seuil et un budget de revue

Non. Le test a influencé le réglage. Il devient une source de développement ; une nouvelle évaluation indépendante serait nécessaire pour revendiquer cette indépendance.

## 28. Comparaison contrôlée et ablation

Elle mesure le pipeline complet modifié. Pour attribuer un gain au contexte seul, fixez les autres facteurs ou présentez explicitement la procédure de sélection identique de chaque variante.

## 29. Validation croisée et analyse des erreurs

Parce qu’ils utilisent la distribution des valeurs. Les groupes internes de validation influenceraient sinon les fréquences et médianes apprises, même sans leurs étiquettes.

## 30. Comprendre le lancement de bout en bout

predict doit fonctionner avec le CSV sale et les artefacts seulement. train et evaluate exigent la paire sale/propre. inspect compare également la paire.

## 31. Lire les résultats sans les survendre

Non. Le rapport doit distinguer le résultat utilisé pour choisir et celui utilisé pour évaluer. L’écart peut refléter suradaptation, variabilité des groupes ou différences de distribution.

## 32. Sauvegarder et prédire sans référence

Une valeur très répétée dans un nouvel upload deviendrait fréquente même si elle était inconnue du train. Le modèle recevrait alors des caractéristiques construites selon une autre procédure que celle évaluée.

## 33. Interface Streamlit et revue humaine

Non. Elle doit signaler un schéma incompatible. Transférer la méthode exige de nouvelles règles, données, étiquettes et évaluations, pas seulement un nouveau fichier.

## 34. Dépannage : comprendre les échecs fréquents

Vérifier le dossier courant puis l’existence du chemin relatif. Se placer dans projet_auditeur ou fournir un chemin absolu correct.

## 35. Extension : apprentissage actif et budget

Non. Toute inspection doit compter dans le budget. Le classifieur constant et l’aléa déclaré permettent de continuer sans annotation gratuite cachée.

## 36. Rapport académique et soutenance

Les règles vérifient des contraintes explicites. Les modèles combinent des indices statistiques. Nous comparons les deux sur les mêmes fournisseurs inconnus pour mesurer si cette complexité apporte une amélioration réelle.

## 37. Planning réaliste et jalons

Corriger et tester l’alignement, puis recalculer les expériences nécessaires avant le gel final. Reporter l’extension optionnelle. Sans labels fiables, les résultats n’ont pas de valeur.

## 38. Adapter la méthode à un autre projet

Un split temporel séparant passé et futur est naturel ; il faut aussi contrôler les séquences proches et calculer les profils avec le passé disponible. Un split uniquement par machine répondrait à une autre question.

## 39. Examen corrigé : vérifier sa compréhension

1 préserver format ; 2 différence exacte ; 3 alignement univoque ; 4 groupes inconnus ; 5 train ; 6 classe erreur rare ; 7 fraction d’erreurs trouvées ; 8 sélectionner ; 9 non ; 10 non. Calcul : TP=8, FP=4, FN=2, TN=86 ; précision=66,67 %, rappel=80 %, F1=72,73 %. Une ville nouvelle peut être correcte. Si les règles gagnent, rapporter le résultat. Un split seul donne une estimation fragile. Les nouvelles annotations restent dans un pool de développement séparé du test.

## 40. Projet autonome : reconstruire sans copier

Une explication complète suit le chemin : besoin, données, référence, groupes, règles, X/y, apprentissage, choix sur validation, gel, test, inférence et revue. Un oubli doit vous ramener à la leçon correspondante.

# Corrigés des TP

## TP1

N1 : value.strip() in {"", "empty"}. N2 : compter les caractères de "0123456789" puis diviser par max(len(value),1). Pour le code postal, reconnaître le manque d’abord, puis vérifier re.fullmatch(r"[0-9]{5}", value). Conserver la chaîne originale à côté du diagnostic.

## TP2

Vérifier set(dirty)==set(clean), puis {key:int(value != clean[key]) for key,value in dirty.items()}. Pour les groupes, choisir des ensembles disjoints puis attribuer chaque ligne à la partition de son établissement ; ne pas tirer les cellules séparément.

## TP3

La fréquence vaut count/len(train). Pour [2,2,100], moyenne=34,6667 et médiane=2. Pour [2,2,2], écart-type=0. Un plancher explicite comme max(écart-type,1) garde une valeur finie ; il impose une convention d’échelle, pas une vérité statistique.

## TP4

F1=2*TP/(2*TP+FP+FN), avec zéro si le dénominateur est nul. Top-2 sélectionne B et C : deux erreurs découvertes parmi trois présentes, donc rappel@2=2/3 et précision@2=1. D et E ont des caractéristiques identiques pour le score illustratif : aucun seuil ne les sépare.

## TP5

La cellule 451/state vaut "ak", est correcte par rapport à la référence, mais reçoit un score proche de 0,990770 : c’est un FP au seuil 0,35. Le profil train lui donne une fréquence nulle. Le détail des contributions explique le calcul linéaire ; il ne prouve pas une causalité métier. top_k utilise sorted(..., reverse=True)[:max(k,0)].

## TP6

Le transfert clients n’améliore pas F1 par rapport aux règles sur le test fourni : les deux valent environ 0,952. Sur inventaire, le modèle vaut environ 0,913 contre 0,810 pour les règles. Ces nombres décrivent deux jeux synthétiques ; ils ne remplacent pas une validation métier indépendante. Votre propre expérience doit conserver ses données, partitions et résultats.