from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from wtforms import StringField, SubmitField
from src.constants import constants


class GuestForm(FlaskForm):
    # def validate_inputs(form, field):
    #     if len(field.data.split(',')) > constants.MAX_JOB_ALLOWED:
    #         raise ValidationError(f"Exceeded the limit of {constants.MAX_JOB_ALLOWED}.")

    name = StringField("User mail id", render_kw={'placeholder': constants.DISPLAY_GUEST_USER_MSG},
                       validators=[DataRequired()])
    submit = SubmitField("submit")
