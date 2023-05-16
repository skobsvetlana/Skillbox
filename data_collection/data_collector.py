import requests
import json
import backoff

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=10,
                      raise_on_giveup=False)
def get_data(pair: str, number: int) -> json:
    path = 'https://api.huobi.pro/market/history/kline?' \
           'period=1day&size={num}&symbol={pair}'.format(num=number, pair=pair)
    response = requests.get(path).text

    return json.loads(response)


