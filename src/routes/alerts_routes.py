from flask import Blueprint, render_template, request, flash, redirect
from src.routes.forms.delete_form import DeleteAlertForm
from src.services.notitification_service import send_email

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
            alert_names = request.form.get("name")
            print(alert_names)
            # TODO: check and remove this condition check after few days
            if len(alert_names) <= constants.ALERT_SIZE:
                flash("recheck the alert name", constants.WARNING)
                return redirect("/delete_alert")
            alert_status = AlertServices.delete_alert(alert_names=alert_names)
            if alert_status:
                flash(f"Deleted {alert_names} successfully", constants.SUCCESS)
            else:
                flash(f"Failed to delete Alert {alert_names} ", constants.ERROR)
    return render_template('alerts/delete.html', name=name, form=form)
