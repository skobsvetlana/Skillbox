import random
class KillError(Exception):
    name = 'KillError'


class DrunkError(Exception):
    name = 'DrunkError'


class CarCrashError(Exception):
    name = 'CarCrashError'


class GluttonyError(Exception):
    name = 'GluttonyError'


class DepressionError(Exception):
    name = 'DepressionError'


class Life:
    __errors = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
    __day_count = 0

    def __init__(self):
        self.my_karma = 0


    def get_day_count(self):
        return self.__day_count


    def write_logs(self, data):
        with open('karma.log', 'a', encoding='utf-8') as file:
            file.write(data)


    def one_day(self):
        self.__day_count += 1
        try:
            n = random.randint(1, 10)
            if n == 10:
                raise random.choice(self.__errors)
            else:
                self.my_karma += random.randint(1, 7)
        except KillError as err:
            self.write_logs(f'День {self.__day_count}-ый {err.name}\n')
        except DrunkError as err:
            self.write_logs(f'День {self.__day_count}-ый {err.name}\n')
        except CarCrashError as err:
            self.write_logs(f'День {self.__day_count}-ый {err.name}\n')
        except GluttonyError as err:
            self.write_logs(f'День {self.__day_count}-ый {err.name}\n')
        except DepressionError as err:
            self.write_logs(f'День {self.__day_count}-ый {err.name}\n')


