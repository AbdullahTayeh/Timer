from flask import Flask, jsonify, request
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/start_timer', methods=['POST'])
def start_timer():
    duration = request.json['duration']
    start_time = time.time()
    end_time = start_time + duration
    return jsonify({'end_time': end_time})

@app.route('/get_remaining_time', methods=['GET'])
def get_remaining_time():
    end_time = float(request.args.get('end_time'))
    current_time = time.time()
    remaining_time = max(0, end_time - current_time)
    return jsonify({'remaining_time': remaining_time})

if __name__ == '__main__':
    app.run(debug=True)
