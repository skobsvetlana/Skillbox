from typing import Callable
import functools


def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    '''Декоратор. Декорирует декораторы'''

    def wrapped(*args, **kwargs):
        @functools.wraps(func)
        def wrapper(func: Callable) -> Callable:
            print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
            result = func
            return result

        return wrapper

    return wrapped


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Callable:
    '''Декоратор.'''

    @functools.wraps(func)
    def wrapper(func: Callable, *args, **kwargs) -> Callable:
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
