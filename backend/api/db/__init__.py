# Define a custom DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Initialize SQLAlchemy at the module level
db = SQLAlchemy(model_class=Base)
