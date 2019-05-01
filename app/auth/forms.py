from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    husband_ID = StringField("Husband's ID",validators=[Required()])
    wife_ID = StringField("Wife's ID",validators=[Required()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember Us')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    husband_name = StringField("Husband's Full Name", validators = [Required()])
    husband_ID = StringField("Husband's ID",validators=[Required()])
    husband_email = StringField("Husband's Email Address", validators = [Required(), Email()])
    wife_name = StringField("Wife's Full Name", validators = [Required()])
    wife_ID = StringField("Wife's ID",validators=[Required()])
    wife_email = StringField("Wife's Email Address", validators = [Required(), Email()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Register')

    def validate_id(self, data_field):
        if User.query.filter_by(husband_email = data_field.data).first() or User.query.filter_by(wife_email = data_field.data).first():
            raise ValidationError('There is a couple owning one of those emails')

    def validate_username(self, data_field):
        if User.query.filter_by(husband_ID = data_field.data).first() or User.query.filter_by(wife_ID = data_field.data).first():
            raise ValidationError("One of the ID's is registered as married")
