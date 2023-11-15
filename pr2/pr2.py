print('')
x=int(input('Введите координаты х'))
y=int(input('Введите координаты у'))
if (y > 0 and x > 0) and (x > 0 and y < 5) and (x < 5 and y > 0) and (x < 5 and y < 5):
    print(x, y)