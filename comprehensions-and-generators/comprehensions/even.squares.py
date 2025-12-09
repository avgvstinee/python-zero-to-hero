

# using a map and filter

even_square = list(map(lambda e : e **2 , filter(lambda s: not s % 2, range(10))))
print(even_square)  # Output: [0, 4, 16, 36, 64]

# using a comprehension

even_square_comprehension = [e ** 2 for e in range(10) if not e % 2]

print (even_square == even_square_comprehension)  # Output: True