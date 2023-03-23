from typing import Callable, Any
import functools
import traceback
from datetime import datetime

def logging(func: Callable, *args, **kwargs) -> Callable:
    """Декоратор, который название функции и ее документацию.
     В случае ошибки во время выполнения декорируемой функции, в файл function_errors.log
     записываются название функции и ошибки. """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('Наименование функции: {func_name}'
              '\nДокументация: {docs}'.format(func_name=func.__name__, docs=func.__doc__))

        try:
            result = func(*args, **kwargs)
            print('*' * 100, '\n')

            return result
        except Exception:
            print('*' * 100, '\n')
            date = datetime.now()
            err = traceback.format_exc().split('\n')[-2]
            data = '{date}\t{func_name}\t{err}\n'.format(date=date,
                                                         func_name=func.__name__,
                                                         err = err
                                                         )

            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write(data)

    return wrapped_func


@logging
def test() -> None:
    '''Какая-то функция'''

    print('<Тут что-то происходит...>')


@logging
def say_hello(name: str) -> str:
    ''':return: строку "Hello, name" '''


    return 'Hello {name}'.format(name=name)


@logging
def say_goodbye(name: str) -> str:
    ''':return: строку "Goodbye, name" '''

    return 'Goodbye {name}'.format(name=name)


@logging
def cubes_sum(number: int) -> int:
    '''Функция нахождения суммы кубов для
    каждого N от 1 до 10000, где 0 <= N <= number

    :return: сумма кубов'''

    result = 0
    for _ in range(number + 1):
        result += sum([i ** 3 for i in range(10000)])

    return result


@logging
def sqared_sum() -> int:
    '''Функция нахождения суммы квадратов для
    каждого N от 1 до 10000, где 0 <= N <= 100

    :return: сумма квадратов'''

    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i ** 3 for i in range(10000)])

    return result


test()
say_hello()
say_goodbye('Tom')
cubes_sum('100')
sqared_sum()