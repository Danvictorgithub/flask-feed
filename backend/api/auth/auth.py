from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from api.db.models import User
from . import authBp
from ..db import db


@authBp.route("/me", methods=["GET"])
@jwt_required()
def me():
    current_user = get_jwt_identity()

    user = User.query.get(int(current_user))
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200


@authBp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    if not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid username or password"}), 401
    access_token = create_access_token(
        identity=str(user.id), additional_claims={"username": user.username}
    )
    return jsonify({"access_token": access_token})


@authBp.route("/sign_up", methods=["POST"])
def sign_up():
    # Validate if username and password exist in the form
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Check if the username already exists in the database
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error": "Username already exists"}), 409

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create a new user
    try:
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"id": new_user.id, "username": new_user.username}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500
