n = int(input("Ввод: "))
a = []
num = 0
s = 0
for i in range(n):
    x = []
    for j in range(n):
        x.append(int(input()))
    a.append(x)
for i in a:
    print()
    for j in i:
        print(j, end = '')
for i in range(n):
    for j in range(i + 1, n)
        if a[i][j] > 0:
            num += 1
            s += a[i][j]
print("Сумма:", s)
print("Число:", num)
