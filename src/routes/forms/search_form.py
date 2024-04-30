from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from wtforms import StringField, SubmitField
from src.constants import constants


class SearchForm(FlaskForm):
    name = StringField("User mail id", render_kw={'placeholder': 'Enter your Mail ID'}, validators=[DataRequired()])
    submit = SubmitField("Search")