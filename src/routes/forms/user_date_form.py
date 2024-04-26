from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from wtforms.fields import DateField, BooleanField
from src.constants import constants


class UserDateForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d'
                          # , validators=[DataRequired()]
                          )
    enddate = DateField('End Date', format='%Y-%m-%d'
                        # , validators=[DataRequired()]
                        )
    include_all_dates = BooleanField('Include all dates')
    submit = SubmitField('submit')
    #include_all = BooleanField('Include All')
