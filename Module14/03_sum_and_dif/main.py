def calculate_sum_of_didgits(number):
    result = 0
    while number > 0:
        result += number % 10
        number //= 10

    return result


def  calculate_number_of_digits(number):
    counter = 0
    while number > 0:
        number //= 10
        counter += 1

    return counter

number = int(input('Введите целое положительное число: '))

sum_of_didgits = calculate_sum_of_didgits(number)
number_of_digits = calculate_number_of_digits(number)

print('Сумма чисел: {}'.format(sum_of_didgits))
print('Количество цифр в числе: {}'.format(number_of_digits))
print('Разность суммы и количества цифр: {}'.format(sum_of_didgits - number_of_digits))