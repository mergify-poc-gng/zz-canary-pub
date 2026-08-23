import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    # REMOTE source: HTTP request parameter -> shell command sink
    host = request.args.get("host")
    return subprocess.check_output("ping -c 1 " + host, shell=True)


@app.route("/calc")
def calc():
    # REMOTE source: HTTP request parameter -> eval sink
    expr = request.args.get("expr")
    return str(eval(expr))
