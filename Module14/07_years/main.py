# Задача 7. Годы

def same_digits_is_three(number):
    zeros = 0
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    sevens = 0
    eights = 0
    nines = 0

    for digit in str(number):
        if digit == '0':
            zeros += 1
            if zeros == 3:
                return True
        elif digit == '1':
            ones += 1
            if ones == 3:
                return True
        elif digit == '2':
            twos += 1
            if twos == 3:
                return True
        elif digit == '3':
            threes += 1
            if threes == 3:
                return True
        elif digit == '4':
            fours += 1
            if fours == 3:
                return True
        elif digit == '5':
            fives += 1
            if fives == 3:
                return True
        elif digit == '6':
            sixes += 1
            if sixes == 3:
                return True
        elif digit == '7':
            sevens += 1
            if sevens == 3:
                return True
        elif digit == '8':
            eights += 1
            if eights == 3:
                return True
        elif digit == '9':
            nines += 1
            if nines == 3:
                return True

    return False

year1 = int(input('Введите первый год: '))
year2 = int(input('Введите второй год: '))

for year in range(year1, year2 + 1):
    if same_digits_is_three(year):
        print(year)