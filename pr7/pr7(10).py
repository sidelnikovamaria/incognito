n = int(input())
a = input()
b = input()
c = input()
x = 0
for i in range(100, n + 1):
    z = str(i)
    if a in z and  b  in  z and c in z:
        x += 1
print(x)
