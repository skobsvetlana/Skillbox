from blackjack_func import get_results, get_players, play
from blackjack_class import Deck, Player


my_deck = Deck()
while True:
    try:
        players_num = int(input('Input number of players: '))
    except ValueError:
        print('Error: You have to enter integer')
    else:
        break

players = [Player('dealer')]

get_players(players_num, my_deck, players)

play(players[1:], my_deck)

get_results(players, my_deck)



