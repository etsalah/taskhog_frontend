from bottle import Bottle, static_file, template
from routes import user


app = Bottle(__name__)

ROUTES = [
    ('/user', user.app),
]

for route in ROUTES:
    app.mount(route[0], route[1])


@app.get('/')
def index():
    return template('dashboard')


@app.get('/<type_>/<file_path:path>')
def static_file_server(type_, file_path):
    return static_file(file_path, 'static/{0}'.format(type_))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
