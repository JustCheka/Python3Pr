list_1 = [1, 2, 3, 4, 5, 3, 6, 69, 3]
k = 3

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)