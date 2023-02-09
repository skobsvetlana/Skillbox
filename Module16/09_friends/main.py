balance = []
friends = int(input('Кол-во друзей: '))

for _ in range(friends):
    balance.append(0)

debts = int(input('Долговых расписок: '))

for i in range(debts):
    print(f'\n{i + 1}-я расписка')

    lender = int(input('Кому: '))
    debtor = int(input('От кого: '))
    amount = int(input('Сколько: '))

    balance[lender - 1] -= amount
    balance[debtor - 1] += amount

print('\nБаланс друзей:')

for i in range(friends):
    print(f'{i + 1}: {balance[i]}')
