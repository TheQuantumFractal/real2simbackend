from flask import Flask, jsonify, request
import edge_lib
<<<<<<< HEAD
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
=======

app = Flask(__name__)
>>>>>>> 1eab7a5cc4dd315c81c875ab8573a5d83787cc76

@app.route('/users', methods=['GET'])
def index():
    users = edge_lib.get_users()
    return jsonify({
        'success': True,
        'users': users
    })

@app.route('/users/get', methods=['GET'])
def user_get():
    name = request.args['name']
    user = edge_lib.get_user(name) 
    return jsonify({
        'success': True,
        'user': user
    })

@app.route('/couples', methods=['GET'])
def couples():
    users = edge_lib.get_couples()
    return jsonify({
        'success': True,
<<<<<<< HEAD
        'users': users
    })

@app.route('/compatible', methods=['GET'])
def compatible():
    compatibles = edge_lib.get_compatible()
    return jsonify({
        'success': True,
        'compatibles': compatibles
    })


=======
        'couples': users
    })

>>>>>>> 1eab7a5cc4dd315c81c875ab8573a5d83787cc76
@app.route('/couples/get', methods=['GET'])
def couple_get():
    person1 = request.args['person1']
    person2 = request.args['person2']
    user = edge_lib.get_couple(person1, person2)
    return jsonify({
        'success': True,
        'users': user
    })