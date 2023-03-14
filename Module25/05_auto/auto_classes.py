import math

class Auto:
    def __init__(self, coordinates: object = (0, 0), angle: object = 45) -> object:
        self.set_coordinates(coordinates)
        self.set_angle(angle)


    def __str__(self):
        return 'Автомобиль сейчас находится в точке с координатами {}, направление движения - {} градусов'.format(
            self.__coordinates,
            self.__angle
        )


    def move(self, distance):
        x, y = self.__coordinates
        x += round(distance * math.cos(math.radians(self.__angle)), 0)
        y += round(distance * math.sin(math.radians(self.__angle)), 0)
        self.__coordinates = (x, y)


    # def change_direction(self, new_angle):
    #     self.__angle = new_angle


    def turn_right(self, angle):
        self.__angle -= angle


    def turn_left(self, angle):
        self.__angle += angle

    def set_coordinates(self, coordinates):
        if isinstance(coordinates, tuple):
            if len(coordinates) == 2:
                self.__coordinates = coordinates
            else:
                print("Необходимоввести две координаты через запятую (x, y): ")
        else:
            print('Координаты необходимо ввести в круглых скобках через запятую (x, y')


    def set_angle(self, angle):
        if 0 < angle < 360:
            self.__angle = angle
        else:
            print('Угол должен быть числом от 0 до 360')


    def get_coordinates(self):
        return self.__coordinates


    def get_angle(self):
        return self.__angle


class Bus(Auto):
    total_money = 0
    def __init__(self):
        super().__init__()
        self.passenger_count = 0
        self.money = 0
        self.ticket_price = 25


    def __str__(self):
        return 'Автобус сейчас находится в точке с координатами {}, направление движения - {} градусов.' \
               '\nСейчас в автобусе {} пассажиров. Водитель заработал за поездку {} рублей. ' \
               'Заработал всего - {}'.format(
            self.get_coordinates(),
            self.get_angle(),
            self.passenger_count,
            self.money,
            self.total_money
        )


    def get_in(self, num):
        if num > 0:
            self.passenger_count += num
        else:
            print('Количество пассажиров должно быть больше 0')


    def get_out(self, num):
        if 0 < num  < self.passenger_count:
            self.passenger_count -= num
        else:
            print('Количество пассажиров должно быть больше 0 и меньше {}'.format(self.passenger_count))


    def set_ticket_price(self, new_ticket_price):
        self.ticket_price = new_ticket_price


    def move(self, distance):
        super().move(distance)
        self.money = distance * self.passenger_count * self.ticket_price
        self.total_money += self.money





