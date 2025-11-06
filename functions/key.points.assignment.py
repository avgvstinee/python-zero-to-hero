
# Assignment to Parameters in Python Functions

value = 10

def func(val):
    val = 20 # defining a local variable (val) inside the function , not changing the global variable(value)

func(value)
print(value)  # Output: 10