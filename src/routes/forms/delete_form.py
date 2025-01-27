from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from wtforms import StringField, SubmitField
from src.constants import constants


class DeleteAlertForm(FlaskForm):
    # def validate_alert_inputs(form, field):
    #     alert_names = field.data.split(',')
    #     max_inputs = constants.MAX_ALERT_ALLOWED
    #
    #     if len(alert_names) > max_inputs:
    #         raise ValidationError(f"Exceeded the limit of {max_inputs} alert names.")
    #
    def validate_alert_inputs(form, field):
        if len(field.data.split(',')) > constants.MAX_ALERT_ALLOWED:
            raise ValidationError(f"Exceeded the limit of {constants.MAX_ALERT_ALLOWED} alert names.")

    name = StringField("Alert Name", render_kw={'placeholder': constants.DISPLAY_ALERT_MSG},
                       validators=[DataRequired(), validate_alert_inputs])
    submit = SubmitField("submit")
