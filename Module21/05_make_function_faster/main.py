# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result


def factorial(n):
    if n < len(factorial_list):
        return factorial_list[n]

    if n == 0:
        return 1

    res = n * factorial(n - 1)
    factorial_list.append(res)
    return res


def calculating_math_func(data):
    result = factorial(data)
    result /= data ** 3
    result = result ** 10
    return result

factorial_list = [1]

