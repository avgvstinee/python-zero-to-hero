
remainder = value % modulus

# Traditional way

if remainder :
    print(f" Not divisible! the remainder is {remainder}.")
    
# Using the walrus operator

if remainder := value % modulus:
    print(f" Not divisible! the remainder is {remainder}.")