from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    husband_name = db.Column(db.String(255))
    husband_email = db.Column(db.String(255), unique = True, index = True)
    husband_ID = db.Column(db.String(255), unique = True, index = True)
    wife_name = db.Column(db.String(255))
    wife_email = db.Column(db.String(255), unique = True, index = True)
    wife_ID = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    husband_pic_path = db.Column(db.String(255))
    wife_pic_path = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.husband_name} and {self.wife_name}'
