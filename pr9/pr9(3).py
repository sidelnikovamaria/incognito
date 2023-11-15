n = int(input())
def k(n):
    if 0 < n < 10:
        resulat = 'Простое'
    else:
        for i in range(2, n):
            if n % 1 == 0:
                resulat = 'Сложное'
                break
            else:
                resulat = 'Простое'
        return(resulat)
print(k(n))