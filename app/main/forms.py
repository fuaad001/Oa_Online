from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required, Length, EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    husband_vows = TextAreaField("The Husband's vows", validators = [Required()])
    wife_vows = TextAreaField("The Wife's vows", validators = [Required()])
    dowry_agreement = TextAreaField("The Dowry agreement", validators = [Required()])
    other_agreements = TextAreaField("Any other agreements", validators = [Required()])

    submit = SubmitField('Submit')
