# While loop for binary representation

n = 39
remainders = []
while n > 0:
    remainder = n % 2 # Get the remainder when n is divided by 2
    remainders.append(remainder) # we keep track of the remainders
    n = n // 2 # we divide n by 2
remainders.reverse() # The binary representation is the reverse of the remainders
print(remainders) # Output: [1, 0, 0, 11, 1] 
    
    