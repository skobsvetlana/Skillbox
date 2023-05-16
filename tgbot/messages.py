help_message = '''
Через этого бота можно посмотреть минимальное или максимальное значение стоимости 
выбранной криптовалюты на Huobi.
\nОтправь команду /currency, чтобы чтобы выбрать криптовалюту.
\nУзнать историю выполненных команду /history.
'''

start_message = 'Привет!\n' + help_message
last_day = '/last_day Посмотреть стоимость за предыдущий день'
custom = '''
/custom Посмотреть стоимость за выбранный диапазон в днях. 
Максимальное количество дней, за которое можно получить стоимость - 2000
'''

low = '/low - посмотреть минимальное значение.'
high = '/high - посмотреть максимальное значение.'
currency = '/currency - выбрать криптовалюту.'
history = '/history - узнать историю выполненных команду.'

MESSAGES = {
    'start': start_message,
    'help': help_message,
    'last_day': last_day,
    'custom': custom,
    'low': low,
    'high': high,
    'currency': currency,
    'history': history
}