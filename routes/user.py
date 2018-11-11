from bottle import Bottle, json_dumps

app = Bottle(__name__)


@app.get('/')
def index():
    return json_dumps({'msg': 'user handler'})