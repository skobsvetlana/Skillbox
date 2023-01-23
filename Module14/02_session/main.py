#Задача 2. Сессия
def calculate_line_equation(x1, y1, x2, y2):
    if x1 == x2:
        return 'x = ' + str(x1)

    if y1 == y2:
        return 'y = ' + str(y1)

    x_diff = x1 - x2
    y_diff = y1 - y2

    if x_diff == 0 and y_diff == 0:
        return "Ошибка ввода. Координаты первой и второй точки совпадают."

    k = y_diff / x_diff
    b = y2 - k * x2

    if b < 0:
        result = "y = " + str(k) + " * x - " + str(abs(b))
    else:
        result = "y = " + str(k) + " * x + " + str(b)

    return result


print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

result = calculate_line_equation(x1, y1, x2, y2)

print("\nУравнение прямой, проходящей через эти точки:")
print(result)

