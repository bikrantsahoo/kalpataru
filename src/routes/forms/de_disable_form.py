from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from wtforms import StringField, SubmitField
from src.constants import constants


class DisableForm(FlaskForm):
    def validate_inputs(form, field):
        if len(field.data.split(',')) > constants.MAX_JOB_ALLOWED:
            raise ValidationError(f"Exceeded the limit of {constants.MAX_JOB_ALLOWED}.")

    name = StringField("Job Id's", render_kw={'placeholder': constants.DISPLAY_DE_MSG},
                       validators=[DataRequired(), validate_inputs])
    submit = SubmitField("submit")
