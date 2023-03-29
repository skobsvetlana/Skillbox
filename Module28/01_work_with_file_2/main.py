import os
import functools
from typing import Callable, Any

class File:
    """Модернизированная версия контекст-менеджера File — теперь при попытке
    открыть несуществующий файл менеджер автоматически создаёт и открывает этот
    файл в режиме записи.
    """

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None


    def __enter__(self):
        if not os.path.exists(self.filename):
            self.file = open(self.filename, 'w')
            self.file.close()

        self.file = open(self.filename, self.mode)

        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

        return True



with File('example.txt', 'r') as file:
    file.read()

with File('example.txt', 'w') as file:
    file.write('Hello')





