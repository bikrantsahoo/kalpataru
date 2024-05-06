from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError, Length, NumberRange
from wtforms import StringField, SubmitField
from src.constants import constants


class ModifyMobileNumber(FlaskForm):
    # def is_integer(self, field):
    #     if not field.data.isdigit():
    #         raise ValidationError('Customer Id must be an integer or number.')

    # name = StringField("Customer Id", render_kw={'placeholder': 'Enter customer id'},
    #                    validators=[DataRequired(),
    #                                is_integer])
    mobile_number = StringField("New Mobile Num", render_kw={'placeholder': 'Enter mobile number'},
                                validators=[DataRequired(),
                                            Length(min=10, max=10,
                                                   message="Mobile number must be exactly 10 numbers.")])
    submit = SubmitField("submit")
