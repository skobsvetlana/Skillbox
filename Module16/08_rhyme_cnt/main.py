n = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {k}-й человек')

people = [x for x in range(1, n + 1)]
start_ind = 0
multiplier = 1

while n > 1:
    if k > n:
        remove_ind = start_ind + k % n - 1
    else:
        remove_ind = start_ind + k - 1

    print(f'\nТекущий круг людей: {people}')
    print(f'Начало счёта с номера {people[start_ind]}')
    print(f'Выбывает человек под номером {people[remove_ind]}')
    people.remove(people[remove_ind])
    n -= 1
    start_ind = remove_ind

    if start_ind == n:
        start_ind = 0

print(f'\nОстался человек под номером {people[0]}')


