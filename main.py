num_arr = [12, 15, 2, 1, 7, 8, 23, 45, -1, -5]

largest_num = num_arr[0]
for item in num_arr:
    if item > largest_num:
        largest_num = item
print(f"Max: {largest_num}")
