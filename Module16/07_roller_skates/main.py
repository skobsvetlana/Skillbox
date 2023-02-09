skates = []
n = int(input('Кол-во коньков: '))

for i in range(n):
    print(f'Размер {i + 1}-й пары: ')
    number = int(input())
    skates.append(number)

people = []
k = int(input('Кол-во людей: '))

for i in range(k):
    print(f'Размер ноги {i + 1}-го человека: ')
    number = int(input())
    people.append(number)

count = 0
skates.sort()


for el in people:
    if el in skates:
        count += 1
        skates.remove(el)
        n -= 1
    elif el <= skates[n - 1]:
        count += 1
        skates.remove(skates[n - 1])
        n -= 1

print(f'Наибольшее кол-во людей, которые могут взять ролики: {count}')

