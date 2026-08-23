import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    # REGRESSION: remote input flows straight into a shell
    host = request.args.get("host")
    return subprocess.check_output("ping -c 1 " + host, shell=True)


@app.route("/calc")
def calc():
    # REGRESSION: remote input flows into eval
    expr = request.args.get("expr")
    return str(eval(expr))
