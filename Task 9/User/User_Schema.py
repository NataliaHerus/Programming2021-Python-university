from passlib.hash import pbkdf2_sha256 as sha256
from flask_login import UserMixin
from User.User import *
from app import *


class User(UserMixin, User, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    _email = db.Column(db.String(100), unique=False)
    password = db.Column(db.String(100))
    _first_name = db.Column(db.String(30))
    _last_name = db.Column(db.String(30))
    role = db.Column(db.String(5))

    def __init__(self, **d):
        super().__init__(**d)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(_email=email).first()

    @staticmethod
    def verify_hash(password, hash_):
        return sha256.verify(password, hash_)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email',
                  'first_name', 'last_name')
