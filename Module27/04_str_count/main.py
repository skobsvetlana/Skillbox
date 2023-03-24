class Decorator:
    def __init__(self, func):
        self._func = func
        self.count = 0


    def __call__(self, *args, **kwargs):
        self.count += 1
        result = self._func(*args, **kwargs)
        print('Функция {func_name} вызывалась {count} раз(а)\n'.format(func_name=self._func.__name__,
                                                                  count=self.count))

        return result


@Decorator
def test() -> None:
    '''Какая-то функция'''

    print('<Тут что-то происходит...>')



test()
test()
test()
