from datetime import datetime

from app import db


class UserMixin:
    @classmethod
    def get_user_from_email(cls, email):
        try:
            return db.session.query(Users).filter(Users.email == email).one()
        except Exception as e:
            print(e)
            return None


class Users(UserMixin, db.Model):
    """
    Defines the attributes of users table in the database
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
