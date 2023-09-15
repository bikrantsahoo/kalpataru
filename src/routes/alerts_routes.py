from flask import Blueprint, render_template, request, flash, redirect
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

# from src.services.alert_services import AlertServices

alert_bp = Blueprint("alerts", __name__)


# creating form class
# TODO: try to get good practice (adding separate class for forms )
class DeleteAlertForm(FlaskForm):
    name = StringField("Alert Name", render_kw={'placeholder': 'Enter alert name'}, validators=[DataRequired()])
    submit = SubmitField("submit")


@alert_bp.route("/active_alert")
def active_alert():
    return render_template('alerts/alerts.html')


@alert_bp.route("/delete_alert", methods=["GET", "POST"])
def delete_alert():
    name = None
    form = DeleteAlertForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    print(request)
    print(request.method)
    if request.method == "POST":
        req = request.form
        alert_name = req.get("name")
        print(alert_name)
        if len(alert_name) <= 5:
            flash("recheck the alert name", "warning")
            return redirect("/delete_alert")

        # alert_status = AlertServices().delete_alert(alert_name=alert_name)
        alert_status = "danger"
        if alert_status:
            # ToDo: flash may not work
            flash(f"Alert {alert_name} alert_status", alert_status)
        else:
            flash("Alert  ", alert_status)
    return render_template('alerts/delete.html', name=name, form=form)
