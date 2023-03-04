import os

def add_to_file(file, data):
    with open(file, 'a', encoding='utf-8') as file:
        file.write(' '.join(data))
        file.write('\n')


file_name = 'registrations.txt'
path = os.path.abspath(os.path.join(file_name))

with open(path, 'r', encoding='utf-8') as file:
    for line in file.read().split('\n'):
        try:
            data = line.split()

            if not data[0].isalpha():
                add_to_file('registrations_bad.log', data)
                raise NameError
            elif '@' not in data[1] or '.' not in data[1]:
                add_to_file('registrations_bad.log', data)
                raise SyntaxError
            elif int(data[2]) < 10 or int(data[2]) > 100:
                add_to_file('registrations_bad.log', data)
                raise ValueError
            else:
                add_to_file('registrations_good.log', data)
        except IndexError:
            print('НЕ присутствуют все три поля: IndexError')
        except NameError:
            print('Поле имени содержит НЕ только буквы: NameError')
        except SyntaxError:
            print('Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError')
        except ValueError:
            print('Поле «Возраст» НЕ является числом от 10 до 99: ValueError')