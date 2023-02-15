my_str = 'abcd'
tpl = (10, 20, 30, 40)

n = min(len(my_str), len(tpl))
res = ((my_str[i], tpl[i]) for i in range(n))

print(res)

for el in res:
    print(el)

