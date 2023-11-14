n = int(input())
a = input()
b = input()
c = input()
x = 0
for i in range(100, n + 1):
    digit = str(i)
    if a in digit and  b  in  digit and c in digit:
        x += 1
print(x)
