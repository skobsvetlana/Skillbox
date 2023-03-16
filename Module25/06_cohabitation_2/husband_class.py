from resident_class import Resident

class Husband(Resident):
    def __init__(self, name, home):
        super().__init__(name, home)


    def play(self):
        self.happiness += 20
        self.satiety -= 10


    def work(self):
        self.home.money += 150
        self.satiety -= 10
        self.earned_money += 150


    def husband_day(self):
        if self.satiety < 20:
            if self.home.food == 0:
                self.work()
                act = 'Поработал'
            else:
                self.eat()
                act = 'Поел'
        elif self.satiety == 40:
            self.pet_the_cat()
            act = 'Погладил кошку'
        elif self.happiness < 20:
            self.play()
            act = 'Поиграл на компьютере'
        else:
            self.work()
            act = 'Поработал'

        return act
