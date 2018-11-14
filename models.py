from flask_sqlalchemy import SQLAlchemy
from main import app


# Init the sqlalchemy object
db = SQLAlchemy(app)


class User(db.Model):
    """Represents Proected users."""

    __tablename__ = "users"
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


    def __repr__(self):
        """Define the string format for instance of User"""
        return "<Model User `{}`>".format(self.username)
