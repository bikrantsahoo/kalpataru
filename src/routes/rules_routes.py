from flask import Blueprint, jsonify, render_template, request
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField, SubmitField

rule_bp = Blueprint("rules", __name__)


# creating form class
class RuleForm(FlaskForm):
    name = StringField("Rule Name", render_kw={'placeholder': 'Enter multiple Rule names in comma separated'},
                       validators=[DataRequired()])
    submit = SubmitField("submit")


@rule_bp.route("/disable_multiple_rule", methods=["GET", "POST"])
def disable_multiple_rule():
    name = None
    form = RuleForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('rules/disable_rules.html', name=name, form=form)


# @rule_bp.route("/on_disable", methods=["POST"])
# def on_disable():
#     form = RuleForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         # Perform database operation using db_service
#         # result = db_service.execute_query("SELECT * FROM rules WHERE name = :name", name=name)
#         # Process the result or perform other actions
#         return 'Rules deleted successfully!'
#     return render_template('rules/on_disable.html')
