# pythagorean.triple.comprehension.py
from math import sqrt


# this step is the same as before
maximum = 10
triples = [
    (a, b, sqrt(a**2 + b**2))
    for a in range(1, maximum)
    for b in range(a, maximum)
]
# here we combine filter and map in one CLEAN list comprehension
triples = [
    (a, b, int(c)) for a, b, c in triples if c.is_integer()
]

print(triples)  # prints: [(3, 4, 5), (6, 8, 10)]