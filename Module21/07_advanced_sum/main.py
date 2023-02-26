def flat(my_list):
    if not my_list:
        return []

    if isinstance(my_list[0], list):
        return flat(my_list[0]) + flat(my_list[1:])
    else:
        return my_list[:1] + flat(my_list[1:])


def my_sum(*args, res=0):
    for arg in args:
        if isinstance(arg, list):
           my_list = flat(arg)
           res += sum(my_list)
        else:
            res += arg

    return res

#print(my_sum([[1, 2, [3]], [1], 3]))
#print(my_sum(1, 2, 3, 4, 5))

