import requests
import json
import backoff

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException,
                      max_tries=10,
                      raise_on_giveup=False)
def make_request(pair: str, number: int) -> json:
    """
    Функция отправляет запрос на Huobi с целью получения
    общедоступной рыночной информации, такой как количество свечей,
    глубина и торговая информация.
    Параметры запроса:
    period - период каждой свечи (1min, 5min, 15min, 30min, 60min,
    4hour, 1day, 1mon, 1week, 1year);
    size - количество возвращаемых данных (1 - 2000);
    symbol - торговый символ для запроса (поддерживаются все торговые
    символы, например, btcusd, bccbtcn (для получения свечей для ETP NAV,
    symbol = торговый символ ETP + суффикс 'nav', например: btc3lusdtnav))
    Функция возвращает данные в формате JSON.
    """

    path = 'https://api.huobi.pro/market/history/kline?' \
           'period=1day&size={num}&symbol={pair}'.format(num=number, pair=pair)
    response = requests.get(path).text

    return json.loads(response)


