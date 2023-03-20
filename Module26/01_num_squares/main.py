from collections.abc import Iterable

# класс-итератор
class SquareNumbers:
    def __init__(self, num: int) -> None:
        self.num = num
        self.cur_val = 0


    def __iter__(self):
        return self


    def __next__(self) -> int:
        if self.cur_val < self.num:
            self.cur_val += 1
            return self.cur_val ** 2
        else:
            raise StopIteration


my_iter = SquareNumbers(num=3)
for i in my_iter:
    print(i, end=' ')

print('\n')


# функция-генератор
def square_numbers(num: int):
    for i in range(1, num + 1):
        yield i ** 2


my_gen = square_numbers(num=3)
for i in my_gen:
    print(i, end=' ')

print('\n')


# генераторное выражение

num = 4
[print(i ** 2, end=' ') for i in range(1, num)]