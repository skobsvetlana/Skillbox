def reversed_word(word):
    res = []
    spam = []

    for sym in word:
        if sym.isalpha():
            spam.append(sym)
        else:
            res.append(''.join(spam[::-1]))
            res.append(sym)
            spam = []
    res.append(''.join(spam[::-1]))

    return ''.join(res)


text = input('Сообщение: ').split()
res = []

for word in text:
    if word.isalpha():
        res.append(word[::-1])
    else:
        res.append(reversed_word(word))

res = ' '.join(res)

print(res)