from typing import Callable, Any
import functools

def how_are_you(func: Callable, *args, **kwargs) -> Callable:
    """Декоратор, спрашивающий 'Как дела?' """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        ans = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)

        return result

    return wrapped_func


@how_are_you
def test() -> None:
    '''Какая-то функция'''

    print('<Тут что-то происходит...>')


test()
