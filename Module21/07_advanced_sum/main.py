def flat(obj):
    result = []
    for el in obj:
        if isinstance(el, int):
            result.append(el)
        else:
            result.extend(flat(el))
    return result


def my_sum(*args):
    return sum(flat(args))


# print(my_sum([[1, 2, [3]], [1], 3]))
# print(my_sum(1, 2, 3, 4, 5))
