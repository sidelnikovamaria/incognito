text = 'в этом тексте есть слово сколько раз это слово повторяется'.split('')
c = 0
word = 'слово'
for i in text:
    if i == word:
        c += 1
print(c)
