#!/home/ryan/paper-router/venv/bin/python

from bottle import route, run, static_file

project_root = '/home/ryan/paper-router'

@route('/')
def any():
    return static_file('index.html', root=project_root)

@route('/<url:path>')
def any(url):
    return static_file('index.html', root=project_root)

run(host='0.0.0.0', port=8000, debug=True)
