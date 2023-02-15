def symbol_count(text):
    res = dict()
    for sym in text:
        if sym in res:
            res[sym] += 1
        else:
            res[sym] = 1

    return res


text = input('Введите строку: ')

if len(text) <= 1:
    print('Нельзя сделать палиндромом')
else:
    res = symbol_count(text)
    odd_count = 0

    for value in res.values():
        if value % 2 != 0:
            odd_count += 1

        if odd_count > 1:
            print('Нельзя сделать палиндромом')
            break
    else:
        print('Можно сделать палиндромом')



