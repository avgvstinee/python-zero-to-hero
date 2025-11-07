
# Recurvise factorial 

def factorial(number):
    if number in (0,1):   # base case
        return 1
    return number * (number - 1) # recursive case

print(factorial(5))  # Output: 120