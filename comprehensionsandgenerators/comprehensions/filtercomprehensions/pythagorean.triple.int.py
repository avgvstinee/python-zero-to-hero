# pythagorean.triple.int.py
from math import sqrt


maximum = 10
triples = [
    (a, b, sqrt(a**2 + b**2))
    for a in range(1, maximum)
    for b in range(a, maximum)
]
triples = filter(lambda triple: triple[2].is_integer(), triples)

# this will make the third number in the tuples integer
triples = list(
    map(lambda triple: triple[:2] + (int(triple[2]),), triples)
)

print(triples)  # prints: [(3, 4, 5), (6, 8, 10)]