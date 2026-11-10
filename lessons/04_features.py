"""Calcul manuel vérifiable d'un vecteur et d'un profil train."""
import numpy as np

train = ["al", "al", "ca", "ny"]
value = "xx"
frequency = train.count(value) / len(train)
length_deviation = abs(len(value)-np.median([len(v) for v in train]))
digit_ratio = sum(c in "0123456789" for c in value) / max(len(value), 1)
print([len(value), digit_ratio, frequency, length_deviation])
assert frequency == 0.0
assert length_deviation == 0.0
