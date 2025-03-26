from flask import Blueprint

postBp = Blueprint("posts", __name__)

from .post import index, show, create
