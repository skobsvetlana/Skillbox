def get_input_parameters(number):
    return int(number)


def display_result(odd_numbers):
    print(odd_numbers)


def get_odd_numbers(number):
    result = []

    for i in range(number):
        if i % 2 == 0:
            result.append(i)

    return result


if __name__ == '__main__':
    number = get_input_parameters()  # получаем параметры
    odd_numbers = get_odd_numbers(number)  # получаем нечётные числа
    display_result(odd_numbers)  # выводим результат
