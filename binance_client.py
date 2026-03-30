# Binance Client

This file will handle the integration with the Binance API. It will contain functions for connecting to the API, retrieving market data, and executing trades.

## Installation

To use this client, you need to install the `python-binance` package:

```bash
pip install python-binance
```

## Example

```python
from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def get_symbol_price(self, symbol):
        return self.client.get_symbol_ticker(symbol=symbol)

# Initialize the client
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
binance_client = BinanceClient(api_key, api_secret)

# Get price for a symbol
print(binance_client.get_symbol_price('BTCUSDT'))
```