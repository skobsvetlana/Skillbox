class Potato:
    states = {0: 'Картофель осажен',
              1: 'Картофель пророс',
              2: 'Молодой картофель',
              3: 'Картофель созрел'
              }

    def __init__(self, index):
        self.index = index
        self.state = 0


    def grow(self):
        if self.state < 3:
            self.state += 1

        self.print_state()


    def print_state(self):
        print('Potato {} сейчас {}'.format(self.index, Potato.states[self.state]))


    def is_ripe(self):
        if self.state == 3:
            return True

        return False


class PotatoGarden:
    def __init__(self, count):
        self.potatos = [Potato(index) for index in range(1, count + 1)]


    def grow_all(self):
        print('Potatos are growing')
        for potato in self.potatos:
            potato.grow()


    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatos]):
            return False
        else:
            return True

    def get_info(self):
        return len(self.potatos)


class Gardener:
    def __init__(self, name, garden=PotatoGarden(0)):
        self.name = name
        self.garden = garden


    def plant(self, count):
        self.garden = PotatoGarden(count)


    def care(self):
        if self.garden:
            print('Садовник позаботился о грядке')
            self.garden.grow_all()
        else:
            print('У Вас еще нет грядки. Картофель сначала нужно посадить.')


    def harvest(self):
        if self.garden:
            if self.garden.are_all_ripe():
                print('Садовник собрал урожай картофеля.')
                self.garden = PotatoGarden(0)
            else:
                print('Картофель еще не созрел. Собирать урожай нельзя.')
        else:
            print('У Вас еще нет грядки. Картофель сначала нужно посадить.')


    def print_info(self):
        num = self.garden.get_info()
        if not num:
            print('{}, Грядки пока нет'.format(self.name))
        else:
            print('{}, Есть грядка из {} картошек'.format(self.name, num))








