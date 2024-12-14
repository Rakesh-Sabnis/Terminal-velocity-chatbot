from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/claude', methods=['POST'])
def claude_proxy():
    try:
        # Get the request data from the client
        data = request.json
        
        # Make the API call to Anthropic
        response = requests.post(
            'https://api.anthropic.com/v1/messages',
            headers={
                'Authorization': 'Bearer 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',  # Replace with your actual API key
                'Content-Type': 'application/json',
                'anthropic-version': '2023-06-01'
            },
            json=data
        )
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Return the response from Anthropic
        return jsonify(response.json())
    
    except requests.RequestException as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
