import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


    def get_info(self):
        return self.suit, self.value


class Deck:
    points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7 ': 7, '8': 8,
              '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}
    suits = ('Diamonds', 'Hearts', 'Clubs', 'Spades')

    def __init__(self):
        cards_suits = [el for sub_list in [[suit] * 13 for suit in self.suits] for el in sub_list]
        cards_values = [el for sub_list in [[value for value in self.points.keys()] * 4] for el in sub_list]
        res = zip(cards_suits, cards_values)

        self.cards = [Card(suit, value) for (suit, value) in res]


    def get_card(self):
        n = len(self.cards) - 1
        random_num = random.randint(0, n)
        card = self.cards.pop(random_num)

        return card


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []


    def show_the_cards(self):
        print(f"\n{self.name}'s cards: ")
        for card in self.cards:
            print(f'{card.get_info()}')










