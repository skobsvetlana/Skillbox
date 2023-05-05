import requests
import json

def get_data(number: int, pair: str) -> json:
    path = 'https://api.huobi.pro/market/history/kline?' \
           'period=1day&size={num}&symbol={pair}'.format(num=number,pair=pair)
    response = requests.get(path)

    return json.loads(response.text)

#print(get_data(2, 'btcusdt'))