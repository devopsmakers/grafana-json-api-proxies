from flask import Flask

app = Flask(__name__)

_SERVER_NAME = 'iCal SimpleJson Proxy'

@app.route("/")
def ok():
    return "OK"

@app.route("/query")
def query():
    return {}

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Headers'] = 'accept, content-type'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
