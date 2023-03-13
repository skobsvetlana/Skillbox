class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.set_age(age)



    def __str__(self):
        return '\nИмя: {}\nФамилия: {}\nВозраст: {}'.format(self.__name,
                                                         self.__surname,
                                                         self.__age
                                                         )


    def get_age(self):
        return self.__age


    def get_name(self):
        return self.__name


    def get_surname(self):
        return self.__surname


    def set_age(self, age):
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст.')


class Employee(Person):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.set_salary(salary)


    def __str__(self):
        info = super().__str__()
        info = ' '.join(
            (
                info,
                'Зарплата {}'.format(self.calc_salary())
            )
        )
        return info


    def set_salary(self, salary):
        if salary > 0:
            return salary
        else:
            print("Сумма заработной платы должна быть болше 0")


    def calc_salary(self, salary):
        pass


    def change_salary(self, new_salary):
        self.salary = new_salary


class Manager(Employee):
    def __init__(self, name, surname, age, salary=13000):
        super().__init__(name, surname, age, salary)
        self.salary = salary


    def calc_salary(self):
        return self.salary


class Agent(Employee):
    def __init__(self, name, surname, age, sales_volume, salary=5000):
        super().__init__(name, surname, age, salary)
        self.salary = salary
        self.percent = 0.05
        self.set_sales_volume(sales_volume)


    def set_sales_volume(self, sales_volume):
        if sales_volume >= 0:
            self.sales_volume = sales_volume
        else:
            print('Объем продаж не может быть меньше 0')

    def calc_salary(self):
        return self.salary + self.sales_volume * 0.05


    def change_percent(self, new_percent):
        self.percent = new_percent


class Woker(Employee):
    def __init__(self, name, surname, age, hours_worked, salary=100):
        super().__init__(name, surname, age, salary)
        self.salary = salary
        self.set_hours_worked(hours_worked)

    def set_hours_worked(self, hours_worked):
        if hours_worked >= 0:
            self.hours_worked = hours_worked
        else:
            print('Количество отработанных часов не может быть меньше 0')


    def calc_salary(self):
        return self.salary * self.hours_worked


