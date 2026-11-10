"""Compléter une fonction à la fois, puis lancer python -m ateliers.verifier_exercices."""


def is_missing(value):
    """N1 : True pour chaîne vide, espaces, texte exact empty ; False sinon."""
    raise NotImplementedError("N1 : remplacer cette ligne par votre solution")


def digit_ratio(value):
    """N2 : fraction de chiffres ASCII ; renvoyer 0.0 pour la chaîne vide."""
    raise NotImplementedError("N2")


def column_frequency(train_values, value):
    """N3 : fréquence calculée sur train ; zéro si train vide ou valeur inconnue."""
    raise NotImplementedError("N3")


def aligned_labels(dirty, clean):
    """N4 : dict clé->valeur ; renvoyer dict clé->0/1 ; refuser des clés différentes."""
    raise NotImplementedError("N4")


def f1_from_counts(tp, fp, fn):
    """N5 : F1 = 2*TP/(2*TP+FP+FN) ; zéro si le dénominateur est nul."""
    raise NotImplementedError("N5")


def top_k(records, k):
    """N6 : trier liste de dicts sur score décroissant, sans modifier l'original."""
    raise NotImplementedError("N6")
