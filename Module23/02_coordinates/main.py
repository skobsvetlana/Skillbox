import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


# try:
#     file = open('coordinates.txt', 'r')
#     for line in file:
#         nums_list = line.split()
#         res1 = f(int(nums_list[0]), int(nums_list[1]))
#         try:
#             res2 = f2(int(nums_list[0]), int(nums_list[1]))
#             try:
#                 number = random.randint(0, 100)
#                 file_2 = open('result.txt', 'w')
#                 my_list = sorted([res1, res2, number])
#                 file_2.write(' '.join(my_list))
#             except Exception:
#                 print("Что-то пошло не так")
#         except Exception:
#             print("Что-то пошло не так со второй функцией")
#         finally:
#             file.close()
#             file_2.close()
# except Exception:
#     print("Что-то пошло не так с первой функцией")


number = random.randint(0, 100)

try:
    with open('coordinates.txt', 'r') as file_r:
        for line in file_r.read().split('\n'):
            x, y = tuple(line.split())

            try:
                res1 = f(int(x), int(y))
            except ZeroDivisionError:
                print('Ошибка: деление на ноль в f')

            try:
                res2 = f2(int(x), int(y))
            except ZeroDivisionError:
                print('Ошибка: деление на ноль в f2')

            try:
                my_list = sorted([res1, res2, number])
                my_list = [str(el) for el in my_list]

                with open('result.txt', 'a') as file_w:
                    file_w.write(' '.join(my_list) + '\n')
            except TypeError:
                print('Ошибка: тип данных для записи в файл не строка')
            except NameError as n_error:
                arg = n_error.args[0].split()[1]
                print(f'Ошибка: имя переменной {arg} не определено')
except FileNotFoundError as n_err:
    print(f'Ошибка: файла не существует')
finally:
    print('Программа закончила работу')


