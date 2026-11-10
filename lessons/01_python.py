"""Bases : lancer python lessons/01_python.py."""
value = "01000"
print(value, len(value), type(value).__name__)
values = ["01000", "abc", "", "20000"]


def valid_zip(text):
    return len(text) == 5 and all(c in "0123456789" for c in text)


for text in values:
    print(repr(text), valid_zip(text))

frequencies = {}
for text in ["al", "al", "ca"]:
    frequencies[text] = frequencies.get(text, 0) + 1
print(frequencies)
