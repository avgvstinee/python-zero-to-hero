
# Get the lengths of words in a list using map and len

names = ["Anna", "Bob", "Charlie", "Diana"]

lengths = list(map(len, names))

print(lengths)  # Output: [4, 3, 7, 5]


numbers = [1,2,3,4,5]

add = list(map(lambda a: a *2 , numbers))
print(add)  # Output: [1, 4, 9, 16, 25]