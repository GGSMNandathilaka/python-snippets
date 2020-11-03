num_arr = [5, 2, 1, 5, 7, 4, 2, 2]
uniques = []
for item in num_arr:
    if item not in uniques:
        uniques.append(item)
print(uniques)