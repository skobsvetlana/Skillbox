def my_zip(*arg):
    n = min([len(obj) for obj in arg])
    res = ((obj[i] for obj in arg) for i in range(n))

    return res


# res = my_zip([1, 2, 3, 4, 5], (3, 4, 5), "asdf")
#
# for el in res:
#     print(list(el))

