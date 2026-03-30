import unittest
import requests

class TestWebhookValidation(unittest.TestCase):

    def test_valid_order(self):
        data = {'action': 'buy', 'quantity': 10, 'symbol': 'BTCUSDT'}
        response = requests.post('https://api.yourservice.com/webhook', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())

    def test_missing_fields(self):
        data = {'action': 'buy'}  # Missing 'quantity' and 'symbol'
        response = requests.post('https://api.yourservice.com/webhook', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_invalid_action(self):
        data = {'action': 'invalid_action', 'quantity': 10, 'symbol': 'BTCUSDT'}
        response = requests.post('https://api.yourservice.com/webhook', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_zero_negative_quantity(self):
        for quantity in [0, -10]:
            data = {'action': 'buy', 'quantity': quantity, 'symbol': 'BTCUSDT'}
            response = requests.post('https://api.yourservice.com/webhook', json=data)
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', response.json())

    def test_status_endpoint(self):
        response = requests.get('https://api.yourservice.com/status')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.json())

    def test_health_endpoint(self):
        response = requests.get('https://api.yourservice.com/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn('healthy', response.json())

    def test_balance_endpoint(self):
        response = requests.get('https://api.yourservice.com/balance')
        self.assertEqual(response.status_code, 200)
        self.assertIn('balance', response.json())

    def test_price_endpoint(self):
        response = requests.get('https://api.yourservice.com/price')
        self.assertEqual(response.status_code, 200)
        self.assertIn('price', response.json())

if __name__ == '__main__':
    unittest.main()