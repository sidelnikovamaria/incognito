a = input()
i = 0
while ':' in a:
    a = a.replace(":", "%", 1)
    i += 1
print(a)
print(i)
