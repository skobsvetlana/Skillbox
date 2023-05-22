from data_collection.data_collector import make_request

def get_max_high_value(pair: str, number: int = 1) -> float | None:
    """
    Функция вызывает функцию  data_collection.data_collector.make_request, которая
    возвращает данные запроса на Huobi в формате JSON.
    Возвращает максимальное значение среди всех по ключу 'high'.
    """

    data = make_request(pair, number)

    if data['status'] != 'error':
        high = max([el['high'] for el in data['data']])

        return high

    return None


