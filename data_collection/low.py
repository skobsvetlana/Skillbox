from data_collection.data_collector import get_data
def low(pair: str, number: int=1) -> float | None:
    data = get_data(pair, number)

    if data and data['status'] != 'error':
        low = min([el['low'] for el in data['data']])

        return low

    return None


#print(low(pair='btcusdt'))