from flask import Blueprint, render_template, request, flash, redirect
from src.routes.forms.de_disable_form import DisableForm

from src.services.de_job_services import DeServices
from src.constants import constants

de_bp = Blueprint("de_jobs", __name__)


@de_bp.route("/manage_job", methods=["GET", "POST"])
def manage_job():
    name = None
    form = DisableForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if request.method == "POST":
            job_instance_id = request.form.get("name")
            toggle_switch = request.form.get("toggle_switch")
            print(toggle_switch)
            print(job_instance_id)
            # TODO: check and remove this condition check after few days
            # if len(job_instance_id) <= constants.ALERT_SIZE:
            #     flash("recheck the alert name", constants.WARNING)
            #     return redirect("/delete_alert")
            if toggle_switch == "on":
                status = DeServices.manage_job(job_instance_ids=job_instance_id, enable=True)
            else:
                status = DeServices.manage_job(job_instance_ids=job_instance_id, enable=False)

            if status:
                flash(f"Disable {job_instance_id} successfully", constants.SUCCESS)
            else:
                flash(f"Failed to disable job {job_instance_id} ", constants.ERROR)
    return render_template('de/disable.html', name=name, form=form)
