from flask import Flask, request, jsonify
from flask_wtf.csrf import CSRFProtect
import os
import logging
from logging.handlers import RotatingFileHandler
import openai
import requests

# Initialize the Flask application
app = Flask(__name__)

try:
    # Set the secret key from environment variables
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    
    # Initialize CSRF protection
    csrf = CSRFProtect(app)
    
    # Configure logging
    log_file_path = os.environ.get('LOG_FILE_PATH', 'app.log')
    handler = RotatingFileHandler(log_file_path, maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    
    # Configure OpenAI API key
    openai.api_key = os.environ['OPENAI_API_KEY']
    
    # Configure TradingView API credentials
    trading_view_api_key = os.environ['TRADING_VIEW_API_KEY']
    trading_view_api_url = os.environ['TRADING_VIEW_API_URL']
    
    app.logger.info('Flask application initialized successfully with CSRF protection, logging, OpenAI API, and TradingView API configured.')
    
except Exception as e:
    app.logger.error('Error during Flask application initialization: %s', str(e))
    raise

@app.route('/get_trade_signal', methods=['POST'])
def get_trade_signal():
    try:
        # Extract market data from the request
        market_data = request.json.get('market_data')
        
        # Generate trade signal using OpenAI GPT
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Generate a trading signal based on the following market data: {market_data}",
            max_tokens=50
        )
        
        trade_signal = response.choices[0].text.strip()
        
        # Prepare the trade order based on the trade signal
        trade_order = {
            "api_key": trading_view_api_key,
            "signal": trade_signal,
            "market_data": market_data
        }
        
        # Send trade order to TradingView's API
        trade_response = requests.post(trading_view_api_url, json=trade_order)
        
        if trade_response.status_code == 200:
            app.logger.info('Trade executed successfully: %s', trade_response.text)
            return jsonify({'message': 'Trade executed successfully', 'details': trade_response.text})
        else:
            app.logger.error('Failed to execute trade: %s', trade_response.text)
            return jsonify({'error': 'Failed to execute trade', 'details': trade_response.text}), trade_response.status_code
    
    except Exception as e:
        app.logger.error('Failed to generate trade signal or execute trade: %s', str(e))
        return jsonify({'error': 'Failed to generate trade signal or execute trade', 'details': str(e)}), 500

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Flask application!'})

if __name__ == '__main__':
    app.run(debug=True)