def is_symetrical(my_list, n, shift):
    n += shift
    central_ind = n // 2

    if n % 2 == 0:
        ind1 = central_ind - 1
        ind2 = central_ind
    else:
        ind1 = central_ind - 1
        ind2 = central_ind + 1

    for _ in range(central_ind - shift):
        if my_list[ind1] != my_list[ind2]:
            return False
        else:
            ind1 -= 1
            ind2 += 1

    return True


def fill_my_list(n):
    for _ in range(n):
        num = int(input('Число: '))
        my_list.append(num)


my_list = []
n = int(input('Кол-во чисел: '))
fill_my_list(n)

shift = 0

for _ in range(n - 1):
    ans = is_symetrical(my_list, n, shift)

    if ans == True:
        break

    shift += 1

if shift == 0:
    print('Это симметричная последовательность')
else:
    res = my_list[0:shift]
    res.reverse()

    print(f'Нужно приписать чисел: {shift}')
    print(f'Сами числа: {res}')




