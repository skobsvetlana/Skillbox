import functools
from typing import Callable, Optional, Dict

app: Dict[str, Callable] = dict()

def callback(_func: Optional[Callable] = None, *, route: str = None) -> Callable:
    def decorator_callback(func: Callable) -> Callable:
        """ Декоратор функции обратного вызова """
        app[route] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            function_call = func(*args, **kwargs)
            return function_call

        return wrapper

    if _func is None:
        return decorator_callback
    return decorator_callback(_func)


@callback(route='//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
