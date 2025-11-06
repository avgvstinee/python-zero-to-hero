
# Optional Parameters 

def func(a, b=5, c=8):
    print(a,b,c)

func(2)  # Output: 2 5 8
func(b=3, a=7, c=10)  # Output: 7 3 10
func(1, c=4)  # Output: 1 5 4
func(9, 6, 3)  # Output: 9 6 3
func(c=12, a=4)  # Output: 4 5 12

