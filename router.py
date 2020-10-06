# -*- coding: utf-8 -*-
import flask
from http import HTTPStatus
import CalculateService

app = flask.Flask (__name__)


@app.route('/')
def hello_wold():
    return 'hello world'

@app.route('/getScale/<key>')
def get_scale(key):
    cs = CalculateService.CalculateService()

    response = None
    result = cs.get_scale(key)

    if result != False:
        response = flask.make_response(flask.jsonify(result), HTTPStatus.OK)
    else:
        response = flask.make_response(flask.jsonify(result), HTTPStatus.BAD_REQUEST)
    return response

if __name__ == "__main__":
    app.run()