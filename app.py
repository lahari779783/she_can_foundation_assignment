from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), 'frontend'),
    static_url_path=''
)

CORS(app)

# In-memory data storage
users = [
    {'name': 'Lahari', 'referral_code': 'lahari2025', 'donations': 1234}
]

leaderboard = [
    {"name": "Lahari", "donations": 5000},
    {"name": "Ravi", "donations": 3500},
    {"name": "Ananya", "donations": 2700},
    {"name": "Kabir", "donations": 2000},
    {"name": "Sneha", "donations": 1500}
]

# Serve login page
@app.route('/')
@app.route('/login')
def serve_login():
    return send_from_directory(app.static_folder, 'login.html')

# Serve dashboard page
@app.route('/dashboard')
def serve_dashboard():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# Get dummy intern data
@app.route('/api/intern-data', methods=['GET'])
def get_intern_data():
    return jsonify(users[0])

# Get leaderboard data
@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify(leaderboard)

# Add a new user (for testing)
@app.route('/api/add-user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    referral_code = data.get('referral_code')
    donations = data.get('donations', 0)

    if name and referral_code:
        new_user = {
            'name': name,
            'referral_code': referral_code,
            'donations': donations
        }
        users.append(new_user)
        return jsonify({'message': 'User added successfully', 'user': new_user}), 201
    else:
        return jsonify({'error': 'Missing name or referral_code'}), 400

# Main entry
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
