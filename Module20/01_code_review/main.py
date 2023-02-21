def get_info(data):
    interests = set()
    total_surname_len = 0

    for info in data.values():
        interests.update(info['interests'])
        total_surname_len += len(info['surname'])

    return interests, total_surname_len


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


pairs = [(i_student, students[i_student]['age']) for i_student in students]
interests, total_surname_len = get_info(students)


print('Список пар "ID студента — возраст": {}'.format(pairs))
print('\nПолный список интересов всех студентов: {}'.format(interests))
print('\nОбщая длина всех фамилий студентов: {}'.format(total_surname_len))
