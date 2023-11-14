a = [1, 2, 3, 4, 0, 6, 0]
mean = sum(a) / len(a)
a = [it if it else mean for it in a]
print(a)
