# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 12, 6, 7, 8, 15]
k = 11

diff = abs(k - list_1[0])
num = list_1[0]

for item in list_1:
    if abs(k - item ) < diff:
        diff = abs(k - item)
        num = item
print(num)