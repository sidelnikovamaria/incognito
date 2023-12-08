from random import randint
n = int(input())
m = int(input())
a = []
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,100))
    a.append(b)
f = open('SidelnikovaMariaRomanovna_UB-31_vvod.txt', 'w')
for i in a:
    for j in i:
        f.write(str(j))
        f.write(' ')
    f.write("\n")
f.close()
f = open('SidelnikovaMariaRomanovna_UB-31_vvod.txt', 'r')
a = []
for i in f:
    b = []
    s = i.split(' ')
    for j in s:
        if j == '\n':
            continue
        b.append(int(j))
    a.append(b)
print(a)
f.close()
for i in a:
    minimum = i.index(min(i))
    maximum = i.index(max(i))
    i[maximum], i[0] = i[0], i[maximum]
    i[minimum], i[-1] = i[-1], i[minimum]
f = open('SidelnikovaMariaRomanovna_UB-31_vivod.txt', 'w')
for i in a:
    for j in i:
        f.write(str(j))
        f.write(' ')
    f.write('\n')
f.close()