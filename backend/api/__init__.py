import os
from flask import Flask
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)

    # Configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    # Disable deprecated feature
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    jwt = JWTManager(app)

    from .db import db

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Import models to ensure they are registered with SQLAlchemy
    from .db.models import User

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Define a simple route
    @app.route("/")
    def hello_world():
        return {"message": "Welcome to Flask-Feed API by dv8"}

    # Register blueprints
    from .auth import authBp
    from .posts import postBp

    app.register_blueprint(authBp, url_prefix="/auth")
    app.register_blueprint(postBp, url_prefix="/posts")

    return app
