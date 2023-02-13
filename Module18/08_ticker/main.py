str1 = input('Первая строка: ')
str2 = input('Вторая строка: ')
count = 0

if str1 == str2:
    print('Строки равны')
else:
    for i in range(len(str1)):
        str2 = str2[-1] + str2[:-1]
        count += 1
        if str1 == str2:
            print(f'\nПервая строка получается из второй со сдвигом {count}.')
            break
    else:
        print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')

