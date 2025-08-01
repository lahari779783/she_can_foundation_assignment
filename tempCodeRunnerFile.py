from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), 'frontend'),
    static_url_path=''
)

CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/login')
def serve_login():
    return send_from_directory(app.static_folder, 'login.html')

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/intern-data', methods=['GET'])
def get_intern_data():
    return jsonify({
        'name': 'Lahari',
        'referral_code': 'lahari2025',
        'donations': 1234
    })

if __name__ == '__main__':
    app.run(debug=True)
