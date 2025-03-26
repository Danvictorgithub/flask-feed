from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from api.db import db
from api.db.models import Post
from . import postBp


@postBp.route("/", methods=["GET"])
def index():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])


@postBp.route("/<int:post_id>", methods=["GET"])
def show(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(post.to_dict())


@postBp.route("/", methods=["POST"])
@jwt_required()
def create():
    current_user = get_jwt_identity()
    title = request.form.get("title")
    content = request.form.get("content")
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400

    new_post = Post(title=title, content=content, user_id=current_user)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201
