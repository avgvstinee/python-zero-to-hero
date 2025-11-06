
# Combination of both positional and keyword arguments

def fullName(firstName, middleName, lastName):
    print(firstName, middleName, lastName)
    
# positional argument always comes first before keyword arguments, otherwise it will raise a syntax error

fullName("Kholofelo", lastName="Shokane", middleName="Augustine")  # Output: Kholofelo Augustine Shokane