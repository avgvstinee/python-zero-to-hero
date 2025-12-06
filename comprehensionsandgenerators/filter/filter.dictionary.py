
people = [
    {"name": "Aki", "score": 90},
    {"name": "Neo", "score": 40},
    {"name": "Lebo", "score": 75},
]

passed = list(filter(lambda p: p["score"] >= 50, people))
print(passed)