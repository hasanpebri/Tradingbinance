import os
from dotenv import load_dotenv
from tradingview_webhook import app as webhook_app
from binance_client import BinanceClient
import logging

# Load environment variables
load_dotenv()

# Initialize Binance Client with API credentials from .env file
binance_client = BinanceClient()  # Add appropriate arguments if needed

# Run Flask webhook server on port 5000
if __name__ == '__main__':
    webhook_app.run(port=5000)