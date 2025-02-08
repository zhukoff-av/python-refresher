import json
import requests
import time

url = "https://api.binance.com/api/v3/ticker/price"


def get_btc_price():
    """
    Fetches the current Bitcoin (BTC) price in USDT from Binance API.

    Returns:
        float: The current BTC price in USDT

    Example:
        >>> isinstance(get_btc_price(), float)
        True
    """
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    content = json.loads(response.content)
    return float(content["price"])


def get_btc_prices(ticker):
    btc_prices = []
    for i in range(10):
        response = requests.get(url, params={'symbol': ticker})
        content = json.loads(response.content)
        price = float(content["price"])
        time.sleep(1)
        btc_prices.append(price)
    print(min(btc_prices))
    print(max(btc_prices))


if __name__ == "__main__":
    get_btc_prices('BTCUSDT')
    get_btc_prices('ETHUSDT')
