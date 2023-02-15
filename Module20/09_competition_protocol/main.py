def get_best_results(data):
    res = []

    for name, info in data.items():
        ind, score = sorted(info, key=lambda x: x[1])[-1]
        res.append((name, ind, score))

    res = sorted(res, key=lambda x: (x[2], -x[1]))[-3:]

    return reversed(res)


protocol = dict()
n = int(input('Сколько записей вносится в протокол? '))

for i in range(1, n + 1):
    print(f'{i}-я запись: ')
    score, name = tuple(input().split())

    if name in protocol:
        protocol[name].append((i, int(score)))
    else:
        protocol[name] = [(i, int(score))]

# protocol = {
#     'Jack': [(1, 69485), (6, 95715)],
#     'qwerty': [(2, 95715), (5, 197128)],
#     'Alex': [(3, 95715), (7, 93289), (8, 95715)],
#     'M': [(4, 83647), (9, 95715)]
# }

res = get_best_results(protocol)

for i, el in enumerate(res):
    name, ind, score = el
    print('{}-е место. {} ({})'.format(i + 1, name, score))
