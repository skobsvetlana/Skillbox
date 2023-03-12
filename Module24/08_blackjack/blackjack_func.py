from blackjack_class import Player, Card
def get_results(players, my_deck):
    print('*' * 100)
    max_points = 0
    winner = ''
    for player in players:
        pl_points = get_player_points(player, my_deck)
        print(player.show_the_cards())
        print(pl_points)

        if max_points < pl_points <= 21:
            max_points = pl_points
            winner = player.name

    print("{} won with {} points".format(winner, max_points))



def get_player_points(player, my_deck):
    res = 0
    aces = []

    for card in player.cards:
        if card.value == 'ace':
            aces.append(my_deck.points[card.value])
        else:
            res += my_deck.points[card.value]
    for ace in aces:
        if res + ace > 21:
            res += 1
        else:
            res += ace

    return res


def get_players(players_num, my_deck, players):
    for _ in range(players_num):
        name = input("Input player's name: ")
        players.append(Player(name))

    for _ in range(2):
        for player in players:
            player.cards.append(my_deck.get_card())


def play(players, my_deck):
    for player in players:
        while True:
            player.show_the_cards()
            ans = input('Do you want take one more card? y/n   ').lower()

            if ans == 'y':
                taken_card = my_deck.get_card()
                player.cards.append(taken_card)
                pl_points = get_player_points(player, my_deck)
                if pl_points > 21:
                    print(taken_card.get_info())
                    print('player {} have got {} points'.format(player.name, pl_points))
                    break
            elif ans == 'n':
                break
            else:
                print('input is not correct')
