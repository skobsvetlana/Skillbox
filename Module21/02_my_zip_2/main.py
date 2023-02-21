def my_zip(res, *arg):
    if [] not in arg:
        arg = [list(x) for x in arg]
        res.append(tuple([x.pop(0) for x in arg]))
        my_zip(res, *arg)


res = []
my_zip(res, {'a': 1, 'b': 2, 'c': 3}, [1, 2, 3, 4, 5], (3, 4, 5), "asdf")

#print(res)
