'''Задача 2. Финансовый отчёт
Что нужно сделать

Васе пришло очередное задание — автоматизация финансовой отчётности. Звучит сложно, а на деле нужно просто написать код, который будет считать нужные для отчёта вычисления автоматически. Вычисления, которые нужно реализовать в программе: сумму дохода первых двух кварталов поделить на сумму последних двух кварталов, чтобы понять динамику роста или падения дохода.

Алгоритм действий в программе:

Запросить у пользователя четыре числа.
Отдельно сложить два первых и два вторых.
Разделить первую сумму на вторую.
Вывести результат на экран.
'''
print('Задача 2. Финансовый отчёт')

income_1 = int(input('Введите сумму дохода за 1 квартал '))
income_2 = int(input('Введите сумму дохода за 2 квартал '))
income_3 = int(input('Введите сумму дохода за 3 квартал '))
income_4 = int(input('Введите сумму дохода за 4 квартал '))

print('динамика роста/падения дохода', (income_1 + income_2) / (income_3 + income_4))
print()