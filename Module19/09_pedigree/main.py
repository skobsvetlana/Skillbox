n = int(input('Введите количество человек: '))
tree = dict()

for i in range(n - 1):
    print('{}-ая пара: '.format(i + 1), end='')
    pair = input().split()
    if pair[1] in tree:
        tree[pair[0]] = tree[pair[1]] + 1
    else:
        tree[pair[1]] = 0
        tree[pair[0]] = tree[pair[1]] + 1

for key, value in sorted(tree.items()):
    print(key, value)





