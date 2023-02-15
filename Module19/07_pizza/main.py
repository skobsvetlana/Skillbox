n = int(input('Введите количество заказов: '))
orders = dict()

for i in range(n):
    print('{}-ый заказ: '.format(i + 1), end='')
    order = input('').split()
    order[2] = int(order[2])

    if order[0] in orders:
        if order[1] in orders[order[0]]:
            orders[order[0]][order[1]] += order[2]
        else:
            orders[order[0]][order[1]] = order[2]
    else:
        orders[order[0]] = {order[1] : order[2]}


names = sorted(orders.keys())
for name in names:
    print('{}:'.format(name))
    for pizza, num in orders[name].items():
        print('\t{}:{}'.format(pizza, num))