import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the main HTML page"""
    return render_template('index.html')

@app.route('/api/greet')
def greet():
    """API endpoint that returns JSON"""
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'success',
        'environment': os.environ.get('FLASK_ENV', 'production')
    })

if __name__ == '__main__':
    app.run(debug=True)