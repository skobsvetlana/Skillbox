from datetime import datetime

def log(message):
    '''
    Функция создает файл с названием <user_id>.log, если его не существует и
    добавляет в него записи с данными о пользователе (имя, фамилия, id, user_name),
    текущим временем и текстом сообщения введенного пользователем
    '''

    with open(f'tgbot/logs/{message.from_user.id}.log', 'a', encoding='utf-8') as f:
        print(f"{datetime.now()} Сообщение от {message.from_user.first_name} "
              f"{message.from_user.last_name} "
              f"(id={str(message.from_user.id)}, username={str(message.from_user.username)}) {message.text}",
              file=f)