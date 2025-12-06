

grades = [18,23,30,27]
averages = [22,21,29,24]

# zip(list1, list2) ➜ [(list1[0], list2[0]), (list1[1], list2[1]), ...]

results = list(zip(grades,averages ))
print(results)  # Output: [(18, 22), (23, 21), (30, 29), (27, 24)]


# Equivalent using map and lambda

results_map = list(map(lambda *a: a, grades, averages))
print(results_map)  # Output: [(18, 22), (23, 21), (30, 29), (27, 24)]      