print('Задание №1')
x = int(input())
y = 1
z = 0
a = [int(input()) for i in range(x)]
for b in a:
    y *= b
    z += b
print(y, z)
print('Задание №2')
l = int(input())
a = [int(input()) for i in range(l)]
s = 0
for j in a:
    s += j
    m = s/l
for k in range(len(a)):
    if a[k] == 0:
        a[k] = m
print(a)
