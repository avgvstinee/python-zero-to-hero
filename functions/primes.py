
# Primes 

from math import ceil, sqrt

def get_prime(n):
    '''calculate a list of primes up to n (included)'''
    
    primelist = []
    for candidate in range(2, n+1):
        is_prime = True
        root = ceil(sqrt(candidate)) # division limit
        for prime in primelist: # we try only the primes
            if prime > root: # no need to check further
                break
            if candidate % prime == 0: # found a divisor
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
    return primelist

print(get_prime(30))  # prints [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]