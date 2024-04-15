from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from wtforms.fields import DateField
from src.constants import constants


class DateForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    enddate = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('submit')
