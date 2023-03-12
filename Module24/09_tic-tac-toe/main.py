from tic_tac_toe_class import Game

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')

tic_tac_toe = Game(player1, player2)


while True:
    tic_tac_toe.make_a_move(player1)
    if tic_tac_toe.is_game_over(player1):
        break

    tic_tac_toe.make_a_move(player2)
    if tic_tac_toe.is_game_over(player2):
        break















