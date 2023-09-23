from flask import Blueprint, render_template, request, flash, redirect
from src.routes.forms.delete_form import DeleteAlertForm

from src.services.alert_services import AlertServices
from src.constants import constants

alert_bp = Blueprint("alerts", __name__)


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
        if request.method == "POST":
            alert_name = request.form.get("name")
            print(alert_name)
            # TODO: check and remove this condition check after few days
            if len(alert_name) <= constants.ALERT_SIZE:
                flash("recheck the alert name", constants.WARNING)
                return redirect("/delete_alert")
            alert_status = AlertServices.delete_alert(alert_name=alert_name)
            if alert_status:
                flash(f"Deleted {alert_name} successfully", constants.SUCCESS)
            else:
                flash(f"Failed to delete Alert {alert_name} ", constants.ERROR)
    return render_template('alerts/delete.html', name=name, form=form)