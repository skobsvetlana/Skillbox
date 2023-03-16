class Resident:
    earned_money = 0
    eaten_food = 0
    bought_fur_coats = 0

    def __init__(self, name, home):
        super().__init__()
        self.name = name
        self.home = home
        self.satiety = 30
        self.happiness = 100


    def eat(self):
        food = 0

        if self.home.food > 30:
            food = 30
        elif self.home.food > 0:
            food = self.home.food
        else:
            print('Еды нет!!!!!')

        self.satiety += food
        self.home.food -= food
        self.eaten_food += food



    def pet_the_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def is_ok(self):
        if self.happiness == 0 or self.satiety == 0:
            print('Что-то пощло не так с {}'.format(self.name))
            return False
        else:
            return True
