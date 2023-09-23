from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from wtforms import StringField, SubmitField
from src.constants import constants


class RuleForm(FlaskForm):
    def validate_rule_inputs(form, field):
        if len(field.data.split(',')) > constants.MAX_RULE_ALLOWED:
            raise ValidationError(f"Exceeded the limit of {constants.MAX_RULE_ALLOWED} rule names.")

    name = StringField("Rule Name", render_kw={'placeholder': 'Enter multiple Rule names in comma separated'},
                       validators=[DataRequired(), validate_rule_inputs])
    submit = SubmitField("submit")
