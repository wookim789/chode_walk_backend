# -*- coding: utf-8 -*-
from flask.app import Flask
from flask import jsonify, make_response
from flask_cors import CORS
from http import HTTPStatus
import calculate_service as cls

app = Flask (__name__)

# cors
CORS(app)

@app.route('/')
def hello_wold():
    return 'hello wookim'

@app.route('/getScale/<key>')
def get_scale(key):
    cs = cls.CalculateService()

    response = None
    result = cs.get_scale(key)

    if result != False:
        response = make_response(jsonify(result), HTTPStatus.OK)
    else:
        response = make_response(jsonify(result), HTTPStatus.BAD_REQUEST)
    return response


