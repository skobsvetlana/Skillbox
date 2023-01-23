#Задача 5. Наименьший делитель
def smallest_common_divisor(number):
    result = 1

    for i in range(2, number + 1):
        if number % i == 0:
            result = i
            break

    return result

number = int(input('Введите число: '))
result = smallest_common_divisor(number)

print('Наименьший делитель, отличный от единицы: {}'.format(result))