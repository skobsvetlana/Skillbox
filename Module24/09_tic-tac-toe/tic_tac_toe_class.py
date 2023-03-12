class Cell:
    def __init__(self, value, index):
        self.value = value
        self.index = index


    def get_cell_value_for_print(self):
        if self.value:
            return self.value
        else:
            return self.index


class Board:
    def __init__(self):
        self.board = [Cell(False, i) for i in range(1, 10)]


    def show_bord(self):
        for i, cell in enumerate(self.board):
            print(cell.get_cell_value_for_print(), end=' ')
            if (i + 1) % 3 == 0:
                print()
        print()


    def is_cell_empty(self, num):
        if not self.find_the_cell(num).value:
            return True
        else:
            return False


    def is_board_full(self):
        if all([cell.value for cell in self.board]):
            return True
        else:
            return False


    def find_the_cell(self, num):
        for cell in self.board:
            if cell.index == num:

                return cell


    def change_the_cell(self, num, symbol):
        cell = self.find_the_cell(num)
        cell.value = symbol


class Player:
    def __init__(self, name):
        self.name = name
        self.cell = set()


class Game:
    win_combinations = [{1, 2, 3,}, {4, 5, 6,}, {7, 8, 9,},
                        {1, 4, 7,}, {2, 5 ,8}, {3, 6, 9},
                        {1, 5, 9}, {3, 5, 7}]
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.board.show_bord()


    def is_won(self, player_name):
        if player_name == self.player1.name:
            player = self.player1
        else:
            player = self.player2

        for el in self.win_combinations:
            if el.issubset(player.cell):
                print('Игрок {} выиграл.'.format(player.name))
                return True

        return False


    def is_game_over(self, player_name):
        if self.is_won(player_name):
            return True
        elif self.board.is_board_full():
            print("Игра окончена. Ничья.")
            return True
        else:
            return False


    def get_symbol(self, player_name):
        if player_name == self.player1.name:
            player = self.player1
            symbol = 'X'
        else:
            player = self.player2
            symbol = 'O'

        return player, symbol


    def make_a_move(self, player_name):
        player, symbol = self.get_symbol(player_name)

        while True:
            try:
                cell = int(input(f'Ход игрока {player.name}. Введите номер свободной ячейки: '))
                if not self.board.is_cell_empty(cell):
                    raise ValueError
                if cell < 1 or cell > 9:
                    raise AttributeError
            except ValueError:
                print('Клетка занята. Выберете другую клетку.')
            except AttributeError:
                print('Номер клетки должен быть равен числу от 1 до 9.')
            else:
                self.board.change_the_cell(cell, symbol)
                player.cell.add(cell)
                break

        self.board.show_bord()
        print()








