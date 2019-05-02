from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,SelectFiels,RadioField,SubmitField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import Divorce
from wtforms import ValidationError

