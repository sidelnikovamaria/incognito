import math
x = float(input())
y = float(input())
z = float(input())
t = float(input())
def square(x, y, z, t):
    p = (x + y + z + t) / 4
    s1 = x * y * 0.5
    s2 = math.sqrt(p * (p - x) * (p - y) * (p - z) * (p - t))
    return s1, s2
print(square(x, y, z, t))