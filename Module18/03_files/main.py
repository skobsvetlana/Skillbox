def is_spec_symbols(name):
    spec_symbols = '@№$%^&*()'

    for symbol in spec_symbols:
        if file_name.startswith(symbol):
            return True

    return False


file_extension = ['.txt', '.docx']
file_name = input('Название файла: ')

if is_spec_symbols(file_name):
    print('Ошибка: название начинается на один из специальных символов.')

elif file_name.endswith('.txt') or file_name.endswith('.docx'):
    print('Файл назван верно.')

else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')