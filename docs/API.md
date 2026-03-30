# API Documentation

## API Overview
This document provides details about the API used for interacting with the Trading Binance application.

### Base URL
The base URL for all endpoints is: `https://api.tradingbinance.com`

## Endpoints

### POST /tradingview-webhook
This endpoint is used to receive alerts from TradingView.

#### Request Body
The expected JSON format is:
```json
{
  "symbol": "BTCUSDT",
  "price": 50000,
  "action": "buy"
}
```

#### Example Usage
**cURL:**
```bash
curl -X POST https://api.tradingbinance.com/tradingview-webhook \
     -H 'Content-Type: application/json' \
     -d '{"symbol": "BTCUSDT", "price": 50000, "action": "buy"}'
```

**Python:**
```python
import requests

url = 'https://api.tradingbinance.com/tradingview-webhook'
payload = {"symbol": "BTCUSDT", "price": 50000, "action": "buy"}
response = requests.post(url, json=payload)
print(response.json())
```

#### Error Handling
- **400 Bad Request**: This indicates that the request was incorrectly formatted or missing required fields.
- **500 Internal Server Error**: This may occur if there is an issue on the server side. Please try again later.

### GET /status
This endpoint returns the current status of the API.

#### Example Usage
**cURL:**
```bash
curl -X GET https://api.tradingbinance.com/status
```

**Python:**
```python
import requests

url = 'https://api.tradingbinance.com/status'
response = requests.get(url)
print(response.json())
```

## Future Planned Endpoints
- **GET /trading-history**: Retrieve the trading history for a user.
- **POST /set-alerts**: Set price alerts for specific trading pairs.

## Conclusion
This API aims to provide robust functionality for trading automation and monitoring. Please refer to this documentation for any questions relating to its usage.