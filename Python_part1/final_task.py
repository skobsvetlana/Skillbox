# MyProfile app

SEPARATOR = '------------------------------------------'


def checking_number_of_symbols(text):
    count = 0
    for _ in str(text):
        count += 1

    return count


def check_phone_number(phone_number):
    result = ''
    for symbol in phone_number:
        if symbol == '+' or ('0' <= symbol <= '9'):
            result += symbol

    return result


def check_zip_code(zip_code):
    result = ''
    for symbol in zip_code:
        if '0' <= symbol <= '9':
            result += symbol

    return result


def options_choice(text):
    while True:
        print(text)

        option = int(input('Введите номер пункта меню: '))
        if option == 0:
            break
        elif option == 2 or option == 1:
            return option
        else:
            print('\nВведите корректный пункт меню\n')
    return option


def print_general_info(name, age, phone_number, email, zip_code, address, additional_info):
    print(SEPARATOR)
    print('Имя:    ', name)
    if 11 <= age % 100 <= 19:
        years_parameter = 'лет'
    elif age % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age, years_parameter)
    print('Телефон:', phone_number)
    print('E-mail: ', email)
    print('Индекс: ', zip_code)
    print('Адрес: ', address)
    if additional_info:
        print('')
        print('Дополнительная информация:')
        print(additional_info)
    # print social links
    # print('')
    # print('Социальные сети и мессенджеры')
    # print('Вконтакте:', v)
    # print('Telegram: ', t)
    # print('Tiktok:   ', tk)


def print_business_info(ogrnip, inn, checking_account, bank_name, bic, correspondent_account):
    print('\nИнформация о предпринимателе')
    print('ОГРНИП:    ', ogrnip)
    print('ИНН:', inn)
    print('Банковские реквизиты')
    print('Р/c:', checking_account)
    print('Банк: ', bank_name)
    print('БИК: ', bic)
    print('К/с: ', correspondent_account)


def input_general_info():
    # input general info
    name = input('Введите имя: ')

    while 1:
        # validate user age
        age = int(input('Введите возраст: '))
        if age > 0:
            break
        print('Возраст должен быть положительным')

    phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
    phone_number = check_phone_number(phone_number)

    email = input('Введите адрес электронной почты: ')
    zip_code = input('Введите почтовый индекс: ')
    zip_code = check_zip_code(zip_code)
    address = input('Введите почтовый адрес (без индекса): ')
    additional_info = input('Введите дополнительную информацию:\n')

    return name, age, phone_number, email, zip_code, address, additional_info


def input_business_info():
    while True:
        ogrnip = int(input('Введите ОГРНИП:  '))
        lenth = checking_number_of_symbols(ogrnip)
        if lenth == 15:
            break
        print('ОГРНИП должен содержать 15 цифр')

    inn = int(input('Введите ИНН:  '))

    while True:
        checking_account = input('Введите расчетный счет:  ')
        lenth = checking_number_of_symbols(checking_account)
        if lenth == 20:
            break
        print('Расчетный счет должен содержать 20 цифр')

    bank_name = input('Введите название банка:  ')
    bic = int(input('Введите БИК:  '))
    correspondent_account = int(input('Введите корреспондентский счет:  '))

    return ogrnip, inn, checking_account, bank_name, bic, correspondent_account


def submenu_edit_info():
    submenu_edit = SEPARATOR + '\nВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ\n1 - Общая информация\n2 - Информация о предпринимателе\n0 - Назад'
    option = options_choice(submenu_edit)

    return option


def submenu_print_info():
    submenu_print = SEPARATOR + '\nВЫВЕСТИ ИНФОРМАЦИЮ\n1 - Общая информация\n2 - Вся информация\n0 - Назад'
    option = options_choice(submenu_print)

    return option


def main_menu():
    main_menu = SEPARATOR + '\nГЛАВНОЕ МЕНЮ\n1 - Ввести или обновить информацию\n2 - Вывести информацию\n0 - Завершить работу'
    option = options_choice(main_menu)

    return option


# user profile
name = ''
age = 0
phone_number = ''
email = ''
zip_code = ''
address = ''
additional_inf = ''

# social links
# v = ''
# t = ''
# tk = ''

# business profile
ogrnip = ''
inn = ''
checking_account = ''
bank_name = ''
bic = ''
correspondent_account = ''

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    option = main_menu()

    if option == 0:
        break

    elif option == 1:
        while True:
            submenu_edit_option = submenu_edit_info()

            if submenu_edit_option == 0:
                break

            elif submenu_edit_option == 1:
                name, age, phone_num, email, zip_code, address, additional_inf = input_general_info()

            else:
                ogrnip, inn, checking_account, bank_name, bic, correspondent_account = input_business_info()

    else:
        while True:
            submenu_print_option = submenu_print_info()
            print('submenu_print_option =', submenu_print_option)
            if submenu_print_option == 0:
                break

            elif submenu_print_option == 1:
                print_general_info(name, age, phone_num, email, zip_code, address, additional_inf)

            else:
                print_general_info(name, age, phone_num, email, zip_code, address, additional_inf)
                print()
                print_business_info(ogrnip, inn, checking_account, bank_name, bic, correspondent_account)







