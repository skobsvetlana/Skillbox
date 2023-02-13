n = int(input('Введите количество человек: '))
tree = dict()

for i in range(n - 1):
    print('{}-ая пара: '.format(i + 1), end='')
    pair = input().split()

print(tree)
