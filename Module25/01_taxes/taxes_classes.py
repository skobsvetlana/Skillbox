class Property:
    def __init__(self, worth):
        self.worth = worth


    def calc_the_tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)


    def calc_the_tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)


    def calc_the_tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)


    def calc_the_tax(self):
        return self.worth / 500



class Person:
    def __init__(self, name, money):
        self.name = name
        self.set_money(money)
        self.property = []


    def __str__(self):
        property = [(type(el).__name__, el.worth) for el in self.property]
        info = '\n{}, денег - {}\nСобственность - {}'.format(self.name, self.get_money(), property)

        return info
        
        
    def print_taxes(self):
        taxes = self.calc_taxes()
        diff = self.__money - taxes
        
        if diff >= 0:
            res = 'Денег для оплаты налогов достаточно.'
        else:
            res = f'Денег для оплаты налогов не достаточно. Не хватает {abs(diff)} рублей.'
        
        
        print('Общая сумма налогов, которую нужно заплатить {name} составляет {tax} рублей. {info}'.format(
            name=self.name,
            tax=taxes,
            info=res
        ))


    def set_money(self, money):
        if money > 0:
            self.__money = money
        else:
            raise Exception('Денег не может быть меньше 0.')


    def get_money(self):
        return self.__money


    def add_property(self, property):
        if isinstance(property, Property):
            self.property.append(property)
        else:
            print('{} не добавлен. Так как не является экземпляром класса property.'.format(property))

        
        
    def calc_taxes(self):
        taxes = 0

        for el in self.property:
            taxes += el.calc_the_tax()

        return taxes







    
    
        



