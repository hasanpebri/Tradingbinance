from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/tradingview-webhook', methods=['POST'])
def tradingview_webhook():
    data = request.json

    # Process the alert here
    print("Received alert:", data)

    # You can add your trading logic here
    # For example: if data['strategy']['order_action'] == 'buy', execute buy order

    return jsonify({'status': 'success', 'message': 'Alert received'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)