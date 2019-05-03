from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,DateField,SelectField,SubmitField
from wtforms.validators import Required, Length, EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    husband_vows = TextAreaField("The Husband's vows", validators = [Required()])
    wife_vows = TextAreaField("The Wife's vows", validators = [Required()])
    dowry_agreement = TextAreaField("The Dowry agreement", validators = [Required()])
    other_agreements = TextAreaField("Any other agreements", validators = [Required()])

    submit = SubmitField('Submit')

class CivilMarriage(FlaskForm):
    husband_name = StringField("Groom Name", validators = [Required()])
    husband_id = StringField("Groom ID", validators = [Required()])
    husband_dob = DateField("Groom Date of Birth", validators = [Required()])
    husband_consent = SelectField('Do you consent to Marriage', choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], validators = [Required()])
    wife_name = StringField("Bride Name", validators = [Required()])
    wife_id = StringField("Bride ID", validators = [Required()])
    wife_dob = DateField("Bride Date of Birth", validators = [Required()])
    wife_consent = SelectField('Do you consent to Marriage', choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], validators = [Required()])
    witness1_name = StringField("First Witness Name", validators = [Required()])
    witness1_id = StringField("First Witness ID", validators = [Required()])
    witness1_dob = DateField("First Witness Date of Birth", validators = [Required()])
    witness2_name = StringField("Second Witness Name", validators = [Required()])
    witness2_id = StringField("Second Witness ID", validators = [Required()])
    witness2_dob = DateField("Second Witness Date of Birth", validators = [Required()])
    husband_signature = StringField("Groom Signature", validators = [Required()])
    wife_signature = StringField("Bride Signature", validators = [Required()])
    witness1_signature = StringField("First Witness Signature", validators = [Required()])
    witness2_signature = StringField("Second Witness Signature", validators = [Required()])
    registrar_signature = StringField("Registrar Signature", validators = [Required()])

    submit = SubmitField('Submit')
