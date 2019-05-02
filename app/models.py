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
    notices = db.relationship("Notice", backref= "user", lazy="dynamic")
    certificates = db.relationship("Certificate", backref= "user", lazy="dynamic")
    impediments = db.relationship("Impediment", backref= "user", lazy="dynamic")

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

class Notice(db.Model):
    __tablename__ = 'notices'

    id = db.Column(db.Integer, primary_key = True)
    district = db.Column(db.String(255))
    spouse = db.Column(db.String(255))
    g_name = db.Column(db.String(255))
    g_condition = db.Column(db.String(255))
    g_occupation = db.Column(db.String(255))
    g_age = db.Column(db.Integer)
    g_residence = db.Column(db.String(255))
    g_consent = db.Column(db.String(255))
    b_name = db.Column(db.String(255))
    b_condition = db.Column(db.String(255))
    b_occupation = db.Column(db.String(255))
    b_age = db.Column(db.Integer)
    b_residence = db.Column(db.String(255))
    b_consent = db.Column(db.String(255))
    dd = db.Column(db.Integer)
    mm = db.Column(db.String(255))
    yy = db.Column(db.Integer)
    signature = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Certificate(db.Model):
    __tablename__ = 'certificates'

    g_date = db.Column(db.Date())
    g_name = db.Column(db.String(255))
    g_condition = db.Column(db.String(255))
    g_occupation = db.Column(db.String(255))
    g_age = db.Column(db.Integer)
    g_residence = db.Column(db.String(255))
    g_fname = db.Column(db.String(255))
    g_foccupation = db.Column(db.String(255))
    b_date = db.Column(db.Date())
    b_name = db.Column(db.String(255))
    b_condition = db.Column(db.String(255))
    b_occupation = db.Column(db.String(255))
    b_age = db.Column(db.Integer)
    b_residence = db.Column(db.String(255))
    g_fname = db.Column(db.String(255))
    g_foccupation = db.Column(db.String(255))
    groom = db.Column(db.String(255))
    bride = db.Column(db.String(255))
    witness1 = db.Column(db.String(255))
    witness2 = db.Column(db.String(255))
    date = db.Column(db.Date())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Impediment(db.Model):
    __tablename__ = 'impediments'

    spouse = db.Column(db.String(255))
    at = db.Column(db.String(255))
    in_input = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    forename = db.Column(db.String(255))
    country = db.Column(db.String(255))
    date = db.Column(db.Date())
    father = db.Column(db.String(255))
    sex = db.Column(db.String(255))
    race = db.Column(db.String(255))
    religion = db.Column(db.String(255))
    residence = db.Column(db.String(255))
    condition = db.Column(db.String(255))
    occupation = db.Column(db.String(255))
    dd = db.Column(db.Integer)
    mm = db.Column(db.String(255))
    yy = db.Column(db.Integer)
    signature = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
