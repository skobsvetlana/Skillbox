data = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Петров', 'Илья'): 15,
    ('Петрова', 'Анна'): 7,
    ('Петрова', 'Дарья'): 65,
    ('Синицына', 'Анна'): 7,
    ('Синицын', 'Артем'): 36,
}

surname = input('Введите фамилию: ').lower()

for key, value in data.items():
    data_surname, data_name = key
    if data_surname.lower().startswith(surname) or surname.startswith(data_surname.lower()):
        print(data_surname, data_name, value)
