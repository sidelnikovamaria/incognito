m = int(input(''))
k = int(input(''))
symm = 0
i = 1
a = 0
b = 1
for i in range(m + 1):
    c = a + b
    a, b = b, c
    if (i >= k) and (i <= (m+1)):
        symm += c
    i += 1
print(symm)
