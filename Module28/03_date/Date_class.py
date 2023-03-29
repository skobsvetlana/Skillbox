class Date:
    '''Класс для проверки числа даты на корректность;
    конвертации строки даты в объект класса Date, состоящий из
    соответствующих числовых значений дня, месяца и года.'''
    @classmethod
    def from_string(cls, date: str) -> object:
        try:
            day, month, year = tuple(date.split('-'))
            return 'День: {d}    Месяц: {m}    Год: {y}'.format(d=day,
                                                                m=month,
                                                                y=year)
        except:
            print('Неверный формат даты')


    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        date = tuple(date.split('-'))
        if len(date) != 3:
            return False

        day, month, year = date

        if int(day) < 1 or int(day) > 31:
            return False

        if int(month) < 1 or int(month) > 12:
            return False

        return True