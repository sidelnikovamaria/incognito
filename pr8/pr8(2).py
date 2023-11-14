from random import random
n = int(input())
m = int(input())
b = [[random.randrage(10) for i in range(m)] for j in range(n)]
for i, row in enumerate(b):
    max = min = 0
    for i, row in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(b)
