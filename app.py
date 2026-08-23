import shlex
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    # safe: no shell, argument list is quoted
    return subprocess.check_output(["ping", "-c", "1", shlex.quote(host)])
