# Импорты bootle
from bottle import run, request, route, view, HTTPError, static_file

# Данные хоста
HOST = 'localhost'
PORT = 8080


@route('/')
@view('index')
def index():
    pass

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/static/')

if __name__ == '__main__':
    run(host=HOST, port=PORT, reloader=True, debug=True)
