from data_collection.data_collector import make_request
def get_mim_low_value(pair: str, number: int=1) -> float | None:
    """
    Функция вызывает функцию  data_collection.data_collector.make_request, которая
    возвращает данные запроса на Huobi в формате JSON.
    Возвращает минимальное значение среди всех по ключу 'low'.
    """

    data = make_request(pair, number)

    if data and data['status'] != 'error':
        low = min([el['low'] for el in data['data']])

        return low

    return None


