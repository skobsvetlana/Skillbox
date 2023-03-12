import random

class Student:
    def __init__(self, name, group_num, academic_performance):
        self.name = name
        self.group_num = group_num
        self.academic_performance = academic_performance


    def print_info(self):
        #print(self.name, self.group_num, self.academic_performance)
        print('{}, номер группы: {}, оценки: {}'.format(self.name,
                                                                 self.group_num,
                                                                 self.academic_performance
                                                                 ))


    def get_avr_score(self):
        return sum(self.academic_performance) / len(self.academic_performance)


class Students:
    def __init__(self, count):
        self.students = [Student(f'Name{i} Surname{i}',
                            random.randint(1, 10),
                            [random.randint(1, 5),
                             random.randint(1, 5),
                             random.randint(1, 5),
                             random.randint(1, 5),
                             random.randint(1, 5)]) for i in range(1, count + 1)]


    def get_info(self):
        for student in self.students:
            student.print_info()
        print()


    def students_sort(self):
        students_sorted = sorted(self.students, key=lambda x: x.get_avr_score())
        for student in students_sorted:
            student.print_info()
        print()