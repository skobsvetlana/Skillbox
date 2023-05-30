from pydantic import BaseSettings, SecretStr

class Settings(BaseSettings):
    '''
    Класс для хранения переменных окружения.
    '''

    bot_token: SecretStr

    class Config:
        '''
        Класс для хранения параметров переменных окружения.
        '''
        env_file = './.env'
        env_file_encoding = 'utf-8'


config = Settings()






