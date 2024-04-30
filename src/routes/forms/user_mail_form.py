from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

def validate_email_domain(form, field):
    email_list = field.data.split(',')
    for email in email_list:
        if not email.strip().endswith('@ril.com'):
            raise ValidationError('Email is invalid')

class UserMailForm(FlaskForm):
    name = StringField("Enter Mail List", render_kw={'placeholder': "Enter comma separated mail id's without quotes"},
                       validators=[DataRequired(), validate_email_domain])
    submit = SubmitField("submit")
