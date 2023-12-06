print('Задание №1')
n = int(input())
a = input()
b = input()
c = input()
x = 0
if 210 < n < 231:
    for i in range(100, n + 1):
        z = str(i)
        if a in z and  b  in  z and c in z:
            x += 1
print(x)

print('Задание №2')
s = "Привет как дела ?"
a = s.split()
a.reverse()
result = " ".join(a)
print(result)
