from typing import Callable, Any
import functools
import time

def how_are_you(func: Callable, *args, **kwargs) -> Callable:
    """Декоратор, который перед выполнением декорируемой
    функции ждёт несколько секунд. """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('Ждем 3 секунды.')
        time.sleep(3)
        result = func(*args, **kwargs)

        return result

    return wrapped_func


@how_are_you
def test() -> None:
    '''Какая-то функция'''

    print('<Тут что-то происходит...>')


test()