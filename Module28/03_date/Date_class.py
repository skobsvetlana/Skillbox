class Date:
    '''Класс для проверки числа даты на корректность;
    конвертации строки даты в объект класса Date, состоящий из
    соответствующих числовых значений дня, месяца и года.'''

    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return 'День: {d}    Месяц: {m}    Год: {y}'.format(d=self.day,
                                                            m=self.month,
                                                            y=self.year)

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        try:
            day, month, year = map(int, tuple(date.split('-')))
            return Date(day, month, year)
        except:
            print('Неверный формат даты')

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        date = tuple(date.split('-'))
        if len(date) != 3:
            return False

        day, month, year = map(int, date)

        if 1 < day <= 31:
            return False

        if 1 < month <= 12:
            return False

        return True
