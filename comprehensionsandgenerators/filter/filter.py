
test = [2,5,8,0,0,0,1,0]

# Filtering None Values
result = list(filter(None, test))
print(result)  # Output: [2, 5, 8, 1]

result2 = list(filter(lambda x: x , test))
print(result2)  # Output: [2, 5, 8, 1]

result3 = list(filter(lambda x: x > 4 , test))
print(result3)  # Output: [5, 8]

