from flask import Flask
from flask import jsonify
from flask import Response

app = Flask(__name__)

@app.route('/hello', methods =['GET'])
def api_hello():

    data = {
        'hello' : 'world',
    }

    resp = jsonify(data)
    resp.status_code = 200
    return resp


