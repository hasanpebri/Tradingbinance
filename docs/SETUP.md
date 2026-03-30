# Setup Guide for Tradingbinance

## Prerequisites
- Ensure you have Git installed. You can download it from [git-scm.com](https://git-scm.com/downloads).
- Make sure Python is installed (preferably Python 3.7 or higher). Download from [python.org](https://www.python.org/downloads/).
- Install pip, the package installer for Python, which usually comes with Python.

## Cloning the Repository
1. Open your terminal/command prompt.
2. Clone the repository using Git:
   ```bash
   git clone https://github.com/hasanpebri/Tradingbinance.git
   ```
3. Navigate into the cloned repository:
   ```bash
   cd Tradingbinance
   ```

## Virtual Environment Setup
1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

## Dependency Installation
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Binance API Key Configuration
1. Create a Binance account at [binance.com](https://www.binance.com).
2. Once logged in, navigate to API Management.
3. Create a new API key and copy the key and secret to a secure location.

## Environment Variables Setup
1. Create a `.env` file in the root directory of the project.
2. Add your Binance API key and secret in the following format:
   ```env
   BINANCE_API_KEY=your_api_key_here
   BINANCE_API_SECRET=your_api_secret_here
   ```

## Local Testing
1. Run the application:
   ```bash
   python main.py
   ```
2. Check for any errors in the console.

## Ngrok Exposure
1. Download and install [ngrok](https://ngrok.com/download).
2. Expose your local server:
   ```bash
   ngrok http 5000
   ```
3. Note the forwarding URL provided by ngrok.

## TradingView Webhook Configuration
1. Go to your TradingView account.
2. Open the alerts panel and click on "Create alert."
3. In the alert settings, select "Webhook URL" and paste the ngrok forwarding URL.
4. Set the alert conditions according to your trading strategy.

## Webhook Testing
1. Trigger a test alert in TradingView to ensure everything is functioning.
2. Monitor the server console for incoming webhook requests.

## Production Deployment Options
- Consider using platforms like Heroku, AWS, or Azure to deploy your application in a production environment.
- Ensure that your environment variables are securely configured in the production environment.
- Setup monitoring for your application to track performance and errors.

---

### Last Updated: 2026-03-30 11:27:45 UTC
