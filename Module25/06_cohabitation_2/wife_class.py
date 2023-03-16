from resident_class import Resident

class Wife(Resident):
    def __init__(self, name, home):
        super().__init__(name, home)


    def do_shopping(self):
        self.satiety -= 10
        self.home.money -= 30
        self.home.food += 30


    def buy_fur_coat(self):
        self.satiety -= 10
        self.home.money -= 350
        self.happiness = 60
        self.bought_fur_coats += 1


    def clean_the_house(self):
        self.satiety -= 10
        if self.home.dirt > 100:
            self.home.dirt -= 100
        else:
            self.home.dirt = 0


    def buy_cat_food(self):
        self.satiety -= 10
        self.home.money -= 10
        self.home.cat_food += 10

    def wife_day(self):
        if self.satiety < 20:
            if self.home.food == 0:
                self.do_shopping()
                act = 'Купила продукты'
            else:
                self.eat()
                act = 'Поела'
        elif self.home.food < 40:
            self.do_shopping()
            act = 'Купила продукты'
        elif self.happiness < 20:
            if self.home.money >= 350:
                self.buy_fur_coat()
                act = 'Купила шубу'
            else:
                self.pet_the_cat()
                act = 'Погладила кошку'
        elif self.home.dirt > 50:
            self.clean_the_house()
            act = 'Убралась в доме'
        elif self.home.cat_food <= 10:
            self.buy_cat_food()
            act = 'Купила корм для кошек'
        else:
            self.pet_the_cat()
            act = 'Погладила кошку'

        return act
