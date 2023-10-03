from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from src.constants import constants


class DisableForm(FlaskForm):
    name = StringField("Disable Job", render_kw={'placeholder': constants.DISPLAY_DE_MSG},
                       validators=[DataRequired()])
    submit = SubmitField("submit")
