def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
res = fibonacci(num_pos)

print(f'Число: {res}')
