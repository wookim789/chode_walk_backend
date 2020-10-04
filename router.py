import flask
from CalculateService import CalculateService

app = flask.Flask (__name__)


@app.route('/')
def hello_wold():
    return 'hello world'

@app.route('/getScale/<key>')
def get_scale(key):
    cs = CalculateService()
    return flask.jsonify(cs.get_scale(key))

if __name__ == "__main__":
    app.run()