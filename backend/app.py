from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return {"message": "Flask Feed API by DV8"}
