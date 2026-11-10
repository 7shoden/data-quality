"""Corrigés des six fonctions ; consulter après avoir essayé le fichier à compléter."""


def is_missing(value):
    return value.strip() in {"", "empty"}


def digit_ratio(value):
    return sum(c in "0123456789" for c in value) / max(len(value), 1)


def column_frequency(train_values, value):
    return train_values.count(value) / len(train_values) if train_values else 0.0


def aligned_labels(dirty, clean):
    if set(dirty) != set(clean):
        raise ValueError("Clés différentes")
    return {key: int(value != clean[key]) for key, value in dirty.items()}


def f1_from_counts(tp, fp, fn):
    denom = 2 * tp + fp + fn
    return 2 * tp / denom if denom else 0.0


def top_k(records, k):
    return sorted(records, key=lambda row: row["score"], reverse=True)[: max(k, 0)]
