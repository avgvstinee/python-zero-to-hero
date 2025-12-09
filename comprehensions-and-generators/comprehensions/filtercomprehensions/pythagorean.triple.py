# pythagorean.triple.py
from math import sqrt


# this will generate all possible pairs
maximum = 10
triples = [
    (a, b, sqrt(a**2 + b**2))
    for a in range(1, maximum)
    for b in range(a, maximum)
]
# this will filter out all non pythagorean triples
triples = list(
    filter(lambda triple: triple[2].is_integer(), triples)
)

print(triples)  # prints: [(3, 4, 5.0), (6, 8, 10.0)]