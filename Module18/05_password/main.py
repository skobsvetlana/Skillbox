def is_strong(text):
    capital_letter_count = 0
    digit_count = 0

    if len(text) < 8:
        return False

    for symbol in text:
        if symbol.isupper():
            capital_letter_count += 1
        elif symbol.isdigit():
            digit_count += 1

    if capital_letter_count < 1:
        return False

    if digit_count < 3:
        return False

    return True

while True:
    password = input('Придумайте пароль: ')

    if is_strong(password):
        print('Это надёжный пароль!')
        break

    print('Пароль ненадёжный. Попробуйте ещё раз.')
