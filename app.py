from flask import Flask, jsonify
import edge_lib

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def index():
    users = edge_lib.get_users()
    return jsonify({
        'success': True,
        'users': users
    })
