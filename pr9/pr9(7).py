def f(a, b):
    if a < b:
        return f(b, a+1)
    if b < a:
        print(a)
        return f(a-1, b)
    if a == b:
        return b
a = int(input())
b = int(input())
print(f(a, b))