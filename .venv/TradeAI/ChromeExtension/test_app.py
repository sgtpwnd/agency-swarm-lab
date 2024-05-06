import os
os.environ['SECRET_KEY'] = 'your_secret_key_here'
import unittest
from unittest.mock import patch
import json
from app import app

class TestTradeAIApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('openai.Completion.create')
    @patch('requests.post')
    def test_query_to_trade_execution(self, mock_trade, mock_openai):
        # Mocking OpenAI response
        mock_openai.return_value = {
            'choices': [{'text': 'buy'}]
        }
        
        # Mocking TradingView API response
        mock_trade.return_value.status_code = 200
        mock_trade.return_value.json.return_value = {"status": "success", "details": "Trade executed"}

        # Simulate POST request with user query
        response = self.app.post('/trade', data=json.dumps({'query': 'Should I buy AAPL stock today?'}),
                                 content_type='application/json')
        
        # Check if the response is successful
        self.assertEqual(response.status_code, 200)
        self.assertIn('Trade executed', response.get_data(as_text=True))

    def test_error_handling_invalid_input(self):
        # Test sending invalid input
        response = self.app.post('/trade', data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('No input provided', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()