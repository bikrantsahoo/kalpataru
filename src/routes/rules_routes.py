from flask import Blueprint, render_template, request, flash, redirect
from src.routes.forms.rule_form import RuleForm

from src.services.rule_services import RuleServices
from src.constants import constants

rule_bp = Blueprint("rules", __name__)


@rule_bp.route("/disable_multiple_rule", methods=["GET", "POST"])
def disable_multiple_rule():
    name = None
    form = RuleForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if request.method == "POST":
            rule_names = request.form.get("name")
            print(rule_names)
            if len(rule_names) <= constants.RULE_SIZE:
                flash("recheck the rule name", constants.WARNING)
                return redirect("/disable_multiple_rule")
            status = RuleServices.disable_multiple_rule(rule_names=rule_names)
            if status:
                flash(f"Deleted  {rule_names} successfully", constants.SUCCESS)
            else:
                flash(f"Failed to delete rule  {rule_names} ", constants.ERROR)
    return render_template('rules/disable_rules.html', name=name, form=form)
