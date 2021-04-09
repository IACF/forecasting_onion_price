from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)


@app.route('/api/price', methods=['POST'])
def index():
    with open('price.json') as price_file:
        prices = json.load(price_file)

    return jsonify({
        'prices': prices
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
