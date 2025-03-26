from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return {"message": "Welcome to Flask-Feed API by dv8"}

    return app
