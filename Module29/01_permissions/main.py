import functools
from typing import Callable, Any


def check_permission(user: str, permission_list=None) -> Callable:
    if permission_list is None:
        permission_list = user_permissions

    def check_permission_dec(func: Callable) -> Callable:
        """Декоратор, проверяющий есть ли у ползователя право применять метод"""

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            if user in permission_list:
                result = func(*args, **kwargs)
            else:
                raise PermissionError('У пользователя {user} недостаточно прав, '
                                      'чтобы выполнить функцию {func_name}'.format(user=user,
                                                                                   func_name=func.__name__
                                                                                   ))

            return result

        return wrapped_func

    return check_permission_dec


user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
