def is_prime(n):
    if n < 2:
        return False
    elif n % 2 == 0:
        return n == 2
    d = 3

    while d * d <= n and n % d != 0:
        d += 2

    return d * d > n


def crypto(obj):
    return [el for ind, el in enumerate(obj) if is_prime(ind)]


# print(crypto('О Дивный Новый мир!'))
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
