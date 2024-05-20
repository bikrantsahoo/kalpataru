from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from wtforms import StringField, SubmitField
from src.constants import constants

class IPSearchForm(FlaskForm):
    def validate_ip_format(form, field):
        ip = field.data
        parts = ip.split('.')
        if len(parts) != 4:
            raise ValidationError('Invalid IP address format')

        for part in parts:
            try:
                if not 0 <= int(part) <= 255:
                    raise ValueError()
            except ValueError:
                raise ValidationError('Invalid IP address format')

    name = StringField("", render_kw={'placeholder': 'Enter Single IP to '},
                      validators=[DataRequired(), validate_ip_format])
    submit = SubmitField("Submit")
