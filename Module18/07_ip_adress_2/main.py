def symbol_checkout(sym):
    for el in sym:
        if el.isalpha():
            return 1
    else:
        return 2


ip = input('Введите IP: ').split('.')

for el in ip:
    if el.isdigit():
        if int(el) > 255:
            print(f'{el} превышает 255.')
            break
    else:
        res = symbol_checkout(el)

        if res == 1:
            print(f'{el} — это не целое число.')
            break
        elif res == 2:
            print('Адрес — это четыре числа, разделённые точками.')
            break
else:
    print('IP-адрес корректен.')


