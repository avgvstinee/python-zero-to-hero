
# Iterable unpacking 
# syntax : *iterable_name to unpack the values

def carName(make, model, year):
    print(make, model, year)
car = ["Toyota", "Corolla", 2020]
carName(*car)  # Output: Toyota Corolla 2020