from flask import Blueprint

authBp = Blueprint("auth", __name__)

from .auth import login, sign_up
