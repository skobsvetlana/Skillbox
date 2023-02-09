def is_correct(sym):
    pass


ip = input('Введите IP: ').split('.')

for el in ip:
    if el.isdigit():
       if int(el) > 255:
           print('{} превышает 255.'.format(el))
           break
    else:
        print(el)

else:
    print('IP-адрес корректен.')

