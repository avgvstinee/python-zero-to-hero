
students = [
    dict(id=0, credit = dict(math = 9, physics = 6, history = 7)),
    dict(id=1, credit = dict(math = 6, physics = 7, latin = 10)),
    dict(id=2, credit = dict(history = 8, physics = 9, chemistry = 10)),  
    dict(id=3, credit = dict(math = 5, physics = 5, geography = 7)),
]

def decorate(student):
   # create a 2-tuple  (sum of credits, student) from student dict.
    return (sum(student['credit'].values()), student) 

def undecorate(decorated_student):
    # discard sum of credits, return original student dict
    return decorated_student[1]


# decorate
students = sorted(map(decorate, students), reverse=True)
# undecorate
students = list(map(undecorate, students))

print(students)