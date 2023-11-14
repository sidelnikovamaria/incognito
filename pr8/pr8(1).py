import random
pol = 0
s = 0
n = int(input("Ввод: "))
a = [[random.randrange(10) for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] <= 0:
            continue
        if a[i][j] > 0:
            pol += 1
            s += a[i][j]
print("Сумма:", s)
print("Число:", pol)
