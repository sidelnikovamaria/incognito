print('Задание №1')
x=[int(input()) for i in range(10)]
for j in range(len(x)):
    if x[j]<0 and x[j+1] < 0:
        print(x[j], x[j+1])
print('Задание №2')
x=[int(input()) for i in range(10)]
y=0
for j in range(len(x)):
    if x[j]>5:
        y += x[j]
print(y)
