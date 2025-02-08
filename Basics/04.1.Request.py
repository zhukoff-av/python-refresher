import asyncio
import aiohttp
import json
import time
import ssl
from datetime import datetime


async def get_price(session, ticker):
    """
    Asynchronously fetches the price for a given ticker

    Args:
        session: aiohttp ClientSession object
        ticker (str): Trading pair symbol (e.g., 'BTCUSDT')

    Returns:
        float: Current price for the trading pair
    """
    url = "https://api.binance.com/api/v3/ticker/price"
    # Creating SSL context that ignores certificate verification
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with session.get(url, params={'symbol': ticker}, ssl=ssl_context) as response:
        content = await response.text()
        data = json.loads(content)
        return float(data["price"])


async def monitor_prices(ticker, duration_seconds=60):
    """
    Monitors prices with maximum possible frequency for a given duration

    Args:
        ticker (str): Trading pair symbol (e.g., 'BTCUSDT')
        duration_seconds (int): Duration of monitoring in seconds
    """
    prices = []
    start_time = time.time()

    # Create a ClientSession with SSL configuration
    connector = aiohttp.TCPConnector(ssl=False)  # Disable SSL verification
    async with aiohttp.ClientSession(connector=connector) as session:
        while time.time() - start_time < duration_seconds:
            try:
                price = await get_price(session, ticker)
                timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                prices.append(price)
                print(f"{timestamp} - {ticker}: {price}")
            except Exception as e:
                print(f"Error: {e}")

            await asyncio.sleep(0.1)  # 100ms between requests

    # Output statistics
    if prices:  # Only if we have collected some prices
        print("\nStatistics:")
        print(f"Total requests: {len(prices)}")
        print(f"Min price: {min(prices)}")
        print(f"Max price: {max(prices)}")
        print(f"Average requests per second: {len(prices) / duration_seconds:.2f}")


# Start monitoring
if __name__ == "__main__":
    ticker = "BTCUSDT"
    asyncio.run(monitor_prices(ticker))
