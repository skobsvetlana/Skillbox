'''Задача 6. Маятник
Что нужно сделать

Известно, что амплитуда качающегося маятника с каждым разом затухает на 8,4% от амплитуды прошлого колебания. Если качнуть маятник, то, строго говоря, он не остановится никогда, просто амплитуда будет постоянно уменьшаться до тех пор, пока мы не сочтём такой маятник остановившимся. Напишите программу, определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

Программа получает на вход начальную амплитуду колебания в сантиметрах и конечную амплитуду его колебаний, которая считается остановкой маятника. Обеспечьте контроль ввода.

Пример:

Введите начальную амплитуду: 1

Введите амплитуду остановки: 0.1

Маятник считается остановившимся через 27 колебаний'''

print('Задача 6. Маятник \n')


def swing_num(start_amplitude, stop_amplitude):
    count = 0
    amplitude = start_amplitude
    while amplitude > stop_amplitude:
        amplitude -= amplitude * 0.084
        count += 1

    return count


start_amplitude = float(input('Введите начальную амплитуду: '))
stop_amplitude = float(input('Введите амплитуду остановки: '))

res = swing_num(start_amplitude, stop_amplitude)

print(f'\nМаятник считается остановившимся через {res} колебаний')




























