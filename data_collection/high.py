from data_collection.data_collector import get_data

def high(pair: str, number: int = 1) -> float | None:
    data = get_data(pair, number)

    if data['status'] != 'error':
        high = max([el['high'] for el in data['data']])

        return high

    return None


#print(high(pair='btcusdt'))
