
# Positional-only parameters 

def func(a, b, /,c):
    print(a, b,c)

func(1, 2, 3)  # Output: 1 2 3
func(4, 5, c=6)  # Output: 4 5
# func(a, b=8, c=9)  # This will raise a TypeError