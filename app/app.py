# -*- coding: utf-8 -*-
from flask import Flask as fl
from http import HTTPStatus
import CalculateService
from flask_cors import CORS

app = fl.Flask (__name__)

# cors
CORS(app)

@app.route('/')
def hello_wold():
    return 'hello wookim'

@app.route('/getScale/<key>')
def get_scale(key):
    cs = CalculateService.CalculateService()

    response = None
    result = cs.get_scale(key)

    if result != False:
        response = fl.make_response(fl.jsonify(result), HTTPStatus.OK)
    else:
        response = fl.make_response(fl.jsonify(result), HTTPStatus.BAD_REQUEST)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')