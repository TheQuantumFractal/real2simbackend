from flask import Flask
import edge_lib

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def hello():
    return edge_lib.get_users()
