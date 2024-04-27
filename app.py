from flask import Flask, jsonify, request
import edge_lib

app = Flask(__name__)

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
        'users': users
    })

@app.route('/couples/get', methods=['GET'])
def couple_get():
    person1 = request.args['person1']
    person2 = request.args['person2']
    user = edge_lib.get_couple(person1, person2)
    return jsonify({
        'success': True,
        'users': user
    })