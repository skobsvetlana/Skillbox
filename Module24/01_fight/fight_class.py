import random

class Warrior:
    def __init__(self):
        self.health = 100


class Fight:
    def __init__(self):
        self.units = (Warrior(), Warrior())


    def get_info(self, ind):
        return self.units[ind].health


    def hit(self):
        attaker = random.randint(0, 1)

        if attaker == 0:
            attaked = 1
        else:
            attaked = 0

        self.units[attaked].health -= 20
        print('Unit{} has attaked unit{}, attacted unit health is {}'.format(
            attaker + 1, attaked + 1, self.get_info(attaked)
        ))


    def fight(self):
        while True:
            if self.units[0].health == 0:
                print('Unit2 won!!!')
                break
            elif self.units[1].health == 0:
                print('Unit1 won!!!')
                break

            self.hit()

