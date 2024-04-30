from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError, Length
from wtforms import StringField, SubmitField
from src.constants import constants


class PincodeForm(FlaskForm):
    def validate_pincode(form, field):
        if not field.data.isdigit():
            raise ValidationError('Pincode should be an integer or number.')

    # if len(pincode) != 6 or not pincode.isdigit():
    #     raise ValidationError("Pincode must be 6 digits and contain only integers.")

    name = StringField("Pincode", render_kw={'placeholder': "enter pincode"},
                       validators=[DataRequired(),
                                   Length(min=6, max=6,
                                          message="pincode should be in 6 digits")])

    submit = SubmitField("submit")
