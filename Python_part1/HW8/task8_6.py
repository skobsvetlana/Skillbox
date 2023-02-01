'''Задача 6. Письмо
Что нужно сделать

У нас есть квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги, которое не помещается в конверт. Напишите программу, которая подскажет, сколько раз нужно сложить письмо пополам, чтобы оно поместилось в конверт. Размеры письма вводятся с клавиатуры.

'''

print()
print('Задача 6. Письмо')

envelope_width = 12
letter_width = int(input('Введите размер письма: '))
count = 0
for letter_size in range(letter_width, envelope_width + envelope_width % 2, -letter_width // 2):
    count += 2
print('нужно сложить письмо пополам, чтобы оно поместилось в конверт {} раз'.format(count))

# print()
# count = 0
# while letter_width > envelope_width:
# letter_width /= 2
# count += 2
# print(letter_width, count)


