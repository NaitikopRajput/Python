lst = [1, 2, 3, 2, 4, 3, 5, 6, 5]

unique_lst = []

for num in lst:
    if num not in unique_lst:
        unique_lst.append(num)

print(unique_lst)
